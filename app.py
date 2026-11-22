"""נציג AI: מצגת חלק ד. גרפים (Plotly) ודיאגרמות זרימה (Graphviz). RTL, עיצוב בהיר."""
import datetime as dt

import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="נציג AI", page_icon="■", layout="wide", initial_sidebar_state="collapsed")

NAVY = "#0B1B3A"
TEAL = "#0F9D8A"
AMBER = "#F5A524"
RED = "#E5484D"
GREEN = "#2EB67D"
GREY = "#64748B"
LIGHT = "#F2F6FA"
LINE = "#D7E0EA"
FONT = "Arial, Helvetica, sans-serif"

CSS = f"""
<style>
html, body, [class*="css"] {{ font-family: {FONT}; }}
.stApp {{ background: #FFFFFF; color: {NAVY}; direction: rtl; }}
header, footer, [data-testid="stSidebar"] {{ display: none !important; }}
.stApp::before {{ content: ""; position: fixed; top: 0; left: 0; right: 0; height: 8px; background: linear-gradient(90deg, {TEAL}, {AMBER}, {RED}); }}
.block-container {{ max-width: 1200px; padding-top: 2.4rem; padding-bottom: 2rem; }}
.badge {{ display: inline-block; background: {NAVY}; color: #fff; border-radius: 999px; padding: 4px 14px; font-size: 13px; font-weight: 700; }}
.title {{ font-size: 40px; font-weight: 800; line-height: 1.2; margin: 14px 0 22px; color: {NAVY}; }}
.sub {{ font-size: 18px; color: {GREY}; margin: -8px 0 18px; line-height: 1.6; }}
.card {{ background: {LIGHT}; border-radius: 16px; padding: 20px 22px; border-right: 6px solid {TEAL}; height: 100%; }}
.card h4 {{ margin: 0 0 6px; font-size: 19px; color: {NAVY}; }}
.card p {{ margin: 0; color: {GREY}; font-size: 16px; line-height: 1.55; }}
.kpi {{ font-size: 54px; font-weight: 800; color: {TEAL}; line-height: 1; }}
.legend {{ display: flex; gap: 18px; font-size: 14px; color: {GREY}; margin-top: 4px; }}
.dot {{ display: inline-block; width: 12px; height: 12px; border-radius: 50%; margin-left: 6px; vertical-align: middle; }}
.quote {{ background: #fff; border: 1px solid {LINE}; border-radius: 14px; padding: 18px 20px; box-shadow: 0 4px 14px rgba(11,27,58,.06); }}
.cite {{ display: inline-block; background: {TEAL}22; color: {TEAL}; border-radius: 8px; padding: 3px 10px; font-size: 13px; font-weight: 700; margin-top: 10px; }}
[data-testid="stPlotlyChart"], [data-testid="stGraphVizChart"] {{ direction: ltr; }}
.stButton > button {{ background: #fff; color: {NAVY}; border: 1px solid {LINE}; border-radius: 12px; font-size: 17px; font-weight: 700; min-height: 48px; }}
.stButton > button:hover {{ border-color: {TEAL}; color: {TEAL}; }}
.stButton > button:disabled {{ color: #A9B6C6; }}
.stButton > button[kind="primary"] {{ background: {TEAL}; color: #fff; border: none; }}
.stButton > button[kind="primary"]:hover {{ background: #0c8a7a; color: #fff; }}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


def head(num, title, sub=None):
    st.markdown(f'<span class="badge">{num}</span><div class="title">{title}</div>', unsafe_allow_html=True)
    if sub:
        st.markdown(f'<div class="sub">{sub}</div>', unsafe_allow_html=True)


def card(title, body, color=TEAL):
    return f'<div class="card" style="border-right-color:{color}"><h4>{title}</h4><p>{body}</p></div>'


def base_layout(fig, height=380):
    fig.update_layout(
        font=dict(family=FONT, size=15, color=NAVY),
        paper_bgcolor="white", plot_bgcolor="white",
        margin=dict(l=20, r=20, t=40, b=20), height=height,
    )
    return fig


def flow(dot_src, height=None):
    st.graphviz_chart(dot_src)


# ---------- שקף 0: כריכה ----------
def slide_cover():
    st.markdown('<span class="badge">מטלת Data & AI PM</span>', unsafe_allow_html=True)
    st.markdown('<div class="title" style="font-size:80px;margin-top:30px">נציג AI</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="sub" style="font-size:24px;color:{NAVY}">מהחלטת ארכיטקטורה ועד ניהול משבר בשטח</div>', unsafe_allow_html=True)
    flow("""
    digraph G {
      rankdir=RL; bgcolor="transparent";
      node [shape=box, style="rounded,filled", fontname="Arial", fontsize=15, color="none", fontcolor="white", margin="0.25,0.15"];
      edge [color="#64748B", penwidth=1.6, arrowsize=0.8];
      A [label="א · החלטה\\nשלוש דרכים", fillcolor="#0B1B3A"];
      B [label="ב · מוצר\\nPRD", fillcolor="#0F9D8A"];
      C [label="ג · משבר\\nסדר עדיפויות", fillcolor="#F5A524"];
      D [label="ד · ניהול\\nשלוש החלטות", fillcolor="#2EB67D"];
      A -> B -> C -> D;
    }
    """)


# ---------- שקף 1: הפרויקט (זרימה) ----------
def slide_project():
    head("1", "הסוכן עונה לנציג תוך שניות, ורק מתוך מסמך מאושר",
         "כך נראית שאלה אחת מתחילתה ועד הסוף.")
    flow("""
    digraph G {
      rankdir=RL; bgcolor="transparent"; nodesep=0.5; ranksep=0.6;
      node [shape=box, style="rounded,filled", fontname="Arial", fontsize=14, color="#D7E0EA", fillcolor="#F2F6FA", fontcolor="#0B1B3A", margin="0.25,0.12"];
      edge [color="#64748B", arrowsize=0.8, fontname="Arial", fontsize=12, fontcolor="#64748B"];
      Q [label="נציג שואל:\\nמה הריבית לדיור?", fillcolor="#0B1B3A", fontcolor="white"];
      D [label="מסמך מאושר\\nקיים?", shape=diamond, style="filled", fillcolor="#FFFFFF", color="#0F9D8A", fontsize=13, margin="0.05"];
      Y [label="תשובה + ציטוט\\nתוך 3 שניות", fillcolor="#2EB67D", fontcolor="white", color="none"];
      N [label="אין מקור\\nפנה למומחה", fillcolor="#E5484D", fontcolor="white", color="none"];
      P [label="תשובה שגויה?\\nP0 = עצירה", shape=box, fillcolor="#F5A524", fontcolor="#0B1B3A", color="none"];
      Q -> D;
      D -> Y [label="כן"];
      D -> N [label="לא"];
      Y -> P [label="בדיקה"];
    }
    """)
    c1, c2, c3 = st.columns(3)
    c1.markdown(card("מה בנינו", "סוכן שעונה על מוצרים, נהלים ורגולציה.", TEAL), unsafe_allow_html=True)
    c2.markdown(card("למי", "ותיקים שמכירים הכול, וחדשים שעדיין לומדים.", AMBER), unsafe_allow_html=True)
    c3.markdown(card("הצלחה", "זמן חיפוש קצר, 90% תשובות נכונות, ואפס P0.", GREEN), unsafe_allow_html=True)


# ---------- שקף 2: שלוש דרכים (מפת חום + טווח זמן) ----------
def slide_tracks():
    head("2", "כלי הרכבה לא נותן מוח, הוא שכבה מעל אחת משתי הדרכים",
         "הצבעים: ירוק מתאים, צהוב בתנאי, אדום בעייתי.")
    criteria = ["אבטחה", "מיקום נתונים", "רגולציה", "עברית ודיוק", "עלות", "זמן עד פיילוט", "תחזוקה"]
    tracks = ["ענן מנוהל", "הרצה בבית", "כלי הרכבה"]
    z = [[2, 2, 2, 2, 2, 2, 3],
         [2, 3, 2, 2, 2, 1, 1],
         [2, 2, 2, 2, 2, 2, 2]]
    text = [["בתנאי", "בתנאי", "בתנאי", "בתנאי", "בתנאי", "בתנאי", "מתאים"],
            ["בתנאי", "מתאים", "בתנאי", "בתנאי", "בתנאי", "בעייתי", "בעייתי"],
            ["בתנאי"] * 7]
    fig = go.Figure(go.Heatmap(
        z=z, x=criteria, y=tracks, text=text, texttemplate="%{text}",
        colorscale=[[0, RED], [0.5, AMBER], [1, GREEN]], zmin=1, zmax=3,
        showscale=False, xgap=3, ygap=3, textfont=dict(color="#0B1B3A", size=13),
    ))
    fig.update_yaxes(autorange="reversed", tickfont=dict(size=15))
    fig.update_xaxes(side="top", tickfont=dict(size=13))
    st.plotly_chart(base_layout(fig, 300), width="stretch")

    weeks_low = [8, 20, 12]
    weeks_high = [12, 26, 16]
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(
        y=tracks, x=[h - l for l, h in zip(weeks_low, weeks_high)], base=weeks_low, orientation="h",
        marker_color=[TEAL, AMBER, GREY], text=[f"{l}-{h} שבועות" for l, h in zip(weeks_low, weeks_high)],
        textposition="inside", insidetextanchor="middle", textfont=dict(color="white", size=14),
    ))
    fig2.update_yaxes(autorange="reversed")
    fig2.update_layout(title=dict(text="זמן עד פיילוט (לפי המטלה)", font=dict(size=16)), showlegend=False)
    st.plotly_chart(base_layout(fig2, 230), width="stretch")


# ---------- שקף 3: ההחלטה (זרימה עם תנאים) ----------
def slide_decision():
    head("3", "בחרתי היברידי, ושלושה תנאים מחליטים אם הוא עולה לאוויר",
         "המחיר: תלות בספק, ודיוק בעברית שעוד לא הוכח.")
    flow("""
    digraph G {
      rankdir=RL; bgcolor="transparent"; nodesep=0.4; ranksep=0.55;
      node [shape=box, style="rounded,filled", fontname="Arial", fontsize=14, color="none", fontcolor="#0B1B3A", fillcolor="#F2F6FA", margin="0.22,0.12"];
      edge [color="#64748B", arrowsize=0.8, fontname="Arial", fontsize=12];
      T [label="שלושה תנאים", fillcolor="#0B1B3A", fontcolor="white"];
      G1 [label="1 · אזור ישראלי"];
      G2 [label="2 · אישור: לא נשמרות תשובות"];
      G3 [label="3 · מבחן עברית 90%+"];
      OK [label="היברידי:\\nענן בישראל + שכבת הרכבה", fillcolor="#2EB67D", fontcolor="white"];
      NO [label="תוכנית ב':\\nמסמכים בלבד + מודל בבנק", fillcolor="#F5A524"];
      T -> G1; T -> G2; T -> G3;
      G1 -> OK [label="כולם עוברים"]; G2 -> OK; G3 -> OK;
      G1 -> NO [label="אחד נכשל", style=dashed];
      G2 -> NO [style=dashed]; G3 -> NO [style=dashed];
    }
    """)


# ---------- שקף 4: המוצר (שני נציגים + כרטיס תשובה) ----------
def slide_product():
    head("4", "הוותיק רוצה ציטוט, החדש רוצה לדעת מתי לא לסמוך",
         "אותה תשובה, שני נציגים, ואותו עיקרון: אין מקור, אין תשובה.")
    c1, c2 = st.columns([1, 1.3])
    with c1:
        st.markdown(card("הוותיק", "לא סומך על כלי שטעה פעם אחת. לכן כל תשובה עם קישור לסעיף.", TEAL), unsafe_allow_html=True)
        st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
        st.markdown(card("החדש", "מפחד לשאול. לכן ״אין מקור״ הוא תשובה לגיטימית, לא כישלון.", AMBER), unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="quote">
          <div style="color:{GREY};font-size:14px">הנציג שאל</div>
          <div style="font-size:18px;font-weight:700;margin:4px 0 14px">מה הריבית המקסימלית על הלוואה לדיור?</div>
          <div style="background:{LIGHT};border-radius:10px;padding:14px;font-size:16px;line-height:1.6">
            התשובה: לפי נוהל ההלוואות לדיור, הריבית המקסימלית היא כפי שמפורסם לתאריך התוקף.
            <br><span class="cite">ציטוט: נוהל הלוואות לדיור · סעיף 3.2 · גרסה 4</span>
          </div>
          <div style="color:{GREY};font-size:13px;margin-top:10px">זמן תשובה P95: עד 3 שניות</div>
        </div>
        """, unsafe_allow_html=True)


