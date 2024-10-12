# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bundle_enum_end_user_type import BundleEnumEndUserType
from openapi_server.models.bundle_enum_sort_by import BundleEnumSortBy
from openapi_server.models.bundle_enum_sort_direction import BundleEnumSortDirection
from openapi_server.models.bundle_enum_status import BundleEnumStatus
from openapi_server.models.list_bundle_response import ListBundleResponse
from openapi_server.models.numbers_v2_regulatory_compliance_bundle import NumbersV2RegulatoryComplianceBundle


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_bundle(client):
    """Test case for create_bundle

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'email': 'email_example',
        'end_user_type': openapi_server.BundleEnumEndUserType(),
        'friendly_name': 'friendly_name_example',
        'iso_country': 'iso_country_example',
        'number_type': 'number_type_example',
        'regulation_sid': 'regulation_sid_example',
        'status_callback': 'status_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/RegulatoryCompliance/Bundles',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_bundle(client):
    """Test case for delete_bundle

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/RegulatoryCompliance/Bundles/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_bundle(client):
    """Test case for fetch_bundle

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/RegulatoryCompliance/Bundles/{sid}'.format(sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_bundle(client):
    """Test case for list_bundle

    
    """
    params = [('Status', openapi_server.BundleEnumStatus()),
                    ('FriendlyName', 'friendly_name_example'),
                    ('RegulationSid', 'regulation_sid_example'),
                    ('IsoCountry', 'iso_country_example'),
                    ('NumberType', 'number_type_example'),
                    ('HasValidUntilDate', True),
                    ('SortBy', openapi_server.BundleEnumSortBy()),
                    ('SortDirection', openapi_server.BundleEnumSortDirection()),
                    ('ValidUntilDate', '2013-10-20T19:20:30+01:00'),
                    ('ValidUntilDate&lt;', '2013-10-20T19:20:30+01:00'),
                    ('ValidUntilDate&gt;', '2013-10-20T19:20:30+01:00'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/RegulatoryCompliance/Bundles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_bundle(client):
    """Test case for update_bundle

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'email': 'email_example',
        'friendly_name': 'friendly_name_example',
        'status': openapi_server.BundleEnumStatus(),
        'status_callback': 'status_callback_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/RegulatoryCompliance/Bundles/{sid}'.format(sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

