# Ada Modunda Mikro şebeke Optimizasyonu (GAMS – MILP)

Bu depo, ada modunda çalışan bir mikro şebeke için geliştirilmiş tam kapsamlı bir Karma-Tamsayılı Doğrusal Programlama (MILP) optimizasyon modelini içermektedir. Model GAMS ortamında CPLEX çözücüsü kullanılarak uygulanmış olup, tüm veri kümeleri, senaryo temelli sonuçlar ve görselleştirme çıktıları projeye dahildir.

Bu çalışma, yenilenebilir üretim, dizel jeneratör planlaması ve BESS enerji yönetimi dâhil olmak üzere mikro şebeke işletiminin şeffaf, tekrarlanabilir ve mühendislik odaklı bir çerçevede incelenmesini amaçlamaktadır.

---

## 1. Mikroşebeke Mimarisi

Model, 24 saatlik bir zaman diliminde tamamen ada modunda çalışan bir mikro şebekeyi kapsamaktadır ve şu bileşenlerden oluşur:

* **Fotovoltaik (PV) üretim**
* **Rüzgâr türbini (WT) üretim**
* **Dizel jeneratör (DG)** aç/kapa karar değişkenleri ile
* **Batarya Enerji Depolama Sistemi (BESS)**
* **Kritik, yarı kritik ve esnek yükler**

Yük önceliklendirme yapısı, kritik ve yarı kritik yüklerin her koşulda kesintisiz beslenmesini garanti eder.

---

## 2. Proje Yapısı

```
├── gams/              # GAMS optimizasyon modelleri
│   ├── scenario1.gms
│   └── scenario2.gms
│
├── data/              # Girdi veri setleri
│
├── results/           # Model çıktıları
│   ├── scenario1_results.csv
│   ├── scenario2_results.csv
│   └── plots/
│       ├── s1_plot_*.png  # 7 grafik (Senaryo 1)
│       └── s2_plot_*.png  # 7 grafik (Senaryo 2)
│
├── docs/              # Ek dokümantasyon
│   └── PROJECT_OVERVIEW.md
│
├── requirements.txt   # Görselleştirmeler için Python bağımlılıkları
└── README.md

```

---

## 3. Senaryolar

### **Senaryo 1 – Deterministik Temel Durum**

Sabit üretim ve yük profillerinin kullanıldığı referans senaryodur.

### **Senaryo 2 – Gerçek Meteorolojik Veri**

Güneş radyasyonu ve rüzgâr hızına ilişkin gerçek veri setleri kullanılarak yenilenebilir belirsizliğinin yansıtıldığı senaryodur.

Her iki senaryo da aynı model yapısını ve kısıtları korur; böylece doğrudan karşılaştırma mümkündür.

---

## 4. MILP Optimizasyon Modeli

Optimizasyon problemi, mikro şebekenin toplam işletme maliyetini minimize eder ve fiziksel/operasyonel kısıtlar altında çözülür.

### **Amaç Fonksiyonu**

Minimizasyon kapsamı:

* Dizel jeneratör yakıt maliyeti
* Başlatma/durdurma maliyetleri
* (Varsa) karşılanamayan esnek yük cezaları

### **Temel Kısıtlar**

* **Enerji dengesi:** Her saat için arz = talep
* **Yenilenebilir sınırları:** PV/WT üst limitleri
* **DG operasyonu:** ikili aç/kapa kararı, güç sınırları, başlatma koşulları
* **BESS modeli:** şarj/deşarj sınırları, şarj verimi, deşarj verimi
* **SOC limitleri:** 20% ≤ SOC ≤ 90%
* **Yük önceliği:** kritik ve yarı kritik yükler tam olarak karşılanmak zorundadır

Ayrıntılı açıklamalar **docs/PROJECT_OVERVIEW.md** dosyasında sunulmuştur.

---

## 5. Sonuçlar

Her senaryo için ana çıktılar aşağıdaki CSV dosyalarında sunulur:

* **scenario1_results.csv**
* **scenario2_results.csv**

Bu dosyalar saatlik olarak şu değişkenleri içerir:

* PV üretimi
* WT üretimi
* DG güç çıktısı
* BESS şarj/deşarj değerleri
* SOC (State of Charge)
* Karşılanan yük (kritik, yarı kritik, esnek)
* Toplam arz ve karşılanamayan yük

Bu veriler, ilgili grafiklerin oluşturulmasında doğrudan kullanılmıştır.

---

## 6. Görselleştirmeler (14 Grafik)

**plots/** dizininde toplam 14 grafik bulunmaktadır:

* **7 adet – Senaryo 1**
* **7 adet – Senaryo 2**

Her iki senaryoda da grafik adlandırma yapısı birebir aynıdır; bu sayede karşılıklı inceleme kolaylaşır.

### Her senaryoda yer alan grafikler:

1. Batarya Güç Profili
2. Emisyon Göstergeleri
3. Enerji Akış Diyagramı
4. Yenilenebilir Enerji Kullanımı
5. Yük Dağılımı (kritik / yarı kritik / esnek)
6. SOC (State of Charge) Profili
7. Toplam İşletme Maliyeti

---

## 7. Modelin Çalıştırılması

### **Gereksinimler**

* GAMS + CPLEX Çözücüsü
* Python (görseller için)

### **Adımlar**

1. GAMS’i açın.
2. `scenario1.gms` veya `scenario2.gms` dosyasını yükleyin.
3. **F9** ile çalıştırın.
4. Çıktılar otomatik olarak **results/** klasörüne yazılır.
5. Grafiklerin yeniden oluşturulması için:

```
pip install -r requirements.txt
```

---

## 8. Lisans

Bu proje **MIT Lisansı** altında dağıtılmaktadır.

---

## 9. İletişim

Her türlü soru veya iş birliği için:

* E-posta veya LinkedIn bilgisi burada belirtilebilir.

Bu çalışma, GAMS ve MILP tabanlı mikro şebeke optimizasyonuna yönelik akademik, araştırma ve mühendislik portföyü kullanımına uygun, kapsamlı bir örnek uygulama sunmaktadır.