# ---------- שקף 5: הגבולות (זרימת החלטה) ----------
def slide_limits():
    head("5", "הסוכן עונה על מוצרים ונהלים, לא נוגע בחשבון ולא מייעץ",
         "כל שאלה עוברת את הבדיקה הזו לפני שמקבלת תשובה.")
    flow("""
    digraph G {
      rankdir=LR; bgcolor="transparent"; nodesep=0.35; ranksep=0.5;
      node [shape=box, style="rounded,filled", fontname="Arial", fontsize=14, color="none", fontcolor="#0B1B3A", fillcolor="#F2F6FA", margin="0.22,0.12"];
      edge [color="#64748B", arrowsize=0.8, fontname="Arial", fontsize=12];
      S [label="שאלה", fillcolor="#0B1B3A", fontcolor="white"];
      K [label="בתחום?", shape=diamond, fillcolor="#FFFFFF", color="#0F9D8A", margin="0.03"];
      INS [label="מוצרים · נהלים\\nהסברי רגולציה מאושרים", fillcolor="#2EB67D", fontcolor="white"];
      OUT [label="נתוני לקוח · פעולה בחשבון\\nייעוץ · התחייבות", fillcolor="#E5484D", fontcolor="white"];
      SRC [label="יש מסמך מאושר?", shape=diamond, fillcolor="#FFFFFF", color="#0F9D8A", margin="0.03"];
      ANS [label="תשובה + ציטוט", fillcolor="#2EB67D", fontcolor="white"];
      NO [label="״אין מקור מאושר,\\nפנה למומחה״", fillcolor="#F5A524"];
      S -> K;
      K -> INS [label="כן"];
      K -> OUT [label="לא"];
      INS -> SRC;
      SRC -> ANS [label="כן"];
      SRC -> NO [label="לא"];
      OUT -> NO [label="סירוב קבוע"];
    }
    """)


