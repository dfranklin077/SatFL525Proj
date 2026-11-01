"""Module 4: Intermittent contact

The whole lesson as one self-contained HTML document (text, charts, sliders and
quiz all run in the browser). It is shown by interface/fl_modules.py.
"""
TITLE = 'Module 4: Intermittent contact'

HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Module 4: Intermittent contact</title>
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
</style>
</head>
<body>
<main>
<p style="margin:0 0 6px"><span class="tag">Module 4 of 8 · Live demo</span></p>
<h1>Intermittent contact: who gets to join a round</h1>
<p class="lede">Module 2 showed that a satellite can talk to a ground station for only a few minutes at a time. Here that fact becomes a rule for federated learning: a satellite can join a round only if it has one contact to receive the model and a later one to send its update back. You choose how a round ends and watch what that does to speed and to accuracy. Every number you can move is defined.</p>

<nav class="nav" aria-label="Module sections"><a href="#s1">1 What a round needs</a><a href="#s2">2 One round, three endings</a><a href="#s3">3 Train through the contacts</a><a href="#s4">4 Fast rounds can be biased</a><a href="#s5">5 What helps</a><a href="#s6">6 Limits</a></nav>

<section class="box sec" id="s1">
<h2>1 What a round needs from the orbit</h2>
<p class="cap" style="margin:0 0 8px">In Module 1 a round has three steps: the server sends the model, each satellite trains on its own images, and each satellite sends back its update. A phone does all three over wifi within minutes. A satellite can send or receive only during a <b>contact window</b>, the few minutes when it is high enough above the ground station’s horizon to hold a link (Module 2, section 2). Between windows it cannot hear the server or answer it, although it can keep training on board.</p>
<p class="cap" style="margin:0 0 8px">That turns one round into a schedule. A satellite takes part in a round only if it has one contact to <em>receive</em> the model and a later contact to <em>return</em> the update. The first contact starts its training and the second ends it. In this module each satellite’s contacts come at regular intervals. Real passes are uneven, but they can be computed from the orbit ahead of time, which is the big difference from phones, whose availability is random (Module 2, section 5).</p>
<div class="f">contacts of satellite k:        o_k,  o_k + g_k,  o_k + 2·g_k,  …
receive time (model arrives):   r_k = first contact at or after t₀
return time (update leaves):    u_k = first contact at or after r_k + τ
averaging (who is included):    w_global ← Σ over included k of (n_k / n) · w_k</div>
<p class="key"><b>Symbols.</b> <b>t₀</b>: the moment a round starts, which is when the server has finished the previous round and has a new model to send. Time is counted in hours from the start of the run. <b>g_k</b>: the <em>revisit gap</em>, the hours between satellite k’s contacts. <b>o_k</b>: the <em>offset</em>, the time of its first contact after the run starts. <b>τ</b>: <em>training time</em>, the hours satellite k needs on board to train after receiving the model. <b>n_k</b>: the number of images satellite k holds. <b>n</b>: the total number of images held by the satellites that are included. <b>Included</b>: the satellites whose update arrives in time under the rule that ends the round (section 2).</p>
<p class="cap"><b>Why a gap sets a floor.</b> A round starts at t₀. The model reaches satellite k at its next contact, somewhere between 0 and g_k hours later. If τ is shorter than the gap, the update leaves at the contact after that, one gap later. So even when the server waits as long as needed, a satellite with a 24-hour gap needs between 24 and 48 hours to take part in one round, and a satellite with a 2-hour gap needs between 2 and 4. The two contacts are separate because the model and the update both have to fit inside a window, and the algorithm sends first and receives later (Module 1, section 2). Whether a model fits inside one window is the question of Module 2, Lab 4, and here it is assumed to fit.</p>
</section>

