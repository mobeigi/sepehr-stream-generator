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
* Each Sepehr m3u link is generated by a REST endpoint
* Returned link contains a **s** (secret) parameter and **t** (time) parameter
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
* Jam-e-Jam 1
* Jam-e-Jam 2
* Jam-e-Jam 3
* IRIB 1
* IRIB 2
* IRIB 3
* IRIB 4
* IRIB 5
* IRIB IRINN
* IRIB Amouzesh
* IRIB Quran
* IRIB Mostanad
* IRIB Namayesh
* IRIB Ofogh
* IRIB Varzesh
* IRIB Pouya
* IRIB Salamat
* IRIB Nasim
* IRIB Tamasha
* IRIB Omid
* IRIB Shoma
* IRIB Iran Kala
* IRIB Javaneh
* IRIB Nama
* IRIB Jam
* IRIB Shiran
* IRIB Sepehr
* IRIB Nava
* IRIB Thaqalein
* IRIB Labbayk

## Contributions
Contributions are always welcome!
Just make a [pull request](../../pulls).

## Licence
GNU General Public License v3.0