# Algeo02-19031
## Website Search Engine sederhana
> Website Search Engine sederhana mengenai Information Retrieval (IR) atau “Sistem Temu Balik Informasi” dengan model ruang vektor.

## Anggota Kelompok
* Daniel Mario Reynaldi/13519031
* Farhan Nur Hidayat Denira/13519071
* Safiq Faray/13519145

Asisten :

## General Info
Search Engine dibuat dengan menggunakan Python 3 dan Flask.

## Setup
Website dapat dibuka dengan melakukan langkah-langkah berikut ini:
1. Pastikan device/perangkat telah terinstall python 3.
2. Pastikan pip dan virtualenv sudah terinstall pada device, apabila belum, cara install dapat dilihat di https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/ .
3. Lakukan Download atau clone pada project ini.
4. Buka command prompt, lalu change directory ke folder Algeo02-19031.
5. Buat virtual environment dengan nama "venv", pada laptop Windows dapat dilakukan dengan mengetik "virtualenv venv" di cmd, untuk cara lengkap membuat virtual environment dapat dilihat pada link di langkah 2.
6. Aktifkan virtual environment, pada laptop windows ketik ".\env\Scripts\activate", untuk OS lain dapat dilihat pada link di langkah 2.
7. Install flask dengan command "pip install flask", cara lengkap dapat dilihat di https://pypi.org/project/Flask/ .
8. Install flask_wtf dengan command "pip install flask_wtf", cara lengkap dapat dilihat di https://flask-wtf.readthedocs.io/en/stable/install.html
9. Install nltk dan bs4 dengan command "pip install nltk" dan "pip install bs4".
10. Change directory ke folder src, dengan command "cd src".
11. Lakukan export, untuk cmd ketik "set FLASK_APP=main.py", sedangkan untuk UNIX shells, ketik "export FLASK_APP=main.py".
12. Run program dengan command "flask run".
13. Apabila tidak ada error, maka link website lokal dapat dilihat, copy link tersebut ke browser dan search engine akan muncul. NOTE : apabila muncul error "module tertentu not found", maka module dapat diinstall dengan command "pip install module-name".

## Using
1. Upload satu atau bebarapa file html yang sudah disediakan dengan menggunakan tombol upload.
2. Format penamaan file adalah harus sebagai berikut "[title].html", title adalah elemen yang dibatasi tag <title> di file html, tanpa tanda "[]".
3. Masukkan keyword yang ingin dicari pada Search bar, lalu tekan tombol search.
4. Akan muncul list laman website terurut berdasarkan kerelevanan antara website dan search query, serta Term Table.
5. Pilih laman web yang ingin dibaca.

## Features
* Search engine
* Document uploader
* Term Table
* Halaman Perihal