<section class="box sec" id="s2">
<h2>2 One round, three ways to end it</h2>
<p class="cap" style="margin:0 0 8px">The server has to decide when a round is over. The choice is a rule, and it decides which satellites count. Pick a rule and move the sliders.</p>
<div class="ctl" role="group" aria-label="Rule for ending a round" style="margin:0 0 8px"><button type="button" id="pa" class="p">Wait for all</button><button type="button" id="pd">Deadline D</button><button type="button" id="pf">First n</button></div>
<svg id="tl" style="max-width:720px" viewBox="0 0 560 402" role="img" aria-label="Contact times of 12 satellites and how one round plays out"></svg>
<div class="lg" id="tll"></div>
<div class="two" style="margin-top:8px">
<div>
<div class="sl v"><label for="g2">Revisit gap of the rarely seen group</label><input id="g2" type="range" min="6" max="48" step="1" value="24" data-k="grare"><output></output></div>
<div class="sl v"><label for="t2">Training time τ</label><input id="t2" type="range" min="0.5" max="6" step="0.5" value="1" data-k="tau"><output></output></div>
<div class="sl v"><label for="d2">Deadline D</label><input id="d2" type="range" min="4" max="48" step="1" value="12" data-k="D"><output></output></div>
<div class="sl v"><label for="n2">First n of 12</label><input id="n2" type="range" min="3" max="12" step="1" value="9" data-k="nf"><output></output></div>
</div>
<div>
<div class="stats"><div><b id="inc">–</b><span>satellites included, of 12</span></div><div><b id="rl">–</b><span>round length</span></div></div>
<p class="cap" id="left" style="margin:0"></p>
</div>
</div>
<p class="cap" style="margin-top:8px"><b>Reading the figure.</b> Each row is one satellite, in three groups by how often it passes the station: <em>often</em> (6 satellites, gaps near 2 hours), <em>sometimes</em> (3 satellites, gaps near 6 hours) and <em>rarely</em> (3 satellites, with the gap you set). Each satellite’s own gap is its group’s value times a random factor between 0.8 and 1.2, and its offset is random. Grey dots are contacts. The round starts at hour 0. The blue dot is when the model arrives at a satellite, and the green dot is when its update comes back. A red ring means the update would come back after the round has already ended, so that satellite is left out. The dashed line is when the server closes the round. <b>New contact pattern</b> draws new gaps and offsets.</p>
<div class="ctl"><button type="button" id="ncp">New contact pattern</button></div>
<p class="cap est" style="margin:6px 0 8px;font-style:italic">Not exact: shown to illustrate a trend.</p>
<div class="loop l3">
<div><b>Wait for all</b>The server closes the round when the last update has arrived, so every satellite is included every round. The model sees all the data. A round lasts as long as the slowest satellite needs, which is between one and two of that satellite’s gaps when its training fits inside one gap, so a few rarely seen satellites set the pace for everyone.</div>
<div><b>Deadline D</b>The server closes the round D hours after it starts and averages the updates that have arrived by then. Rounds have a fixed, short length. A satellite whose receive and return contacts cannot both fit inside D is left out of every round, however many rounds are run, because its gap does not change.</div>
<div><b>First n</b>The server closes the round when the n-th update arrives and drops the rest (the extra clients that Module 1, section 2, mentions). Rounds are as quick as the n-th quickest satellite. The same quick satellites win round after round, so the same ones tend to be left out each time.</div>
</div>
</section>

<section class="box sec" id="s3">
<h2>3 Train through the contacts</h2>
<p class="cap" style="margin:0 0 8px" id="cur"></p>
<p class="cap" style="margin:0 0 8px">The same 12 satellites and contacts as section 2, now trained round after round from an untrained model, once with each rule. The curves are drawn against hours rather than rounds, because the clock is what contact windows change. Each satellite holds 50 images from the four classes of Module 3’s toy, and trains for E = 20 local steps with η = 0.5 each round, as in Module 3. The switch below decides whether a satellite’s data depends on how often it is seen. <b>On:</b> the six often-seen satellites hold classes A and B, the three sometimes-seen satellites hold class C, and the three rarely seen satellites hold class D. <b>Off:</b> every satellite holds a random mix of all four classes.</p>
<div class="two">
<div>
<svg id="cv" viewBox="0 0 380 230" role="img" aria-label="Test accuracy against hours for three ways of ending a round"></svg>
<div class="lg"><span><i style="background:var(--acc)"></i>Wait for all</span><span><i style="background:var(--c0)"></i>Deadline D</span><span><i style="background:var(--c3)"></i>First n</span></div>
</div>
<div>
<div class="sl v"><label for="d3">Deadline D</label><input id="d3" type="range" min="4" max="48" step="1" value="12" data-k="D"><output></output></div>
<div class="sl v"><label for="n3">First n of 12</label><input id="n3" type="range" min="3" max="12" step="1" value="9" data-k="nf"><output></output></div>
<div class="sl v"><label for="y3">Run length (days)</label><input id="y3" type="range" min="2" max="21" step="1" value="14" data-k="days"><output></output></div>
<div class="ctl" style="margin:10px 0 0"><label style="display:flex;gap:8px;align-items:center;font-size:14px;cursor:pointer"><input type="checkbox" id="tied" checked> Data depends on the orbit group</label></div>
</div>
</div>
<div class="scroll"><table class="wrap" id="tb" style="margin-top:10px"></table></div>
<p class="say" id="v3" style="margin:10px 0 0;font-size:14px;min-height:0"></p>
<p class="cap" style="margin-top:10px"><b>Accuracy of the final model on each class.</b> Same colours as the curves, one bar per rule.</p>
<svg id="pc" style="max-width:480px" viewBox="0 0 380 130" role="img" aria-label="Per-class accuracy of the final global model for each rule"></svg>
<div class="f">each included satellite k:   w_k ← train(w_global, own images)     (E = 20 steps, η = 0.5)
average:                     w_global ← Σ (n_k / n) · w_k                (over included k)
the round ends at:           all → the last u_k
                             deadline → t₀ + D
                             first n → the n-th smallest u_k
