"""Interactive learning modules 1-4, shown on the Learn page.

render_learn_hub() is the whole Learn page: a switch between these interactive
modules and the existing concept lessons in interface/learn.py. app.py only needs
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

from interface.learn import render_learn as render_concept_lessons
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
      if (f && h > 0 && Math.abs(f.getBoundingClientRect().height - h) > 2) f.style.height = h + "px";
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


LEARN_VIEWS = ["Interactive modules", "Concept lessons"]


def render_learn_hub() -> None:
    """The Learn page: the interactive modules next to the existing concept lessons."""
    view = st.radio(
        "Learn view", LEARN_VIEWS, horizontal=True, key="learn_view", label_visibility="collapsed"
    )
    if view == LEARN_VIEWS[0]:
        render_modules()
    else:
        render_concept_lessons()
