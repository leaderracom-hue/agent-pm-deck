"""נציג AI: מצגת חלק ד. Streamlit, RTL, עיצוב גרפי."""
import streamlit as st

st.set_page_config(page_title="נציג AI", page_icon="■", layout="wide", initial_sidebar_state="collapsed")

NAVY = "#0B1B3A"
TEAL = "#14B8A6"
AMBER = "#F59E0B"
RED = "#EF4444"
GREEN = "#22C55E"
INK = "#EAF0FA"
MUTED = "#9FB0C8"
CARD = "#132A52"

CSS = f"""
<style>
html, body, [class*="css"] {{ font-family: "Segoe UI", "Arial", sans-serif; }}
.stApp {{ background: {NAVY}; color: {INK}; direction: rtl; }}
header, footer, [data-testid="stSidebar"] {{ display: none !important; }}
.block-container {{ max-width: 1180px; padding-top: 2.2rem; padding-bottom: 2rem; }}
.kicker {{ color: {TEAL}; font-weight: 600; letter-spacing: .02em; font-size: 15px; }}
.title {{ font-size: 46px; font-weight: 800; line-height: 1.15; margin: 6px 0 14px; color: {INK}; }}
.lead {{ font-size: 20px; color: {MUTED}; line-height: 1.6; margin-bottom: 24px; }}
.card {{ background: {CARD}; border-radius: 18px; padding: 22px 24px; height: 100%; border: 1px solid #1d3766; }}
.card h4 {{ margin: 0 0 8px; font-size: 19px; color: {INK}; }}
.card p {{ margin: 0; color: {MUTED}; font-size: 16px; line-height: 1.6; }}
.big {{ font-size: 64px; font-weight: 800; color: {TEAL}; line-height: 1.1; }}
.tag {{ display: inline-block; padding: 5px 12px; border-radius: 999px; font-size: 14px; font-weight: 600; margin: 3px 4px 3px 0; }}
.dot {{ display: inline-block; width: 12px; height: 12px; border-radius: 50%; margin-left: 8px; vertical-align: middle; }}
.row {{ display: flex; gap: 14px; direction: rtl; }}
.arrow {{ align-self: center; font-size: 30px; color: {MUTED}; }}
.stepbox {{ flex: 1; background: {CARD}; border-radius: 16px; padding: 18px; text-align: center; border: 1px solid #1d3766; }}
.stepbox b {{ font-size: 18px; color: {INK}; }}
.stepbox span {{ display: block; color: {MUTED}; font-size: 14px; margin-top: 6px; }}
.bigq {{ font-size: 30px; font-weight: 700; color: {INK}; line-height: 1.5; }}
.check {{ color: {GREEN}; font-weight: 800; margin-left: 8px; }}
.cross {{ color: {RED}; font-weight: 800; margin-left: 8px; }}
.bar {{ height: 14px; border-radius: 8px; background: #1d3766; overflow: hidden; margin: 8px 0 16px; }}
.stButton > button {{ background: {CARD}; color: {INK}; border: 1px solid #2a4a85; border-radius: 12px; font-size: 17px; font-weight: 600; min-height: 48px; }}
.stButton > button:hover {{ border-color: {TEAL}; color: {TEAL}; }}
.stButton > button:disabled {{ background: transparent; color: #4b6188; border-color: #1d3766; }}
.stButton > button[kind="primary"] {{ background: {TEAL}; color: {NAVY}; border: none; }}
.stButton > button[kind="primary"]:hover {{ background: #2dd4bf; color: {NAVY}; }}
.stApp::before {{ content: ""; position: fixed; top: 0; left: 0; right: 0; height: 6px; background: {TEAL}; }}
.bar > div {{ height: 100%; border-radius: 8px; }}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


def card(title, body):
    return f'<div class="card"><h4>{title}</h4><p>{body}</p></div>'


def tag(text, color):
    return f'<span class="tag" style="background:{color}22;color:{color};border:1px solid {color}66">{text}</span>'


def dot(color):
    return f'<span class="dot" style="background:{color}"></span>'


def slide_cover():
    st.markdown(f"""
    <div style="margin-top:70px">
      <div class="kicker">מטלת Data & AI PM · פרויקט בנק</div>
      <div class="title" style="font-size:88px">נציג AI</div>
      <div class="lead" style="font-size:26px;color:{INK}">מהחלטת ארכיטקטורה ועד ניהול משבר בשטח</div>
      <div style="margin-top:40px;display:flex;gap:12px">
        {tag("3 חלקים", TEAL)}{tag("9 שקפים + כיסוי", AMBER)}{tag("אסף", MUTED)}
      </div>
    </div>
    """, unsafe_allow_html=True)


def slide_project():
    st.markdown('<div class="kicker">1 · הפרויקט</div>', unsafe_allow_html=True)
    st.markdown('<div class="title">סוכן שעונה לנציג תוך שניות, רק מתוך נהלים מאושרים</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.markdown(card("מה בנינו", "סוכן AI שעונה לנציג המוקד על מוצרים, נהלים ורגולציה, בזמן אמת."), unsafe_allow_html=True)
    c2.markdown(card("למי", "נציגי המוקד: ותיקים שמכירים הכול, וחדשים שעדיין לומדים."), unsafe_allow_html=True)
    c3.markdown(card("מה נחשב הצלחה", "זמן חיפוש קצר יותר, 90% תשובות נכונות, ואפס טעויות חמורות."), unsafe_allow_html=True)


def slide_tracks():
    st.markdown('<div class="kicker">2 · שלוש דרכים</div>', unsafe_allow_html=True)
    st.markdown('<div class="title">כלי הרכבה לא נותן מוח. הוא שכבה מעל אחת משתי הדרכים</div>', unsafe_allow_html=True)
    cols = st.columns(3)
    data = [
        ("ענן מנוהל", "כמו לשכור דירה", [("אבטחה", AMBER), ("עברית", AMBER), ("זמן עד פיילוט", AMBER)], TEAL),
        ("הרצה בבית", "כמו לקנות דירה", [("אבטחה", GREEN), ("עברית", RED), ("זמן עד פיילוט", RED)], AMBER),
        ("כלי הרכבה", "כמו ארגז לגו", [("אבטחה", AMBER), ("עברית", AMBER), ("זמן עד פיילוט", AMBER)], MUTED),
    ]
    for col, (name, sub, rows, accent) in zip(cols, data):
        body = "".join(f'<div style="margin:8px 0">{dot(c)}{label}</div>' for label, c in rows)
        col.markdown(
            f'<div class="card" style="border-top:4px solid {accent}"><h4>{name}</h4>'
            f'<p style="margin-bottom:12px">{sub}</p>'
            f'<div style="color:{INK};font-size:16px">{body}</div></div>',
            unsafe_allow_html=True,
        )
    st.markdown(f'<p class="lead" style="margin-top:20px;font-size:16px">{dot(GREEN)}מתאים &nbsp; {dot(AMBER)}מתאים בתנאי &nbsp; {dot(RED)}בעייתי</p>', unsafe_allow_html=True)


def slide_decision():
    st.markdown('<div class="kicker">3 · ההחלטה והמחיר</div>', unsafe_allow_html=True)
    st.markdown('<div class="big">בחרתי היברידי</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="lead" style="font-size:22px;color:{INK}">המחיר: תלות בספק, ודיוק בעברית שעוד לא הוכח.</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.markdown(card("1 · אזור ישראלי", "המודל זמין בישראל, או שאני בודק חלופה."), unsafe_allow_html=True)
    c2.markdown(card("2 · בלי שמירה", "אישור בכתב שהספק לא שומר תשובות."), unsafe_allow_html=True)
    c3.markdown(card("3 · עברית 90%", "מבחן של 200 שאלות. מתחת לזה, לא עולים לאוויר."), unsafe_allow_html=True)
    st.markdown(f'<p class="lead" style="margin-top:22px;font-size:18px">אם התנאים לא עוברים, אני עובר לתוכנית ב\': שלב א על מסמכים בלבד, עם מודל שרץ בבנק.</p>', unsafe_allow_html=True)


def slide_product():
    st.markdown('<div class="kicker">4 · המוצר</div>', unsafe_allow_html=True)
    st.markdown('<div class="title">שאלה על ריבית: תשובה עם ציטוט, או "אין מקור"</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="row" style="margin-top:14px">
      <div class="stepbox"><b>הנציג שואל</b><span>על ריבית הלוואה לדיור</span></div>
      <div class="arrow">←</div>
      <div class="stepbox"><b>מסמך מאושר?</b><span>בעלים, גרסה, תוקף</span></div>
      <div class="arrow">←</div>
      <div class="stepbox" style="border-color:{GREEN}"><b>כן: תשובה + ציטוט</b><span>עד 3 שניות, P95</span></div>
      <div class="arrow">|</div>
      <div class="stepbox" style="border-color:{RED}"><b>לא: "אין מקור"</b><span>מפנה למומחה</span></div>
    </div>
    """, unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    c1.markdown(card("הוותיק", "לא סומך על כלי שטועה פעם אחת. לכן כל תשובה עם מקור לחיצה."), unsafe_allow_html=True)
    c2.markdown(card("החדש", "מפחד לשאול. לכן ״אין מקור״ הוא תשובה לגיטימית, לא כישלון."), unsafe_allow_html=True)


