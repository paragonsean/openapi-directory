# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.credas_api_models_errors_error_response import CredasApiModelsErrorsErrorResponse
from openapi_server.models.credas_api_models_registrations_add_instant_registration_request import CredasApiModelsRegistrationsAddInstantRegistrationRequest
from openapi_server.models.credas_api_models_registrations_add_instant_registration_response import CredasApiModelsRegistrationsAddInstantRegistrationResponse
from openapi_server.models.credas_api_models_registrations_add_registration_request import CredasApiModelsRegistrationsAddRegistrationRequest
from openapi_server.models.credas_api_models_registrations_add_registration_response import CredasApiModelsRegistrationsAddRegistrationResponse
from openapi_server.models.credas_api_models_registrations_check_submitted_id_documents_response import CredasApiModelsRegistrationsCheckSubmittedIdDocumentsResponse
from openapi_server.models.credas_api_models_registrations_paged_registration_summary import CredasApiModelsRegistrationsPagedRegistrationSummary
from openapi_server.models.credas_api_models_registrations_registration_settings import CredasApiModelsRegistrationsRegistrationSettings
from openapi_server.models.credas_api_models_registrations_registration_summary import CredasApiModelsRegistrationsRegistrationSummary
from openapi_server.models.credas_api_models_registrations_supported_id_document import CredasApiModelsRegistrationsSupportedIdDocument
from openapi_server.models.credas_api_models_registrations_update_contact_details_request import CredasApiModelsRegistrationsUpdateContactDetailsRequest
from openapi_server.models.credas_api_models_registrations_update_registration_status_request import CredasApiModelsRegistrationsUpdateRegistrationStatusRequest
from openapi_server.models.credas_api_models_status_overrides_override_check_status_request import CredasApiModelsStatusOverridesOverrideCheckStatusRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_add_instant_registration(client):
    """Test case for add_instant_registration

    Creates new registration record, adds an ID document and optional selfie image in one go.
    """
    body = openapi_server.CredasApiModelsRegistrationsAddInstantRegistrationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='POST',
        path='/api/registrations/instant',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_add_registration(client):
    """Test case for add_registration

    Creates new registration.
    """
    body = openapi_server.CredasApiModelsRegistrationsAddRegistrationRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='POST',
        path='/api/registrations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_registrations_id_pdf_export_sections_get(client):
    """Test case for api_registrations_id_pdf_export_sections_get

    Returns a PDF report for a given registration containing specified sections
    """
    params = [('Comments', True),
                    ('ContactDetails', True),
                    ('StandardChecks', True),
                    ('PepSanctionChecks', True),
                    ('ProofOfOwnership', True),
                    ('BankAccountCheck', True),
                    ('CreditStatusCheck', True),
                    ('Liveness', True),
                    ('ExcludeSelfie', True),
                    ('ExcludeIDDocuments', True),
                    ('DIATFSection', True)]
    headers = { 
        'Accept': 'application/json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='GET',
        path='/api/registrations/{id}/pdf-export-sections'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_check_submitted_id_documents(client):
    """Test case for check_submitted_id_documents

    Checks if submitted documents are sufficient to complete registration.
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='GET',
        path='/api/registrations/{id}/check-submitted-id-documents'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_registration_pdf_export(client):
    """Test case for get_registration_pdf_export

    Returns PDF export for a given registration.
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='GET',
        path='/api/registrations/{id}/pdf-export'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_registration_search(client):
    """Test case for get_registration_search

    Gets paged registration list by search criteria or nothing if there are no matching fields.  Optional parameters may be appended to the query string.  Maximum page size is 50.
    """
    params = [('pageNum', 0),
                    ('pageSize', 50),
                    ('forename', 'forename_example'),
                    ('surname', 'surname_example'),
                    ('email', 'email_example'),
                    ('dob', 'dob_example')]
    headers = { 
        'Accept': 'application/json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='GET',
        path='/api/registrations/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_registration_settings(client):
    """Test case for get_registration_settings

    Gets registration settings or nothing if there are no settings associated with the registration.
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='GET',
        path='/api/registrations/{id}/settings'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_registration_summaries_by_reference_id(client):
    """Test case for get_registration_summaries_by_reference_id

    Finds registrations by the ReferenceId.
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='GET',
        path='/api/registrations/referenceid/{reference_id}/summary'.format(reference_id='reference_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_registration_summary(client):
    """Test case for get_registration_summary

    Finds a registration by the Id.
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='GET',
        path='/api/registrations/{id}/summary'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_registration_summary_by_reg_code(client):
    """Test case for get_registration_summary_by_reg_code

    Finds a registration by the RegCode.
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='GET',
        path='/api/registrations/regcode/{reg_code}/summary'.format(reg_code='reg_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_registration_supported_id_documents(client):
    """Test case for get_registration_supported_id_documents

    Get a list of supported id document for the specified registration id.
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='GET',
        path='/api/registrations/{id}/supported-id-documents'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_share_code_pdf_export(client):
    """Test case for get_share_code_pdf_export

    Returns settlement status PDF (Share Code) for a given registration.
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='GET',
        path='/api/registrations/{id}/pdf-settlement-status'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_override_check_status(client):
    """Test case for override_check_status

    Sets an override for a specific check on the registration.
    """
    body = openapi_server.CredasApiModelsStatusOverridesOverrideCheckStatusRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='PUT',
        path='/api/registrations/{id}/override-check-status'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resend_invitation(client):
    """Test case for resend_invitation

    Resends any invitation for the specified registration.
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='POST',
        path='/api/registrations/{id}/resend-invitation'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_contact_details(client):
    """Test case for update_contact_details

    Updates a registration's contact details.
    """
    body = openapi_server.CredasApiModelsRegistrationsUpdateContactDetailsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='PUT',
        path='/api/registrations/{id}/contact-details'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_registration_settings(client):
    """Test case for update_registration_settings

    Updates registration settings.
    """
    body = openapi_server.CredasApiModelsRegistrationsRegistrationSettings()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='PUT',
        path='/api/registrations/{id}/settings'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_registration_status(client):
    """Test case for update_registration_status

    Updates the status of the registration to one specified in the request.
    """
    body = openapi_server.CredasApiModelsRegistrationsUpdateRegistrationStatusRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'apikey': 'apikey_example',
    }
    response = await client.request(
        method='PUT',
        path='/api/registrations/{id}/status'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