# ---------- שקף 6: המשבר (גרף דיוק + מפת חסמים) ----------
def slide_crisis():
    head("6", "שלושה חסמים. הראשון, הדיוק, קובע את כל השאר",
         "הדיוק הנוכחי נמוך מסף העצירה של 85%.")
    c1, c2 = st.columns(2)
    with c1:
        fig = go.Figure(go.Bar(
            x=[77], y=["דיוק נוכחי"], orientation="h", marker_color=RED,
            text=["77%"], textposition="inside", textfont=dict(color="white", size=18), width=0.5,
        ))
        fig.add_vline(x=85, line=dict(color=AMBER, width=3, dash="dash"),
                      annotation_text="סף עצירה 85%", annotation_position="top")
        fig.add_vline(x=90, line=dict(color=GREEN, width=3, dash="dot"),
                      annotation_text="יעד 90%", annotation_position="bottom")
        fig.update_xaxes(range=[0, 100], ticksuffix="%")
        st.plotly_chart(base_layout(fig, 260), width="stretch")
        st.markdown(f'<div class="sub" style="font-size:15px">23% שגיאות = 77% דיוק, במדגם של 200 שאלות.</div>', unsafe_allow_html=True)
    with c2:
        fig2 = go.Figure(go.Scatter(
            x=[2, 5, 3], y=[5, 4, 3], mode="markers+text",
            marker=dict(size=[46, 40, 34], color=[RED, AMBER, AMBER]),
            text=["1 · דיוק", "2 · Compliance", "3 · VP"], textposition="middle right",
            textfont=dict(size=14),
        ))
        fig2.update_xaxes(title="קל לתיקון ←  → קשה", range=[0.5, 6], showgrid=False, tickvals=[])
        fig2.update_yaxes(title="דחיפות", range=[2, 6], showgrid=False, tickvals=[])
        st.plotly_chart(base_layout(fig2, 260), width="stretch")