the next round starts where this one ended.</div>
<p class="key"><b>Symbols.</b> <b>D</b>: the deadline, in hours after a round starts. <b>n</b> (in “first n”): how many updates the server waits for, out of 12. <b>Run length</b>: how many days the clock runs; a round that would end after that is not counted. <b>Rounds finished</b>: rounds that closed before the run ended. This counts rounds, not learning: two rules can finish the same number of rounds and end at different accuracy, because each round averages only the satellites that were included (section 4). <b>Mean round length</b>: run time spent per finished round. <b>Hours to reach 80%</b>: the end time of the first round after which test accuracy is at least 80%. <b>Rounds joined</b>: for each group of satellites (often, sometimes or rarely seen), the average share of finished rounds in which one of its satellites was included. Test accuracy is measured on 1,000 fresh points, 250 per class, as in Module 3, where the best any classifier can do is about 87%.</p>
<p class="cap"><b>Reading the numbers.</b> Every curve is computed live by the code on this page. With the default sliders (rarely seen gap 24 hours, τ = 1 hour, D = 12 hours, n = 9, 14 days) and the switch on, waiting for all reached 80% after a median of 45 hours across ten different contact patterns (36 to 53 hours) and ended at about 87%. The deadline rule ended at about 67 to 68% and never reached 80%, and neither did first n with n = 9 (about 67%). With n = 6 the model ended near 47%. With the switch off, every rule ended near 86%, and the early-closing rules got there much sooner, with medians of 12 hours for the deadline rule, 10 for n = 9 and 4 for n = 6, against 45 for waiting for all. With 1,000 test points an accuracy carries about ±1 point of sampling noise.</p>
<p class="cap est" style="margin:2px 0 8px;font-style:italic">Not exact: shown to illustrate a trend.</p>
</section>

<section class="box sec" id="s4">
<h2>4 Why a fast round can be a biased round</h2>
<p class="cap" style="margin:0 0 8px">Closing a round early looks like a pure win: rounds are shorter, so the clock moves faster. Section 3 shows the catch. After each round the server averages only the satellites that were included, weighted by their share of the included images. The new model is therefore built from the included satellites’ data and nothing else.</p>
<div class="loop l3">
<div><b>Who is left out is not random</b>The satellites with the longest gaps are the ones that cannot finish inside a short deadline, and the same ones are slow in every round. So they are missing from every average, not from a few. A rarely seen satellite with a 24-hour gap never fits inside a 12-hour deadline.</div>
<div><b>The effect depends on the data</b>With the switch off, every satellite holds the same kind of images, so any included group teaches the model the same thing and leaving some out costs very little. With the switch on, class D lives only on the rarely seen satellites. If they never join, the model never sees class D, and its accuracy on that class falls to near zero in the bars above.</div>
<div><b>Speed, coverage, accuracy</b>Waiting for all gives coverage at the cost of time. A deadline or a small n gives time at the cost of coverage. Whether the cost shows up as lost accuracy depends on whether orbit and data are linked, which is the same question as Module 3 asked of label skew.</div>
</div>
<p class="cap" style="margin-top:8px"><b>Rounds are not the same as learning.</b> Two rules can finish the same number of rounds and still end at different accuracy, because each round teaches only what the included satellites hold. A deadline that lets some of the rarely seen satellites in on some rounds and not others teaches class D strongly in one round and weakly in the next, so the final accuracy depends on which kind of round came last. A round with none of them can also undo earlier teaching. In a separate test where all 12 satellites joined the first three rounds and the rarely seen ones were left out afterwards, accuracy on class D fell from about 88% to 49%, 20%, 6% and then 0% over the next four rounds. The satellites that did join never held a D image, so each round of training pushed the model’s score for D down.</p>
<p class="cap est" style="margin:2px 0 8px;font-style:italic">Not exact: shown to illustrate a trend.</p>
<p class="cap" style="margin-top:8px"><b>What the switch does and does not claim.</b> It shows both possible worlds side by side. In a real constellation, how strongly data depends on contact frequency is not known from this demo. A satellite that rarely passes one station may fly over very different ground, or it may not. The point is the mechanism: if the two are linked, early rounds will be biased, and if they are not, they will not.</p>
</section>