def slide_limits():
    st.markdown('<div class="kicker">5 · הגבולות</div>', unsafe_allow_html=True)
    st.markdown('<div class="title">עונה על מוצרים ונהלים. לא נוגע בחשבון ולא מייעץ</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.markdown(card(f'<span class="check">✓</span>עונה על', "מוצרים, נהלים מאושרים, והסברי רגולציה מתוך מסמך."), unsafe_allow_html=True)
    c2.markdown(card(f'<span class="cross">✕</span>לא עושה', "נתוני לקוח, פעולות בחשבון, ייעוץ השקעות, התחייבות בשם הבנק."), unsafe_allow_html=True)
    c3.markdown(card("כשלא יודע", "אומר: 'אין מקור מאושר, פנה למומחה'. בלי ניחוש."), unsafe_allow_html=True)


def slide_crisis():
    st.markdown('<div class="kicker">6 · המשבר</div>', unsafe_allow_html=True)
    st.markdown('<div class="title">שלושה חסמים. הראשון קובע הכול</div>', unsafe_allow_html=True)
    items = [
        ("1 · דיוק המודל", "23% שגיאות (כ-77% דיוק) מול 85% סף עצירה", RED, 77),
        ("2 · Compliance", "אסור לטעון נתוני לקוח. בשלב א אין כאלה", AMBER, 60),
        ("3 · VP מבקש פעולות", "שינוי גבול שדורש החלטת ועדה", AMBER, 40),
    ]
    for title, sub, color, pct in items:
        st.markdown(
            f'<div class="card" style="margin-bottom:12px"><h4>{dot(color)}{title}</h4>'
            f'<p>{sub}</p><div class="bar"><div style="width:{pct}%;background:{color}"></div></div></div>',
            unsafe_allow_html=True,
        )
    st.markdown(f'<p class="lead" style="font-size:17px">הלקח: בחרתי כיוון לפני מבחן העברית. המבחן היה צריך להקדים את הבחירה.</p>', unsafe_allow_html=True)


def slide_recovery():
    st.markdown('<div class="kicker">7 · מה עשיתי</div>', unsafe_allow_html=True)
    st.markdown('<div class="title">לכל חסם: פתרון, בעלים, ומה אפשר לעשות כבר</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.markdown(card("דיוק", "שלושה מודלים על 200 שאלות, תוך שבועיים. מי שעובר 90% נבחר. בעלים: R&D + Compliance."), unsafe_allow_html=True)
    c2.markdown(card("Compliance", "שלב א על מסמכי נהלים בלבד, עם אישור בכתב. בעלים: ניהול מוצר."), unsafe_allow_html=True)
    c3.markdown(card("VP", "לא פעולות בשלב א. דשבורד שבועי תוך 3 שבועות במקום. הוועדה מחליטה."), unsafe_allow_html=True)


def slide_gate():
    st.markdown('<div class="kicker">8 · הפיילוט</div>', unsafe_allow_html=True)
    st.markdown('<div class="title">15 נציגים, מוקד אחד, שישה שבועות</div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="card">
      <h4>מתי מרחיבים לכל המוקד</h4>
      <p style="color:{INK};font-size:17px;line-height:2">
        <span class="check">✓</span>דיוק 90% ומעלה<br>
        <span class="check">✓</span>אפס P0. כל P0 מקפיאה את ההרחבה<br>
        <span class="check">✓</span>אישורי ענן ו-Compliance בכתב<br>
        <span class="check">✓</span>שביעות רצון נציגים 4 ומעלה<br>
        <span class="check">✓</span>זמן תשובה P95 עד 3 שניות בשעות שיא
      </p>
    </div>
    """, unsafe_allow_html=True)


def slide_decisions():
    st.markdown('<div class="kicker">9 · מה אני מבקש מהוועדה</div>', unsafe_allow_html=True)
    st.markdown('<div class="title">שלוש החלטות, היום</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.markdown(f'<div class="card"><div class="big" style="font-size:52px">1</div><h4>בדיקת שני מודלים</h4><p>שבועיים, מבחן של 200 שאלות, עם תקציב.</p></div>', unsafe_allow_html=True)
    c2.markdown(f'<div class="card"><div class="big" style="font-size:52px">2</div><h4>שלב א: נהלים בלבד</h4><p>בכפוף לאישור Compliance בכתב.</p></div>', unsafe_allow_html=True)
    c3.markdown(f'<div class="card"><div class="big" style="font-size:52px">3</div><h4>בלי פעולות בשלב א</h4><p>דשבורד כ-Quick Win, ותאריך לשלב ב.</p></div>', unsafe_allow_html=True)


def slide_coverage():
    st.markdown('<div class="kicker">כיסוי</div>', unsafe_allow_html=True)
    st.markdown('<div class="title">מה יש בכל חלק</div>', unsafe_allow_html=True)
    rows = [
        ("א.1", "טבלת השוואה: שלוש דרכים, שבע שורות ועוד שלוש"),
        ("א.2", "החלטה (היברידי), נימוקים, מחיר ותנאים"),
        ("א.3", "שלושה סיכונים, ארבעה מדדים, תנאי סף"),
        ("ב", "PRD: בעיה, חמישה סיפורי משתמש, גבולות, רגולציה, השקה"),
        ("ג", "משבר: סדר עדיפויות, עמוד לוועדה, התאוששות, Go/No-Go, מייל שבועי"),
        ("ד", "המצגת"),
    ]
    html = "".join(
        f'<div style="display:flex;gap:18px;padding:12px 0;border-bottom:1px solid #1d3766">'
        f'<div style="min-width:70px;color:{TEAL};font-weight:800;font-size:20px">{k}</div>'
        f'<div style="font-size:18px;color:{INK}">{v}</div></div>'
        for k, v in rows
    )
    st.markdown(f'<div class="card">{html}</div>', unsafe_allow_html=True)


SLIDES = [
    slide_cover,
    slide_project,
    slide_tracks,
    slide_decision,
    slide_product,
    slide_limits,
    slide_crisis,
    slide_recovery,
    slide_gate,
    slide_decisions,
    slide_coverage,
]

if "idx" not in st.session_state:
    st.session_state.idx = 0

idx = st.session_state.idx
total = len(SLIDES)

SLIDES[idx]()

st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)
nav1, nav2, nav3 = st.columns([1, 2, 1])
with nav1:
    if st.button("הקודם", disabled=idx == 0, use_container_width=True):
        st.session_state.idx = idx - 1
        st.rerun()
with nav2:
    st.markdown(
        f'<div style="text-align:center;color:{MUTED};padding-top:8px">{idx + 1} / {total}</div>',
        unsafe_allow_html=True,
    )
with nav3:
    if st.button("הבא", disabled=idx == total - 1, use_container_width=True, type="primary"):
        st.session_state.idx = idx + 1
        st.rerun()
