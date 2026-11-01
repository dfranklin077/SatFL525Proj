"""Module 3: IID vs non-IID data

The whole lesson as one self-contained HTML document (text, charts, sliders and
quiz all run in the browser). It is shown by interface/fl_modules.py.
"""
TITLE = 'Module 3: IID vs non-IID data'

HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Module 3: IID vs non-IID data</title>
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
a{color:var(--acc)}
.nav a{color:var(--ink)}
.ctl button.p{color:#fff}
.lg span{display:inline-flex;align-items:center}
.lg i{width:14px;height:10px}
.five{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:10px}
.six{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:8px}
@media(max-width:900px){.five{grid-template-columns:repeat(3,minmax(0,1fr))}.six{grid-template-columns:repeat(3,minmax(0,1fr))}}
@media(max-width:520px){.five{grid-template-columns:repeat(2,minmax(0,1fr))}}
.fig svg{width:100%;height:auto;display:block}
.fig .cap{font-size:12px}
#s2 .wrap td:last-child,#s2 .wrap th:last-child{min-width:250px}
</style>
</head>
<body>
<main>
<p style="margin:0 0 6px"><span class="tag">Module 3 of 8 · Live demo</span></p>
<h1>IID vs non-IID: what happens when satellites see different data</h1>
<p class="lede">In Module 1 three clients each missed three digits and the federated model still reached about 96%. Here you control <em>how</em> the data differs between satellites and watch federated averaging cope. Every number you can move is defined.</p>

<nav class="nav" aria-label="Module sections"><a href="#s1">1 What IID means</a><a href="#s2">2 Ways to differ</a><a href="#s3">3 Set the skew</a><a href="#s4">4 Train on it</a><a href="#s5">5 Each satellite</a><a href="#s6">6 What helps</a><a href="#s7">7 In satellite studies</a><a href="#s8">8 Limits</a></nav>

<section class="box sec" id="s1">
<h2>1 What IID means, and why federated data almost never is</h2>
<p class="cap" style="margin:0 0 8px">“IID” stands for independent and identically distributed. For training it means every example is drawn from the same pool, in no special order. If you shuffled all the data and dealt it out to clients, each client’s share would look like the whole. Federated data can be thought of as drawn in two steps: first pick a client <i>i</i> from some distribution Q over clients, then draw an example (x, y) from that client’s own distribution P<sub>i</sub>(x, y), where x is the input (an image) and y its label. “Non-IID” usually means P<sub>i</sub> differs from P<sub>j</sub> for different clients. The most common sources of difference are that each client is a particular user, a particular place, or a particular time window. A hospital’s records reflect the region it serves, and a phone’s data reflects its owner’s habits. The IID assumption almost never holds when data stays on devices.</p>
<div class="loop l3">
<div><b>IID</b>Every satellite’s images look like a random sample of all images. Every client’s update points roughly the same way, so averaging them is almost the same as training on pooled data.</div>
<div><b>Non-IID</b>Each satellite’s images follow its own distribution P<sub>i</sub>. Its local training pulls the model toward what it sees, so updates can disagree.</div>
<div><b>Why it matters for satellites</b>A satellite’s data is set by where and when it looks: its ground track, the season, the sun angle and cloud. Geography and time are typical sources of non-IID data.</div>
</div>
<p class="cap" style="margin-top:10px">Data on one device is non-IID in a second way if it is in an unshuffled order, for example consecutive video frames. That kind of intra-client correlation can generally be fixed by local shuffling, so this module is about differences <em>between</em> clients.</p>
<h3 class="sub">How orbits turn into label skew: a sample map</h3>
<p class="cap" style="margin:0 0 8px">The map below is a world of four land-cover types: A water, B forest, C desert, D city. Three satellites each image a strip along their ground track. What a satellite sees is whatever lies under its strip, so satellites that fly over different places collect different class mixes. Widen the tilt and each track sweeps across more kinds of land, and the mixes grow more alike.</p>
<div class="two">
<div><svg id="mp" viewBox="0 0 360 190" role="img" aria-label="A land-cover map with three ground tracks"></svg></div>
<div>
<div class="sl v"><label for="mpa">Track tilt (rows swept)</label><input id="mpa" type="range" min="0" max="5" step="0.5" value="1"><output id="mpao"></output></div>
<div class="sl v"><label for="mpw">Swath width (rows)</label><input id="mpw" type="range" min="1" max="4" step="0.5" value="2"><output id="mpwo"></output></div>
<svg id="mpb" viewBox="0 0 300 100" role="img" aria-label="Class mix collected by each satellite"></svg>
<div class="lg" id="mpl"></div>
</div>
</div>
<p class="key"><b>How to read it.</b> Each cell of the map is one patch of ground. Track tilt is how far, in rows, a satellite’s track swings north and south of its middle row as it goes round; swath width is how many rows wide the camera strip is. A satellite’s class mix is the share of each land type among the cells under its strip. A real satellite’s ground track shifts from one orbit to the next, which this picture does not show.</p>
<p class="cap est" style="margin:2px 0 8px;font-style:italic">Not exact: shown to illustrate a trend.</p>
</section>

<section class="box sec" id="s2">
<h2>2 Five ways client data can differ</h2>
<p class="cap" style="margin:0 0 8px">Non-IID data splits into the cases below, according to which part of P<sub>i</sub>(x, y) changes. The last column names the control in this module’s demo that creates each kind, and says what it does.</p>
<div class="five" id="tx" style="margin-bottom:10px"></div>
<p class="cap est" style="margin:2px 0 8px;font-style:italic">Not exact: shown to illustrate a trend.</p>
<div class="scroll"><table class="wrap">
<tr><th>Kind</th><th>What changes</th><th>Example</th><th>A satellite version</th><th>Variable you change</th></tr>
<tr><td><b>Label distribution skew</b> (prior probability shift)</td><td>P<sub>i</sub>(y): how common each class is</td><td>Kangaroos only in Australia or zoos; clients tied to geo-regions</td><td>A satellite over ocean sees mostly water; one over farmland sees mostly crops</td><td><b>Dirichlet α</b>, or <b>classes per satellite n</b>. Each satellite’s class shares are drawn from a Dirichlet distribution with concentration α. A large α (100) gives every satellite nearly the same mix as the whole, so the data is close to IID. A small α (0.1) puts most of a satellite’s images in one or two classes. With n, each satellite instead sees exactly n of the 4 classes, equally often, and the classes are handed out in turn: n = 1 is one class each, a different one for each satellite, so they differ as much as they can; n = 4 is all of them, so every satellite looks like the whole.</td></tr>
<tr><td><b>Feature distribution skew</b> (covariate shift)</td><td>P<sub>i</sub>(x), with P(y | x) shared</td><td>Handwriting: same words, different stroke width and slant</td><td>Different sensors, calibration or sun angle</td><td><b>Feature shift s</b>. Moves all of one satellite’s points by the distance s, in a random direction that differs from satellite to satellite, so its inputs sit in a different place from the others’. The four classes are clusters with spread 1 and centres at ±1.5, so s = 2 moves a satellite by more than one cluster’s spread. This is a simple offset, only a rough stand-in for a different sensor or sun angle.</td></tr>
<tr><td><b>Same label, different features</b> (concept drift)</td><td>P<sub>i</sub>(x | y)</td><td>Homes look different around the world; parked cars snow-covered only in some places; day vs night, seasons</td><td>The same land cover in summer vs winter, or under cloud</td><td><b>Feature shift s</b> again; there is no separate control for this kind. The shift moves every class on a satellite together, so each class sits somewhere else than it does on the other satellites, like the same forest looking different in another season. It imitates this kind only roughly.</td></tr>
<tr><td><b>Same features, different label</b> (concept shift)</td><td>P<sub>i</sub>(y | x)</td><td>Sentiment and next-word labels vary by person and region</td><td>Two operators label the same scene differently</td><td><b>None.</b> The demo does not model this kind: every point keeps the label of the cluster it was drawn from. Modelling it would mean giving the same input different labels on different satellites.</td></tr>
<tr><td><b>Quantity skew</b> (unbalancedness)</td><td>How much data each client has</td><td>Clients can hold vastly different amounts</td><td>Different imaging volumes per satellite</td><td><b>Unequal sizes</b> (the checkbox). Off, every satellite holds 50 images. On, each satellite’s size n<sub>k</sub> is drawn at random, never below 12, so some satellites hold several times as many images as others. FedAvg weights each satellite by n<sub>k</sub> / n, so a larger satellite pulls the average harder.</td></tr>
</table></div>
<p class="cap"><b>Two more from the same section.</b> If Q, the distribution over which clients take part, changes during training, independence is violated; an example is phones that train at night, which ties participation to longitude. For satellites the analogue is that which satellites are in contact depends on orbit and place, which Module 4 takes up. Training and deployment clients can also differ (dataset shift). Real datasets probably mix these effects, and most synthetic non-IID experiments only use label skew, made by splitting a flat dataset by label. This module’s sliders do the same kind of synthetic splitting.</p>
</section>

<section class="box sec" id="s3">
<h2>3 Set the skew and look at the partition</h2>
<p class="cap" style="margin:0 0 8px">The toy: 4 classes, A to D (think of them as land-cover types), each a blob of points in a 2-D feature space, six satellites. The model is a small linear softmax classifier with 12 numbers. It is a stand-in so the effects are visible; it is not satellite imagery.</p>
<h3 class="sub">What the settings look like</h3>
<p class="cap" style="margin:0 0 8px">Each square is one partition of the same 300 images over six satellites (rows S1 to S6) and four classes (columns A to D); darker means a larger share of that satellite’s images. These are drawn from the same code as the demo below, with the same random seed, so you can compare them with the controls. The first is close to IID. The last gives every satellite exactly one class, handed out in turn (S1 only A, S2 only B, and so on), so the satellites differ as much as they can.</p>
<div class="six" id="gal"></div>
<div class="two">
<div>
<div class="ctl" style="margin:0 0 6px"><button type="button" id="mdir" class="p">Label mix (Dirichlet α)</button><button type="button" id="mcls">Classes per satellite (n)</button></div>
<div class="sl v" id="rowa"><label for="al">Dirichlet α</label><input id="al" type="range" min="0" max="5" value="3"><output id="alo"></output></div>
<div class="sl v" id="rown" style="display:none"><label for="nc">Classes per satellite n</label><input id="nc" type="range" min="1" max="4" value="1"><output id="nco"></output></div>
<div class="sl v"><label for="sh">Feature shift s</label><input id="sh" type="range" min="0" max="2" step="0.1" value="0"><output id="sho"></output></div>
<label style="display:block;font-size:14px;color:var(--mute);margin-top:10px"><input type="checkbox" id="uq"> Unequal sizes (quantity skew)</label>
<div class="ctl"><button type="button" id="rs">Resample the data</button></div>
<p class="cap" id="cov" style="margin-top:8px"></p>
</div>
<div>
<svg id="mix" viewBox="0 0 360 190" role="img" aria-label="Class mix of each satellite, as stacked bars"></svg>
<div class="lg" id="lgc"></div>
<p class="cap" id="skw" style="margin-top:6px"></p>
</div>
</div>
<div class="two" style="margin-top:12px">
<div>
<svg id="sc" viewBox="0 0 300 300" role="img" aria-label="Scatter plot of the points held by the selected satellites"></svg>
<div class="ctl" id="chips" style="margin-top:6px"></div>
</div>
<div>
<div class="f">class mix of satellite k:
  p_k = (p_k,A, p_k,B, p_k,C, p_k,D)
Dirichlet mode:  p_k ~ Dirichlet(α)
n-class mode:    n classes each,
                 k, k+1, ... (wrapping)
feature shift:   inputs of satellite k
                 move by s, random angle</div>
<p class="key"><b>Symbols.</b> <b>α</b>: Dirichlet concentration. Large α gives every satellite a mix close to the global one (near-IID). Small α puts most of a satellite’s data in one or two classes. <b>n</b>: how many classes each satellite sees at all (4 means all of them). The classes are handed out in turn: with n = 1, S1 sees only A, S2 only B, and so on. IID asks that the satellites look like one another, not that each one be simple, so the fewer classes each satellite gets, the less alike they are; at n = 4 every satellite sees every class and they all look alike. <b>s</b>: size of the per-satellite shift, in the same units as the features; each class blob has spread 1 and the blob centres sit at ±1.5. <b>n<sub>k</sub></b>: how many images satellite k holds (50 each unless “unequal sizes” is on).</p>
</div>
</div>
<h3 class="sub">What each control does</h3>
<ul class="cap" style="margin:4px 0 8px;padding-left:20px">
<li><b>Label mix (Dirichlet α):</b> each satellite’s class shares are drawn at random. A large α gives every satellite about the same mix, and a small α lets one or two classes take most of a satellite’s share.</li>
<li><b>Classes per satellite (n):</b> each satellite gets exactly n of the four classes, handed out in turn.</li>
<li><b>Feature shift s:</b> moves all of one satellite’s points by s in a random direction.</li>
<li><b>Unequal sizes:</b> satellites hold different numbers of images.</li>
<li><b>Resample:</b> draws the same kind of split again. Small α varies a lot between draws.</li>
</ul>
<p class="cap"><b>Reading the sliders.</b> The slider offers α = 100 (effectively IID), 1, 0.5, 0.3, 0.2 and 0.1, a range used in published split-learning experiments. “Resample” changes the random seed of the generated partition.</p>
</section>

<section class="box sec" id="s4">
<h2>4 Train on it: federated averaging against two baselines</h2>
<p class="cap" style="margin:0 0 8px" id="cur"></p>
<p class="cap" style="margin:0 0 8px">Three runs use the same data and the same number of local steps. <b>Pooled</b> trains on all the data in one place, as if you could download everything (Module 2 says you usually cannot). <b>FedAvg, IID re-deal</b> shuffles the same images and deals them back out to the satellites in the same sizes, so only the <em>distribution across satellites</em> changes. <b>FedAvg, your partition</b> uses the skew you set in section 3. All six satellites join every round (partial participation is Module 4). The gap is biggest in the first few rounds, so try lowering Rounds to 3.</p>
<div class="two">
<div>
<svg id="cv" viewBox="0 0 380 230" role="img" aria-label="Test accuracy over rounds for three runs"></svg>
<div class="lg"><span><i style="background:var(--mute)"></i>Pooled</span><span><i style="background:var(--c1)"></i>FedAvg, IID re-deal</span><span><i style="background:var(--c0)"></i>FedAvg, your partition</span></div>
</div>
<div>
<div class="sl v"><label for="E">Local epochs E</label><input id="E" type="range" min="1" max="50" value="20"><output id="Eo"></output></div>
<div class="sl v"><label for="lr">Learning rate η</label><input id="lr" type="range" min="0.1" max="1" step="0.05" value="0.5"><output id="lro"></output></div>
<div class="sl v"><label for="R">Rounds R</label><input id="R" type="range" min="3" max="40" value="15"><output id="Ro"></output></div>
<div class="sl v"><label for="mu">Proximal strength μ</label><input id="mu" type="range" min="0" max="1.5" step="0.1" value="0"><output id="muo"></output></div>
<div class="scroll"><table class="wrap" style="margin-top:10px">
<tr><th></th><th>Pooled</th><th>IID re-deal</th><th>Your partition</th></tr>
<tr><td>Final accuracy</td><td id="fp">–</td><td id="fi">–</td><td id="fc">–</td></tr>
<tr><td>Rounds to be within 2 points of pooled</td><td>–</td><td id="ri">–</td><td id="rc">–</td></tr>
<tr><td>Update agreement, round 1</td><td>–</td><td id="ai">–</td><td id="ac">–</td></tr>
</table></div>
</div>
</div>
<p class="say" id="v4" style="margin:10px 0 0;font-size:14px;min-height:0"></p>
<div class="ctl"><button type="button" id="ten">Average over 10 random draws</button></div>
<p class="cap" id="tenr" role="status" style="min-height:20px"></p>
<p class="cap" style="margin-top:10px"><b>Accuracy of the global model on each class.</b> Grey outline: IID re-deal. Filled: your partition.</p>
<svg id="pc" style="max-width:480px" viewBox="0 0 380 120" role="img" aria-label="Per-class accuracy of the final global model"></svg>
<div class="f">local training (satellite k):  repeat E times:  w ← w − η · ( ∇loss_k(w) + μ · (w − w_global) )
aggregation:                      w_global ← Σ_k (n_k / n) · w_k          (n = Σ n_k)
update agreement:                 average cosine similarity between pairs of updates (w_k − w_global)</div>
<p class="key"><b>Symbols.</b> <b>w</b>: the 12 model numbers (a weight pair and a bias for each of 4 classes). <b>E</b>: local epochs, each one a full pass of gradient descent over the satellite’s own images (as in Module 1). <b>η</b>: learning rate, the step size. A step that is too large overshoots the low point of the loss. This toy’s loss is gentle, so even the slider’s top value shows no clear overshoot; bouncing needs a step several times larger. Small wobbles in the curves near the plateau come mainly from the satellites pulling in different directions (section 6), not from the step size. <b>R</b>: rounds. <b>μ</b>: strength of the proximal term from FedProx (section 6); 0 is plain FedAvg. <b>n<sub>k</sub>/n</b>: satellite k’s share of all images, its weight in the average. <b>Update agreement</b>: 1 means all satellites’ updates point the same way, 0 means unrelated. Low agreement is the sign that the local models are diverging from the global model and from each other, which is the core difficulty of non-IID data. Test accuracy is measured on 1,000 fresh points, 250 per class, drawn with no shift.</p>
<p class="cap"><b>Reading the numbers.</b> All curves are computed live from the toy model by the code on this page. If the data had no shift and the classes were perfectly known, the best any classifier could do on this layout is about 87%, by arithmetic: each axis is separated at a point 1.5 spread-units from each blob, so Φ(1.5)² ≈ 0.933² ≈ 0.87. With only 1,000 test points an accuracy has about ±1 point of sampling noise, so differences of a point or two are not meaningful on one draw. “Rounds to be within 2 points” and “update agreement” are the measures used here. The 10-draw button repeats the whole experiment with ten seeds and reports the mean and spread.</p>
<p class="cap"><b>When the IID re-deal scores lower.</b> With a large feature shift (s = 2, for example) the re-deal can end below your partition, and so can the pooled run, even though all three use the same images. The test points are drawn with no shift. The pooled run and the re-deal mix the six differently shifted clouds together, which blurs each class, and the model fits that blur instead of the clean test points. On your partition each satellite first trains on its own cloud, which is clean by itself, so less is lost. Over 200 draws with the default settings and s = 2, the partition ended about 1 point above the re-deal with an even label mix (α = 100) and about 4 points above it at α = 0.3. Giving every satellite the same shift removes the effect, and with one class per satellite the re-deal still comes out ahead on average. So with feature shift on, the re-deal no longer isolates the label skew: set s = 0 to compare the label skew alone.</p>
<p class="cap est" style="margin:2px 0 8px;font-style:italic">Not exact: shown to illustrate a trend.</p>
<h3 class="sub">What goes wrong when updates disagree</h3>
<div class="loop l3">
<div><b>Conflicting updates</b>Each satellite’s update is biased toward its own data. Averaged together, the updates can pull the model in different directions, so the path toward a good model can zigzag instead of running straight. Low update agreement, above, is this measured.</div>
<div><b>Model drift</b>The zigzag can keep the shared model from settling: it may oscillate or stall instead of approaching the best single model. Section 6 draws one cause, client drift, where each satellite runs toward its own best model.</div>
<div><b>A compromise model</b>Even when training settles, the result is a compromise. It is not the best model for any one satellite or for the whole mix, and it often scores lower than a model trained on IID data. Section 5 compares it with each satellite’s own model.</div>
</div>
<p class="cap" style="margin-top:8px">In this toy you see the mild versions: low agreement, slower early progress, and a final model often a little below the IID re-deal. Stronger skew makes all three worse, and in harder settings training can fail to reach an accurate model at all.</p>
</section>

<section class="box sec" id="s5">
<h2>5 Each satellite on its own, and the global model on each satellite</h2>
<p class="cap" style="margin:0 0 8px">Same partition as section 3. For each satellite: its class mix, how well the <em>global</em> model does on that satellite’s own images, how well a model trained only on that satellite does on its own images, and how well that local-only model does on the global test set. The local-only models get the same total number of gradient steps (R × E) and no averaging.</p>
<div class="scroll"><table id="tb" class="wrap">
<tr><th>Satellite</th><th>Images n<sub>k</sub></th><th>Class mix</th><th>Global model, own data</th><th>Local-only, own data</th><th>Local-only, global test</th></tr>
</table></div>
<p class="cap" style="margin-top:8px"><b>What to look for.</b> With n = 1 (one class per satellite) a local-only model is perfect on its own data and only about 25 to 50% on the global test, because it learns to say one thing. The same point in words: if each client’s P<sub>i</sub>(y) has only a single label, finding a good global model can be hard but a good local model is trivial, since a constant prediction suffices. This is also Module 1’s missing-digits result in a controlled form. The global model is a compromise in the same sense: on a satellite’s own images it scores at or a little below that satellite’s local-only model (compare the two columns), but it keeps working on every class, which the local-only model does not.</p>
<p class="cap est" style="margin:2px 0 8px;font-style:italic">Not exact: shown to illustrate a trend.</p>
<p class="cap"><b>Reading the numbers.</b> Computed live from the toy, as in section 4. “Own data” accuracy uses the satellite’s training images, so the local-only column is optimistic; the model is small enough that overfitting is slight, but it is not a held-out score.</p>
</section>

<section class="box sec" id="s6">
<h2>6 What helps</h2>
<p class="cap" style="margin:0 0 8px">Non-IID data can slow convergence, make training less stable and in bad cases make it diverge. These are the common responses. The proximal slider in section 4 lets you try the first.</p>
<h3 class="sub">Why disagreement hurts: client drift, drawn</h3>
<p class="cap" style="margin:0 0 8px">Here each satellite’s loss is drawn as a tilted oval bowl (dashed). Its low point is the spot that fits that satellite’s data best. The ✕ is the best single model for everyone together. Starting from the black dot at the lower left, the black path is the shared model over 15 rounds of averaging. With one local step per round the path ends on the ✕. With many local steps each satellite runs all the way to the bottom of its own bowl, and the average of those bottoms is not the ✕.</p>
<div class="two">
<div><svg id="dr" viewBox="0 0 360 300" role="img" aria-label="Three loss bowls, their optima, and the path of federated averaging"></svg></div>
<div>
<div class="sl v"><label for="drs">Disagreement between satellites</label><input id="drs" type="range" min="0" max="10" value="10"><output id="drso"></output></div>
<div class="sl v"><label for="dre">Local steps per round E</label><input id="dre" type="range" min="1" max="50" value="20"><output id="dreo"></output></div>
<div class="stats" style="margin-top:12px"><div><b id="drd">–</b><span>distance from the best single model</span></div><div><b id="drc">–</b><span>update agreement, round 1</span></div></div>
<p class="cap" id="drt" style="margin-top:8px"></p>
<div class="lg"><span><i style="background:var(--ink)"></i>shared model path</span><span><i style="background:var(--acc)"></i>best single model ✕</span></div>
</div>
</div>
<p class="key"><b>Symbols.</b> Each bowl is the loss ½ (w − a<sub>k</sub>)ᵀ H<sub>k</sub> (w − a<sub>k</sub>), where a<sub>k</sub> is satellite k’s own optimum and H<sub>k</sub> sets the oval’s shape and tilt. “Disagreement” scales how far apart the a<sub>k</sub> are: at 0 they coincide, as for IID data. E is the number of gradient steps each satellite takes per round, with step size 0.2. Update agreement is the average cosine between the satellites’ round-1 moves.</p>
<p class="cap"><b>What this shows.</b> Three quadratic bowls with fixed shapes, equal weights for the three satellites, and no sampling noise. It reproduces a known effect: FedAvg with many local steps settles away from the pooled optimum when client objectives differ, because with too many epochs each client drifts toward its own data. It is not the model of the demo above, and the distances are in map units.</p>
<p class="cap est" style="margin:2px 0 8px;font-style:italic">Not exact: shown to illustrate a trend.</p>
<div class="loop l2">
<div><b>Limit how far local training drifts</b>FedProx adds a proximal term that keeps each local model near the global one, and lets slow clients contribute partial work. It has been reported to improve on FedAvg empirically. In this toy it helps the first few rounds a little and does little for the final accuracy; try μ between 0.5 and 1. In this toy the local steps become unstable once η × μ exceeds about 2, so the sliders are limited to stay below that.</div>
<div><b>Do fewer local steps</b>The analysis of local SGD gets worse under non-IID data: to reach the same rate the number of local updates has to be much smaller than in the IID case. Move E down in section 4 and watch the gap to the IID re-deal close; the toy shows the same direction.</div>
<div><b>Share a small common dataset, or model outputs</b>A small globally shared dataset can be used (public, non-sensitive, or a distillation of the data) to make clients more similar. For example, the server holds a small public set that every client uses to fine-tune its local model. Related is knowledge distillation: clients share what their models output (their logits, the scores before the final probabilities) instead of raw data. Sending local data to the server breaks the privacy premise of FL, and sending proxy data to everyone needs effort to collect.</div>
<div><b>Stop insisting on one model</b>Personalized or multi-task models are another option. Each client’s identity then becomes part of the model, which makes the degenerate cases easy (section 5). The cost is that a client with no data has no model, and a single global model is easier to validate before deployment.</div>
<div style="grid-column:1/-1"><b>Choose or group the clients</b>Instead of picking clients at random, a round can pick clients whose combined data looks more like the whole, so the sample is more representative. Hierarchical FL goes further: it groups clients with similar data, trains a sub-model for each group, then combines the sub-models into the global model. Which satellites can join a round is set by the orbit (Module 4), so free choice is limited. The demo uses all six satellites every round, so it cannot show this one.</div>
</div>
<p class="cap" style="margin-top:10px">Different kinds of skew call for different fixes. Under feature skew the labelling rule P(y | x) is shared, so one global model can make sense. When the same features get different labels on different clients, some personalization may be essential. And limiting any one client’s contribution, which privacy also needs (Module 1 section 7), is another way to change the objective under heterogeneity. Each of these trades something for its gain, often extra communication or extra computation, so a more robust method is not free.</p>
</section>

<section class="box sec" id="s7">
<h2>7 How satellite studies handle it</h2>
<div class="scroll"><table class="wrap">
<tr><th>Study</th><th>How data is made non-IID</th><th>What it reports</th></tr>
<tr><td>Split federated learning on satellites</td><td>EuroSAT (27,000 images, 10 categories) and RESISC45 (31,500 images, 45 scene classes); 12 satellites in 3 orbital planes; VGG-16. Class mix per satellite follows a Dirichlet(α) split, or a “pathological” split with only n classes.</td><td>Sequential split learning (the model is cut between satellite and ground, and satellites take turns; Module 8) is fast under IID but is not robust under non-IID data (smaller α or n), since each global update depends on data from a single satellite. The design adds class balance to which gradients are sent. A motivating figure uses α = 0.5 to show that missing gradients cause local overfitting, worse under high heterogeneity.</td></tr>
<tr><td>Federated learning in satellite constellations</td><td>ResNet-18 on CIFAR-10, 40 satellites in 5 orbital planes. Half of the 10 classes go to 20 satellites (orbits one and two and the first four of orbit three); the other half go to the remaining 20. So each satellite sees 5 of 10 classes.</td><td>FedSat, an asynchronous method, beat FedAvg and FedAsync in convergence time with a single ground station in Bremen, including on non-IID data. Satellite participation rates differ, and handling this algorithmically is an open problem.</td></tr>
</table></div>
<h3 class="sub">The constellation split, drawn</h3>
<svg id="mt" style="max-width:640px" viewBox="0 0 460 190" role="img" aria-label="A grid of 5 orbital planes of 8 satellites; the first 20 hold half the classes and the remaining 20 hold the other half"></svg>
<p class="cap" style="margin-top:4px">The constellation has 40 satellites in 5 orbital planes. The first 20 (planes 1 and 2 and the first four satellites of plane 3) share half of the CIFAR-10 classes equally; the other 20 share the other half. The order within plane 3 is only indicative.</p>
<p class="cap"><b>How to read this.</b> CIFAR-10 and EuroSAT are ordinary image sets split by a rule, not data recorded by satellites with real ground tracks.</p>
</section>

<section class="box sec" id="s8">
<h2>8 What this demo can and cannot tell you</h2>
<ul class="cap" style="margin:4px 0 0;padding-left:20px">
<li>A linear model on two features is far simpler than the CNNs used in practice. The class-mix effect shows clearly in update agreement and in per-satellite results, but the final-accuracy gap is often only a few points here. Larger effects (slower, unstable or divergent training) are described in harder settings and are not reproduced here.</li>
<li>In this toy the non-IID cost shows up mostly as slower progress. With one class per satellite, the gap to the IID re-deal averages about 5 points after 2 rounds, 3 after 5 and under 2 after 15 (10 seeds, E = 20, η = 0.5; reproduce it with the 10-draw button and Rounds set to 2, 5 and 15).</li>
<li>One draw can mislead. If a class barely appears anywhere (small α), no method can learn it, and the pooled run suffers too. The 10-draw button shows how much results move between draws.</li>
<li>All six satellites take part every round and each one holds the same number of images unless you switch that. Real satellites join unevenly (Module 4) and arrive stale (Module 5).</li>
<li>Concept shift (same input, different label) is not modelled, and the feature shift is a simple per-satellite offset.</li>
</ul>
</section>

<section class="box sec" id="keypoints">
<h2>Key points</h2>
<ul class="cap" style="margin:4px 0 0;padding-left:20px">
<li>Data is IID when every client’s share looks like a random sample of the whole. Satellites are rarely IID, because what a satellite sees depends on where and when it looks.</li>
<li>Non-IID data comes in five kinds: label skew, feature skew, the same label looking different, the same features getting different labels, and unequal amounts. Orbits mostly create label skew and feature skew.</li>
<li>The effects to watch are updates that disagree (low update agreement), slower progress in early rounds, and weaker accuracy on some classes. In this toy the final-accuracy gap is small, and the larger effects appear in harder settings.</li>
<li>Responses include fewer local steps, a proximal term (FedProx), choosing or grouping clients, a small shared dataset or shared model outputs, and personalized models. Each has a cost.</li>
</ul>
</section>

<section class="box q" style="margin-top:16px">
<h2>Check your understanding</h2>
<div class="q2">
<div>One satellite flies over open ocean and another over farmland, so their class proportions differ. Which kind of non-IID is this?</div>
<button type="button" data-m="Not quite. Feature skew changes how the inputs look, with the labelling rule shared. Here the proportion of each class differs.">Feature distribution skew</button>
<button type="button" data-m="Right. P_i(y) differs between clients, as with kangaroos found only in certain regions. (Your toy’s Dirichlet and n-class sliders make exactly this.)">Label distribution skew</button>
<button type="button" data-m="Not quite. Quantity skew is about how much data each client holds, not what is in it.">Quantity skew</button>
<p class="fb" role="status" style="min-height:44px;margin:10px 0 0;font-size:14px"></p>
</div>
<div class="q2" style="margin-top:14px">
<div>The same land cover looks different in summer and in winter. Which kind is that?</div>
<button type="button" data-m="Right. P_i(x | y) changes while the label’s frequency can stay the same. Seasonal effects and day versus night belong under this heading.">Same label, different features</button>
<button type="button" data-m="Not quite. The label has not changed meaning; the look of the same label has.">Same features, different label</button>
<button type="button" data-m="Not quite. Label skew is about how often each class occurs.">Label distribution skew</button>
<p class="fb" role="status" style="min-height:44px;margin:10px 0 0;font-size:14px"></p>
</div>
<div class="q2" style="margin-top:14px">
<div>In section 5, set n = 1. Why is each local-only model perfect on its own data but poor on the global test?</div>
<button type="button" data-m="Not quite. The model is the same size. It is the data that is narrow.">The model is too small</button>
<button type="button" data-m="Right. With one class it can just predict that class, which is trivially accurate locally and wrong for the other three classes. This is the constant-prediction point.">It learns to predict its one class everywhere</button>
<button type="button" data-m="Not quite. Nothing is lost in transmission; local-only models are never averaged.">Its updates were lost in transmission</button>
<p class="fb" role="status" style="min-height:44px;margin:10px 0 0;font-size:14px"></p>
</div>
<div class="q2" style="margin-top:14px">
<div>What does a small Dirichlet α, such as 0.1, do to the partition?</div>
<button type="button" data-m="Right. Small α makes each satellite’s class shares very uneven, so most of its images fall in one or two classes (compare the α = 0.1 square in section 3).">It puts most of each satellite’s images in one or two classes</button>
<button type="button" data-m="Not quite. That is what a large α does: every satellite’s mix then looks like the whole.">It gives every satellite the same mix of classes</button>
<button type="button" data-m="Not quite. Image counts are set by the unequal sizes switch, not by α.">It gives some satellites far more images than others</button>
<p class="fb" role="status" style="min-height:44px;margin:10px 0 0;font-size:14px"></p>
</div>
</section>
<p class="key" style="margin-top:16px">Next: Module 4, intermittent contact (choose it from the module list at the top of the page)</p>
</main>

<script>
function rng(a){return function(){a|=0;a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
function gauss(r){return Math.sqrt(-2*Math.log(1-r()))*Math.cos(6.2832*r())}
function gamma(a,r){if(a<1){return gamma(a+1,r)*Math.pow(r(),1/a)}var d=a-1/3,c=1/Math.sqrt(9*d);for(;;){var x=gauss(r),v=1+c*x;if(v<=0)continue;v=v*v*v;var u=r();if(Math.log(u)<.5*x*x+d-d*v+d*Math.log(v))return d*v}}
var C=4,K=6,CEN=[[-1.5,-1.5],[1.5,-1.5],[-1.5,1.5],[1.5,1.5]],SD=1.0;
function pt(c,r){return{x:CEN[c][0]+gauss(r)*SD,y:CEN[c][1]+gauss(r)*SD,c:c}}
// o: {mode:'dir'|'cls', alpha, ncls, shift, unequal, seed}
function makeData(o){
 var r=rng(o.seed||11),sizes=[],i,k,c;
 for(k=0;k<K;k++)sizes.push(o.unequal?Math.max(12,Math.round(50*Math.exp(0.9*gauss(r)-0.4))):50);
 var cl=[];
 for(k=0;k<K;k++){
  var p=[];
  if(o.mode=='cls'){for(c=0;c<C;c++)p.push(0);for(var j=0;j<o.ncls;j++)p[(k+j)%C]=1/o.ncls}
  else{var s=0;for(c=0;c<C;c++){var gv=gamma(o.alpha,r);p.push(gv);s+=gv}for(c=0;c<C;c++)p[c]/=s}
  var ang=r()*6.2832,sh=[Math.cos(ang)*o.shift,Math.sin(ang)*o.shift],d=[];
  for(i=0;i<sizes[k];i++){var u=r(),acc=0,cc=C-1;for(c=0;c<C;c++){acc+=p[c];if(u<acc){cc=c;break}}var q=pt(cc,r);q.x+=sh[0];q.y+=sh[1];d.push(q)}
  cl.push({d:d,p:p,n:sizes[k]})}
 var rt=rng(777),test=[];for(i=0;i<1000;i++)test.push(pt(i%C,rt));
 return{cl:cl,test:test}}
function redeal(D,seed){var r=rng(seed),all=[];D.cl.forEach(function(c){c.d.forEach(function(q){all.push(q)})});
 for(var i=all.length-1;i>0;i--){var j=Math.floor(r()*(i+1)),t=all[i];all[i]=all[j];all[j]=t}
 var o=0,cl=D.cl.map(function(c){var d=all.slice(o,o+c.n);o+=c.n;var cnt=[0,0,0,0];d.forEach(function(q){cnt[q.c]++});return{d:d,p:cnt.map(function(v){return v/c.n}),n:c.n}});return{cl:cl,test:D.test}}
// params: array length C*3 : [wx,wy,b] per class
function logits(w,q){var z=[],m=-1e9,c;for(c=0;c<C;c++){var v=w[c*3]*q.x+w[c*3+1]*q.y+w[c*3+2];z.push(v);if(v>m)m=v}var s=0;for(c=0;c<C;c++){z[c]=Math.exp(z[c]-m);s+=z[c]}for(c=0;c<C;c++)z[c]/=s;return z}
function acc(w,d){var a=0;d.forEach(function(q){var p=logits(w,q),b=0;for(var c=1;c<C;c++)if(p[c]>p[b])b=c;if(b==q.c)a++});return a/d.length}
function classAcc(w,d){var a=[0,0,0,0],n=[0,0,0,0];d.forEach(function(q){var p=logits(w,q),b=0;for(var c=1;c<C;c++)if(p[c]>p[b])b=c;n[q.c]++;if(b==q.c)a[q.c]++});return a.map(function(v,i){return n[i]?v/n[i]:null})}
function train(w0,d,E,lr,mu,g){var w=w0.slice();for(var e=0;e<E;e++){var gr=new Array(C*3).fill(0);d.forEach(function(q){var p=logits(w,q);for(var c=0;c<C;c++){var r=p[c]-(q.c==c?1:0);gr[c*3]+=r*q.x;gr[c*3+1]+=r*q.y;gr[c*3+2]+=r}});for(var k=0;k<C*3;k++){var gg=gr[k]/d.length;if(mu)gg+=mu*(w[k]-g[k]);w[k]-=lr*gg}}return w}
function cosine(a,b){var s=0,x=0,y=0;for(var i=0;i<a.length;i++){s+=a[i]*b[i];x+=a[i]*a[i];y+=b[i]*b[i]}return x&&y?s/Math.sqrt(x*y):0}
function fedavg(D,o){var g=new Array(C*3).fill(0),h=[acc(g,D.test)],cos1=null;
 var n=D.cl.reduce(function(s,c){return s+c.n},0);
 for(var t=0;t<o.rounds;t++){var ws=D.cl.map(function(c){return train(g,c.d,o.E,o.lr,o.mu,g)});
  if(t==0){var ds=ws.map(function(w){return w.map(function(v,i){return v-g[i]})}),s=0,m=0;for(var i=0;i<ds.length;i++)for(var j=i+1;j<ds.length;j++){s+=cosine(ds[i],ds[j]);m++}cos1=s/m}
  var ng=new Array(C*3).fill(0);ws.forEach(function(w,i){var f=D.cl[i].n/n;for(var k=0;k<C*3;k++)ng[k]+=f*w[k]});g=ng;h.push(acc(g,D.test))}
 return{h:h,g:g,cos1:cos1}}
function pooled(D,o){var all=[];D.cl.forEach(function(c){c.d.forEach(function(q){all.push(q)})});var g=new Array(C*3).fill(0),h=[acc(g,D.test)];for(var t=0;t<o.rounds;t++){g=train(g,all,o.E,o.lr,0,g);h.push(acc(g,D.test))}return{h:h,g:g}}


(function(){
var $=function(i){return document.getElementById(i)};
function css(n){return getComputedStyle(document.documentElement).getPropertyValue(n).trim()}
var ALPHAS=[100,1,0.5,0.3,0.2,0.1],NAMES=['A','B','C','D'];
var S={mode:'dir',seed:11,sel:-1};
function cols(){return [css('--c0'),css('--c1'),css('--c2'),css('--c3')]}
function opts(){return{mode:S.mode,alpha:ALPHAS[+$('al').value],ncls:+$('nc').value,shift:+$('sh').value,unequal:$('uq').checked,seed:S.seed}}
function pct(v){return v==null?'–':(v*100).toFixed(0)+'%'}
function pct1(v){return (v*100).toFixed(1)+'%'}
var D,I,A,B,P,op,loc;
function compute(){
 var o=opts();D=makeData(o);I=redeal(D,5+S.seed);
 op={rounds:+$('R').value,E:+$('E').value,lr:+$('lr').value,mu:+$('mu').value};
 A=fedavg(D,op);B=fedavg(I,op);P=pooled(D,{rounds:op.rounds,E:op.E,lr:op.lr});
 loc=D.cl.map(function(c){var w=train(new Array(12).fill(0),c.d,op.rounds*op.E,op.lr,0,null);return{own:acc(w,c.d),glob:acc(w,D.test)}});
}
function labels(){
 var o=opts();
 $('alo').textContent=o.alpha>=100?'100 (≈IID)':o.alpha;$('nco').textContent=o.ncls+(o.ncls==4?' (IID-like)':'');
 $('sho').textContent=o.shift.toFixed(1);
 $('Eo').textContent=$('E').value;$('lro').textContent=(+$('lr').value).toFixed(2);$('Ro').textContent=$('R').value;$('muo').textContent=(+$('mu').value).toFixed(1);
 $('cur').textContent='Current partition (from section 3): '+(o.mode=='dir'?'Dirichlet α = '+(o.alpha>=100?'100 (≈IID)':o.alpha):o.ncls+' class'+(o.ncls>1?'es':'')+' per satellite')+', feature shift s = '+o.shift.toFixed(1)+', '+(o.unequal?'unequal':'equal')+' sizes.';
}
function drawMix(){
 var c=cols(),h='',W=360,y0=6,bh=22,gap=8;
 D.cl.forEach(function(s,k){var y=y0+k*(bh+gap),x=34;
  h+='<text x="0" y="'+(y+15)+'" font-size="12" fill="'+css('--mute')+'">S'+(k+1)+'</text>';
  for(var j=0;j<4;j++){var w=s.p[j]*(W-34-52);if(w>0)h+='<rect x="'+x+'" y="'+y+'" width="'+w+'" height="'+bh+'" fill="'+c[j]+'"/>';x+=w}
  h+='<text x="'+(W-48)+'" y="'+(y+15)+'" font-size="12" fill="'+css('--mute')+'">n = '+s.n+'</text>'});
 $('mix').innerHTML=h;
 $('lgc').innerHTML=NAMES.map(function(n,j){return '<span><i style="background:'+c[j]+'"></i>Class '+n+'</span>'}).join('');
 var tot=[0,0,0,0];D.cl.forEach(function(s){s.d.forEach(function(q){tot[q.c]++})});
 var miss=[];tot.forEach(function(v,j){if(v<5)miss.push(NAMES[j])});
 var nT=0,q4=[0,0,0,0];D.cl.forEach(function(s){nT+=s.n;for(var j=0;j<4;j++)q4[j]+=s.n*s.p[j]});q4=q4.map(function(v){return v/nT});
 var sk=0;D.cl.forEach(function(s){var tv=0;for(var j=0;j<4;j++)tv+=Math.abs(s.p[j]-q4[j]);sk+=s.n/nT*tv/2});
 $('skw').innerHTML='<b>Skew score '+sk.toFixed(2)+'.</b> The average gap between each satellite’s class shares and the pooled shares: half the sum of the absolute differences, averaged over satellites. 0 means every satellite has the same mix; with four equally common classes the largest possible value is 0.75 (one class each). Compare it with update agreement in section 4.';
 $('cov').textContent=miss.length?'Class '+miss.join(', ')+' has almost no examples on any satellite, so no method can learn it from this draw. Press Resample.':'';
}
function drawScatter(){
 var c=cols(),h='',sc=30,o=150;
 h+='<rect x="0" y="0" width="300" height="300" fill="none" stroke="'+css('--line')+'"/>';
 h+='<line x1="150" x2="150" y1="0" y2="300" stroke="'+css('--line')+'"/><line y1="150" y2="150" x1="0" x2="300" stroke="'+css('--line')+'"/>';
 CEN.forEach(function(p,j){h+='<circle cx="'+(o+p[0]*sc)+'" cy="'+(o-p[1]*sc)+'" r="'+(sc*1)+'" fill="none" stroke="'+c[j]+'" stroke-dasharray="3 3" opacity=".6"/>'});
 D.cl.forEach(function(s,k){if(S.sel>=0&&S.sel!=k)return;s.d.forEach(function(q){h+='<circle cx="'+(o+q.x*sc)+'" cy="'+(o-q.y*sc)+'" r="3" fill="'+c[q.c]+'" opacity=".8"/>'})});
 $('sc').innerHTML=h;
}
function chips(){
 var h=document.createElement('div');
 var el=$('chips');el.innerHTML='';
 ['All'].concat(D.cl.map(function(_,k){return 'S'+(k+1)})).forEach(function(t,i){var b=document.createElement('button');b.type='button';b.textContent=t;b.className=(S.sel==i-1)?'p':'';b.onclick=function(){S.sel=i-1;chips();drawScatter()};el.appendChild(b)});
}
function axis(){return ''}
function drawCurves(){
 var W=380,H=230,L=36,Rr=8,T=10,Bt=28,R=op.rounds,sx=function(t){return L+t/R*(W-L-Rr)},lo=.2,hi=1,sy=function(v){return T+(hi-v)/(hi-lo)*(H-T-Bt)};
 var h='';
 [.25,.5,.75,1].forEach(function(v){h+='<line x1="'+L+'" x2="'+(W-Rr)+'" y1="'+sy(v)+'" y2="'+sy(v)+'" stroke="'+css('--line')+'"/><text x="'+(L-4)+'" y="'+(sy(v)+4)+'" font-size="11" text-anchor="end" fill="'+css('--mute')+'">'+(v*100)+'%</text>'});
 h+='<line x1="'+L+'" x2="'+(W-Rr)+'" y1="'+sy(.871)+'" y2="'+sy(.871)+'" stroke="'+css('--mute')+'" stroke-dasharray="2 4"/><text x="'+(W-Rr)+'" y="'+(sy(.871)-3)+'" font-size="10" text-anchor="end" fill="'+css('--mute')+'">best possible ≈ 87%</text>';
 for(var t=0;t<=R;t+=Math.max(1,Math.round(R/6)))h+='<text x="'+sx(t)+'" y="'+(H-10)+'" font-size="11" text-anchor="middle" fill="'+css('--mute')+'">'+t+'</text>';
 h+='<text x="'+((L+W)/2)+'" y="'+(H)+'" font-size="10" text-anchor="middle" fill="'+css('--mute')+'">round</text>';
 function line(a,col,dash){return '<polyline fill="none" stroke="'+col+'" stroke-width="2.2" '+(dash?'stroke-dasharray="6 4" ':'')+'points="'+a.map(function(v,i){return sx(i).toFixed(1)+','+sy(v).toFixed(1)}).join(' ')+'"/>'}
 h+=line(P.h,css('--mute'),1)+line(B.h,css('--c1'))+line(A.h,css('--c0'));
 $('cv').innerHTML=h;
}
function within(h,target){for(var i=0;i<h.length;i++)if(h[i]>=target)return i;return null}
function stats(){
 var R=op.rounds,fp=P.h[R],fi=B.h[R],fc=A.h[R],tg=fp-.02,ri=within(B.h,tg),rc=within(A.h,tg);
 $('fp').textContent=pct1(fp);$('fi').textContent=pct1(fi);$('fc').textContent=pct1(fc);
 $('ri').textContent=ri==null?'not in '+R:ri;$('rc').textContent=rc==null?'not in '+R:rc;
 $('ai').textContent=B.cos1.toFixed(2);$('ac').textContent=A.cos1.toFixed(2);
 var gap=(fi-fc)*100,cs=B.cos1-A.cos1;
 $('v4').textContent='Update agreement falls from '+B.cos1.toFixed(2)+' (IID re-deal) to '+A.cos1.toFixed(2)+' (your partition). The final-accuracy gap is '+gap.toFixed(1)+' points on this draw'+(Math.abs(gap)<2?', which is within the draw-to-draw noise of a single run (often 1 to 2 points; press “Average over 10 random draws” for a steadier number)':'')+'. '+(rc==null?'Your partition did not get within 2 points of pooled in '+R+' rounds.':(ri!=null&&rc>ri?'It needed '+(rc-ri)+' more round'+(rc-ri>1?'s':'')+' than the IID re-deal to get within 2 points of pooled.':''));
}
function drawClass(){
 var c=cols(),a=classAcc(A.g,D.test),b=classAcc(B.g,D.test),h='',W=380;
 for(var j=0;j<4;j++){var x=40+j*84;h+='<rect x="'+x+'" y="'+(100-b[j]*90)+'" width="30" height="'+(b[j]*90)+'" fill="none" stroke="'+css('--mute')+'"/><rect x="'+(x+34)+'" y="'+(100-a[j]*90)+'" width="30" height="'+(a[j]*90)+'" fill="'+c[j]+'"/><text x="'+(x+32)+'" y="116" font-size="11" text-anchor="middle" fill="'+css('--mute')+'">Class '+NAMES[j]+' · '+pct(a[j])+'</text>'}
 h+='<line x1="30" x2="'+(W-4)+'" y1="100" y2="100" stroke="'+css('--line')+'"/>';
 $('pc').innerHTML=h;
}
function table(){
 var c=cols(),R=op.rounds,html='<tr><th>Satellite</th><th>Images n<sub>k</sub></th><th>Class mix</th><th>Global model, own data</th><th>Local-only, own data</th><th>Local-only, global test</th></tr>';
 D.cl.forEach(function(s,k){var bar='<span style="display:flex;width:110px;height:12px">'+s.p.map(function(p,j){return p>0?'<i style="display:block;width:'+(p*100)+'%;background:'+c[j]+'"></i>':''}).join('')+'</span>';
  html+='<tr><td>S'+(k+1)+'</td><td>'+s.n+'</td><td>'+bar+'</td><td>'+pct(acc(A.g,s.d))+'</td><td>'+pct(loc[k].own)+'</td><td>'+pct(loc[k].glob)+'</td></tr>'});
 $('tb').innerHTML=html;
}
function full(){labels();compute();drawMix();drawScatter();chips();drawCurves();stats();drawClass();table();$('tenr').textContent=''}
function ten(){
 var o=opts(),a=[],b=[],p=[],lo=[];
 for(var s=1;s<=10;s++){var oo=Object.assign({},o,{seed:s}),d=makeData(oo),i=redeal(d,5+s),q={rounds:op.rounds,E:op.E,lr:op.lr,mu:op.mu};
  a.push(fedavg(d,q).h[q.rounds]);b.push(fedavg(i,q).h[q.rounds]);p.push(pooled(d,q).h[q.rounds])}
 function ms(x){var m=x.reduce(function(u,v){return u+v},0)/x.length,v=x.reduce(function(u,w){return u+(w-m)*(w-m)},0)/(x.length-1);return[m,Math.sqrt(v)]}
 var A_=ms(a),B_=ms(b),P_=ms(p),g=b.map(function(v,i){return v-a[i]}),G=ms(g);
 $('tenr').textContent='Over 10 draws (seeds 1 to 10), final accuracy: pooled '+pct1(P_[0])+' (sd '+(P_[1]*100).toFixed(1)+'), IID re-deal '+pct1(B_[0])+' (sd '+(B_[1]*100).toFixed(1)+'), your partition '+pct1(A_[0])+' (sd '+(A_[1]*100).toFixed(1)+'). Average gap, IID re-deal minus yours: '+(G[0]*100).toFixed(1)+' points (sd '+(G[1]*100).toFixed(1)+').';
}
function setMode(m){S.mode=m;$('mdir').className=m=='dir'?'p':'';$('mcls').className=m=='cls'?'p':'';$('rowa').style.display=m=='dir'?'':'none';$('rown').style.display=m=='cls'?'':'none';full()}
$('mdir').onclick=function(){setMode('dir')};$('mcls').onclick=function(){setMode('cls')};
['al','nc','sh','uq','E','lr','R','mu'].forEach(function(i){$(i).oninput=full;$(i).onchange=full});
$('rs').onclick=function(){S.seed++;full()};$('ten').onclick=ten;
Array.prototype.forEach.call(document.querySelectorAll('.q2'),function(q){var fb=q.querySelector('.fb');Array.prototype.forEach.call(q.querySelectorAll('button'),function(b){b.onclick=function(){fb.textContent=b.getAttribute('data-m')}})});
/* ---------- new visuals ---------- */
function T(x,y,s,o){o=o||{};return '<text x="'+x+'" y="'+y+'" font-size="'+(o.s||11)+'" fill="'+(o.c||css('--mute'))+'" text-anchor="'+(o.a||'start')+'"'+(o.b?' font-weight="700"':'')+'>'+s+'</text>'}
function taxo(){
 var c=cols(),ink=css('--ink'),mu=css('--mute'),ln=css('--line'),r=rng(9),h=[];
 function wrap(title,svg,cap){return '<div class="fig"><svg viewBox="0 0 150 110" role="img" aria-label="'+title+'">'+svg+'</svg><p class="cap"><b>'+title+'</b><br>'+cap+'</p></div>'}
 function side(){return '<line x1="75" x2="75" y1="14" y2="100" stroke="'+ln+'" stroke-dasharray="3 3"/>'+T(37,10,'Client 1',{a:'middle',s:9})+T(113,10,'Client 2',{a:'middle',s:9})}
 // 1 label skew
 var s='',a=[.55,.25,.1,.1],b=[.1,.15,.2,.55];
 a.forEach(function(v,j){s+='<rect x="'+(8+j*16)+'" y="'+(98-v*70)+'" width="12" height="'+(v*70)+'" fill="'+c[j]+'"/>'});
 b.forEach(function(v,j){s+='<rect x="'+(84+j*16)+'" y="'+(98-v*70)+'" width="12" height="'+(v*70)+'" fill="'+c[j]+'"/>'});
 h.push(wrap('Label skew',side()+s,'P(y) differs: classes occur in different proportions.'));
 // 2 feature skew
 s='';for(var i=0;i<18;i++){var j=i%3;s+='<circle cx="'+(24+r()*26)+'" cy="'+(36+r()*50)+'" r="3" fill="'+c[j]+'"/><circle cx="'+(98+r()*26)+'" cy="'+(36+r()*50)+'" r="3" fill="'+c[j]+'"/>'}
 h.push(wrap('Feature skew',side()+s,'P(x) differs: inputs sit in different places, same labelling rule.'));
 // 3 same label diff features
 s='';var u=function(x,col,al){var t='';for(var j=0;j<4;j++)for(var i=0;i<4;i++)t+='<rect x="'+(x+i*9)+'" y="'+(34+j*9)+'" width="8" height="8" fill="'+col+'" opacity="'+(al*(.55+.45*((i*7+j*5)%3)/2)).toFixed(2)+'"/>';return t};
 s=u(19,c[1],1)+u(95,mu,1)+T(37,90,'summer forest',{a:'middle',s:9})+T(113,90,'winter forest',{a:'middle',s:9})+T(75,104,'both labelled “forest”',{a:'middle',s:9,c:c[1]});
 h.push(wrap('Same label, different features',side()+s,'P(x | y) differs: one label looks different.'));
 // 4 same features, different label
 s='<rect x="29" y="34" width="36" height="36" fill="'+mu+'" opacity=".5"/><rect x="85" y="34" width="36" height="36" fill="'+mu+'" opacity=".5"/>'+'<rect x="22" y="76" width="50" height="16" rx="8" fill="none" stroke="'+c[0]+'"/>'+T(47,88,'“wet”',{a:'middle',s:10,c:c[0]})+'<rect x="78" y="76" width="50" height="16" rx="8" fill="none" stroke="'+c[2]+'"/>'+T(103,88,'“flooded”',{a:'middle',s:10,c:c[2]});
 h.push(wrap('Same features, different label',side()+s,'P(y | x) differs: the same input gets different labels.'));
 // 5 quantity
 s='';for(i=0;i<5;i++)s+='<circle cx="'+(30+(i%3)*8)+'" cy="'+(92-Math.floor(i/3)*8)+'" r="3.2" fill="'+ink+'"/>';for(i=0;i<30;i++)s+='<circle cx="'+(94+(i%6)*8)+'" cy="'+(92-Math.floor(i/6)*8)+'" r="3.2" fill="'+ink+'"/>';
 h.push(wrap('Quantity skew',side()+s,'One client holds far more data than another.'));
 $('tx').innerHTML=h.join('');
}
var MAPS=['AAAAAAAABBBBBAAAAAAAAAAA','AAAAABBBBBBBBBBBAAAAAAAA','AAABBBBBBBDDBBBBBAACCAAA','AAABBBBDDBBBBBBAACCCCCAA','AAAACCCCCBBBBBAAACCCCCDA','AAAACCCCCCCBBBAAAAACCDDA','AAAAAACCCCBBBBBAAAAAAAAA','AAAAAAAACBBBBBBAAAAAAAAA','AAAAAAAAAABBBBBBAAAAAAAA','AAAAAAAAAAABBBBAAAAAAAAA','AAAAAAAAAAAAAAAAAAAAAAAA','AAAAAAAAAAAAAAAAAAAAAAAA'];
function map(){
 var amp=+$('mpa').value,w=+$('mpw').value;$('mpao').textContent=amp.toFixed(1);$('mpwo').textContent=w.toFixed(1);
 var c=cols(),cell=15,h='',R=12,Cn=24,mid=[2,5.5,9],ph=[0,1.2,2.4],cnt=[[0,0,0,0],[0,0,0,0],[0,0,0,0]],ink=css('--ink');
 for(var y=0;y<R;y++)for(var x=0;x<Cn;x++){var cl='ABCD'.indexOf(MAPS[y][x]);h+='<rect x="'+(x*cell)+'" y="'+(y*cell)+'" width="'+cell+'" height="'+cell+'" fill="'+c[cl]+'" opacity=".32"/>'}
 function row(k,x){return mid[k]+amp*Math.sin(2*Math.PI*(x+.5)/Cn*1.5+ph[k])}
 for(var k=0;k<3;k++){var pts=[];for(x=0;x<Cn;x++){var ry=row(k,x);for(y=0;y<R;y++)if(Math.abs(y+.5-ry-.5+.5-.5)<=w/2){var cl2='ABCD'.indexOf(MAPS[y][x]);cnt[k][cl2]++}}
  for(var xx=0;xx<=Cn*4;xx++){var X=xx/4,Y=row(k,Math.min(Cn-.01,X));pts.push((X*cell).toFixed(1)+','+((Y+.5)*cell).toFixed(1))}
  h+='<polyline fill="none" stroke="'+ink+'" stroke-width="'+(w*cell).toFixed(1)+'" opacity=".16" stroke-linecap="butt" points="'+pts.join(' ')+'"/><polyline fill="none" stroke="'+ink+'" stroke-width="1.6" '+(k==1?'':'stroke-dasharray="'+(k==0?'6 3':'2 3')+'" ')+'points="'+pts.join(' ')+'"/>'+T(3,((row(k,0)+.5)*cell)-6,'S'+(k+1),{s:11,c:ink,b:1})}
 $('mp').innerHTML=h;
 var b='';for(k=0;k<3;k++){var tot=cnt[k].reduce(function(a,v){return a+v},0)||1,x0=40;b+=T(0,18+k*32,'S'+(k+1),{s:12,c:ink});for(var j=0;j<4;j++){var ww=cnt[k][j]/tot*250;if(ww>0)b+='<rect x="'+x0+'" y="'+(6+k*32)+'" width="'+ww+'" height="18" fill="'+c[j]+'"/>';x0+=ww}}
 $('mpb').innerHTML=b;
 $('mpl').innerHTML=['A water','B forest','C desert','D city'].map(function(n,j){return '<span><i style="background:'+c[j]+'"></i>'+n+'</span>'}).join('');
}
function gallery(){
 var sets=[['Near-IID (α = 100)',{mode:'dir',alpha:100}],['α = 1',{mode:'dir',alpha:1}],['α = 0.3',{mode:'dir',alpha:.3}],['α = 0.1',{mode:'dir',alpha:.1}],['2 classes each',{mode:'cls',ncls:2}],['1 class each',{mode:'cls',ncls:1}]],c=cols(),h='';
 sets.forEach(function(s){var o=Object.assign({shift:0,unequal:false,seed:11},s[1]),D=makeData(o),svg='';
  D.cl.forEach(function(cl,k){for(var j=0;j<4;j++){var p=cl.p[j];svg+='<rect x="'+(18+j*22)+'" y="'+(6+k*16)+'" width="20" height="14" fill="'+c[j]+'" opacity="'+(.08+.92*p).toFixed(2)+'"/>'}svg+=T(2,17+k*16,'S'+(k+1),{s:9})});
  for(var j=0;j<4;j++)svg+=T(28+j*22,112,'ABCD'[j],{a:'middle',s:9});
  h+='<div class="fig"><svg viewBox="0 0 110 118" role="img" aria-label="Class shares for '+s[0]+'">'+svg+'</svg><p class="cap" style="text-align:center">'+s[0]+'</p></div>'});
 $('gal').innerHTML=h;
}
var DRO=[[-1.5,-.8],[1.6,-.9],[0,1.7]],DRP=[[2,.3,20],[.3,2,0],[1.2,.5,-40]];
function drift(){
 var s=+$('drs').value/10,E=+$('dre').value;$('drso').textContent=s.toFixed(1);$('dreo').textContent=E;
 var H=DRP.map(function(p){var t=p[2]*Math.PI/180;return{l1:p[0],l2:p[1],c:Math.cos(t),s:Math.sin(t)}});
 function Hx(h,u){var a=h.c*u[0]+h.s*u[1],b=-h.s*u[0]+h.c*u[1];a*=h.l1;b*=h.l2;return[h.c*a-h.s*b,h.s*a+h.c*b]}
 var A=DRO.map(function(o){return[o[0]*s,o[1]*s]}),g=[-3,2.5],tr=[g.slice()],cos1=null,lr=.2,R=15,r1=null;
 for(var r=0;r<R;r++){var ws=A.map(function(a,k){var w=g.slice();for(var e=0;e<E;e++){var gr=Hx(H[k],[w[0]-a[0],w[1]-a[1]]);w=[w[0]-lr*gr[0],w[1]-lr*gr[1]]}return w});
  if(r==0){r1=ws.map(function(w){return[w[0]-g[0],w[1]-g[1]]});var sc=0,m=0;for(var i=0;i<3;i++)for(var j=i+1;j<3;j++){var u=r1[i],v=r1[j];sc+=(u[0]*v[0]+u[1]*v[1])/(Math.hypot(u[0],u[1])*Math.hypot(v[0],v[1])||1);m++}cos1=sc/m}
  g=[(ws[0][0]+ws[1][0]+ws[2][0])/3,(ws[0][1]+ws[1][1]+ws[2][1])/3];tr.push(g.slice())}
 var M=[[0,0],[0,0]],b=[0,0];H.forEach(function(h,k){var e1=Hx(h,[1,0]),e2=Hx(h,[0,1]);M[0][0]+=e1[0];M[1][0]+=e1[1];M[0][1]+=e2[0];M[1][1]+=e2[1];var ha=Hx(h,A[k]);b[0]+=ha[0];b[1]+=ha[1]});
 var det=M[0][0]*M[1][1]-M[0][1]*M[1][0],opt=[(b[0]*M[1][1]-b[1]*M[0][1])/det,(M[0][0]*b[1]-M[1][0]*b[0])/det];
 var S=44,ox=180,oy=140,X=function(v){return ox+v*S},Y=function(v){return oy+v*S},cl=[css('--c0'),css('--c1'),css('--c2')],h='';
 h+='<rect x="1" y="1" width="358" height="298" fill="none" stroke="'+css('--line')+'"/>';
 H.forEach(function(hh,k){var Lv=.8,r1_=Math.sqrt(2*Lv/hh.l1),r2_=Math.sqrt(2*Lv/hh.l2),ang=Math.atan2(hh.s,hh.c)*180/Math.PI;
  h+='<ellipse cx="'+X(A[k][0])+'" cy="'+Y(A[k][1])+'" rx="'+(r1_*S)+'" ry="'+(r2_*S)+'" transform="rotate('+ang+' '+X(A[k][0])+' '+Y(A[k][1])+')" fill="none" stroke="'+cl[k]+'" stroke-width="2" stroke-dasharray="5 3"/><circle cx="'+X(A[k][0])+'" cy="'+Y(A[k][1])+'" r="4" fill="'+cl[k]+'"/>'+T(X(A[k][0])+6,Y(A[k][1])-6,'S'+(k+1),{c:cl[k],b:1,s:12})});
 h+='<polyline fill="none" stroke="'+css('--ink')+'" stroke-width="1.8" points="'+tr.map(function(p){return X(p[0]).toFixed(1)+','+Y(p[1]).toFixed(1)}).join(' ')+'"/>';
 tr.forEach(function(p,i){h+='<circle cx="'+X(p[0])+'" cy="'+Y(p[1])+'" r="'+(i==0?5:2.4)+'" fill="'+css('--ink')+'"/>'});
 h+=T(X(tr[0][0])+8,Y(tr[0][1])+4,'start',{s:10,c:css('--ink')});
 h+='<circle cx="'+X(g[0])+'" cy="'+Y(g[1])+'" r="6" fill="none" stroke="'+css('--ink')+'" stroke-width="2"/>'+T(X(g[0])+9,Y(g[1])+14,'after 15 rounds',{s:10,c:css('--ink')});
 h+='<g stroke="'+css('--acc')+'" stroke-width="3"><line x1="'+(X(opt[0])-6)+'" y1="'+(Y(opt[1])-6)+'" x2="'+(X(opt[0])+6)+'" y2="'+(Y(opt[1])+6)+'"/><line x1="'+(X(opt[0])-6)+'" y1="'+(Y(opt[1])+6)+'" x2="'+(X(opt[0])+6)+'" y2="'+(Y(opt[1])-6)+'"/></g>';
 $('dr').innerHTML=h;
 var d=Math.hypot(g[0]-opt[0],g[1]-opt[1]);$('drd').textContent=d.toFixed(2);$('drc').textContent=s==0?'1.00':cos1.toFixed(2);
 $('drt').textContent=s==0?'With no disagreement every bowl has the same low point, so any number of local steps leads to it.':(d<.1?'With '+E+' local step'+(E>1?'s':'')+' the shared model ends essentially on the best single model.':'The shared model has settled '+d.toFixed(2)+' map units away from the best single model, pulled toward the satellites’ own low points. Fewer local steps shrink that gap.');
}
function mtt(){
 var c=cols(),h='';for(var p=0;p<5;p++){h+=T(0,24+p*30,'Plane '+(p+1),{s:11});for(var i=0;i<8;i++){var idx=p*8+i,set=idx<20?0:1,x=70+i*46,y=14+p*30;h+='<rect x="'+x+'" y="'+y+'" width="36" height="18" rx="4" fill="'+c[set]+'" opacity=".85"/>'+T(x+18,y+13,idx+1,{a:'middle',s:10,c:'#fff'})}}
 h+='<rect x="70" y="170" width="12" height="10" fill="'+c[0]+'"/>'+T(86,179,'classes 1–5 (satellites 1–20)',{s:10})+'<rect x="260" y="170" width="12" height="10" fill="'+c[1]+'"/>'+T(276,179,'classes 6–10 (satellites 21–40)',{s:10});
 $('mt').innerHTML=h;
}
function vis3(){taxo();map();gallery();drift();mtt()}
$('mpa').oninput=map;$('mpw').oninput=map;$('drs').oninput=drift;$('dre').oninput=drift;

vis3();
full();
if(window.matchMedia)matchMedia('(prefers-color-scheme:dark)').addEventListener('change',function(){full();vis3()});
})();
</script>
</body>
</html>
'''
