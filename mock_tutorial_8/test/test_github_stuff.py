import mock_tutorial_8.src as users
from mock_tutorial_8.src import get_follower_names


def substitute_func(username):
    return '[{"login": "aishapectyo"},{"login": "jradavenport"},{"login": "kridicule"}]'


def test_get_follower_names_returns_name_list(monkeypatch):
    monkeypatch.setattr(users, 'get_user_followers', substitute_func)
    assert 'jradavenport' in get_follower_names('nhuntwalker')
