# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.appointment_reminder_view_model import AppointmentReminderViewModel
from openapi_server.models.appointment_reminders_input_model import AppointmentRemindersInputModel
from openapi_server.models.business_service_list_view_model import BusinessServiceListViewModel
from openapi_server.models.business_service_view_model import BusinessServiceViewModel
from openapi_server.models.content_result import ContentResult
from openapi_server.models.email_template_input_model import EmailTemplateInputModel
from openapi_server.models.email_template_list_view_model import EmailTemplateListViewModel
from openapi_server.models.google_service_account_creds import GoogleServiceAccountCreds
from openapi_server.models.location_input_model import LocationInputModel
from openapi_server.models.location_list_view_model import LocationListViewModel
from openapi_server.models.location_update_model import LocationUpdateModel
from openapi_server.models.location_view_model import LocationViewModel
from openapi_server.models.locations_input_model import LocationsInputModel
from openapi_server.models.master_email_template_settings_view_model import MasterEmailTemplateSettingsViewModel
from openapi_server.models.master_template_settings_input_model import MasterTemplateSettingsInputModel
from openapi_server.models.resource_image_input_model import ResourceImageInputModel


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_locations_bulk_post(client):
    """Test case for setup_v1_locations_bulk_post

    Create Locations Bulk
    """
    body = {"locations":[{"settings":{"bookAheadValue":7,"enableWorldTimezones":True,"bookInAdvance":1,"bookAheadUnit":4,"customerBookingsPerDay":1,"bookingTimerMins":1},"website":"website","address":{"country":"country","city":"city","postalCode":"postalCode","addressLine1":"addressLine1","addressLine2":"addressLine2","state":"state"},"businessHours":{"thu":{"isOpen":True,"is24Hours":True,"startTime":2,"endTime":3},"tue":{"isOpen":True,"is24Hours":True,"startTime":2,"endTime":3},"sat":{"isOpen":True,"is24Hours":True,"startTime":2,"endTime":3},"wed":{"isOpen":True,"is24Hours":True,"startTime":2,"endTime":3},"fri":{"isOpen":True,"is24Hours":True,"startTime":2,"endTime":3},"mon":{"isOpen":True,"is24Hours":True,"startTime":2,"endTime":3},"sun":{"isOpen":True,"is24Hours":True,"startTime":2,"endTime":3}},"adminName":"adminName","friendlyId":"friendlyId","appointmentReminders":{"emailFirstReminderInterval":6,"emailSecondReminderInterval":5,"smsSecondReminder":7,"smsSecondReminderInterval":9,"smsFirstReminder":5,"emailFirstReminder":0,"smsFirstReminderInterval":2,"emailSecondReminder":1},"defaults":{"customerState":True,"businessNotification":True,"emailInfo":True,"enableUtcTimezone":True,"customerCity":True,"autoUpdateCustomer":True},"phone":"phone","regionId":"regionId","name":"name","timezoneName":"timezoneName","fax":"fax","email":"email","adminEmail":"adminEmail"},{"settings":{"bookAheadValue":7,"enableWorldTimezones":True,"bookInAdvance":1,"bookAheadUnit":4,"customerBookingsPerDay":1,"bookingTimerMins":1},"website":"website","address":{"country":"country","city":"city","postalCode":"postalCode","addressLine1":"addressLine1","addressLine2":"addressLine2","state":"state"},"businessHours":{"thu":{"isOpen":True,"is24Hours":True,"startTime":2,"endTime":3},"tue":{"isOpen":True,"is24Hours":True,"startTime":2,"endTime":3},"sat":{"isOpen":True,"is24Hours":True,"startTime":2,"endTime":3},"wed":{"isOpen":True,"is24Hours":True,"startTime":2,"endTime":3},"fri":{"isOpen":True,"is24Hours":True,"startTime":2,"endTime":3},"mon":{"isOpen":True,"is24Hours":True,"startTime":2,"endTime":3},"sun":{"isOpen":True,"is24Hours":True,"startTime":2,"endTime":3}},"adminName":"adminName","friendlyId":"friendlyId","appointmentReminders":{"emailFirstReminderInterval":6,"emailSecondReminderInterval":5,"smsSecondReminder":7,"smsSecondReminderInterval":9,"smsFirstReminder":5,"emailFirstReminder":0,"smsFirstReminderInterval":2,"emailSecondReminder":1},"defaults":{"customerState":True,"businessNotification":True,"emailInfo":True,"enableUtcTimezone":True,"customerCity":True,"autoUpdateCustomer":True},"phone":"phone","regionId":"regionId","name":"name","timezoneName":"timezoneName","fax":"fax","email":"email","adminEmail":"adminEmail"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/v1/locations/bulk',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_locations_get(client):
    """Test case for setup_v1_locations_get

    List Locations
    """
    params = [('name', 'name_example'),
                    ('serviceId', 'service_id_example'),
                    ('friendlyId', 'friendly_id_example'),
                    ('deleted', True),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/locations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_locations_id_appointmentreminders_get(client):
    """Test case for setup_v1_locations_id_appointmentreminders_get

    Get Reminders
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/locations/{id}/appointmentreminders'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_locations_id_appointmentreminders_put(client):
    """Test case for setup_v1_locations_id_appointmentreminders_put

    Update Reminders
    """
    body = {"emailFirstReminderInterval":6,"emailSecondReminderInterval":5,"smsSecondReminder":7,"smsSecondReminderInterval":9,"smsFirstReminder":5,"emailFirstReminder":0,"smsFirstReminderInterval":2,"emailSecondReminder":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/setup/v1/locations/{id}/appointmentreminders'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_locations_id_delete(client):
    """Test case for setup_v1_locations_id_delete

    Delete Location
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/setup/v1/locations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_locations_id_deleteallimages_delete(client):
    """Test case for setup_v1_locations_id_deleteallimages_delete

    Delete All Location Images
    """
    params = [('uppercase', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/setup/v1/locations/{id}/deleteallimages'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_locations_id_deleteimage_delete(client):
    """Test case for setup_v1_locations_id_deleteimage_delete

    Delete Location Image
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/setup/v1/locations/{id}/deleteimage'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_locations_id_email_templates_get(client):
    """Test case for setup_v1_locations_id_email_templates_get

    List Email Templates
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/locations/{id}/email/templates'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_locations_id_email_templates_master_delete(client):
    """Test case for setup_v1_locations_id_email_templates_master_delete

    Delete Master Template Settings
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/setup/v1/locations/{id}/email/templates/master'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_locations_id_email_templates_master_get(client):
    """Test case for setup_v1_locations_id_email_templates_master_get

    Get Master Template Settings
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/locations/{id}/email/templates/master'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_locations_id_email_templates_master_post(client):
    """Test case for setup_v1_locations_id_email_templates_master_post

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
        path='/setup/v1/locations/{id}/email/templates/master'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_locations_id_email_templates_post(client):
    """Test case for setup_v1_locations_id_email_templates_post

    Create Custom Template
    """
    body = {"templateName":"templateName","templateContent":"templateContent"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/v1/locations/{id}/email/templates'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_locations_id_email_templates_template_name_delete(client):
    """Test case for setup_v1_locations_id_email_templates_template_name_delete

    Delete Custom Template
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/setup/v1/locations/{id}/email/templates/{template_name}'.format(id='id_example', template_name='template_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_locations_id_email_templates_template_name_get(client):
    """Test case for setup_v1_locations_id_email_templates_template_name_get

    Get Email Template
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/locations/{id}/email/templates/{template_name}'.format(id='id_example', template_name='template_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_locations_id_get(client):
    """Test case for setup_v1_locations_id_get

    Get Location
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/locations/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_locations_id_google_service_account_delete(client):
    """Test case for setup_v1_locations_id_google_service_account_delete

    Delete Google Cal Access
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/setup/v1/locations/{id}/google/service/account'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_locations_id_google_service_account_post(client):
    """Test case for setup_v1_locations_id_google_service_account_post

    Create Google Cal Access
    """
    body = {"token_uri":"token_uri","client_x509_cert_url":"client_x509_cert_url","private_key_id":"private_key_id","project_id":"project_id","auth_provider_x509_cert_url":"auth_provider_x509_cert_url","auth_uri":"auth_uri","client_email":"client_email","private_key":"private_key","type":"type","client_id":"client_id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/v1/locations/{id}/google/service/account'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_locations_id_holidays_holiday_id_closed_put(client):
    """Test case for setup_v1_locations_id_holidays_holiday_id_closed_put

    Update Location Holidays
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/setup/v1/locations/{id}/holidays/{holiday_id}/{closed}'.format(id='id_example', holiday_id='holiday_id_example', closed=True),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_locations_id_put(client):
    """Test case for setup_v1_locations_id_put

    Update Location
    """
    body = {"settings":{"bookAheadValue":6,"enableWorldTimezones":True,"bookInAdvance":1,"bookAheadUnit":0,"customerBookingsPerDay":5,"bookingTimerMins":5},"website":"website","address":{"country":"country","city":"city","postalCode":"postalCode","addressLine1":"addressLine1","addressLine2":"addressLine2","state":"state"},"businessHours":{"thu":{"isOpen":True,"is24Hours":True,"startTime":2,"endTime":3},"tue":{"isOpen":True,"is24Hours":True,"startTime":2,"endTime":3},"sat":{"isOpen":True,"is24Hours":True,"startTime":2,"endTime":3},"wed":{"isOpen":True,"is24Hours":True,"startTime":2,"endTime":3},"fri":{"isOpen":True,"is24Hours":True,"startTime":2,"endTime":3},"mon":{"isOpen":True,"is24Hours":True,"startTime":2,"endTime":3},"sun":{"isOpen":True,"is24Hours":True,"startTime":2,"endTime":3}},"adminName":"adminName","friendlyId":"friendlyId","appointmentReminders":{"emailFirstReminderInterval":6,"emailSecondReminderInterval":5,"smsSecondReminder":7,"smsSecondReminderInterval":9,"smsFirstReminder":5,"emailFirstReminder":0,"smsFirstReminderInterval":2,"emailSecondReminder":1},"defaults":{"customerState":True,"businessNotification":True,"emailInfo":True,"enableUtcTimezone":True,"customerCity":True,"autoUpdateCustomer":True},"phone":"phone","regionId":"regionId","name":"name","timezoneName":"timezoneName","fax":"fax","email":"email","adminEmail":"adminEmail"}
    params = [('removeRegion', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/setup/v1/locations/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_locations_id_recover_put(client):
    """Test case for setup_v1_locations_id_recover_put

    Recover Location
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/setup/v1/locations/{id}/recover'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_locations_id_services_delete(client):
    """Test case for setup_v1_locations_id_services_delete

    Delete Linked Services
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/setup/v1/locations/{id}/services'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_locations_id_services_get(client):
    """Test case for setup_v1_locations_id_services_get

    List Location Linked Services
    """
    params = [('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/locations/{id}/services'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_locations_id_services_post(client):
    """Test case for setup_v1_locations_id_services_post

    Create Linked Service
    """
    body = ['body_example']
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/v1/locations/{id}/services'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_locations_id_settings_scope_settings_scope_put(client):
    """Test case for setup_v1_locations_id_settings_scope_settings_scope_put

    Update Location Scope
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/setup/v1/locations/{id}/settings/scope/{settings_scope}'.format(id='id_example', settings_scope='settings_scope_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_locations_id_uploadimage_post(client):
    """Test case for setup_v1_locations_id_uploadimage_post

    Upload Location Image
    """
    body = {"imageFileData":"imageFileData","imageFileName":"imageFileName"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/v1/locations/{id}/uploadimage'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_setup_v1_locations_post(client):
    """Test case for setup_v1_locations_post

    Create Location
    """
    body = {"settings":{"bookAheadValue":7,"enableWorldTimezones":True,"bookInAdvance":1,"bookAheadUnit":4,"customerBookingsPerDay":1,"bookingTimerMins":1},"website":"website","address":{"country":"country","city":"city","postalCode":"postalCode","addressLine1":"addressLine1","addressLine2":"addressLine2","state":"state"},"businessHours":{"thu":{"isOpen":True,"is24Hours":True,"startTime":2,"endTime":3},"tue":{"isOpen":True,"is24Hours":True,"startTime":2,"endTime":3},"sat":{"isOpen":True,"is24Hours":True,"startTime":2,"endTime":3},"wed":{"isOpen":True,"is24Hours":True,"startTime":2,"endTime":3},"fri":{"isOpen":True,"is24Hours":True,"startTime":2,"endTime":3},"mon":{"isOpen":True,"is24Hours":True,"startTime":2,"endTime":3},"sun":{"isOpen":True,"is24Hours":True,"startTime":2,"endTime":3}},"adminName":"adminName","friendlyId":"friendlyId","appointmentReminders":{"emailFirstReminderInterval":6,"emailSecondReminderInterval":5,"smsSecondReminder":7,"smsSecondReminderInterval":9,"smsFirstReminder":5,"emailFirstReminder":0,"smsFirstReminderInterval":2,"emailSecondReminder":1},"defaults":{"customerState":True,"businessNotification":True,"emailInfo":True,"enableUtcTimezone":True,"customerCity":True,"autoUpdateCustomer":True},"phone":"phone","regionId":"regionId","name":"name","timezoneName":"timezoneName","fax":"fax","email":"email","adminEmail":"adminEmail"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/setup/v1/locations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_locations_services_id_delete(client):
    """Test case for setup_v1_locations_services_id_delete

    Unlink Service
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/setup/v1/locations/services/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_setup_v1_locations_services_id_get(client):
    """Test case for setup_v1_locations_services_id_get

    Get Linked Service
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/setup/v1/locations/services/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

