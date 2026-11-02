const $=(s,r=document)=>r.querySelector(s),$$=(s,r=document)=>[...r.querySelectorAll(s)];
const D=window.ABR||{services:[],certs:{},images:[],wa:"",email:""};
const S=D.services,IM=D.images,WA=D.wa;let L="id",cur=S[0]?S[0].k:"";
const P={scale:"M12 3v18M6 21h12M4 7h16M4 7l-2.5 7a3 3 0 005 0zM20 7l-2.5 7a3 3 0 005 0z",doc:"M7 3h7l4 4v14H7zM14 3v4h4M10 12h5M10 16h5",biz:"M3 8h18v12H3zM9 8V5h6v3M3 13h18",home:"M3 11l9-7 9 7M5 10v10h14V10M10 20v-6h4v6",users:"M16 20v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2M10 10a3 3 0 100-6 3 3 0 000 6M20 20v-2a3 3 0 00-2-3M16 4a3 3 0 010 6",chat:"M4 5h16v11H9l-5 4z",heart:"M12 20s-7-4.5-7-10a4 4 0 017-2.5A4 4 0 0119 10c0 5.5-7 10-7 10z"};
const ic=k=>`<svg class="ico" viewBox="0 0 24 24"><path d="${P[k]||P.chat}"/></svg>`;
const T=s=>s[L]||s.id;

function render(){
  if(!$("#tabs")||!S.length)return;
  const l=S.find(s=>s.k===cur)||S[0],d=T(l);
  $("#tabs").innerHTML=S.map(s=>`<button class="tab ${s.k===l.k?"on":""}" role="tab" data-k="${s.k}">${ic(s.i)}${T(s)[0]}</button>`).join("");
  const m=IM[S.indexOf(l)%IM.length]||["",""];
  $("#det").outerHTML=`<div class="det" id="det" aria-live="polite"><div class="dt">${ic(l.i)}<h3>${d[0]}</h3><p>${d[1]}</p><ul>${d[2].map(x=>`<li>${x}</li>`).join("")}</ul><a class="b g" href="#contact" data-pick="${l.k}">${L==="id"?"Ceritakan persoalan Anda":"Tell us your situation"}</a></div><img class="di" src="${m[0]}" alt="" style="object-position:${m[1]}"></div>`;
  const t=$("#t");if(t){const v=t.value;t.innerHTML=S.map(s=>`<option value="${s.k}">${T(s)[0]}</option>`).join("");t.value=v||l.k}
}
document.addEventListener("click",e=>{
  const a=e.target.closest(".tab,[data-pick]");if(!a)return;
  cur=a.dataset.k||a.dataset.pick;render();const t=$("#t");if(t)t.value=cur;
});

function setLang(x){L=x;document.documentElement.lang=x;$("#lg").textContent=x==="id"?"EN":"ID";
  $$("[data-en]").forEach(el=>{if(!el.dataset.id)el.dataset.id=el.innerHTML;el.innerHTML=x==="en"?el.dataset.en:el.dataset.id});
  $$("[data-ph-en]").forEach(el=>{if(!el.dataset.phId)el.dataset.phId=el.placeholder;el.placeholder=x==="en"?el.dataset.phEn:el.dataset.phId});
  render();rc();}
$("#lg").onclick=()=>setLang(L==="id"?"en":"id");

const mb=$("#mb"),nv=$("#nv");
mb.onclick=()=>{const o=nv.classList.toggle("open");mb.setAttribute("aria-expanded",o);mb.textContent=o?"×":"☰"};
nv.onclick=e=>{if(e.target.tagName==="A"){nv.classList.remove("open");mb.textContent="☰"}};

$$(".pn").forEach(p=>{const on=()=>{$$(".pn").forEach(x=>x.classList.toggle("on",x===p))};["mouseenter","focusin","click"].forEach(v=>p.parentElement.addEventListener(v,on))});

const fc=$("#fc");
if(fc)fc.onclick=e=>{const c=e.target.closest(".chip");if(!c)return;$$("#fc .chip").forEach(x=>x.classList.toggle("on",x===c));$$(".art").forEach(a=>a.hidden=c.dataset.f!=="all"&&a.dataset.c!==c.dataset.f)};

