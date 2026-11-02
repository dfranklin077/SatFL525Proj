"""Interactive learning modules 1-4, shown on the Learn page.

render_learn_hub() is the whole Learn page: a switch between these interactive
modules and a tab of additional resources. app.py only needs
this one import, which replaces `from interface.learn import render_learn`:
    from interface.fl_modules import render_learn_hub as render_learn_page
render_modules() is the module picker on its own.

Each lesson is one self-contained HTML document, kept in module1.py to module4.py
next to this file, and shown with streamlit.components.v1.html, so it needs no extra
package and no data file.

Two small things are added to every lesson when it is shown:
  * the lesson is forced to its light theme, because this app is light-themed
    (change THEME to None to follow the visitor's device setting instead);
  * a script makes the frame as tall as the lesson, so the page scrolls once,
    and makes the lesson's "#section" links scroll the page.
"""
from __future__ import annotations

import streamlit as st
import streamlit.components.v1 as components

from interface import module1, module2, module3, module4

MODULES = {
    "Module 1 · FL basics": module1.HTML,
    "Module 2 · Satellite application": module2.HTML,
    "Module 3 · IID vs non-IID": module3.HTML,
    "Module 4 · Intermittent contact": module4.HTML,
}

THEME = "light"  # "light", "dark", or None to follow the visitor's device setting

_FRAME_SCRIPT = """
<script>
(function () {
  function fit() {
    try {
      var b = document.body, cs = getComputedStyle(b);
      var h = Math.ceil(b.getBoundingClientRect().height + parseFloat(cs.marginTop) + parseFloat(cs.marginBottom));
      var f = window.frameElement;
      if (!f || h <= 0) return;
      if (Math.abs(f.getBoundingClientRect().height - h) > 2) f.style.height = h + "px";
      // Streamlit keeps the frame's wrapper at the height we asked for; make it follow, or the
      // page footer is drawn on top of the lesson.
      var c = f.parentElement;
      if (c && Math.abs(c.getBoundingClientRect().height - h) > 2) c.style.height = h + "px";
    } catch (e) {}
  }
  window.addEventListener("load", fit);
  window.addEventListener("resize", fit);
  if (window.ResizeObserver) new ResizeObserver(fit).observe(document.body);
  setTimeout(fit, 300);
  document.addEventListener("click", function (e) {
    var a = e.target.closest ? e.target.closest('a[href^="#"]') : null;
    if (!a) return;
    var t = document.getElementById(a.getAttribute("href").slice(1));
    if (!t) return;
    e.preventDefault();
    t.scrollIntoView({ behavior: "smooth", block: "start" });
  });
})();
</script>
<style>section[id]{scroll-margin-top:72px}</style>
"""


def _frame_html(html: str) -> str:
    if THEME:
        html = html.replace(
            "<head>",
            "<head><script>document.documentElement.setAttribute('data-theme','%s');</script>" % THEME,
            1,
        )
    head, sep, tail = html.rpartition("</body>")
    return head + _FRAME_SCRIPT + sep + tail


def render_modules() -> None:
    choice = st.radio(
        "Module", list(MODULES), horizontal=True, key="learn_module", label_visibility="collapsed"
    )
    components.html(_frame_html(MODULES[choice]), height=1400, scrolling=True)


# Background reading, listed under the module it goes with. To add a source, add one line to a list
# below: _src(title, where it is published, link, one sentence on what it covers).
def _src(title: str, where: str, url: str, about: str) -> dict:
    return {"title": title, "where": where, "url": url, "about": about}


IBM_BLOG = _src(
    "What is federated learning?", "IBM Research blog",
    "https://research.ibm.com/blog/what-is-federated-learning",
    "A plain-language overview: why training moves to where the data is, how that fits privacy rules, "
    "and how it applies to data streaming from sensors, including those on satellites.",
)
DLAI_COURSE = _src(
    "Intro to Federated Learning (short course)", "DeepLearning.AI",
    "https://learn.deeplearning.ai/courses/intro-to-federated-learning",
    "A beginner course on why federated learning is used, how a training round works, which settings can be "
    "tuned (such as how clients are chosen each round), and how privacy techniques such as differential privacy fit in. "
    "Its exercises use the Flower framework.",
)
KAIROUZ = _src(
    "Advances and Open Problems in Federated Learning", "arXiv survey (1912.04977)",
    "https://arxiv.org/abs/1912.04977",
    "A long survey of the field: how federated learning works, and open problems such as non-IID data, "
    "communication cost and privacy.",
)
MEDIUM_NONIID = _src(
    "Federated Learning and the Non-IID Challenge", "Medium",
    "https://medium.com/@manansrivastava01/federated-learning-and-the-non-iid-challenge-850a27d5ac4d",
    "A short article on how clients holding different kinds of data affects how well and how fast the shared "
    "model converges, and what can be done about it.",
)
SAT_FL = _src(
    "Federated Learning in Satellite Constellations", "arXiv (2206.00307)",
    "https://arxiv.org/abs/2206.00307",
    "An article on the new context satellite constellations bring to federated learning, where connectivity "
    "is limited and intermittent.",
)

