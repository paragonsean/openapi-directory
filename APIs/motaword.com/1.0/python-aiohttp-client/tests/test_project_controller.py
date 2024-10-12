# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cm import CM
from openapi_server.models.callback_result import CallbackResult
from openapi_server.models.cancel_project_request import CancelProjectRequest
from openapi_server.models.error import Error
from openapi_server.models.invoice import Invoice
from openapi_server.models.list_order_type import ListOrderType
from openapi_server.models.new_project import NewProject
from openapi_server.models.operation_status import OperationStatus
from openapi_server.models.package import Package
from openapi_server.models.package_status import PackageStatus
from openapi_server.models.progress import Progress
from openapi_server.models.project import Project
from openapi_server.models.project_id import ProjectId
from openapi_server.models.project_launch_response import ProjectLaunchResponse
from openapi_server.models.project_list import ProjectList
from openapi_server.models.project_payment import ProjectPayment
from openapi_server.models.project_status import ProjectStatus
from openapi_server.models.project_update import ProjectUpdate
from openapi_server.models.report_content import ReportContent
from openapi_server.models.user_list import UserList


pytestmark = pytest.mark.asyncio

async def test_assign_cm(client):
    """Test case for assign_cm

    Assign a CM to the project
    """
    body = {"user_id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/projects/{id}/assign-cm'.format(id=74),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cancel_project(client):
    """Test case for cancel_project

    Cancel your translation project
    """
    body = {"reason":"reason"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/projects/{id}/cancel'.format(id=74),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_project(client):
    """Test case for create_project

    Create a new project
    """
    body = {"callback_url":"callback_url","glossaries[]":"","coupon_code":"coupon_code","styleguides[]":"","target_languages[]":["target_languages[]","target_languages[]"],"custom":["custom","custom"],"source_language":"source_language","documents[]":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/projects',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_project(client):
    """Test case for delete_project

    Delete your translation project
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/projects/{id}'.format(id=74),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deliver_project(client):
    """Test case for deliver_project

    Deliver project
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/projects/{id}/deliver'.format(id=74),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_download(client):
    """Test case for download

    Download your translated project
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/{id}/download'.format(id=74),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_download_html_invoice(client):
    """Test case for download_html_invoice

    Download project invoice (HTML)
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/{id}/invoice.html'.format(id=74),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_download_language(client):
    """Test case for download_language

    Download your translated project language
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/{id}/download/{language}'.format(id=74, language='en-US'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_download_pdf_invoice(client):
    """Test case for download_pdf_invoice

    Download project invoice (PDF)
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/{id}/invoice.pdf'.format(id=74),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_invoice(client):
    """Test case for get_invoice

    View project invoice
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/{id}/invoice'.format(id=74),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_progress(client):
    """Test case for get_progress

    View progress of a project
    """
    params = [('raw', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/{id}/progress'.format(id=74),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project(client):
    """Test case for get_project

    View a translation project
    """
    params = [('with[]', ['_with_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/{id}'.format(id=74),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_vendors(client):
    """Test case for get_project_vendors

    Get a list of vendors.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/{project_id}/vendors'.format(project_id=74),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_projects(client):
    """Test case for get_projects

    View your translation projects
    """
    params = [('page', 1),
                    ('per_page', 10),
                    ('status[]', [openapi_server.ProjectStatus()]),
                    ('with_pending', True),
                    ('with_started', True),
                    ('with_completed', True),
                    ('order_by', id),
                    ('order_type', openapi_server.ListOrderType()),
                    ('with[]', ['_with_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_quote_id_from_internal_id(client):
    """Test case for get_quote_id_from_internal_id

    Get Quote Id
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/from-internal-id/{project_id}'.format(project_id=74),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vendor_projects(client):
    """Test case for get_vendor_projects

    List projects as a vendor
    """
    params = [('joined', True),
                    ('completed', True),
                    ('page', 1),
                    ('per_page', 10)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/vendor',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vendor_projects_by_user_id(client):
    """Test case for get_vendor_projects_by_user_id

    Get a list of user/vendor projects
    """
    params = [('joined', True),
                    ('completed', True),
                    ('page', 1),
                    ('per_page', 10)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/{user_id}/projects/vendor'.format(user_id=1),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_launch_project(client):
    """Test case for launch_project

    Launch your translation project
    """
    body = {"budget_code":"budget_code","bin":"bin","stripe_token":"stripe_token","card_id":0,"payment_method":"corporate","payment_code":"payment_code"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/projects/{id}/launch'.format(id=74),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_package(client):
    """Test case for package

    Package your translated project
    """
    params = [('async', 0)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/projects/{id}/package'.format(id=74),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_package_language(client):
    """Test case for package_language

    Package your translated project language
    """
    params = [('async', 0)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/projects/{id}/package/{language}'.format(id=74, language='en-US'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_recreate_project(client):
    """Test case for recreate_project

    Recreate your translation project from scratch. This is a risky action, you will lose current translations.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/projects/{id}/recreate'.format(id=74),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_quote_email(client):
    """Test case for send_quote_email

    Send a quote email
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/projects/{id}/email-quote'.format(id=74),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_submit_project_reports(client):
    """Test case for submit_project_reports

    Submit feedback report for a project
    """
    body = {"activity_type":"activity_type","message":"message"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/projects/{id}/reports'.format(id=74),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_track_package(client):
    """Test case for track_package

    Track translation packaging status
    """
    params = [('key', 'key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/{id}/package/check'.format(id=74),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_trigger_callback(client):
    """Test case for trigger_callback

    Trigger a call to your callback URL related to this project.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/{id}/callback/{action_type}'.format(id=74, action_type='action_type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_project(client):
    """Test case for update_project

    Update project info and settings
    """
    body = {"callback_url":"callback_url","coupon_code":"coupon_code","target_languages[]":["target_languages[]","target_languages[]"],"custom":["custom","custom"],"source_language":"source_language"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/projects/{id}'.format(id=74),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

