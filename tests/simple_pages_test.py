"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/about">About</a>' in response.data
    assert b'<a class="nav-link" href="/git">Git Hub</a>' in response.data
    assert b'<a class="nav-link" href="/docker">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/pyflask">Py Flask</a>' in response.data
    assert b'<a class="nav-link" href="/cicd">CI/CD</a>' in response.data

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Mauricios Site" in response.data

def test_request_about(client):
    """This makes the about page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About Mauricio" in response.data

def test_request_git(client):
    """This makes the git page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b"Git Hub" in response.data

def test_request_docker(client):
    """This makes the docker page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"Docker" in response.data

def test_request_pyflask(client):
    """This makes the py flask page"""
    response = client.get("/pyflask")
    assert response.status_code == 200
    assert b"Python and Flask" in response.data

def test_request_cicd(client):
    """This makes the ci cd page"""
    response = client.get("/cicd")
    assert response.status_code == 200
    assert b"CI/CD" in response.data

def test_request_pytutorial(client):
    """This makes the learn python page"""
    response = client.get("/pytutorial")
    assert response.status_code == 200
    assert b"Python Tutorial" in response.data

def test_request_abstraction(client):
    """This makes the learn python page"""
    response = client.get("/oop")
    assert response.status_code == 200
    assert b"Object Oriented Programming" in response.data

def test_request_aaatesting(client):
    """This makes the learn python page"""
    response = client.get("/aaatest")
    assert response.status_code == 200
    assert b"AAA Testing" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404