# ---------- שקף 7: התוכנית (Gantt) ----------
def slide_recovery():
    head("7", "לכל חסם: מה עושים, מי אחראי, ומתי", "שמונה שבועות, מיום האישור.")
    t0 = dt.date(2026, 11, 23)
    rows = [
        ("דיוק", "בחינת 3 מודלים על 200 שאלות", 0, 2, "R&D + Compliance"),
        ("דיוק", "החלטה: מודל או תוכנית ב'", 2, 3, "ועדה"),
        ("Compliance", "אישור כתוב לשלב א", 0, 1, "Compliance"),
        ("VP", "דשבורד שבועי (Quick Win)", 0, 3, "ניהול מוצר"),
        ("פיילוט", "הכנה ובדיקת עומס", 3, 6, "הנדסה"),
        ("פיילוט", "15 נציגים, מוקד אחד", 6, 8, "מנהל מוקד"),
    ]
    fig = go.Figure()
    colors = {"R&D + Compliance": TEAL, "ועדה": NAVY, "Compliance": GREEN, "ניהול מוצר": AMBER,
              "הנדסה": GREY, "מנהל מוקד": RED}
    for block, label, start, end, owner in rows:
        fig.add_trace(go.Bar(
            y=[label], x=[end - start], base=[start], orientation="h",
            marker_color=colors.get(owner, GREY), name=owner,
            text=[owner], textposition="inside", insidetextanchor="middle",
            textfont=dict(color="white", size=13), showlegend=False,
            hovertemplate=f"{label}<br>{owner}<extra></extra>",
        ))
    fig.update_yaxes(autorange="reversed", tickfont=dict(size=14))
    fig.update_xaxes(title="שבוע", tickmode="linear", dtick=1, range=[0, 8])
    st.plotly_chart(base_layout(fig, 360), width="stretch")


