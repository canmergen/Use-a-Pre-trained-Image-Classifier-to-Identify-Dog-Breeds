---
title: \textcolor[HTML]{FF6200}{OSA Growth Intelligence Model}
subtitle: \textcolor[HTML]{FF6200}{Stratejik Detaylı Proje Özeti ve Yol Haritası}
fontsize: 11pt
geometry: "a4paper,portrait,left=2.5cm,right=2.5cm,top=2cm,bottom=2cm,headheight=1.0cm,headsep=0.5cm"
header-includes:
  - \usepackage{fancyhdr}
  - \usepackage{xcolor}
  - \usepackage{sectsty}
  - \usepackage{graphicx}
  - \usepackage{lastpage}
  - \usepackage{titling}
  - \usepackage{enumitem}
  - \setlist[itemize,1]{label=$\bullet$}
  - \setlist[itemize,2]{label=$\circ$}
  - \setlist[itemize,3]{label=$\diamond$}
  - \setlist[itemize,4]{label=$\cdot$}
  - \setlength{\droptitle}{-1.5cm}
  - \pretitle{\begin{center}\huge\bfseries}
  - \posttitle{\end{center}\vspace{-0.8cm}}
  - \predate{}
  - \postdate{}
  - \sectionfont{\color[HTML]{FF6200}}
  - \subsectionfont{\color[HTML]{FF6200}}
  - \subsubsectionfont{\color[HTML]{FF6200}}
  - \paragraphfont{\color[HTML]{FF6200}}
  - \pagestyle{fancy}
  - \fancyhead[L]{\includegraphics[height=0.6cm]{ing_logo_final.png}}
  - \fancyhead[R]{\textcolor{black}{Ocak 2026}}
  - \fancyfoot[L]{\textbf{OSA Growth Intelligence Model} $\cdot$ Yönetici Özeti}
  - \fancyfoot[C]{}
  - \fancyfoot[R]{\thepage\ / \pageref{LastPage}}
  - \renewcommand{\headrulewidth}{0.4pt}
  - \renewcommand{\footrulewidth}{0.4pt}
  - \fancypagestyle{plain}{\pagestyle{fancy}}
---

# 1. YÖNETİCİ ÖZETİ

Bu teknik doküman, OSA Growth Intelligence modellemesinin stratejik hedeflerini, teknik mimarisini, veri temellerini ve uygulama yol haritasını içeren tek ve nihai yönetici özetidir.

## 1.1. Proje Amacı ve Kapsamı

OSA Growth Intelligence (Pricing \& Saving) Modeli, bankanın 2026 yıl sonu hedefi olan 120 Milyar TL bakiye büyüklüğüne ulaşabilmesi için **optimal faiz oranını** matematiksel olarak belirleyen bir karar destek sistemidir. Projenin temel çıkış noktası, faiz kararlarını sezgisel yaklaşımdan veri odaklı bir yapıya taşımak ve periyodik karar döngülerinde (haftalık veya aylık) yöneticilere "Bu dönem faizi ne yapmalıyız?" sorusuna somut, sayısal cevaplar sunmaktır.

Model, sadece bir tahmin aracı değil, aynı zamanda piyasa koşullarına göre kendini uyarlayan dinamik bir optimizasyon sistemidir. Düzenli olarak güncellenen "Rolling Gap Analysis" mekanizması sayesinde, hedefin ne kadar gerisinde veya önünde olduğumuzu hesaplar ve buna göre **beş farklı senaryoda** aksiyon önerir: **Best Effort** (Kritik risk), **Trend Repair** (Yüksek risk), **Cost Efficiency** (Yönetilebilir bölge), **Margin Testing** (Konforlu bölge) ve **Growth/Upside** (Hedef fazlası). Gap analysis'in sıklığı (haftalık veya aylık), model retrain periyoduna bağlı olarak belirlenecektir.

## 1.2. İş Problemi ve Mevcut Durum

Turuncu Hesap faiz kararları, bugüne kadar ağırlıklı olarak sezgisel yaklaşım ve rakip takibi ile alınmıştır. Bu geleneksel yaklaşım, bankanın uzun vadeli hedeflerine ulaşmasında beş kritik risk oluşturmaktadır:

- \textcolor[HTML]{FF6200}{\textbf{Reaktif Karar Alma (Pazar Takipçiliği):}} Rakip faiz artırdığında "biz de artıralım" refleksi ile hareket edilmektedir. Bu durum, bankayı piyasada "oyun kurucu" değil "takipçi" konumuna düşürmektedir. İnisiyatifin kaybedilmesi, proaktif bilanço yönetimini imkansız kılmakta ve marka algısını zayıflatmaktadır. Rakip faiz artırdığında geç tepki verilmesi, müşteri kaybına neden olabilmektedir.
- \textcolor[HTML]{FF6200}{\textbf{Hedef Belirsizliği ve Sürpriz Riski:}} "120 Milyar TL'ye ulaşmak için bu hafta tam olarak ne yapmalıyız?" sorusunun sayısal bir cevabı yoktur. Kararlar iyi niyetli tahminlere dayansa da hedefin ne kadar gerisinde (Gap) veya önünde olunduğu matematiksel olarak belirsizdir. Bu durum, yıl sonunda "Hedef tutmadı" sürprizi ile karşılaşma olasılığını artırır.
- \textcolor[HTML]{FF6200}{\textbf{Maliyet Optimizasyonu Eksikliği (Para Masada Kalıyor):}} Hedefi tutturacak en düşük (optimal) faiz oranı bilinmediği için, yönetici "emin olmak" adına gereksiz yüksek faiz verme eğilimindedir. Örneğin, 46% faiz ile hedef tutabilecekken 47% faiz verilmesi, bankanın karlılığından (Spread) feragat etmesi ve paranın masada bırakılması yani yıllık gereksiz yere milyonlarca TL ekstra maliyet demektir. Faiz kararları "doğru" olabilir ama "optimal" değildir. Banka ya hedefi kaçırır ya da gereksiz maliyet yapar.
- \textcolor[HTML]{FF6200}{\textbf{Operasyonel Sürdürülebilirlik ve Kişi Bağımlılığı (Key Person Risk):}} Mevcut süreçler, büyük ölçüde manuel Excel tabloları ve belirli kişilerin uzmanlığına (Know-How) dayalıdır. Bu da kurumsal hafızanın oluşmasını engellemekte ve operasyonel hata riskini artırmaktadır. Karar verici uzmanın olmadığı durumlarda sürecin kalitesi ve hızı düşmektedir.
- \textcolor[HTML]{FF6200}{\textbf{Simülasyon ve Senaryo Eksikliği (Stress Testing):}} Yönetim, "Faizi 50% yaparsak ne olur?" veya "Dolar kuru 10% artarsa mevduat nasıl etkilenir?" gibi "What-If" sorularına mevcut yapıda yanıt alamamaktadır. Geçmiş veriye dayalı lineer projeksiyonlar, piyasa şoklarını veya radikal strateji değişikliklerinin etkisini simüle etmekte yetersiz kalmaktadır.

\newpage

## 1.3. Çözüm Mimarisi

Geliştirilen sistem, bu sorunları çözmek için **Tahmin -> Projeksiyon -> Optimizasyon** olmak üzere üç katmanlı bir mimari sunar:

\small

|     | Katman           |     | İşlev                                               |     | Amaç                                                   |
| --- | ---------------- | --- | --------------------------------------------------- | --- | ------------------------------------------------------ |
| 1.  | **Tahmin**       |     | Haftalık Net Akış (NET%) oranını tahmin eder.       |     | Modelin temel prensibidir, piyasa davranışını öngörür. |
| 2.  | **Projeksiyon**  |     | Tahmini TL Bakiyeye dönüştürerek yıl sonuna uzatır. |     | "Hedef tutuyor mu?" kontrolünü sağlar.                 |
| 3.  | **Optimizasyon** |     | Hedef farkına (Gap) göre**Optimal Faizi** önerir.   |     | En düşük maliyetle hedefe ulaşmayı sağlar.             |

\normalsize

Bu yapı sayesinde faiz kararları, "tahmin" olmaktan çıkıp, bankanın stratejik hedefine (120B TL) kilitlenmiş bir **"Hedef Yönetimi Aracı"**na dönüşür.

## 1.4. Geliştirilen Referans Modellerin Karşılaştırmalı Sonuç Analizi

Bu çalışma, Net Akış tahmininde kullanılan Legacy Base Model ile Updated Base Model yaklaşımlarının hem statik (tek seferlik eğitim) hem de dinamik (haftalık yeniden eğitim) senaryolar altında performanslarını karşılaştırmak amacıyla gerçekleştirilmiştir. Amaç; operasyonel karar destek süreçlerinde en yüksek tahmin doğruluğu, adaptasyon kabiliyeti ve model kalitesini sağlayan mimarinin belirlenmesidir. Baz referans modellerin detaylarına da 2. Teknik Mimari ve Model Metodolojisi kısmında yer verilmiştir.

### 1.4.1. Model Mimari Karşılaştırması

Aşağıdaki tablo, geliştirilen 4 farklı model mimarisinin temel yapısal özelliklerini özetlemektedir:

\small

| Model                      |     Eğitim      |               Feature Set                | Dinamiklik |  Uyum   |
| :------------------------- | :-------------: | :--------------------------------------: | :--------: | :-----: |
| **Legacy Base (Static)**   |  Tek seferlik   |            Makro Değişkenler             |    Yok     | Sınırlı |
| **Legacy Base (Dynamic)**  | Haftalık eğitim |            Makro Değişkenler             |    Yok     |  Orta   |
| **Updated Base (Static)**  |  Tek seferlik   | Makro Değişkenler + NET_lag1 + NET_roll3 | Kısmi Var  |  Orta   |
| **Updated Base (Dynamic)** | Haftalık eğitim | Makro Değişkenler + NET_lag1 + NET_roll3 |  **Var**   | **İyi** |

\normalsize

Model gelişimi, **İçerik** (Feature Set) ve **Çeviklik** (Dinamiklik) eksenlerinde birbirini tamamlayan stratejik hamlelerle ilerlemiştir. Bu evrim sürecinde elde edilen üç kritik stratejik bulgu şöyledir:

1. **Hız Tek Başına Yeterli Değildir (Agility Trap):** Mevcut Legacy yapının sadece eğitim sıklığını artırmak (Legacy Dynamic), modelin piyasa uyumunu sınırlı seviyeden orta seviyeye çekmiştir. Ancak model hala mikro-davranışsal sinyalleri (ürün bazlı hareketleri) göremediği için performans iyileşmesi belli bir noktada doygunluğa ulaşmıştır (Saturation).
2. **İçerik Kalitesi Kritiktir (Data Richness):** Modele eklenen momentum ve trend değişkenleri (Updated Static), yapısal olarak statik kalsa dahi formülün açıklama gücünü ($R^2$) tek başına ciddi oranda artırmıştır. Bu durum, doğru verinin en az doğru algoritma kadar hayati olduğunu kanıtlamıştır.
3. **Optimal Sinerji (Sustainability):** Hem zenginleştirilmiş veri setinin (Feature Set) hem de haftalık adaptasyon yeteneğinin (Dinamiklik) birleştirildiği **Updated Base (Dynamic)** mimarisi, sinerji etkisi yaratmıştır. Bu yapı, makro trendleri kaçırmadan anlık piyasa değişimlerine reaksiyon verebilen en **optimal ve sürdürülebilir çözüm** olarak öne çıkmıştır.

\newpage

### 1.4.2. Statik Model Performansı – Metrik Bazlı Karşılaştırma

Aşağıdaki grafik ve tablo, Statik senaryoda Legacy ve Updated modellerin kafa kafaya (head-to-head) performans farkını göstermektedir:

\begin{center}
\includegraphics[width=0.75\textwidth]{images/fig_head_to_head_static.png}
\end{center}

\small

| Metrik    |     | Legacy Static | Updated Static |   İyileşme   |
| :-------- | --- | :-----------: | :------------: | :----------: |
| **$R^2$** |     |    0.7092     |     0.8027     | **+ 0.0935** |
| **MAE**   |     |    0.7962     |     0.6834     | **- 14.2%**  |
| **RMSE**  |     |    0.9766     |     0.8102     | **- 17.0%**  |
| **AIC**   |     |     78.83     |     61.41      | **- 17.42**  |

\normalsize

Updated Base Model, mevcut güvenilir yapının üzerine inşa edilerek, yalnızca **Net Lag1** ve **Net Roll3** değişkenlerinin eklenmesiyle modelin açıklama gücünü önemli ölçüde yukarı taşımıştır. Bu sonuç, **formül gücünün (Pure Formula Power)** ve değişken seçimindeki isabetin bir göstergesidir. Böylece Updated Base Model (Static), referans alınan Legacy yapıya kıyasla daha hassas ve tutarlı bir tahmin performansı sergilemiştir.

### 1.4.3. Dinamik Model Performansı – Metrik Bazlı Karşılaştırma

Dinamik (haftalık yeniden eğitim) senaryoda, her iki modelin de adaptasyon hızı arttığında aradaki yapısal farkın etkisi aşağıdaki gibi ölçülmüştür:

\begin{center}
\includegraphics[width=0.75\textwidth]{images/fig_head_to_head_dynamic.png}
\end{center}

\small

| Metrik   | Legacy Dynamic | Updated Dynamic |  İyileşme   |
| :------- | :------------: | :-------------: | :---------: |
| **MAE**  |     0.6637     |     0.5258      | **- 20.8%** |
| **RMSE** |     0.8315     |     0.6485      | **- 22.0%** |

\normalsize

Dinamik senaryoda Updated Base Model, **haftalık yeniden eğitim** ile **kısa vadeli hafıza (Lag \& Trend)** özelliklerini birleştirerek piyasa değişimlerine karşı üstün bir adaptasyon yeteneği kazanmıştır. Sık eğitim ile kazanılan çeviklik, zenginleştirilmiş bilgi seti ile desteklendiğinde, modelin tahmin gücü ve ayrıştırma kabiliyeti (Separation Power) maksimize edilmiştir.