<section class="box sec" id="s5">
<h2>5 What helps</h2>
<p class="cap" style="margin:0 0 8px">Because a constellation’s contacts can be computed from its orbits, a server can plan around them instead of waiting to be surprised. These are the common ideas. Each has a cost, and later modules develop several.</p>
<div class="loop l2">
<div><b>Plan the round from the orbit</b>The server can calculate in advance every satellite’s receive and return times. It can choose a deadline long enough for the satellites it needs (up to twice the longest gap among them), or choose which satellites to wait for, instead of picking a deadline blindly. The cost is a longer round, as in the wait-for-all curve.</div>
<div><b>Select for coverage, not just speed</b>Pick the satellites that will finish in time, but check that together they cover every class, and include a slow satellite that holds a class nobody else has. This is client selection with the data in mind (Module 3, section 6). It needs the server to know roughly what each satellite holds, which can itself leak information.</div>
<div><b>Overlap the two contacts</b>Send the next model during the same contact that returns the last update, so a satellite is never idle between rounds. The price is that the update was computed from an older model, which is staleness (Module 5).</div>
<div><b>Let satellites relay for each other</b>With links between satellites, a rarely seen satellite can hand its update to a neighbour that will pass the station soon (Module 7). That shortens its effective gap without more ground stations.</div>
<div><b>Add ground stations</b>More stations in more places mean more contacts per day, so every gap shrinks. This is the direct fix and also the expensive one.</div>
<div><b>Stop waiting altogether</b>Asynchronous methods apply each update whenever it arrives, so a slow satellite never delays a round, at the price of stale updates (Module 5).</div>
</div>
</section>

<section class="box sec" id="s6">
<h2>6 What this demo can and cannot tell you</h2>
<ul class="cap" style="margin:4px 0 0;padding-left:20px">
<li>Contacts here are single moments that repeat at a fixed gap. Real contacts last minutes, differ in length, and are uneven, so the exact times will be off even though the logic (receive, train, return) holds.</li>
<li>The model and the update are assumed to fit inside one contact window each. Module 2, Lab 4, shows when that fails.</li>
<li>There is one ground station and no link failures. Packet loss would delay some updates (Module 2, Lab 3), and more stations would shorten the gaps.</li>
<li>The group gaps (about 2, 6 and a gap you set) and the group sizes are illustrative. They are not measurements of any constellation.</li>
<li>Training time τ is the same for every satellite. Satellites that train at different speeds are Module 6.</li>
<li>The learning problem is the small linear toy of Module 3. The size of the accuracy loss in section 3 comes from that toy and from the way classes are assigned to groups; the direction (speed against coverage) does not.</li>
<li>The averaging is plain FedAvg. Updates that arrive late and are still used are Module 5.</li>
</ul>
</section>

<section class="box sec" id="keypoints">
<h2>Key points</h2>
<ul class="cap" style="margin:4px 0 0;padding-left:20px">
<li>A satellite joins a round only if it has a contact to receive the model and a later one to return the update. With a revisit gap g and training that fits inside one gap, that takes between one and two gaps.</li>
<li>The server must pick a rule for ending a round: wait for all, close at a deadline, or close after the first n updates. The rule decides which satellites count.</li>
<li>Rules that close early make rounds quicker but leave out the satellites with long gaps, the same ones every time.</li>
<li>Leaving satellites out costs accuracy only when they hold data the others lack. Then the model never learns it, as class D in the demo.</li>
<li>Contacts can be computed from orbits, so servers can plan, select for coverage, overlap contacts, relay through neighbours, or add stations. Each has a cost.</li>
</ul>
</section>

<section class="box q" style="margin-top:16px">
<h2>Check your understanding</h2>
<div class="q2">
<div>A satellite’s revisit gap is 24 hours and its training takes 1 hour. About how long does it need to take part in one round, counted from the moment the round starts?</div>
<button type="button" data-m="Not quite. The model first has to reach the satellite, which happens at its next contact, and the update can only leave at a contact after training.">About 1 hour</button>
<button type="button" data-m="Right. The model arrives between 0 and 24 hours after the start, and the update leaves one gap after that, so the total is between 24 and 48 hours.">Between 24 and 48 hours</button>
<button type="button" data-m="Not quite. It depends on when its first contact falls after the round starts, so it can be anywhere from one gap to two gaps.">Always exactly 24 hours</button>
<p class="fb" role="status" style="min-height:44px;margin:10px 0 0;font-size:14px"></p>
</div>
<div class="q2" style="margin-top:14px">
<div>A server closes every round 12 hours after it starts. A satellite has a 24-hour gap. What happens to it?</div>
<button type="button" data-m="Not quite. One contact could receive the model, but the update cannot leave until the next one, a full gap later. Two contacts never fit inside 12 hours.">It joins every second round</button>
<button type="button" data-m="Right. Receiving takes one contact and returning takes the next, at least a gap later, so its update always arrives after the 12-hour round has closed. It is left out of every round.">It is left out of every round</button>
<button type="button" data-m="Not quite. A contact inside the round is enough to receive the model, but not to return the update, which needs a second one.">It joins whenever one contact falls inside the round</button>
<p class="fb" role="status" style="min-height:44px;margin:10px 0 0;font-size:14px"></p>
</div>
<div class="q2" style="margin-top:14px">
<div>In section 3, when did leaving the rarely seen satellites out of the rounds cost accuracy?</div>
<button type="button" data-m="Not quite. With the switch off, every rule ended near the same accuracy, because every satellite held the same kind of data.">Always</button>
<button type="button" data-m="Right. When class D lived only on those satellites, the model never saw it. When all satellites held a mix, the others taught the same thing and little was lost.">Only when they held data the others did not</button>
<button type="button" data-m="Not quite. Round length changes how quickly accuracy arrives, not whether a missing class can be learned.">Only when rounds were long</button>
<p class="fb" role="status" style="min-height:44px;margin:10px 0 0;font-size:14px"></p>
</div>
</section>
<p class="key" style="margin-top:16px">Next in the series: Module 5, staleness and scheduling, where updates that arrive late are still used.</p>
</main>

