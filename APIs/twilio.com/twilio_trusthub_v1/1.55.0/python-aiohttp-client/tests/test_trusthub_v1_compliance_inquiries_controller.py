# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.trusthub_v1_compliance_inquiry import TrusthubV1ComplianceInquiry


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_compliance_inquiry(client):
    """Test case for create_compliance_inquiry

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'notification_email': 'notification_email_example',
        'primary_profile_sid': 'primary_profile_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/ComplianceInquiries/Customers/Initialize',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_compliance_inquiry(client):
    """Test case for update_compliance_inquiry

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'primary_profile_sid': 'primary_profile_sid_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/ComplianceInquiries/Customers/{customer_id}/Initialize'.format(customer_id='customer_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

