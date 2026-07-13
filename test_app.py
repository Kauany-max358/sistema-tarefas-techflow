import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_criar_tarefa(client):
    resposta = client.post('/tarefas', json={"titulo": "Aprender CI/CD", "prioridade": "Alta"})
    assert resposta.status_code == 201
    assert "Aprender CI/CD" in str(resposta.data)

def test_listar_tarefas(client):
    resposta = client.get('/tarefas')
    assert resposta.status_code == 200