# -*- coding: utf-8 -*-
"""
Generator situs statis ABR & AML Law Firm.
Ubah data di bagian ATAS file ini, lalu jalankan:  python build.py
Hasil: index.html, artikel/, tim/, kebijakan-privasi.html, 404.html, sitemap.xml, robots.txt
"""
import html, json, os, datetime
from PIL import Image

# ===================== DATA (ubah di sini) =====================
SITE_URL = "https://abramllawfirm.vercel.app"   # GANTI dengan domain asli, lalu jalankan ulang build.py
NAME     = "ABR & AML Law Firm"
BRAND    = "ABR & AML"
TAGLINE  = "Your Trusted Legal Partner"
ADDRESS  = "Jl. Pendidikan, Link. Pelopor No. 01, RT 001/RW 003, Kelurahan Karundang, Kecamatan Cipocok Jaya, Kota Serang, Banten"
STREET   = "Jl. Pendidikan, Link. Pelopor No. 01, RT 001/RW 003, Kelurahan Karundang, Kecamatan Cipocok Jaya"
EMAIL    = "aribintaralawyer@gmail.com"
PHONE    = "+62 812-6482-4151"       # PERIKSA (ditafsirkan dari 1081264824151)
WA       = "6281264824151"           # PERIKSA
HOURS    = "24 jam"
MAP_URL  = "https://maps.app.goo.gl/Sx3TwVSirpcqDvvh8?g_st=ic"
IG       = ["aribintaralawyeroficial", "amlp_lawfirm"]

TITLE_HOME = "Pengacara & Advokat di Serang, Banten | ABR & AML Law Firm"
DESC_HOME  = "Pengacara dan advokat di Kota Serang, Banten: hukum pidana, perdata, bisnis, ketenagakerjaan, keluarga. Layanan 24 jam. Jl. Pendidikan, Karundang, Cipocok Jaya."

ABOUT = [
 "ABR & AML Law Firm merupakan firma hukum yang berkomitmen untuk memberikan layanan hukum yang profesional, berintegritas, dan berorientasi pada perlindungan hak serta kepentingan klien. Kami hadir sebagai mitra hukum bagi individu, pelaku usaha, perusahaan, dan institusi dalam menghadapi berbagai persoalan hukum secara tepat, strategis, dan bertanggung jawab.",
 "Dengan pendekatan yang mengutamakan ketelitian, analisis hukum yang komprehensif, serta pemahaman terhadap kebutuhan setiap klien, ABR & AML Law Firm menyediakan layanan hukum melalui jalur litigasi maupun nonlitigasi. Kami percaya bahwa setiap permasalahan hukum memerlukan penanganan yang cermat, strategi yang terukur, dan solusi yang berlandaskan peraturan perundang-undangan yang berlaku.",
 "Bagi kami, kepercayaan merupakan fondasi utama dalam hubungan profesional dengan klien. Oleh karena itu, kami senantiasa menjunjung tinggi integritas, kerahasiaan, etika profesi, dan kualitas pelayanan dalam setiap penanganan perkara.",
 "ABR & AML Law Firm berupaya menjadi mitra hukum yang dapat diandalkan dalam memberikan pendampingan, perlindungan, serta solusi hukum yang sesuai dengan kebutuhan klien.",
]
ABOUT_EN = [
 "ABR & AML Law Firm is a law firm committed to providing professional, high-integrity legal services focused on protecting clients' rights and interests. We serve as a legal partner for individuals, business owners, companies, and institutions in addressing various legal matters accurately, strategically, and responsibly.",
 "With an approach that prioritizes thoroughness, comprehensive legal analysis, and an understanding of each client's needs, ABR & AML Law Firm provides legal services through both litigation and non-litigation channels. We believe every legal issue requires careful handling, a measured strategy, and a solution grounded in prevailing laws and regulations.",
 "For us, trust is the foundation of every professional relationship with our clients. We therefore uphold integrity, confidentiality, professional ethics, and quality of service in every matter we handle.",
 "ABR & AML Law Firm strives to be a reliable legal partner, providing representation, protection, and legal solutions suited to each client's needs.",
]
VISION = "Menjadi firma hukum yang profesional, berintegritas, dan terpercaya dengan mengedepankan keadilan, kepastian hukum, serta perlindungan kepentingan klien melalui layanan hukum yang berkualitas, strategis, dan berorientasi pada solusi."
MISSION = [
 "Memberikan layanan hukum yang profesional, berkualitas, dan berorientasi pada solusi.",
 "Menjunjung tinggi integritas, etika profesi, dan kerahasiaan klien.",
 "Melindungi hak dan kepentingan klien berdasarkan hukum yang berlaku.",
 "Mengupayakan penyelesaian permasalahan hukum secara efektif dan strategis.",
 "Membangun kepercayaan melalui pelayanan yang transparan, bertanggung jawab, dan berintegritas.",
]

VISION_EN = "To be a professional, honest, and trusted law firm that upholds justice, legal certainty, and the protection of client interests through quality, strategic, solution-oriented legal services."
# (judul singkat ID, judul EN, teks EN) - urutan sama dengan MISSION
MISSION_META = [
 ("Layanan profesional","Professional service","Provide professional, high-quality, solution-oriented legal services."),
 ("Integritas & kerahasiaan","Integrity & confidentiality","Uphold integrity, professional ethics, and client confidentiality."),
 ("Perlindungan hak","Protecting rights","Protect clients' rights and interests under applicable law."),
 ("Penyelesaian strategis","Strategic resolution","Pursue effective and strategic resolution of legal matters."),
 ("Kepercayaan klien","Client trust","Build trust through transparent, accountable, and honest service."),
]

