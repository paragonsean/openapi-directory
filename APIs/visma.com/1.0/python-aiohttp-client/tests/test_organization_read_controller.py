# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.organization_details_output_model import OrganizationDetailsOutputModel
from openapi_server.models.organization_settings_model import OrganizationSettingsModel
from openapi_server.models.visma_financials_company_model import VismaFinancialsCompanyModel


pytestmark = pytest.mark.asyncio

async def test_organization_details_get_organization_details(client):
    """Test case for organization_details_get_organization_details

    Get the details of organization.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/organizationdetails',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organization_settings_get_organization_settings(client):
    """Test case for organization_settings_get_organization_settings

    Get the settings of organization.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/organizationsettings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_organizations_get_visma_financials_company_info(client):
    """Test case for organizations_get_visma_financials_company_info

    Get Visma.net Financials integration company information.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/integrations/vismafinancials/companyinformation',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

