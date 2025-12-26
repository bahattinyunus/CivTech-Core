# �️ CivTech-Core

![CivTech-Core Banner](assets/civtech_core_banner.png)

> **"İnşaat Mühendisliğini Yapay Zeka ve Otomasyon ile Yeniden Keşfetmek"**
> *Reinventing Civil Engineering through Artificial Intelligence and Automation*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)](https://github.com/bahattinyunus/CivTech-Core)
[![Code Style](https://img.shields.io/badge/Code%20Style-Black-000000?style=for-the-badge)](https://github.com/psf/black)

**CivTech-Core**, geleneksel inşaat mühendisliği disiplinlerini modern bilgisayar bilimleri teknolojileriyle (**Yapay Zeka, Nesnelerin İnterneti, Büyük Veri Analitiği**) birleştiren, açık kaynaklı, yeni nesil bir mühendislik çekirdeğidir. Bu depo, betonarme yapıların statik hesaplamalarından şantiye yönetimindeki lojistik akışlara kadar her adımı dijitalleştirmeyi amaçlayan bir "İşletim Sistemi" vizyonu taşır.

Sadece bir kod kütüphanesi değil; mühendislerin "akıllı şehirler" ve "otonom yapılar" çağına geçişi için gerekli olan entelektüel ve teknik altyapıyı sunan yaşayan bir ekosistemdir. Geleceğin şehirlerini inşa etmek için gereken dijital tuğlaları burada kodluyoruz.

---

## 🎯 Misyon ve Vizyon: Mühendisliğin Yeni Çağı

### Statik Dünyadan Dinamik Evrene Geçiş
Geleneksel inşaat mühendisliği, yüzyıllardır büyük ölçüde deterministik hesaplamalara, statik güvenlik katsayılarına ve manuel iterasyonlara dayanmaktadır. Ancak içinde yaşadığımız modern dünya karmaşık, dinamik ve veri doludur. **CivTech-Core**, mühendisliği "yapı inşa etmekten" öteye taşıyarak, yapıları "yaşayan, veri üreten ve kararlar alabilen organizmalar" olarak ele alır. Amacımız, betonun fiziksel dayanıklılığını, kodun sonsuz esnekliği ile birleştirmektir.

### Veri Egemenliği (Data Sovereignty) ve Dijital İkizler
Vizyonumuz, fiziksel dünyadaki her bir kolonun, kirişin ve sensörün siber uzayda yaşayan, nefes alan birer dijital ikizini (Digital Twin) oluşturmaktır. Bu sayede, deprem anında saniyeler içinde hasar tespiti yapan algoritmalar, şantiyede malzeme israfını sıfıra indiren otonom botlar ve enerji verimliliğini maksimize eden adaptif cephe sistemleri birer hayal olmaktan çıkıp endüstri standardı haline gelecektir. Biz, inşaat sektörünün **"Dijital Rönesansı"**nı başlatıyoruz.

---

## 🛠️ Temel Modüller ve Teknik Derinlik

Bu repo, her biri spesifik bir mühendislik problemine odaklanan, modüler ve genişletilebilir bir mimari üzerine kurulmuştur. Her modül, kendi alanındaki en iyi teknolojileri (State-of-the-Art) kullanır.

### 1. 🧠 [AI-Structural-Analysis](./AI-Structural-Analysis) (Yapay Zeka Destekli Yapısal Analiz)

Bu modül, klasik sonlu elemanlar yöntemini (FEM) yapay zeka ile hibritleyerek benzeri görülmemiş bir hız ve optimizasyon sunar.
*   **Generative Design (Üretken Tasarım):** İnsan zihninin sınırlarını aşan tasarımlar için Genetik algoritmalar (Genetic Algorithms) ve topoloji optimizasyonu kullanır. Belirlenen yük koşulları, rüzgar hızı ve malzeme kısıtları altında, minimum malzeme ile maksimum dayanımı sağlayan geometriyi sistem otomatik olarak üretir. Mühendisin rolü "çizmek" değil, "sınır koşullarını belirlemek" haline gelir.
*   **Sismik Tahmin Modelleri (ML-Based Seismic Prediction):** Geçmiş elli yılın deprem verileri (Time-History Analysis) üzerinde eğitilmiş gelişmiş Derin Öğrenme (Deep Learning) modelleri (LSTM, Transformer), yapının lineer olmayan davranışlarını ve plastikleşme noktalarını milisaniyeler içinde tahmin eder. Bu, günler süren analiz sürelerini saniyelere indirger ve acil durum senaryoları için hayati önem taşır.

### 2. �️ [BIM-Automation](./BIM-Automation) (Yapı Bilgi Modellemesi Otomasyonu)

BIM süreçlerini manuel veri girişinin hantal yapısından kurtarıp, tam otomatik "Script-Based" bir iş akışına dönüştürür.
*   **Computational Geometry (Hesaplamalı Geometri):** Revit ve Rhino gibi endüstri standardı yazılımlar için geliştirilen karmaşık Python betikleri (Dynamo & Grasshopper entegrasyonu), parametrik tasarımların doğrudan BIM ortamına aktarılmasını sağlar. Karmaşık cephe sistemleri, amorf kabuk yapılar veya parametrik stadyum çatıları tek bir tıklama ile modellenebilir ve revize edilebilir.
*   **Auto-Schedule & 4D Planning:** Yapay zeka motorumuz, 3D model üzerinden anlık olarak metraj çıkarır (Quantity Take-off), maliyet analizi yapar ve şantiye iş programını (4D) optimize eder. Tedarik zinciri aksamalarını öngörerek "Just-in-Time" malzeme sevkiyatını yönetir, böylece stok maliyetlerini minimize eder.

### 3. 📡 [IoT-Structural-Health](./IoT-Structural-Health) (Yapısal Sağlık İzleme)

Binaların sinir sistemini oluşturarak onları "akıllı" varlıklara dönüştürür.
*   **Sensor Fusion (Sensör Füzyonu):** Binanın kritik noktalarına yerleştirilen ivmeölçerler, gerinim ölçerler (strain gauges) ve fiber optik sensörlerden gelen yüksek frekanslı ham veriyi Kalman Filtreleri ile işleyerek gürültüden arındırır ve anlamlı bilgiye dönüştürür.
*   **Real-Time Fatigue Analysis (Gerçek Zamanlı Yorulma Analizi):** Yapısal elemanlardaki mikro çatlakları, korozyonu ve malzeme yorulmasını sürekli izler. Kritik eşik değerleri aşıldığında (örneğin bir deprem sonrası artçı şokta veya aşırı rüzgar yüklemesinde), bina sakinlerine veya yetkililere otomatik uyarı gönderen "Erken Uyarı Sistemi"ni barındırır.

### 4. 🎓 [Education-Curriculum](./Education-Curriculum) (Yeni Nesil Müfredat)

Sadece bugünü değil, geleceği de inşa etmek için mühendislik eğitiminde radikal bir reform paketi sunar.
*   **First Principles Thinking:** Mühendislik problemlerini ezber formüllerle (Black Box) çözmeyi reddeder; bunun yerine fiziksel temel prensiplerden türeterek ve Python simülasyonları ile modelleyerek (White Box) öğretir.
*   **Interactive Notebooks:** Statik, Mukavemet, Akışkanlar Mekaniği ve Zemin Mekaniği gibi temel dersler için hazırlanmış, zenginleştirilmiş Jupyter Notebook'ları içerir. Öğrenciler diferansiyel denklemleri kağıt üzerinde değil, `SciPy` ve `NumPy` kütüphaneleri ile interaktif olarak çözer, sonuçları 3D olarak görselleştirir ve parametrelerle oynayarak fiziği hisseder.

---

## 🏛️ Sistem Mimarisi

CivTech-Core, ölçeklenebilir ve güvenli, katmanlı bir yazılım mimarisine sahiptir:

1.  **Veri Katmanı (Data Layer):** Sahadaki IoT sensörlerinden, meteoroloji istasyonlarından ve BIM modellerinden gelen heterojen verinin (CSV, JSON, SQL, Time-Series) toplandığı ve normalize edildiği katman.
2.  **İşleme Çekirdeği (Core Processing):** Python ekosisteminin gücünü arkasına alan (Pandas, TensorFlow, PyTorch, Scikit-learn) algoritmaların çalıştığı, ham verinin stratejik bilgiye dönüştüğü analiz merkezi.
3.  **Arayüz Katmanı (Interface Layer):** Mühendislerin sistemle etkileşime girdiği CLI (Command Line Interface), Web Dashboard'ları (React/Flask) veya BIM Eklentileri (Revit Add-ins).

---

## 🚀 Başlangıç Rehberi

Bu "Mühendislik Komuta Merkezi"ne katılmak ve kendi makinenizde çalıştırmak için aşağıdaki teknik adımları takip ediniz.

### Donanım ve Yazılım Gereksinimleri
*   **İşletim Sistemi:** Windows 10/11 (Endüstriyel BIM yazılımları ile tam uyumluluk için önerilir) veya Linux (Sunucu tarafı işlemler ve model eğitimi için).
*   **Python:** Sürüm 3.9 veya üzeri (Type hinting ve modern syntax desteği için).
*   **BIM Entegrasyonu:** Autodesk Revit 2023+ veya Rhino 7+ (Gerekli API lisanslarına sahip olmanız beklenir).
*   **Donanım:** Makine öğrenmesi modellerini eğitmek ve büyük veri setlerini işlemek için NVIDIA CUDA destekli bir ekran kartı (GPU) ve minimum 16GB RAM önerilir.

### Adım Adım Kurulum

1.  **Depoyu Klonlayın:**
    Terminalinizi açın ve en güncel çekirdek kodlarını yerel makinenize indirin.
    ```bash
    git clone https://github.com/bahattinyunus/CivTech-Core.git
    cd CivTech-Core
    ```

2.  **Sanal Ortam Oluşturun:**
    Proje bağımlılıklarının diğer projelerinizle çakışmasını önlemek için izole bir Python ortamı kurun.
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # Windows için
    # source venv/bin/activate  # Linux/Mac için
    ```

3.  **Bağımlılıkları Yükleyin:**
    Gerekli tüm bilimsel ve mühendislik kütüphanelerini (numpy, pandas, tensorflow, revitron, scipy vb.) tek komutla yükleyin.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Sistemi Test Edin:**
    Kurulumun başarısını doğrulamak ve sistemin sağlıklı çalıştığından emin olmak için birim testleri çalıştırın.
    ```bash
    python -m unittest discover tests
    ```

---

## � Karşılaştırmalı Mühendislik Tablosu

CivTech-Core yaklaşımının neden devrim niteliğinde olduğunu gösteren paradigmatik farklar:

| Özellik | Geleneksel Mühendislik Yaklaşımı | CivTech-Core (Dijital) Yaklaşımı |
| :--- | :--- | :--- |
| **Karar Mekanizması** | Tecrübeye dayalı sezgisel tahminler, manuel iterasyonlar ve "göz kararı" yaklaşımlar. | Büyük veri analitiği, istatistiksel modelleme ve yapay zeka destekli matematiksel optimizasyon. |
| **Güvenlik Anlayışı** | Bilinmezliği örtmek için yüksek güvenlik katsayıları ile aşırı boyutlandırma (Over-design). | Gerçek zamanlı sensör verisi ile yapının anlık sağlık durumunu izleme, proaktif bakım ve hassas mühendislik. |
| **Verimlilik** | Şantiye sahasında plansızlık ve hata kaynaklı %20-30'lara varan malzeme ve zaman israfı. | Generative Design ve 4D planlama ile %100 malzeme optimizasyonu, minimum atık (Zero-Waste) ve sürdürülebilirlik. |
| **Proje Süreci** | Birbirinden kopuk, haberleşmeyen disiplinler (Mimari, Statik, Mekanik) ve versiyon karmaşası. | Tek bir merkezi dijital model (BIM) üzerinde tam entegre, disiplinlerarası, eş zamanlı çalışma. |
| **Yapının Doğası** | İnşa edildiği gün ölmeye ve eskimeye başlayan, zamanla yorulan statik beton kütleleri. | Sensörlerle nefes alan, veri üreten, kendi durumunu raporlayan ve zamana adapte olan sibernetik yapılar. |

---

## 🤝 Katkıda Bulunma Protokolü

Bu proje, açık kaynak felsefesine sıkı sıkıya bağlıdır ve kolektif zeka ile güçlenir. Küresel mühendislik topluluğunun her türlü katkısına açıktır.

1.  **Fork & Branch:** Projeyi kendi hesabınıza fork'layın ve geliştireceğiniz özellik için `feature/YeniAlgoritma` isminde açıklayıcı bir dal (branch) açın.
2.  **Kod Standartları:** Yazdığınız Python kodlarının PEP 8 standartlarına uygun olduğundan, okunabilir olduğundan ve yeterli docstring (dokümantasyon) içerdiğinden emin olun.
3.  **Test:** Yazdığınız her yeni fonksiyon veya modül için kapsamlı birim testleri (Unit Test) eklemeyi unutmayın. "Test edilmemiş kod, bozuk koddur."
4.  **Pull Request:** Geliştirmenizi tamamladığınızda, yaptığınız değişiklikleri detaylıca anlatan bir Pull Request gönderin. Topluluk yöneticileri kodunuzu inceleyip ana çekirdeğe dahil edecektir.

---

## 📜 Yasal Uyarı ve Lisans

Bu proje, **MIT Lisansı** altında özgür yazılım olarak sunulmaktadır.
Kodların eğitim, araştırma ve kişisel gelişim amaçlı kullanımı tamamen serbesttir ve teşvik edilir. Ancak, gerçek dünya inşaat projelerinde (**özellikle can güvenliğini doğrudan ilgilendiren kritik statik hesaplamalarda**) kullanıldığında, tüm sorumluluk uygulayıcı mühendise aittir. Yazılım, yetkin bir mühendisin denetimi ve onayı olmaksızın nihai karar verici mekanizma olarak kullanılmamalıdır.

Detaylar ve lisans metninin tamamı için [LICENSE](./LICENSE) dosyasına bakınız.

---

<div align="center">

**CivTech-Core**
*Gelecek betonda değil, betonun içindeki veride saklıdır.*

[![Author](https://img.shields.io/badge/Author-Bahattin%20Yunus%20Çetin-lightgrey?style=flat-square)](https://github.com/bahattinyunus)
[![Location](https://img.shields.io/badge/Base-Trabzon%2C%20Turkey-red?style=flat-square)](https://maps.google.com)

</div>
