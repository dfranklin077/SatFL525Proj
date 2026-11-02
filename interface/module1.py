"""Module 1: Federated learning basics

The whole lesson as one self-contained HTML document (text, charts, sliders and
quiz all run in the browser). It is shown by interface/fl_modules.py.
"""
TITLE = 'Module 1: Federated learning basics'

HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Module 1: Federated Learning (FL) Basics – How local models become a global model</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&display=swap">
<style>
:root{--bg:#f3f6fa;--surf:#fff;--ink:#0f1b2d;--mute:#5a6b82;--line:#d5dde8;--acc:#1f5eff;
--c0:#e4572e;--c1:#12a37f;--c2:#9b5de5;--c3:#e09f00;--c4:#00a6d6;--c5:#d6336c;
box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#070d1a;--surf:#0f1a2e;--ink:#e8eef8;--mute:#93a3bb;--line:#243350;--acc:#6b9bff;
--c0:#ff7a52;--c1:#3dd6ac;--c2:#c08bff;--c3:#ffc233;--c4:#4cd0f5;--c5:#ff6b9f}}
:root[data-theme="dark"]{--bg:#070d1a;--surf:#0f1a2e;--ink:#e8eef8;--mute:#93a3bb;--line:#243350;--acc:#6b9bff;
--c0:#ff7a52;--c1:#3dd6ac;--c2:#c08bff;--c3:#ffc233;--c4:#4cd0f5;--c5:#ff6b9f}
html{scroll-padding-top:env(safe-area-inset-top,0px)}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 "Space Grotesk",system-ui,-apple-system,"Segoe UI",sans-serif}
main{max-width:1000px;margin:0 auto;padding:28px 18px 48px}
h1{font-size:clamp(26px,4.5vw,40px);line-height:1.1;margin:4px 0 10px;letter-spacing:-.02em}
h2{font-size:18px;margin:0 0 8px}
.lede{color:var(--mute);max-width:62ch;margin:0 0 22px}
.tag{display:inline-block;font-size:13px;color:var(--acc);border:1px solid var(--acc);border-radius:99px;padding:1px 10px}
.grid{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,1fr);gap:16px}
@media(max-width:760px){.grid{grid-template-columns:minmax(0,1fr)}}
.box{min-width:0;background:var(--surf);border:1px solid var(--line);border-radius:10px;padding:14px}
svg{display:block;width:100%;height:auto}
.ctl{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0 0}
button{font:inherit;font-weight:500;border:1px solid var(--line);background:var(--surf);color:var(--ink);border-radius:8px;padding:8px 14px;cursor:pointer}
button.p{background:var(--acc);border-color:var(--acc);color:#fff}
button:focus-visible,input:focus-visible{outline:2px solid var(--acc);outline-offset:2px}
.sl{display:grid;grid-template-columns:130px 1fr 36px;align-items:center;gap:8px;font-size:14px;margin-top:8px;color:var(--mute)}
.sl output{color:var(--ink);text-align:right}
.sl input[type=range]{min-width:0;width:100%}
.steps{display:flex;gap:6px;margin-bottom:10px}
.st{flex:1;font-size:13px;padding:6px 8px;border-radius:8px;border:1px solid var(--line);color:var(--mute);text-align:center}
.st.on{border-color:var(--acc);color:var(--ink);background:color-mix(in srgb,var(--acc) 12%,transparent)}
.say{min-height:76px;margin:0 0 12px}
.scroll{overflow-x:auto}
table{border-collapse:collapse;width:100%;font-size:13px;font-variant-numeric:tabular-nums}
td,th{text-align:left;padding:5px 6px;border-bottom:1px solid var(--line);white-space:nowrap}
th{color:var(--mute);font-weight:500}
.dot{display:inline-block;width:10px;height:10px;border-radius:50%;margin-right:6px}
.stats{display:flex;gap:18px;flex-wrap:wrap;margin:0 0 6px}
.stats b{font-size:26px;display:block;line-height:1.1}
.stats span{font-size:13px;color:var(--mute)}
.f{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:13px;background:color-mix(in srgb,var(--acc) 8%,transparent);border-radius:8px;padding:10px 12px;margin-top:12px;overflow-x:auto;white-space:pre}
.key{font-size:13px;color:var(--mute);margin-top:8px}
.two{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:14px}
@media(max-width:760px){.two{grid-template-columns:minmax(0,1fr)}}
.loop{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin-top:12px}
.loop.l3{grid-template-columns:repeat(3,1fr)}
.loop.l4{grid-template-columns:repeat(4,1fr)}
.loop.l2{grid-template-columns:repeat(2,1fr)}
.loop.l2 div,.loop.l3 div{line-height:1.5}
table.wrap td,table.wrap th{white-space:normal;vertical-align:top}
table.wrap td:first-child{min-width:110px}
@media(max-width:760px){.loop.l3{grid-template-columns:1fr}.loop.l4{grid-template-columns:1fr 1fr}.loop.l2{grid-template-columns:1fr}}
@media(max-width:760px){.loop{grid-template-columns:1fr 1fr}}
.loop div{border:1px solid var(--line);border-radius:8px;padding:8px 10px;font-size:13px;color:var(--mute)}
.loop b{display:block;color:var(--ink);font-size:14px}
.cap{font-size:13px;color:var(--mute);margin:4px 0 0}
.q button{display:block;width:100%;text-align:left;margin-top:6px}
.sec{margin-bottom:16px}
@media (prefers-reduced-motion:reduce){.pk{display:none}}
svg text{font-family:inherit}
.nav{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 16px}
.nav a{font-size:13px;border:1px solid var(--line);border-radius:99px;padding:2px 10px;text-decoration:none;background:var(--surf);color:var(--ink)}
.dg{display:grid;grid-template-columns:78px repeat(10,1fr);gap:4px;align-items:center;margin-top:10px;font-size:13px}
.dg span{text-align:center;border-radius:4px;padding:3px 0;border:1px solid var(--line)}
.dg .no{background:color-mix(in srgb,var(--c0) 25%,transparent);color:var(--c0);text-decoration:line-through}
.dg .ok{background:color-mix(in srgb,var(--c1) 18%,transparent)}
.sl.w{grid-template-columns:150px 1fr 52px}
.lg{display:flex;flex-wrap:wrap;gap:4px 14px;font-size:13px;color:var(--mute);margin-top:6px}
.lg i{display:inline-block;width:18px;height:3px;border-radius:2px;margin-right:6px;vertical-align:middle}
code{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:12px}
@media(max-width:480px){.sl.w{grid-template-columns:110px 1fr 46px}}
</style>
</head>
<body>
<main>
<span class="tag">Module 1 of 8 · Live demo</span>
<h1>Federated learning (FL) basics: how local models become a global model</h1>
<p class="lede">Several satellites each hold their own images. They never share the images. Instead, each one trains a small model locally and sends only the model weights to a server, which averages them. Step through one round at a time and watch the shared model improve.</p>

<nav class="nav" aria-label="Module sections"><a href="#intro">Start here</a><a href="#s1">1 The data problem</a><a href="#s2">2 The idea</a><a href="#s3">3 Why not centralize</a><a href="#s4">4 Silos and devices</a><a href="#s5">5 Try a round</a><a href="#s6">6 Tuning</a><a href="#s7">7 Privacy</a><a href="#s8">8 Bandwidth</a></nav>

<section class="box sec" id="intro">
<h2>Start here: what federated learning is and why it exists</h2>
<p style="margin:0 0 8px;font-size:15px"><b>Federated learning (FL)</b> trains one shared machine-learning model on data that is spread over many places, without gathering that data in one place. Each place is a <b>client</b>: a phone, a hospital or, here, a satellite. A client trains the model on its own data and sends back only what it learned, the model’s <b>weights</b> (the adjustable numbers inside it). A <b>server</b> combines the clients’ weights into one improved <b>global model</b>, by averaging them in proportion to how much data each client holds (federated averaging, or <b>FedAvg</b>), and sends it out for the next round. The raw data never leaves the client.</p>

<p class="cap" style="margin:8px 0 0">How the module follows this story: sections 1 to 4 show why the data stays put and who takes part, section 5 lets you run rounds yourself, and sections 6 to 8 cover the controls, the privacy leaks and the traffic bill.</p>
</section>

<section class="box sec" id="s1">
<h2>1 The data problem: what one dataset cannot see</h2>
<h2 style="margin-top:0">First, how machine learning usually works</h2>
<div class="loop l3">
<div><b>A model</b>A function with adjustable numbers called weights. A neural network is the best-known kind. The demo in section 5 uses a tiny one: a straight-line classifier, which sorts points into two classes with a line, and has three weights.</div>
<div><b>Data</b>The examples the model learns from: labeled images, audio clips, sensor readings. For a satellite, a picture and what it shows.</div>
<div><b>Training</b>Adjusting the weights over many passes through the data until the model does a useful task well, such as spotting objects in images, transcribing speech or playing the board game Go. Using the finished model afterwards (inference) is one pass, and the weights stay fixed.</div>
</div>
<h2 style="margin-top:16px">A model can only learn what its data contains</h2>
<p class="cap" style="margin:0 0 8px">More and more varied data makes better models. Llama 3, a family of large language models from Meta, trained on about 15 trillion tokens (a token is a word or a piece of a word) against about 2 trillion for Llama 2, and the 8B version of Llama 3 (8 billion weights) beat the 70B version of Llama 2 (70 billion weights). Yet all the high-quality public English text there is comes to roughly 15 trillion tokens, while privately stored instant messages alone are estimated at about 650 trillion and stored emails at about 1,200 trillion. All of these are estimates, quoted only to compare scale.</p>
<p class="cap est" style="margin:2px 0 8px;font-style:italic">Not exact: shown to illustrate a trend.</p>
<p class="cap" style="margin:0">A classic test uses handwritten digits from MNIST (the Modified National Institute of Standards and Technology database, a standard set of 70,000 digit images). Three clients each hold part of the data, with three digits missing from each. Red, struck-through digits are missing.</p>
<div class="dg" id="dg"></div>
<div class="ctl"><button type="button" id="ba" class="p">Each client trains alone</button><button type="button" id="bf">Train federated</button></div>
<p class="say" id="dgo" role="status" style="margin-top:10px"></p>
<p class="cap"><b>The setup.</b> Three PyTorch models (PyTorch is a widely used Python library for building and training neural networks) are trained on MNIST, each missing three digits, then one federated model is trained for 3 rounds over the same three clients. The buttons switch which result is shown. <b>Why a model alone fails:</b> a model that never saw a digit learns never to predict it. The confusion matrix (a table counting how often each true digit is predicted as each digit) shows a missing 1 being labeled as a similar digit, often 2 or 8. <b>Why federated works:</b> the averaged model has, through the three clients, learned from all ten digits, so no column of its confusion matrix is empty.</p>
<script>(function(){var R=[[1,3,7],[2,5,8],[4,6,9],[]],h='';R.forEach(function(m,i){h+='<b>'+(i<3?'Client '+(i+1):'Together')+'</b>';for(var d=0;d<10;d++)h+='<span class="'+(m.indexOf(d)>=0?'no':'ok')+'">'+d+'</span>'});document.getElementById('dg').innerHTML=h;var o=document.getElementById('dgo'),a=document.getElementById('ba'),f=document.getElementById('bf');function s(x){a.className=x?'p':'';f.className=x?'':'p';o.textContent=x?'Alone, each model reaches about 65 to 70% on all ten digits but 0% on the digits it never saw. It learns never to predict them: a missing 1 is often labeled 2 or 8.':'Federated for 3 rounds, the same three clients reach about 96% on all digits, and 94 to 96% on the digits each one was missing. No client shared any images.'}a.onclick=function(){s(1)};f.onclick=function(){s(0)};s(1)})()</script>
</section>

<section class="box sec" id="s2">
<h2>2 The idea: send the model to the data, not the data to the model</h2>
<div class="two">
<div>
<svg viewBox="0 0 360 220" role="img" aria-label="Centralized learning: three satellites send raw images to one server">
<defs><symbol id="sat" viewBox="-16 -10 32 20"><rect x="-5" y="-4" width="10" height="8" rx="1.5" fill="currentColor"/><rect x="-15" y="-3" width="8" height="6" fill="none" stroke="currentColor" stroke-width="1.4"/><rect x="7" y="-3" width="8" height="6" fill="none" stroke="currentColor" stroke-width="1.4"/></symbol>
<marker id="ar" viewBox="0 0 8 8" refX="6" refY="4" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L8 4L0 8z" fill="var(--mute)"/></marker></defs>
<g stroke="var(--c0)" stroke-width="6" opacity=".35" stroke-linecap="round"><path d="M78 40L238 104"/><path d="M78 110L238 110"/><path d="M78 180L238 116"/></g>
<g fill="var(--c0)"><rect class="pk" width="9" height="9" x="-4" y="-4"><animateMotion dur="2.4s" repeatCount="indefinite" path="M78 40L238 104"/></rect><rect class="pk" width="9" height="9" x="-4" y="-4"><animateMotion dur="2.4s" begin=".8s" repeatCount="indefinite" path="M78 110L238 110"/></rect><rect class="pk" width="9" height="9" x="-4" y="-4"><animateMotion dur="2.4s" begin="1.6s" repeatCount="indefinite" path="M78 180L238 116"/></rect></g>
<g style="color:var(--ink)"><use href="#sat" x="22" y="26" width="56" height="28"/><use href="#sat" x="22" y="96" width="56" height="28"/><use href="#sat" x="22" y="166" width="56" height="28"/></g>
<rect x="238" y="84" width="96" height="52" rx="8" fill="var(--surf)" stroke="var(--ink)" stroke-width="1.5"/><text x="286" y="108" text-anchor="middle" font-size="13" font-weight="700" fill="var(--ink)">Ground server</text><text x="286" y="125" text-anchor="middle" font-size="11" fill="var(--mute)">trains on all data</text>
<text x="150" y="212" text-anchor="middle" font-size="12" fill="var(--c0)" font-weight="700">Raw images travel: huge, private</text>
</svg>
<p class="cap"><b>Centralized.</b> Every image is downlinked first. Satellite bandwidth is scarce, and the data may be sensitive.</p>
</div>
<div>
<svg viewBox="0 0 360 220" role="img" aria-label="Federated learning: server sends global model to satellites, satellites return trained weights">
<g stroke="var(--acc)" stroke-width="1.5" fill="none" marker-end="url(#ar)" marker-start="url(#ar)"><path d="M82 42L234 100"/><path d="M82 110L234 110"/><path d="M82 178L234 120"/></g>
<g fill="var(--acc)"><circle class="pk" r="4.5"><animateMotion dur="5.2s" repeatCount="indefinite" path="M234 100L82 42" keyPoints="0;1;1" keyTimes="0;.5;1" calcMode="linear"/><animate attributeName="opacity" dur="5.2s" repeatCount="indefinite" values="1;0;0" keyTimes="0;.5;1" calcMode="discrete"/></circle><circle class="pk" r="4.5"><animateMotion dur="5.2s" repeatCount="indefinite" path="M234 110L82 110" keyPoints="0;1;1" keyTimes="0;.5;1" calcMode="linear"/><animate attributeName="opacity" dur="5.2s" repeatCount="indefinite" values="1;0;0" keyTimes="0;.5;1" calcMode="discrete"/></circle><circle class="pk" r="4.5"><animateMotion dur="5.2s" repeatCount="indefinite" path="M234 120L82 178" keyPoints="0;1;1" keyTimes="0;.5;1" calcMode="linear"/><animate attributeName="opacity" dur="5.2s" repeatCount="indefinite" values="1;0;0" keyTimes="0;.5;1" calcMode="discrete"/></circle></g>
<g fill="var(--c1)"><circle class="pk" r="4.5"><animateMotion dur="5.2s" repeatCount="indefinite" path="M82 42L234 100" keyPoints="0;0;1" keyTimes="0;.5;1" calcMode="linear"/><animate attributeName="opacity" dur="5.2s" repeatCount="indefinite" values="0;1;1" keyTimes="0;.5;1" calcMode="discrete"/></circle><circle class="pk" r="4.5"><animateMotion dur="5.2s" repeatCount="indefinite" path="M82 110L234 110" keyPoints="0;0;1" keyTimes="0;.5;1" calcMode="linear"/><animate attributeName="opacity" dur="5.2s" repeatCount="indefinite" values="0;1;1" keyTimes="0;.5;1" calcMode="discrete"/></circle><circle class="pk" r="4.5"><animateMotion dur="5.2s" repeatCount="indefinite" path="M82 178L234 120" keyPoints="0;0;1" keyTimes="0;.5;1" calcMode="linear"/><animate attributeName="opacity" dur="5.2s" repeatCount="indefinite" values="0;1;1" keyTimes="0;.5;1" calcMode="discrete"/></circle></g>
<g style="color:var(--ink)"><use href="#sat" x="22" y="26" width="56" height="28"/><use href="#sat" x="22" y="96" width="56" height="28"/><use href="#sat" x="22" y="166" width="56" height="28"/></g>
<g fill="var(--surf)" stroke="var(--mute)"><rect x="6" y="58" width="34" height="16" rx="4" stroke-dasharray="3 2"/><rect x="6" y="128" width="34" height="16" rx="4" stroke-dasharray="3 2"/><rect x="6" y="198" width="34" height="16" rx="4" stroke-dasharray="3 2"/></g>
<g font-size="10" fill="var(--mute)" text-anchor="middle"><text x="23" y="70">data</text><text x="23" y="140">data</text><text x="23" y="210">data</text></g>
<rect x="234" y="84" width="100" height="52" rx="8" fill="var(--surf)" stroke="var(--ink)" stroke-width="1.5"/><text x="284" y="108" text-anchor="middle" font-size="13" font-weight="700" fill="var(--ink)">Ground server</text><text x="284" y="125" text-anchor="middle" font-size="11" fill="var(--mute)">averages weights</text>
<text x="230" y="210" text-anchor="middle" font-size="12" fill="var(--acc)" font-weight="700">Weights travel: small, no images</text>
</svg>
<p class="cap"><b>Federated.</b> Blue dots carry the global model from the server to the satellites first; then the green dots carry the trained weights back to the server. They take turns, as in a real round. The data stays in the dashed boxes.</p>
</div>
</div>
<p class="cap est" style="margin:2px 0 8px;font-style:italic">Not exact: shown to illustrate a trend.</p>
<div class="loop">
<div><b>0 Initialize</b>The server creates the global model.</div>
<div><b>1 Send</b>It sends the model to the connected satellites.</div>
<div><b>2 Train locally</b>Each satellite trains on its own images.</div>
<div><b>3 Return</b>Each satellite sends its updated model back.</div>
<div><b>4 Aggregate</b>The server averages them into a new global model. Step 5: repeat 1 to 4 until it converges.</div>
</div>
<h2 style="margin-top:16px">Sending and receiving happen in turns, not at once</h2>
<p class="cap" style="margin:0 0 8px">In the standard version, federated averaging (FedAvg, which is also what the demo in section 5 runs), the server and the clients do not send and receive at the same time: a round runs in phases, and each phase waits for the one before it. A new phase can only start once all clients complete their computations, and FedAvg belongs to this <i>synchronous</i> class.</p>
<div class="loop l4">
<div><b>Phase 1: server sends</b>The server sends the current global model, only to the clients picked for this round. Nobody is uploading yet.</div>
<div><b>Phase 2: clients train</b>No communication at all. The server waits while each client works at its own speed.</div>
<div><b>Phase 3: clients return</b>Updates come back one by one. The server cannot aggregate until enough of them have arrived.</div>
<div><b>Phase 4: server aggregates</b>The new global model exists only now. Then the next round can start.</div>
</div>
<p class="cap" style="margin-top:10px"><b>A link can carry traffic both ways,</b> but within one round the algorithm sends first and receives later, which is why the animation above shows the two directions taking turns.</p>
<p class="cap"><b>The clients are not in lockstep with each other either.</b> They train for different lengths of time and finish at different moments, so a round lasts as long as the slowest client the server is willing to wait for. For very large populations, a round can start with extra clients and close once enough have reported, which drops the stragglers, the slowest clients.</p>
<p class="cap"><b>Satellites make the waiting much worse.</b> A satellite can only talk during a ground-contact window. In one worked example, one satellite with a late contact holds the first global FedAvg iteration back by more than nine hours. One remedy is <i>asynchronous</i> FL, such as FedAsync (a general-purpose asynchronous method) and FedSat (an asynchronous version of FedAvg designed for satellites): the server updates the global model whenever any update arrives, and satellites keep computing while offline. The price is stale updates and slower convergence. Another route: a satellite trains on the parts of the model it has already received while the remaining parts are still arriving. Modules 4 and 5 return to both ideas.</p>
<p class="cap" style="margin-top:10px">Cross-silo FL (the clients are organizations or data centers) has a few clients that are available every round; cross-device FL (the clients are phones and other small devices) has many clients that come and go. A satellite constellation sits in between: few clients, but each one is only reachable during a ground-contact window. By default the demo in section 5 selects every satellite every round; its Clients per round slider changes that, and Module 4 adds realistic contact windows.</p>
<h2 style="margin-top:16px">What federated learning changes, and when it fits</h2>
<p class="cap" style="margin:0 0 8px">FL reverses the direction of travel: the server sends the model to the data instead of collecting the data. It was invented for cases like the phone keyboard, where typed text should never leave the phone. The loop above walks through it. It fits best when three things hold:</p>
<div class="loop l3">
<div><b>Local data matters</b>The data on the device is more useful than any stand-in a server could hold. A satellite’s own images are the obvious example.</div>
<div><b>Privacy or size is a concern</b>The data is sensitive, or too large to move. Satellite imagery is large, and can be sensitive.</div>
<div><b>Labels are available</b>The client can tell what the right answer is. A keyboard learns it from what you type next. For a satellite image the label has to come from somewhere, which is a design question. The demos here sidestep it by giving every satellite labeled data.</div>
</div>
</section>

<section class="box sec" id="s3">
<h2>3 The case against collecting the data</h2>
<h2 style="margin-top:0">Where the data is, and what machine learning has usually done about it</h2>
<p class="cap" style="margin:0 0 8px">Data is born on devices: a phone running an app, a car collecting sensor readings, a laptop keyboard, a smart speaker, a satellite camera. It is also born in many places at once: many devices running the same app, or several organizations producing data for the same task. The usual answer has been to copy all of it to one central server, in a data center or the cloud, and train there.</p>
<p class="cap" style="margin:0 0 8px">That works when the data already sits on a server, such as holiday photos or web-traffic analytics. It breaks down in healthcare, cars, finance and secure messaging, where the data cannot be moved, or where the data one holder has is not enough to train a good model. Three obstacles keep coming back: laws that restrict moving data, people’s expectation that some data never leaves their device, and sensors that produce more data than anyone can ship or store (taken one at a time below). A satellite constellation meets the third head-on: a camera can make more imagery than the radio link to the ground can carry, and Module 2 puts numbers on that.</p>
<div class="loop l3">
<div><b>Regulation</b>Laws such as the European Union’s General Data Protection Regulation (GDPR) and California’s Consumer Privacy Act (CCPA) restrict moving data, and can even stop one organization from pooling its own users’ data across regions.</div>
<div><b>User expectation</b>People expect sensitive input, like passwords typed on a keyboard, to stay on their device. That use case is why FL was invented.</div>
<div><b>Data volume</b>Cameras and other sensors produce more data than is practical or worthwhile to collect. Satellite imagery is the extreme case.</div>
</div>
<h2 style="margin-top:16px">What the whole system optimizes</h2>
<div class="f">min f(w) = Σ p_k · F_k(w),   k = 1 … N
min    = pick the w that makes f(w) as small as possible
Σ      = add up the terms for every client k
w      = the model's weights
N      = number of clients (devices, satellites)
F_k(w) = loss on client k's data (how wrong the model is)
p_k    = how much client k counts (in the demo, n_k / n)</div>
<h2 style="margin-top:16px">What gets hard next</h2>
<div class="loop l4">
<div><b>Statistical heterogeneity</b>Clients’ data is not identically distributed (non-IID, as described at the top). See Module 3.</div>
<div><b>Expensive communication</b>Slow links and limited contact. See section 8 and Modules 2, 4 and 5.</div>
<div><b>Systems heterogeneity</b>Different hardware, connectivity and power. See Module 6.</div>
<div><b>Privacy and security</b>Updates can still leak information, so extra protection may be needed. See section 7.</div>
</div>
<h2 style="margin-top:16px">The catch: the clients’ data is rarely alike</h2>
<p class="cap" style="margin:0 0 8px">Keeping raw data on the device is FL’s main privacy benefit, but the weights that come back are computed from that data and can still leak information (section 7). The second catch is statistical. In ordinary training the data is shuffled, so every batch (a small group of examples used for one training step) looks like a random sample of the whole: the data is <b>independent and identically distributed (IID)</b>. Federated clients are rarely like that. A hospital’s records reflect its region, a phone’s data reflects one person’s habits, and a satellite sees only the stretch of Earth under its orbit. Data that differs from client to client in this way is <b>non-IID</b>, and it is one of the main reasons federated training is harder than the usual kind. Here is what it does:</p>
<div class="loop l3">
<div><b>Updates disagree</b>Each client trains on its own skewed slice, so its update is biased toward what that client sees. Averaging updates that pull in different directions makes the global model zigzag instead of improving steadily.</div>
<div><b>Models drift</b>Each local model moves away from the global model and from the other clients’ models, and the more local training it does, the further it goes. This is called client drift.</div>
<div><b>Accuracy suffers</b>Even when training settles, the result is a compromise that is not best for any single client, and it is often less accurate than a model trained on pooled data (everyone’s data combined in one place).</div>
</div>
<p class="cap" style="margin:10px 0 0">Fixes exist, and each trades something away: more communication, more computation, or a little shared data. FedProx adds a penalty that keeps each client’s local model close to the global one. Other fixes pick or group clients so that each round is more representative, give every client a small shared public data set to train on as well, or have clients share what their models predict (knowledge distillation) instead of raw data. This module keeps the data IID on purpose, so the mechanics of a round stay clear. Module 3 makes it non-IID, shows the damage, and goes through the fixes.</p>
</section>

<section class="box sec" id="s4">
<h2>4 Who takes part: silos, devices and satellites</h2>
<p class="cap" style="margin:0 0 8px">A working definition from the field: several clients solve a learning problem together under a coordinating server. Each client’s raw data stays put, and only focused updates meant for immediate aggregation are shared. The server coordinates but never sees raw data, and it is usually not one physical machine. There are two broad kinds. In cross-silo FL the clients are organizations or data centers, each holding a silo of data. In cross-device FL the clients are phones and Internet of Things (IoT) devices, meaning everyday objects and sensors with a network connection. A satellite constellation has features of both. Within either kind, clients can be alike (the same hardware) or very different (mixed hardware and connections).</p>
<div class="scroll"><table>
<tr><th>Difference</th><th>Cross-silo</th><th>Cross-device</th><th>A satellite constellation</th></tr>
<tr><td>Clients</td><td>Organizations or regional datacenters</td><td>Phones and IoT devices</td><td>Satellites owned by one operator</td></tr>
<tr><td>How many</td><td>Typically 2 to 100</td><td>Up to about 10¹⁰</td><td>Tens to hundreds</td></tr>
<tr><td>Availability</td><td>Almost always available</td><td>Only a fraction at any time</td><td>Predictable but intermittent contact</td></tr>
<tr><td>Reliability</td><td>Fairly reliable</td><td>5% or more drop out each round</td><td>Bursty link loss</td></tr>
<tr><td>Same client each round?</td><td>Yes, stateful</td><td>Usually a fresh sample</td><td>Yes, the same satellites</td></tr>
<tr><td>Main bottleneck</td><td>Compute or communication</td><td>Usually communication</td><td>Communication and onboard compute</td></tr>
</table></div>
<p class="cap">For scale, cross-device rounds involve 100s to 1000s of clients, 1000s of rounds, and 1 to 10 minutes per round.</p>
<div class="loop l4">
<div><b>Finance</b>Transaction data must stay in its region, yet is needed to train anti-money-laundering models.</div>
<div><b>Keyboards</b>Gboard, Google’s phone keyboard, trains across hundreds of millions of phones. A federated next-word model was reported 24% more accurate than the n-gram baseline (a model that predicts the next word from the few words before it).</div>
<div><b>Hospitals</b>The United Kingdom’s National Health Service (NHS) and the University of Oxford trained an early screener for COVID (coronavirus disease) on data from 130,000 patients.</div>
<div><b>Imaging</b>Intel and the University of Pennsylvania (Penn) set up 29 institutions to train brain-tumor detection without sharing patient data.</div>
</div>
</section>

<div class="grid">
<div class="box">
<h2 id="s5">5 Try a round: each satellite’s private data</h2>
<svg id="plot" viewBox="0 0 360 360" role="img" aria-label="Scatter plot of each satellite’s data with decision boundaries"></svg>
<div class="key">Circles are class A, diamonds are class B. Colour shows which satellite owns the point. The thick line is the global model’s boundary; dashed lines are local models.</div>
</div>

<div class="box">
<div class="steps" id="steps">
<div class="st">1 Send global</div><div class="st">2 Train locally</div><div class="st">3 Average</div>
</div>
<p class="say" id="say"></p>
<div class="stats">
<div><b id="sRound">0</b><span>rounds done</span></div>
<div><b id="sAcc">–</b><span>global accuracy</span></div>
<div><b id="sLoss">–</b><span>global loss</span></div>
</div>
<div class="ctl">
<button class="p" id="next">Next step</button>
<button id="round">Run a full round</button>
<button id="auto">Auto-play</button>
<button id="reset">Reset</button>
</div>
<div class="sl"><label for="K">Satellites K</label><input id="K" type="range" min="2" max="6" value="4"><output id="Ko">4</output></div>
<div class="sl"><label for="E">Local epochs E</label><input id="E" type="range" min="1" max="30" value="5"><output id="Eo">5</output></div>
<div class="sl"><label for="L">Learning rate η</label><input id="L" type="range" min="1" max="20" value="5"><output id="Lo">0.5</output></div>
<div class="sl"><label for="M">Clients/round m</label><input id="M" type="range" min="1" max="4" value="4"><output id="Mo">4</output></div>
<div class="sl"><label for="SC" title="2 local epochs in rounds 1 and 2, then 5">Epoch schedule</label><input id="SC" type="checkbox" style="justify-self:start;width:18px;height:18px"><output id="SCo">off</output></div>
<div class="key">The epoch schedule uses 2 local epochs in rounds 1 and 2, then 5. While it is on, it overrides the epochs slider.</div>
</div>
</div>

<div class="grid" style="margin-top:16px">
<div class="box">
<h2>What each satellite sends</h2>
<div class="scroll"><table id="tbl"></table></div>
<div class="f" id="formula"></div>
</div>
<div class="box">
<h2>Global accuracy by round</h2>
<svg id="chart" viewBox="0 0 360 200" role="img" aria-label="Line chart of global accuracy per round"></svg>
<div class="key">Accuracy is measured on a held-out set pooled from all satellites. The server never sees that data in a real system; here it only lets us check progress.</div>
<p class="cap est" style="margin:2px 0 8px;font-style:italic">Not exact: shown to illustrate a trend.</p>
</div>
</div>
<section class="box sec" id="s5b" style="margin-top:16px">
<h2>What the symbols and controls in this demo mean</h2>
<p class="cap" style="margin:0 0 6px"><b>One round, written out.</b> This is exactly what the demo does each time you press Run a full round:</p>
<div class="f">for each round:
  1. the server picks m of the K satellites at random
  2. it sends each picked satellite the current global weights w_global
  3. satellite k starts from w_global and takes E gradient steps
     (step size η) on its own n_k points, giving w_k
  4. each picked satellite sends w_k back
  5. the server sets  w_global = Σ (n_k / n) · w_k
     (the sum runs over the picked satellites; n = their total n_k)</div>
<p class="cap"><b>What to look for.</b> After <i>Train locally</i>, each dashed line has moved toward what that satellite’s own points prefer, so the weights in the table differ from satellite to satellite. After <i>Average</i>, the new global line sits among them, pulled most by the satellites with the largest shares (satellite 3 by default, with 39% of the points). Then set Local epochs to 1 and see how many rounds it takes to pass 80%. Satellites K and Clients/round m change who takes part and each satellite’s share. They barely change where the accuracy settles, because every satellite draws from the same distribution. With m below K the curve is jumpier from round to round, because each round follows only the few satellites picked, and their small datasets pull the line in slightly different directions. They matter more in Module 3, where the satellites’ data differs.</p>
<p class="cap" style="margin:0 0 8px"><b>The model.</b> So everything runs in your browser, each satellite trains a three-number model: logistic regression with weights w = (w₁, w₂, b), where b is the bias that shifts the line. For a point at position (x, y) it predicts the chance of class B as 1 / (1 + e<sup>−(w₁x + w₂y + b)</sup>), where e ≈ 2.718 is Euler’s number. The straight line on the plot is where that chance is 50%, so changing w moves the line.</p>
<p class="cap"><b>The data.</b> Satellite k holds n<sub>k</sub> points drawn from two overlapping clouds: class A centred near (−1, −0.9) and class B near (1, 0.9), each with spread 0.9. Satellites 1 to 6 hold 40, 24, 60, 30, 46 and 20 points; those sizes are chosen so the shares differ. Every satellite draws from the same distribution, which is what IID (independent and identically distributed) means; Module 3 changes that. Accuracy is measured on 300 further points from the same distribution that nobody trains on.</p>
<div class="scroll" style="margin-top:8px"><table class="wrap">
<tr><th>Symbol or control</th><th>Meaning</th></tr><tr><td>n<sub>k</sub></td><td>How many data points (in the real setting, images) satellite k holds.</td></tr><tr><td>n</td><td>The total of n<sub>k</sub> over the satellites picked this round.</td></tr><tr><td>Share n<sub>k</sub> / n</td><td>Satellite k’s weight in the average. Twice the data means twice the say.</td></tr><tr><td>w<sub>k</sub></td><td>The three weights satellite k sends back after training locally.</td></tr><tr><td>w_global</td><td>The new global weights: the sum of (n<sub>k</sub> / n) · w<sub>k</sub> over the picked satellites.</td></tr><tr><td>Satellites K</td><td>How many clients exist, 2 to 6.</td></tr><tr><td>Local epochs E</td><td>One epoch is one pass of gradient descent over the satellite’s n<sub>k</sub> points. Here each pass uses all the points at once, so E epochs means E weight updates.</td></tr><tr><td>Learning rate η</td><td>The step size: each update is w ← w − η · (average gradient). The slider runs 0.1 to 2.0. A step that is too large overshoots the low point of the loss, so the loss bounces instead of falling, and one that is too small is slow. This toy’s loss is gentle, so even 2.0 shows no visible overshoot: a larger η mainly reaches the plateau in fewer rounds. Clear bouncing needs a step many times larger than the slider allows. If the global loss rises and falls from round to round, that is usually the choice of satellites (clients per round m below K), not the step size.</td></tr><tr><td>Clients/round m</td><td>How many of the K satellites are picked at random each round. The ratio m / K is the fraction picked.</td></tr><tr><td>Epoch schedule</td><td>2 local epochs in rounds 1 and 2, then 5.</td></tr><tr><td>Local loss, global loss</td><td>Average log-loss (cross-entropy) over a set of points; lower is better. Local loss uses that satellite’s own data. Global loss uses the 300 test points.</td></tr><tr><td>Global accuracy</td><td>The share of the 300 test points the global line classifies correctly.</td></tr>
</table></div>
<p class="cap"><b>One independent check.</b> Because the two clouds overlap, even the best possible straight line is right only about 93% of the time: the cloud centres are 2.69 apart with spread 0.9, which gives a ceiling of Φ(1.49) ≈ 93.3% (Φ is the standard normal cumulative distribution function: the share of a bell curve that lies below a point 1.49 standard deviations above its centre). The global curve levels off around 93 to 94%, as that ceiling predicts. With 300 test points, expect about ±1.5 points of sampling noise.</p>
</section>
<section class="box sec" id="s6" style="margin-top:16px">
<h2>6 Tuning: who trains, for how long, and how results are combined</h2>
<p class="cap" style="margin:0 0 8px">Federated learning adds knobs that ordinary training does not have. Most of them are controlled on the server.</p>
<div class="loop l4">
<div><b>Client selection</b>With a handful of clients, use all of them every round. With millions of phones, pick a few hundred, at most a few thousand, per round; adding more has diminishing returns. Random choice is the common default.</div>
<div><b>Client configuration</b>The server sends settings along with the model each round: local epochs, learning rate, anything the client needs to train or evaluate. Settings can change from round to round.</div>
<div><b>Aggregation</b>Federated averaging (FedAvg) is the baseline. Others improve on it in some settings. FedAdam applies the Adam optimizer, which adapts the step size of each weight, on the server. FedMedian takes the median of each weight across clients instead of the mean, so one extreme client counts for less. <span style="white-space:nowrap">q-FedAvg</span> gives clients with higher loss more weight, aiming for a more even accuracy across clients.</div>
<div><b>Client-side processing</b>Each client can pre-process data, control its local training, and post-process the weights before sending them back.</div>
</div>
<p class="cap">Example: rounds 1 and 2 train 2 local epochs and round 3 onward trains 5. With 10 clients, picking 60% samples 6 per round, and client-side evaluation can be switched off. The demo in section 5 has matching controls: <b>Clients per round</b> and <b>Epoch schedule</b>. Cyclic training is another option, where the model visits one client after another; it is useful but, strictly speaking, not federated learning.</p>
</section>

<section class="box sec" id="s7">
<h2>7 Privacy: federated learning is not private by default</h2>
<p class="cap" style="margin:0 0 8px">Keeping raw data on the device is data minimization. The model updates that leave the device can still leak information, so FL is usually paired with privacy-enhancing technologies (PETs). The attacker may be a client, the server or a third party.</p>
<p class="cap" style="margin:0 0 4px"><b>Why updates can leak at all.</b> A model update is computed from the client’s data, so it is a function of that data. The three attacks below ask for progressively more.</p>
<div class="loop l3">
<div><b>Membership inference</b>This attack works out whether one exact record was in the training data. The attacker holds a candidate record and checks how the model responds to it. Models tend to be more confident on examples they were trained on, and that gap gives the answer away. Membership can itself be sensitive: the attack has been run on hospital discharge records. Satellite example: learning that a particular site’s images were used in training could reveal that someone imaged that site.</div>
<div><b>Attribute inference</b>This attack recovers facts about the training data that the model was never meant to learn: not whether record X is in, but what kind of data a client has. Research shows that in collaborative learning, a participant who sees the updates can infer that another participant’s photos include people wearing glasses, even though the model was trained to predict gender. Satellite example: an observer of a cloud-detection model’s updates might learn that a satellite mostly images coastline.</div>
<div><b>Reconstruction</b>This attack rebuilds the data itself. In one study a malicious server rebuilt a client’s images with surprisingly good quality. A well-known example, “Deep Leakage from Gradients”, recovered images pixel by pixel and text token by token from shared gradients.</div>
</div>
<p class="cap" style="margin-top:10px"><b>What attack studies show, and their limits.</b></p>
<ul class="cap" style="margin:4px 0 0;padding-left:20px">
<li><b>Membership inference on a finished model.</b> The classic study attacked a model only through its prediction outputs (black box) and did not involve federated training. Leakage grew with the number of output classes: on purchase data, attack precision rose from 0.51 with 2 classes to 0.94 with 100, where 0.5 is chance. Overfitting, where a model fits its training examples so closely that it does worse on new ones, raised it too, but it is not the only cause. Differentially private training would protect against this attack by construction, possibly at a cost in accuracy.</li>
<li><b>Attribute inference in collaborative learning.</b> This study targeted federated-style training directly. In FedAvg the attacker sees only the average of the updates, and the attacks still worked, though they weakened as participants were added (an AUC of about 0.8 with 12 participants in one test; AUC, the area under the receiver operating characteristic (ROC) curve, is the chance that the attacker ranks a true case above a false one, so 0.5 is guessing and 1.0 is perfect). Secure aggregation alone does not stop these attacks, since the attacker only needs the aggregate.</li>
<li><b>Gradient inversion.</b> This attack starts from the gradient of a single step on a small batch: up to 8 images of up to 64 × 64 pixels in the tests. FedAvg with several local steps was not analyzed. What stopped the attack: noise large enough to cut accuracy on CIFAR-100 (a standard set of 60,000 small colour photos in 100 classes; CIFAR stands for the Canadian Institute For Advanced Research) from 76.3% to 45.3%, 8-bit quantization (each number stored in 8 bits instead of 32; 53.7%), or zeroing more than about 20% of the gradient entries. 16-bit precision did not help.</li>
</ul>
<p class="cap" style="margin-top:10px">Three design principles limit exposure: <b>focused collection</b> (devices report only what the computation needs), <b>ephemeral reports</b> (the server never keeps per-device reports) and <b>only-in-aggregate</b> (engineers can only see the combined result).</p>
<h2 style="margin-top:16px">Differential privacy: clip, then add noise</h2>
<p class="cap" style="margin:0 0 8px">Differential privacy (DP) answers one question: could an observer tell whether a particular client took part? Imagine training one model on everyone’s data and a second with Alice’s client removed. DP guarantees the two results are nearly indistinguishable, so nothing in the result reveals whether Alice was there. How nearly is set by a number, ε (epsilon).</p>
<div class="f">A training procedure A is (ε, δ)-differentially private if, for any two datasets
D and D′ that differ by one client, and any set S of possible outcomes:

    P( A(D) ∈ S )  ≤  e^ε · P( A(D′) ∈ S ) + δ</div>
<p class="cap">Smaller ε means more privacy; at ε = 0 the two outcomes would be identically distributed. δ is a tiny allowed probability that the guarantee fails. For FL the natural unit is a whole client (“user-level” DP), a stronger promise than protecting one record, because a client holds many records. DP hides one client’s contribution. It does not hide facts that are true of the whole population, which is also what the model is supposed to learn.</p>
<p class="cap" style="margin:8px 0 0">Two ingredients make the promise possible. <b>Clipping</b> caps how much any one client’s update can change the result, which bounds its sensitivity, the most one client can change the result. <b>Noise</b> is then calibrated to that cap so the output looks statistically the same with or without any one client. Here is the central-DP recipe, step by step:</p>
<div class="loop">
<div><b>1 Update</b>Each client computes Δ<sub>k</sub> = w<sub>k</sub> − w_global: how far local training moved its weights.</div>
<div><b>2 Clip</b>If the size of Δ<sub>k</sub> is above C, shrink Δ<sub>k</sub> to size C. Now no client can move the model by more than C.</div>
<div><b>3 Average</b>The server combines the clipped updates, as in FedAvg.</div>
<div><b>4 Add noise</b>Gaussian (bell-curve) noise with standard deviation σ · C / m is added, where σ (sigma) is the noise multiplier you choose, C is the clip size from step 2, and m is how many clients were averaged. (A common variant writes z · S / the expected clients per round, where z is the noise multiplier and S the clip size, and caps each client’s weight at 1.)</div>
<div><b>5 Account</b>Real systems then compute ε from σ, the share of clients sampled each round, and the number of rounds (a “moments accountant”, a method for adding up the privacy spent over many rounds). The demo skips this step.</div>
</div>
<div class="loop l3">
<div><b>Why clip first</b>Without the clip, one client could send an enormous update and no fixed amount of noise would hide it. Noise has to be sized against a known maximum.</div>
<div><b>What it costs</b>The noise on the average shrinks as m grows, which is why DP suits many clients. For moderate privacy budgets, without a sufficiently large dataset, the noise can cause a large drop in accuracy.</div>
<div><b>Real numbers</b>A language model was trained over 763,430 users, about 5,000 per round, and reached ε ≈ 4.6 (δ = 10<sup>−9</sup>) with top-1 accuracy (how often the model’s single best next-word guess is right) of 17.49% against 17.62% without privacy. With 10<sup>8</sup> users the same noise gives ε ≈ 1.2. With enough users, privacy costs extra computation rather than accuracy. The same algorithm on a face-attribute task with up to 30 participants never converged; thousands of participants are needed.</div>
</div>
<p class="cap" style="margin-top:8px">Six satellites is therefore a harsh case, which makes the effect easy to see in the demo below.</p>
<h3 class="sub">Where the noise can be added</h3>
<div class="loop l3">
<div><b>Central DP</b>Clients send clipped updates; the server adds noise to the aggregate. Best accuracy, but you must trust the server not to look at individual updates first.</div>
<div><b>Local DP</b>Each client clips and adds noise before anything leaves. No trusted server is needed, but noise is added once per client instead of once in total, so it takes far more clients, or a weaker ε, to reach the same accuracy.</div>
<div><b>Secure aggregation</b>Another privacy-enhancing technique. Clients mask their updates cryptographically so the server can compute the sum but cannot read any single update. The sum itself can still leak, so it is usually combined with DP.</div>
</div>
<h2 style="margin-top:16px">What does privacy cost? Try it</h2>
<div class="two">
<div>
<div class="sl w"><label for="C7">Clip norm C</label><input id="C7" type="range" min="1" max="20" value="5"><output id="C7o">0.5</output></div>
<div class="sl w"><label for="S7">Noise multiplier σ</label><input id="S7" type="range" min="0" max="40" value="20"><output id="S7o">10.0</output></div>
<div class="ctl"><button type="button" id="nd">New noise draw</button></div>
<p class="key">C is the largest size a satellite’s update may have (the update is w<sub>k</sub> − w_global, three numbers, and its size is its length). σ is the noise multiplier: the noise added to the average has standard deviation σ × C ÷ m, with m = 6 here. The gray curve is plain FedAvg with no clip or noise. The bold curve is the average of 20 different noise draws; the thin dashed one is a single draw, which can land far from the average (press New noise draw to see another).</p>
<div class="stats" style="margin-top:14px">
<div><b id="a7">–</b><span>accuracy at round 30, no noise</span></div>
<div><b id="m7">–</b><span>average over 20 noise draws (lowest to highest)</span></div>
<div><b id="d7">–</b><span>this one noise draw</span></div>
<div><b id="n7">–</b><span>noise standard deviation added per round</span></div>
<div><b id="r7">–</b><span>rounds for the average to reach 80%</span></div>
</div>
</div>
<div>
<svg id="c7" viewBox="0 0 360 200" role="img" aria-label="Line chart of global accuracy over 30 rounds with and without clipping and noise"></svg>
<div class="lg" id="l7"></div>
</div>
</div>
<p class="cap est" style="margin:2px 0 8px;font-style:italic">Not exact: shown to illustrate a trend.</p>
<p class="cap">Simplified central DP on the same six satellites: each update is clipped to norm C, the weighted average is taken, then Gaussian noise with standard deviation σ·C/6 is added. A small C slows learning on its own, and a large σ makes the curve jump around. This shows the trade-off, not a guarantee. No privacy budget ε is computed, a single noise draw is one random outcome (the average of 20 is shown too), and the demo weights each satellite by n<sub>k</sub> / n while sizing the noise as if each counted 1/6. The standard recipe caps every client’s weight at 1 so the sensitivity stays bounded; with equal weights its noise is σ · C / m, the form used here, but weighting by n<sub>k</sub> / n is a different estimator. So σ is a teaching dial rather than a calibrated privacy setting. Privacy enhancements often cost utility, and noisy training converges more slowly, typically needing 50 or more rounds.</p>
</section>

<section class="box sec" id="s8">
<h2>8 Bandwidth: what a federated run costs to move</h2>
<p class="cap" style="margin:0 0 8px">Every round moves a model to each chosen client and an update back. Even a small model adds up fast. Sizes are in megabytes (MB), gigabytes (GB, 1,000 MB) and terabytes (TB, 1,000 GB). Link speeds are in megabits per second (Mbps), and one byte is 8 bits, so a 53 MB model is 424 megabits.</p>
<div class="f">total traffic = (model sent + update returned) × clients × fraction chosen per round × rounds</div>
<div class="two" style="margin-top:12px">
<div>
<p class="key" style="margin:0 0 6px">Example models: Pythia-14M is a small open language model with 14 million weights; MobileNetV3 is a compact image-classification network built for phones; ResNet50 is a 50-layer image-classification network.</p>
<div class="ctl" style="margin:0 0 4px"><button type="button" data-ms="53">Pythia-14M, 53 MB</button><button type="button" data-ms="22">MobileNetV3, 22 MB</button><button type="button" data-ms="98">ResNet50, 98 MB</button></div>
<div class="ctl" style="margin:0 0 6px"><button type="button" data-p="53,2,100,1,100,100">2 clients, 1 round</button><button type="button" data-p="53,100,50,1000,100,100">100 clients, half per round, 1000 rounds</button></div>
<div class="sl w"><label for="MS">Model size (MB)</label><input id="MS" type="number" min="1" max="5000" value="53" style="width:100%;font:inherit;padding:4px 6px"><output id="MSo"></output></div>
<div class="sl w"><label for="N8">Clients</label><input id="N8" type="range" min="2" max="1000" value="2"><output id="N8o">2</output></div>
<div class="sl w"><label for="FR">Chosen per round</label><input id="FR" type="range" min="10" max="100" step="10" value="100"><output id="FRo">100%</output></div>
<div class="sl w"><label for="RD">Rounds</label><input id="RD" type="range" min="1" max="1000" value="1"><output id="RDo">1</output></div>
<div class="sl w"><label for="LY">Layers communicated</label><input id="LY" type="range" min="10" max="100" step="5" value="100"><output id="LYo">100%</output></div>
<div class="sl w"><label for="RT">Returned update size</label><input id="RT" type="range" min="5" max="100" step="5" value="100"><output id="RTo">100%</output></div>
</div>
<div>
<div class="f" id="calc" style="margin-top:0"></div>
<div class="stats" style="margin-top:14px">
<div><b id="tot8">–</b><span>total traffic</span></div>
<div><b id="per8">–</b><span>per client, per round</span></div>
<div><b id="tm8">–</b><span>per satellite, per round, on Module 2’s links</span></div>
</div>
</div>
</div>
<p class="cap">Check: a 53 MB model, 2 clients, all chosen, 1 round gives (53 + 53) × 2 = 212 MB. The time line uses Module 2’s example links: 15 Mbps to send the model up to a satellite and 111 Mbps for its update to come down. Model sizes for MobileNetV3 and ResNet50 are the ones used in Module 2.</p>
<p class="cap"><b>What the sliders mean.</b> <i>Model size</i> is the size of the weights in MB. <i>Clients</i> is the total cohort, not the number picked. <i>Chosen per round</i> is the share picked each round. <i>Rounds</i> is how many times the loop runs. <i>Layers communicated</i> is the share of the model that travels in each direction, as when only some layers change (pre-trained models). <i>Returned update size</i> is what comes back as a share of what went out (sparsification, quantization). The two percentage sliders are what-ifs you choose, not measured values; for example, going from 32-bit to 8-bit numbers would be 25%.</p>
<p class="cap"><b>How far to trust the totals and times.</b> The totals are arithmetic, not measurements, and they ignore protocol overhead and retransmitted packets. The time line is size × 8 ÷ link rate, using 15 Mbps up to a satellite and 111 Mbps down. Real links lose packets and vary, which Module 2 covers.</p>
<p class="cap est" style="margin:2px 0 8px;font-style:italic">Not exact: shown to illustrate a trend.</p>
<p class="cap"><b>A note on directions.</b> In FL, “upload” means client to server. For a satellite that is the satellite-to-ground downlink, the faster direction here (111 Mbps), while the model the server sends out travels on the slower ground-to-satellite uplink (about 15 Mbps, with 5.2 times the packet loss). On phones, upload is usually the slow side. In satellite FL, these figures suggest the broadcast of the model is the more constrained leg.</p>
<div class="loop l2">
<div><b>Sparsification</b>Send only the biggest changes. Keep the k largest-magnitude entries of the update (top-k) and treat the rest as zero, so you transmit just those values and their positions. It tends to save more late in training, when more entries are small. It is one way to shrink each round’s message, but tricks borrowed from data-center training, such as carrying the dropped error into later rounds, can go stale in FL because a client may not be picked again for a long time.</div>
<div><b>Quantization</b>Use fewer bits per number. Weights are usually 32-bit floating-point numbers (floats), so storing each in 8 bits makes the update 4 times smaller, and in 4 bits, 8 times smaller (simple arithmetic). Substantial quantization (for example 4 bits) has been reported to work without losing accuracy on EMNIST (Extended MNIST, a data set of handwritten letters and digits). It does not combine freely with everything: standard secure aggregation and DP noise were not designed for quantized values, so combining them is still open research.</div>
<div><b>Pre-trained models</b>Start from a model that already fits the task and train only part of it, so only the parts that change need to travel. A LoRA (low-rank adaptation) example: one 1024 × 1024 weight matrix has 1,048,576 values, but rank-8 adapters B (1024 × 8) and A (8 × 1024) have 16,384, which is 64× fewer to train and send. The catch: averaging A and B separately is not the same as averaging their product B·A, which adds “cross-term noise”. Methods such as FLoRA (federated LoRA, which stacks the clients’ adapters instead of averaging them) and FFA-LoRA (Federated Freeze A LoRA, which freezes A so that only B is trained and averaged) fix that.</div>
<div><b>More local training</b>Run several epochs on each client before sending, so fewer rounds, and fewer transfers, are needed. The warning: with too many epochs, each client’s model drifts toward its own data and the average can get worse. Whether that happens depends on how different the clients’ data are, which Module 3 revisits with non-IID data. The epoch schedule in section 5 is a mild version: few epochs first, more later.</div>
</div>
</section>

<section class="box sec" id="keypoints" style="margin-top:16px">
<h2>Key points</h2>
<ul class="cap" style="margin:4px 0 0;padding-left:20px">
<li>In federated learning the data stays where it is. Each client trains locally and sends only weights, and the server averages them, giving a client with more data (n<sub>k</sub> / n) more say.</li>
<li>Clients’ data is rarely alike. When it is not IID (independent and identically distributed), local models drift toward their own data and the average can be worse than pooled training. This module keeps the data IID so the mechanics stay clear, and Module 3 breaks that on purpose.</li>
<li>A round runs in phases: the server sends, the clients train, the clients return, the server aggregates. Sending and receiving do not happen at once, and the slowest client sets the pace of a synchronous round.</li>
<li>Updates can still leak information. Clipping each update and adding noise (differential privacy) limits that, at a cost in accuracy that is largest when few clients take part.</li>
<li>Traffic is (model sent + update returned) × clients × fraction chosen × rounds. Smaller updates, fewer layers and fewer rounds all cut it.</li>
<li>The main knobs are which clients take part, how many local epochs they run, and how results are combined. More local epochs make each round more productive but can pull each client toward its own data, which Module 3 explores.</li>
</ul>
</section>

<section class="box q" style="margin-top:16px">
<h2>Check your understanding</h2>
<p id="qscore" role="status" style="font-size:13px;color:var(--mute);margin:0 0 6px"></p>
<div class="q2">
<div><b>1.</b> One satellite holds twice as many images as another. In FedAvg, how much does its trained model count in the average?</div>
<button type="button" data-m="Not quite. FedAvg weights each client by its share of the data, n_k / n, so a larger dataset pulls the average harder. Try the Satellites slider and watch the Share column.">The same as the other one</button>
<button type="button" data-m="Right. The weight is n_k / n, so twice the images means twice the influence. That is also why one satellite with lots of skewed data can drag the global model, which Module 3 explores.">Twice as much, in proportion to its data</button>
<button type="button" data-m="Not quite. The server starts with a global model but learns nothing on its own: it only averages what the satellites send back.">Not at all, only the server’s model counts</button>
<p class="fb" role="status" style="min-height:44px;margin:10px 0 0;font-size:14px"></p>
</div>
<div class="q2" style="margin-top:14px">
<div><b>2.</b> In differential privacy for FL, what does clipping do?</div>
<button type="button" data-m="Not quite. Clipping does not remove anyone from training; it shrinks each client’s update to a maximum size.">It removes clients whose updates look suspicious</button>
<button type="button" data-m="Right. Capping each update bounds how much any single client can change the result, and that bound is what lets the noise be set to hide any one client.">It caps how much one client’s update can change the result</button>
<button type="button" data-m="Not quite. That is what sparsification and quantization do (section 8). Clipping is about limiting sensitivity, not size on the wire.">It compresses updates to save bandwidth</button>
<p class="fb" role="status" style="min-height:44px;margin:10px 0 0;font-size:14px"></p>
</div>
<div class="q2" style="margin-top:14px">
<div><b>3.</b> A 53 MB model goes to 100 clients, 20% are chosen each round, and an update of the same size comes back. Total traffic after 10 rounds?</div>
<button type="button" data-m="Not quite. 2,120 MB is one round: 53 × 2 × 100 × 0.2. Multiply by the 10 rounds.">2,120 MB</button>
<button type="button" data-m="Right. 53 × 2 × 100 × 0.2 × 10 = 21,200 MB, about 21 GB.">21,200 MB</button>
<button type="button" data-m="Not quite. 106,000 MB forgets that only 20% of the clients are chosen each round.">106,000 MB</button>
<p class="fb" role="status" style="min-height:44px;margin:10px 0 0;font-size:14px"></p>
</div>
<div class="q2" style="margin-top:14px">
<div><b>4.</b> The satellites’ data is not alike (not IID). What can go wrong with plain averaging?</div>
<button type="button" data-m="Not quite. Identifying the sender is not the issue. The problem is what the updates contain.">The server can no longer tell which satellite sent which update</button>
<button type="button" data-m="Not quite. Averaging does not cancel differences in the data. Each local model moves toward its own data, and the average of those can sit away from what is best for everyone.">Nothing, because averaging always cancels out the differences</button>
<button type="button" data-m="Right. This is the catch of non-IID data. This module keeps the data IID so the mechanics stay clear, and Module 3 breaks that on purpose.">Local models drift toward their own data, so the average can be worse than pooled training</button>
<p class="fb" role="status" style="min-height:44px;margin:10px 0 0;font-size:14px"></p>
</div>
<div class="q2" style="margin-top:14px">
<div><b>5.</b> In a synchronous round, what sets how long the round takes?</div>
<button type="button" data-m="Right. The server cannot average until the updates it is waiting for have arrived, so the slowest client sets the pace.">The slowest client the server waits for</button>
<button type="button" data-m="Not quite. Clients do not copy each other. The server waits for the updates it needs, so a fast client does not shorten the round.">The fastest client, because the others copy its result</button>
<button type="button" data-m="Not quite. The server holds no training data in this setup. The time depends on the clients and the links.">The size of the server’s own dataset</button>
<p class="fb" role="status" style="min-height:44px;margin:10px 0 0;font-size:14px"></p>
</div>
<div class="q2" style="margin-top:14px">
<div><b>6.</b> With differential privacy, when is the accuracy cost largest?</div>
<button type="button" data-m="Not quite. The noise added to the average has standard deviation σ × C ÷ m, where m is the number of clients, so more clients means less noise. Try the demo with a different m in mind.">When many clients take part</button>
<button type="button" data-m="Right. The noise on the average is σ × C ÷ m, so fewer clients (a smaller m) means more noise on the average, and each client’s update is a bigger part of the result.">When few clients take part</button>
<button type="button" data-m="Not quite. The noise on the average is σ × C ÷ m, so it depends on how many clients are averaged.">It is the same whatever the number of clients</button>
<p class="fb" role="status" style="min-height:44px;margin:10px 0 0;font-size:14px"></p>
</div>
<div class="q2" style="margin-top:14px">
<div><b>7.</b> Everything else stays the same and the fraction of clients chosen each round goes from 20% to 40%. What happens to the total traffic?</div>
<button type="button" data-m="Not quite. Traffic is (model sent + update returned) × clients × fraction chosen × rounds, so the fraction is a direct multiplier.">It stays the same, because the model size has not changed</button>
<button type="button" data-m="Not quite. The fraction doubled, from 0.2 to 0.4, so the traffic doubles. It does not grow by 20 percentage points of itself.">It goes up by about 20%</button>
<button type="button" data-m="Right. Traffic is proportional to the fraction chosen, so 0.4 instead of 0.2 means twice as many transfers per round.">It doubles</button>
<p class="fb" role="status" style="min-height:44px;margin:10px 0 0;font-size:14px"></p>
</div>
</section>


<script>
/* quiz handler is in the main script */
</script>
<p class="key" style="margin-top:16px">Next: Module 2, the case against downloading all the satellite data (choose it from the module list at the top of the page)</p>
</main>
<script>
(function(){
function rng(a){return function(){a|=0;a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
function gaussFrom(r){return function(){return Math.sqrt(-2*Math.log(1-r()))*Math.cos(6.2832*r())}}
var SZ=[40,24,60,30,46,20],COL=['--c0','--c1','--c2','--c3','--c4','--c5'];
var $=function(i){return document.getElementById(i)};
function mkData(K,seed){var R=rng(seed),gs=gaussFrom(R);function pt(){var c=R()<.5?0:1,m=c?1:-1;return{x:m+gs()*.9,y:m*.9+gs()*.9,c:c}}
var test=[],cl=[],i,j;for(i=0;i<300;i++)test.push(pt());for(i=0;i<K;i++){var d=[];for(j=0;j<SZ[i];j++)d.push(pt());cl.push({d:d,w:null,on:true})}return{test:test,cl:cl}}
function sg(z){return 1/(1+Math.exp(-z))}
function ev(w,d){var l=0,a=0;d.forEach(function(p){var q=sg(w[0]*p.x+w[1]*p.y+w[2]);q=Math.min(Math.max(q,1e-9),1-1e-9);l-=p.c?Math.log(q):Math.log(1-q);if((q>.5)==!!p.c)a++});return{loss:l/d.length,acc:a/d.length}}
function train(w0,d,E,lr){var w=w0.slice();for(var e=0;e<E;e++){var g=[0,0,0];d.forEach(function(p){var r=sg(w[0]*p.x+w[1]*p.y+w[2])-p.c;g[0]+=r*p.x;g[1]+=r*p.y;g[2]+=r});for(var k=0;k<3;k++)w[k]-=lr*g[k]/d.length}return w}
function aggregate(g,parts,dp,rn){var n=0,k,out=[0,0,0];parts.forEach(function(c){n+=c.d.length});
if(!dp){parts.forEach(function(c){var s=c.d.length/n;for(k=0;k<3;k++)out[k]+=s*c.w[k]});return out}
parts.forEach(function(c){var dl=[c.w[0]-g[0],c.w[1]-g[1],c.w[2]-g[2]],nm=Math.sqrt(dl[0]*dl[0]+dl[1]*dl[1]+dl[2]*dl[2]),f=nm>dp.C?dp.C/nm:1,s=c.d.length/n;for(k=0;k<3;k++)out[k]+=s*f*dl[k]});
var sd=dp.sigma*dp.C/parts.length;return[g[0]+out[0]+sd*rn(),g[1]+out[1]+sd*rn(),g[2]+out[2]+sd*rn()]}
function pickSel(K,m,r){var idx=[],i,j,t;for(i=0;i<K;i++)idx.push(i);for(i=K-1;i>0;i--){j=Math.floor(r()*(i+1));t=idx[i];idx[i]=idx[j];idx[j]=t}return idx.slice(0,m)}
function epochsFor(o,round){return o.sched?(round<2?2:5):o.E}
function sim(o){var D=mkData(o.K,7),g=[1.2,-1.4,.3],h=[ev(g,D.test).acc],r=rng(99),rn=gaussFrom(rng(o.nseed||123)),cyc=0;
for(var t=0;t<o.rounds;t++){var E=epochsFor(o,t);
if(o.mode=='cyclic'){var c=D.cl[cyc%o.K];cyc++;g=train(g,c.d,E,o.lr)}
else{var sel=pickSel(o.K,o.m,r),parts=sel.map(function(i){var c=D.cl[i];return{d:c.d,w:train(g,c.d,E,o.lr)}});g=aggregate(g,parts,o.dp,rn)}
h.push(ev(g,D.test).acc)}return h}
function v(n){return getComputedStyle(document.documentElement).getPropertyValue(n)}
function f2(x){return(x>=0?'+':'−')+Math.abs(x).toFixed(2)}

/* ---------- section 5: step-by-step demo ---------- */
var S={K:4,E:5,sched:false,lr:.5,m:4,round:0,phase:0,g:[1.2,-1.4,.3],cl:[],hist:[],test:[],timer:null,rs:null};
function init(){var D=mkData(S.K,7);S.test=D.test;S.cl=D.cl;S.g=[1.2,-1.4,.3];S.round=0;S.phase=0;S.rs=rng(99);S.hist=[ev(S.g,S.test).acc]}
function step(){var p=S.phase;
if(p==0||p==3){var m=Math.min(S.m,S.cl.length),sel=pickSel(S.cl.length,m,S.rs);S.cl.forEach(function(c,i){c.on=sel.indexOf(i)>=0;c.w=c.on?S.g.slice():null});S.phase=1}
else if(p==1){var E=epochsFor(S,S.round);S.cl.forEach(function(c){if(c.on)c.w=train(S.g,c.d,E,S.lr)});S.phase=2}
else{var parts=S.cl.filter(function(c){return c.on});S.g=aggregate(S.g,parts,null,null);S.round++;S.hist.push(ev(S.g,S.test).acc);S.phase=3}
draw()}
function X(x){return(x+3)/6*360}function Y(y){return 360-(y+3)/6*360}
function line(w,st,dash,sw,op){var a=w[0],b=w[1],c=w[2],x1,y1,x2,y2;
if(Math.abs(b)>1e-4){x1=-3;x2=3;y1=-(a*x1+c)/b;y2=-(a*x2+c)/b}else{x1=x2=-c/(a||1e-4);y1=-3;y2=3}
return'<line x1="'+X(x1)+'" y1="'+Y(y1)+'" x2="'+X(x2)+'" y2="'+Y(y2)+'" stroke="'+st+'" stroke-width="'+sw+'"'+(dash?' stroke-dasharray="6 5"':'')+' opacity="'+op+'" stroke-linecap="round"/>'}
function msg(){var K=S.cl.length,on=S.cl.filter(function(c){return c.on}).length,E=epochsFor(S,S.round);
if(S.phase==0)return'Ready. The global model is a straight line that separates the two classes badly. Press Next step to begin a round.';
if(S.phase==1)return'The server picked '+on+' of '+K+' satellites and sent them the global weights.'+(on<K?' The faded ones sit this round out.':' All dashed lines now sit exactly on the global line.');
if(S.phase==2)return'Each picked satellite runs '+E+' local epoch'+(E>1?'s':'')+' of gradient descent on its own data only. Its line moves toward what its local data prefers. Only the weights leave the satellite, never the data.';
return'The server averages the weights of the '+on+' picked satellite'+(on>1?'s':'')+', giving those with more data more say. The new global line sits between their local ones. Press Next step to start another round.'}
function draw(){
var h='<rect width="360" height="360" fill="none"/><line x1="180" y1="0" x2="180" y2="360" stroke="'+v('--line')+'"/><line x1="0" y1="180" x2="360" y2="180" stroke="'+v('--line')+'"/>';
S.cl.forEach(function(c,i){var col=v(COL[i]),op=(S.phase>=1&&!c.on)?.18:.75;c.d.forEach(function(p){var x=X(Math.max(-2.95,Math.min(2.95,p.x))),y=Y(Math.max(-2.95,Math.min(2.95,p.y)));
h+=p.c?'<path d="M'+x+' '+(y-5)+'L'+(x+5)+' '+y+'L'+x+' '+(y+5)+'L'+(x-5)+' '+y+'Z" fill="'+col+'" opacity="'+op+'"/>':'<circle cx="'+x+'" cy="'+y+'" r="4" fill="'+col+'" opacity="'+op+'"/>'})});
if(S.phase>=1)S.cl.forEach(function(c,i){if(c.w)h+=line(c.w,v(COL[i]),1,2,S.phase==3?.45:.95)});
h+=line(S.g,v('--ink'),0,3.5,1);$('plot').innerHTML=h;
var m=ev(S.g,S.test);$('sRound').textContent=S.round;$('sAcc').textContent=(m.acc*100).toFixed(0)+'%';$('sLoss').textContent=m.loss.toFixed(2);
$('say').textContent=msg();
var st=$('steps').children,i;for(i=0;i<3;i++)st[i].className='st'+((S.phase==i+1)?' on':'');
var parts=S.cl.filter(function(c){return c.on}),n=0,nAll=0;parts.forEach(function(c){n+=c.d.length});S.cl.forEach(function(c){nAll+=c.d.length});
var t='<tr><th>Satellite</th><th>Images n<sub>k</sub></th><th>Share n<sub>k</sub>/n</th><th>Weights sent (w₁, w₂, bias)</th><th>Local loss</th></tr>';
S.cl.forEach(function(c,i){var w=c.w&&S.phase>=2?c.w:null;
t+='<tr><td><span class="dot" style="background:'+v(COL[i])+'"></span>Sat '+(i+1)+'</td><td>'+c.d.length+'</td><td>'+(c.on?(c.d.length/n*100).toFixed(0)+'%':'idle')+'</td><td>'+(w?w.map(f2).join(', '):'–')+'</td><td>'+(w?ev(w,c.d).loss.toFixed(2):'–')+'</td></tr>'});
t+='<tr><td><b>Global</b></td><td>'+nAll+'</td><td>100%</td><td>'+S.g.map(f2).join(', ')+'</td><td>'+m.loss.toFixed(2)+'</td></tr>';$('tbl').innerHTML=t;
var F='w_global = Σ (n_k / n) · w_k'+(parts.length<S.cl.length?'   over the '+parts.length+' picked satellites':'')+'\n';
if(S.phase>=2){for(var k=0;k<3;k++){F+=['w₁','w₂','bias'][k]+'  = '+parts.map(function(c){return(c.d.length/n).toFixed(2)+'×'+(c.w[k]).toFixed(2)}).join(' + ')+'\n'}}
else F+='(train locally first to see the numbers)';
$('formula').textContent=F;
lines('chart',[{col:'--acc',vals:S.hist,w:2.5,dots:1}],Math.max(S.hist.length-1,5))}
function lines(id,series,N){var W=360,Ht=200,px=36,py=14,iw=W-px-12,ih=Ht-py-28,a='',i,yy;
for(i=0;i<=4;i++){yy=py+ih-ih*i/4;a+='<line x1="'+px+'" x2="'+(W-12)+'" y1="'+yy+'" y2="'+yy+'" stroke="'+v('--line')+'"/><text x="'+(px-6)+'" y="'+(yy+4)+'" font-size="11" text-anchor="end" fill="'+v('--mute')+'">'+(i*25)+'%</text>'}
var sp=N>20?5:(N>10?2:1);
for(i=0;i<=N;i+=sp)a+='<text x="'+(px+iw*i/N)+'" y="'+(Ht-16)+'" font-size="11" text-anchor="middle" fill="'+v('--mute')+'">'+i+'</text>';
series.forEach(function(s){var d='';s.vals.forEach(function(q,i){d+=(i?'L':'M')+(px+iw*i/N).toFixed(1)+' '+(py+ih-ih*q).toFixed(1)+' '});
a+='<path d="'+d+'" fill="none" stroke="'+v(s.col)+'" stroke-width="'+(s.w||2)+'"'+(s.dash?' stroke-dasharray="5 4"':'')+' stroke-linejoin="round"/>';
if(s.dots)s.vals.forEach(function(q,i){a+='<circle cx="'+(px+iw*i/N)+'" cy="'+(py+ih-ih*q)+'" r="3.5" fill="'+v(s.col)+'"/>'})});
a+='<text x="'+(px+iw/2)+'" y="'+(Ht-3)+'" font-size="12" text-anchor="middle" fill="'+v('--mute')+'">communication round</text>';
$(id).innerHTML=a}
function legend(id,series){$(id).innerHTML=series.map(function(s){return'<span><i style="background:'+v(s.col)+'"></i>'+s.name+'</span>'}).join('')}
function stop(){if(S.timer){clearInterval(S.timer);S.timer=null;$('auto').textContent='Auto-play'}}
function full(){do step();while(S.phase!=3)}
$('next').onclick=function(){stop();step()};
$('round').onclick=function(){stop();full()};
$('auto').onclick=function(){if(S.timer){stop();return}$('auto').textContent='Pause';S.timer=setInterval(function(){if(S.round>=25){stop();return}step()},1100)};
$('reset').onclick=function(){stop();init();draw()};
$('K').oninput=function(){var K=+this.value;$('Ko').textContent=K;S.K=K;S.m=K;$('M').max=K;$('M').value=K;$('Mo').textContent=K;stop();init();draw()};
$('M').oninput=function(){S.m=+this.value;$('Mo').textContent=this.value};
$('SC').onchange=function(){S.sched=this.checked;$('SCo').textContent=this.checked?'on':'off';$('E').disabled=this.checked};
$('E').oninput=function(){$('Eo').textContent=this.value;S.E=+this.value};
$('L').oninput=function(){S.lr=this.value/10;$('Lo').textContent=(this.value/10).toFixed(1)};

/* ---------- labs (sections 6 and 7) ---------- */
var BASE={K:6,m:6,E:5,sched:false,lr:.5,rounds:15,mode:'fedavg'};
function o(x){var r={},k;for(k in BASE)r[k]=BASE[k];for(k in x)r[k]=x[k];return r}
function firstAt(h,t){for(var i=0;i<h.length;i++)if(h[i]>=t)return i;return null}
var nseed=123,base30=sim(o({rounds:30}));
function draw7(){var C=+$('C7').value/10,sgm=+$('S7').value/2;$('C7o').textContent=C.toFixed(1);$('S7o').textContent=sgm.toFixed(1);
var d=sim(o({rounds:30,dp:{C:C,sigma:sgm},nseed:nseed})),runs=[],i,t;
for(i=0;i<20;i++)runs.push(sim(o({rounds:30,dp:{C:C,sigma:sgm},nseed:5000+i*37})));
var avg=[];for(t=0;t<=30;t++){var sm=0;runs.forEach(function(h){sm+=h[t]});avg.push(sm/runs.length)}
var fin=runs.map(function(h){return h[30]}),lo=Math.min.apply(null,fin),hi=Math.max.apply(null,fin),f=firstAt(avg,.8);
var ser=[{name:'No noise',col:'--mute',vals:base30},{name:'Clip + noise, average of 20 draws',col:'--acc',vals:avg,w:2.5},{name:'Clip + noise, this one draw',col:'--c0',vals:d,dash:1}];
lines('c7',ser,30);legend('l7',ser);
$('a7').textContent=(base30[30]*100).toFixed(0)+'%';$('m7').textContent=(avg[30]*100).toFixed(0)+'% ('+(lo*100).toFixed(0)+'–'+(hi*100).toFixed(0)+'%)';$('d7').textContent=(d[30]*100).toFixed(0)+'%';$('n7').textContent=(sgm*C/6).toFixed(2);$('r7').textContent=f===null?'not reached':f}
$('C7').oninput=draw7;$('S7').oninput=draw7;$('nd').onclick=function(){nseed+=17;draw7()};

/* ---------- section 8: bandwidth calculator ---------- */
function fmt(mb){if(mb<1e3&&mb.toFixed(mb<10?1:0)==='1000')mb=1e3;return mb>=1e6?(mb/1e6).toFixed(2)+' TB':mb>=1e3?(mb/1e3).toFixed(mb>=1e5?0:1)+' GB':(mb<10?mb.toFixed(1):mb.toFixed(0))+' MB'}
function fmtT(s){return s<90?s.toFixed(1)+' s':(s/60).toFixed(1)+' min'}
function nn(x){return String(+x.toFixed(1))}
function calc(){var MS=Math.max(1,+$('MS').value||1),N=+$('N8').value,FR=+$('FR').value/100,RD=+$('RD').value,LY=+$('LY').value/100,RT=+$('RT').value/100;
$('N8o').textContent=N;$('FRo').textContent=Math.round(FR*100)+'%';$('RDo').textContent=RD;$('LYo').textContent=Math.round(LY*100)+'%';$('RTo').textContent=Math.round(RT*100)+'%';
var out=MS*LY,back=out*RT,per=out+back,tot=per*N*FR*RD;
$('calc').textContent='('+nn(out)+' MB sent + '+nn(back)+' MB returned)\n× '+N+' clients × '+Math.round(FR*100)+'% chosen per round\n× '+RD+' round'+(RD>1?'s':'')+'\n= '+fmt(tot);
$('tot8').textContent=fmt(tot);$('per8').textContent=fmt(per);$('tm8').textContent=fmtT(out*8/15)+' in, '+fmtT(back*8/111)+' out'}
Array.prototype.forEach.call(document.querySelectorAll('[data-ms]'),function(b){b.onclick=function(){$('MS').value=b.getAttribute('data-ms');calc()}});
Array.prototype.forEach.call(document.querySelectorAll('[data-p]'),function(b){b.onclick=function(){var p=b.getAttribute('data-p').split(',');['MS','N8','FR','RD','LY','RT'].forEach(function(id,i){$(id).value=p[i]});calc()}});
['MS','N8','FR','RD','LY','RT'].forEach(function(id){$(id).oninput=calc});

/* ---------- quiz ---------- */
(function(){var qs=document.querySelectorAll('.q2'),tot=qs.length,ans=0,ok=0,sc=document.getElementById('qscore');function upd(){sc.textContent=ans?('Answered '+ans+' of '+tot+' · '+ok+' right on the first try'):('Choose an answer for each of the '+tot+' questions. You get feedback straight away.')}Array.prototype.forEach.call(qs,function(q){var fb=q.querySelector('.fb'),done=false;Array.prototype.forEach.call(q.querySelectorAll('button'),function(b){b.onclick=function(){var m=b.getAttribute('data-m');fb.textContent=m;if(!done){done=true;ans++;if(/^Right/.test(m))ok++;upd()}}})});upd()})();

function drawAll(){draw();draw7()}
init();drawAll();calc();
if(window.matchMedia)matchMedia('(prefers-color-scheme:dark)').addEventListener&&matchMedia('(prefers-color-scheme:dark)').addEventListener('change',drawAll);
})();
</script>
</body>
</html>
'''
