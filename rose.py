# Realistic Full Bloom 3D Rose 🌹✨ for Minahil Ramzan

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>For Minahil Ramzan ❤️</title>
<style>
body {
    margin:0;
    padding:0;
    height:100vh;
    width:100vw;
    display:flex;
    justify-content:center;
    align-items:center;
    flex-direction:column;
    background: radial-gradient(circle at center, #ffd6eb, #ff66b2, #cc0066);
    overflow:hidden;
    font-family: 'Segoe UI', sans-serif;
    text-align:center;
}

/* Scene */
.scene {
    perspective: 1200px;
    margin-bottom: 20px;
}

.rose {
    width: 60vw;
    max-width: 240px;
    height: 60vw;
    max-height: 240px;
    position: relative;
    transform-style: preserve-3d;
}

/* Realistic Petals */
.petal {
    position: absolute;
    width: 60%;
    height: 70%;
    left: 20%;
    top: 15%;
    background: radial-gradient(circle at 30% 30%, #ff99cc, #ff0066);
    border-radius: 60% 60% 70% 70%;
    transform-origin: bottom center;
    box-shadow: 0 10px 25px rgba(0,0,0,0.3);
    transition: transform 2s ease;
}

/* More petals with rotation for realism */
.petal:nth-child(1) { transform: rotateY(0deg) rotateX(80deg); z-index:9; }
.petal:nth-child(2) { transform: rotateY(30deg) rotateX(80deg); z-index:8; }
.petal:nth-child(3) { transform: rotateY(60deg) rotateX(80deg); z-index:7; }
.petal:nth-child(4) { transform: rotateY(90deg) rotateX(80deg); z-index:6; }
.petal:nth-child(5) { transform: rotateY(120deg) rotateX(80deg); z-index:5; }
.petal:nth-child(6) { transform: rotateY(150deg) rotateX(80deg); z-index:4; }
.petal:nth-child(7) { transform: rotateY(180deg) rotateX(80deg); z-index:3; }
.petal:nth-child(8) { transform: rotateY(210deg) rotateX(80deg); z-index:2; }
.petal:nth-child(9) { transform: rotateY(240deg) rotateX(80deg); z-index:1; }

/* Bloom animation (staggered for realism) */
.bloom .petal:nth-child(1){ transform: rotateY(0deg) rotateX(15deg); transition-delay:0s; }
.bloom .petal:nth-child(2){ transform: rotateY(30deg) rotateX(15deg); transition-delay:0.1s; }
.bloom .petal:nth-child(3){ transform: rotateY(60deg) rotateX(15deg); transition-delay:0.2s; }
.bloom .petal:nth-child(4){ transform: rotateY(90deg) rotateX(15deg); transition-delay:0.3s; }
.bloom .petal:nth-child(5){ transform: rotateY(120deg) rotateX(15deg); transition-delay:0.4s; }
.bloom .petal:nth-child(6){ transform: rotateY(150deg) rotateX(15deg); transition-delay:0.5s; }
.bloom .petal:nth-child(7){ transform: rotateY(180deg) rotateX(15deg); transition-delay:0.6s; }
.bloom .petal:nth-child(8){ transform: rotateY(210deg) rotateX(15deg); transition-delay:0.7s; }
.bloom .petal:nth-child(9){ transform: rotateY(240deg) rotateX(15deg); transition-delay:0.8s; }

/* Message styling */
.message {
    font-size: 4vw;
    color:white;
    margin-top:12px;
    white-space: pre-line;
}
.urdu {
    margin-top:8px;
    direction: rtl;
    font-size: 4.5vw;
    font-weight:500;
}

/* Button */
button {
    margin-top:20px;
    padding:12px 20px;
    font-size:4vw;
    border:none;
    border-radius:25px;
    background:white;
    color:#cc0066;
    box-shadow:0 0 15px white;
}

/* Falling petals */
.fall {
    position:absolute;
    top:-40px;
    font-size:20px;
    animation:fall linear infinite;
}
@keyframes fall { to { transform: translateY(110vh) rotate(360deg); } }

/* Sparkles */
.sparkle {
    position:absolute;
    width:4px;
    height:4px;
    background:white;
    border-radius:50%;
    animation:sparkle 2s infinite alternate;
}
@keyframes sparkle { from {opacity:0.3;} to{opacity:1;} }
</style>
</head>
<body>

<div class="scene">
    <div class="rose" id="rose">
        <div class="petal"></div>
        <div class="petal"></div>
        <div class="petal"></div>
        <div class="petal"></div>
        <div class="petal"></div>
        <div class="petal"></div>
        <div class="petal"></div>
        <div class="petal"></div>
        <div class="petal"></div>
    </div>
</div>

<div class="message" id="message"></div>
<button onclick="forgive()">کیا آپ مجھے معاف کریں گی؟ 💖</button>

<script>
let text = "Minahil Ramzan 💗\\nI am truly sorry... 🌹\\nYou mean everything to me ❤️\\n\\n";
let urdu = "Draamoo 💕\\nمجھے واقعی اپنی غلطی کا احساس ہے۔\\nآپ میری زندگی کی سب سے قیمتی چیز ہیں۔\\nبراہ کرم مجھے معاف کر دیں۔ 🌹❤️";
let i=0;

// Auto bloom on page load
window.onload = function() {
    setTimeout(()=>{document.getElementById("rose").classList.add("bloom");}, 1000);
    setTimeout(typeWriter, 3000);
};

function typeWriter(){
    if(i<text.length){
        document.getElementById("message").innerHTML += text.charAt(i);
        i++;
        setTimeout(typeWriter,40);
    } else {
        document.getElementById("message").innerHTML += "<div class='urdu'>"+urdu+"</div>";
    }
}

function forgive(){ alert("آپ کا بہت شکریہ ❤️🌹"); }

/* Falling petals */
for(let j=0;j<15;j++){
    let petal=document.createElement("div");
    petal.className="fall";
    petal.innerHTML="🌸";
    petal.style.left=Math.random()*100+"vw";
    petal.style.animationDuration=(6+Math.random()*4)+"s";
    document.body.appendChild(petal);
}

/* Sparkles */
for(let k=0;k<30;k++){
    let s=document.createElement("div");
    s.className="sparkle";
    s.style.top=Math.random()*100+"vh";
    s.style.left=Math.random()*100+"vw";
    document.body.appendChild(s);
}
</script>
</body>
</html>
"""

file_name = "index.html"

with open(file_name,"w",encoding="utf-8") as f:
    f.write(html_content)

print("Ultra-realistic full bloom rose HTML created successfully 🌹✨")
print("Upload this file to Netlify or GitHub Pages and send her the link 💖")