# (slug, ikon, id[judul, ringkasan, [butir]], en[judul, ringkasan, [butir]])
SERVICES = [
 ("hukum-pidana","scale",["Hukum Pidana","Pendampingan sejak pemeriksaan awal hingga persidangan.",["Pendampingan saat pemeriksaan","Penyusunan pembelaan","Kehadiran di persidangan"]],["Criminal Law","Representation from the first examination through trial.",["Accompaniment during examination","Preparing the defense","Appearing at trial"]]),
 ("hukum-perdata","doc",["Hukum Perdata","Kajian sengketa dan langkah penyelesaian perkara perdata.",["Analisis sengketa","Somasi dan negosiasi","Gugatan dan pembelaan"]],["Civil Law","Dispute assessment and resolution of civil matters.",["Dispute analysis","Demand letters and negotiation","Claims and defense"]]),
 ("hukum-bisnis-korporasi-perusahaan","biz",["Hukum Bisnis, Korporasi & Perusahaan","Dukungan hukum untuk kontrak dan kegiatan usaha.",["Penyusunan dan telaah kontrak","Legalitas badan usaha","Penyelesaian sengketa usaha"]],["Business, Corporate & Company Law","Legal support for contracts and business operations.",["Drafting and reviewing contracts","Business entity legality","Business dispute resolution"]]),
 ("hukum-ketenagakerjaan","users",["Hukum Ketenagakerjaan","Pendampingan persoalan hubungan kerja.",["Perjanjian kerja","Perselisihan hubungan industrial","Hak dan kewajiban para pihak"]],["Employment Law","Guidance on employment relationship issues.",["Employment agreements","Industrial disputes","Rights and duties of the parties"]]),
 ("hukum-keluarga-perkawinan","heart",["Hukum Keluarga & Perkawinan","Pendampingan perkara perkawinan dan hubungan keluarga.",["Perkawinan dan perceraian","Hak asuh anak dan nafkah","Harta bersama dan waris"]],["Family & Marriage Law","Guidance on marriage and family matters.",["Marriage and divorce","Child custody and maintenance","Joint property and inheritance"]]),
 ("layanan-hukum-lainnya","chat",["Layanan Hukum Lainnya","Langkah awal memahami persoalan dan menentukan tindak lanjut.",["Pemetaan masalah","Penilaian dokumen awal","Rekomendasi langkah"]],["Other Legal Services","A first step to understand your issue and next actions.",["Mapping the problem","Initial document review","Recommended steps"]]),
]

TEAM = [
 ("ari-bintara","Ari Bintara, M.S., S.H., M.H., CLA"),
 ("aknes-monika","Aknes Monika, S.H., CLA., C.MK"),
 ("mediyanto","Mediyanto, S.H., M.H., CLA., C.Med."),
 ("irfan-gunawan","Irfan Gunawan, S.H., CLA."),
 ("suhanah","Suhanah, S.H., CLA."),
]
# (file, anggota, judul, penerbit, tahun)
CERTS = [
 ("ari-best-lawyer-2019","ari-bintara","Indonesia 50 Best Lawyer Award: Best Lawyer in Service Excellent of the Year","Indonesia 50 Best Lawyer Award",2019),
 ("ari-quality-satisfaction-2019","ari-bintara","Excellent Quality Satisfaction Award: Outstanding Lawyer and Trusted Law Office in Service Satisfaction","Indonesia Development Achievement Foundation",2019),
 ("ari-cla","ari-bintara","Certified Legal Auditor (CLA)","Organisasi Advokat PHIGMA",2026),
 ("ari-penyuluhan-hukum","ari-bintara","Penyuluhan Konsultasi Hukum","Universitas Bina Bangsa (KKM 62 Pulo Panjang)",2026),
 ("ari-webinar-penyiaran","ari-bintara","Webinar Hukum: Aspek Hukum UU No. 32 Tahun 2002 tentang Penyiaran","Beranda Hukum Indonesia",2024),
 ("ari-webinar-waris","ari-bintara","Webinar Hukum: Kedudukan Ahli Waris Pengganti dalam KHI","Beranda Hukum Indonesia",2024),
 ("ari-webinar-kredit","ari-bintara","Webinar Hukum: Teknik Pembuatan Perjanjian Kredit, SKMHT dan APHT","Beranda Hukum Indonesia",2022),
 ("ari-webinar-pbg","ari-bintara","Webinar Hukum: Perizinan PBG sebagai Pengganti IMB","Beranda Hukum Indonesia",2022),
 ("ari-diskusi-kurator","ari-bintara","Diskusi Hukum: Peran Kurator dalam Pengurusan dan Pemberesan Harta Pailit","Beranda Hukum Indonesia",2022),
 ("aknes-cmk","aknes-monika","Certified Mediator Knowledge (C.MK)","Talent Legal Law School",2026),
 ("aknes-materi-diklat","aknes-monika","Pendidikan & Pelatihan Mediator Knowledge (4 JP)","Talent Legal Law School",2026),
 ("suhanah-cla","suhanah","Certified Legal Auditor (CLA)","Organisasi Advokat PHIGMA",2026),
]
# (file, keterangan ID, keterangan EN, object-position)
GALLERY = [
 ("team-courthouse","Di lingkungan Pengadilan Negeri Serang","At Serang District Court","50% 50%"),
 ("kunjungan-pa-serang","Kunjungan ke Pengadilan Agama Serang","Visit to Serang Religious Court",""),
 ("tim-kepolisian","Di lingkungan kepolisian","At a police unit","50% 30%"),
 ("pa-pandeglang","Di Pengadilan Agama Pandeglang","At Pandeglang Religious Court","50% 46%"),
 ("kebersamaan-tim","Kebersamaan tim","Team gathering",""),
]
FAQ = [
 ("Apa yang perlu disiapkan sebelum konsultasi?","Kronologi singkat, identitas para pihak, dan dokumen terkait seperti surat, kontrak, atau bukti pembayaran.","What should I prepare before consulting?","A short timeline, the parties involved, and related documents such as letters, contracts, or payment proof."),
 ("Apakah informasi saya dijaga kerahasiaannya?","Ya. Advokat terikat kewajiban menjaga kerahasiaan informasi klien. Hindari mengirim dokumen sensitif melalui formulir di website.","Is my information kept confidential?","Yes. Advocates are bound to keep client information confidential. Avoid sending sensitive documents through the website form."),
 ("Apakah saya harus datang ke kantor?","Tim akan mengonfirmasi konsultasi tatap muka atau daring setelah pesan awal Anda kami terima.","Do I need to visit the office?","The team will confirm in-person or online consultation after we receive your first message."),
 ("Kapan saya dapat menghubungi kantor?","Layanan kami tersedia 24 jam. Anda dapat mengirim pesan melalui formulir atau WhatsApp.","When can I contact the office?","Our service is available 24 hours. You can send a message through the form or WhatsApp."),
]
# (slug, kategori, slug-kategori, judul, ringkasan, isi, judul EN, ringkasan EN, tanggal)
ARTICLES = [
 ("langkah-awal-saat-menghadapi-persoalan-hukum","Umum","umum","Langkah awal saat menghadapi persoalan hukum","Cara mengumpulkan informasi dan menyiapkan konsultasi yang terarah.",
  "Menghadapi persoalan hukum sering terasa membingungkan. Beberapa langkah awal berikut dapat membantu Anda lebih siap.\n\n1. Tuliskan kronologi singkat: apa yang terjadi, kapan, di mana, dan siapa saja yang terlibat.\n2. Kumpulkan dokumen terkait, seperti surat, kontrak, kuitansi, bukti pembayaran, atau percakapan tertulis.\n3. Simpan bukti asli dan jangan mengubah atau menghapusnya.\n4. Hindari menandatangani dokumen yang belum Anda pahami isinya.\n5. Konsultasikan dengan advokat agar langkah selanjutnya sesuai dengan kondisi Anda.\n\nInformasi ini bersifat umum dan bukan nasihat hukum untuk perkara tertentu.",
  "First steps when facing a legal issue","How to gather information and prepare for a focused consultation.","2026-10-27"),
 ("mengapa-dokumentasi-penting-dalam-sengketa","Perdata","perdata","Mengapa dokumentasi penting dalam sengketa","Menyimpan dokumen dan kronologi secara tertib sejak awal.",
  "Dalam sengketa perdata, dokumen sering menjadi dasar untuk menjelaskan hubungan hukum para pihak.\n\nSimpan perjanjian, bukti pembayaran, korespondensi, dan catatan penting secara tertib. Susun kronologi berdasarkan tanggal agar mudah dipahami. Dokumentasi yang rapi sejak awal membantu proses konsultasi, negosiasi, maupun penyelesaian perkara.\n\nInformasi ini bersifat umum dan bukan nasihat hukum untuk perkara tertentu.",
  "Why documentation matters","Keeping documents and timelines organized from day one.","2026-10-28"),
 ("mengenal-hak-anda-saat-menjalani-pemeriksaan","Pidana","pidana","Mengenal hak Anda saat menjalani pemeriksaan","Informasi umum tentang pendampingan oleh advokat.",
  "Hukum acara pidana di Indonesia mengatur hak seseorang untuk didampingi penasihat hukum selama menjalani pemeriksaan.\n\nJika Anda dipanggil untuk diperiksa, pelajari lebih dahulu alasan pemanggilan, bawa dokumen identitas, dan pertimbangkan untuk berkonsultasi dengan advokat sebelum memberikan keterangan.\n\nInformasi ini bersifat umum dan bukan nasihat hukum untuk perkara tertentu.",
  "Know your rights during an examination","General information on being accompanied by an advocate.","2026-10-29"),
]
ART_IMGS = [("kunjungan-pa-serang","50% 30%"),("tim-kepolisian","50% 35%"),("team-courthouse","50% 57%")]
# ===============================================================

