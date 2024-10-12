# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.history_item import HistoryItem
from openapi_server.models.history_item_update import HistoryItemUpdate
from openapi_server.models.paginated_response_of_history_item import PaginatedResponseOfHistoryItem
from openapi_server.models.visibility import Visibility


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_add_item(client):
    """Test case for add_item

    Add history item
    """
    body = {"organizationId":"org.acme","visibility":{"public":True,"sharedOrganizationIds":["de.acme","com.porsche","de.bluerain"]},"ownerOrganizationId":"de.bluerain","additionalProperties":{"key":"additionalProperties"},"type":"DISPATCHED","sequenceId":9784,"timestamp":1517232722}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/history/{id4n}'.format(id4n='id4n_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_filtered_list(client):
    """Test case for filtered_list

    List history
    """
    params = [('includePrivate', True),
                    ('organization', 'organization_example'),
                    ('type', ['type_example']),
                    ('qualifier', ['qualifier_example']),
                    ('fromDate', '2013-10-20T19:20:30+01:00'),
                    ('toDate', '2013-10-20T19:20:30+01:00'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/history/{id4n}'.format(id4n='id4n_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list(client):
    """Test case for list

    DEPRECATED - List history
    """
    params = [('includePrivate', True),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/history/{id4n}/{organization_id}'.format(id4n='id4n_example', organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_item(client):
    """Test case for retrieve_item

    Get history item
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/history/{id4n}/{organization_id}/{sequence_id}'.format(id4n='id4n_example', organization_id='organization_id_example', sequence_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_item(client):
    """Test case for update_item

    Update history item
    """
    body = {"organizationId":"de.acme","visibility":{"public":True,"sharedOrganizationIds":["de.acme","com.porsche","de.bluerain"]}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v1/history/{id4n}/{organization_id}/{sequence_id}'.format(id4n='id4n_example', organization_id='organization_id_example', sequence_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_item_visibility(client):
    """Test case for update_item_visibility

    Set history item visibility
    """
    body = {"public":True,"sharedOrganizationIds":["de.acme","com.porsche","de.bluerain"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/history/{id4n}/{organization_id}/{sequence_id}/visibility'.format(id4n='id4n_example', organization_id='organization_id_example', sequence_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

