# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.rti_transaction_base import RtiTransactionBase


pytestmark = pytest.mark.asyncio

async def test_delete_rti_transaction(client):
    """Test case for delete_rti_transaction

    Delete the RTI transaction
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/RtiTransaction/{rti_transaction_id}'.format(employer_id='employer_id_example', rti_transaction_id='rti_transaction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_rti_transaction_tags_0(client):
    """Test case for get_all_rti_transaction_tags_0

    Get all RTI transaction tags
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/RtiTransactions/Tags'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rti_transaction_from_employer(client):
    """Test case for get_rti_transaction_from_employer

    Get the RTI transaction
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/RtiTransaction/{rti_transaction_id}'.format(employer_id='employer_id_example', rti_transaction_id='rti_transaction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rti_transaction_summaries_from_employer(client):
    """Test case for get_rti_transaction_summaries_from_employer

    Get all RTI transaction summaries for the employer
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/RtiTransactions/Summary'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rti_transaction_summary_from_employer(client):
    """Test case for get_rti_transaction_summary_from_employer

    Get the RTI transaction summary
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/RtiTransaction/{rti_transaction_id}/Summary'.format(employer_id='employer_id_example', rti_transaction_id='rti_transaction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rti_transactions_from_employer(client):
    """Test case for get_rti_transactions_from_employer

    Get all RTI transactions for the employer
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/RtiTransactions'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rti_transactions_with_tag_0(client):
    """Test case for get_rti_transactions_with_tag_0

    Get RTI transactions with tag
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/RtiTransactions/Tag/{tag_id}'.format(employer_id='employer_id_example', tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