E = lambda s: html.escape(str(s), quote=True)
SLUG2NAME = dict(TEAM)
TODAY = datetime.date.today().isoformat()
ROOT = os.path.dirname(os.path.abspath(__file__))

def w(path, content):
    p = os.path.join(ROOT, path); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(content)

def jd(o): return json.dumps(o, ensure_ascii=False).replace("</", "<\\/")
def cert_caption(c): return f"{c[2]}, {c[4]}"
def is_wide(f):
    z = Image.open(os.path.join(ROOT, "assets/gallery", f + ".jpg")).size
    return z[0] > z[1] * 1.15

ICONS = {
 "pin": '<path d="M12 21s-7-6.2-7-11a7 7 0 0114 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.6"/>',
 "mail": '<rect x="3" y="5" width="18" height="14" rx="2.5"/><path d="M3.5 7.5l8.5 6 8.5-6"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.2 2"/>',
 "phone": '<path d="M5 4h3.5l1.8 4.6-2.3 1.4a11 11 0 005.1 5.1l1.4-2.3L20 14.6V18a2 2 0 01-2.2 2A15.5 15.5 0 014 6.2 2 2 0 015 4z"/>',
 "ig": '<rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r=".9" fill="currentColor" stroke="none"/>',
 "wa": '<path d="M20 11.8A8 8 0 018.2 19L4 20l1.1-4.1A8 8 0 1120 11.8z"/><path d="M9.2 8.6c.2 2.4 2.4 4.6 4.8 4.8l1.2-1.3-1.8-1-.8.7a4 4 0 01-1.9-1.9l.7-.8-1-1.8z"/>',
 "map": '<path d="M9 4L3 6v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/>',
 "copy": '<rect x="9" y="9" width="11" height="11" rx="2"/><path d="M5 15V6a2 2 0 012-2h9"/>',
 "send": '<path d="M21 3L10.5 13.5"/><path d="M21 3l-6.5 18-4-8.5L2 8.5z"/>',
 "user": '<circle cx="12" cy="8" r="4"/><path d="M4.5 20a7.5 7.5 0 0115 0"/>',
 "tag": '<path d="M4 4h8l8 8-8 8-8-8z"/><circle cx="8.5" cy="8.5" r="1.2"/>',
 "msg": '<path d="M4 5h16v11H9l-5 4z"/>',
 "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
 "lock": '<rect x="5" y="11" width="14" height="9" rx="2"/><path d="M8 11V8a4 4 0 018 0v3"/>',
}
def ic(name, cls="ico"): return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{ICONS[name]}</svg>'
ICON_SCALE = '<svg class="ico" viewBox="0 0 24 24"><path d="M12 3v18M6 21h12M4 7h16M4 7l-2.5 7a3 3 0 005 0zM20 7l-2.5 7a3 3 0 005 0z"/></svg>'

