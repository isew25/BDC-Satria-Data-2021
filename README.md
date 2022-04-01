# BDC - Satria Data 2021

Tim : 

<img src="./assets/LogoUSD.png" width="100">


Universitas Sanata Dharma Yogyakarta | `SD20210000128`


|     |     |
| --- | --- |
| Ignatius Sarwo Edhi Wiyoto   | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ignatius-sarwo-edhi-wiyoto-168058197/) |
| Ferdinandus Steven Millicent | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/fstevenm/) |
| Albert Ricky Setiawan        | [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/albert-setiawan-440a92138/) |


<br/>

Repository ini digunakan untuk merekam kegiatan lomba Big Data Challege - Satria Data 2021 yang diikuti oleh tim dari program studi Matematika Universitas Sanata Dharma Yogyakarta. Tim berhasil memperoleh peringkat ketiga akurasi terbaik untuk model jenis kelamin. 

<img src="./assets/klasemen.png" width="900">

## Task
Memprediksi Jenis Kelamin dan Usia seseorang dari foto. Pada lomba ini tidak diperkenankan menggunakan transfer learning, penggunaan arsitektur model pada https://keras.io/api/applications/ diperbolehkan tetapi harus di set `weights=None`.

## [Notebook](./notebook)

Beberapa notebook yang kami gunakan untuk mengerjakan challenge.

1. `[STARTER] BDC - 2021` : Starter notebook untuk mengerjakan challenge pertama dalam `BDC - Satria Data 2021`.
2. `[PREPROCESS] BDC - 2021` : Notebook untuk melakukan preprocessing terhadap data gambar.
3. `[CLUSTERING] BDC - 2021` : Notebook untuk melakukan eksperimen mengcluster gambar dengan tujuan untuk memperoleh insight.
4. `[GENDER] BDC - 2021` : Final notebook untuk challenge pertama yaitu gender detection.
5. `[AGE] BDC - 2021` : Final notebook untuk challenge kedua yaitu age detection.

## Preprocessing
Data yang diperoleh Melakukan preprocessing data gambar yang akan dilatih kedalam model.

1. Crop + Rotate
    <img src="./assets/rotate.png" width="900">
3. Select
    <img src="./assets/select.png" width="900">

## Augmentasi
<img src="./assets/augmentasi.png" width="900">


## Deployment
<img src="./assets/image72.gif" width="900">
