"""Module 2: Why not download all the satellite data

The whole lesson as one self-contained HTML document (text, charts, sliders and
quiz all run in the browser). It is shown by interface/fl_modules.py.
"""
TITLE = 'Module 2: Why not download all the satellite data'

HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Module 2: The case against downloading all the satellite data</title>
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
#qa{min-height:44px;margin:10px 0 0;font-size:14px}
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

.sl.v{grid-template-columns:170px 1fr 60px}
@media(max-width:480px){.sl.v{grid-template-columns:1fr 60px}.sl.v label{grid-column:1/-1}}
.trio{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
@media(max-width:760px){.trio{grid-template-columns:minmax(0,1fr)}}
.fig{min-width:0;border:1px solid var(--line);border-radius:10px;padding:10px;background:var(--surf)}
.fig .cap{margin-top:6px}
.sl.c{grid-template-columns:90px 1fr 46px;margin-top:4px}
h3.sub{font-size:15px;margin:16px 0 6px}

.sl.v{grid-template-columns:170px 1fr 84px}
@media(max-width:480px){.sl.v{grid-template-columns:1fr 84px}.sl.v label{grid-column:1/-1}}
.bar{height:22px;border-radius:6px;background:var(--line);overflow:hidden;margin-top:6px}
.bar i{display:block;height:100%;width:0}
a{color:var(--acc)}
.nav a{color:var(--ink)}
.ctl button.p{color:#fff}
.trio{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
@media(max-width:760px){.trio{grid-template-columns:minmax(0,1fr)}}
.fig{min-width:0;border:1px solid var(--line);border-radius:10px;padding:10px;background:var(--surf)}
.fig .cap{margin-top:6px}
h3.sub{font-size:15px;margin:16px 0 6px}
</style>
</head>
<body>
<main>
<p style="margin:0 0 6px"><span class="tag">Module 2 of 8 · Visual explanation with labs</span></p>
<h1>The case against downloading all the satellite data</h1>
<p class="lede">Federated learning only makes sense if the obvious alternative, sending every image to the ground and training there, does not work. This module tests that claim one obstacle at a time: too much data, too little contact, a poor link, and a satellite that is not a data center. Each section has a number you can move.</p>

<nav class="nav" aria-label="Module sections"><a href="#s1">1 Volume</a><a href="#s2">2 Contact</a><a href="#s3">3 The link</a><a href="#s4">4 Send the model</a><a href="#s5">5 Constellations</a><a href="#s6">6 Onboard compute</a><a href="#s7">7 Ownership</a><a href="#s8">8 Main points</a><a href="#s9">9 What FL leaves open</a></nav>

<section class="box sec" id="gloss">
<h2>Words used on this page</h2>
<div class="loop l3">
<div><b>Ground station (GS)</b>An antenna on Earth that talks to satellites. In FL terms it hosts the server (the “parameter server”, PS).</div>
<div><b>Pass / contact window</b>The stretch of time during which a satellite is in view of a GS and can send or receive. Outside it, nothing can be exchanged.</div>
<div><b>Uplink and downlink</b>Uplink is ground to satellite. Downlink is satellite to ground. In FL wording “upload” means client to server, which for a satellite uses the downlink. This page uses the satellite terms.</div>
</div>
</section>

<section class="box sec" id="s1">
<h2>1 Too much data: what an Earth-observation satellite collects</h2>
<p class="cap" style="margin:0 0 8px">Earth-observation satellites image continuously. Constellations such as Planet now collect over 350 million km² of imagery per day, which is tens to hundreds of terabytes per day for the whole constellation. About 45% of LEO satellites in orbit are on Earth-observation missions, and most systems still use a “bent-pipe” design: the satellite relays raw data to the ground. Short contact windows and limited bandwidth can cause weeks- or even months-long delays in downloading daily terabytes of satellite data.</p>
<div class="stats">
<div><b>350 M km²</b><span>imaged per day, Planet</span></div>
<div><b>10s–100s TB</b><span>per day, whole constellation</span></div>
<div><b>~45%</b><span>of LEO satellites are Earth observation</span></div>
<div><b>weeks–months</b><span>to download daily terabytes</span></div>
</div>
<h3 class="sub">Three ways to use what the satellite sees</h3>
<div class="trio">
<div class="fig"><svg id="a1" viewBox="0 0 240 150" role="img" aria-label="Bent pipe: all raw images are sent to the ground station"></svg><p class="cap"><b>Download everything (“bent pipe”).</b> Every image goes down first and training happens on the ground. This architecture hits a downlink bottleneck.</p></div>
<div class="fig"><svg id="a2" viewBox="0 0 240 150" role="img" aria-label="Onboard inference: the satellite sends results or compressed images"></svg><p class="cap"><b>Process on board, send less (inference).</b> The satellite runs a model and sends answers or compressed images. Nothing here improves a shared model.</p></div>
<div class="fig"><svg id="a3" viewBox="0 0 240 150" role="img" aria-label="Federated learning: the model goes up to the satellite and the update comes down"></svg><p class="cap"><b>Federated learning.</b> The global model goes up to the satellite, it trains on its own images, and only the update comes back down.</p></div>
</div>
<p class="cap" style="margin-top:6px">Arrow thickness shows roughly how much travels.</p>
<p class="cap est" style="margin:2px 0 8px;font-style:italic">Not exact: shown to illustrate a trend.</p>
<p class="cap" style="margin-top:12px"><b>Lab 1: time to send one day of imagery from one satellite.</b> The contact assumptions are fixed and shown below. You choose how much the satellite collects and how long it keeps running.</p>
<div class="two">
<div>
<div class="sl v"><label for="d1">Data per day D</label><input id="d1" type="range" min="0.05" max="5" step="0.05" value="1"><output id="d1o"></output></div>
<div class="sl v"><label for="n1">Days running N</label><input id="n1" type="range" min="1" max="90" value="30"><output id="n1o"></output></div>
<table class="wrap" style="margin-top:12px">
<tr><th>Fixed assumption</th><th>Value</th></tr>
<tr><td>Passes per day P₀</td><td>12</td></tr>
<tr><td>Minutes per pass T₀</td><td>5</td></tr>
<tr><td>Downlink rate R₀</td><td>111.01 Mbps</td></tr>
</table>
</div>
<div>
<div class="stats">
<div><b id="c1">–</b><span>can be downlinked per day</span></div>
<div><b id="s1s">–</b><span>of one day’s data fits</span></div>
</div>
<div class="bar"><i id="b1" style="background:var(--c1)"></i></div>
<div class="stats" style="margin-top:12px">
<div><b id="t1">–</b><span>to send one day of data</span></div>
<div><b id="bk1">–</b><span>unsent after N days</span></div>
</div>
<p class="cap" id="v1" style="margin-top:10px"></p>
</div>
</div>
<div class="f">capacity per day  C = P₀ × T₀ × 60 s × R₀ ÷ 8 ÷ 1000   (GB)
days to send one day  = D × 1000 ÷ C
unsent after N days   = N × (D × 1000 − C) ÷ 1000   (TB, if D × 1000 &gt; C)</div>
<p class="key"><b>Symbols.</b> D: terabytes collected per satellite per day (your choice). N: days the satellite keeps collecting without the backlog being cleared. P₀, T₀, R₀: passes per day, minutes per pass, and downlink rate in megabits per second. The ÷ 8 turns bits into bytes.</p>
<p class="cap"><b>Reading the numbers.</b> Capacity (about 50 GB per day) is 12 × 5 × 60 = 3,600 s of contact, times 111.01 Mbps, divided by 8. The 5 minutes per pass sits between the reported “under 6” and “about 4”. The data volume D is your choice. Real systems report “daily terabytes” without saying for how many satellites; the default of 1 TB is the smallest value that matches delays of weeks or months: at 1 TB the lab gives 20 days. The downlink rate was measured on a communications network, and an Earth-observation downlink can differ.</p>
<p class="cap est" style="margin:2px 0 8px;font-style:italic">Not exact: shown to illustrate a trend.</p>
</section>

<section class="box sec" id="s2">
<h2>2 Too little contact: a satellite is mostly out of reach</h2>
<p class="cap" style="margin:0 0 8px">A LEO satellite moves at about 7.6 km/s, so it is only in view of any one ground station briefly. Each satellite averages 12 contact opportunities a day, each under 6 minutes, so data transfer is unavailable for over 96% of the orbital period. A second view: contact lasts about 4 minutes of a 95-minute orbit. A typical ground-station contact is a few minutes.</p>
<h3 class="sub">Why a pass is short: the geometry</h3>
<svg id="orb" style="max-width:720px;margin:0 auto" viewBox="0 0 360 172" role="img" aria-label="A satellite orbiting Earth with a ground station; the part of the orbit in view is highlighted"></svg>
<div class="two" style="margin-top:8px">
<div>
<div class="sl v"><label for="oh">Orbit altitude h</label><input id="oh" type="range" min="300" max="2000" step="50" value="500"><output id="oho"></output></div>
<div class="sl v"><label for="oe">Minimum elevation e</label><input id="oe" type="range" min="5" max="40" value="20"><output id="oeo"></output></div>
</div>
<div>
<div class="stats" style="margin-top:0"><div><b id="op">–</b><span>orbital period</span></div><div><b id="ot">–</b><span>longest possible pass</span></div><div><b id="of">–</b><span>of one orbit in view</span></div></div>
<p class="cap" id="ov" style="margin-top:8px"></p>
</div>
</div>
<div class="f">visible half-angle   λ = arccos( R · cos e ÷ (R + h) ) − e
orbital period       T = 2π · √( (R + h)³ ÷ μ )
longest pass         = 2λ ÷ 360° × T      (satellite passes directly over the station)</div>
<p class="key"><b>Symbols.</b> R: Earth’s radius, 6,371 km. h: orbit altitude above the ground. e: the lowest angle above the horizon at which the station can still use the link (antennas and terrain block lower angles). λ: how many degrees of orbit, either side of straight overhead, the satellite is in view. μ: Earth’s gravitational parameter, 398,600 km³/s². Earth and orbit are drawn at true relative size, with the satellite’s sweep slowed down for viewing.</p>
<p class="cap"><b>Reading the numbers.</b> These are standard spherical-Earth geometry and Kepler’s third law. The defaults are a 20° minimum elevation and a 500 km altitude. At 500 km the period comes out at about 94.5 minutes, close to a 95-minute orbit. The result is a best case: a satellite that passes off to one side of the station is in view for less time, which is consistent with passes of 4 to under 6 minutes. Atmosphere, terrain and antenna limits are ignored.</p>
<p class="cap est" style="margin:2px 0 8px;font-style:italic">Not exact: shown to illustrate a trend.</p>
<div class="two">
<div>
<svg id="tl" viewBox="0 0 720 88" role="img" aria-label="24-hour timeline with ground-contact windows"></svg>
<p class="cap">Blue bars are contact windows, drawn evenly spaced. Real passes are not evenly spaced: in one worked example, a single satellite’s long gap delayed a whole round by over nine hours. Faint ticks mark one 95-minute orbit each.</p>
</div>
<div>
<div class="sl v"><label for="p2">Passes per day P</label><input id="p2" type="range" min="2" max="40" value="12"><output id="p2o"></output></div>
<div class="sl v"><label for="t2">Minutes per pass T</label><input id="t2" type="range" min="1" max="10" value="5"><output id="t2o"></output></div>
<div class="stats" style="margin-top:12px">
<div><b id="in2">–</b><span>of the day in contact</span></div>
<div><b id="out2">–</b><span>out of contact</span></div>
<div><b id="gap2">–</b><span>average wait between passes</span></div>
</div>
<p class="cap" id="v2" style="margin-top:10px"></p>
</div>
</div>
<div class="f">in contact   = P × T ÷ 1440 min
average wait = 1440 ÷ P − T   (minutes, if passes were evenly spaced)
orbits / day = 1440 ÷ 95 ≈ 15.2</div>
<p class="key"><b>Symbols.</b> P: contact windows per day. T: minutes per window. 1440 is the number of minutes in a day. 95 minutes is the orbital period.</p>
<p class="cap"><b>Reading the numbers.</b> 12 passes of under 6 minutes leave over 96% of the day out of contact; 4 minutes in a 95-minute orbit gives the same picture, since 4 ÷ 95 is 4.2%. The sliders are yours. Note that 12 passes at the full 6 minutes would be 72 minutes, or 5% of the day, so “over 96% unavailable” implies passes averaging about 4.8 minutes or less.</p>
<p class="cap est" style="margin:2px 0 8px;font-style:italic">Not exact: shown to illustrate a trend.</p>
</section>

<section class="box sec" id="s3">
<h2>3 A poor link: slow, lopsided, and lossy in bursts</h2>
<p class="cap" style="margin:0 0 8px">Even during a pass the link is not a clean pipe. These are measured figures for real satellite links.</p>
<svg id="asym" style="max-width:560px;margin:0 auto" viewBox="0 0 360 172" role="img" aria-label="Downlink is thick and has low loss; uplink is thin and has higher loss"></svg>
<p class="cap" style="margin:4px 0 10px">Arrow thickness is drawn in proportion to the rates (111.01 : 12.43). The jagged marks on the uplink stand for the bursts in the table below.</p>
<div class="scroll"><table class="wrap">
<tr><th>Property</th><th>Value</th><th>Note</th></tr>
<tr><td>Downlink vs uplink rate</td><td>111.01 vs 12.43 Mbps (8.93×)</td><td>Starlink ground-station measurements. Another measurement study uses 15 Mbps for the uplink.</td></tr>
<tr><td>Packet loss, uplink vs downlink</td><td>1.24% vs 0.24% (5.2×)</td><td>Average in non-congested conditions. Uplink here means ground to satellite, the direction that carries the global model.</td></tr>
<tr><td>Bursts</td><td>Loss jumps to 3–15% every 3–5 s; one episode can lose over 100 packets in a row</td><td>From measurement studies.</td></tr>
<tr><td>Heavy tail</td><td>About 12% of samples above 5% loss, 6% above 10%, rare peaks of 50%. A ground station reconnects about 4 times a minute.</td><td>From measurement studies.</td></tr>
</table></div>
<p class="cap" style="margin-top:12px"><b>Lab 3: same average loss, different shape.</b> 2,000 packets are sent in a row. Each square is a packet; red means lost. Compare scattered loss with bursts at the same average rate.</p>
<div class="two">
<div>
<svg id="pk" viewBox="0 0 700 140" role="img" aria-label="2000 packets, lost ones in red"></svg>
<div class="ctl"><button type="button" id="mr" class="p">Scattered</button><button type="button" id="mb">Bursty</button><button type="button" id="mn">Resample</button></div>
</div>
<div>
<div class="sl v"><label for="p3">Average loss p</label><input id="p3" type="range" min="0.1" max="10" step="0.01" value="1.24"><output id="p3o"></output></div>
<div class="sl v"><label for="l3">Burst length L</label><input id="l3" type="range" min="2" max="120" value="40"><output id="l3o"></output></div>
<div class="stats" style="margin-top:12px">
<div><b id="x3">–</b><span>lost in this sample</span></div>
<div><b id="e3">–</b><span>separate loss events</span></div>
<div><b id="r3">–</b><span>longest run lost</span></div>
</div>
<p class="cap" id="v3" style="margin-top:10px"></p>
</div>
</div>
<div class="f">extra time if each lost packet were re-sent once = p ÷ (1 − p)
at p = 1.24%  →  about 1.3%      a measured retransmission result: +89.6%</div>
<p class="key"><b>Symbols.</b> p: the average fraction of packets lost (default 1.24%, the measured uplink figure). L: the average burst length in packets, used only in “Bursty” mode (default 40; bursts of over 100 packets are reported). Scattered mode drops each packet independently. Bursty mode drops runs of about L packets, with the same expected total.</p>
<p class="cap"><b>Reading the numbers.</b> The formula p ÷ (1 − p) assumes independent losses, each fixed by one resend. The +89.6% is the measured slowdown of one training round (RSD46-WHU dataset) when parameters were sent with retransmission over real satellite loss traces. The gap between 1.3% and 89.6% is the point: average loss understates the damage, and the bursty, persistent, highly dynamic loss pattern is the main bottleneck. Ignoring lost packets is no fix either: with plain UDP at a uniform 10% loss, accuracy fell by up to 27.5% in the worst case. Across realistic satellite loss, conventional terrestrial transmission methods cost over 7% average accuracy and over 20% more convergence time. Earlier work found that DenseNet needed over 190% longer to converge in non-terrestrial settings than on the ground.</p>
<p class="cap est" style="margin:2px 0 8px;font-style:italic">Not exact: shown to illustrate a trend.</p>
</section>

<section class="box sec" id="s4">
<h2>4 Send the model, not the data</h2>
<p class="cap" style="margin:0 0 8px">Federated learning sends model weights instead of images. That helps only if the weights are small compared with the data, and if they fit through the link during a contact. This lab checks both.</p>
<div id="mbtn" class="ctl" style="margin-top:0"></div>
<div class="two" style="margin-top:12px">
<div>
<div id="bbtn" class="ctl" style="margin:0 0 4px"></div>
<div class="sl v"><label for="u4">Uplink rate U</label><input id="u4" type="range" min="5" max="50" value="15"><output id="u4o"></output></div>
<div class="sl v"><label for="r4">Downlink rate R</label><input id="r4" type="range" min="10" max="300" value="111"><output id="r4o"></output></div>
<div class="sl v"><label for="w4">Usable window W</label><input id="w4" type="range" min="2" max="60" value="10"><output id="w4o"></output></div>
<div class="sl v"><label for="k4">Training rounds K</label><input id="k4" type="range" min="1" max="500" value="50"><output id="k4o"></output></div>
<div class="sl v"><label for="d4">Raw data D</label><input id="d4" type="range" min="0.05" max="5" step="0.05" value="1"><output id="d4o"></output></div>
</div>
<div>
<div class="stats">
<div><b id="sz4">–</b><span>model size s</span></div>
<div><b id="rx4">–</b><span>to receive it (uplink)</span></div>
<div><b id="tx4">–</b><span>to send it back (downlink)</span></div>
</div>
<p class="cap" id="f4" style="margin-top:8px"></p>
<div class="stats" style="margin-top:12px">
<div><b id="tot4">–</b><span>model traffic over K rounds</span></div>
<div><b id="sh4">–</b><span>of the raw data D</span></div>
<div><b id="be4">–</b><span>rounds until it equals D</span></div>
</div>
<p class="cap" id="v4" style="margin-top:8px"></p>
</div>
</div>
<h3 class="sub">How the quantities compare (log scale)</h3>
<p class="cap" style="margin:0 0 6px">Each bar is one of the quantities above, on a scale where every step to the right is ten times more. It follows the sliders: change the model, the rounds or the raw data and watch the bars move.</p>
<div class="scroll"><div style="min-width:560px"><svg id="lad" viewBox="0 0 640 170" role="img" aria-label="Log-scale bars comparing raw data, daily downlink capacity, model size and total model traffic"></svg></div></div>
<h3 class="sub">Whether the model fits in a contact window</h3>
<p class="cap" style="margin:0 0 6px">Each bar is one contact window, in seconds. The red line is how long it takes to receive the model at the uplink rate above (U). Green windows are long enough to deliver the whole model in one go; grey ones are not.</p>
<div class="scroll"><div style="min-width:560px"><svg id="wnd" viewBox="0 0 640 190" role="img" aria-label="Sixteen contact windows compared with the time needed to receive the model"></svg></div></div>
<p class="cap" id="wndt" style="margin-top:4px"></p>
<p class="cap"><b>About these two drawings.</b> The bars in the first are the same arithmetic as the numbers above. In the second, the 16 window lengths are random values between 2 and 10 seconds, matching windows of at most 10 s. Resample to see another set.</p>
<p class="cap est" style="margin:2px 0 8px;font-style:italic">Not exact: shown to illustrate a trend.</p>
<div class="ctl"><button type="button" id="wnr">New set of windows</button></div>
<div class="f">size            s = s₃₂ × b ÷ 32            (s₃₂ = the preset’s size at 32 bits)
receive time    t_rx = s × 8 ÷ U            windows needed = ⌈ t_rx ÷ W ⌉
send-back time  t_tx = s × 8 ÷ R
model traffic   = K × 2 × s                 (one copy down, one copy up, per round)
break-even      = D × 1,000,000 ÷ (2 × s)</div>
<p class="key"><b>Symbols.</b> s: model size in megabytes. b: bits stored per weight (32 is full precision; fewer is quantization, Module 1 section 8). U and R: uplink and downlink rate in Mbps. W: the length of one usable stretch of contact, in seconds. K: how many rounds this one satellite takes part in. D: terabytes of raw data it would otherwise send (same scale as Lab 1). The factor 8 converts megabytes to megabits.</p>
<p class="cap"><b>Reading the numbers.</b> The three model sizes are MobileNetV3 Large 22 MB, EfficientNetB3 48 MB and ResNet50 98 MB. They look like full 32-bit weights, so 32 is the default. The uplink default is 15 Mbps and the downlink default is 111 Mbps. For the 22 MB model the lab gives 11.7 s. The 10 s window is the stretch of a pass that is usable, since a whole pass is minutes long. K and D are your what-ifs, and the bit widths are arithmetic. The traffic comparison counts weights only, ignoring protocol overhead and retransmissions.</p>
<p class="cap est" style="margin:2px 0 8px;font-style:italic">Not exact: shown to illustrate a trend.</p>

<h2 style="margin-top:16px">Start training before the download ends</h2>
<p class="cap" style="margin:0 0 8px">A worked example: downloading the model takes 14.7 s (11.7 s of transmission plus 3 s waiting for the next window), training takes 22.1 s, and the whole round takes 37.9 s because training only starts after the last block arrives; the other stages make up the rest. The fix, overlapped block-wise scheduling (OBS), splits the model into blocks and trains on a block as soon as it arrives, so the GPU is not idle during the download. It has been reported to give up to a 20.5× speedup in end-to-end training against baselines.</p>
<div class="two">
<div>
<svg id="gt" viewBox="0 0 400 142" role="img" aria-label="Timeline of download and training, sequential versus overlapped"></svg>
</div>
<div>
<div class="sl v"><label for="m4">Blocks M</label><input id="m4" type="range" min="1" max="16" value="4"><output id="m4o"></output></div>
<div class="stats" style="margin-top:12px">
<div><b id="sq4">–</b><span>download then train</span></div>
<div><b id="ov4">–</b><span>overlapped</span></div>
</div>
</div>
</div>
<div class="f">download D_t = 14.7 s    training T_t = 22.1 s    blocks M
block i is trained when it has arrived and block i−1 is done
M = 1 gives download then train: 14.7 + 22.1 = 36.8 s</div>
<p class="key"><b>Symbols.</b> D_t and T_t: the example durations for downloading and training. M: how many equal blocks the model is cut into (real blocks can be adaptive; here they are equal, to keep the demo simple).</p>
<p class="cap"><b>Reading the numbers.</b> The overlapped finish time assumes equal blocks, no waiting between windows, and no upload. It shows why overlap helps, not how much it helps in a real system.</p>
<p class="cap est" style="margin:2px 0 8px;font-style:italic">Not exact: shown to illustrate a trend.</p>
</section>

<section class="box sec" id="s5">
<h2>5 A constellation is not one satellite</h2>
<p class="cap" style="margin:0 0 8px">Satellite FL differs from phones in two ways. A constellation is owned and run by one operator and contacts follow orbital mechanics, so client availability is predictable instead of random. And there are orders of magnitude fewer clients, so each carries more of the data; it is prudent to include as many satellites as possible in each round rather than sampling a few. Constellations fall into three connectivity classes:</p>
<div class="trio" style="margin-bottom:8px">
<div class="fig"><svg id="k1" viewBox="0 0 240 150" role="img" aria-label="Sporadic direct: satellites on separate orbits, one connected to the ground station at a time"></svg><p class="cap"><b>Sporadic direct.</b> Each satellite is alone on its orbit. Only the one currently passing over the station can talk to it.</p></div>
<div class="fig"><svg id="k2" viewBox="0 0 240 150" role="img" aria-label="Near-persistent: satellites in one orbit linked to each other, one linked to the ground station"></svg><p class="cap"><b>Near-persistent.</b> Satellites in one orbit are linked to their neighbours, so whichever member is over the station can carry the whole cluster’s updates.</p></div>
<div class="fig"><svg id="k3" viewBox="0 0 240 150" role="img" aria-label="Multi-hop: two clusters linked together, the route to the ground station passes through both"></svg><p class="cap"><b>Multi-hop.</b> Clusters are linked to each other too, so an update can hop from a cluster that never sees the station to one that does.</p></div>
</div>
<p class="cap" style="margin:0 0 8px">Solid lines are working links, dashed are unavailable at this moment.</p>
<p class="cap est" style="margin:2px 0 8px;font-style:italic">Not exact: shown to illustrate a trend.</p>
<div class="loop l3">
<div><b>Sporadic direct</b>Long offline gaps between short contacts with the server. Typical when satellites have no inter-satellite links or a single ground station runs the learning.</div>
<div><b>Near-persistent direct</b>Satellites in a cluster share data over links between neighbours in the same orbit, so some member is usually in contact.</div>
<div><b>Multi-hop</b>Clusters also reach each other over inter-cluster links, so updates can be relayed through several satellites and clusters.</div>
</div>
<p class="cap" style="margin-top:10px">An example: with FedAvg, a single ground station and one satellite per orbit, the first global iteration takes over nine hours, because of one slow satellite (C4 in the example). Each client gets the model on its first contact, trains, returns the update on its second, and the server waits for everyone. Asynchronous methods avoid the wait by updating whenever an update arrives, at the price of staleness (Module 5).</p>
<p class="cap"><b>Lab 5: the slowest satellite sets the pace.</b> Each row is a satellite; dots are its contacts over 24 hours with the one ground station. The red line is when synchronous FedAvg first has all the updates.</p>
<div class="two">
<div>
<svg id="cs" viewBox="0 0 720 230" role="img" aria-label="Contact times for several satellites over 24 hours"></svg>
<div class="ctl"><button type="button" id="cn">Resample</button></div>
</div>
<div>
<div class="sl v"><label for="k5">Satellites K</label><input id="k5" type="range" min="2" max="8" value="5"><output id="k5o"></output></div>
<div class="sl v"><label for="g5">Longest revisit gap g_max</label><input id="g5" type="range" min="2" max="12" value="9"><output id="g5o"></output></div>
<div class="stats" style="margin-top:12px">
<div><b id="ts5">–</b><span>first synchronous aggregate</span></div>
<div><b id="as5">–</b><span>asynchronous updates by then</span></div>
</div>
<p class="cap" id="v5" style="margin-top:10px"></p>
</div>
</div>
<div class="f">satellite k:  revisit gap g_k (hours),  first contact o_k
contacts at   o_k, o_k + g_k, o_k + 2·g_k, ...
synchronous first aggregate  T_s = max over k of (o_k + g_k)
asynchronous updates by T_s  = sum over k of floor((T_s − o_k) ÷ g_k)</div>
<p class="key"><b>Symbols.</b> K: number of satellites. g_k: hours between satellite k’s contacts, drawn between 1.5 h and g_max. o_k: when its first contact happens, between 0 and g_k. T_s: when the server has every client’s first returned update. Local training is assumed to fit inside one gap.</p>
<p class="cap"><b>Reading the numbers.</b> The structure is that the first contact receives the model, the second returns the update, and the server waits for all. The gaps and offsets here are random values. Real contact times are computable from orbits, so a real scheduler would not use random numbers.</p>
<p class="cap est" style="margin:2px 0 8px;font-style:italic">Not exact: shown to illustrate a trend.</p>
</section>

<section class="box sec" id="s6">
<h2>6 A satellite is not a data center</h2>
<p class="cap" style="margin:0 0 8px">FL training is often about 10 times more compute-intensive than inference, which makes it impractical for resource-constrained satellites. One example is Planet’s onboard NVIDIA Jetson, which has about one-tenth the GPU cores of an RTX 3090. Satellites also have a limited energy supply that depends on sunlight and eclipse. Orbital data-center projects are a different design from the Earth-observation satellites studied here, so this module does not cover them.</p>
<div class="two">
<div>
<div class="sl v"><label for="tg6">Ground epoch time t_g</label><input id="tg6" type="range" min="5" max="120" value="20"><output id="tg6o"></output></div>
<div class="sl v"><label for="e6">Local epochs E</label><input id="e6" type="range" min="1" max="20" value="5"><output id="e6o"></output></div>
<div class="sl v"><label for="q6">Compute ratio ρ</label><input id="q6" type="range" min="0.05" max="1" step="0.05" value="0.1"><output id="q6o"></output></div>
</div>
<div>
<div class="stats">
<div><b id="gs6">–</b><span>ground GPU, E epochs</span></div>
<div><b id="ss6">–</b><span>satellite, E epochs</span></div>
<div><b id="inf6">–</b><span>satellite, inference only (÷10)</span></div>
</div>
<p class="cap" id="v6" style="margin-top:10px"></p>
</div>
</div>
<div class="f">ground time    = E × t_g
satellite time = E × t_g ÷ ρ
inference time ≈ satellite time ÷ 10</div>
<p class="key"><b>Symbols.</b> t_g: seconds to train one pass over the local data on a ground GPU (your choice). E: local epochs (Module 1). ρ: the satellite’s compute as a fraction of the ground GPU, default 0.1.</p>
<p class="cap"><b>Reading the numbers.</b> ρ = 0.1 is one-tenth the GPU cores, and the ÷ 10 is “often 10×” for training versus inference. Treating GPU cores as speed is crude: memory, clocks and power limits also matter, so real ratios differ. t_g is your what-if. The results are arithmetic, not benchmarks.</p>
<p class="cap est" style="margin:2px 0 8px;font-style:italic">Not exact: shown to illustrate a trend.</p>
</section>

<section class="box sec" id="s7">
<h2>7 Who owns the data</h2>
<p class="cap" style="margin:0 0 8px">The centralized approach has two bottlenecks. The first is the constrained link (sections 1 to 3). The second is that satellites often keep their data locally because of commercial competition and data-ownership concerns. FL fits this: each owner trains on its own images and shares only model updates. Infringed data ownership is also one of the costs of collecting everything in one place. Two cautions:</p>
<ul class="cap" style="margin:4px 0 0;padding-left:20px">
<li>A single constellation is usually owned by one operator, so within one constellation the ownership argument is weaker and the bandwidth argument carries more of the weight. Ownership matters most when several operators want one shared model.</li>
<li>Keeping data local is not the same as keeping it private. Module 1 section 7 covers what updates can still leak and how differential privacy limits it.</li>
</ul>
</section>

<section class="box sec" id="s8">
<h2>8 The main points side by side</h2>
<p class="cap" style="margin:0 0 8px">Three obstacles (data volume, contact, link), the comparison that favours sending the model, and the compute limit. Each row says what it means for training a shared model.</p>
<div class="scroll"><table class="wrap">
<tr><th>Topic</th><th>What it means for training</th></tr>
<tr><td><b>Too much data</b></td><td>Only 5% of a day’s data can be sent, so the backlog grows every day (section 1).</td></tr>
<tr><td><b>Too little contact</b></td><td>A satellite can exchange anything only in a few short windows (section 2).</td></tr>
<tr><td><b>A poor link</b></td><td>Sending the model to the satellite uses the slow, lossy direction (section 3).</td></tr>
<tr><td><b>Model versus data</b></td><td>FL moves far fewer bytes than downloading, but a 22 MB model needs 11.7 s at 15 Mbps, longer than a 10 s window (section 4).</td></tr>
<tr><td><b>Weak onboard compute</b></td><td>Local training takes about 10 times as long as on the ground (section 6).</td></tr>
</table></div>
<p class="cap est" style="margin:2px 0 8px;font-style:italic">Not exact: shown to illustrate a trend.</p>
</section>

<section class="box sec" id="s9">
<h2>9 What FL does not fix: where the next modules pick up</h2>
<p class="cap" style="margin:0 0 8px">Sending the model removes the data-volume problem, and the rest of this series is about what remains.</p>
<div class="loop l3">
<div><b>Module 3: IID vs non-IID</b>Each satellite sees different parts of the Earth, so local datasets differ. Module 1 section 1 showed what missing classes do.</div>
<div><b>Module 4: intermittent contact</b>Sections 2 and 5 here: clients can be reached only briefly and unevenly, so who joins a round is decided by the orbit.</div>
<div><b>Module 5: staleness and scheduling</b>Asynchronous updates arrive late, and pipelining is a scheduling answer to waiting.</div>
<div><b>Module 6: resource heterogeneity</b>Section 6: satellites differ in compute and energy, and slower ones hold up synchronous rounds.</div>
<div><b>Module 7: inter-satellite links</b>Section 5: near-persistent and multi-hop connectivity let satellites combine updates before reaching the ground.</div>
<div><b>Module 8: split FL</b>Plain FL is impractical for constrained satellites, and intermittent connectivity can slow split-FL convergence by over 20× (VGG-16, EuroSAT, 12 satellites), which motivates its design.</div>
</div>
</section>

<section class="box q" style="margin-top:16px">
<h2>Check your understanding</h2>
<div class="q2">
<div>A satellite has 12 passes a day, each under 6 minutes. About what share of the day can it exchange data?</div>
<button type="button" data-m="Not quite. 12 passes of at most 6 minutes is at most 72 minutes, which is 5% of 1,440 minutes, not a quarter.">About a quarter of the day</button>
<button type="button" data-m="Right. At most 72 of 1,440 minutes is 5%, and the unavailable share is over 96%, which fits passes averaging under about 4.8 minutes. 4 of 95 minutes gives the same picture.">Roughly 4 to 5%</button>
<button type="button" data-m="Not quite. That is the share it is out of contact. In contact it is only about 4 to 5%.">About 96%</button>
<p class="fb" role="status" style="min-height:44px;margin:10px 0 0;font-size:14px"></p>
</div>
<div class="q2" style="margin-top:14px">
<div>A 22 MB model is sent at 15 Mbps. Why is this a problem for a 10 s window?</div>
<button type="button" data-m="Right. 22 × 8 ÷ 15 is about 11.7 s, longer than the window, so the model cannot be delivered in one stretch and has to wait for a rare long connection or be split.">It takes about 11.7 s, longer than the window</button>
<button type="button" data-m="Not quite. 22 MB is the model’s size, and the problem is how long it takes to move at 15 Mbps.">22 MB is bigger than the satellite’s memory</button>
<button type="button" data-m="Not quite. Packet loss makes it worse, but the 11.7 s figure comes from size and rate alone, before any loss.">Packet loss makes every transfer fail</button>
<p class="fb" role="status" style="min-height:44px;margin:10px 0 0;font-size:14px"></p>
</div>
<div class="q2" style="margin-top:14px">
<div>Why does synchronous FedAvg with a single ground station start slowly?</div>
<button type="button" data-m="Not quite. The satellites do not need to share data; the issue is timing.">The satellites cannot share data with each other</button>
<button type="button" data-m="Right. The server waits for every selected client, so the satellite with the longest gap between contacts decides when the first aggregate exists. In the example that was over nine hours.">It waits for the slowest satellite’s contacts</button>
<button type="button" data-m="Not quite. Model size matters in other sections, but their example is about contact timing.">The model is too large to aggregate</button>
<p class="fb" role="status" style="min-height:44px;margin:10px 0 0;font-size:14px"></p>
</div>
<div class="q2" style="margin-top:14px">
<div>In federated learning, what travels between the ground and the satellites?</div>
<button type="button" data-m="Not quite. That is the download-everything design from section 1. In federated learning the images stay on the satellite.">The raw images, so the ground can train on them</button>
<button type="button" data-m="Not quite. Each satellite has to send its update back, or the server has nothing to average.">Only the global model; nothing comes back</button>
<button type="button" data-m="Right. Each satellite trains on its own images and only model updates travel, so the model improves without the images moving.">The model out to the satellites and the updates back</button>
<p class="fb" role="status" style="min-height:44px;margin:10px 0 0;font-size:14px"></p>
</div>
</section>


<p class="key" style="margin-top:16px">Next: Module 3, IID vs non-IID data (choose it from the module list at the top of the page)</p>
</main>

<script>
(function(){
var $=function(i){return document.getElementById(i)};
function g(i){return +$(i).value}
function css(n){return getComputedStyle(document.documentElement).getPropertyValue(n).trim()}
function fmtT(s){return s<90?s.toFixed(1)+' s':s<5400?(s/60).toFixed(1)+' min':s<172800?(s/3600).toFixed(1)+' h':(s/86400).toFixed(1)+' days'}
function fmtMB(mb){return mb>=1e6?(mb/1e6).toFixed(2)+' TB':mb>=1000?(mb/1000).toFixed(mb>=1e4?0:1)+' GB':mb.toFixed(mb<10?1:0)+' MB'}
function rng(seed){var a=seed>>>0;return function(){a|=0;a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
function svgEl(h){return h}

/* ---- Lab 1 ---- */
function lab1(){
var D=g('d1'),N=g('n1');
$('d1o').textContent=D.toFixed(2)+' TB';$('n1o').textContent=N+' d';
var capGB=12*5*60*111.01/8/1000,genGB=D*1000,share=Math.min(1,capGB/genGB);
$('c1').textContent=capGB.toFixed(1)+' GB';
$('s1s').textContent=(share*100).toFixed(share<.1?1:0)+'%';
$('b1').style.width=(share*100)+'%';
var days=genGB/capGB;
$('t1').textContent=days<=1?'under a day':days.toFixed(days<10?1:0)+' days';
var bk=Math.max(0,N*(genGB-capGB)/1000);
$('bk1').textContent=bk.toFixed(bk<10?2:1)+' TB';
$('v1').textContent=days>1.05?'Each day adds a backlog. Sending one day of data takes about '+days.toFixed(days<10?1:0)+' times as long as collecting it, so the queue only grows.':'At this volume one day of data fits in one day of contact.';
}
/* ---- Lab 2 ---- */
function lab2(){
var P=g('p2'),T=g('t2');
$('p2o').textContent=P;$('t2o').textContent=T+' min';
var con=Math.min(1,P*T/1440);
var h='<rect x="0" y="22" width="720" height="26" rx="5" fill="'+css('--line')+'"/>';
for(var o=0;o<1440;o+=95)h+='<rect x="'+(o/1440*720)+'" y="18" width="1" height="34" fill="'+css('--mute')+'" opacity=".35"/>';
for(var i=0;i<P;i++){var x=(i+.5)/P*720,w=Math.max(2,T/1440*720);h+='<rect x="'+(x-w/2)+'" y="16" width="'+w+'" height="38" fill="'+css('--acc')+'"/>'}
for(i=0;i<=24;i+=6)h+='<text x="'+(i/24*720)+'" y="82" font-size="18" fill="'+css('--mute')+'" text-anchor="'+(i==0?'start':i==24?'end':'middle')+'">'+i+' h</text>';
$('tl').innerHTML=h;
$('in2').textContent=(con*100).toFixed(1)+'%';$('out2').textContent=((1-con)*100).toFixed(1)+'%';
var gap=1440/P-T;$('gap2').textContent=gap>=90?(gap/60).toFixed(1)+' h':Math.max(0,gap).toFixed(0)+' min';
$('v2').textContent=con*100<=4.2?'This is at or below the 4 to 4.2% typically in contact.':'This is more contact than typical (about 4% of the day). Real satellites with one ground station sit near the low settings.';
}
/* ---- Lab 3 ---- */
var mode='r',seed=7,N3=2000;
function lab3(){
var p=g('p3')/100,L=g('l3');
$('p3o').textContent=(p*100).toFixed(2)+'%';$('l3o').textContent=L;
var r=rng(seed*7919+(mode=='b'?13:0)),lost=new Uint8Array(N3);
if(mode=='r'){for(var i=0;i<N3;i++)if(r()<p)lost[i]=1}
else{var nb=p*N3/L,whole=Math.floor(nb),k=whole+(r()<nb-whole?1:0);
for(var b=0;b<k;b++){var s=Math.floor(r()*N3),len=Math.max(1,Math.round(-Math.log(1-r())*L));for(var j=s;j<Math.min(N3,s+len);j++)lost[j]=1}}
var cols=100,cell=7,h='',cnt=0,ev=0,run=0,best=0;
for(i=0;i<N3;i++){
 if(lost[i]){cnt++;run++;if(run>best)best=run;if(run==1)ev++}else run=0;
 h+='<rect x="'+((i%cols)*cell)+'" y="'+(Math.floor(i/cols)*cell)+'" width="'+(cell-1)+'" height="'+(cell-1)+'" rx="1" fill="'+(lost[i]?css('--c0'):css('--line'))+'"/>';
}
$('pk').innerHTML=h;
$('x3').textContent=(cnt/N3*100).toFixed(2)+'%';$('e3').textContent=ev;$('r3').textContent=best;
$('v3').textContent=(mode=='r'?'Scattered loss: many separate single-packet gaps, each easy to repair with one resend.':'Bursty loss: far fewer events, but each removes a long stretch. A repair has to wait out the whole outage, and bursts of over 100 packets have been reported.')+' With only 2,000 packets, the actual rate wanders around the setting (press Resample).';
$('mr').className=mode=='r'?'p':'';$('mb').className=mode=='b'?'p':'';
}
/* ---- Lab 4 ---- */
var MODELS=[['MobileNetV3 Large',22],['EfficientNetB3',48],['ResNet50',98]],msel=0,BITS=[32,16,8,4],bsel=0;
function lab4(){
var U=g('u4'),R=g('r4'),W=g('w4'),K=g('k4'),D=g('d4');
$('u4o').textContent=U+' Mbps';$('r4o').textContent=R+' Mbps';$('w4o').textContent=W+' s';$('k4o').textContent=K;$('d4o').textContent=D.toFixed(2)+' TB';
var s=MODELS[msel][1]*BITS[bsel]/32;
$('sz4').textContent=fmtMB(s);
var rx=s*8/U,tx=s*8/R;
$('rx4').textContent=fmtT(rx);$('tx4').textContent=fmtT(tx);
var wn=Math.ceil(rx/W);
$('f4').textContent=rx<=W?'It fits in one window of '+W+' s ('+rx.toFixed(1)+' s needed).':'It does not fit: '+rx.toFixed(1)+' s needed against a '+W+' s window, so it must be split over at least '+wn+' windows, or wait for a longer one.';
var tot=K*2*s;
$('tot4').textContent=fmtMB(tot);
var sh=tot/(D*1e6);
$('sh4').textContent=(sh*100).toFixed(sh<.01?3:sh<.1?2:1)+'%';
var be=D*1e6/(2*s);
$('be4').textContent=be>=100?Math.round(be).toLocaleString():be.toFixed(1);
var pc=(sh*100).toFixed(sh<.01?3:sh<.1?2:1),rr=K+' round'+(K==1?'':'s');
$('v4').textContent=sh<.05?'Over '+rr+' the model traffic is only '+pc+'% of the raw data. Once rounds exceed the break-even, FL would move more bytes than simply downloading the data.':sh<1?'Over '+rr+' the model traffic is already '+pc+'% of the raw data, so the saving is shrinking. Past the break-even, FL would move more bytes than downloading.':'Over '+rr+' FL moves more bytes ('+pc+'% of the raw data) than downloading the raw data would.';
Array.prototype.forEach.call($('mbtn').children,function(c,j){c.className=j==msel?'p':''});if(window.ladder_ok){ladder();windows()}
Array.prototype.forEach.call($('bbtn').children,function(c,j){c.className=j==bsel?'p':''});
}
/* ---- pipeline gantt ---- */
function gantt(){
var M=g('m4');$('m4o').textContent=M;
var Dt=14.7,Tt=22.1,d=Dt/M,t=Tt/M,fin=0,starts=[];
for(var i=0;i<M;i++){var st=Math.max((i+1)*d,fin);starts.push(st);fin=st+t}
var seq=Dt+Tt,ov=fin,scale=360/Math.max(seq,1);
var h='',c1=css('--c4'),c2=css('--c3');
function row(y,label,list){h+='<text x="0" y="'+(y-4)+'" font-size="11" fill="'+css('--mute')+'">'+label+'</text>';list.forEach(function(b){h+='<rect x="'+(20+b[0]*scale)+'" y="'+(y+(b[2]==c2?18:0))+'" width="'+Math.max(1,(b[1]-b[0])*scale-.5)+'" height="16" fill="'+b[2]+'"/>'})}
var A=[[0,Dt,c1],[Dt,seq,c2]];
var B=[];for(i=0;i<M;i++){B.push([i*d,(i+1)*d,c1]);B.push([starts[i],starts[i]+t,c2])}
B.sort(function(a,b){return a[2]==c1?-1:1});
row(28,'Download, then train',A);row(82,'Overlapped ('+M+' block'+(M>1?'s':'')+')',B);
h+='<g font-size="10" fill="'+css('--mute')+'"><text x="20" y="136">0 s</text><text x="'+(20+seq*scale)+'" y="136" text-anchor="end">'+seq.toFixed(1)+' s</text></g>';
h+='<rect x="20" y="3" width="8" height="8" fill="'+c1+'"/><text x="31" y="11" font-size="10" fill="'+css('--mute')+'">download</text><rect x="90" y="3" width="8" height="8" fill="'+c2+'"/><text x="101" y="11" font-size="10" fill="'+css('--mute')+'">train</text>';
$('gt').innerHTML=h;
$('sq4').textContent=seq.toFixed(1)+' s';$('ov4').textContent=ov.toFixed(1)+' s';
}
/* ---- Lab 5 ---- */
var s5=3;
function lab5(){
var K=g('k5'),gm=g('g5');$('k5o').textContent=K;$('g5o').textContent=gm+' h';
var r=rng(s5*104729),gs=[],os=[],Ts=0;
for(var k=0;k<8;k++){var gk=1.5+(gm-1.5)*r(),ok=r()*gk;gs.push(gk);os.push(ok)}
for(k=0;k<K;k++)Ts=Math.max(Ts,os[k]+gs[k]);
var W=720,H=230,L=40,sx=function(t){return L+t/24*(W-L-6)};
var h='';
for(var k2=0;k2<K;k2++){var y=14+k2*26;
 h+='<line x1="'+L+'" x2="'+(W-6)+'" y1="'+(y+8)+'" y2="'+(y+8)+'" stroke="'+css('--line')+'"/><text x="0" y="'+(y+13)+'" font-size="16" fill="'+css('--mute')+'">S'+(k2+1)+'</text>';
 for(var t=os[k2],j=0;t<=24;t+=gs[k2],j++)h+='<circle cx="'+sx(t)+'" cy="'+(y+8)+'" r="'+(j==0?5:4)+'" fill="'+(j==0?css('--c4'):j==1?css('--c1'):css('--mute'))+'"/>';
}
for(var q=0;q<=24;q+=6)h+='<text x="'+sx(q)+'" y="'+(H-4)+'" font-size="17" fill="'+css('--mute')+'" text-anchor="'+(q==0?'start':q==24?'end':'middle')+'">'+q+' h</text>';
h+='<line x1="'+sx(Ts)+'" x2="'+sx(Ts)+'" y1="4" y2="'+(H-22)+'" stroke="'+css('--c0')+'" stroke-width="2" stroke-dasharray="5 3"/>';
$('cs').innerHTML=h;
var asy=0;for(k=0;k<K;k++)asy+=Math.floor((Ts-os[k])/gs[k]);
$('ts5').textContent=Ts.toFixed(1)+' h';$('as5').textContent=asy;
$('v5').textContent='Blue dot: first contact, the model is received. Green dot: second contact, the update is returned. The server cannot aggregate before the last green dot. Asynchronous FL would already have applied '+asy+' update'+(asy==1?'':'s')+' by then.';
}
/* ---- Lab 6 ---- */
function lab6(){
var tg=g('tg6'),E=g('e6'),q=g('q6');
$('tg6o').textContent=tg+' s';$('e6o').textContent=E;$('q6o').textContent=q.toFixed(2);
var gs=E*tg,ss=gs/q;
$('gs6').textContent=fmtT(gs);$('ss6').textContent=fmtT(ss);$('inf6').textContent=fmtT(ss/10);
$('v6').textContent='The satellite takes '+(1/q).toFixed(1)+' times as long as the ground GPU ('+fmtT(ss)+' against '+fmtT(gs)+'). If its next contact comes sooner than '+fmtT(ss)+', the update is not ready and the round either waits or skips this satellite (Modules 4 and 6).';
}
/* ---- wiring ---- */
/* ---------- new visuals ---------- */
function T(x,y,s,o){o=o||{};return '<text x="'+x+'" y="'+y+'" font-size="'+(o.s||11)+'" fill="'+(o.c||css('--mute'))+'" text-anchor="'+(o.a||'start')+'"'+(o.b?' font-weight="700"':'')+'>'+s+'</text>'}
function satIcon(x,y,col,op,sc){op=op==null?1:op;sc=sc||1;return '<g opacity="'+op+'" transform="translate('+x+' '+y+') scale('+sc+')"><rect x="-6" y="-4" width="12" height="8" rx="2" fill="'+col+'"/><rect x="-16" y="-3" width="8" height="6" fill="none" stroke="'+col+'"/><rect x="8" y="-3" width="8" height="6" fill="none" stroke="'+col+'"/></g>'}
function gsIcon(x,y,col){return '<path d="M'+(x-9)+' '+y+'L'+x+' '+(y-12)+'L'+(x+9)+' '+y+'Z" fill="'+col+'"/><rect x="'+(x-12)+'" y="'+y+'" width="24" height="4" fill="'+col+'"/>'}
function arrow(x1,y1,x2,y2,col,w,dash){var a=Math.atan2(y2-y1,x2-x1),hl=Math.max(6,w*1.6),px=x2-Math.cos(a)*hl*.4,py=y2-Math.sin(a)*hl*.4;return '<line x1="'+x1+'" y1="'+y1+'" x2="'+(x2-Math.cos(a)*hl*.8)+'" y2="'+(y2-Math.sin(a)*hl*.8)+'" stroke="'+col+'" stroke-width="'+w+'"'+(dash?' stroke-dasharray="4 3"':'')+'/><path d="M'+x2+' '+y2+'L'+(x2-Math.cos(a)*hl+Math.sin(a)*hl*.55)+' '+(y2-Math.sin(a)*hl-Math.cos(a)*hl*.55)+'L'+(x2-Math.cos(a)*hl-Math.sin(a)*hl*.55)+' '+(y2-Math.sin(a)*hl+Math.cos(a)*hl*.55)+'Z" fill="'+col+'"/>'}
function box(x,y,w,h,t,col,s){return '<rect x="'+x+'" y="'+y+'" width="'+w+'" height="'+h+'" rx="6" fill="'+css('--surf')+'" stroke="'+(col||css('--ink'))+'"/>'+T(x+w/2,y+h/2+4,t,{a:'middle',s:s||10,c:col||css('--ink')})}
function arch(){
 var ink=css('--ink'),mu=css('--mute'),c0=css('--c0'),acc=css('--acc'),c1=css('--c1');
 function base(){return satIcon(40,34,ink)+'<path d="M10 150Q120 112 230 150" fill="'+css('--line')+'" opacity=".5"/>'+gsIcon(190,118,ink)+T(190,140,'ground station',{a:'middle',s:9})}
 $('a1').innerHTML=base()+arrow(60,40,176,106,c0,10)+T(130,52,'all raw images',{a:'middle',c:c0,s:11})+T(40,18,'satellite',{a:'middle',s:9})+box(8,60,64,20,'stores images',mu,9)+T(158,138,'train here ▸',{a:'end',s:10,c:ink});
 $('a2').innerHTML=base()+box(6,52,72,22,'run model',acc,10)+arrow(60,44,176,106,acc,2.2)+T(150,62,'answers or',{a:'middle',s:10,c:acc})+T(150,75,'small images',{a:'middle',s:10,c:acc})+T(40,18,'satellite',{a:'middle',s:9})+T(158,138,'no shared model ▸',{a:'end',s:9});
 $('a3').innerHTML=base()+box(6,52,72,22,'train locally',c1,10)+arrow(176,98,62,48,mu,2.2)+arrow(66,56,176,112,c1,3.2)+T(110,40,'global model ↑',{a:'middle',s:10,c:mu})+T(160,70,'update ↓',{a:'middle',s:10,c:c1})+T(40,18,'satellite',{a:'middle',s:9});
}
function constel(){
 var ink=css('--ink'),mu=css('--mute'),acc=css('--acc'),ln=css('--line');
 function earth(){return '<path d="M0 150Q120 118 240 150Z" fill="'+ln+'" opacity=".6"/>'+gsIcon(120,128,ink)}
 function orbitArc(cx,cy,r,a1,a2){return '<path d="M'+(cx+r*Math.sin(a1))+' '+(cy-r*Math.cos(a1))+'A'+r+' '+r+' 0 0 1 '+(cx+r*Math.sin(a2))+' '+(cy-r*Math.cos(a2))+'" fill="none" stroke="'+ln+'" stroke-dasharray="2 3"/>'}
 var h=earth()+'<path d="M10 70Q120 10 230 70" fill="none" stroke="'+ln+'" stroke-dasharray="2 3"/><path d="M20 98Q120 52 220 98" fill="none" stroke="'+ln+'" stroke-dasharray="2 3"/>';
 var s=[[40,52,0],[200,52,0],[60,88,0],[120,70,1]];
 s.forEach(function(p){h+=p[2]?'<line x1="'+p[0]+'" y1="'+(p[1]+4)+'" x2="120" y2="116" stroke="'+acc+'" stroke-width="2"/>':'<line x1="'+p[0]+'" y1="'+(p[1]+4)+'" x2="120" y2="116" stroke="'+mu+'" stroke-dasharray="3 3" opacity=".5"/>';h+=satIcon(p[0],p[1],p[2]?acc:ink,p[2]?1:.5)});
 h+=T(120,18,'offline',{a:'middle',s:9})+T(120,36,'in view',{a:'middle',s:9,c:acc});
 $('k1').innerHTML=h;
 // k2
 h=earth()+'<path d="M10 78Q120 14 230 78" fill="none" stroke="'+ln+'" stroke-dasharray="2 3"/>';
 var q=[[30,64],[75,45],[120,38],[165,45],[210,64]];
 for(var i=0;i<q.length-1;i++)h+='<line x1="'+q[i][0]+'" y1="'+q[i][1]+'" x2="'+q[i+1][0]+'" y2="'+q[i+1][1]+'" stroke="'+acc+'" stroke-width="1.6"/>';
 h+='<line x1="120" y1="42" x2="120" y2="116" stroke="'+acc+'" stroke-width="2"/>';
 q.forEach(function(p,i){h+=satIcon(p[0],p[1],i==2?acc:ink,1,.75)});
 h+=T(120,22,'links between neighbours',{a:'middle',s:9});
 $('k2').innerHTML=h;
 // k3
 h=earth()+'<path d="M6 60Q60 18 114 60" fill="none" stroke="'+ln+'" stroke-dasharray="2 3"/><path d="M126 60Q180 18 234 60" fill="none" stroke="'+ln+'" stroke-dasharray="2 3"/>';
 var A=[[22,54],[50,38],[80,38],[106,54]],B=[[134,54],[160,38],[190,38],[218,54]];
 [A,B].forEach(function(c){for(var i=0;i<3;i++)h+='<line x1="'+c[i][0]+'" y1="'+c[i][1]+'" x2="'+c[i+1][0]+'" y2="'+c[i+1][1]+'" stroke="'+acc+'" stroke-width="1.4"/>'});
 h+='<line x1="106" y1="52" x2="134" y2="52" stroke="'+css('--c2')+'" stroke-width="2.4"/><line x1="106" y1="55" x2="120" y2="116" stroke="'+acc+'" stroke-width="2"/>';
 A.concat(B).forEach(function(p,i){h+=satIcon(p[0],p[1],i==3?acc:ink,1,.6)});
 h+=T(63,22,'cluster 1',{a:'middle',s:9})+T(177,22,'cluster 2',{a:'middle',s:9})+T(120,76,'link between clusters',{a:'middle',s:9,c:css('--c2')});
 $('k3').innerHTML=h;
}
function asym(){
 var ink=css('--ink'),c0=css('--c0'),c1=css('--c1'),h='';
 h+=satIcon(310,30,ink)+T(310,52,'satellite',{a:'middle',s:10})+'<path d="M0 170Q60 138 130 170Z" fill="'+css('--line')+'" opacity=".6"/>'+gsIcon(52,138,ink)+T(52,160,'ground station',{a:'middle',s:10});
 h+=arrow(284,42,86,104,c1,12)+T(8,16,'downlink: satellite → ground',{s:11,c:c1,b:1})+T(8,31,'111.01 Mbps · loss 0.24%',{s:11,c:c1});
 var x1=100,y1=128,x2=296,y2=58;h+=arrow(x1,y1,x2,y2,c0,1.4);
 for(var i=1;i<=4;i++){var t=i/5,x=x1+(x2-x1)*t,y=y1+(y2-y1)*t;h+='<path d="M'+(x-5)+' '+(y+3)+'l3 -7l3 7l3 -7" fill="none" stroke="'+c0+'" stroke-width="1.4"/>'}
 h+=T(352,150,'uplink: ground → satellite',{a:'end',s:11,c:c0,b:1})+T(352,165,'12.43 Mbps · loss 1.24%',{a:'end',s:11,c:c0});
 $('asym').innerHTML=h;
}
var os_=0,oraf=null;
function orbit(){
 var hh=+$('oh').value,e=+$('oe').value,Re=6371,a=Re+hh,er=e*Math.PI/180,lam=Math.acos(Re*Math.cos(er)/a)-er,Tp=2*Math.PI*Math.sqrt(a*a*a/398600);
 $('oho').textContent=hh+' km';$('oeo').textContent=e+'°';
 var pass=2*lam/(2*Math.PI)*Tp;
 $('op').textContent=(Tp/60).toFixed(1)+' min';$('ot').textContent=(pass/60).toFixed(1)+' min';$('of').textContent=(lam/Math.PI*100).toFixed(1)+'%';
 $('ov').textContent='At '+hh+' km with e = '+e+'°, a satellite passing straight over the station is in view for at most about '+(pass/60).toFixed(1)+' minutes of a '+(Tp/60).toFixed(1)+'-minute orbit. Real systems: under 6 minutes to about 4.';
 var Rp=300,Ro=Rp*a/Re,cx=180,gy=120,cy=gy+Rp,gsx=cx,ink=css('--ink'),mu=css('--mute'),acc=css('--acc'),ln=css('--line');
 function pt(th){return[cx+Ro*Math.sin(th),cy-Ro*Math.cos(th)]}
 var p1=pt(-lam),p2=pt(lam),th0=Math.min(Math.asin(Math.min(.99,165/Ro)),Math.max(.3,2.2*lam)),q1=pt(-th0),q2=pt(th0);
 var h='<circle cx="'+cx+'" cy="'+cy+'" r="'+Rp+'" fill="'+ln+'" opacity=".55"/>'+T(cx,gy+34,'Earth',{a:'middle',s:13});
 h+='<path d="M'+q1[0]+' '+q1[1]+'A'+Ro+' '+Ro+' 0 0 1 '+q2[0]+' '+q2[1]+'" fill="none" stroke="'+mu+'" stroke-dasharray="3 3"/>';
 h+='<path d="M'+p1[0]+' '+p1[1]+'A'+Ro+' '+Ro+' 0 0 1 '+p2[0]+' '+p2[1]+'" fill="none" stroke="'+acc+'" stroke-width="4"/>';
 h+='<line x1="'+gsx+'" y1="'+gy+'" x2="'+p1[0]+'" y2="'+p1[1]+'" stroke="'+acc+'" stroke-dasharray="3 3" opacity=".7"/><line x1="'+gsx+'" y1="'+gy+'" x2="'+p2[0]+'" y2="'+p2[1]+'" stroke="'+acc+'" stroke-dasharray="3 3" opacity=".7"/>';
 h+=gsIcon(gsx,gy,ink)+T(gsx+14,gy+14,'ground station',{s:10})+T(8,14,'blue arc: satellite is in view of the station',{s:11,c:acc});
 h+='<g id="osat"></g><text id="ost" x="352" y="14" font-size="11" text-anchor="end" fill="'+mu+'"></text>';
 $('orb').innerHTML=h;
 orbit.s={lam:lam,th0:th0,cx:cx,cy:cy,Ro:Ro};
 if(!oraf)tick(0);else frame(os_);
}
function frame(t){var s=orbit.s;if(!s)return;var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion:reduce)').matches,ph=reduce?.5:(t/9000)%1,th=-s.th0+2*s.th0*ph,x=s.cx+s.Ro*Math.sin(th),y=s.cy-s.Ro*Math.cos(th),inv=Math.abs(th)<=s.lam,g=$('osat');if(!g)return;
 g.innerHTML=satIcon(x,y,inv?css('--acc'):css('--ink'),1);var tx=$('ost');if(tx){tx.textContent=inv?'in contact':'out of view';tx.setAttribute('fill',inv?css('--acc'):css('--mute'))}}
function tick(t){os_=t;frame(t);oraf=requestAnimationFrame(tick)}
var wins=null,wseed=5;
function ladder(){
 var s=MODELS[msel][1]*BITS[bsel]/32,K=g('k4'),D=g('d4'),R=g('r4');
 var cap=12*5*60*R/8,rows=[['One day of raw data D',D*1e6,css('--c0')],['Downlink capacity per day',cap,css('--c3')],['Model traffic over K rounds',K*2*s,css('--c1')],['One model, s',s,css('--acc')]];
 var X0=200,W=420,lo=0,hi=7.2,h='';
 function xl(v){return X0+Math.max(0,Math.log10(Math.max(v,1)))/hi*W}
 for(var e=0;e<=7;e++){var x=X0+e/hi*W;h+='<line x1="'+x+'" x2="'+x+'" y1="4" y2="128" stroke="'+css('--line')+'"/>'+T(x,146,['1 MB','10 MB','100 MB','1 GB','10 GB','100 GB','1 TB','10 TB'][e],{a:'middle',s:11})}
 rows.forEach(function(r,i){var y=10+i*30;h+=T(0,y+16,r[0],{s:12,c:css('--ink')})+'<rect x="'+X0+'" y="'+y+'" width="'+Math.max(2,xl(r[1])-X0)+'" height="22" fill="'+r[2]+'"/>'+T(Math.min(xl(r[1])+6,X0+W-70),y+16,fmtMB(r[1]),{s:12,c:css('--ink')})});
 $('lad').innerHTML=h;
}
function windows(){
 var U=g('u4'),s=MODELS[msel][1]*BITS[bsel]/32,t=s*8/U,r=rng(wseed*77);
 if(!wins||wins.seed!=wseed){wins=[];for(var i=0;i<16;i++)wins.push(2+8*r());wins.seed=wseed}
 var X0=40,W=590,H=190,top=10,bot=160,ymax=Math.max(12,Math.ceil(t/2)*2+2),sy=function(v){return bot-(v/ymax)*(bot-top)};
 var h='';for(var v=0;v<=ymax;v+=ymax>30?10:2)h+='<line x1="'+X0+'" x2="'+(X0+W)+'" y1="'+sy(v)+'" y2="'+sy(v)+'" stroke="'+css('--line')+'"/>'+T(X0-6,sy(v)+4,v,{a:'end',s:11});
 var n=0;wins.forEach(function(w,i){var x=X0+8+i*(W-8)/16,ok=w>=t;if(ok)n++;h+='<rect x="'+x+'" y="'+sy(w)+'" width="'+((W-8)/16-8)+'" height="'+(bot-sy(w))+'" fill="'+(ok?css('--c1'):css('--mute'))+'" opacity="'+(ok?1:.45)+'"/>'+T(x+((W-8)/16-8)/2,bot+14,i+1,{a:'middle',s:10})});
 h+='<line x1="'+X0+'" x2="'+(X0+W)+'" y1="'+sy(t)+'" y2="'+sy(t)+'" stroke="'+css('--c0')+'" stroke-width="2.5" stroke-dasharray="6 4"/>'+T(X0+W,sy(t)-5,'time to receive the model: '+t.toFixed(1)+' s',{a:'end',s:11,c:css('--c0'),b:1})+T(8,12,'s',{s:10})+T(X0+W/2,H-2,'contact window number',{a:'middle',s:10});
 $('wnd').innerHTML=h;
 $('wndt').textContent=n+' of 16 windows are long enough to deliver '+fmtMB(s)+' in one go at '+U+' Mbps (time needed '+t.toFixed(1)+' s).';
}
function vis(){window.ladder_ok=1;arch();constel();asym();orbit();ladder();windows()}
$('oh').oninput=orbit;$('oe').oninput=orbit;$('wnr').onclick=function(){wseed++;windows()};

function all(){lab1();lab2();lab3();lab4();gantt();lab5();lab6();vis()}
['d1','n1'].forEach(function(i){$(i).oninput=lab1});
['p2','t2'].forEach(function(i){$(i).oninput=lab2});
['p3','l3'].forEach(function(i){$(i).oninput=lab3});
$('mr').onclick=function(){mode='r';lab3()};$('mb').onclick=function(){mode='b';lab3()};$('mn').onclick=function(){seed++;lab3()};
['u4','r4','w4','k4','d4'].forEach(function(i){$(i).oninput=lab4});
$('m4').oninput=gantt;
['k5','g5'].forEach(function(i){$(i).oninput=lab5});$('cn').onclick=function(){s5++;lab5()};
['tg6','e6','q6'].forEach(function(i){$(i).oninput=lab6});
MODELS.forEach(function(x,i){var b=document.createElement('button');b.type='button';b.textContent=x[0]+' ('+x[1]+' MB)';b.onclick=function(){msel=i;lab4()};$('mbtn').appendChild(b)});
BITS.forEach(function(x,i){var b=document.createElement('button');b.type='button';b.textContent=x+'-bit';b.onclick=function(){bsel=i;lab4()};$('bbtn').appendChild(b)});
Array.prototype.forEach.call(document.querySelectorAll('.q2'),function(q){var fb=q.querySelector('.fb');Array.prototype.forEach.call(q.querySelectorAll('button'),function(b){b.onclick=function(){fb.textContent=b.getAttribute('data-m')}})});
all();
if(window.matchMedia)matchMedia('(prefers-color-scheme:dark)').addEventListener('change',all);
})();
</script>
</body>
</html>
'''