def schema(extra=None):
    d = {"@context":"https://schema.org","@type":"LegalService","@id":SITE_URL+"/#organization","name":NAME,
         "description":DESC_HOME,"url":SITE_URL+"/","image":SITE_URL+"/assets/og-image.jpg","logo":SITE_URL+"/assets/logo-icon-512.png",
         "telephone":PHONE,"email":EMAIL,"hasMap":MAP_URL,
         "address":{"@type":"PostalAddress","streetAddress":STREET,"addressLocality":"Kota Serang","addressRegion":"Banten","addressCountry":"ID"},
         "openingHoursSpecification":{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],"opens":"00:00","closes":"23:59"},
         "areaServed":[{"@type":"City","name":"Serang"},{"@type":"AdministrativeArea","name":"Banten"}],
         "knowsAbout":[s[2][0] for s in SERVICES],
         "sameAs":[f"https://instagram.com/{i}" for i in IG]}
    return d

def head(title, desc, path, B, H, extra_ld=None, noindex=False):
    ld = [schema()] + ([extra_ld] if extra_ld else [])
    robots = '<meta name="robots" content="noindex">' if noindex else ""
    return f'''<!doctype html><html lang="id"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#0b1423">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">{robots}
<link rel="canonical" href="{SITE_URL}{path}">
<link rel="icon" href="{B}favicon.ico" sizes="48x48"><link rel="icon" type="image/png" sizes="32x32" href="{B}assets/favicon-32.png"><link rel="icon" type="image/png" sizes="192x192" href="{B}assets/favicon-192.png"><link rel="apple-touch-icon" href="{B}assets/apple-touch-icon.png">
<meta property="og:type" content="website"><meta property="og:locale" content="id_ID"><meta property="og:site_name" content="{E(NAME)}"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{SITE_URL}{path}"><meta property="og:image" content="{SITE_URL}/assets/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="geo.region" content="ID-BT"><meta name="geo.placename" content="Kota Serang">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,wght@6..96,500;6..96,700&family=Instrument+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{B}css/abr.css">
<script type="application/ld+json">{jd(ld)}</script>
</head><body>
<div class="tb"><div class="wrap"><span data-en="Legal guidance grounded in integrity and professionalism">Pendampingan hukum dengan integritas dan profesionalisme</span><span>{E(EMAIL)} &nbsp;|&nbsp; {E(PHONE)}</span></div></div>
<header class="hd"><div class="wrap"><a class="brand" href="{H}#home" aria-label="{E(NAME)}"><img class="logo" src="{B}assets/logo.png" alt="{E(NAME)}" width="171" height="42"></a>
<nav id="nv"><a href="{H}#about" data-en="About">Tentang</a><a href="{H}#team" data-en="Advocates">Tim Advokat</a><a href="{H}#services" data-en="Services">Layanan</a><a href="{H}#process" data-en="Process">Alur</a><a href="{H}#gallery" data-en="Gallery">Galeri</a><a href="{H}#insights" data-en="Insights">Wawasan</a><a href="{H}#contact" data-en="Contact">Kontak</a></nav>
<div class="act"><button class="lang" id="lg" type="button" aria-label="Switch language">EN</button><a class="b g" href="{H}#contact" data-en="Consult now">Konsultasi</a><button class="mb" id="mb" aria-label="Menu" aria-expanded="false">☰</button></div></div><i id="bar"></i></header>
<main>
'''

def foot(B, H, abr=None, priv="kebijakan-privasi.html"):
    data = f"<script>window.ABR={jd(abr or {'wa':WA,'email':EMAIL,'services':[],'certs':{},'images':[]})};</script>"
    return f'''
</main>
<footer class="ft"><div class="wrap fto"><img src="{B}assets/logo.png" alt="{E(NAME)}" width="156" height="38" style="height:38px;width:auto"><div class="so"><a href="https://wa.me/{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{ic("wa")}</a><a href="mailto:{E(EMAIL)}" aria-label="Email">{ic("mail")}</a>{"".join(f'<a href="https://instagram.com/{i}" target="_blank" rel="noopener" aria-label="Instagram {i}">{ic("ig")}</a>' for i in IG)}<a href="{E(MAP_URL)}" target="_blank" rel="noopener" aria-label="Google Maps">{ic("map")}</a></div></div><div class="wrap"><span>© <span id="y"></span> {E(NAME)}</span><span data-en="Website information is not a substitute for legal advice on a specific matter.">Informasi website bukan pengganti nasihat hukum untuk perkara tertentu.</span><a href="{B}{priv}" data-en="Privacy Policy">Kebijakan Privasi</a></div><div class="wrap" style="margin-top:10px;font-size:.82rem;opacity:.8"><address style="font-style:normal">{E(NAME)} · {E(ADDRESS)}</address></div></footer>
<a class="b g fab" id="fab" href="{H}#contact" data-en="Consult now">Konsultasi</a>
<dialog id="lb"><img alt=""><p></p></dialog>
{data}
<script src="{B}js/abr.js"></script>
</body></html>'''

