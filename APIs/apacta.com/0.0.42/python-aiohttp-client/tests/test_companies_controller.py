# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.companies_company_id_companies_integration_feature_settings_get200_response import CompaniesCompanyIdCompaniesIntegrationFeatureSettingsGet200Response
from openapi_server.models.companies_company_id_companies_integration_feature_settings_post_request import CompaniesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest
from openapi_server.models.companies_company_id_form_templates_get200_response import CompaniesCompanyIdFormTemplatesGet200Response
from openapi_server.models.companies_company_id_get200_response import CompaniesCompanyIdGet200Response
from openapi_server.models.companies_company_id_integration_feature_settings_get200_response import CompaniesCompanyIdIntegrationFeatureSettingsGet200Response
from openapi_server.models.companies_company_id_integration_feature_settings_integration_feature_setting_id_get200_response import CompaniesCompanyIdIntegrationFeatureSettingsIntegrationFeatureSettingIdGet200Response
from openapi_server.models.companies_company_id_integration_settings_companies_integration_setting_id_get200_response import CompaniesCompanyIdIntegrationSettingsCompaniesIntegrationSettingIdGet200Response
from openapi_server.models.companies_company_id_integration_settings_get200_response import CompaniesCompanyIdIntegrationSettingsGet200Response
from openapi_server.models.companies_company_id_integration_settings_post_request import CompaniesCompanyIdIntegrationSettingsPostRequest
from openapi_server.models.companies_company_id_price_margins_price_margins_id_get200_response import CompaniesCompanyIdPriceMarginsPriceMarginsIdGet200Response
from openapi_server.models.companies_company_id_price_margins_price_margins_id_post_request import CompaniesCompanyIdPriceMarginsPriceMarginsIdPostRequest
from openapi_server.models.companies_get200_response import CompaniesGet200Response
from openapi_server.models.companies_subscription_self_service_get200_response import CompaniesSubscriptionSelfServiceGet200Response
from openapi_server.models.create_success_response import CreateSuccessResponse
from openapi_server.models.empty_success_response import EmptySuccessResponse
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.forbidden_error import ForbiddenError


pytestmark = pytest.mark.asyncio