\newpage
\fancyfoot[L]{\textbf{OSA Growth Intelligence Model} $\cdot$ Teknik Mimari ve Model Metodolojisi}

# 2. TEKNİK MİMARİ VE MODEL METODOLOJİSİ

## 2.1. Proje Çıkış Noktası ve Evrimi

Projenin başlangıç aşamasında temel soru **"Faiz oranlarındaki değişimin mevduat hacmine etkisi nedir?"** şeklindeydi. Bu, klasik bir talep esnekliği (elasticity) tahmini yaklaşımıydı. Ancak Banka Yönetimi'nin 2026 yılı için koyduğu **120 Milyar TL**'lik net bakiye hedefi, projenin vizyonunu kökten değiştirmiştir.

Sadece "ne olacağını tahmin etmek" yerine, "istenen sonucun gerçekleşmesi için ne yapılması gerektiğini hesaplamak" (**Prescriptive Analytics**) öncelik haline gelmiştir. Bu doğrultuda model, pasif bir tahmin aracından, **Tersine Mühendislik (Reverse Engineering)** prensibiyle çalışan stratejik bir "Hedef Yönetim Sistemi"ne evrilmiştir. Bu sistem, girilen faize göre sonuç tahmini yapmak yerine, hedeflenen sonuca (120B TL) ulaşmak için gereken **optimal faizi** önermektedir.

## 2.2. Hedef Değişken Tanımı (Target Variable Definition)

Modelin tahmin hedefi olarak Toplam Bakiye (Balance) yerine **Haftalık Net Akış Oranı (Net Flow %)** seçilmiştir. Bunun stratejik ve teknik nedenleri şunlardır:

1. **Öncü Gösterge (Leading Indicator):** Bakiye, geçmiş faizlerin birikimli sonucudur (Lagging Indicator). Buna karşın **Net Akış**, müşterinin o haftaki faiz kararına verdiği _anlık ve doğrudan_ tepkidir. Piyasadaki trend dönüşleri, henüz toplam bakiyeye yansımadan önce akış verisinde kendini belli eder. Bu özellik, yönetime "erken uyarı sistemi" sağlar.
2. **Organik Büyüme Ayrıştırması:** Bankadaki toplam mevduat, faiz tahakkukları (Accrual) nedeniyle hiç yeni para girmese bile kendiliğinden büyür. Net Akış metriği ise bu yapay büyümeyi filtreler ve sadece **"Yeni Para Girişi" (Fresh Money)** ile **"Para Çıkışını" (Churn)** ölçer. Bankanın rakiplerinden ne kadar pazar payı kazandığı veya kaybettiği ancak bu saf metrik ile takip edilebilir.
3. **Mevsimsellik ve Konjonktürden Arındırma:** Net Akış oranı yüzdesel bir değer olduğu için, bakiyenin büyüklüğünden bağımsızdır (Scale Invariant). Bu sayede, bankanın portföyü 50 Milyar TL iken verdiği tepki ile 100 Milyar TL iken verdiği tepki, aynı matematiksel düzlemde modellenebilir. Bu normalizasyon, modelin tarihsel veriden daha sağlıklı öğrenmesini sağlar.

- **KPI Formülasyonu:** Mevcut Bakiye \* (1 + Tahmin Edilen Net Flow %) = Gelecek Hafta Bakiyesi.
- **Senaryo Analizi:** 100 Milyar TL Bakiye için:
  - **+ %0.5 Net Akış:** 100 \* (1 + 0.005) = **100.5 Milyar TL** (Organik Büyüme sağlandı).
  - **- %0.2 Net Akış:** 100 \* (1 - 0.002) = **99.8 Milyar TL** (Müşteri kaybı/Churn yaşandı).
  - _Bu haftalık hareketlerin kümülatif etkisi, sene sonu Hacim hedefini belirler._

## 2.3. Mevcut Durum: Proof of Concept Sonuçları

PoC (Proof of Concept) aşamasında, mevcut yetkinlikler ile hedeflenen yapay zeka mimarisi arasında yapılandırılmış bir benchmarking çalışması yürütülmüştür. Değerlendirme yalnızca tahmin doğruluğunu değil; **operasyonel uygulanabilirlik**, **açıklanabilirlik** ve **sürdürülebilirlik** kriterlerini de kapsayacak şekilde tasarlanmıştır.

Bu kapsamda iki ana model mimarisi, farklı zaman kurguları altında (Statik vs. Dinamik) karşılaştırılmıştır. Referans olarak bankada kullanılan ve olgunluğu kanıtlanmış **Legacy Base Model (Gretl/Excel)** alınmış; meydan okuyan alternatif olarak modern veri bilimi teknikleriyle geliştirilen **Updated Base Model (Python)** konumlandırılmıştır.

Modelin piyasa dinamiklerine uyum hızını ölçmek üzere **Yeniden Eğitim Sıklığı (Retraining Frequency)** kritik bir Ar-Ge başlığı olarak ele alınmıştır. Güncellenmeyen (statik), aylık güncellenen ve haftalık güncellenen senaryolar simüle edilerek “daha taze veri her zaman daha iyi sonuç üretir mi?” sorusu nicel olarak test edilmiştir.

## 2.4. Detaylı İstatistiksel Terimler Sözlüğü

Modelin doğruluk seviyesini, genelleme kapasitesini ve istikrarını çok boyutlu olarak analiz edebilmek için kapsamlı bir performans metrik seti kullanılmıştır. Bu metrikler, modelin sadece ne kadar iyi tahmin ettiğini değil, aynı zamanda hataların yapısını ve istatistiksel güvenilirliğini de ortaya koyar. Seçilen temel göstergeler ve analizdeki rolleri aşağıda özetlenmiştir:

\small

| Metrik Seti                                |           Anlamı / Amacı           |
| :----------------------------------------- | :--------------------------------: |
| **R² / Adjusted R²**                       |        Genel açıklayıcılık         |
| **F, Significance F, t, p-value**          |      İstatistiksel anlamlılık      |
| **MAE, RMSE**                              |         Tahmin hassasiyeti         |
| **Spearman, GAUC**                         | Göreli sıralama ve ayrıştırma gücü |
| **AIC, Condition Number, Overfitting Gap** |    Model kalitesi ve stabilite     |

\normalsize

Bu metrik seti bir bütün olarak değerlendirildiğinde, modelin performansı hakkında tamamlayıcı ve dengeli bir içgörü sağlar. Takip eden bölümlerde, her bir metriğin teknik tanımı ve model değerlendirmesindeki kritik önemi detaylandırılmıştır.

### 2.4.1. Regresyon İstatistikleri (Regression Statistics)

- **Multiple R (Çoklu Korelasyon Katsayısı):** Modelin ürettiği tahminler ile gerçek gözlemler arasındaki doğrusal ilişkinin gücünü gösterir. Değer yükseldikçe modelin tahminlerinin gerçek değerlerle birlikte hareket etme kabiliyeti artar. Yön bilgisi vermez, sadece ilişkinin gücünü ölçer.
- **R Square (R² – Belirlilik Katsayısı):** Bağımsız değişkenlerin, bağımlı değişkendeki toplam varyansın ne kadarını açıkladığını gösterir. Modelin açıklayıcılık seviyesinin temel ölçütüdür. Yüksek olması, modelin genel seviyeyi iyi yakaladığını ifade eder; ancak tek başına yeterli değildir.
- **Adjusted R Square (Düzeltilmiş R²):** R²’nin, değişken sayısını dikkate alan versiyonudur. Gereksiz veya zayıf değişken eklendiğinde cezalandırma yapar. Bu nedenle model karşılaştırmalarında R²’ye kıyasla daha güvenilir bir metriktir.
- **Standard Error (Standart Hata):** Model tahminlerinin, gerçek değerlerden ortalama ne kadar saptığını gösterir. Modelin tipik hata büyüklüğünü ifade eder. Daha düşük değer, daha isabetli tahminler anlamına gelir.
- **Observations (Gözlem Sayısı):** Modelin eğitildiği veri noktası sayısını ifade eder. İstatistiksel sonuçların güvenilirliği açısından önemlidir; küçük örneklemde yüksek performans aldatıcı olabilir.

### 2.4.2. ANOVA (Varyans Analizi) Metrikleri

- **df (Degrees of Freedom – Serbestlik Derecesi):** İstatistiksel hesaplamalarda kullanılan bağımsız bilgi miktarını ifade eder. Model ve hata bileşenleri için ayrı ayrı değerlendirilir.
- **SS (Sum of Squares – Kareler Toplamı):** Verideki toplam değişkenliğin ayrıştırılmasını sağlar.
  - Regression SS: Model tarafından açıklanan varyans.
  - Residual SS: Modelin açıklayamadığı, hata olarak kalan varyans.

- **MS (Mean Square – Ortalama Kareler):** Kareler toplamının serbestlik derecesine bölünmesiyle elde edilir. Varyansın normalize edilmiş bir ölçüsüdür ve F istatistiğinin hesaplanmasında kullanılır.
- **F Statistic (F İstatistiği):** Modelin bir bütün olarak istatistiksel olarak anlamlı olup olmadığını test eder. Modelin açıkladığı varyansın, açıklayamadığı varyansa oranını temsil eder. Yüksek olması, modelin rastgele bir yapıya sahip olmadığını gösterir.
- **Significance F:** F istatistiğine ait olasılık (p-değeri)'dir. Modelin açıklayıcılığının tamamen şans eseri olma ihtimalini ölçer. Düşük olması, modelin istatistiksel olarak anlamlı olduğunu gösterir.

### 2.4.3. Katsayılar Tablosu (Coefficients)

- **Intercept (Sabit Terim):** Tüm bağımsız değişkenler sıfır kabul edildiğinde, bağımlı değişkenin aldığı baz seviyedir. Modelin başlangıç noktasını tanımlar.
- **Coefficient (Katsayı):** İlgili bağımsız değişkenin bir birimlik değişiminin, bağımlı değişken üzerinde oluşturduğu etkiyi gösterir. İşaret yönü (pozitif/negatif), etkinin yönünü belirtir.
- **Standard Error (Katsayı Standart Hatası):** Katsayının tahminindeki belirsizlik seviyesini ölçer. Düşük olması, katsayının daha güvenilir tahmin edildiğini gösterir.
- **t Statistic (t Değeri):** Katsayının sıfırdan istatistiksel olarak anlamlı biçimde farklı olup olmadığını test eder. Katsayının, kendi standart hatasına oranıdır.
- **P-value:** İlgili değişkenin etkisinin tamamen rastgele oluşmuş olma olasılığıdır. Düşük olması, değişkenin modelde anlamlı bir açıklayıcı olduğunu gösterir.
- **Confidence Interval (Güven Aralığı):** Katsayının belirli bir güven düzeyinde hangi aralıkta yer alabileceğini gösterir. Aralığın sıfırı içermemesi, değişkenin anlamlılığına ek bir kanıttır.

### 2.4.4. Model Seçimi ve Stabilite Metrikleri

- **Overfitting Gap:** Eğitim ve test performansları arasındaki farkı ölçer. Düşük olması, modelin ezber yapmadığını ve genelleme kabiliyetinin iyi olduğunu gösterir.
- **AIC (Akaike Information Criterion):** Modelin uyum-karmaşıklık dengesini ölçer. Daha az parametreyle benzer açıklayıcılık sunan modelleri tercih eder. Model karşılaştırmalarında kullanılır.

### 2.4.5. Tahmin Hatası Metrikleri

- **MAE (Mean Absolute Error):** Tahmin hatalarının mutlak değerlerinin ortalamasını ölçer. Modelin tipik hata büyüklüğünü sade ve yorumlanabilir biçimde ifade eder.
- **RMSE (Root Mean Squared Error):** Hataların karelerinin ortalamasının kareköküdür. Büyük hataları daha fazla cezalandırır; uç sapmalara daha duyarlıdır.

### 2.4.6. Sıralama ve Ayırt Etme Metrikleri

- **Spearman Rank Correlation:** Modelin, gözlemleri doğru sıralama kabiliyetini ölçer. Mutlak seviyeden ziyade göreli karşılaştırmaların önemli olduğu durumlar için kritiktir.
- **GAUC (Grouped AUC / Global AUC):** Modelin farklı dönemleri veya grupları birbirinden ayırt etme gücünü ölçer. Genel seviye açıklayıcılığı yüksek olsa bile, dönemsel ayrıştırma zayıf olabilir; bu metriğin amacı bu farkı yakalamaktır.

## 2.5. Legacy Base Model (Statik Yaklaşım – Referans Başlangıç Noktası)

İlk aşamada, üst yönetim tarafından geliştirilen ve bugüne kadar başarıyla kullanılan Excel/Gretl tabanlı modelin mantığı Python ortamına taşınmıştır. Bu model, makroekonomik dinamikleri (Faiz, Kur, Mevsimsellik) doğru tespit ederek **güçlü bir "Baseline" (Referans Noktası)** oluşturmuştur. Amacımız, bu sağlam temeli koruyarak, modelin piyasa değişimlerine karşı çevikliğini artırmaktır.

\small

| Feature               | Coefficients |  Etki   |                        Business Açıklama                         |
| :-------------------- | :----------: | :-----: | :--------------------------------------------------------------: |
| **Intercept**         |   - 0.8236   | Negatif |                Modelin baz (başlangıç) seviyesi.                 |
| **w/TLREF**           |   + 0.4166   | Pozitif |      Haftalık TL fonlama maliyeti (Genel faiz göstergesi).       |
| **PPK**               |   - 0.4017   | Negatif |                 PPK faiz kararı haftası (Dummy).                 |
| **YearEnd**           |   - 0.8368   | Negatif |          Yıl sonu / bilanço kapama etkisi (Takvimsel).           |
| **EXP(CB avg-TLREF)** |   - 0.4334   | Negatif | CB fonlama maliyeti ile piyasa faizi farkının non-lineer etkisi. |
| **Market anomaly**    |   + 2.1370   | Pozitif |          Olağandışı piyasa koşulları / finansal şoklar.          |

\normalsize

\newpage

