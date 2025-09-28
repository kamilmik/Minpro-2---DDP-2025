# Mini Project 2 DDP-2025

# Profil

Nama : Muhammad Ibrahim Kamil \
NIM : 2509116012 \
Sistem Informasi A'2025 

# Flowchart
berikut adalah Flowchart dari program :
<img width="1395" height="1300" alt="MINPRO2 drawio" src="https://github.com/user-attachments/assets/e1cb0285-963b-4567-9ccb-ae6ec159746c" />


# Alur Program
*Login :* \
Pada halaman awal, program akan menampilkan login, user diminta untuk menginput Usernam dan Password(yang dihide menggunakan library pwinput). setelah diinput, program akan menentukan apakah yang login adalah manager atau karyawan.

- tampilan awal login dan jika user benar input akun : \
  <img width="428" height="192" alt="image" src="https://github.com/user-attachments/assets/8c9c2342-d486-4493-b9a2-c7602fd36ed5" />\
- tampilan jika user salah input username/password : \
  <img width="427" height="177" alt="image" src="https://github.com/user-attachments/assets/f26df628-6d10-4730-8288-51b205715d96" />\

\antara berhasil atau tidak nya login, user diminta menekan enter untuk melanjutkan aksi.

# ROLE MANAGER :
disajikan tampilan menu awal manager yang lebih banyak pilihan dibandingkan login sebagai karyawan, terdapat 5 pilihan.\
<img width="316" height="193" alt="image" src="https://github.com/user-attachments/assets/162f1fba-bfd8-4981-93aa-e76c01e7361f" />\
- lihat produk (READ)
  ketika user memilih input 1 (read) maka program akan mengecek apakah list produk ada, jika iya maka akan ditampilkan :\
  <img width="446" height="241" alt="image" src="https://github.com/user-attachments/assets/a265d76b-4328-49c3-b6eb-4c38fb1312fe" />\
  jika tidak maka program akan memberi info tidak ada produk :\
  <img width="471" height="137" alt="image" src="https://github.com/user-attachments/assets/342df988-a2cc-4148-ba11-a4b3f997567c" />\


- Tambah Produk (ADD)
  ketika user memilih input 2 (Add) maka program akan mengalihkan menu ke menu add, dan user akan menginput nama, modal, dan harga produk baru sesuai yang diinginkan, berikut jika user menginput produk dengan benar: \
  <img width="482" height="210" alt="image" src="https://github.com/user-attachments/assets/b74cf347-d650-462e-a4f2-974cd0baa44a" /> \
  dan jika user mengisi input modal/harga selain angka, program akan memberi tahu kesalahan user dan meminta user menginput ulang dengan value yang benar :\
  <img width="490" height="244" alt="image" src="https://github.com/user-attachments/assets/a4b87b07-ffb3-4eef-904d-1e9ceb6f03e5" />\
 
- Edit Produk (UPDATE)
  user memilih input 3, pada menu update, program akan membaca list tabel dan memberikan informasi tersebut ke user, dan menyuruh user untuk memilih produk mana yang ingin diedit, lalu program akan meminta input baru untuk tiap detail produk yang dipilih(jika diisi kosong maka detail tersebut tidak dirubah) setelah user menginput semua, maka program akan mengganti data lama dengan data baru:\

  <img width="476" height="262" alt="image" src="https://github.com/user-attachments/assets/9308aba5-6b72-4e18-a104-ec8f0ef6fea5" />\

  jika input user benar (dan modal tidak diubah, hanya nama dan harga yang diubah) :\
   <img width="551" height="443" alt="image" src="https://github.com/user-attachments/assets/dc91b1df-a190-44bc-80a2-5442a60a1835" />\
   dan jika input user salah pada modal/harga (tekan enter dan program mengembalikan user ke menu, tanpa jadi mengedit produk) :\
<img width="512" height="399" alt="image" src="https://github.com/user-attachments/assets/88270717-cf5b-43b0-802c-1c6a96a37d03" /> \


- Hapus Produk (DELETE)
  user memilih input 4, pada menu delete, program akan membaca list tabel dan memberikan informasi tersebut ke user, dan menyuruh user untuk memilih produk mana yang ingin dihapus sesuai urutan angka, lalu program akan crosscheck apakah user yakin dengan pilihan menghapus, jika tidak akan kembali ke menu utama, dan jika iya maka program akan menghapus data yang dipilih dari list: \
<img width="490" height="365" alt="image" src="https://github.com/user-attachments/assets/b105ceeb-3899-47a2-bfcf-e47ce2d53c8b" />\

dan jika user salah menginput nomor produk : \
<img width="502" height="302" alt="image" src="https://github.com/user-attachments/assets/849bf4ca-694e-4e19-a7db-ba16e9f91098" />\

- LOGOUT
  jika manager memilih ini, program akan me logout akun manager dan memberi input apakah manager ingin login lagi? jika iya maka program akan mengembalikan ke halaman login dan jika tidak maka program akan berhenti sepenuhnya(akhir program): \
  <img width="413" height="252" alt="image" src="https://github.com/user-attachments/assets/632c7f28-914f-44a1-b83b-f43a9cebc937" />\

- Jika User salah input pilih menu\
  <img width="465" height="255" alt="image" src="https://github.com/user-attachments/assets/834d1fe3-cc49-45bc-a7dd-ede0da4dfd50" />\


# ROLE KARYAWAN
disajikan tampilan menu awal karyawan yang lebih terbatas pilihannya dibandingkan login sebagai manager, terdapat 2 pilihan.\
<img width="340" height="159" alt="image" src="https://github.com/user-attachments/assets/32324f74-068d-4355-9f53-a0d8bdc47748" /> \

- Lihat Produk (READ)
  ketika user memilih input 1 (read) maka program akan mengecek apakah list produk ada, jika iya maka akan ditampilkan :\
  <img width="448" height="244" alt="image" src="https://github.com/user-attachments/assets/f77b73ce-aacc-49fc-98f2-fe42e86a27a8" />\
dan jika tidak maka akan memberi info pada user bahwa tidak ada produk!\

<img width="471" height="137" alt="image" src="https://github.com/user-attachments/assets/0e886e14-c01d-429f-8d27-9b08ad47ba01" />\

-LOGOUT 
  jika karyawan memilih ini, program akan me logout akun karyawan dan memberi input apakah user ingin login lagi? jika iya maka program akan mengembalikan ke halaman login dan jika tidak maka program akan berhenti sepenuhnya(akhir program): \
  <img width="598" height="175" alt="image" src="https://github.com/user-attachments/assets/e7c3c439-dd4c-4b65-8a53-db4f73a4373f" />\

- jika user salah pada input menu \
  <img width="467" height="204" alt="image" src="https://github.com/user-attachments/assets/fc9a49d1-b0e4-421f-9c15-c4ad498336ba" />

# KEYBOARDINTERUPTD
  eror handling keyboard interrupted jika user menekan tombol ctrl + c dimanapun program
  <img width="514" height="140" alt="image" src="https://github.com/user-attachments/assets/b927e7a8-adb6-4fa7-b376-bce3694de931" />

  



