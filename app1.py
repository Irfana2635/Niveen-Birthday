import streamlit as st
import streamlit.components.v1 as components
import random

# Page config
st.set_page_config(page_title="Happy Birthday 💙", layout="centered")

# 🎨 Styling (Animated Blue Background)
st.markdown("""
<style>
.stApp {
    background: linear-gradient(-45deg, #0a1f44, #1e90ff, #00bfff, #87cefa);
    background-size: 400% 400%;
    animation: gradient 10s ease infinite;
    text-align: center;
    color: white;
    position: relative;
    z-index: 1;
}

@keyframes gradient {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

.title {
    font-size: 60px;
    font-weight: bold;
    animation: glow 2s infinite alternate;
}

@keyframes glow {
    from { text-shadow: 0 0 10px white; }
    to { text-shadow: 0 0 30px #00bfff; }
}
</style>
""", unsafe_allow_html=True)

# 🖼️ Floating Background Images
images = [
    "https://cdn-icons-png.flaticon.com/512/3075/3075977.png",  # biryani
    "https://cdn-icons-png.flaticon.com/512/861/861512.png",    # football
    "https://cdn-icons-png.flaticon.com/512/3655/3655600.png",  # chess
    "https://cdn-icons-png.flaticon.com/512/1046/1046784.png",  # ice cream
    "https://cdn-icons-png.flaticon.com/512/1046/1046786.png",  # milkshake
    "https://cdn-icons-png.flaticon.com/512/1046/1046769.png",  # chocolate
    "https://cdn-icons-png.flaticon.com/512/590/590685.png"     # kadala mittai
]

bg_elements = ""
for i in range(15):
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    size = random.randint(40, 100)
    img = random.choice(images)

    bg_elements += f"""
    <img src="{img}" style="
        position:absolute;
        left:{x}%;
        top:{y}%;
        width:{size}px;
        opacity:0.15;
    ">
    """

st.markdown(f"""
<div style="position:fixed; width:100%; height:100%; top:0; left:0; z-index:0;">
{bg_elements}
</div>
""", unsafe_allow_html=True)

# 🎉 Title
st.markdown('<div class="title">🎉 Happy Birthday Naaye ❤️</div>', unsafe_allow_html=True)

st.markdown("### 🎂 Wishing you happiness, success & lots of smiles!")

# 🎁 Surprise Button
if st.button("🎁 Click for Surprise"):
    st.balloons()
    st.success("💙 You are special! Enjoy your day 🎉")

# 🎵 Music (Perfect - Ed Sheeran)
components.html("""
<iframe width="0" height="0"
src="https://www.youtube.com/embed/2Vv-BfVoq4g?autoplay=1&loop=1&playlist=2Vv-BfVoq4g"
frameborder="0" allow="autoplay"></iframe>
""", height=0)

# 🎆 Confetti Animation
components.html("""
<script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
<script>
setInterval(() => {
  confetti({
    particleCount: 80,
    spread: 70,
    origin: { y: 0.6 }
  });
}, 2000);
</script>
""", height=0)