# ---------- שקף 8: הפיילוט (זרימה עם שערים) ----------
def slide_pilot():
    head("8", "15 נציגים, מוקד אחד, שישה שבועות, ורק אז מרחיבים",
         "כל P0 מקפיאה את ההרחבה עד תחקור ותיקון.")
    flow("""
    digraph G {
      rankdir=LR; bgcolor="transparent"; nodesep=0.3; ranksep=0.45;
      node [shape=box, style="rounded,filled", fontname="Arial", fontsize=14, color="none", fontcolor="#0B1B3A", fillcolor="#F2F6FA", margin="0.2,0.12"];
      edge [color="#64748B", arrowsize=0.8, fontname="Arial", fontsize=12];
      G [label="שערים\\nדיוק 90% · אפס P0\\nענן + DPA · שביעות רצון 4\\nP95 ≤ 3 שניות", fillcolor="#0B1B3A", fontcolor="white"];
      P [label="פיילוט\\n15 נציגים · שישה שבועות"];
      W [label="גל 2\\n60 נציגים"];
      F [label="כל המוקד", fillcolor="#2EB67D", fontcolor="white"];
      G -> P -> W -> F;
      P -> G [label="P0", style=dashed, color="#E5484D", fontcolor="#E5484D"];
    }
    """)


# ---------- שקף 9: שלוש החלטות ----------
def slide_decisions():
    head("9", "שלוש החלטות לוועדה, היום", "כל אחת פותחת את הצעד הבא.")
    c1, c2, c3 = st.columns(3)
    c1.markdown(f'<div class="card" style="border-right-color:{TEAL}"><div class="kpi">1</div><h4>בדיקת שני מודלים</h4><p>שבועיים, 200 שאלות, עם תקציב.</p></div>', unsafe_allow_html=True)
    c2.markdown(f'<div class="card" style="border-right-color:{AMBER}"><div class="kpi" style="color:{AMBER}">2</div><h4>שלב א: נהלים בלבד</h4><p>בכפוף לאישור Compliance בכתב.</p></div>', unsafe_allow_html=True)
    c3.markdown(f'<div class="card" style="border-right-color:{GREEN}"><div class="kpi" style="color:{GREEN}">3</div><h4>בלי פעולות בשלב א</h4><p>דשבורד כ-Quick Win, ותאריך לשלב ב.</p></div>', unsafe_allow_html=True)


# ---------- שקף כיסוי ----------
def slide_coverage():
    head("כיסוי", "איפה כל חלק במטלה")
    flow("""
    digraph G {
      rankdir=LR; bgcolor="transparent"; nodesep=0.3; ranksep=0.4;
      node [shape=box, style="rounded,filled", fontname="Arial", fontsize=14, color="none", fontcolor="white", margin="0.22,0.14"];
      edge [color="#64748B", arrowsize=0.8];
      A1 [label="א.1 טבלת השוואה", fillcolor="#0B1B3A"];
      A2 [label="א.2 החלטה ומחיר", fillcolor="#0B1B3A"];
      A3 [label="א.3 סיכונים ומדדים", fillcolor="#0B1B3A"];
      B [label="ב PRD\\nסיפורים · גבולות · השקה", fillcolor="#0F9D8A"];
      C [label="ג משבר\\nעדיפויות · התאוששות · Go/No-Go", fillcolor="#F5A524", fontcolor="#0B1B3A"];
      D [label="ד מצגת", fillcolor="#2EB67D"];
      A1 -> A2 -> A3 -> B -> C -> D;
    }
    """)


SLIDES = [
    slide_cover, slide_project, slide_tracks, slide_decision, slide_product,
    slide_limits, slide_crisis, slide_recovery, slide_pilot, slide_decisions, slide_coverage,
]

if "idx" not in st.session_state:
    st.session_state.idx = 0

idx = st.session_state.idx
total = len(SLIDES)

SLIDES[idx]()

st.markdown("<div style='height:30px'></div>", unsafe_allow_html=True)
nav1, nav2, nav3 = st.columns([1, 2, 1])
with nav1:
    if st.button("הקודם", disabled=idx == 0, width="stretch"):
        st.session_state.idx = idx - 1
        st.rerun()
with nav2:
    st.markdown(f'<div style="text-align:center;color:{GREY};padding-top:10px">{idx + 1} / {total}</div>', unsafe_allow_html=True)
with nav3:
    if st.button("הבא", disabled=idx == total - 1, width="stretch", type="primary"):
        st.session_state.idx = idx + 1
        st.rerun()
