# Ada Modunda Mikroşebeke Optimizasyonu (GAMS – MILP)

Bu çalışma, ada modunda işletilen bir mikroşebekenin 24 saatlik operasyon planlamasının **Karma-Tamsayılı Doğrusal Programlama (MILP)** yöntemiyle modellenmesini içermektedir. Optimizasyon modeli GAMS ortamında CPLEX çözücüsü kullanılarak geliştirilmiştir. Her iki senaryonun sonuçları, Python ile üretilen grafiklerle birlikte depoda sunulmaktadır.

Modelde fotovoltaik üretim, rüzgâr türbini, dizel jeneratör ve batarya enerji depolama sistemi birlikte değerlendirilmiştir. Kritik, yarı kritik ve esnek yükler için ayrı besleme seviyeleri tanımlanmış olup, her üç yük grubu modelde **tam hizmet kısıtı** ile temsil edilmiştir.

---

## 1. Sistem Yapısı

Modelde kullanılan bileşenler:

* **Fotovoltaik (PV) üretim**
* **Rüzgâr türbini (WT) üretim**
* **Dizel jeneratör (DG)** ikili aç/kapa durumu ve minimum üretim sınırı
* **Batarya Enerji Depolama Sistemi (BESS)**
* **Kritik, yarı kritik ve esnek yük grupları**

Tüm üretim, depolama ve yük akışları saatlik çözünürlükte ele alınmıştır.

---

## 2. Depo Yapısı

```
├── gams/              
│   ├── scenario1.gms
│   └── scenario2.gms
│
├── data/              
│   └── README_DATA.md
│   
├── results/           
│   ├── scenario1_results.csv
│   ├── scenario2_results.csv
│   └── plots/
│       ├── s1_plot_*.png 
│       └── s2_plot_*.png  
│
├── scripts/
│   └── generate_plots.py
│
├── requirements.txt  
└── README_EN.md
└── README_TR.md
```

---

## 3. Senaryolar

### **Senaryo 1 – Deterministik durum**

PV ve WT kapasite değerleri sabit üretim profilleri üzerinden tanımlanmıştır.

### **Senaryo 2 – Gerçek Meteorolojik Veri**

PV ve WT kapasite limitleri, gerçek güneş radyasyonu ve rüzgâr hızı verileri üzerinden hesaplanmıştır.

Her iki senaryoda aynı karar değişkenleri, kısıtlar ve amaç fonksiyonu kullanılmaktadır. Veri kaynakları farklı olduğu için mutlak üretim seviyeleri değişmekle birlikte, operasyonel davranış ve kısıt etkileri açısından sonuçlar doğrudan karşılaştırılabilir niteliktedir.

---

## 4. Optimizasyon Modeli

### **Amaç Fonksiyonu**

Toplam işletme maliyetini en aza indirmek. Modele dahil edilen maliyetler:

* PV üretim maliyeti
* WT üretim maliyeti
* Batarya şarj/deşarj maliyeti
* DG yakıt maliyeti

Modelde yük kesilmediği için kesinti maliyeti bulunmamaktadır.

### **Temel Kısıtlar**

* Saatlik enerji dengesi
* PV ve WT kapasite sınırları
* DG maksimum/minimum güç sınırları
* DG ikili durum değişkeni
* BESS şarj/deşarj limitleri
* SOC aralığı (%20 – %90)
* Kritik, yarı kritik ve esnek yüklerin tam karşılanması

---

## 5. Çıktılar

Her senaryoya ait CSV dosyalarında şu değişkenler yer almaktadır:

* PV üretimi
* WT üretimi
* DG çıktısı ve çalışma durumu
* BESS şarj/deşarj değerleri
* SOC profili
* Kritik, yarı kritik ve esnek yüklerin karşılanma durumu
* Toplam arz ve enerji bileşenlerinin dağılımı
* DG kaynaklı karbon emisyonu

Bu değerler grafiklerde doğrudan kullanılmaktadır.

---

## 6. Grafikler

Her senaryoda 7 adet olmak üzere toplam 14 grafik bulunmaktadır:

 1. Batarya güç akışı
 2. Karbon emisyonu
 3. Enerji akışı ve kaynak dağılımı
 4. Yenilenebilir üretim profili
 5. Yük dağılımı
 6. SOC profili
 7. Toplam işletme maliyeti

---

## 7. Modelin Çalıştırılması

### **Gereksinimler**

* GAMS + CPLEX
* Python 

### **Adımlar**

1. İlgili senaryoyu çalıştırın:
`scenario1.gms` veya `scenario2.gms`
2. Çıktılar `results/` dizinine kaydedilir.
3. Grafik üretimi için:
```
pip install -r requirements.txt
python scripts/generate_plots.py
```

---

## 8. Lisans

Proje **MIT Lisansı** ile paylaşılmaktadır.

---

## 9. İletişim

Teknik değerlendirme, danışmanlık ve iş birliği talepleri için iletişime geçebilirsiniz.