/* Lightbox: galeri (.gi) dan sertifikat (.cb) */
const lb=$("#lb");
if(lb){
  document.addEventListener("click",e=>{
    const g=e.target.closest(".gi,.cb");if(!g)return;
    const img=$("img",g);$("img",lb).src=g.dataset.s||img.src;
    $("p",lb).textContent=g.classList.contains("gi")?(L==="id"?g.dataset.c:(g.dataset.e||g.dataset.c)):g.dataset.c;
    lb.showModal();
  });
  lb.onclick=()=>lb.close();
}

/* Sertifikat per anggota */
const C=D.certs||{};
function rc(){$$(".pn").forEach(p=>{const m=p.parentElement,a=C[p.dataset.m]||[];let el=$(".mc",m);
  if(!el){el=document.createElement("div");el.className="mc";m.appendChild(el)}
  el.innerHTML=`<span class="pl">${L==="id"?"Sertifikat":"Certificates"}</span>`+(a.length?`<div class="ctl">${a.map(c=>`<button class="cb" type="button" data-s="${c[0]}" data-c="${c[1]}" title="${c[1]}"><img src="${c[0]}" alt="${c[1]}" loading="lazy"></button>`).join("")}</div>`:`<span class="ce">${L==="id"?"Segera ditambahkan":"Coming soon"}</span>`)})}

/* Formulir: siapkan pesan, lalu salin / kirim lewat WhatsApp atau email (tanpa server) */
const f=$("#f");
if(f){
  f.onsubmit=e=>{e.preventDefault();
    const sv=S.find(s=>s.k===$("#t").value)||S[0],nm=$("#n").value;
    const t=`${L==="id"?"Halo ABR & AML Law Firm, saya":"Hello ABR & AML Law Firm, I am"} ${nm}. ${L==="id"?"Kategori":"Category"}: ${sv?T(sv)[0]:"-"}.\n${$("#m").value}\n\nEmail: ${$("#e").value}`;
    $("#ot").textContent=t;
    $("#wa").href=`https://wa.me/${WA}?text=${encodeURIComponent(t)}`;
    $("#em").href=`mailto:${D.email}?subject=${encodeURIComponent((L==="id"?"Konsultasi hukum - ":"Legal consultation - ")+nm)}&body=${encodeURIComponent(t)}`;
    $("#out").style.display="block";$("#out").scrollIntoView({behavior:"smooth",block:"nearest"})};
  $("#cp").onclick=()=>{const tx=$("#ot").textContent,fb=()=>{const a=document.createElement("textarea");a.value=tx;a.style.position="fixed";a.style.opacity="0";document.body.appendChild(a);a.select();try{document.execCommand("copy")}catch(_){}a.remove()};
    (navigator.clipboard?navigator.clipboard.writeText(tx).catch(fb):fb());const sp=$("#cp span"),o=sp.innerHTML;sp.textContent=L==="id"?"Tersalin ✓":"Copied ✓";setTimeout(()=>{sp.innerHTML=o},1600)};
}

/* Progress bar, tombol mengambang, menu aktif */
const links=$$("nav a"),bar=$("#bar"),fab=$("#fab");
addEventListener("scroll",()=>{const h=document.documentElement;bar.style.transform=`scaleX(${scrollY/(h.scrollHeight-innerHeight||1)})`;
  const c=$("#contact");fab.classList.toggle("on",scrollY>innerHeight*.8&&(!c||c.getBoundingClientRect().top>innerHeight*.6))},{passive:true});
(()=>{const secs=$$("main section[id]");if(!secs.length)return;
  const o=new IntersectionObserver(es=>es.forEach(en=>{if(en.isIntersecting)links.forEach(a=>a.classList.toggle("on",a.hash==="#"+en.target.id))}),{rootMargin:"-45% 0px -50% 0px"});
  secs.forEach(s=>o.observe(s))})();
$("#y").textContent=new Date().getFullYear();
render();rc();
