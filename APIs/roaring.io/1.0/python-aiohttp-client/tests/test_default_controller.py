# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.company_board_members_multi import CompanyBoardMembersMulti
from openapi_server.models.company_board_members_result import CompanyBoardMembersResult
from openapi_server.models.company_credit_decision_result import CompanyCreditDecisionResult
from openapi_server.models.company_economy_overview_multi import CompanyEconomyOverviewMulti
from openapi_server.models.company_economy_overview_result import CompanyEconomyOverviewResult
from openapi_server.models.company_event_request_body import CompanyEventRequestBody
from openapi_server.models.company_event_result import CompanyEventResult
from openapi_server.models.company_lookup_request_body import CompanyLookupRequestBody
from openapi_server.models.company_overview_multi import CompanyOverviewMulti
from openapi_server.models.company_overview_result import CompanyOverviewResult
from openapi_server.models.company_signatory_multi import CompanySignatoryMulti
from openapi_server.models.company_signatory_result import CompanySignatoryResult
from openapi_server.models.not_found import NotFound
from openapi_server.models.server_error import ServerError


pytestmark = pytest.mark.asyncio

async def test_company_board_members_get(client):
    """Test case for company_board_members_get

    
    """
    params = [('countryCode', 'country_code_example'),
                    ('companyId', 'company_id_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/company/1.0/company-board-members',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_company_board_members_post(client):
    """Test case for company_board_members_post

    
    """
    body = {"companyIds":["companyIds","companyIds"]}
    params = [('countryCode', 'country_code_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/company/1.0/company-board-members',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_company_credit_decision_get(client):
    """Test case for company_credit_decision_get

    
    """
    params = [('countryCode', 'country_code_example'),
                    ('companyId', 'company_id_example'),
                    ('template', 'template_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/company/1.0/company-credit-decision',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_company_economy_overview_get(client):
    """Test case for company_economy_overview_get

    
    """
    params = [('countryCode', 'country_code_example'),
                    ('companyId', 'company_id_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/company/1.0/company-economy-overview',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_company_economy_overview_post(client):
    """Test case for company_economy_overview_post

    
    """
    body = {"companyIds":["companyIds","companyIds"]}
    params = [('countryCode', 'country_code_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/company/1.0/company-economy-overview',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_company_event_post(client):
    """Test case for company_event_post

    
    """
    body = {"requests":[{"date":"date","companyId":"companyId"},{"date":"date","companyId":"companyId"}]}
    params = [('countryCode', 'country_code_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/company/1.0/company-event',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_company_overview_get(client):
    """Test case for company_overview_get

    
    """
    params = [('countryCode', 'country_code_example'),
                    ('companyId', 'company_id_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/company/1.0/company-overview',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_company_overview_post(client):
    """Test case for company_overview_post

    
    """
    body = {"companyIds":["companyIds","companyIds"]}
    params = [('countryCode', 'country_code_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/company/1.0/company-overview',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_company_signatory_get(client):
    """Test case for company_signatory_get

    
    """
    params = [('countryCode', 'country_code_example'),
                    ('companyId', 'company_id_example')]
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='GET',
        path='/company/1.0/company-signatory',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_company_signatory_post(client):
    """Test case for company_signatory_post

    
    """
    body = {"companyIds":["companyIds","companyIds"]}
    params = [('countryCode', 'country_code_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/company/1.0/company-signatory',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_company_simple_search_get(client):
    """Test case for company_simple_search_get

    
    """
    params = [('countryCode', 'country_code_example'),
                    ('companyName', 'company_name_example'),
                    ('town', 'town_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/company/1.0/company-simple-search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