# ---------------- HOME ----------------
def home():
    B = H = ""
    st = lambda p: f"assets/{p}"
    services_js = [{"k":s[0],"i":s[1],"id":s[2],"en":s[3]} for s in SERVICES]
    certs_js = {}
    for slug,_ in TEAM:
        certs_js[slug] = [[st(f"certificates/{c[0]}.jpg"), cert_caption(c)] for c in CERTS if c[1]==slug]
    images = [[st("gallery/team-courthouse.jpg"),"50% 57%"],[st("gallery/kunjungan-pa-serang.jpg"),"50% 30%"],[st("gallery/tim-kepolisian.jpg"),"50% 35%"],[st("gallery/kunjungan-pa-serang.jpg"),"50% 65%"],[st("gallery/tim-kepolisian.jpg"),"50% 45%"],[st("gallery/team-courthouse.jpg"),"50% 57%"]]
    abr = {"wa":WA,"email":EMAIL,"services":services_js,"certs":certs_js,"images":images}

    team_html = ""
    for i,(slug,name) in enumerate(TEAM):
        pos = ' style="--p:50% 15%"' if slug=="ari-bintara" else ""
        team_html += f'<div class="mem"><article class="pn {"on" if i==0 else ""}" tabindex="0" data-n="{E(name.split()[0])}" data-m="{slug}"><img src="{st(f"team/{slug}.jpg")}" alt="{E(name)}"{pos}><div class="pi"><b>{E(name)}</b><span data-en="Advocate">Advokat</span><a class="b g" href="#contact" data-en="Contact">Hubungi</a></div></article></div>\n'

    gal = ""
    for f,idc,en,pos in GALLERY:
        ps = f' style="object-position:{pos}"' if pos else ""
        gal += f'<button class="gi {"wide" if is_wide(f) else ""}" data-c="{E(idc)}" data-e="{E(en)}"><img src="{st(f"gallery/{f}.jpg")}" alt="{E(idc)}" loading="lazy"{ps}><span data-en="{E(en)}">{E(idc)}</span></button>\n'

    cats = []
    for a in ARTICLES:
        if (a[2],a[1]) not in cats: cats.append((a[2],a[1]))
    chips = '<button class="chip on" data-f="all" data-en="All">Semua</button>' + "".join(f'<button class="chip" data-f="{s}">{E(n)}</button>' for s,n in cats)
    arts = ""
    for i,a in enumerate(ARTICLES):
        im = ART_IMGS[i%3]
        arts += f'<article class="art" data-c="{a[2]}"><img class="ai" src="{st(f"gallery/{im[0]}.jpg")}" alt="" loading="lazy" style="object-position:{im[1]}"><small>{E(a[1])}</small><h3 data-en="{E(a[6])}"><a href="artikel/{a[0]}.html">{E(a[3])}</a></h3><p data-en="{E(a[7])}">{E(a[4])}</p></article>\n'

    faq = "".join(f'<details><summary data-en="{E(q[2])}">{E(q[0])}</summary><p data-en="{E(q[3])}">{E(q[1])}</p></details>\n' for q in FAQ)
    ig = "".join(f'<a href="https://instagram.com/{i}" target="_blank" rel="noopener" style="margin-right:14px;text-decoration:underline">&#64;{i}</a>' for i in IG)
    paras = "".join(f'<p data-en="{E(en)}">{E(p)}</p>' for p,en in zip(ABOUT, ABOUT_EN))
    mission = "".join(f'<div class="st"><b data-en="{E(MISSION_META[i][1])}">{E(MISSION_META[i][0])}</b><p data-en="{E(MISSION_META[i][2])}">{E(m)}</p></div>' for i,m in enumerate(MISSION))

    ig_names = " · ".join("@"+i for i in IG)
    ct_html = f'''<div class="qa">
<a class="qb wa" href="https://wa.me/{WA}" target="_blank" rel="noopener"><span class="qi">{ic("wa")}</span><span><b>WhatsApp</b><small>{E(PHONE)}</small></span></a>
<a class="qb em" href="mailto:{E(EMAIL)}"><span class="qi">{ic("mail")}</span><span><b>Email</b><small>{E(EMAIL)}</small></span></a>
{"".join(f'<a class="qb ig" href="https://instagram.com/{i}" target="_blank" rel="noopener"><span class="qi">{ic("ig")}</span><span><b>Instagram</b><small>@{i}</small></span></a>' for i in IG)}
<a class="qb mp full" href="{E(MAP_URL)}" target="_blank" rel="noopener"><span class="qi">{ic("map")}</span><span><b>Google Maps</b><small data-en="Open the office location">Buka lokasi kantor</small></span></a></div>
<div class="ct"><div class="cr"><span class="ci">{ic("pin")}</span><div><b data-en="Address">Alamat</b><address style="font-style:normal">{E(ADDRESS)}</address></div></div>
<div class="cr"><span class="ci">{ic("clock")}</span><div><b data-en="Service hours">Jam layanan</b>{E(HOURS)}</div></div></div>'''
    form_html = f'''<form class="fc" id="f"><h3 data-en="Send a first message">Kirim pesan awal</h3><p data-en="Do not include confidential details.">Jangan sertakan data rahasia.</p><div class="fg">
<label class="fl"><span class="lb">{ic("user","ico fi")}<span data-en="Name">Nama</span></span><input id="n" required autocomplete="name" placeholder="Nama lengkap" data-ph-en="Full name"></label>
<label class="fl"><span class="lb">{ic("mail","ico fi")}<span>Email</span></span><input id="e" type="email" required autocomplete="email" placeholder="nama@email.com" data-ph-en="name@email.com"></label>
<label class="fl full"><span class="lb">{ic("tag","ico fi")}<span data-en="Category">Kategori</span></span><select id="t"></select></label>
<label class="fl full"><span class="lb">{ic("msg","ico fi")}<span data-en="Short message">Pesan singkat</span></span><textarea id="m" required minlength="10" placeholder="Ceritakan singkat persoalan Anda..." data-ph-en="Briefly describe your situation..."></textarea></label>
<div class="full"><button class="b g sb" type="submit">{ic("send")}<span data-en="Prepare message">Siapkan pesan</span></button></div></div>
<p class="fnote">{ic("lock","ico fi")}<span data-en="Your data stays on your device until you choose to send it.">Data Anda tetap di perangkat Anda sampai Anda memilih mengirimnya.</span></p>
<div id="out" role="status"><div class="oh">{ic("check")}<b data-en="Your message is ready">Pesan Anda siap dikirim</b></div><pre id="ot"></pre>
<div class="oa"><button class="ob cp" type="button" id="cp">{ic("copy")}<span data-en="Copy">Salin</span></button><a class="ob wa" id="wa" target="_blank" rel="noopener">{ic("wa")}<span>WhatsApp</span></a><a class="ob em" id="em">{ic("mail")}<span>Email</span></a></div>
<small data-en="The message is sent only when you choose WhatsApp or Email. Do not include confidential details.">Pesan baru terkirim saat Anda memilih WhatsApp atau Email. Jangan sertakan data rahasia.</small></div></form>'''

    lead_id = f"{NAME}, pengacara dan advokat di Kota Serang, Banten, hadir untuk memberikan pendampingan hukum yang berintegritas, terukur, dan berorientasi pada penyelesaian terbaik bagi setiap klien."
    lead_en = f"{NAME}, lawyers and advocates in Serang, Banten, provides legal support grounded in integrity, careful analysis, and a focus on the best available path forward for every client."

    body = f'''
<section class="hero" id="home"><div class="wrap">
<div class="hc"><div class="eb">{E(TAGLINE)}</div><h1><span class="ln"><span data-en="Resolute in law.">Tegas dalam hukum.</span></span><span class="ln"><span data-en="Professional in representation.">Profesional dalam pendampingan.</span></span></h1>
<p class="lead" data-en="{E(lead_en)}">{E(lead_id)}</p>
<div class="hb"><a class="b g" href="#contact" data-en="Request a Consultation ↗">Jadwalkan Konsultasi ↗</a><a class="b o" href="#team" data-en="Meet Our Team">Kenali Tim Kami</a></div></div>
<div class="hf"><img src="{st("gallery/team-courthouse.jpg")}" alt="Tim advokat ABR &amp; AML di depan media center Pengadilan Negeri Serang" fetchpriority="high"><div class="hcap"><span data-en="Together for responsible legal representation">Bersama untuk pendampingan hukum yang bertanggung jawab</span><span>{E(BRAND)}</span></div></div></div>
<div class="tr"><div class="wrap"><div class="ti"><span class="ic">{ICON_SCALE}</span><span><b data-en="Integrity">Integritas</b><small data-en="Protecting client trust">Menjaga kepercayaan klien</small></span></div><div class="ti"><span class="ic"><svg class="ico" viewBox="0 0 24 24"><path d="M12 3l9 9-9 9-9-9z"/></svg></span><span><b data-en="Professionalism">Profesional</b><small data-en="Careful and accountable">Cermat dan bertanggung jawab</small></span></div><div class="ti"><span class="ic"><svg class="ico" viewBox="0 0 24 24"><circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3"/></svg></span><span><b data-en="Solution-Oriented">Berorientasi Solusi</b><small data-en="Focused on legal needs">Fokus pada kebutuhan hukum</small></span></div><div class="ti"><span class="ic"><svg class="ico" viewBox="0 0 24 24"><path d="M6 11h12v9H6zM8 11V8a4 4 0 018 0v3"/></svg></span><span><b data-en="Confidentiality">Kerahasiaan</b><small data-en="Respecting client privacy">Menghormati privasi klien</small></span></div></div></div></section>

<section class="sec" id="about"><div class="wrap about"><figure class="ap" style="margin:0"><img src="{st("gallery/tim-kepolisian.jpg")}" alt="Dokumentasi kebersamaan tim" loading="lazy"></figure>
<div class="ac"><div class="eb" data-en="About {E(NAME)}">Tentang {E(NAME)}</div><h2 data-en="Guidance with integrity. Advocacy with professionalism.">Mendampingi dengan integritas. Memperjuangkan dengan profesionalisme.</h2>
{paras}
<a class="b bd" href="#team" data-en="Meet Our Advocates →">Kenali Tim Advokat →</a><div class="vg"><div class="vc"><svg class="ico" viewBox="0 0 24 24"><path d="M12 3l9 9-9 9-9-9z"/></svg><b data-en="Integrity">Integritas</b><p data-en="Acting honestly and safeguarding trust.">Bertindak jujur dan menjaga kepercayaan.</p></div><div class="vc">{ICON_SCALE}<b data-en="Professionalism">Profesionalisme</b><p data-en="Careful analysis and clear communication.">Analisis yang cermat dan komunikasi jelas.</p></div><div class="vc"><svg class="ico" viewBox="0 0 24 24"><path d="M12 20s-7-4.5-7-10a4 4 0 017-2.5A4 4 0 0119 10c0 5.5-7 10-7 10z"/></svg><b data-en="Care">Kepedulian</b><p data-en="Understanding context and client needs.">Memahami konteks dan kebutuhan klien.</p></div></div></div></div></section>

<section class="sec dk" id="vision"><div class="wrap pg"><figure class="fr"><img src="{st("gallery/kunjungan-pa-serang.jpg")}" alt="Anggota tim di Pengadilan Agama Serang" loading="lazy" style="aspect-ratio:4/5;object-position:50% 62%"></figure><div><h2 data-en="Vision & Mission">Visi & Misi</h2><p class="sub" data-en="The values that guide every matter we handle.">Nilai yang memandu setiap perkara yang kami tangani.</p>
<div class="vsn"><small data-en="VISION">VISI</small><p data-en="{E(VISION_EN)}">{E(VISION)}</p></div>
<div class="mhd" data-en="OUR MISSION">MISI KAMI</div>
<div class="steps">{mission}</div></div></div></section>

<section class="sec" id="team"><div class="wrap"><h2 data-en="Meet our advocates">Kenali tim advokat kami</h2><p class="sub" data-en="Hover, tap, or tab through the portraits to see who is who.">Arahkan kursor, ketuk, atau tekan Tab pada potret untuk melihat profil.</p>
<div class="pns" id="pns">
{team_html}</div></div></section>

<section class="sec mist" id="services"><div class="wrap"><h2 data-en="Legal services">Layanan hukum</h2><p class="sub" data-en="Choose an area to see what the team can help with.">Pilih bidang untuk melihat bantuan yang dapat diberikan tim.</p><div class="svc"><div class="tabs" id="tabs" role="tablist"></div><div class="det" id="det" aria-live="polite"></div></div></div></section>

<section class="sec dk" id="process"><div class="wrap pg"><figure class="fr"><img src="{st("gallery/tim-kepolisian.jpg")}" alt="Anggota tim berfoto bersama dengan kepalan tangan" loading="lazy" style="aspect-ratio:4/5;object-position:45% 40%"></figure><div><h2 data-en="How we work with you">Cara kami bekerja bersama Anda</h2><p class="sub" data-en="Four clear steps from your first message to ongoing support.">Empat langkah jelas dari pesan pertama hingga pendampingan.</p><div class="steps">
<div class="st"><b data-en="Tell us">Ceritakan</b><p data-en="Send a short summary of your situation.">Kirim ringkasan singkat persoalan Anda.</p></div><div class="st"><b data-en="Initial review">Tinjauan awal</b><p data-en="The team studies the facts and documents.">Tim mempelajari fakta dan dokumen terkait.</p></div><div class="st"><b data-en="Plan">Susun langkah</b><p data-en="We explain options and the way forward.">Kami jelaskan pilihan dan langkah yang tepat.</p></div><div class="st"><b data-en="Representation">Pendampingan</b><p data-en="We stay with you through the process.">Kami mendampingi Anda sepanjang prosesnya.</p></div></div></div></div></section>

<section class="sec" id="gallery"><div class="wrap"><h2 data-en="In the field">Di lapangan</h2><p class="sub" data-en="Tap a photo to enlarge it.">Ketuk foto untuk memperbesar.</p><div class="gal" id="gal">
{gal}</div></div></section>

<section class="sec mist" id="insights"><div class="wrap lt"><h2 data-en="Legal insights">Wawasan hukum</h2><p class="sub" data-en="Short guides to help you prepare.">Panduan singkat untuk persiapan Anda.</p>
<div class="chips" id="fc">{chips}</div>
<div class="arts">
{arts}</div>
<p style="margin:26px 0 0"><a class="b bd" href="artikel/index.html" data-en="All articles →">Semua artikel →</a></p>
</div></section>

<section class="sec"><div class="wrap fq"><figure class="fr"><img src="{st("gallery/pa-pandeglang.jpg")}" alt="Tim advokat di Pengadilan Agama Pandeglang" loading="lazy" style="aspect-ratio:4/5;object-position:50% 46%"></figure><div><h2 data-en="Common questions">Pertanyaan umum</h2>
{faq}</div></div></section>

<section class="sec dk" id="contact"><div class="wrap cg"><div><h2 data-en="Need legal guidance?">Butuh pendampingan hukum?</h2><p class="sub" data-en="Write a short message. We turn it into a ready-to-send note.">Tulis pesan singkat. Kami ubah menjadi pesan siap kirim.</p>
{ct_html}
<figure class="fr cf"><img src="{st("gallery/tim-kepolisian.jpg")}" alt="Tim {E(NAME)}" loading="lazy" style="aspect-ratio:16/7;object-position:50% 35%"></figure></div>
{form_html}</div></section>
'''
    w("index.html", head(TITLE_HOME, DESC_HOME, "/", B, H) + body + foot(B, H, abr))

