# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_applicant_delete_attributes_v2(client):
    """Test case for applicant_delete_attributes_v2

    Deletes a custom attribute for an applicant.
    """
    params = [('email', 'email_example'),
                    ('name', 'name_example'),
                    ('pool', 'pool_example'),
                    ('commonAppYear', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/applicant/attributes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applicant_get_attribute_names_v2(client):
    """Test case for applicant_get_attribute_names_v2

    Gets the custom applicant attributes used by the organization.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/applicant/attributes/names',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_applicant_get_attributes_v2(client):
    """Test case for applicant_get_attributes_v2

    Gets the custom attributes for an applicant.
    """
    params = [('email', 'email_example'),
                    ('pool', 'pool_example'),
                    ('commonAppYear', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/applicant/attributes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_applicant_post_attributes_v2(client):
    """Test case for applicant_post_attributes_v2

    Updates the custom attributes for an applicant.
    """
    data = {'key': 'data_example'}
    params = [('email', 'email_example'),
                    ('pool', 'pool_example'),
                    ('commonAppYear', 56)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/applicant/attributes',
        headers=headers,
        json=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

