from app import app
import pytest

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    # اختبار صفحة البداية للـ API هل بترد بنجاح ولا لأ
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert "Welcome" in data["message"]
