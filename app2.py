import streamlit as st
import streamlit.components.v1 as components
import random
import base64

# Page config
st.set_page_config(page_title="Happy Birthday 💙", layout="centered")

# 🔄 Convert local image to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()

# 👉 Replace with your image file name
img_base64 = get_base64_image("Niveen.jpeg")

# 🎨 Styling (Background + Center Image)
st.markdown(f"""
<style>
.stApp {{
    background: linear-gradient(-45deg, #0a1f44, #1e90ff, #00bfff, #87cefa);
    background-size: 400% 400%;
    animation: gradient 10s ease infinite;
    text-align: center;
    color: white;
    position: relative;
    z-index: 1;
}}

@keyframes gradient {{
    0% {{background-position: 0% 50%;}}
    50% {{background-position: 100% 50%;}}
    100% {{background-position: 0% 50%;}}
}}

.title {{
    font-size: 60px;
    font-weight: bold;
    animation: glow 2s infinite alternate;
}}

@keyframes glow {{
    from {{ text-shadow: 0 0 10px white; }}
    to {{ text-shadow: 0 0 30px #00bfff; }}
}}

/* 🌫️ Center Image Styling */
.center-img {{
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 280px;
    border-radius: 20px;
    opacity: 0.35;
    filter: blur(1.5px) brightness(0.9);
    box-shadow: 0 0 40px rgba(255,255,255,0.3);
    z-index: 0;
}}
</style>

<!-- 🖼️ Center Image -->
<img src="data:image/jpeg;base64,{img_base64}" class="center-img">

""", unsafe_allow_html=True)

# 🖼️ Floating Background Images
images = [
    "https://cdn-icons-png.flaticon.com/512/3075/3075977.png",
    "https://cdn-icons-png.flaticon.com/512/861/861512.png",
    "https://cdn-icons-png.flaticon.com/512/3655/3655600.png",
    "https://cdn-icons-png.flaticon.com/512/1046/1046784.png",
    "https://cdn-icons-png.flaticon.com/512/1046/1046786.png",
    "https://cdn-icons-png.flaticon.com/512/1046/1046769.png",
    "https://cdn-icons-png.flaticon.com/512/590/590685.png"
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
        opacity:0.12;
    ">
    """

st.markdown(f"""
<div style="position:fixed; width:100vw; height:100vh; top:0; left:0; z-index:-1; overflow:hidden;">
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
