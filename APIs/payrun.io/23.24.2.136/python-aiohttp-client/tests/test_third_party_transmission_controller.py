# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.third_party_transaction import ThirdPartyTransaction


pytestmark = pytest.mark.asyncio

async def test_delete_third_party_transaction(client):
    """Test case for delete_third_party_transaction

    Delete third party transaction
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/ThirdPartyTransaction/{third_party_transaction_id}'.format(employer_id='employer_id_example', third_party_transaction_id='third_party_transaction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_third_party_transaction(client):
    """Test case for get_third_party_transaction

    Get a third party transaction
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/ThirdPartyTransaction/{third_party_transaction_id}'.format(employer_id='employer_id_example', third_party_transaction_id='third_party_transaction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_third_party_transactions(client):
    """Test case for get_third_party_transactions

    Get all third party transaction links
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/ThirdPartyTransactions'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

