import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import faiss
from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration

# 1. Veri Hazırlığı ve Ön İşleme

# Log dosyasını okuma ve işleme
log_file_path = "sample_web_traffic.log"

with open(log_file_path, "r") as log_file:
    log_data = log_file.readlines()

log_pattern = re.compile(
    r'(?P<ip>\S+) - - \[(?P<timestamp>[^\]]+)\] "(?P<method>\S+) (?P<url>\S+) HTTP/1\.1" (?P<status>\d+) - "(?P<user_agent>[^"]+)"'
)

log_entries = []
for log_entry in log_data:
    match = log_pattern.match(log_entry)
    if match:
        log_entries.append(match.groupdict())

log_df = pd.DataFrame(log_entries)
log_df['timestamp'] = pd.to_datetime(log_df['timestamp'] + " +0000", format="%d/%b/%Y:%H:%M:%S %z")

# Verileri metin olarak birleştirip vektörleştirme
log_df['text'] = log_df['method'] + " " + log_df['url'] + " " + log_df['status'] + " " + log_df['user_agent']
vectorizer = TfidfVectorizer()
text_vectors = vectorizer.fit_transform(log_df['text']).toarray()

# FAISS ile vektör veri tabanı oluşturma
dimension = text_vectors.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(text_vectors)

# 2. RAG Modelinin Kurulumu ve Entegrasyonu

# Tokenizer ve modelin yüklenmesi
tokenizer = RagTokenizer.from_pretrained("facebook/rag-sequence-nq")
retriever = RagRetriever.from_pretrained("facebook/rag-sequence-nq", index_name="exact", use_dummy_dataset=True)
model = RagSequenceForGeneration.from_pretrained("facebook/rag-sequence-nq", retriever=retriever)

# FAISS ile vektör veri tabanını modelle entegre etme
retriever.index = index
model.retriever.index = retriever.index

# 3. Soru-Cevap Sistemi

def answer_question(question, model, tokenizer, vectorizer):
    # Sorgu vektörleştirme
    query_vector = vectorizer.transform([question]).toarray()
    D, I = index.search(query_vector, 5)
    
    # Bulunan log kayıtlarından yanıt oluşturma
    relevant_logs = log_df.iloc[I[0]]['text'].values.tolist()
    inputs = tokenizer(question, return_tensors="pt")
    inputs['context_input_ids'] = tokenizer(relevant_logs, return_tensors="pt", padding=True, truncation=True).input_ids.unsqueeze(0)
    generated = model.generate(**inputs)
    return tokenizer.batch_decode(generated, skip_special_tokens=True)[0]

# 4. Performans Değerlendirmesi ve Test

# Örnek sorgu
question = "Hangi sayfalar en sık ziyaret edildi?"
answer = answer_question(question, model, tokenizer, vectorizer)
print("Cevap:", answer)
