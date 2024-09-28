import pytest
from fastapi.testclient import TestClient
from main import app

cliente = TestClient(app)

def test_create_jogador_success():
    response = cliente.post("/novoJogador?select_cor=1")
    assert response.status_code == 201

def test_create_jogador_insuccess2():
    response = cliente.post("/novoJogador?select_cor=1")
    assert response.status_code == 400

def test_create_jogador_succes3():
    response = cliente.post("/novoJogador?select_cor=3")
    assert response.status_code == 201

def test_create_jogador_success4():
    response = cliente.post("/novoJogador?select_cor=4")
    assert response.status_code == 201

def test_create_jogador_success5():
    response = cliente.post("/novoJogador?select_cor=5")
    assert response.status_code == 201

def test_create_jogador_success6():
    response = cliente.post("/novoJogador?select_cor=6")
    assert response.status_code == 201

def test_create_jogador_insuccess7():
    response = cliente.post("/novoJogador?select_cor=1")
    assert response.status_code == 400

 