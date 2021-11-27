<p align="center">
<img src="https://i.imgur.com/rDPxW5y.png" height="110px" width="auto"/>
<br/>
<h3 align="center">Sepehr Stream Generator</h3>
<p align="center">Get latest stream links from Sepehr to produce working m3u file</p>
<h2></h2>
</p>
<br />

<p align="center">
<a href="../../issues"><img src="https://img.shields.io/github/issues/mobeigi/sepehr-stream-generator.svg?style=flat-square" /></a>
<a href="../../pulls"><img src="https://img.shields.io/github/issues-pr/mobeigi/sepehr-stream-generator.svg?style=flat-square" /></a> 
<a href="LICENSE.md"><img src="https://img.shields.io/github/license/mobeigi/sepehr-stream-generator.svg?style=flat-square" /></a>
</p>

## Description
Get latest stream links from Sepehr to produce working m3u file.  
I am using this alongside [Xteve](https://github.com/xteve-project/xTeVe) to get Sepehr live streams into Plex Live TV / DVR.

## Notes
* Each Sepehr M3U link is generated by a REST endpoint
* Returned stream urls contains a **s** (secret) parameter and **t** (time) parameter
  * The secret (s) is some encrypted key that ties the m3u stream link to your IP address. It will only be viewable from the IP which made the initial REST request.
  * It appears as if the time (t) is either the issue epoch or the epoch afterwhich the link will expire.
  * Both parameters are needed and must match for the stream to work.

## Instructions
1. Clone repo on a machine on your local network you intend to watch the stream on  
`git clone git@github.com:mobeigi/sepehr-stream-generator.git`
2. Set up pipenv environment  
`pipenv install`
3. Run the `sepehrstreamgenerator` module  
`pipenv run python -m sepehrstreamgenerator`
5. Check the output folder (`out`) for the created `sepehr.m3u` file
6. Setup a cron job to regenerate the `sepehr.m3u` file every 15 minutes so internal stream links remain valid

## Channel list 
#### 79 channels generated on 27/11/2021
* IRIB 1 (یک)
* IRIB 2 (دو)
* IRIB 3 (سه)
* IRIB 4 (چهار)
* IRIB 5 (پنج)
* IRIB IRINN (خبر)
* IRIB Amouzesh (آموزش)
* IRIB Quran (قرآن)
* IRIB Mostanad (مستند)
* IRIB Namayesh (نمایش)
* IRIB Ofogh (افق)
* IRIB Varzesh (ورزش)
* IRIB Pouya (پویا)
* IRIB Salamat (سلامت)
* IRIB Nasim (نسیم)
* IRIB Iran Kala (ایران کالا)
* IRIB Omid (امید)
* IRIB Tamasha (تماشا)
* IRIB Shoma (شما)
* IRIB Sepehr (سپهر)
* presstv (پرس تی وی)
* alalam (العالم)
* hausatvha (هوسا تی وی)
* IRIB iFilm (آی فیلم فارسی)
* ifilmen (آی فیلم انگلیسی)
* ifilmdari (آی فیلم دری)
* filmarabic (آی فیلم عربی)
* sahar1 (سحر آذری)
* sahar2 (سحر اردو)
* sahar3 (سحر کردی)
* sahar4 (سحر بالکان)
* saharafghan (سحر افغانستان)
* alkosar (الکوثر)
* hispan (هیسپان)
* Jam-e-Jam 1 (Vienna) (جام جم)
* Jam-e-Jam 2 (North America) (جام جم ۲)
* Jam-e-Jam 3 (Asia/Australia) (جام جم ۳)
* abadan (آبادان)
* azarbayjan (آذربایجان غربی)
* sahand (سهند)
* alborz (البرز)
* esfahan (اصفهان)
* sabalan (سبلان)
* ilam (ایلام)
* bushehr (بوشهر)
* jahanbin (جهان بین)
* khorasanjonoobi (خراسان جنوبی)
* khorasanrazavi (خراسان رضوی)
* khorasanshomali (خراسان شمالی - اترک)
* khalijefars (خلیج فارس)
* khoozestan (خوزستان)
* eshragh (اشراق)
* semnan (سمنان)
* hamoon (هامون)
* fars (فارس)
* qazvin (قزوین)
* noor (نور)
* kordestan (کردستان)
* kerman (کرمان)
* kermanshah (کرمانشاه)
* dena (دنا)
* kish (کیش)
* golestan (گلستان)
* baran (باران)
* aflak (افلاک)
* taban (تابان)
* mazandaran (مازندران)
* aftab (آفتاب)
* mahabad (مهاباد)
* hamedan (همدان)
* IRIB Jam (جام)
* labbaik (لبیک)
* hausatvra (رادیو هوسا)
* IRIB Habib TV (حبیب)
* IRIB Javaneh (جوانه)
* ara (آرا)
* IRIB Nama (نما)
* IRIB Nava (نوا)
* bazarmohtava (ایام)

## Contributions
Contributions are always welcome!
Just make a [pull request](../../pulls).

## Licence
GNU General Public License v3.0
