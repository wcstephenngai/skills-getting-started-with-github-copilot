from urllib.parse import quote

import src.app as app_module


def test_signup_adds_new_participant(client):
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    response = client.post(
        f"/activities/{quote(activity_name, safe='')}/signup",
        params={"email": email},
    )

    assert response.status_code == 200
    assert response.json() == {"message": f"Signed up {email} for {activity_name}"}
    assert email in app_module.activities[activity_name]["participants"]


def test_signup_rejects_duplicate_participant(client):
    activity_name = "Chess Club"
    email = "michael@mergington.edu"

    response = client.post(
        f"/activities/{quote(activity_name, safe='')}/signup",
        params={"email": email},
    )

    assert response.status_code == 400
    assert response.json() == {"detail": "Student already signed up"}


def test_signup_rejects_unknown_activity(client):
    response = client.post(
        f"/activities/{quote('Unknown Club', safe='')}/signup",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}