Legacy Base Model'e ait excel formülü aşağıda verilmiştir:

$$
\begin{aligned}
Net_{t+1} = &-0.8236 + 0.4166 \cdot \text{w/TLREF}_t - 0.4017 \cdot PPK_t - 0.8368 \cdot YearEnd_t \\
&- 0.4334 \cdot \exp(\text{CBavg}_t - TLREF_t) + 2.1370 \cdot MarketAnomaly_t
\end{aligned}
$$

Legacy Base Model, Net Akış'ı tahmin etmek amacıyla temel makroekonomik göstergeler kullanılarak oluşturulmuş, tek seferlik (static) eğitim yaklaşımına sahip bir regresyon modelidir.

- **Yüksek Genel Açıklayıcılık:** $R^2 = 0.7092$, Adjusted $R^2 = 0.6789$ ve Multiple R = 0.8422 değerleri, mevcut değişken setinin Net Akış üzerindeki ana trendleri **başarıyla yakaladığını** kanıtlamaktadır. Yönetimin belirlediği değişkenler matematiksel olarak doğrulanmıştır. **Overfitting Gap = 0.0303** ile düşük seviyededir.
- **Güçlü Sıralama Yeteneği:** Spearman Rank Corr = 0.8149 seviyesi, modelin "Hangi hafta daha yüksek giriş olur?" sorusuna doğru yanıt verdiğini gösterir. AIC = 78.8264 ile makul bir uyum-karmaşıklık dengesi sunarken, **Condition Number = 22.6786** seviyesi kabul edilebilir düzeydedir.
- **Tahmin İstikrarı:** Test setinde MAE = 0.7962 ve RMSE = 0.9766 değerleri, modelin genel seviye tahminlerinde tutarlı ancak sınırlı hassasiyete sahip olduğunu göstermektedir.
- **Gelişim Alanı (Time-Sensitivity):** GAUC = 0.5383 değeri, modelin genel yönü bilse de, piyasa rejimindeki (Dönemsel) kırılımları ayrıştırmakta zorlanabildiğini işaret etmektedir. Bu durum, modelin hatalı olmasından değil, **yapısı gereği "Statik" olmasından** kaynaklanmaktadır. Validasyon kriterlerine göre (Yeşil: >65%, Sarı: 60-65%, Kırmızı: <60%) bu alan, dinamik modellemenin katacağı en büyük katma değer noktasıdır.

Geçmiş verilerle oluşturulan bu sağlam yapının üzerine, piyasa adaptasyonunu eklemek projenin bir sonraki doğal adımı olmuştur.

\begin{center}
\includegraphics[width=0.85\textwidth]{images/fig_a1.png}
\end{center}

\vspace{0.1cm}

\begin{center}
\includegraphics[width=0.85\textwidth]{images/resid_base_model_static.png}
\end{center}

\newpage

**Sonuç:** Legacy Base Model, değişken seçimi ve kurgusuyla doğru bir temel atmıştır; referans ve karşılaştırma modeli olarak anlamlı olmakla birlikte, operasyonel karar destek süreçleri için tek başına yeterli değildir. Legacy Base Model özelinde statik olarak tasarlanmış modelin üzerine, dinamik olarak haftalık eğitime gidilmiş olsaydı sonuçlar nasıl gelirdi? Sorusuna cevap vermek adına aynı featurelar kullanılarak haftalık model retraini de denenmiştir.

## 2.6. Legacy Base Model (Dinamik Yaklaşım – Haftalık Yeniden Eğitim)

Mevcut modelin **güçlü temelini**, değişen piyasa koşullarına daha hızlı adapte etmek ve "Maksimum Verim" ilkesini test etmek amacıyla **dinamik bir yeniden eğitim ("Dynamic Retraining")** simülasyonu gerçekleştirilmiştir. Bu kurguda model yapısı değiştirilmeden, sadece öğrenme yöntemi haftalık güncellenen verilerle (Recursive Walk-Forward Validation) beslenerek, modelin reaksiyon hızı ölçümlenmiştir.

**Çeviklik Testi ve Performans Artışı:**
Statik yapıdan dinamik yapıya geçiş, beklendiği gibi modelin performansında **anında ve belirgin bir iyileşme** sağlamıştır.

- **Doğruluk Artışı:** **MAE (0.6637)** ve **RMSE (0.8315)** seviyelerine inilerek, statik yapıya göre yaklaşık **%16.6'lık bir performans kazanımı** elde edilmiştir.
- **Adaptasyon Yeteneği:** Aşağıdaki görselde de görüldüğü üzere, model piyasa dalgalanmalarına (Volatilite) çok daha hızlı tepki vermeye başlamış ve trend takibini sıkılaştırmıştır.

\begin{center}
\includegraphics[width=0.85\textwidth]{images/fig_a2.png}
\end{center}

**Stratejik Öğrenim ve "Updated Model" İhtiyacı:**
Bu çalışma, "Sık Güncelleme"nin (Agility) değerini kanıtlamış, ancak tek başına yeterli olmadığını da göstermiştir. Elde edilen %16.6'lık artış, mevcut değişken setinin (Makro Veriler) sınırlarına dayandığımızı ("Saturation Point") işaret etmiştir.

- **Tespit:** Model ne kadar sık eğitilirse eğitilsin, sadece _makroekonomik_ verilerle beslendiğinde, piyasadaki _davranışsal_ ve _mikro_ değişimleri (Banka içi ürün hareketleri, kampanya etkileri vb.) yakalamakta zorlanmaktadır.
- **Karar:** Bu bulgu, projenin yönünü **"Sadece Modeli Hızlandırma"**dan **"Bilgi Setini Genişletme"** stratejisine çevirmiştir.

**Sonuç:** Dinamik simülasyon, projenin **"Proof of Concept"** aşamasını başarıyla tamamlamış ve Updated Base Model'e geçiş için gerekli sayısal kanıtı sunmuştur. Artık hedef; bu hızlı öğrenen yapıyı, daha zengin bir veri setiyle (Feature Engineering) besleyerek **Updated Base Model** mimarisini kurmaktır.

\newpage

## 2.7. Updated Base Model (Statik Yaklaşım – Formül İyileştirmesi)

Updated Base Model, Legacy Base Model'de kullanılan 5 temel makroekonomik değişkeni birebir kullanıp, üzerine **2 adet davranışsal değişken** daha eklenerek oluşturulmuştur.

- **NET_lag1 (Momentum):** Bir önceki haftanın akış performansı. Geçen hafta giriş olduysa bu hafta da olma eğilimini ölçer.
- **NET_roll3 (Trend Düzeltme / Mean Reversion):** Son 3 haftanın hareketli ortalaması. Trendin aşırıya kaçıp kaçmadığını dengeler.

Bu modelin amacı; eklenen bu iki değişkenin model performansına (özellikle ayrıştırma gücüne) etkisini ölçmek ve Challenger (Nihai) Model geliştirilene kadar operasyonel süreçlerde "geçici ana model" (Interim Champion) olarak kullanılabilirliğini test etmektir.

\small

| Feature               | Coefficients | Etki    | Business Açıklama                                         |
| :-------------------- | :----------- | :------ | :-------------------------------------------------------- |
| **Intercept**         | - 0.6891     | Negatif | Modelin baz (başlangıç) seviyesi.                         |
| **w/TLREF**           | + 0.3507     | Pozitif | Piyasadaki haftalık TL fonlama maliyeti.                  |
| **PPK**               | - 0.2722     | Negatif | PPK faiz kararı haftası (Dummy).                          |
| **YearEnd**           | - 0.7448     | Negatif | Yıl sonu / bilanço kapama etkisi.                         |
| **EXP(CB avg-TLREF)** | - 0.3464     | Negatif | CB fonlama maliyeti farkı (Non-lineer).                   |
| **Market anomaly**    | + 1.7151     | Pozitif | Olağandışı piyasa koşulları.                              |
| **NET_lag1**          | + 0.4906     | Pozitif | **Momentum Etkisi:** Geçen haftaki hareketin devamlılığı. |
| **NET_roll3**         | - 0.4040     | Negatif | **Trend Düzeltme:** Ortalamadan sapma dengesi.            |

\normalsize

Updated Base Model'e ait formül aşağıda verilmiştir:

$$
\begin{aligned}
Net_{t+1} = &-0.6891 + 0.3507 \cdot \text{w/TLREF}_t - 0.2722 \cdot PPK_t - 0.7448 \cdot YearEnd_t \\
&- 0.3464 \cdot \exp(\text{CBavg}_t - TLREF_t) + 1.7151 \cdot MarketAnomaly_t \\
&+ 0.4906 \cdot Net_{t-1} - 0.4040 \cdot \left(\frac{Net_{t-1} + Net_{t-2} + Net_{t-3}}{3}\right)
\end{aligned}
$$

**\textcolor[HTML]{FF6200}{Model Performans Analizi:}**

- **Yüksek Açıklayıcılık:** $R^2 = 0.8027$ ve Adjusted $R^2 = 0.7706$ seviyesine ulaşılmıştır. Multiple R = 0.8959 olup, Legacy modele göre (0.71) ciddi bir sıçrama kaydedilmiştir. **Overfitting Gap = 0.0321** ile güvenilir aralıktadır.
- **Gelişmiş Düzeltme Notu:** Condition Number ile ilgili, doğrusal bağlantı/ölçek hassasiyetine dair sınırlı bir uyarı üretmektedir; kabul edilebilir olmakla birlikte değişken korelasyonları izlenmelidir.
- **Tahmin Hassasiyeti (Test):** **MAE = 0.6834** ve **RMSE = 0.8102** olarak ölçülmüştür. RMSE'nin MAE'den büyük olması, büyük hataların daha fazla cezalandırıldığını ve bazı dönemlerde sapmaların arttığını ima eder.
- **Ayrıştırma (Separation) Gücü:** modelin dönemleri birbirinden ayırma kabiliyeti **GAUC = 0.6481** (Sarı alanda, yeşil eşiğine yakın) olarak ölçülmüştür. Bu sonuç, statik modelin (0.53) üzerine anlamlı bir katman eklendiğini, ancak hala >%65 hedefine ("Yeşil") tam ulaşılamadığını göstermektedir.

Geçmişteki verilerle bir kereliğine eğitilip güncel verileri tahmin ederken kullanılan bu statik modelin geleceği tahmin etmekteki başarısı haricen görselleştirilip dokümana dahil edilmiştir.

\begin{center}
\includegraphics[width=0.85\textwidth]{images/fig_b1.png}
\end{center}

\vspace{0.1cm}

\begin{center}
\includegraphics[width=0.85\textwidth]{images/resid_updated_model_static.png}

\end{center}

**Sonuç ve Stratejik Değerlendirme:**
Elde edilen sonuçlar, Yönetim'in makroekonomik öngörülerine eklenen **Momentum** ve **Trend** bileşenlerinin modelin tahmin gücünü ciddi oranda artırdığını kanıtlamıştır ($R^2 \approx 0.80$). Bu performans, Updated Base Model'i önceki yapıya göre çok daha güçlü bir **"Yeni Referans Noktası" (New Base)** konumuna taşımıştır.

Ancak, mimari ne kadar güçlü olursa olsun, "Statik" (Tek seferlik eğitim) yapısı nedeniyle piyasa değişimlerine adaptasyonu sınırlı kalmaktadır. Bu nedenle, bu modelin **Challenger (Nihai) Model** adayı olabilmesi için operasyonel çevikliğe kavuşması gerekmektedir. Ekip bu doğrultuda şu soruyu sormuştur:
_"Başarısı kanıtlanmış bu güçlü feature setini, statik bırakmak yerine her hafta güncellersek sonuçlar ne olur?"_

Bu motivasyonla, Updated Base Model'in **dinamik yeniden eğitim (Dynamic Retraining)** yeteneğiyle birleştiği nihai senaryo test edilmiştir.

## 2.8. Updated Base Model (Dinamik Yaklaşım – Haftalık Yeniden Eğitim)

Updated Base Model'in (Statik) başarısını **maksimize etmek** ve piyasa değişimlerine **anlık uyum (Real-Time Adaptation)** yeteneği kazandırmak amacıyla, dinamik yeniden eğitim süreci devreye alınmıştır. Amaç; Momentum ve Trend bileşenleriyle güçlendirilmiş mimariyi, "sürekli öğrenen" bir yapıya dönüştürerek tahmin istikrarını en üst seviyeye çıkarmaktır.

Bu kurguda, modelin feature seti ve regresyon yapısı korunmuş; ancak eğitim metodolojisi **Recursive Walk-Forward Validation** (İlerleyen Pencereli Doğrulama) standardına yükseltilmiştir. Model her hafta yeni gelen veriyi öğrenme setine katarak kendini günceller. Bu sayede, geçmişin birikimli bilgisi (Long-term Memory) ile son haftanın piyasa sinyalleri (Short-term Signal) hibrit bir şekilde modele yansıtılır.

\newpage

**Performans Sıçraması (\%23.1):**
Statik yapıdan dinamik yapıya geçiş, modelin potansiyelini tam anlamıyla ortaya çıkarmıştır.

- **Hata Minimizasyonu:** **MAE = 0.5258** ve **RMSE = 0.6485** seviyelerine inilerek, statik Updated modele göre %23.1, Legacy modele göre ise çok daha dramatik bir iyileşme sağlanmıştır.
- **Operasyonel Güvenilirlik:** Modelin piyasa kırılımlarını takip etme hızı (Reaction Speed) operasyonel kullanım için gereken olgunluk seviyesine ulaşmıştır.

\begin{center}
\includegraphics[width=0.85\textwidth]{images/fig_b2.png}
\end{center}

**Stratejik Konumlandırma (Interim Champion):**
Elde edilen bu sonuçlar, **Updated Base Model (Dinamik)** mimarisinin, mevcut makroekonomik ve davranışsal değişken setiyle ulaşılabilecek **"Optimal Performans Noktası" (Efficient Frontier)** olduğunu göstermektedir.