# ---------------- TIM ----------------
def team_pages():
    B, H = "../", "../index.html"
    for slug,name in TEAM:
        certs = [c for c in CERTS if c[1]==slug]
        ch = ""
        if certs:
            tiles = "".join(f'<button class="gi cert" data-c="{E(cert_caption(c))}"><img src="{B}assets/certificates/{c[0]}.jpg" alt="{E(c[2])}" loading="lazy"><span>{E(cert_caption(c))}</span></button>' for c in certs)
            ch = f'<section class="sec mist"><div class="wrap"><h2 data-en="Certificates">Sertifikat</h2><p class="sub" data-en="Tap a certificate to enlarge it.">Ketuk sertifikat untuk memperbesar.</p><div class="gal">{tiles}</div></div></section>'
        pos = "50% 15%" if slug=="ari-bintara" else "50% 20%"
        body = f'''<section class="sec top"><div class="wrap fq"><figure class="fr"><img class="auto" src="{B}assets/team/{slug}.jpg" alt="{E(name)}" style="aspect-ratio:4/5;object-position:{pos}"></figure>
<div><a class="back" href="{H}#team" data-en="← Back to the team">← Kembali ke tim</a><h1 style="font-size:clamp(1.8rem,4vw,2.8rem)">{E(name)}</h1><p class="sub" style="margin-bottom:18px">Advokat · {E(NAME)}, Serang, Banten</p>
<div class="ps"><p>Advokat pada {E(NAME)}.</p></div><a class="b g" href="{H}#contact" data-en="Contact">Hubungi</a></div></div></section>{ch}'''
        ld = {"@context":"https://schema.org","@type":"Person","name":name,"jobTitle":"Advokat","worksFor":{"@id":SITE_URL+"/#organization"},"url":f"{SITE_URL}/tim/{slug}.html","image":f"{SITE_URL}/assets/team/{slug}.jpg"}
        t = f"{name} — Advokat di Serang, Banten | {NAME}"
        d = f"Profil {name}, advokat pada {NAME}, Kota Serang, Banten."
        w(f"tim/{slug}.html", head(t, d, f"/tim/{slug}.html", B, H, ld) + body + foot(B, H))

