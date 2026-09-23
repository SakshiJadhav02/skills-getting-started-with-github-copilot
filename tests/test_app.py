from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    email = "newstudent@mergington.edu"
    activity = "Chess Club"

    signup_response = client.post(f"/activities/{activity}/signup?email={email}")
    assert signup_response.status_code == 200

    response = client.delete(f"/activities/{activity}/participants/{email}")
    assert response.status_code == 200
    assert email not in response.json()["participants"]

    refreshed = client.get("/activities")
    assert email not in refreshed.json()[activity]["participants"]
