import json

import pytest as pytest

from sample_service.app import app


@pytest.mark.asyncio
async def test_can_get_organizations():
    response = await app.test_client().get("api/v1/organizations")
    assert response.status_code == 200

    response_data = json.loads(await response.get_data())
    assert len(response_data) == 1

    organization = response_data[0]

    assert organization["id"] == "org1"
    assert organization["name"] == "Org 1"
    assert organization["documentType"] == "organization"
