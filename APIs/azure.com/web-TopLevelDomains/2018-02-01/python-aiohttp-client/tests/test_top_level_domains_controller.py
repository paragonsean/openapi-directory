# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tld_legal_agreement_collection import TldLegalAgreementCollection
from openapi_server.models.top_level_domain import TopLevelDomain
from openapi_server.models.top_level_domain_agreement_option import TopLevelDomainAgreementOption
from openapi_server.models.top_level_domain_collection import TopLevelDomainCollection
from openapi_server.models.top_level_domains_list_default_response import TopLevelDomainsListDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_top_level_domains_get(client):
    """Test case for top_level_domains_get

    Get details of a top-level domain.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DomainRegistration/topLevelDomains/{name}'.format(name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_top_level_domains_list(client):
    """Test case for top_level_domains_list

    Get all top-level domains supported for registration.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DomainRegistration/topLevelDomains'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_top_level_domains_list_agreements(client):
    """Test case for top_level_domains_list_agreements

    Gets all legal agreements that user needs to accept before purchasing a domain.
    """
    agreement_option = {"forTransfer":True,"includePrivacy":True}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.DomainRegistration/topLevelDomains/{name}/listAgreements'.format(name='name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=agreement_option,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