# ---------------- ARTIKEL ----------------
def blocks(text):
    out = ""
    for blk in text.split("\n\n"):
        lines = blk.split("\n")
        if all(l[:1].isdigit() and ". " in l[:4] for l in lines):
            out += "<ol style='padding-left:22px;margin:0 0 16px'>" + "".join(f"<li>{E(l.split('. ',1)[1])}</li>" for l in lines) + "</ol>"
        else:
            out += "<p>" + "<br>".join(E(l) for l in lines) + "</p>"
    return out

def article_pages():
    B, H = "../", "../index.html"
    for a in ARTICLES:
        body = f'''<section class="sec top"><div class="wrap nw"><a class="back" href="{B}artikel/index.html" data-en="← All articles">← Semua artikel</a>
<div class="eb" style="color:#a9843c">{E(a[1])} · {datetime.date.fromisoformat(a[8]).strftime("%d-%m-%Y")}</div><h1 style="font-size:clamp(1.8rem,4vw,2.8rem)" data-en="{E(a[6])}">{E(a[3])}</h1>
<div class="ps">{blocks(a[5])}</div><p class="note" data-en="This article is informational and is not legal advice.">Artikel ini bersifat informatif, bukan nasihat hukum.</p>
<p style="margin-top:26px"><a class="b g" href="{H}#contact" data-en="Consult with our team">Konsultasi dengan tim kami</a></p></div></section>'''
        ld = {"@context":"https://schema.org","@type":"Article","headline":a[3],"description":a[4],"datePublished":a[8],"inLanguage":"id","author":{"@id":SITE_URL+"/#organization"},"publisher":{"@id":SITE_URL+"/#organization"},"mainEntityOfPage":f"{SITE_URL}/artikel/{a[0]}.html","image":SITE_URL+"/assets/og-image.jpg"}
        w(f"artikel/{a[0]}.html", head(f"{a[3]} | {NAME}", a[4], f"/artikel/{a[0]}.html", B, H, ld) + body + foot(B, H))
    # indeks
    cats = []
    for a in ARTICLES:
        if (a[2],a[1]) not in cats: cats.append((a[2],a[1]))
    chips = '<button class="chip on" data-f="all" data-en="All">Semua</button>' + "".join(f'<button class="chip" data-f="{s}">{E(n)}</button>' for s,n in cats)
    arts = "".join(f'<article class="art" data-c="{a[2]}"><small>{E(a[1])}</small><h3 data-en="{E(a[6])}"><a href="{a[0]}.html">{E(a[3])}</a></h3><p data-en="{E(a[7])}">{E(a[4])}</p></article>' for a in ARTICLES)
    body = f'<section class="sec mist top"><div class="wrap lt"><h1 style="font-size:clamp(1.8rem,4vw,2.8rem)" data-en="Legal insights">Wawasan hukum</h1><p class="sub" data-en="Short guides to help you prepare.">Panduan singkat untuk persiapan Anda.</p><div class="chips" id="fc">{chips}</div><div class="arts">{arts}</div></div></section>'
    w("artikel/index.html", head(f"Wawasan Hukum — Artikel Pengacara & Advokat | {NAME}", "Panduan hukum singkat dari ABR & AML Law Firm, pengacara dan advokat di Serang, Banten.", "/artikel/", B, H) + body + foot(B, H))

