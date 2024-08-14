Web Trafik Loglarına Dayalı Yapay Zeka Destekli Soru-Cevap Sistemi Geliştirme

Teslim Tarihi: 22 Ağustos 2024  
Geliştirici: Aleyna Altunsu
Kod Repository: https://github.com/AleynaAltunsu/rag

1. Giriş

Bu projede, bir web sitesinin trafik loglarına dayanarak, kullanıcılardan gelen soruları cevaplayan bir soru-cevap (Q&A) sistemi geliştirilmiştir. Sistem, log dosyalarını analiz edip belirli sorulara yanıt verirken Retrieval-Augmented Generation (RAG) modelini kullanır. RAG modeli, bilgi alma ve jeneratif model bileşenlerini birleştirerek kullanıcı sorularına uygun ve anlamlı yanıtlar üretir.

2. Proje Adımları

Aşama 1: Veri Hazırlığı ve Ön İşleme
İlk aşamada, web trafik log dosyası okunmuş, analiz edilmiş ve işlenmiştir. Bu adımda, log dosyasındaki IP adresleri, zaman damgaları, erişilen sayfalar ve kullanıcı ajanı gibi bilgiler çıkarılmıştır. Bu veriler daha sonra metin formatına dönüştürülmüş ve metin verilerini sayısal verilere dönüştüren bir yöntemle vektörleştirilmiştir. Vektörleştirme, bu verileri makine öğrenimi algoritmalarıyla işlenebilir hale getirmiştir.

Aşama 2: RAG Modelinin Kurulumu
İkinci aşamada, Retrieval-Augmented Generation (RAG) modeli kurulmuş ve vektör veri tabanı ile entegre edilmiştir. Bu model iki ana bileşenden oluşur:
1. Bilgi Alma (Retrieval): Kullanıcının sorduğu soruya en uygun log kayıtlarını bulur.
2. Jeneratif Model (Generation): Bulunan log kayıtlarını kullanarak, dil modeli yardımıyla kullanıcı sorusuna uygun bir yanıt üretir.

FAISS (Facebook AI Similarity Search) adlı kütüphane, vektör veri tabanı oluşturmak için kullanılmış ve bu veri tabanı RAG modeli ile entegre edilmiştir.

Aşama 3: Soru-Cevap Sistemi

Bu aşamada, sistem kullanıcının sorusunu alır, vektör veri tabanında arama yaparak en uygun log kayıtlarını bulur ve dil modeli ile yanıt oluşturur. Örneğin, "Hangi sayfalar en sık ziyaret edildi?" gibi bir soruya sistem, ilgili log kayıtlarından yola çıkarak anlamlı bir cevap üretir.

Aşama 4: Performans Değerlendirmesi

Sistemin performansı çeşitli sorularla test edilmiştir. Yapılan testler sonucunda sistemin doğru ve anlamlı yanıtlar üretebildiği gözlemlenmiştir. Ancak, bazı durumlarda dil modelinin performansını artırmak için ek optimizasyonlar yapılabileceği tespit edilmiştir.

Öneriler:
- Vektör veri tabanı iyileştirmesi:Daha fazla ve daha çeşitli log verisi ile sistemin performansı artırılabilir.
- Dil modeli optimizasyonu:RAG modelinin daha büyük bir versiyonu veya başka bir jeneratif model kullanılarak daha kaliteli yanıtlar elde edilebilir.
- Sistem hızlandırması:FAISS indeksleme işlemi optimize edilerek arama süresi kısaltılabilir ve sistem performansı iyileştirilebilir.

3. Sonuç

Bu proje kapsamında geliştirilen RAG tabanlı soru-cevap sistemi, web trafik loglarına dayalı soruları başarılı bir şekilde cevaplayabilmiştir. Log verilerinin işlenmesi, RAG modelinin kurulumu ve entegrasyonu ve son olarak soru-cevap sisteminin çalışır hale getirilmesi adımları başarıyla tamamlanmıştır. Projenin bir sonraki aşamasında, sistemin performansını artırmak için ek iyileştirmeler yapılabilir.