- **Karar:** Bu model, sağladığı yüksek doğruluk ve adaptasyon yeteneği sayesinde, nihai "Challenger Model" geliştirilene kadar Kurum'un **Ana Tahmin Modeli (Interim Champion)** olarak belirlenmiştir.
- **Vizyon:** Gelecek olan Challenger Model çalışmaları, artık "hatayı düzeltmek" için değil, bu yüksek performans standardını (Benchmark) "daha zengin veri setleriyle (Alternatif Veri vb.) aşabilmek" vizyonuyla kurgulanacaktır.

Bu nedenle, operasyonel süreçlerde **Updated Base Model - Dinamik Yaklaşım** ile ilerlenmesi, risk yönetimi ve iş sürekliliği açısından en doğru stratejik adım olarak değerlendirilmiştir.

## 2.9. Model Davranışı ve Nihai Teknik Değerlendirme

Tüm geliştirme süreci boyunca test edilen 4 farklı model versiyonunun teknik karakteristiği ve operasyonel uygunluğu, her birinin kendi bağlamındaki katkılarıyla aşağıda özetlenmiştir:

- **Legacy Base Model (Static):** Piyasa dinamiklerini makro seviyede başarıyla açıklayan, güvenilir bir temel modeldir. Operasyonel karar destek süreçleri için güçlü bir **Referans Noktası (Benchmark)** oluşturmaktadır.
- **Legacy Base Model (Dynamic):** Düzenli eğitim ile tazelenen bu yapı, makro değişkenlerin güncel etkisini yansıtmada oldukça başarılıdır. Mevcut değişken setiyle ulaşılabilen optimum performansı temsil eder.
- **Updated Base Model (Static):** Legacy yapının gücüne eklenen Lag1 (Momentum) ve Roll3 (Mean-Reversion) değişkenleri ile modelin açıklama kapasitesi artırılmıştır. Statik yapısına rağmen, piyasa davranışlarını yakalamada önemli bir yetkinlik kazanmıştır.
- **Updated Base Model (Dynamic):** **Yapısal Güç** ve **Çeviklik** özelliklerini birleştirerek en kapsamlı çözümü sunmaktadır. Geleneksel yapının sağlamlığı ile modern adaptif öğrenme yeteneğini harmanlayarak, tahmin istikrarı açısından en dengeli mimariyi ortaya koymuştur.

\newpage

\normalsize

\vspace{0.2cm}
\noindent \textbf{\textcolor[HTML]{FF6200}{2.9.1. Karşılaştırmalı Tablo (Training Set Performansı Bazında)}}

Aşağıdaki tablo, modellerin eğitim verisi üzerindeki uyum başarısını (Goodness of Fit) göstermektedir:

\small

| Model Versiyonu                  | Feature Sayısı | Eğitim Stratejisi | $R^2$ |  MAE   |
| :------------------------------- | :------------: | :---------------: | :---: | :----: |
| **Legacy Base Model (Static)**   |       5        |   Tek Seferlik    | 0.72  | 0.6556 |
| **Legacy Base Model (Dynamic)**  |       5        | Haftalık Retrain  | 0.72  | 0.6420 |
| **Updated Base Model (Static)**  |       7        |   Tek Seferlik    | 0.80  | 0.5578 |
| **Updated Base Model (Dynamic)** |       7        | Haftalık Retrain  | 0.80  | 0.5441 |

\normalsize

\vspace{0.2cm}
\noindent \textbf{\textcolor[HTML]{FF6200}{2.9.2. Karşılaştırmalı Tablo (Test Set Performansı Bazında)}}

Modellerin gerçek tahmin performansını (Test Seti üzerinde) gösteren sıralama tablosu aşağıdadır. **Rank 1**, en iyi performansı gösteren modeldir.

\small

| Rank | Model Versiyonu              | Güncelleme Stratejisi |  MAE   |
| :--: | :--------------------------- | :-------------------: | :----: |
|  1   | Updated Base Model (Dynamic) |   Haftalık Retrain    | 0.5258 |
|  2   | Legacy Base Model (Dynamic)  |   Haftalık Retrain    | 0.6630 |
|  3   | Updated Base Model (Static)  |     Tek Seferlik      | 0.6835 |
|  4   | Legacy Base Model (Static)   |     Tek Seferlik      | 0.7963 |

\normalsize

\vspace{0.2cm}
\noindent \textbf{\textcolor[HTML]{FF6200}{2.9.3. Retrain Stratejisi Değerlendirmesi}}

Hem feature engineering (değişken zenginleştirme) hem de operasyonel çeviklik (haftalık yeniden eğitim) çalışmaları, modelin tahmin gücüne belirgin katkılar sağlamıştır. Mevcut durumda **7 değişkenli yapı ile haftalık yeniden eğitim** senaryosu, hesaplama maliyeti ile performans kazancı (%34 iyileşme) arasındaki en verimli dengeyi sunmaktadır.

Gelecek dönemde modele yeni değişkenlerin eklenmesiyle karmaşıklık arttığında, maliyet-fayda dengesi yeniden değerlendirilecektir. Güncelleme stratejisi (Retraining Frequency), operasyonel verimlilik gözetilerek optimize edilmeye devam edilecek ve nihai kararlar canlı ortam testleri (A/B Testing) ile doğrulanacaktır.

\normalsize

\normalsize

## 2.10. Modelleme Yaklaşımı: Neden Dinamik Model? (Agility Spectrum)

Projenin metodolojik karar aşamasında, modelin piyasa değişimlerine tepki süresini ve doğruluğunu optimize etmek için üç farklı modelleme stratejisi ("Agility Spectrum") analitik olarak test edilmiştir. **Bu çalışma, yeni eklenen davranışsal özelliklerin (Lag \& Trend) potansiyelini en üst seviyeye çıkarmak amacıyla spesifik olarak Updated Base Model mimarisi üzerinde gerçekleştirilmiştir.**

Modelin hafızasının ne sıklıkla tazelendiği, başarıyı doğrudan etkileyen kritik bir parametredir. Test edilen yöntemler **Quarterly (3 Aylık)**, **Monthly (1 Aylık)** ve **Weekly (1 Haftalık)** olarak ayrılmıştır.

\begin{center}
\includegraphics[width=0.75\textwidth]{images/fig_agility_spectrum.png}
\end{center}

\newpage
\vspace{-0.2cm}
Aşağıdaki performans tablosu, güncelleme sıklığının tahmin hatası (MAE) üzerindeki etkisini özetlemektedir:

\small

| Strateji (Güncelleme Sıklığı) |  MAE   | Performans Değişimi |        Durum        |
| :---------------------------- | :----: | :-----------------: | :-----------------: |
| Quarterly (3 Aylık)           | 0.6835 |      Referans       |       Stabil        |
| Monthly (1 Aylık)             | 0.5948 |  + 13.0% İyileşme   |      Yetersiz       |
| Weekly (1 Haftalık)           | 0.5258 |  + 23.1% İyileşme   | **En İyi Strateji** |

\normalsize

\normalsize

- **Quarterly (3 Aylık) Referans:** Modelin 3 ayda bir güncellendiği bu senaryo, uzun vadeli trendleri takip etmekte başarılı olsa da, kısa vadeli değişimlere karşı en hantal yapıdır. Mevcut statik yapıya en yakın davranışı sergilediği için performans kıyaslamasında **"Baseline" (Referans Noktası)** olarak kabul edilmiştir.
- **Monthly (Aylık) İyileşme:** Model ayda bir eğitildiğinde, standart statik yapıya kıyasla belirli bir iyileşme (%13) sağlamaktadır. Ancak bu süre, volatilitenin yüksek olduğu dönemlerde piyasadaki ani yön değişimlerini (Trend Reversal) yakalamakta geç kalmaktadır.
- **Weekly (Haftalık) Üstünlük:** Haftalık model, piyasadaki **"momentumu"** ve **"trend değişimlerini"** en taze veriyle yakalar. Her hafta bir sonraki haftayı tahmin eder (T+1 Prediction), ardından hata yaptığında ertesi hafta hemen bu hatadan öğrenip katsayılarını düzeltir (**Self-Correction**).

Yapılan kapsamlı testler sonucunda, **Haftalık (Weekly)** strateji en düşük hatayı vererek "Optimal Updating Frequency" olarak belirlenmiştir. Gelecekte model karmaşıklığı arttığında bu karar maliyet/fayda ekseninde yeniden değerlendirilebilir. Ancak Challenger Model oluşturulana kadar, performansın maksimize edilmesi adına **Updated Base Model (Dynamic – Weekly Updated)** mimarisi, teknik performans ve operasyonel uygunluk açısından en doğru yaklaşım olarak değerlendirilmiştir.

\normalsize

\fancyfoot[L]{\textbf{OSA Growth Intelligence Model} $\cdot$ Model Geliştirme Fazları}

# 3. MODEL GELİŞTİRME FAZLARI

Tanımlanan bu beş fazlı yapı, referans bir noktadan başlayıp kontrollü deneylerle (A/B testleri, geriye dönük testler) ilerleyen, ve nihayetinde kullanıcı dostu bir arayüzle "karar desteği" sağlayan uçtan uca bir ürünü temsil eder. Geliştirilen fazlar, akademik validasyon disiplini ile iş dünyasının çeviklik (agility) ihtiyacını dengeleyecek şekilde tasarlanmıştır.

**Metodolojik Not:** Kurgulanan bu yapı (Referans $\rightarrow$ Base $\rightarrow$ Challenger $\rightarrow$ Dashboard), veri bilimi projeleri için "altın standart" kabul edilen **CRISP-DM** (Cross-Industry Standard Process for Data Mining) metodolojisiyle birebir örtüşmekte olup, endüstriyel standartlarda güvenilir bir geliştirme döngüsünü garanti eder.

## 3.1. Faz 1 – Referans Modeli Kurulumu ve Temel Karşılaştırma Zemini

Bu fazın temel amacı, halihazırda kullanılan referans modelin Python ortamında **birebir replikasyonunu** sağlayarak, teknik geliştirme süreci için güvenilir bir başlangıç noktası (benchmark) oluşturmaktır. Bu kapsamda, referans modelde kullanılan tüm değişkenler tanım ve zaman boyutlarıyla birlikte sisteme aktarılmış, iş mantığı ve nedensellik ilişkileri teknik düzlemde irdelenmiştir. Süreç doğrulaması ve karakteristik analizler neticesinde, referans model çıktılarının Python ortamında hatasız şekilde yeniden üretilmesi sağlanmış, böylece ileri analitik geliştirmeler için **Doğrulanmış Referans Model** ve sağlam bir teknik zemin elde edilmiştir.

## 3.2. Faz 2 – Base Model Oluşturulması (Haftalık Güncelleme)

Referans modelin bilgi setini koruyan ancak karar destek süreçlerine daha dinamik yanıt verebilen, operasyonel açıdan güçlendirilmiş bir **Base Model** mimarisi hedeflenmiştir. Bu fazda, temel makroekonomik değişken seti muhafaza edilirken, Net Akış değişkeninin zamansal davranışını (time-series properties) yakalamak adına gecikmeli (lag) ve hareketli ortalama (roll) türevleri modele entegre edilmiştir. Yapılan simülasyonlar sonucunda, statik tek seferlik eğitim yerine **haftalık yeniden eğitim (retrain)** stratejisinin istatistiksel olarak daha üstün olduğu kanıtlanmıştır. Sonuç olarak, Challenger Model tamamlanana kadar operasyonel boşluğu dolduracak yetkinlikte **Base Model (Dynamic)** mimarisi devreye alınmıştır.

## 3.3. Faz 3 – Veri Zenginleştirme ve Feature Engineering

Bu fazda Base Model "sabit bir yapı" olarak kabul edilerek, Challenger Model'e geçiş için gerekli veri çeşitliliğini artırma ve öznitelik mühendisliği çalışmalarına odaklanılmıştır. Modelin "görebildiği" bilgi evrenini genişleterek karmaşık piyasa davranışlarını açıklama gücünü artırmak esastır. Çalışmalar kapsamında farklı zaman pencereleri, alternatif gecikme kombinasyonları ve piyasa rejim değişimlerine (volatilite vb.) duyarlı türev değişkenler geliştirilmiştir. Yapılan ekonomik anlamlılık ve etki analizleri sonucunda, Challenger Model geliştirimi için optimize edilmiş **Zenginleştirilmiş Veri ve Öznitelik Havuzu** oluşturulmuştur.

## 3.4. Faz 4 – Challenger Model Geliştirme ve Karşılaştırmalı Değerlendirme

Zenginleştirilmiş veri seti kullanılarak Base Model'in performans limitlerini aşacak **Challenger Model(ler)** geliştirmek ve bunları sistematik metriklerle kıyaslamak bu fazın temel hedefidir. Genişletilmiş öznitelik seti ile eğitilen alternatif modeller; **tahmin doğruluğu (Accuracy)**, **zaman serisi uyumu (Stability)** ve **rejim değişimlerine adaptasyon (Robustness)** ekseninde Base Model ile karşılaştırılmıştır. Performans artışının getirdiği model karmaşıklığının operasyonel sürdürülebilirlik dengesi gözetilerek yapılan değerlendirmeler neticesinde, karar destek sistemine entegre edilecek **Onaylanmış Challenger (Final) Model** belirlenmiştir.

## 3.5. Faz 5 – Dashboard ve Karar Destek Arayüzü

Teknik model çıktılarının iş birimleri ve üst yönetim tarafından doğrudan tüketilebilir, anlaşılır ve aksiyon odaklı bir yapıya kavuşturulması amacıyla **Karar Destek Arayüzü (Dashboard)** geliştirilmiştir. Seçilen Challenger Model üzerine kurgulanan bu arayüzde; tahmin edilen Net Akış değerlerinin tarihsel seyri, Bütçe hedefleriyle olan anlık fark (Gap) analizleri ve farklı piyasa koşullarına göre üretilen "What-If" senaryoları görselleştirilmiştir. Bu sayede analitik çıktıların iş süreçlerine tam entegrasyonu sağlanmış ve karar vericiler için efektif bir **Executive Dashboard** sunulmuştur.

