import json
from api.app import app
import pytest

@pytest.mark.parametrize("input_data, expected_output", [
    ({"data": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]}, b"9"),  # Adjust the input_data accordingly
    # Add similar lines for each digit (0-9)
])
def test_post_predict(input_data, expected_output):
    response = app.test_client().post("/predict", json={"input_data": input_data})
    assert response.status_code == 200
    assert response.get_data() == expected_output