MCMAHAN = _src(
    "Communication-Efficient Learning of Deep Networks from Decentralized Data", "arXiv (1602.05629)",
    "https://arxiv.org/abs/1602.05629",
    "The paper that introduced federated averaging (FedAvg), the method Modules 1 to 4 use, and showed it "
    "needs far fewer communication rounds than sending every update to the server.",
)
FEDPROX = _src(
    "Federated Optimization in Heterogeneous Networks", "arXiv (1812.06127)",
    "https://arxiv.org/abs/1812.06127",
    "The paper that introduced FedProx, the proximal term behind the strength slider in Module 3, for clients "
    "whose data and computing power differ.",
)
ZHAO_NONIID = _src(
    "Federated Learning with Non-IID Data", "arXiv (1806.00582)",
    "https://arxiv.org/abs/1806.00582",
    "An early study showing that accuracy drops when clients hold different kinds of data, and a fix that "
    "shares a small dataset among the clients.",
)
SHOKRI = _src(
    "Membership Inference Attacks Against Machine Learning Models", "arXiv (1610.05820)",
    "https://arxiv.org/abs/1610.05820",
    "The study of attacks that tell whether a particular record was in a model's training data, one of the "
    "privacy risks in Module 1.",
)
MELIS = _src(
    "Exploiting Unintended Feature Leakage in Collaborative Learning", "arXiv (1805.04049)",
    "https://arxiv.org/abs/1805.04049",
    "Shows that the updates shared in collaborative and federated learning can reveal facts about other "
    "participants' data, such as properties the model was never trained to predict.",
)
ZHU_DLG = _src(
    "Deep Leakage from Gradients", "arXiv (1906.08935)",
    "https://arxiv.org/abs/1906.08935",
    "Shows that training images and text can be rebuilt from the gradients that clients share.",
)
RAZMI = _src(
    "On-board Federated Learning for Satellite Clusters with Inter-Satellite Links", "arXiv (2307.08346)",
    "https://arxiv.org/abs/2307.08346",
    "A follow-up on satellites in one orbit that link to their neighbours, so that updates reach the ground "
    "faster even though each satellite sees the station only briefly.",
)

SOURCES_BY_MODULE = {
    "Module 1 · FL basics": [IBM_BLOG, DLAI_COURSE, KAIROUZ, MCMAHAN, SHOKRI, MELIS, ZHU_DLG],
    "Module 2 · Satellite application": [SAT_FL, RAZMI],
    "Module 3 · IID vs non-IID": [MEDIUM_NONIID, KAIROUZ, ZHAO_NONIID, FEDPROX],
    "Module 4 · Intermittent contact": [SAT_FL, RAZMI, DLAI_COURSE],
}

# Reading that goes beyond Modules 1 to 4. Add the sources for the later modules here.
MORE_RESOURCES = [
    _src(
        "Age-Aware and Energy-Constrained Optimization for Routing and Computation Offloading in LEO Satellite Networks",
        "IEEE Transactions on Mobile Computing (may need a library login)",
        "https://doi.org/10.1109/TMC.2026.3709610",
        "A paper on routing data and offloading computation in low-Earth-orbit networks when energy is limited.",
    ),
    _src(
        "OSGS: A Framework for Online Scheduling of Satellite-Ground Collaborative Inference With Space Edge Computing",
        "IEEE Transactions on Services Computing (may need a library login)",
        "https://doi.org/10.1109/TSC.2026.3688483",
        "A paper on scheduling inference work between satellites and the ground using computing on the satellites.",
    ),
]


def _source_list(sources: list[dict]) -> None:
    for s in sources:
        st.markdown(f"- **[{s['title']}]({s['url']})**  \n  {s['where']}. {s['about']}")


def render_sources() -> None:
    """The 'Additional resources' tab: background reading for each module, then more resources."""
    st.subheader("Additional resources")
    st.caption("Background reading for each lesson. Each link opens the original page.")
    for name, sources in SOURCES_BY_MODULE.items():
        st.markdown(f"#### {name}")
        _source_list(sources)
    st.markdown("#### More resources")
    st.caption("Reading that goes beyond Modules 1 to 4.")
    if MORE_RESOURCES:
        _source_list(MORE_RESOURCES)
    else:
        st.write("More resources will be added here as new modules are released.")


def _view_box(key: str):
    """A container with its own identity (the key argument needs Streamlit 1.43 or newer)."""
    try:
        return st.container(key=key)
    except TypeError:
        return st.container()


LEARN_VIEWS = ["Interactive modules", "Additional resources"]


def render_learn_hub() -> None:
    """The Learn page: the interactive modules, and a tab of additional resources."""
    view = st.radio(
        "Learn view", LEARN_VIEWS, horizontal=True, key="learn_view", label_visibility="collapsed"
    )
    # Each view sits in its own keyed container. Without that, Streamlit reuses the lesson
    # frame's wrapper for the sources list and the wrapper keeps the lesson's tall height.
    if view == LEARN_VIEWS[0]:
        with _view_box("learn_view_modules"):
            render_modules()
    else:
        with _view_box("learn_view_sources"):
            render_sources()