<script>
function rng(a){return function(){a|=0;a=a+0x6D2B79F5|0;var t=Math.imul(a^a>>>15,1|a);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296}}
function gauss(r){return Math.sqrt(-2*Math.log(1-r()))*Math.cos(6.2832*r())}
function logits(w,q){var z=[],m=-1e9,c;for(c=0;c<C;c++){var v=w[c*3]*q.x+w[c*3+1]*q.y+w[c*3+2];z.push(v);if(v>m)m=v}var s=0;for(c=0;c<C;c++){z[c]=Math.exp(z[c]-m);s+=z[c]}for(c=0;c<C;c++)z[c]/=s;return z}
function acc(w,d){var a=0;d.forEach(function(q){var p=logits(w,q),b=0;for(var c=1;c<C;c++)if(p[c]>p[b])b=c;if(b==q.c)a++});return a/d.length}
function classAcc(w,d){var a=[0,0,0,0],n=[0,0,0,0];d.forEach(function(q){var p=logits(w,q),b=0;for(var c=1;c<C;c++)if(p[c]>p[b])b=c;n[q.c]++;if(b==q.c)a[q.c]++});return a.map(function(v,i){return n[i]?v/n[i]:null})}
function train(w0,d,E,lr,mu,g){var w=w0.slice();for(var e=0;e<E;e++){var gr=new Array(C*3).fill(0);d.forEach(function(q){var p=logits(w,q);for(var c=0;c<C;c++){var r=p[c]-(q.c==c?1:0);gr[c*3]+=r*q.x;gr[c*3+1]+=r*q.y;gr[c*3+2]+=r}});for(var k=0;k<C*3;k++){var gg=gr[k]/d.length;if(mu)gg+=mu*(w[k]-g[k]);w[k]-=lr*gg}}return w}
var C=4,K=12,CEN=[[-1.5,-1.5],[1.5,-1.5],[-1.5,1.5],[1.5,1.5]],SD=1.0,NE=20,LR=.5,GMED=6,GFREQ=2;
function pt(c,r){return{x:CEN[c][0]+gauss(r)*SD,y:CEN[c][1]+gauss(r)*SD,c:c}}
function grp(k){return k<6?0:(k<9?1:2)}
function satClass(k){return k<6?k%2:(k<9?2:3)}
function makeData(tied){var r=rng(31),cl=[],k,i;
 for(k=0;k<K;k++){var d=[];for(i=0;i<50;i++){var c=tied?satClass(k):Math.min(3,Math.floor(r()*4));d.push(pt(c,r))}cl.push(d)}
 var rt=rng(777),test=[];for(i=0;i<1000;i++)test.push(pt(i%C,rt));return{cl:cl,test:test}}
function makeContacts(grare,cs){var r=rng(cs),base=[GFREQ,GMED,grare],g=[],o=[],k;
 for(k=0;k<K;k++){var gk=base[grp(k)]*(0.8+0.4*r()),ok=r()*gk;g.push(gk);o.push(ok)}return{g:g,o:o}}
function firstAt(g,o,x){return x<=o?o:o+Math.ceil((x-o)/g)*g}
// pol: 'all' | 'dl' | 'first'
function roundPlan(pol,c,t0,D,nf,tau){var recv=[],ret=[],k;
 for(k=0;k<K;k++){recv.push(firstAt(c.g[k],c.o[k],t0));ret.push(firstAt(c.g[k],c.o[k],recv[k]+tau))}
 var P=[],end;
 if(pol=='all'){end=Math.max.apply(null,ret);for(k=0;k<K;k++)P.push(k)}
 else if(pol=='dl'){end=t0+D;for(k=0;k<K;k++)if(ret[k]<=end)P.push(k)}
 else{var ord=[];for(k=0;k<K;k++)ord.push(k);ord.sort(function(a,b){return ret[a]-ret[b]||a-b});P=ord.slice(0,nf);end=ret[ord[nf-1]]}
 return{recv:recv,ret:ret,P:P,end:end}}
