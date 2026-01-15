from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Te amo 💖</title>
    <style>
        body {
            margin: 0;
            background: black;
            overflow: hidden;
            font-family: Arial, sans-serif;
            color: white;
            text-align: center;
        }

        .container {
            position: absolute;
            top: 40%;
            width: 100%;
            transform: translateY(-50%);
        }

        h1 {
            font-size: 3em;
        }

        button {
            font-size: 1.5em;
            padding: 10px 30px;
            margin: 20px;
            cursor: pointer;
            border-radius: 10px;
            border: none;
        }

        #si {
            background: pink;
        }

        #no {
            background: red;
            color: white;
            position: absolute;
        }

        .heart {
            position: fixed;
            top: -10px;
            font-size: 20px;
            animation: fall linear infinite;
            color: pink;
        }

        @keyframes fall {
            to {
                transform: translateY(110vh);
            }
        }
    </style>
</head>
<body>

<div class="container">
    <h1 id="mensaje">Te amo, ¿me amas? 💕</h1>
    <button id="si" onclick="aceptar()">Sí 💖</button>
    <button id="no" onmouseover="moverNo()">No 💔</button>
</div>

<script>
    const excusas = ["¿Segura?", "¿De verdad?", "¿Estás segurísima?", "Piénsalo bien 😳", "No acepto un no 😈"];
    let intento = 0;

    function aceptar() {
        document.getElementById("mensaje").innerHTML = "😊💖 Sabía que dirías que sí 💖😊";
        document.getElementById("si").style.display = "none";
        document.getElementById("no").style.display = "none";
    }

    function moverNo() {
        const no = document.getElementById("no");
        no.style.left = Math.random() * (window.innerWidth - 100) + "px";
        no.style.top = Math.random() * (window.innerHeight - 100) + "px";
        document.getElementById("mensaje").innerHTML = excusas[intento % excusas.length];
        intento++;
    }

    function crearCorazon() {
        const heart = document.createElement("div");
        heart.className = "heart";
        heart.innerHTML = "💖";
        heart.style.left = Math.random() * 100 + "vw";
        heart.style.animationDuration = (Math.random() * 3 + 2) + "s";
        document.body.appendChild(heart);
        setTimeout(() => heart.remove(), 5000);
    }

    setInterval(crearCorazon, 200);
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
