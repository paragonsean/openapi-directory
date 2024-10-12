# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tenant import Tenant


pytestmark = pytest.mark.asyncio

async def test_configuration_add(client):
    """Test case for configuration_add

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.ADHybridHealthService/configuration',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_configuration_get(client):
    """Test case for configuration_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.ADHybridHealthService/configuration',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_configuration_update(client):
    """Test case for configuration_update

    
    """
    tenant = {"onboarded":True,"disabledReason":6,"privatePreviewTenant":True,"aadPremium":True,"alertSuppressionTimeInMins":0,"lastDisabled":"2000-01-23T04:56:07.000+00:00","agentAutoUpdate":True,"consentedToMicrosoftDevOps":True,"lastVerified":"2000-01-23T04:56:07.000+00:00","initialDomain":"initialDomain","devOpsTtl":"2000-01-23T04:56:07.000+00:00","createdDate":"2000-01-23T04:56:07.000+00:00","tenantInQuarantine":True,"tenantName":"tenantName","countryLetterCode":"countryLetterCode","onboardingAllowed":True,"globalAdminsEmail":["globalAdminsEmail","globalAdminsEmail"],"tenantId":"tenantId","disabled":True,"aadLicense":"aadLicense","pksCertificate":"{}"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/providers/Microsoft.ADHybridHealthService/configuration',
        headers=headers,
        json=tenant,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

