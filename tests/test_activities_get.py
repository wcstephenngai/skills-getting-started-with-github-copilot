def test_get_activities_returns_activity_dictionary(client):
    response = client.get("/activities")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data


def test_get_activities_items_have_expected_fields(client):
    response = client.get("/activities")

    assert response.status_code == 200
    activities = response.json()

    required_fields = {"description", "schedule", "max_participants", "participants"}
    for details in activities.values():
        assert required_fields.issubset(details.keys())
        assert isinstance(details["participants"], list)
        assert isinstance(details["max_participants"], int)