async def test_companies_company_id_companies_integration_feature_settings_c_integration_feature_setting_id_get(client):
    """Test case for companies_company_id_companies_integration_feature_settings_c_integration_feature_setting_id_get

    View a company integration feature setting
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/companies/{company_id}/companies_integration_feature_settings/{c_integration_feature_setting_id}'.format(company_id='company_id_example', c_integration_feature_setting_id='c_integration_feature_setting_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_companies_company_id_companies_integration_feature_settings_c_integration_feature_setting_id_put(client):
    """Test case for companies_company_id_companies_integration_feature_settings_c_integration_feature_setting_id_put

    Edit a company integration feature setting
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/companies/{company_id}/companies_integration_feature_settings/{c_integration_feature_setting_id}'.format(company_id='company_id_example', c_integration_feature_setting_id='c_integration_feature_setting_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_companies_company_id_companies_integration_feature_settings_get(client):
    """Test case for companies_company_id_companies_integration_feature_settings_get

    List a company integration feature settings
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/companies/{company_id}/companies_integration_feature_settings'.format(company_id='company_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_companies_company_id_companies_integration_feature_settings_post(client):
    """Test case for companies_company_id_companies_integration_feature_settings_post

    Add a company integration feature setting
    """
    body = openapi_server.CompaniesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/companies/{company_id}/companies_integration_feature_settings'.format(company_id='company_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_companies_company_id_form_templates_form_template_id_delete(client):
    """Test case for companies_company_id_form_templates_form_template_id_delete

    Delete a form template company
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/companies/{company_id}/form_templates/{form_template_id}'.format(company_id='company_id_example', form_template_id='form_template_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_companies_company_id_form_templates_form_template_id_get(client):
    """Test case for companies_company_id_form_templates_form_template_id_get

    Get a company form template
    """
    params = [('id', 'id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/companies/{company_id}/form_templates/{form_template_id}'.format(company_id='company_id_example', form_template_id='form_template_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_companies_company_id_form_templates_get(client):
    """Test case for companies_company_id_form_templates_get

    Get a list of company form templates
    """
    params = [('form_template_id', 'form_template_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/companies/{company_id}/form_templates'.format(company_id='company_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_companies_company_id_get(client):
    """Test case for companies_company_id_get

    Details of 1 company
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/companies/{company_id}'.format(company_id='company_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_companies_company_id_integration_feature_settings_get(client):
    """Test case for companies_company_id_integration_feature_settings_get

    Get a list of integration feature settings
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/companies/{company_id}/integration_feature_settings'.format(company_id='company_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_companies_company_id_integration_feature_settings_integration_feature_setting_id_get(client):
    """Test case for companies_company_id_integration_feature_settings_integration_feature_setting_id_get

    Show details of 1 integration feature setting
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/companies/{company_id}/integration_feature_settings/{integration_feature_setting_id}'.format(company_id='company_id_example', integration_feature_setting_id='integration_feature_setting_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_companies_company_id_integration_settings_companies_integration_setting_id_delete(client):
    """Test case for companies_company_id_integration_settings_companies_integration_setting_id_delete

    Delete a company integration setting
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/companies/{company_id}/integration_settings/{companies_integration_setting_id}'.format(company_id='company_id_example', companies_integration_setting_id='companies_integration_setting_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_companies_company_id_integration_settings_companies_integration_setting_id_get(client):
    """Test case for companies_company_id_integration_settings_companies_integration_setting_id_get

    Get a company integration setting
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/companies/{company_id}/integration_settings/{companies_integration_setting_id}'.format(company_id='company_id_example', companies_integration_setting_id='companies_integration_setting_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_companies_company_id_integration_settings_companies_integration_setting_id_put(client):
    """Test case for companies_company_id_integration_settings_companies_integration_setting_id_put

    Edit a company integration setting
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/companies/{company_id}/integration_settings/{companies_integration_setting_id}'.format(company_id='company_id_example', companies_integration_setting_id='companies_integration_setting_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_companies_company_id_integration_settings_get(client):
    """Test case for companies_company_id_integration_settings_get

    Get a list of company integration settings
    """
    params = [('identifier', 'identifier_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/companies/{company_id}/integration_settings'.format(company_id='company_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_companies_company_id_integration_settings_post(client):
    """Test case for companies_company_id_integration_settings_post

    Add a company integration setting
    """
    body = openapi_server.CompaniesCompanyIdIntegrationSettingsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/companies/{company_id}/integration_settings'.format(company_id='company_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_companies_company_id_price_margins_price_margins_id_delete(client):
    """Test case for companies_company_id_price_margins_price_margins_id_delete

    Delete a company price margin
    """
    params = [('price_margin_id', 'price_margin_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/companies/{company_id}/price_margins/{price_margins_id}'.format(company_id='company_id_example', price_margins_id='price_margins_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_companies_company_id_price_margins_price_margins_id_get(client):
    """Test case for companies_company_id_price_margins_price_margins_id_get

    Get a list of company price margins
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/companies/{company_id}/price_margins/{price_margins_id}'.format(company_id='company_id_example', price_margins_id='price_margins_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_companies_company_id_price_margins_price_margins_id_post(client):
    """Test case for companies_company_id_price_margins_price_margins_id_post

    Add a company price margin
    """
    body = openapi_server.CompaniesCompanyIdPriceMarginsPriceMarginsIdPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/companies/{company_id}/price_margins/{price_margins_id}'.format(company_id='company_id_example', price_margins_id='price_margins_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_companies_get(client):
    """Test case for companies_get

    Get a list of companies
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/companies',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_companies_subscription_self_service_get(client):
    """Test case for companies_subscription_self_service_get

    URL for subscription selfservice
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/companies/subscription_self_service',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

