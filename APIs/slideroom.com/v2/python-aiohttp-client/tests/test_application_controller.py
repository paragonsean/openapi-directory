# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.request_application_export_result_v2 import RequestApplicationExportResultV2


pytestmark = pytest.mark.asyncio

async def test_application_delete_attributes_v2(client):
    """Test case for application_delete_attributes_v2

    Deletes a custom attribute for an application.
    """
    params = [('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/application/{application_id}/attributes'.format(application_id='application_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_get_attribute_names_v2(client):
    """Test case for application_get_attribute_names_v2

    Gets the custom application attributes used by the organization.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/application/attributes/names',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_get_attributes_v2(client):
    """Test case for application_get_attributes_v2

    Gets the custom attributes for an application.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/application/{application_id}/attributes'.format(application_id='application_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_application_post_attributes_v2(client):
    """Test case for application_post_attributes_v2

    Updates the custom attributes for an application. API Import is available in the Advanced Plan.
    """
    data = {'key': 'data_example'}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/application/{application_id}/attributes'.format(application_id='application_id_example'),
        headers=headers,
        json=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_request_export_by_application_id_v2(client):
    """Test case for application_request_export_by_application_id_v2

    Requests the generation of a single application export file (tabular, pdf, zip).
    """
    params = [('format', 'format_example'),
                    ('roundType', 'round_type_example'),
                    ('roundName', 'round_name_example'),
                    ('tab.export', 'tab_export_example'),
                    ('pdf.includeForms', True),
                    ('pdf.includeReferences', True),
                    ('pdf.includeMedia', True),
                    ('pdf.includeApplicantAttachments', True),
                    ('pdf.includeOrganizationAttachments', True),
                    ('pdf.includeRatings', True),
                    ('pdf.includeFullPageMedia', True),
                    ('pdf.includeHighlights', True),
                    ('pdf.includeComments', True),
                    ('pdf.includeCommonApp', True),
                    ('zip.originalMedia', True),
                    ('zip.includeForms', True),
                    ('zip.includeReferences', True),
                    ('zip.includeMedia', True),
                    ('zip.includeApplicantAttachments', True),
                    ('zip.includeOrganizationAttachments', True),
                    ('zip.includeRatings', True),
                    ('zip.includeComments', True),
                    ('zip.includeCommonApp', True),
                    ('delivery.account', 'delivery_account_example'),
                    ('delivery.folder', 'delivery_folder_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/application/{application_id}/request-export'.format(application_id='application_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_request_export_v2(client):
    """Test case for application_request_export_v2

    Requests the generation of application export files (tabular, pdf, zip).
    """
    params = [('format', 'format_example'),
                    ('roundType', 'round_type_example'),
                    ('roundName', 'round_name_example'),
                    ('tab.export', 'tab_export_example'),
                    ('pdf.includeForms', True),
                    ('pdf.includeReferences', True),
                    ('pdf.includeMedia', True),
                    ('pdf.includeApplicantAttachments', True),
                    ('pdf.includeOrganizationAttachments', True),
                    ('pdf.includeRatings', True),
                    ('pdf.includeFullPageMedia', True),
                    ('pdf.includeHighlights', True),
                    ('pdf.includeComments', True),
                    ('pdf.includeCommonApp', True),
                    ('zip.originalMedia', True),
                    ('zip.includeForms', True),
                    ('zip.includeReferences', True),
                    ('zip.includeMedia', True),
                    ('zip.includeApplicantAttachments', True),
                    ('zip.includeOrganizationAttachments', True),
                    ('zip.includeRatings', True),
                    ('zip.includeComments', True),
                    ('zip.includeCommonApp', True),
                    ('delivery.account', 'delivery_account_example'),
                    ('delivery.folder', 'delivery_folder_example'),
                    ('since', 56),
                    ('pool', 'pool_example'),
                    ('status', 'status_example'),
                    ('searchName', 'search_name_example'),
                    ('email', 'email_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/application/request-export',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

