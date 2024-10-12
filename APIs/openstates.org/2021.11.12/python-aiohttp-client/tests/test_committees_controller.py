# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.committee import Committee
from openapi_server.models.committee_classification import CommitteeClassification
from openapi_server.models.committee_include import CommitteeInclude
from openapi_server.models.committee_list import CommitteeList
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.org_classification import OrgClassification


pytestmark = pytest.mark.asyncio

async def test_committee_detail_committees_committee_id_get(client):
    """Test case for committee_detail_committees_committee_id_get

    Committee Detail
    """
    params = [('include', []),
                    ('apikey', 'apikey_example')]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/committees/{committee_id}'.format(committee_id='committee_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_committee_list_committees_get(client):
    """Test case for committee_list_committees_get

    Committee List
    """
    params = [('jurisdiction', 'jurisdiction_example'),
                    ('classification', openapi_server.CommitteeClassification()),
                    ('parent', 'parent_example'),
                    ('chamber', openapi_server.OrgClassification()),
                    ('include', []),
                    ('apikey', 'apikey_example'),
                    ('page', 1),
                    ('per_page', 20)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/committees',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

