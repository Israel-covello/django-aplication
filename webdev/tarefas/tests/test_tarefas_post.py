import pytest
from django.urls import reverse
from webdev.tarefas.models import Tarefa


@pytest.fixture
def resposta(client, db):
    resp = client.post(reverse('tarefas:home'), data={'nome': 'Tarefa'})
    return resp


def test_tafera_existe_no_bd(resposta):
    assert Tarefa.objects.exists()

