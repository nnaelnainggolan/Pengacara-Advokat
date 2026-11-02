# ABR & AML Law Firm - Situs Statis (tanpa database & login admin)

Isi: HTML + CSS + JavaScript biasa. Siap di-deploy ke Vercel (atau hosting statis mana pun).

## Deploy ke Vercel
Cara A - lewat GitHub (disarankan)
1. Buat repository GitHub, unggah SELURUH isi folder ini (index.html harus di root repo).
2. vercel.com -> Add New -> Project -> pilih repo.
3. Framework Preset: "Other". Build Command & Output Directory: kosongkan. Klik Deploy.

Cara B - lewat CLI
   npm i -g vercel
   vercel --prod        (jalankan di folder ini)

## Pasang domain & SEO (penting)
1. Beli domain (mis. abramllawfirm.com), tambahkan di Vercel: Project -> Settings -> Domains.
2. Buka build.py, ubah SITE_URL ke domain asli, lalu jalankan:  python build.py
   (memperbarui canonical, sitemap.xml, robots.txt, dan data terstruktur). Deploy ulang.
3. Google Search Console: tambahkan domain, kirim https://DOMAIN/sitemap.xml, lalu "Minta pengindeksan" untuk halaman utama.
4. Buat Google Business Profile (kategori Pengacara / Firma hukum) dengan alamat yang sama persis dengan di situs.
5. Pastikan nama, alamat, dan telepon sama di situs, Google Maps, dan Instagram.

## Mengubah isi
Edit data di bagian atas build.py (alamat, telepon, tim, sertifikat, galeri, FAQ, artikel), lalu:
   python build.py        (butuh Python + paket Pillow:  pip install pillow)
Foto/sertifikat baru: taruh di assets/team, assets/certificates, assets/gallery, lalu daftarkan di build.py.
Tanpa Python: edit langsung index.html / file lain secara manual.

## Pratinjau lokal
   Cukup klik dua kali index.html (semua tautan memakai .html sehingga jalan tanpa server).

## Periksa sebelum tayang
- Nomor WhatsApp/telepon: ditafsirkan dari "1081264824151" menjadi 0812-6482-4151 (ubah PHONE & WA di build.py).
- Email Aknes (.con) dan IG "sleepymonic" tidak ditampilkan.
- Watermark CamScanner pada 2 sertifikat 2019; izin foto "kepolisian" dan foto lain.
- Judul "Best Lawyer" pada sertifikat: perhatikan batasan promosi dalam kode etik advokat.
- Formulir: tidak ada server. Pesan dikirim lewat WhatsApp atau email (mailto) atas pilihan pengunjung.

## Logo & ikon tab
- Logo header/footer: assets/logo.png (latar transparan).
- Ikon tab browser: favicon.ico (di root) + assets/favicon-*.png, assets/apple-touch-icon.png.
- Untuk mengganti logo: ganti file-file di atas dengan nama yang sama, lalu deploy ulang.