# ---------------- PRIVASI & 404 ----------------
def misc_pages():
    B = ""; H = "index.html"
    body = f'''<section class="sec top"><div class="wrap nw ps"><h1 style="font-size:clamp(1.8rem,4vw,2.8rem)" data-en="Privacy Policy">Kebijakan Privasi</h1>
<p>Situs ini tidak memiliki database dan tidak menyimpan data pribadi pengunjung di server kami.</p>
<p>Pesan yang Anda siapkan melalui formulir hanya diproses di perangkat Anda. Pesan baru terkirim apabila Anda memilih mengirimkannya melalui WhatsApp atau email, dan setelah itu data ditangani oleh layanan tersebut sesuai kebijakannya masing-masing.</p>
<p>Kami menjaga kerahasiaan setiap informasi yang Anda sampaikan kepada kami. Hindari mengirim dokumen atau data yang sangat sensitif sebelum ada kesepakatan pendampingan.</p>
<p>Untuk pertanyaan atau permintaan penghapusan pesan yang pernah Anda kirim, hubungi kami di <a href="mailto:{E(EMAIL)}" style="text-decoration:underline">{E(EMAIL)}</a>.</p></div></section>'''
    w("kebijakan-privasi.html", head(f"Kebijakan Privasi | {NAME}", "Kebijakan privasi situs ABR & AML Law Firm.", "/kebijakan-privasi.html", B, H) + body + foot(B, H))
    # 404: path absolut (disajikan di URL apa pun)
    B = H = "/"
    body = '<section class="sec dk"><div class="wrap" style="text-align:center"><h1 style="font-size:5rem;color:var(--gold2)">404</h1><p class="sub" style="margin:0 auto 24px" data-en="The page you are looking for was not found.">Halaman yang Anda cari tidak ditemukan.</p><a class="b g" href="/" data-en="Back to home">Kembali ke beranda</a></div></section>'
    w("404.html", head(f"Halaman tidak ditemukan | {NAME}", "Halaman tidak ditemukan.", "/404", B, H, noindex=True) + body + foot(B, H))

def seo_files():
    urls = ["/", "/artikel/", "/kebijakan-privasi.html"] + [f"/artikel/{a[0]}.html" for a in ARTICLES] + [f"/tim/{t[0]}.html" for t in TEAM]
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"<url><loc>{SITE_URL}{u}</loc><lastmod>{TODAY}</lastmod></url>\n" for u in urls) + "</urlset>\n"
    w("sitemap.xml", xml)
    w("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")

if __name__ == "__main__":
    home(); team_pages(); article_pages(); misc_pages(); seo_files()
    print("Selesai: index.html, tim/, artikel/, kebijakan-privasi.html, 404.html, sitemap.xml, robots.txt")
