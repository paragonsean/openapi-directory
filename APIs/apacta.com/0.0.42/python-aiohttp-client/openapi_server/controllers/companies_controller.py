from typing import List, Dict
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
from openapi_server import util


async def companies_company_id_companies_integration_feature_settings_c_integration_feature_setting_id_get(request: web.Request, company_id, c_integration_feature_setting_id) -> web.Response:
    """View a company integration feature setting

    

    :param company_id: 
    :type company_id: str
    :param c_integration_feature_setting_id: 
    :type c_integration_feature_setting_id: str

    """
    return web.Response(status=200)


async def companies_company_id_companies_integration_feature_settings_c_integration_feature_setting_id_put(request: web.Request, company_id, c_integration_feature_setting_id) -> web.Response:
    """Edit a company integration feature setting

    

    :param company_id: 
    :type company_id: str
    :param c_integration_feature_setting_id: 
    :type c_integration_feature_setting_id: str

    """
    return web.Response(status=200)


async def companies_company_id_companies_integration_feature_settings_get(request: web.Request, company_id) -> web.Response:
    """List a company integration feature settings

    

    :param company_id: 
    :type company_id: str

    """
    return web.Response(status=200)


async def companies_company_id_companies_integration_feature_settings_post(request: web.Request, company_id, body=None) -> web.Response:
    """Add a company integration feature setting

    

    :param company_id: 
    :type company_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CompaniesCompanyIdCompaniesIntegrationFeatureSettingsPostRequest.from_dict(body)
    return web.Response(status=200)


async def companies_company_id_form_templates_form_template_id_delete(request: web.Request, company_id, form_template_id) -> web.Response:
    """Delete a form template company

    

    :param company_id: 
    :type company_id: str
    :param form_template_id: Automatically added
    :type form_template_id: str

    """
    return web.Response(status=200)


async def companies_company_id_form_templates_form_template_id_get(request: web.Request, company_id, id, form_template_id) -> web.Response:
    """Get a company form template

    

    :param company_id: 
    :type company_id: str
    :param id: 
    :type id: str
    :param form_template_id: Automatically added
    :type form_template_id: str

    """
    return web.Response(status=200)


async def companies_company_id_form_templates_get(request: web.Request, company_id, form_template_id) -> web.Response:
    """Get a list of company form templates

    

    :param company_id: 
    :type company_id: str
    :param form_template_id: 
    :type form_template_id: str

    """
    return web.Response(status=200)


async def companies_company_id_get(request: web.Request, company_id) -> web.Response:
    """Details of 1 company

    

    :param company_id: 
    :type company_id: str

    """
    return web.Response(status=200)


async def companies_company_id_integration_feature_settings_get(request: web.Request, company_id) -> web.Response:
    """Get a list of integration feature settings

    

    :param company_id: 
    :type company_id: str

    """
    return web.Response(status=200)


async def companies_company_id_integration_feature_settings_integration_feature_setting_id_get(request: web.Request, company_id, integration_feature_setting_id) -> web.Response:
    """Show details of 1 integration feature setting

    

    :param company_id: 
    :type company_id: str
    :param integration_feature_setting_id: 
    :type integration_feature_setting_id: str

    """
    return web.Response(status=200)


async def companies_company_id_integration_settings_companies_integration_setting_id_delete(request: web.Request, company_id, companies_integration_setting_id) -> web.Response:
    """Delete a company integration setting

    

    :param company_id: 
    :type company_id: str
    :param companies_integration_setting_id: 
    :type companies_integration_setting_id: str

    """
    return web.Response(status=200)


async def companies_company_id_integration_settings_companies_integration_setting_id_get(request: web.Request, company_id, companies_integration_setting_id) -> web.Response:
    """Get a company integration setting

    

    :param company_id: 
    :type company_id: str
    :param companies_integration_setting_id: 
    :type companies_integration_setting_id: str

    """
    return web.Response(status=200)


async def companies_company_id_integration_settings_companies_integration_setting_id_put(request: web.Request, company_id, companies_integration_setting_id) -> web.Response:
    """Edit a company integration setting

    

    :param company_id: 
    :type company_id: str
    :param companies_integration_setting_id: 
    :type companies_integration_setting_id: str

    """
    return web.Response(status=200)


async def companies_company_id_integration_settings_get(request: web.Request, company_id, identifier=None) -> web.Response:
    """Get a list of company integration settings

    

    :param company_id: 
    :type company_id: str
    :param identifier: The identifier of an ERP integration
    :type identifier: str

    """
    return web.Response(status=200)


async def companies_company_id_integration_settings_post(request: web.Request, company_id, body=None) -> web.Response:
    """Add a company integration setting

    

    :param company_id: 
    :type company_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CompaniesCompanyIdIntegrationSettingsPostRequest.from_dict(body)
    return web.Response(status=200)


async def companies_company_id_price_margins_price_margins_id_delete(request: web.Request, company_id, price_margin_id, price_margins_id) -> web.Response:
    """Delete a company price margin

    

    :param company_id: 
    :type company_id: str
    :param price_margin_id: 
    :type price_margin_id: str
    :param price_margins_id: Automatically added
    :type price_margins_id: str

    """
    return web.Response(status=200)


async def companies_company_id_price_margins_price_margins_id_get(request: web.Request, company_id, price_margins_id) -> web.Response:
    """Get a list of company price margins

    

    :param company_id: 
    :type company_id: str
    :param price_margins_id: Automatically added
    :type price_margins_id: str

    """
    return web.Response(status=200)


async def companies_company_id_price_margins_price_margins_id_post(request: web.Request, company_id, price_margins_id, body=None) -> web.Response:
    """Add a company price margin

    

    :param company_id: 
    :type company_id: str
    :param price_margins_id: Automatically added
    :type price_margins_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CompaniesCompanyIdPriceMarginsPriceMarginsIdPostRequest.from_dict(body)
    return web.Response(status=200)


async def companies_get(request: web.Request, ) -> web.Response:
    """Get a list of companies

    


    """
    return web.Response(status=200)


async def companies_subscription_self_service_get(request: web.Request, ) -> web.Response:
    """URL for subscription selfservice

    


    """
    return web.Response(status=200)
