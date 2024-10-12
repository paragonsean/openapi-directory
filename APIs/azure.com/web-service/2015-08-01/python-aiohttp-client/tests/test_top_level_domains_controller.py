# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.tld_legal_agreement_collection import TldLegalAgreementCollection
from openapi_server.models.top_level_domain import TopLevelDomain
from openapi_server.models.top_level_domain_agreement_option import TopLevelDomainAgreementOption
from openapi_server.models.top_level_domain_collection import TopLevelDomainCollection


pytestmark = pytest.mark.asyncio

async def test_top_level_domains_get_get_top_level_domains(client):
    """Test case for top_level_domains_get_get_top_level_domains

    Lists all top level domains supported for registration
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

async def test_top_level_domains_get_top_level_domain(client):
    """Test case for top_level_domains_get_top_level_domain

    Gets details of a top level domain
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

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_top_level_domains_list_top_level_domain_agreements(client):
    """Test case for top_level_domains_list_top_level_domain_agreements

    Lists legal agreements that user needs to accept before purchasing domain
    """
    agreement_option = {"includePrivacy":True}
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

