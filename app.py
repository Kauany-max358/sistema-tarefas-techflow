from flask import Flask, request, jsonify

app = Flask(__name__)
tarefas = []
tarefa_id_control = 1

@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas)

@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    global tarefa_id_control
    dados = request.get_json()
    nova_tarefa = {
        "id": tarefa_id_control,
        "titulo": dados.get("titulo"),
        "status": "A Fazer",
        "prioridade": dados.get("prioridade", "Baixa") # Feature da mudança de escopo
    }
    tarefas.append(nova_tarefa)
    tarefa_id_control += 1
    return jsonify(nova_tarefa), 201

@app.route('/tarefas/<int:id>', methods=['DELETE'])
def deletar_tarefa(id):
    global tarefas
    tarefas = [t for t in tarefas if t['id'] != id]
    return jsonify({"message": "Tarefa deletada"}), 200

if __name__ == '__main__':
    app.run(debug=True)