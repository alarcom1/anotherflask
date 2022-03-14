"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/about">About</a>' in response.data
    assert b'<a class="nav-link" href="/git">Git Hub</a>' in response.data
    """assert b'<a class="nav-link" href="/page1">Page 1</a>' in response.data"""
    assert b'<a class="nav-link" href="/docker">Docker</a>' in response.data
    """assert b'<a class="nav-link" href="/page2">Page 2</a>' in response.data"""
    assert b'<a class="nav-link" href="/pyflask">Py Flask</a>' in response.data
    """assert b'<a class="nav-link" href="/page3">Page 3</a>' in response.data"""
    assert b'<a class="nav-link" href="/page4">Page 4</a>' in response.data

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Mauricios Site" in response.data

def test_request_about(client):
    """This makes the about page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About Page" in response.data

def test_request_git(client):
    """This makes the git page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b"Git Hub" in response.data

"""def test_request_page1(client):
    This makes the index page
    response = client.get("/page1")
    assert response.status_code == 200
    assert b"Page 1" in response.data"""

def test_request_docker(client):
    """This makes the docker page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"Docker" in response.data

"""def test_request_page2(client):
    This makes the index page
    response = client.get("/page2")
    assert response.status_code == 200
    assert b"Page 2" in response.data"""

def test_request_pyflask(client):
    """This makes the py flask page"""
    response = client.get("/pyflask")
    assert response.status_code == 200
    assert b"Python and Flask" in response.data

"""def test_request_page3(client):
    This makes the index page
    response = client.get("/page3")
    assert response.status_code == 200
    assert b"Page 3" in response.data"""

def test_request_page4(client):
    """This makes the index page"""
    response = client.get("/page4")
    assert response.status_code == 200
    assert b"Page 4" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404