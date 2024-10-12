# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.score_config_output import ScoreConfigOutput
from openapi_server.models.score_configs_output import ScoreConfigsOutput


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_score_config(client):
    """Test case for create_score_config

    Create Score Configurations
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'api-key': 'special-key',
    }
    data = {
        'country': 'country_example',
        'dataset_affiliations_and_insurances': 3.4,
        'dataset_alert_in_media': 3.4,
        'dataset_business_background': 3.4,
        'dataset_criminal_record': 3.4,
        'dataset_driving_licenses': 3.4,
        'dataset_international_background': 3.4,
        'dataset_legal_background': 3.4,
        'dataset_personal_identity': 3.4,
        'dataset_professional_background': 3.4,
        'dataset_taxes_and_finances': 3.4,
        'dataset_traffic_fines': 3.4,
        'dataset_vehicle_information': 3.4,
        'dataset_vehicle_permits': 3.4,
        'type': 'type_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/config',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_custom_type(client):
    """Test case for delete_custom_type

    Delete Custom Type
    """
    params = [('type', 'type_example'),
                    ('country', 'country_example')]
    headers = { 
        'api-key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/config',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_score_configs(client):
    """Test case for list_score_configs

    List Score Configurations
    """
    params = [('start_key', 'start_key_example')]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/config',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_custom_type(client):
    """Test case for update_custom_type

    Update Custom Type
    """
    headers = { 
        'Content-Type': 'application/x-www-form-urlencoded',
        'api-key': 'special-key',
    }
    data = {
        'country': 'country_example',
        'dataset_affiliations_and_insurances': 3.4,
        'dataset_alert_in_media': 3.4,
        'dataset_business_background': 3.4,
        'dataset_criminal_record': 3.4,
        'dataset_driving_licenses': 3.4,
        'dataset_international_background': 3.4,
        'dataset_legal_background': 3.4,
        'dataset_personal_identity': 3.4,
        'dataset_professional_background': 3.4,
        'dataset_taxes_and_finances': 3.4,
        'dataset_traffic_fines': 3.4,
        'dataset_vehicle_information': 3.4,
        'dataset_vehicle_permits': 3.4,
        'type': 'type_example'
        }
    response = await client.request(
        method='PUT',
        path='/v1/config',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

