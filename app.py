import streamlit as st
from zeros_zones import get_zeta_zero
from pi_zones import get_pi, pi_zones

@st.cache_resource
def load_models():
    return get_zeta_zero, pi_zones, get_pi

get_zeta_zero, pi_zones, get_pi = load_models()

st.set_page_config(page_title="Zone Mini Updated", layout="centered")
st.title("Zone Modeling – النسخة المحسنة")

mode = st.radio("اختر وظيفة", ["Zeta Zero γₙ", "Prime Count π(x)"])

if mode == "Zeta Zero γₙ":
    n = st.number_input("أدخل n بين 1 و 300", min_value=1, max_value=300, step=1)
    if st.button("احسب γₙ"):
        try:
            z = get_zeta_zero(int(n))
            st.success(f"γₙ ≈ {z:.12f}")
        except ValueError as ve:
            st.error(f"خطأ في المدخلات: {ve}")
        except Exception:
            st.error("حدث خطأ غير متوقع.")

else:
    x = st.number_input("أدخل x بين 1 و 10000", min_value=1, max_value=10000, step=1)
    if st.button("احسب π(x)"):
        try:
            p = get_pi(int(x))
            st.success(f"π({x}) = {p}")
        except ValueError as ve:
            st.error(f"خطأ في المدخلات: {ve}")
        except Exception:
            st.error("حدث خطأ غير متوقع.")