\fancyfoot[L]{\textbf{OSA Growth Intelligence Model} $\cdot$ Operasyonel Kullanım ve İş Akışı}

# 4. OPERASYONEL KULLANIM VE İŞ AKIŞI

Modelin operasyonel kullanım döngüsü, sadece statik bir tahmin üretme süreci değil, veriden stratejik aksiyona giden uçtan uca bir **"Growth Intelligence Cycle"** (Büyüme Zekası Döngüsü) olarak kurgulanmıştır. Bu döngü, haftalık periyotlarla (retrain frequency) tetiklenir ve 6 adımlı analitik akışı stratejik bir derinlikle uygular.

**Döngü Notu:** Retrain periyodu, Gap Analizi periyodunu belirler (Haftalık retrain = Haftalık aksiyon kararı). Haftalık güncelleme, volatilitenin yüksek olduğu dönemlerde hedefe göre proaktif faiz (fine-tuning) ayarlaması yapılmasına olanak tanır.

## 4.1. Bütünleşik Karar ve Optimizasyon Mekanizması

OSA Growth Intelligence Modeli, statik hedefler yerine dinamik adaptasyonu esas alan bütünleşik bir karar mekanizması üzerine kuruludur. Bu mekanizma, **"Dinamik Hedefleme"** ve **"Operasyonel Karar Döngüsü"** olmak üzere birbirini takip eden iki ana modülden meydana gelir.

### 4.1.1. Modül A: Dinamik Hedef Hesaplama

Gap analizi, statik bir hedef yerine, model performansına göre sürekli güncellenen **"Dinamik Güvenlik Tamponlu Hedef"** mantığıyla çalışır. Bu sistem, **Sliding Window (Kayan Pencere)** stratejisiyle sürekli öğrenen bir yapıdadır.

**\textcolor[HTML]{FF6200}{Buffer Hesaplama Mekaniği ve Matematiksel Temel:}**

Toplam güvenlik tamponu ($\text{Buffer}_{\text{Total}}$) 3 aşamalı bir hesaplama zinciri ile bulunur:

**\textcolor[HTML]{FF6200}{Adım 1: Model Hatasının (RMSE) Ölçülmesi:}**
Model her hafta son 12 haftalık **Out-of-Sample Backtest** yapar. Gerçekleşen ($y$) ile Tahmin edilen ($\hat{y}$) arasındaki farkın karesinin ortalaması alınır:

$$
\text{RMSE}_t = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2} \quad \text{| Mevcut Değer: } \approx 0.65\%
$$

**\textcolor[HTML]{FF6200}{Adım 2: Haftalık Baz Tamponun Hesaplanması:}**
Burada RMSE (Hata), Bankanın Risk Toleransı (Z-Score) ile çarpılır.

$$
\text{Buffer}_{\text{Weekly}} = \underbrace{1.65}_{\text{Z-Score}} \times \underbrace{\text{RMSE}_t}_{\text{Model Hatası}} \approx 1.07\%
$$

\noindent \textbf{Not:} Z-Score, bankanın hedeflediği güven seviyesine (Risk Policy) bağlı **sabit bir parametredir** (Genelde %95 = 1.65). Her hafta değişen değer, Z-Score değil, onunla çarpılan **Model Hatasıdır (RMSE)**.

$$
Z = \Phi^{-1}(0.95) \approx 1.65 \quad (\text{Sabit Politika})
$$

**\textcolor[HTML]{FF6200}{Adım 3: Toplam Dinamik Tampon (Zaman Etkisi):}**
Finansal belirsizlik zamanın karekökü ($\sqrt{t}$) ile orantılıdır. Yıl sonuna uzakken belirsizlik yüksek, vade yaklaştıkça düşüktür.

$$
\text{Buffer}_{\text{Total}} = \text{Buffer}_{\text{Weekly}} \times \sqrt{\text{Kalan Hafta}}
$$

\textbf{Örnek:} Yıl ortasında 26 hafta varken; $1.07\% \times \sqrt{26} \approx \mathbf{5.45\%}$

**\textcolor[HTML]{FF6200}{Sonuç: Operasyonel Hedefin Belirlenmesi:}**

$$
\text{Target}_{\text{Ops}} = 120B \times (1 + \text{Buffer}_{\text{Total}})
$$

\textbf{Örnek:} Hesaplanan %5.45 tampon ile; $120\text{B} \times 1.0545 \approx \mathbf{126.5\text{B TL}}$
\noindent \textbf{Bilgi:} Hedef sabit değildir, her hafta bu formülle yeniden hesaplanır.

**\textcolor[HTML]{FF6200}{Buffer Adaptasyon Dinamiği (Zaman Ve Performans Etkisi):}**
Model **Sliding Window** (Eskiyi çıkar, yeniyi ekle) ile çalıştığı için, veri seti kalitesi arttıkça yıl sonuna doğru RMSE'nin düşmesi (iyileşmesi) beklenir.

\small

| Senaryo            | Kalan Hafta ($t$) | Model Hatası (RMSE) | Toplam Buffer ($\times \sqrt{t}$) | Operasyonel Hedef ($Target_{Ops}$) |                   Yorum                    |
| :----------------- | :---------------: | :-----------------: | :-------------------------------: | :--------------------------------: | :----------------------------------------: |
| **Yıl Başı**       |        52         |        %0.65        |            **~%7.71**             |            **~129.2B**             |       Başlangıç belirsizliği yüksek.       |
| **Yıl Ortası**     |        26         |        %0.65        |            **~%5.45**             |            **~126.5B**             |          Standart koruma kalkanı.          |
| **Model İyileşti** |      **12**       |      **%0.50**      |            **~%2.86**             |            **~123.4B**             |    Model trendi çözdü, hedef rahatladı.    |
| **Piyasa Şoku**    |       **4**       |      **%0.80**      |            **~%2.64**             |            **~123.2B**             |   Volatilite arttı, güvenlik arttırıldı.   |
| **Son Düzlük**     |       **1**       |      **%0.60**      |            **~%0.99**             |            **~121.2B**             | Modelin öğrenme etkisiyle hata payı düştü. |

\normalsize

\newpage

**\textcolor[HTML]{FF6200}{Bakiye Projeksiyonu (İnteraktif ve Otomatik Simülasyon):}**
Dashboard üzerindeki simülasyon paneli, sadece mevcut durumu değil, **"Automatic Scenario Analysis"** özelliğiyle yıl sonu için bir "güven aralığı" sunar. Sistem, piyasa volatilite verilerini kullanarak 4 farklı otomatik senaryo üretir:

1. **İyimser (Optimistic):** Faiz/Kur dengesinin hacim lehine döndüğü senaryo (Maksimum Bakiye). Tahmin RMSE ve piyasa volatilitesi ($\sigma$) kullanılarak hesaplanan **%95 Güven Aralığı ($1.65\sigma$)** bantlarıdır.
2. **Normal (Base Case):** Mevcut trendin ve makro beklentilerin korunduğu senaryo. Modelin mevcut piyasa şartlarındaki baz tahminidir.
3. **Kötümser (Pessimistic):** Churn oranının arttığı veya kur şoklarının yaşandığı senaryo. Tahmin RMSE ve piyasa volatilitesi ($\sigma$) kullanılarak hesaplanan **%95 Güven Aralığı ($1.65\sigma$)** bantlarıdır.
4. **Daha Kötümser (Worst Case):** Çoklu risk faktörlerinin eş zamanlı tetiklendiği senaryo (Minimum Bakiye). Beklenmedik "Tail Risk" (Kuyruk Riski) ve makroekonomik şokları (örn: USD/TRY ani yükselişi + Churn artışı) simüle eden **$3\sigma$ / Stres Testi** seviyesidir.

Bu araç, kullanıcıya tek bir rakam yerine, **"Yıl sonunda en az X, en fazla Y bakiyede oluruz"** şeklinde net bir Min/Max bandı çizer.

**Senaryo Üretim Metodolojisi:**
Sistem, bu senaryo katmanlarını aşağıdaki matematiksel yaklaşımla ve **standart sapma ($\sigma_{vol}$)** bantlarına göre oluşturur:

$$
\begin{aligned}
\text{Normal (Base Case)} &= \hat{y}_t \quad (\text{Model Tahmini}) \\
\text{İyimser (Optimistic)} &= \hat{y}_t + (1.65 \times \sigma_{vol}) \\
\text{Kötümser (Pessimistic)} &= \hat{y}_t - (1.65 \times \sigma_{vol}) \\
\text{Daha Kötümser (Worst Case)} &= \hat{y}_t - (3.00 \times \sigma_{vol})
\end{aligned}
$$

Burada $\sigma_{vol}$, bankanın tarihsel **Net Akış (Net Flow TL)** volatilitesidir.

**$\sigma_{vol}$ (Volatilite) Nasıl Hesaplanır?**
Model, son 12 haftalık "Haftalık Net Akış (TL)" verilerinin standart sapmasını alarak bu risk parametresini dinamik olarak üretir:

$$
\sigma_{vol} = \sqrt{\frac{\sum (x_i - \bar{x})^2}{N-1}} \quad \text{(TL Bazlı Standart Sapma)}
$$

**Örnek Hesaplama:**
Modelin haftalık **+500 Milyon TL** net giriş tahmin ettiği ve tarihsel hacimsel oynaklığın **300 Milyon TL** ($\sigma_{vol}$) olduğu bir durumda:

- **Normal:** +500 Milyon TL
- **İyimser (+1.65$\sigma$):** $500 + (1.65 \times 300) = \mathbf{+995 \text{ Milyon TL}}$
- **Kötümser (-1.65$\sigma$):** $500 - (1.65 \times 300) = \mathbf{+5 \text{ Milyon TL}}$ (Büyüme durma noktasına gelir)
- **Daha Kötümser (-3$\sigma$):** $500 - (3.00 \times 300) = \mathbf{-400 \text{ Milyon TL}}$ (Net Çıkış/Küçülme başlar)
  Hesaplama, her senaryo için haftalık bazda kümülatif olarak işletilir:
  \vspace{-0.1cm}

$$
\text{Bakiye}_{\text{Yıl Sonu}} = \text{Mevcut Bakiye} + \sum_{i=1}^{n} (\text{Net Akış Tahmini}_i)
$$

\vspace{-0.1cm}

**Stratejik Rol:** Bu interaktif yapı, karar vericilere sadece bir tahmin sunmaz; faiz ve kur "lever"larını (kaldıraçlarını) kullanarak hedefe ulaşmak için en düşük maliyetli rotayı bulma imkanı verir. Bu çıktılar, Modül B'deki Adım 6 (Stratejik Karar Matrisi) için temel girdidir.

### 4.1.2. Modül B: Stratejik Karar Döngüsü

Modül A'da hesaplanan Dinamik Hedef ($Target_{Ops}$), operasyonel sürecin temel girdisidir. Karar mekanizması, bu hedefi alarak "Mevcut Konum" ile "İdeal Rota" arasındaki sapmayı yöneten bir Optimizasyon Problemi çözer.

Aşağıdaki 6 adımlı analiz döngüsü, her Pazartesi sabahı (Retrain sonrası) otomatik olarak çalıştırılır:

**Adım 1: Mevcut Durum Analizi ve Veri Güncelleme (Snapshot)**
Bu adımda sistem, Banka'nın anlık finansal koordinatlarını belirler.

