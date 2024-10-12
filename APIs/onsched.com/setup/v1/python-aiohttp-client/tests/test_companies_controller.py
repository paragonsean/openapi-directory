# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.company_domain_input_model import CompanyDomainInputModel
from openapi_server.models.company_domain_list_view_model import CompanyDomainListViewModel
from openapi_server.models.company_domain_update_model import CompanyDomainUpdateModel
from openapi_server.models.company_domain_view_model import CompanyDomainViewModel
from openapi_server.models.company_input_model import CompanyInputModel
from openapi_server.models.company_update_model import CompanyUpdateModel
from openapi_server.models.company_view_model import CompanyViewModel
from openapi_server.models.content_result import ContentResult
from openapi_server.models.email_template_list_view_model import EmailTemplateListViewModel
from openapi_server.models.master_email_template_settings_view_model import MasterEmailTemplateSettingsViewModel
from openapi_server.models.master_template_settings_input_model import MasterTemplateSettingsInputModel
from openapi_server.models.region_input_model import RegionInputModel
from openapi_server.models.region_list_view_model import RegionListViewModel
from openapi_server.models.region_update_model import RegionUpdateModel
from openapi_server.models.region_view_model import RegionViewModel
from openapi_server.models.timezone_view_model import TimezoneViewModel


pytestmark = pytest.mark.asyncio

async def test_setup_v1_companies_domains_get(client):
    """Test case for setup_v1_companies_domains_get

    List Company Domains
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/companies/domains',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_companies_domains_id_delete(client):
    """Test case for setup_v1_companies_domains_id_delete

    Delete Company Domain
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/setup/v1/companies/domains/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_companies_domains_id_get(client):
    """Test case for setup_v1_companies_domains_id_get

    Get Company Domain
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/companies/domains/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_companies_domains_id_put(client):
    """Test case for setup_v1_companies_domains_id_put

    Update Company Domain
    """
    body = {"domain":"domain"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/setup/v1/companies/domains/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_companies_domains_post(client):
    """Test case for setup_v1_companies_domains_post

    Create Company Domain
    """
    body = {"domain":"domain"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/v1/companies/domains',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_companies_email_templates_get(client):
    """Test case for setup_v1_companies_email_templates_get

    List Email Templates
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/companies/email/templates',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_companies_email_templates_master_delete(client):
    """Test case for setup_v1_companies_email_templates_master_delete

    Delete Master Template Settings
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/setup/v1/companies/email/templates/master',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_companies_email_templates_master_get(client):
    """Test case for setup_v1_companies_email_templates_master_get

    Get Master Template Settings
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/companies/email/templates/master',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_companies_email_templates_master_post(client):
    """Test case for setup_v1_companies_email_templates_master_post

    Create Master Template Settings
    """
    body = {"centerEmailContent":True,"footerFontSize":"footerFontSize","footerPanelWebsiteContact":True,"centerEmailContentPanel":True,"showHeaderPanel":True,"privacyPolicyLink":"privacyPolicyLink","footerLogoHeight":"footerLogoHeight","panelBackgroundColor":"panelBackgroundColor","headerLogoHeight":"headerLogoHeight","footerLogoPadding":"footerLogoPadding","panelLinkColor":"panelLinkColor","showContentPanel":True,"contentBackgroundColor":"contentBackgroundColor","footerPanelPhoneContact":True,"headerLogoPadding":"headerLogoPadding","panelColor":"panelColor","centerEmailFooter":True,"emailColor":"emailColor","showHeaderLogo":True,"contentColor":"contentColor","showFooterLogo":True,"emailBackgroundColor":"emailBackgroundColor","footerPanelEmailContact":True,"emailLinkColor":"emailLinkColor","showFooterPanel":True,"contentLinkColor":"contentLinkColor"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/v1/companies/email/templates/master',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_companies_email_templates_template_name_get(client):
    """Test case for setup_v1_companies_email_templates_template_name_get

    Get Email Template
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/companies/email/templates/{template_name}'.format(template_name='template_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_companies_get(client):
    """Test case for setup_v1_companies_get

    Get Company
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/companies',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_companies_post(client):
    """Test case for setup_v1_companies_post

    Create Company
    """
    body = {"country":"country","website":"website","disableEmailAndSmsNotifications":True,"city":"city","postalCode":"postalCode","bookingWebhookUrl":"bookingWebhookUrl","notificationFromName":"notificationFromName","reminderWebhookUrl":"reminderWebhookUrl","phone":"phone","notificationFromEmailAddress":"notificationFromEmailAddress","resourceWebhookUrl":"resourceWebhookUrl","name":"name","webhookSignatureHash":"webhookSignatureHash","addressLine1":"addressLine1","timezoneName":"timezoneName","addressLine2":"addressLine2","state":"state","customerWebhookUrl":"customerWebhookUrl","fax":"fax","email":"email","registrationEmail":"registrationEmail"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/v1/companies',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_companies_put(client):
    """Test case for setup_v1_companies_put

    Update Company
    """
    body = {"country":"country","website":"website","disableEmailAndSmsNotifications":True,"city":"city","postalCode":"postalCode","bookingWebhookUrl":"bookingWebhookUrl","notificationFromName":"notificationFromName","reminderWebhookUrl":"reminderWebhookUrl","phone":"phone","notificationFromEmailAddress":"notificationFromEmailAddress","resourceWebhookUrl":"resourceWebhookUrl","name":"name","webhookSignatureHash":"webhookSignatureHash","addressLine1":"addressLine1","timezoneName":"timezoneName","addressLine2":"addressLine2","state":"state","customerWebhookUrl":"customerWebhookUrl","fax":"fax","email":"email","registrationEmail":"registrationEmail"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/setup/v1/companies',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_companies_regions_get(client):
    """Test case for setup_v1_companies_regions_get

    List Regions
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/companies/regions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_companies_regions_id_delete(client):
    """Test case for setup_v1_companies_regions_id_delete

    Delete Region
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/setup/v1/companies/regions/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_companies_regions_id_get(client):
    """Test case for setup_v1_companies_regions_id_get

    Get Region
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/companies/regions/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_companies_regions_id_put(client):
    """Test case for setup_v1_companies_regions_id_put

    Update Region
    """
    body = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/setup/v1/companies/regions/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_companies_regions_post(client):
    """Test case for setup_v1_companies_regions_post

    Create Region
    """
    body = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/v1/companies/regions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_companies_timezones_date_get(client):
    """Test case for setup_v1_companies_timezones_date_get

    List Time Zones
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/companies/timezones/{_date}'.format(_date='2013-10-20T19:20:30+01:00'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

