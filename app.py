import streamlit as st
from zeros_zones import get_zeta_zero
from pi_zones import get_pi

st.set_page_config(page_title="Zone Mini", layout="centered")
st.title("Zone Modeling – النسخة المبسطة")

mode = st.radio("اختر وظيفة", ["Zeta Zero γₙ", "Prime Count π(x)"])

if mode == "Zeta Zero γₙ":
    n = st.number_input("أدخل رقم n (بين 1 و 100)", min_value=1, max_value=100, step=1)
    if st.button("احسب γₙ"):
        z = get_zeta_zero(n)
        st.success(f"γₙ ≈ {z:.12f}")

else:
    x = st.number_input("أدخل رقم x (بين 1 و 10000)", min_value=1, max_value=10000, step=1)
    if st.button("احسب π(x)"):
        p = get_pi(x)
        st.success(f"π({x}) = {p}")