- **Mevcut Bakiye (Actual Position):** 105 Milyar TL
- **Operasyonel Hedef (TargetOps):** ~126.5 Milyar TL (Modül A'dan gelir)
- **Kalan Süre:** 26 Hafta

**Adım 2: Modelin Yeniden Eğitilmesi (Retrain)**
Model, en güncel gerçekleşen bakiye verisiyle pazarın yeni dengesini öğrenir.

**Adım 3: Yapısal Tahmin Üretimi (Prediction)**
Updated Base Model, mevcut faiz oranları ve piyasa koşullarında gelecek hafta için kendi "Saf Matematiksel Öngörüsünü" sunar. (Örnek: Model, mevcut şartlarda ancak **%0.45'lik bir büyüme** öngörüyor.)

**Adım 4: Otomatik Senaryo Simülasyonu (Simulation)**
Tahminler kümülatif olarak yıl sonuna taşınır ve 4 olasılık bandı çizilir:

- **Normal (Base Case):** Yıl Sonu ~118.5 Milyar TL (Hedefin altında)
- **İyimser:** ~123.0 Milyar TL
- **Kötümser:** ~114.0 Milyar TL
- **Daha Kötümser:** ~110.0 Milyar TL

**Adım 5: Gap Analizi ve Büyüme Hızı (Quantification)**
Hedeflenen rota ile simüle edilen nokta arasındaki fark ölçülür ve kapatılması gereken hız hesaplanır.

- **Gap:** $Target_{Ops} - \text{Projeksiyon} = 126.5B - 118.5B = \mathbf{8.0B \text{ TL}}$ ek bakiye gerekiyor.
- **Gerekli Hız (Catch-up):** Haftalık ortalama **%0.79 büyüme** gerekiyor.

**Adım 6: Stratejik Karar ve Risk Hesaplaması (Decision)**
Sistem, sadece rakamsal farka değil, bu farkın "Risk Boyutuna" bakar.

- **Risk Durumu (Z-Score Analizi):**
  - **$\sigma_{Risk}$ (Projeksiyon Volatilitesi):** Modelin yıl sonu tahminindeki toplam belirsizlik aralığıdır. Haftalık volatilitenin ($\sigma_{vol}$) karekök zaman kuralı ile genişletilmesiyle hesaplanır:
    $$
    \sigma_{Risk} = \sigma_{vol} \times \sqrt{t} = 0.51B \times \sqrt{26} \approx \mathbf{2.6 \text{ Milyar TL}}
    $$
  - **$Z_{Risk}$ Hesabı:** Oluşan Gap (Açık), bu belirsizliğin kaç katı?
    $$
    Z_{Risk} = \frac{\text{Toplam Gap}}{\sigma_{Risk}} = \frac{8.0B}{2.6B} \approx \mathbf{3.07}
    $$
  * **Hız Analizi (Urgency):** Model tahmini ile gereken hız arasındaki fark ($\Delta\text{Hız} = 0.45\% - 0.79\% = -0.34\%$) negatif ise sistem **"Gecikme Alarmı"** verir.

* **Sonuç:** $Z_{Risk} > 3$ durumu, mevcut sapmanın standart bir dalgalanma olmadığını, **%99.8 ihtimalle** hedefin kaçacağını gösterir. Bu bir **"Yapısal Trend Bozulmasıdır"**.

**Karar:** Matris devreye girer. Gap Kritik seviyede olduğu için **Senaryo A veya B** (Faiz Artışı) önerilir.

**Optimizasyon Hedefi (Volume vs. Cost Balancing):**
Sistem sadece "hedefi tutturmaya" odaklanmaz. Asıl amaç, hedefi tutturacak en düşük maliyetli (Optimal) faiz oranını bulmaktır. Eğer yüksek faiz Churn'ü azaltıyor ama marjı (Spread) çok daraltıyorsa, model bu noktada "Maliyet Etkinliği" filtresini devreye sokarak dengeleyici bir öneri sunar. Dashboard üzerinde bu durum, **"Optimal Büyüme Sınırı" (Efficient Frontier)** olarak takip edilir.

**Yönetişim Notu (Human-in-the-Loop):**
Sistem bu verileri işleyerek nihai bir "Karar" değil, yetkili komitelere (ALCO) sunulmak üzere matematiksel tabanlı bir **"Karar Destek Önerisi" (Recommendation)** üretir. Modelin çıktısı, yönetimin stratejik inisiyatifi ile birleşerek nihai aksiyona dönüşür.

**Maliyet ve Fiyatlama Mantığı (OSA Welcome Mechanics):**
Sistem, "OSA Welcome (Turuncu Hoşgeldin)" faiz oranını, piyasa ortalamasına göre bir "kaldıraç" olarak kullanır. Bu mekanizmada model, Net % (Inflow% - Outflow%) tahmini ile Fiyatlama (Maliyet) arasında bir denge kurar:

1. **Piyasa Esnekliği (Market Elasticity):** Faiz ile hacim arasındaki korelasyondur.
   - **Agresif Fiyatlama (Gereksiz Artış Riski):** OSA Welcome oranı piyasanın çok üzerine çıkarılırsa hacim artışı maksimize olur. Ancak, Mevduat Maliyeti (Cost of Fund) gereksiz yere yükselir ve Net Faiz Marjı (NIM) daralır. Banka, sürdürülemez maliyetle (High Cost of Fund) büyüme gerçekleştirmiş olur.
   - **Defansif Fiyatlama (Gereksiz Azalış Riski):** Maliyeti düşürmek için OSA Welcome çok düşük tutulursa karlılık artar; fakat bu durumda Churn (Çıkış) hızı giriş hızını aşar ($Outflow > Inflow$). Yıl sonu hedefinden uzaklaşılır ve stratejik büyüme planı sekteye uğrar.

2. **Optimizasyon Hedefi:** Modelin asıl görevi, hedefe ulaştıran En Düşük Maliyetli OSA Welcome oranını bulmaktır. Eğer Gap güvenli bölgedeyse (< 1$\sigma$), model otomatik olarak "Fren" yapılmasını önererek bankayı gereksiz faiz giderinden kurtarır. Daha hassas yönetim için sistem aşağıdaki 5 Seviyeli Karar Matrisi'ni kullanır:

| Gap Durumu (Sigma)                        | Analiz (Durum vs Tahmin)        | Stratejik Karar (Action) |
| :---------------------------------------- | :------------------------------ | :----------------------- |
| Gap > 3$\sigma$ (Kritik)                  | Tahmin < Gerekli (Trend Bozuk)  | **Senaryo A**            |
| Gap 2$\sigma$ - 3$\sigma$ (Yüksek)        | Tahmin < Gerekli (Trend Geride) | **Senaryo B**            |
| Gap 1$\sigma$ - 2$\sigma$ (Yönetilebilir) | Tahmin$\approx$ Gerekli (Denge) | **Senaryo C**            |
| Gap 0$\sigma$ - 1$\sigma$ (Konforlu)      | Tahmin > Gerekli (Konforlu)     | **Senaryo D**            |
| Gap < 0 (Hedef Fazlası)                   | Tahmin > Gerekli (İvme Pozitif) | **Senaryo E**            |

**Senaryo Detayları ve Aksiyon Planı:**

1. **Senaryo A - Best Effort (Kritik Müdahale):** Hedeflenen hacimden ciddi oranda (>$3\sigma$) sapıldığı ve mevcut trendin yetersiz kaldığı bu durumda, maliyet ikinci plana atılır. Pazar payı kaybını (Churn) durdurmak ve portföy büyümesini tekrar ivmelendirmek amacıyla, rekabetçiliği maksimize edecek **agresif faiz artışı önerilir**.
2. **Senaryo B - Trend Repair (Trend Onarımı):** Büyüme ivmesinde yavaşlamanın başladığı ve müdahale edilmezse hedeften uzaklaşma riskinin doğduğu senaryodur. Negatif ayrışan trendi erkenden kırmak, açığın büyümesini engellemek ve tekrar "güvenli bölgeye" dönmek için piyasayı yakalayan **proaktif faiz artışı tavsiye edilir**.
3. **Senaryo C - Cost Efficiency (Sürdürülebilir Denge):** Büyüme trendinin hedefle uyumlu olduğu, belirgin bir risk veya fırsat fazlasının bulunmadığı denge durumudur. Ekstra fonlama maliyetine girmeden mevcut büyüme temposunu ve istikrarı sürdürmek adına, mevcut rekabetçi pozisyonu koruyan **"Piyasa Paralel" fiyatlama stratejisi izlenmesi önerilir**.
4. **Senaryo D - Margin Testing (Marj Optimizasyonu):** Hedefin üzerinde, konforlu bir büyüme seyrinin izlendiği durumdur. Hacim kaybı yaratmadan bankanın faiz marjını (NIM) iyileştirmek ve müşterinin fiyat duyarlılığını ölçmek amacıyla, faiz oranında **sınırlı ve kontrollü indirim (Test) yapılması önerilir**.
5. **Senaryo E - Growth/Upside (Karlılık Maksimizasyonu):** Hedefin belirgin şekilde üzerinde performans gösterildiği (<$0$ Gap) durumdur. "Fazla" likiditeyi daha düşük maliyetle yönetmek ve gereksiz faiz giderini banka karlılığına (P&L) aktarmak için **agresif faiz indirimi ile maliyet optimizasyonuna gidilmesi tavsiye edilir**.

\newpage

**Örnek Senaryo Sonucu:**
Analiz edilen örnekte sistem şu matematiksel kanıtlarla karar üretmiştir:

1. **Hacim Riski:** $Z_{Risk} = 3.07$ (Kritik Eşik Geçildi).
2. **Hız Açığı:** Trend Yetersiz.
3. **Karar:** Senaryo A (Best Effort).
4. **Önerilen Aksiyon:** Agresif OSA Welcome Artışı. Hedefi tutturmak için "maliyet" göze alınarak Turuncu Hoşgeldin faizi artırılmalı ve nakit girişi hızlandırılmalıdır.

### 4.1.3. Beklenen İş Etkisi ve Katma Değer (Business Impact)

Bu sistematik yaklaşımın bankanın operasyonel süreçlerine ve bilançosuna somut katkıları şöyledir:

**1. Finansal Kazanım (Cost Optimization):**

- **Faiz Gideri Tasarrufu:** Simülasyon ortamında yapılan geriye dönük testlerde (Backtest), modelin önerdiği dinamik marj yönetimi ile yıllık **%15-20 oranında faiz gideri tasarrufu** sağlanabildiği gözlemlenmiştir. Geleneksel "her zaman yüksek faiz" yaklaşımı yerine, sadece risk anında (Gap > 2$\sigma$, Senaryo A/B) proaktif artış, konfor alanında (Gap < 1$\sigma$, Senaryo D/E) ise maliyet freni uygulanır.
- **Hedef Gerçekleşme Garantisi:** Veri odaklı erken uyarı sistemi, sapmaları henüz "trend" halindeyken (Noise aşamasında) yakalar. Backtest sonuçlarına göre, bu erken müdahale mekanizması sayesinde yıl sonu hedeflerinin tutturulma başarı oranı **>%90 seviyesine** çıkmaktadır (Forecast Accuracy).

**2. Stratejik ve Operasyonel Kazanım (Operational Excellence):**

- **Karar Alma Hızı (Agility):** Eskiden manuel analizler ve veri toplama süreçleriyle saatler süren Üst Yönetim Karar Destek hazırlığı, modelin otomatik çıktıları sayesinde **15 dakikaya** iner.
- **Şeffaflık ve Denetlenebilirlik (Auditability):** Faiz kararları kişisel sezgilere ("Bence piyasa sıkışık, artıralım") değil, matematiksel kanıtlara ("Gap 3 Sigma dışına taştı, model tahmini yetersiz, artış matematiksel zorunluluk") dayandırılır. Bu da kurumsal hafıza ve stratejik yönetim süreçleri için şeffaf bir iz (trace) oluşturur.

### 4.1.4. Genel Akış Özeti: Uçtan Uca Büyüme Zekası Döngüsü

Bu bölüm, OSA Growth Intelligence Modelinin ham veriyi stratejik karara dönüştürürken izlediği "Büyüme Zekası Döngüsü"nü (Growth Intelligence Cycle) özetler. Süreç, statik bir raporlama değil, **"Önce Teşhis Sonra Tedavi"** mantığıyla çalışan 4 aşamalı interaktif bir simülasyondur.

**1. Navigasyon ve Dinamik Hedefleme (Modül A):**
Süreç, **"Bugün nerede olmalıyız?"** sorusunun cevabıyla başlar.

- Model, geçmiş 12 haftalık hata payını (**RMSE**) ve bankanın risk iştahını analiz ederek kendine bir "Güvenlik Tamponu" (**Buffer**) oluşturur.
- Bu tampon, zaman etkisiyle ($\sqrt{t}$) genişletilerek o haftanın **"Operasyonel Hedefi"** (TargetOps) hesaplanır. (Örnek: 100B yerine 102B olması gereken rota).

**2. Teşhis Simülasyonu (Mevcut Durumun Röntgeni):**
Sistem önce **"Mevcut faize dokunmazsak yıl sonunda ne olur?"** sorusunu simüle eder.

- Piyasa verileriyle **4 Olasılık Bandı** (İyimser/Normal/Kötümser/Çok Kötümser) hesaplanır.
- **Gap Analizi:** Eğer bu simülasyonda "Normal Gidişat", "Hedefin" altında kalıyorsa ve bu sapma **2 Sigma** sınırını aşıyorsa, model teşhisi koyar: _"Mevcut 'Normalimiz' bozuldu, Kötümser Bölgeye sürükleniyoruz. Müdahale şart."_

\newpage
\fancyfoot[L]{\textbf{OSA Growth Intelligence Model} $\cdot$ Veri Zenginleştirme}

**3. Reçete Yazımı (Karar Matrisi - Modül B):**
Bu, müdahale adımıdır. Sistem, açığı kapatmak için **5 Seviyeli Karar Matrisi**ni tarar.

- Sistem şu hesabı yapar: _"Sürüklendiğimiz Kötümser rotadan çıkıp tekrar Güvenli Rotaya dönmek için faizi ne kadar artırmalıyım?"_
- **Optimizasyon:** Farklı oranları (Tersine Simülasyon) deneyerek en düşük maliyetli çözümü bulur (Örn: **Senaryo B - Trend Repair**).

**4. Doğrulama Simülasyonu (İnteraktif Test):**
Yöneticiye sunulan nihai ekran budur. Model, önerdiği ilacın etkisini **canlı olarak** gösterir.

- Önerilen aksiyon (Senaryo B) seçildiğinde, sistem **Adım 2'deki 4 Olasılık Bandını bu yeni faiz oranıyla tekrar hesaplar.**
- Ekranda **"Yeni Normal"** eğrisinin yukarı taşındığı ve hedefi yakaladığı net bir şekilde görülür.
- **Sonuç:** Yönetici, _"Eğer bu kararı alırsam, Kötümser senaryom bile hedefin üstüne çıkıyor"_ diyerek kararı matematiksel güvenle onaylar.

**Özet:** Model, 4 Olasılık Senaryosunu sadece bir rapor olarak değil, her stratejik hamlenin sonucunu (Impact Analysis) önceden test ettiği bir **Karar Simülatörü** olarak kullanır.

# 5. VERİ ZENGİNLEŞTİRME

Mevcut modele eklenecek değişken havuzu, piyasadaki hareketliliğin de takip edilebilmesi ve buna uygun bankanın da kararlarını daha net verebilmesi adına araştırılarak listelenmiştir. Model, "Piyasa neye reaksiyon veriyor?" sorusuna cevap ararken aşağıdaki temel göstergeleri kullanır. Buradaki değişkenler temsil niteliğindedir, her bir feature için araştırma yapılacaktır ancak geriye yönelik veri toplanabilirse bu değişkenler dahil edilecektir.

## 5.1. Mevcut Model Bileşenleri (Updated Base Model Features)

Şu anda üretim ortamında çalışan ve Net Akış tahmininin **%80'ini tek başına açıklayan**, istatistiksel gücü kanıtlanmış 7 temel bileşen aşağıdadır:

- **w/TLREF (Mevduat Maliyeti):** Bankamızın uyguladığı ağırlıklı ortalama mevduat maliyeti ile hacim arasındaki pozitif ilişkiyi ölçer. İstatistiksel olarak modelin en güçlü değişkenidir ve müşterinin fiyata duyarlılığını (Price Elasticity) temsil eder.
- **EXP(Spread) (Beklenti Makası):** Piyasa faizi ile TCMB faizi arasındaki makasın non-lineer etkisidir. Piyasa beklentisi bizden yüksekse çıkışın hızlandığını, rakip %50 verirken biz %45 veriyorsak müşterinin bu farka tepki verdiğini gösterir.
- **NET_lag1 (Momentum):** Geçen haftaki akış hareketinin devamlılığını ölçen momentum etkisidir. "Geçen hafta giriş olduysa, bu hafta da olma eğilimindedir" prensibine dayanır.
- **NET_roll3 (Trend Düzeltme):** Son 3 haftanın hareketli ortalamasıdır. Trendin aşırıya kaçtığı durumlarda "Ortalamaya Dönüş" (Mean Reversion) etkisini yakalayarak tahminleri dengeler.
- **PPK (Politika Faizi Haftası):** PPK kararlarının açıklandığı haftalarda piyasadaki bekle-gör eğilimini ve hacimdeki geçici yavaşlamayı ifade eden takvimsel kukla (dummy) değişkendir.
- **YearEnd (Yıl Sonu Etkisi):** Bankaların bilanço kapama dönemlerindeki (Aralık sonu) likidite sıkışıklığı ve mevduat yarışının yarattığı hacimsel düşüş etkisidir.

* **Market Anomaly (Piyasa Şoku):** Olağandışı piyasa koşullarını (Örn: Kur Korumalı Mevduat çıkışı vb.) ve finansal şokları temsil eden, modelin standart dışı durumlara karşı dayanıklılığını sağlayan değişkendir.

### 5.1.1. Temel Özellik Mühendisliği (Excel Kaynağı - Detay)

Yukarıdaki 7 temel model bileşeninin oluşturulmasında kullanılan ve "Feature Engineering" (Öznitelik Mühendisliği) aşamasında hesaplanan detay veri seti aşağıdadır. Bu değişkenler, ham verinin işlenerek modelin anlayacağı matematiksel sinyallere dönüştürülmüş halleridir (Base Features):

**Compound Rates (Bileşik Faizler):**

- **CB Rates (1-3M):** Merkez Bankası ve piyasa yapıcı bankaların 1-3 aylık bileşik faiz oranları.
- **OSA Book / Welcome:** Turuncu Hesap portföyünün ve Hoşgeldin faizinin bileşik getiri karşılıkları.
- **OSA Welcome w/current:** Mevcut müşteriye sunulan Hoşgeldin faizi ile potansiyel faiz arasındaki farkın bileşik etkisi.

**5D Moving Avg (5 Günlük Hareketli Ortalamalar):**

- **Inflow / Outflow / NET:** Günlük volatiliteden arındırılmış, son 5 iş gününün ortalama giriş, çıkış ve net akış oranları (Trend Yumuşatma).

**Complex Rates (Basit ve Bileşik Ayrımı):**

- **TL REF / Bileşik:** Referans faizin basit ve bileşik versiyonları.
- **<1 Month / 1-3 Month:** Vade yapısına göre ayrıştırılmış piyasa faizleri (Basit/Bileşik).

**Deltas (Fark Analizleri):**

- **w/TLREF Delta:** Bankanın maliyeti ile TLREF arasındaki anlık makas.
- **w/1 Month & w/3 Month:** Bankanın faizi ile piyasanın 1 ve 3 aylık ortalamaları arasındaki rekabet farkı.

**Deltas w/OSA Current:** Mevcut müşteriye uygulanan faizin, piyasa referanslarına (TLREF, 1M, 3M) göre durumu.

**Rekabet Farkı (Basit Faiz):**

- **<1 Month - TLREF:** Kısa vadeli mevduat faizi ile gecelik referans faiz arasındaki arbitraj imkanı.
- **1-3 Month - TLREF:** Vadeli mevduatın gecelik piyasaya göre sunduğu prim (Term Premium).

## 5.2. FIRAST Model Bileşenleri (Candidate Features)

Bu çalışma ile paralel yürütülen FIRAST projesinden elde edilen ve modele entegrasyonu planlanan potansiyel değişken havuzudur. Mevcut model "Net" rakama odaklanırken, bu veri seti "Brüt" hareketleri ve alternatif piyasa çarpanlarını da kapsayarak analizi derinleştirir.

- **AoFF (Ağırlıklı Ortalama Fonlama Maliyeti):** TCMB ve bankalararası piyasadaki genel fonlama maliyetidir. Bankanın kendi maliyeti (w/TLREF) ile sektör ortalaması (AoFF) arasındaki fark, rekabetçi konumu belirler.
- **PP Getiri (Para Piyasası Fonları):** Likit fonların (Money Market Funds) sunduğu getiridir. Mevduatın en güçlü rakibi (ikame ürün) olduğu için, buradaki getiri artışlarının mevduattan çıkışı tetikleme riski modelenir.
- **TCMB 1M (1 Aylık Referans Faiz):** Merkez Bankası ve piyasa yapıcıların 1 aylık vadeli fonlama maliyetidir. Bankanın kısa vadeli fiyatlamasında "taban fiyat" (floor) etkisi yaratır.
- **Benchmark (Gösterge Tahvil Faizi):** Piyasanın uzun vadeli faiz beklentisini ve risksiz getiri oranını (Risk-free Rate) yansıtır. Mevduat faizinin, tahvil getirisine göre cazibesini ölçer.
- **BIST100 (Alternatif Getiri):** Borsa endeksinin mevduat üzerindeki "İkame Etkisi"ni (Substitution Effect) ölçer. Borsa rallilerinde risk iştahının artmasıyla mevduattan çıkışın (Outflow) tetiklenip tetiklenmediğini analiz eder.
- **Spot Kredi (Alternatif Maliyet):** Ticari kredi faiz oranlarıdır. Bankanın topladığı mevduatı krediye dönüştürme iştahını (Credit-Deposit Spread) ve paranın alternatif getirisini temsil eder.
- **WebTüFe (Enflasyon Beklentisi):** Online fiyat endeksleri üzerinden anlık enflasyon beklentisini ölçerek, müşterinin "Reel Getiri" arayışını ve faize duyarlılığını tahminler.
- **Sepet Kur (Döviz Kuru Etkisi):** (0.5 USD + 0.5 EUR) sepet kurundaki haftalık değişimi takip eder. TL mevduattan dövize geçiş (Dolarizasyon) eğilimini ve kur şoklarının "Flight to Safety" (Güvenli Limana Kaçış) etkisini modellemeye yarar.
- **Gelen / Giden EFT (Para Trafiği):** Banka üzerindeki işlem hacmini ve paranın dolaşım hızını (Velocity) ölçer. EFT hacmindeki ani artışlar, maaş ödemeleri veya vergi dönemleri gibi likidite çıkış sinyallerini yakalar.
- **Inflow / Outflow (Akış Ayrıştırması):** Modelin hedefi olan Net Akış (NetFlow), aslında **(Giriş - Çıkış)** matematiğinden oluşur. Bu bileşenlerin ayrı ayrı modelenmesi, sorunun "Yetersiz Para Girişi" mi yoksa "Aşırı Para Çıkışı" mı olduğunun kök neden analizini (Root Cause Analysis) sağlar.
- **Opening Account (Yeni Müşteri Kazanımı):** Haftalık yeni açılan hesap adedidir. Hacim büyümesinin sadece faizden mi yoksa sahadaki "Müşteri Edinimi" (Acquisition) başarısından mı kaynaklandığını ayrıştırır.
- **WR Rate / Ratio (Win Rate - Kazanma Oranı):** Bankanın verdiği faiz tekliflerinin, başarılı bir mevduat açılışına dönüşme oranıdır. Ayrıca "WR Ratio" olarak bizim faizimizin piyasa ortalamasına oranı (`Bizim Faiz / Piyasa Ortalama`) üzerinden de fiyatlama verimliliği ölçülür.
- **TVC (Reklam/Kampanya Etkisi):** Televizyon ve medya reklamlarının (Commercials) yayında olduğu haftaları (1/0) gösterir. Pazarlama harcamalarının (Marketing Spend) girişi ne kadar artırdığını ölçen "Lift Etkisi" değişkenidir.
- **Full Workday (Takvim Etkisi):** Haftadaki tam mesai günü sayısıdır. Resmi tatillerin (Bayram vb.) veya yarım günlerin EFT/Havale trafiği üzerindeki "işlem hacmi daraltıcı" etkisini standardize etmek için kullanılır.
- **Interest Rate Offered (Sunulan Faiz):** Bankanın o hafta Turuncu Hoşgeldin paketi kapsamında müşteriye sunduğu faiz oranıdır. Modelin bu faiz ile `w/TLREF` (maliyet) arasındaki dengeyi bulmasını sağlar.
- **Lagged Turuncu Faizi / Hacmi:** Geçmiş haftalarda uygulanan faiz oranları ve stok hacim bilgisidir. Müşterinin hafıza etkisini ve büyüme oranlarının hangi baz seviye üzerinden gerçekleştiğini normalize etmek için modele girer.

## 5.3. Makroekonomik ve Piyasa Göstergeleri (External Market Signals)

FIRAST ve Updated Base Model'in ötesinde, piyasanın genel tansiyonunu ve "alternatif para kaçış rotalarını" izlemek için tanımlanmış stratejik göstergelerdir:

- **Google Trends (Arama Hacmi):** "En yüksek mevduat faizi" veya "Bankalar ne veriyor?" gibi anahtar kelimelerin haftalık aranma hacmidir (Search Volume Index). Müşterinin "Faiz Arama İştahını" (Churn niyetini) sentiment analizinden çok daha net ve sayısal olarak gösteren bir öncü göstergedir.
- **CDS Primi (5 Yıllık):** Türkiye'nin risk primini temsil eder. Yükseldiğinde (Örn: >300 baz puan) tüm faizler yukarı itilir ve kriz anlarının en net habercisidir.
- **VIX Index (Korku Endeksi):** Küresel piyasalardaki oynaklık endeksidir. VIX > 30 olduğunda (Savaş/Kriz), gelişmekte olan piyasalardan güvenli limanlara (Dolar/Altın) kaçış başlar.
- **Kripto Para Hacmi (USDT/TRY):** Klasik Dolarizasyon verisi haftalık gelirken, kripto borsalarındaki 7/24 USDT/TRY hacmi, sermaye kaçış niyetini anlık (Real-time) gösteren bir erken uyarı sinyalidir.
- **Gram Altın:** Geleneksel Türk mevduat yatırımcısının en güçlü alternatifidir. Altın fiyatlarındaki hızlı yükselişler, TL mevduattan çözülmeyi tetikleyebilir.
- **XBANK (Bankacılık Endeksi):** Borsa İstanbul Bankacılık Endeksi, yatırımcının risk iştahını (Risk-on/Risk-off) gösterir. Borsa rallilerinde mevduat çıkışı (Substitution Effect) gözlemlenebilir.
- **Devlet Tahvili Getirileri (2Y & 10Y):** Risksiz getiri oranı (Risk-free Rate) olarak kabul edilir. Mevduat faizinin teorik olarak bu oranın üzerinde olması beklenir ve piyasanın uzun vadeli beklentisini belirler.
- **Net Rezerv Değişimi:** Merkez Bankası rezervlerindeki değişim, piyasadaki döviz likiditesi ve güven endeksi için kritik bir göstergedir.
- **Tüketici Kredi Faizleri:** İhtiyaç kredisi faizleri, bankanın mevduata verebileceği "Tavan Faizi" sınırlar. Kredi/Mevduat makası karlılık için kritiktir.
- **Kur Volatilitesi (Forex Volatility):** Döviz kurlarındaki dalgalanma/oynaklık seviyesidir. Sadece kurun seviyesi (Level) değil, değişimin hızı da mevduattan kaçış (DTH'a geçiş) kararını tetikler.

## 5.4. Banka İçi ve Portföy Yapısı (Internal Micro-Dynamics)

Sadece piyasaya değil, "içeriye" bakarak portföyün yapısal kırılganlığını ölçen parametrelerdir:

- **Total Digital Traffic (Dijital Trafik):** Banka genelindeki toplam "Login" sayısındaki ani dalgalanmalar izlenir. Piyasa hareketlendiğinde kitlesel trafik artar, bu da potansiyel bir para çıkışının (Mass Outflow) en net öncü göstergesidir (Leading Indicator).
- **Avg. Ticket Size (Ortalama Bakiye):** Bankadaki paranın "Büyük" veya "Küçük" yatırımcıda toplanma oranıdır (Elasticity). Paranın %80'i 1M+ tutarlardaysa faiz esnekliği daha yüksek modellenir.
- **Vintage Mix (Portföy Yaşı):** Portföyün ne kadarının "Yeni/Taze" (Hassas para), ne kadarının "Eski/Yerleşik" (Ataletli para) olduğunu gösterir. Herkese tek fiyat uygulansa da, bu karışım (Mix) toplam hacmin fiyata vereceği tepkiyi belirler.
- **Limit Değişim Takvimi:** Banka içi alt limit tutarlarındaki değişim dönemleri (Yılda ~2 kez). Modelin "Intercept Shift" etkisini (Örn: Dönem 1=0, Dönem 2=1, Dönem 3=2) anlamasını sağlayarak hacimdeki teknik düşüşleri doğru yönetmesini sağlar.
- **OSA FTP (Transfer Fiyatlaması):** Banka içi Fon Transfer Fiyatlaması (Fund Transfer Pricing). Mevduatın banka için marjinal değerini ve toplama iştahını belirleyen içsel maliyet parametresidir.
- **Scaling & Data Protocol:** Her iki modelde de faiz oranları (%50) ile hacim (Milyarlar) arasındaki uçurumu kapatmak için tüm veriler **Standart Scaler (Mean=0, Std=1)** ile ölçeklendirilir. Ayrıca verilerin durağanlığını (Stationarity) sağlamak için mutlak değerler yerine haftalık değişimler (Delta t - t-1) kullanılır.

## 5.5. Takvim ve Mevsimsellik (Calendar & Seasonality)

Fiyat dışı "Doğal Akışları" modellemek için kullanılan takvim değişkenleridir:

- **Payday Effect (Maaş Döngüsü):** Ayın 1'i ve 15'i gibi maaş giriş günlerinde faizden bağımsız hacim artışları yaşanır.
- **Tax Season (Vergi Dönemleri):** Şubat, Mayıs, Ağustos gibi vergi ödeme aylarında piyasadan yüklü miktarda TL çıkışı (Likidite Sıkışıklığı) olur.
- **Holiday Cash Demand (Bayram Etkisi):** Bayram tatilleri öncesinde (Arefe günü) ATM nakit çekim talebi patlar ve mevduat hacmi geçici düşüş yaşar.
- **IPO Calendar (Halka Arz Fırtınası):** Büyük ölçekli halka arzların olduğu haftalarda, tasarruf sahipleri mevduat hesaplarını bozup borsaya nakit çıkışı yapar.
- **School/Vacation (Mevsimsel Harcama):** Eylül (Okul açılışı) ve Haziran (Tatil) dönemlerindeki harcama artışlarının yarattığı çıkış etkisidir.
- **Season (Mevsim - Çeyreklik Döngü):** İçinde bulunulan mevsimi gösteren (Kış, İlkbahar, Yaz, Sonbahar) kategorik değişken. Turizm harcamaları, ısınma giderleri veya hasat zamanı gibi nakit akışını etkileyen makro döngüleri temsil eder.

## 5.6. Alternatif Davranışsal Göstergeler (Behavioral Proxies)

Literatürdeki davranışsal finans teorilerinin (Behavioral Economics), bankamızın kredi kartı harcama verileriyle cinsiyetten bağımsız ve etik kurallara uygun (**EU AI Act Compliant**) şekilde matematikselleştirilmesidir. Amaç, müşterinin finansal stres seviyesini "sözlü beyanından" değil, "cüzdan hareketinden" anlamaktır.

- **Ertelemeli Harcama Endeksi (Discretionary Spending Proxy):** Alan Greenspan'in "Men's Underwear Index" teorisinin modernize edilmiş halidir. TCMB ve Banka içi Giyim/Aksesuar harcamalarından takip edilir. Giyim, gıdanın aksine "Ertelenebilir" (Postponable) bir ihtiyaçtır. Ekonomik belirsizlik anında hanehalkı ilk olarak giyim alışverişini keser. Bu kalemde, enflasyondan arındırılmış reel bir düşüş başlaması (`Reel_Giyim_Hacmi = Giyim_Harcaması / Giyim_Enflasyonu`), müşterinin **"Nakit Koruma (Cash Hoarding)"** moduna geçtiğinin en erken sinyalidir.
- **Küçük Lüksler Endeksi (The Lipstick Effect Proxy):** Ekonomi daralırken tüketicilerin büyük lükslerden (Ev, Araba) vazgeçip, kendilerini iyi hissettirecek ulaşılabilir lükslere (Kozmetik) yönelmesi teorisidir. Kriz dönemlerinde bu kalemde harcama düşmez, aksine artar (Substitution Effect). Eğer genel harcama düşerken Kozmetik harcaması artıyorsa, bu **"Stagflasyon"** (Durgunluk içinde enflasyon) belirtisidir. Bankacılık verilerinde ölçülemeyen ve cinsiyetçi risk taşıyan "Hemline Index" (Etek Boyu) yerine, literatürde (Estee Lauder) kanıtlanmış Kozmetik verisi tercih edilmiştir.
- **Refah ve Sosyalleşme Endeksi (Service Economy Proxy):** Restoran ve Yemek Hizmetleri harcamalarından izlenir. İnsanların dışarıda yemek yeme sıklığı, halkın **"Harcanabilir Gelirini" (Disposable Income)** ve geleceğe dair güvenini gösterir. Fiyat artışından değil, talep gücünden kaynaklanan artışı ayrıştırmak için `Reel_Hizmet_Hacmi = (Restoran_Harcaması / Gıda_Hizmet_Enflasyonu)` formülü kullanılır.

## 5.7. İleri Seviye ve Türetilmiş Değişkenler (Advanced & Derived Features)

Gelecek fazlarda (Challenger Model) kullanılmak üzere tanımlanmış, "Comprehensive Overview" dokümanlarında yer alan ileri seviye matematiksel ve regülatif değişkenlerdir:

- **Zorunlu Karşılıklar (Reserve Requirements):** Mevduatın bankaya olan maliyetini (Cost of Funding) doğrudan etkileyen regülasyon parametresidir. TCMB kararlarına göre güncellenir.
- **Piyasa Rejimi Göstergesi (4-Quadrant Model):** Enflasyon ve Faizin durumuna göre piyasayı 4 ana rejimden birine atayan sanal değişkendir. Modelin katsayılarını rejime göre otomatik ayarlamasını (Regime Switching) sağlar.
- **Market Stress (Volatilite Endeksi):** Piyasada sadece yönün değil, "huzursuzluğun" da ölçüldüğü içsel bir metriktir. Hacim değişimlerinin standart sapması (`Rolling Std Dev`) üzerinden hesaplanır.
- **Max Competitor Rate (Piyasa Tavanı):** Sektör ortalaması (Benchmark) yerine, piyasadaki en agresif rakibin verdiği "Tavan Faiz" oranını temsil eder. Rekabetin en uç noktasını ölçer.
- **Interaction Terms (Etkileşimler):** `w/TLREF * EXP_Spread` gibi, bir değişkenin etkisinin diğerine bağlı olduğu durumları (faiz seviyesine göre değişen hassasiyet) modellemek için kullanılan çapraz çarpım değişkenleridir.
- **EMA (Exponential Moving Average):** Yakın geçmişe daha yüksek ağırlık veren "Üstel Hareketli Ortalama" (`span=3`). Modelin trend değişimlerine daha hızlı (Low Latency) tepki vermesini sağlar.
- **Momentum Hızlanması (Acceleration):** Trendin sadece hızını değil, ivmesini (`NET_lag1 - NET_lag2`) ölçer. Trendin doygunluk noktasına (Saturation) ulaşıp ulaşmadığını öngörür.
- **Lagged Interest Rates (Gecikmeli Faizler):** Müşterinin faiz değişimini algılama süresini modellemek için `t-1`, `t-2` ve `t-4` gecikmeli faiz oranları kullanılır. "Geçen ay yapılan artışın bugünkü etkisi"ni ölçer.
- **Stopaj Değişimi (Tax Regime):** Mevduat stopaj oranlarındaki ani değişimler (Örn: %5 -> %7.5). Brüt faiz aynı kalsa bile, müşterinin cebine giren "Net Getiri" azaldığı için ani tepkiler oluşur. Bu bir "Regülasyon Şoku" (Regulatory Shock) değişkenidir.

## 5.8. Operasyonel Karar Destek ve Stratejik Göstergeler (Workflow Support)

Net Akış tahmini yapıldıktan sonra, 4. Bölümde detaylandırılan **"Bakiye Projeksiyonu"** ve **"Gap Analizi"** süreçlerini "aksiyona" dönüştürmek için kullanılan stratejik göstergelerdir. Gereksiz tekrarlardan arındırılarak sadece operasyonel kararı doğrudan etkileyen kalemlere odaklanılmıştır:

- **Fiyat Esneklik Katsayısı (Price Elasticity Index):** Karar matrisindeki en kritik değişkendir. Faizi 25 bps artırmanın hacmi ne kadar tetikleyeceği bu "Dinamik Katsayı" ile hesaplanır. Optimal faiz miktarının matematiksel temelidir.
- **Vade Dönüş ve Yenileme Oranı (Maturity & Rollover Rate):** Sadece "yeni giriş" değil, vadesi dolan paranın ne kadarının bankada kaldığı (Rollover) takip edilir. 4. Bölümdeki projeksiyonun "gerçekçiliğini" ölçen en temel metriktir.
- **Vade Dönüş ve Yenileme Oranı (Maturity & Rollover Rate):** Sadece "yeni giriş" değil, vadesi dolan paranın ne kadarının bankada kaldığı (Rollover) takip edilir. 4. Bölümdeki projeksiyonun "gerçekçiliğini" ölçen en temel metriği.
- **Segment Mix ve LTV Filtresi:** Portföyün segment yapısı ve müşteri kârlılığıdır. Faiz artışı kararı verilirken, hangi segmentin kaçırılmaması gerektiği veya hangi "maliyetli" paranın (low LTV) gözden çıkarılabileceği süzgecini oluşturur.
- **Likidite ve Sermaye Kısıtları (LCR/NSFR/İç Likidite):** Bankanın yasal ve içsel likidite rasyolarıdır. 120B hedefi tutsa bile, regülasyonun veya bilançonun o anki TL ihtiyacı, model önerisi üzerinde bir "Hard Constraint" (Sert Kısıt) oluşturur.
- **Pazar Payı ve Rekabet Hızı:** Sektör büyüme hızı ve rakiplerin tepki verme süresidir. Aksiyonun pazar payını korumaya mı yoksa pazar kapmaya mı yönelik olduğunu ve hamlenin ne kadar "zamanlama avantajı" (First Mover) yaratacağını ölçer.
- **Gap Velocity ve Kritik Bakiye Eşiği:** Hedef (120B) ile bakiye arasındaki farkın kapanma ivmesidir. Eğer ivme negatifse (fark açılıyorsa) ve "Safety Floor" seviyesine yaklaşılıyorsa, sistem otomatik olarak "Acil Durum (Best Effort)" moduna geçer.
- **Aksiyon ve Karar Koridoru (Interest Rate Corridor):** Banka yönetiminin o dönem için izin verdiği minimum ve maksimum faiz sınırlarıdır. Modelin önerdiği "Optimal Faiz" her zaman bu koridor içine (Compliance check) sığdırılarak sunulur.
- **Cannibalization & Budget Check:** Yapılan faiz artışının bütçe içindeki payı ve bankanın kendi vadeli mevduatlarından (Term Deposit) Turuncu'ya kaydırdığı "Maliyetli İç Akış" kontrolüdür. Kararın kârlılığını nihai olarak onaylar.

# 6. DASHBOARD VE KARAR DESTEK ARAYÜZÜ

Modelin çıktısı sadece bir rakam değil, yönetimin "karar verme kaslarını" güçlendiren ve Bölüm 4'teki iş akışını otomatize eden stratejik bir **"Stratejik Karar Kokpiti"** arayüzüdür.

## 6.1. Yönetici Özeti ve Performans Köprüsü

Yönetimin "Hedefin neresindeyiz?" ve "Neden oradayız?" sorularını tek bakışta yanıtlayan görsel analizdir:

- **KPI Kartları:** Anlık Bakiye, Hedef Gerçekleşme (%), Ağırlıklı Ortalama Mevduat Maliyeti (AoFF vs Biz) ve Net Flow (%).
- **Hacim Köprüsü (Waterfall):** Bakiye değişimini bileşenlerine ayırır (Gelen Fon, Giden Fon, Faiz Girişi, Churn).
- **Segment Dinamiği:** Mass, Affluent ve Private segmentlerinin akışlarının ayrı ayrı izlendiği, esneklik (elasticity) değişimlerinin takip edildiği paneldir.

## 6.2. Stratejik Duyarlılık ve "What-If" Simülatörü

Bölüm 4.2'deki karar matrisinin interaktif versiyonudur. Tek bir faiz oranı yerine, karar vericilere farklı faiz seviyelerinde bankanın hedefe ne kadar yaklaşacağını ve maliyetin nasıl değişeceğini simüle eder:

- **Optimal Faiz Önerisi:** Hedefi tutturan **en düşük** maliyetli faiz oranı sistem tarafından otomatik işaretlenir.
- **Spread & Kar Etkisi:** Seçilen her faiz oranının bankanın net kâr marjı (NIM) üzerindeki projeksiyonu gösterilir.

## 6.3. Erken Uyarı ve Risk Isı Haritası (Risk Watch)

Bölüm 5.8'deki operasyonel parametrelerin görselleştirildiği risk yönetim panelidir:

- **Leading Indicator Watch:** Google Trends (arama hacmi), Kripto Hacmi ve Davranışsal Finans sinyallerindeki (Lipstick Effect vb.) ani sapmalar "Trafik Lambası" (Kırmızı/Sarı/Yeşil) mantığıyla sunulur.
- **Bakiye Güvenlik Tamponu (Safety Floor):** Bakiyenin hard-limit eşiğine ne kadar yakın olduğu ve modelin "RMSE payı" hesaba katılarak oluşturulan "Korunaklı Hedef" çizgisi.
- **Vade Dönüş Zirveleri:** Gelecek haftalardaki blok çıkış riskleri takvimi.

## 6.4. Karar Destek Notu (Auto-Generated Executive Memo)

Haftalık komite için sistem tarafından otomatik üretilen teknik nottur. "Neden bu aksiyonu almalıyız?" sorusuna Bölüm 5'teki verilerle (Örn: "Momentum düşüyor (NET_lag1 negatif)" veya "CDS yükseliyor (>300)") kanıta dayalı yanıt sunar.

# 7. SONUÇ VE YÖNETİCİ ÖZETİ

Bu proje ile bankamız, reaktif piyasa takipçiliğinden, proaktif ve veri odaklı bir **"Stratejik Bilanço Yönetimi"** modeline geçiş yapmıştır.

- **Matematiksel Güven:** Haftalık Dinamik Retraining stratejisi sayesinde model hataları **%23** oranında düşürülmüş, pazar hareketlerinin %80'i açıklanabilir (R²=0.80) hale gelmiştir.
- **Kurumsal Hafıza ve Çeviklik:** Karar alma süreci kişilerin uzmanlığından (Key Person Risk) çıkarılıp, verinin objektifliğine taşınmış; bankaya her hafta kendini güncelleyen yaşayan bir **"Kurumsal Zeka"** kazandırılmıştır.
- **Hedef Odaklılık:** Faiz artık bir maliyet kalemi değil, **120 Milyar TL** stratejik hedefine ulaşmak için kullanılan hassas bir "Navigasyon Aracı"dır.
- **Gelecek Vizyonu:** Modele eklenen Davranışsal Finans (Behavioral Proxies) ve Alternatif Veri setleri ile bankamız, piyasadaki psikolojik eşikleri önceden tespit eden bir **"Piyasa Tahminleme ve Optimizasyon Merkezi"** konumuna yükselmiştir.
