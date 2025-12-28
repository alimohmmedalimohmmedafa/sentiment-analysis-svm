import streamlit as st
# تأكد من ربط ملف الموديل الخاص بك
# from model import predict_sentiment 

# دالة تجريبية للمنطق (استبدلها بدالة الـ SVM الخاصة بك)
def predict_sentiment(text):
    if "سعيد" in text or "فرح" in text: return "happy"
    if "حزين" in text or "ألم" in text: return "sad"
    if "غاضب" in text: return "angry"
    return "neutral"

st.set_page_config(
    page_title="تحليل المشاعر - SVM",
    page_icon="🧠",
    layout="centered"
)

# تحسين مظهر الأزرار والخلفية
st.markdown("""
    <style>
    .stButton>button { 
        border-radius: 12px; 
        height: 3.5em; 
        font-weight: bold; 
        background-color: #007bff; 
        color: white;
    }
    .stSelectbox label { font-size: 20px !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🧠 نظام تحليل المشاعر الذكي")
st.write("اختر إحدى الجمل التالية ليقوم نظام **SVM** بتحليل الحالة العاطفية الكامنة خلفها:")

# القائمة المنسدلة فقط
sentences = [
    "اختر جملة تعبر عن حالك...",
    "انا سعيد جدا اليوم",
    "اشعر بفرح كبير",
    "بكيت من شدة الفرح",
    "انا حزين جدا",
    "اشعر بالاكتئاب",
    "بكيت بسبب الالم",
    "انا غاضب جدا",
    "اليوم كان عاديا جدا"
]

selected_text = st.selectbox("📌 القائمة المتاحة:", sentences)

# إدارة حالة الـ Popup
if "show_popup" not in st.session_state:
    st.session_state.show_popup = False
    st.session_state.result = None

# زر التحليل
if st.button("🔍 ابدأ تحليل المشاعر الآن", use_container_width=True):
    if selected_text != "اختر جملة تعبر عن حالك...":
        st.session_state.result = predict_sentiment(selected_text)
        st.session_state.show_popup = True
    else:
        st.error("الرجاء اختيار جملة من القائمة أولاً!")

# ===== عرض النتيجة (Popup) =====
if st.session_state.show_popup:
    res = st.session_state.result
    
    # إعدادات النتائج
    styles = {
        "happy": {"title": "😊 أنت في قمة السعادة", "msg": "استمتع بلحظاتك الجميلة، طاقتك الإيجابية رائعة!", "color": "#28a745"},
        "sad": {"title": "😢 يبدو أنك متضايق", "msg": "لا بأس بالحزن أحياناً، غداً ستشرق الشمس من جديد.", "color": "#17a2b8"},
        "angry": {"title": "😡 أنت في حالة غضب", "msg": "حاول الاسترخاء قليلاً، الغضب لا يحل المشكلات.", "color": "#dc3545"},
        "neutral": {"title": "😐 مشاعر محايدة", "msg": "تبدو في حالة استقرار وهدوء تام.", "color": "#6c757d"}
    }
    
    config = styles.get(res, styles["neutral"])

    # تصميم الـ Popup باستخدام HTML
    st.markdown(f"""
        <div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8); z-index: 999; display: flex; justify-content: center; align-items: center;">
            <div style="background: white; padding: 40px; border-radius: 20px; text-align: center; max-width: 400px; border-bottom: 8px solid {config['color']};">
                <h1 style="color: {config['color']};">{config['title']}</h1>
                <p style="font-size: 1.2em; color: #333;">{config['msg']}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # زر لإغلاق الـ Popup وإعادة التعيين
    if st.button("❌ إغلاق النتيجة"):
        st.session_state.show_popup = False
        st.rerun()