function runPolicy(pol,o){var d=makeData(o.tied),c=makeContacts(o.grare,o.cs),W=new Array(C*3).fill(0),t0=0,pts=[[0,acc(W,d.test)]],parts=[],lens=[],guard=0;
 for(;;){var p=roundPlan(pol,c,t0,o.D,o.nf,o.tau);if(p.end>o.H||++guard>5000)break;
  if(p.P.length){var n=0,j;p.P.forEach(function(k){n+=d.cl[k].length});var ng=new Array(C*3).fill(0);
   p.P.forEach(function(k){var w=train(W,d.cl[k],NE,LR,0,W),f=d.cl[k].length/n;for(j=0;j<C*3;j++)ng[j]+=f*w[j]});W=ng}
  parts.push(p.P);lens.push(p.end-t0);pts.push([p.end,acc(W,d.test)]);t0=p.end}
 return{pts:pts,parts:parts,lens:lens,W:W,rounds:parts.length,test:d.test}}

(function(){
var $=function(i){return document.getElementById(i)};
function css(n){return getComputedStyle(document.documentElement).getPropertyValue(n).trim()}
var NAMES=['A','B','C','D'],GN=['Often','Sometimes','Rarely'];
var S={pol:'all',tied:true,grare:24,tau:1,D:12,nf:9,days:14,cs:21};
var POLS=['all','dl','first'],PN={all:'Wait for all',dl:'Deadline D',first:'First n'},PC={all:'--acc',dl:'--c0',first:'--c3'};
function cols(){return [css('--c0'),css('--c1'),css('--c2'),css('--c3')]}
function pct(v){return (v*100).toFixed(0)+'%'}
function fmtK(k,v){return k=='grare'||k=='D'?v+' h':k=='tau'?v.toFixed(1)+' h':k=='nf'?v:v+' d'}
function sync(){Array.prototype.forEach.call(document.querySelectorAll('input[data-k]'),function(el){var k=el.getAttribute('data-k');el.value=S[k];el.nextElementSibling.textContent=fmtK(k,S[k])})}
function T(x,y,s,o){o=o||{};return '<text x="'+x+'" y="'+y+'" font-size="'+(o.s||17)+'" fill="'+(o.c||css('--mute'))+'" text-anchor="'+(o.a||'start')+'"'+(o.b?' font-weight="700"':'')+(o.h?' stroke="'+css('--surf')+'" stroke-width="5" stroke-linejoin="round" paint-order="stroke"':'')+'>'+s+'</text>'}
function drawTL(){
 var c=makeContacts(S.grare,S.cs),p=roundPlan(S.pol,c,0,S.D,S.nf,S.tau),xm=Math.max(48,Math.ceil((p.end+6)/12)*12);
 var W=560,L=62,R=12,rh=24,hh=24,top=6,x=function(t){return L+t/xm*(W-L-R)},h='',lab='',k,t,cl=cols(),y=top,ys=[];
 var gcol=[css('--c1'),css('--c3'),css('--c0')],gtxt=['Often (gap near 2 h)','Sometimes (gap near 6 h)','Rarely (gap near '+S.grare+' h)'];
 for(k=0;k<K;k++){
  if(k==0||grp(k)!=grp(k-1)){lab+=T(0,y+17,gtxt[grp(k)],{b:1,c:css('--ink'),h:1});y+=hh}
  ys.push(y);y+=rh}
 var axisY=y+4;
 for(t=0;t<=xm;t+=(xm>96?24:12))h+='<line x1="'+x(t)+'" x2="'+x(t)+'" y1="'+top+'" y2="'+axisY+'" stroke="'+css('--line')+'"/>'+T(x(t),axisY+22,t+' h',{a:t==0?'start':(t+(xm>96?24:12)>xm?'end':'middle')});
 for(k=0;k<K;k++){var yy=ys[k]+rh/2-1;
  h+=T(L-6,yy+6,'S'+(k+1)+(S.tied?' '+NAMES[satClass(k)]:''),{a:'end',s:15});
  h+='<line x1="'+L+'" x2="'+(W-R)+'" y1="'+yy+'" y2="'+yy+'" stroke="'+css('--line')+'" stroke-dasharray="2 4"/>';
  for(t=c.o[k];t<=xm;t+=c.g[k])h+='<circle cx="'+x(t)+'" cy="'+yy+'" r="2.8" fill="'+css('--mute')+'" opacity=".75"/>';
  h+='<circle cx="'+x(p.recv[k])+'" cy="'+yy+'" r="6.5" fill="'+css('--c4')+'" stroke="'+css('--surf')+'" stroke-width="1.5"/>';
  var inc=p.P.indexOf(k)>=0;
  if(p.ret[k]<=xm){h+=inc?'<circle cx="'+x(p.ret[k])+'" cy="'+yy+'" r="6.5" fill="'+css('--c1')+'" stroke="'+css('--surf')+'" stroke-width="1.5"/>':'<circle cx="'+x(p.ret[k])+'" cy="'+yy+'" r="6" fill="'+css('--surf')+'" stroke="'+css('--c0')+'" stroke-width="2.5"/>'}
  else h+=T(W-R,yy+6,'›',{a:'end',c:css('--c0'),s:20,b:1})}
 h+='<line x1="'+x(p.end)+'" x2="'+x(p.end)+'" y1="'+top+'" y2="'+axisY+'" stroke="'+css('--c0')+'" stroke-width="2" stroke-dasharray="6 4"/>';
 h+=lab;
 $('tl').setAttribute('viewBox','0 0 560 '+(axisY+34));
 $('tl').innerHTML=h;
 $('tll').innerHTML='<span><i style="background:var(--c4)"></i>model arrives</span><span><i style="background:var(--c1)"></i>update returns in time</span><span><i style="background:transparent;border:2px solid var(--c0);height:8px;width:12px;border-radius:50%"></i>update too late, left out</span><span><i style="background:var(--mute)"></i>other contacts</span><span><i style="background:var(--c0)"></i>round ends (dashed)</span>';
 $('inc').textContent=p.P.length;$('rl').textContent=p.end.toFixed(1)+' h';
 var out=[];for(k=0;k<K;k++)if(p.P.indexOf(k)<0)out.push('S'+(k+1));
 $('left').textContent=out.length?'Left out: '+out.join(', ')+'. Their updates would arrive at or after hour '+p.end.toFixed(1)+'.':'No satellite is left out.';
 [['pa','all'],['pd','dl'],['pf','first']].forEach(function(b){$(b[0]).className=S.pol==b[1]?'p':''})
}
function stepPath(pts,Hh,sx,sy){var d='M'+sx(0).toFixed(1)+' '+sy(pts[0][1]).toFixed(1),i;
 for(i=1;i<pts.length;i++){d+='L'+sx(pts[i][0]).toFixed(1)+' '+sy(pts[i-1][1]).toFixed(1)+'L'+sx(pts[i][0]).toFixed(1)+' '+sy(pts[i][1]).toFixed(1)}
 d+='L'+sx(Hh).toFixed(1)+' '+sy(pts[pts.length-1][1]).toFixed(1);return d}
var RES;
function compute(){
 var o={tied:S.tied,grare:S.grare,tau:S.tau,D:S.D,nf:S.nf,H:S.days*24,cs:S.cs};RES={};
 POLS.forEach(function(p){RES[p]=runPolicy(p,o)});
}
function hoursTo(res,thr){for(var i=0;i<res.pts.length;i++)if(res.pts[i][1]>=thr)return res.pts[i][0];return null}
function share(res){var g=[0,0,0],n=[0,0,0],k;for(k=0;k<K;k++){var cnt=0;res.parts.forEach(function(P){if(P.indexOf(k)>=0)cnt++});g[grp(k)]+=res.rounds?cnt/res.rounds:0;n[grp(k)]++}return g.map(function(v,i){return v/n[i]})}
function drawCurves(){
 var W=380,H=230,L=36,R=8,Tp=10,Bt=34,Hh=S.days*24,lo=.2,hi=1,sx=function(t){return L+t/Hh*(W-L-R)},sy=function(v){return Tp+(hi-v)/(hi-lo)*(H-Tp-Bt)},h='',t;
 [.25,.5,.75,1].forEach(function(v){h+='<line x1="'+L+'" x2="'+(W-R)+'" y1="'+sy(v)+'" y2="'+sy(v)+'" stroke="'+css('--line')+'"/><text x="'+(L-4)+'" y="'+(sy(v)+4)+'" font-size="11" text-anchor="end" fill="'+css('--mute')+'">'+(v*100)+'%</text>'});
 h+='<line x1="'+L+'" x2="'+(W-R)+'" y1="'+sy(.871)+'" y2="'+sy(.871)+'" stroke="'+css('--mute')+'" stroke-dasharray="2 4"/><text x="'+(W-R)+'" y="'+(sy(.871)-3)+'" font-size="10" text-anchor="end" fill="'+css('--mute')+'">best possible ≈ 87%</text>';
 var step=Hh<=72?12:Hh<=168?24:Hh<=336?48:72;
 for(t=0;t<=Hh;t+=step)h+='<text x="'+sx(t)+'" y="'+(H-16)+'" font-size="11" text-anchor="'+(t==0?'start':(t+step>Hh?'end':'middle'))+'" fill="'+css('--mute')+'">'+t+'</text>';
 h+='<text x="'+((L+W)/2)+'" y="'+(H-3)+'" font-size="11" text-anchor="middle" fill="'+css('--mute')+'">hours</text>';
 POLS.slice().reverse().forEach(function(p){h+='<path d="'+stepPath(RES[p].pts,Hh,sx,sy)+'" fill="none" stroke="'+css(PC[p])+'" stroke-width="2.2" stroke-linejoin="round"/>'});
 $('cv').innerHTML=h;
}
function drawTable(){
 var info={},rows;POLS.forEach(function(p){var r=RES[p],t=hoursTo(r,.8),fa=r.pts[r.pts.length-1][1],ml=r.rounds?r.lens.reduce(function(a,b){return a+b},0)/r.rounds:null;
  info[p]={rounds:r.rounds,ml:ml==null?'–':ml.toFixed(1)+' h',fa:(fa*100).toFixed(1)+'%',t:t==null?'not reached':(t==0?'0 h':t.toFixed(0)+' h'),s:share(r)}});
 rows='<tr><th></th>'+POLS.map(function(p){return '<th><span class="dot" style="background:'+css(PC[p])+'"></span>'+PN[p]+'</th>'}).join('')+'</tr>';
 function row(lab,f){return '<tr><td>'+lab+'</td>'+POLS.map(function(p){return '<td>'+f(info[p])+'</td>'}).join('')+'</tr>'}
 rows+=row('Rounds finished',function(x){return x.rounds})+row('Mean round length',function(x){return x.ml})+row('Final accuracy',function(x){return x.fa})+row('Hours to reach 80%',function(x){return x.t})
  +row('Rounds joined: often seen',function(x){return pct(x.s[0])})+row('Rounds joined: sometimes seen',function(x){return pct(x.s[1])})+row('Rounds joined: rarely seen',function(x){return pct(x.s[2])});
 $('tb').innerHTML=rows;
}
function drawClass(){
 var h='',cl=cols(),j,pi;
 for(j=0;j<4;j++){var x0=40+j*84;
  POLS.forEach(function(p,pi){var a=classAcc(RES[p].W,RES[p].test)[j],x=x0+pi*24;
   h+='<rect x="'+x+'" y="'+(90-a*80)+'" width="20" height="'+(a*80)+'" fill="'+css(PC[p])+'"/><text x="'+(x+10)+'" y="'+(90-a*80-3)+'" font-size="9" text-anchor="middle" fill="'+css('--mute')+'">'+pct(a)+'</text>'});
  h+='<text x="'+(x0+35)+'" y="108" font-size="11" text-anchor="middle" fill="'+css('--mute')+'">Class '+NAMES[j]+'</text>'}
 h+='<line x1="30" x2="376" y1="90" y2="90" stroke="'+css('--line')+'"/>';
 $('pc').innerHTML=h;
}
function sentence(){
 var f={},m=0;POLS.forEach(function(p){f[p]=RES[p].pts[RES[p].pts.length-1][1];if(f[p]>m)m=f[p]});
 var days=S.days,s='After '+days+' days: waiting for all finished '+RES.all.rounds+' round'+(RES.all.rounds==1?'':'s')+' and ended at '+(f.all*100).toFixed(0)+'%; the deadline rule finished '+RES.dl.rounds+' and ended at '+(f.dl*100).toFixed(0)+'%; first n finished '+RES.first.rounds+' and ended at '+(f.first*100).toFixed(0)+'%. ';
 var rare=[share(RES.dl)[2],share(RES.first)[2]];
 if(S.tied){var low=POLS.filter(function(p){return f[p]<m-.03});
  s+=low.length?(low.map(function(p){return PN[p]}).join(' and ')+' ended at least 3 points below the best. Check the “rarely seen” row of the table: the rarely seen satellites joined '+pct(rare[0])+' of the deadline rule’s rounds and '+pct(rare[1])+' of first n’s, and class D lives only on them.'):'Every rule ended within 3 points of the best here, so all of them heard from the rarely seen satellites often enough.'}
 else{s+=(m-Math.min(f.all,f.dl,f.first)<.03)?'The data is the same kind everywhere, so leaving satellites out costs little accuracy and the early-closing rules mainly get there sooner.':'Even with the same kind of data everywhere, a rule ended at least 3 points lower; with few satellites included the average is noisier.'}
 $('v3').textContent=s;
}
function cur(){$('cur').textContent='Contact settings from section 2: rarely seen gap '+S.grare+' h, training time τ = '+S.tau.toFixed(1)+' h, contact pattern '+(S.cs-20)+'. Change them above.'}
function full(){sync();drawTL();compute();cur();drawCurves();drawTable();drawClass();sentence()}
Array.prototype.forEach.call(document.querySelectorAll('input[data-k]'),function(el){el.oninput=function(){S[el.getAttribute('data-k')]=+el.value;full()}});
$('tied').onchange=function(){S.tied=this.checked;full()};
[['pa','all'],['pd','dl'],['pf','first']].forEach(function(b){$(b[0]).onclick=function(){S.pol=b[1];drawTL()}});
$('ncp').onclick=function(){S.cs++;full()};
Array.prototype.forEach.call(document.querySelectorAll('.q2'),function(q){var fb=q.querySelector('.fb');Array.prototype.forEach.call(q.querySelectorAll('button'),function(b){b.onclick=function(){fb.textContent=b.getAttribute('data-m')}})});
full();
if(window.matchMedia)matchMedia('(prefers-color-scheme:dark)').addEventListener&&matchMedia('(prefers-color-scheme:dark)').addEventListener('change',full);
})();
</script>
</body>
</html>
'''
