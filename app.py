# app.py
from flask import Flask, render_template, request, jsonify
from agente import AgenteTemperatura

app = Flask(__name__)
agente = AgenteTemperatura()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ciclo', methods=['POST'])
def ciclo():
    dados = request.json or {}
    cam_atual = float(dados.get('cam', 0.0))
    td_base_input = dados.get('td_base', None)

    if td_base_input is not None and td_base_input != "":
        agente.td_base = float(td_base_input)

    resultado = agente.perceber_e_agir(agente.ta, cam_atual)

    return jsonify({
        "status": resultado,
        "memoria": agente.memoria[-8:],
        "tempo_espera": agente.tempo_espera,
        "cam": cam_atual
    })

if __name__ == '__main__':
    app.run(debug=True)