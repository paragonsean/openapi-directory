# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.add_fields_data import AddFieldsData
from openapi_server.models.add_fields_template_response import AddFieldsTemplateResponse
from openapi_server.models.authentication_error import AuthenticationError
from openapi_server.models.authentication_success_response import AuthenticationSuccessResponse
from openapi_server.models.combine_pdfs_data import CombinePdfsData
from openapi_server.models.combined_submission import CombinedSubmission
from openapi_server.models.combined_submission_data import CombinedSubmissionData
from openapi_server.models.copy_template_data import CopyTemplateData
from openapi_server.models.create_combined_submission_response import CreateCombinedSubmissionResponse
from openapi_server.models.create_custom_file_data import CreateCustomFileData
from openapi_server.models.create_custom_file_response import CreateCustomFileResponse
from openapi_server.models.create_folder_data import CreateFolderData
from openapi_server.models.create_html_template_data import CreateHtmlTemplateData
from openapi_server.models.create_submission_batch_response import CreateSubmissionBatchResponse
from openapi_server.models.create_submission_data_request_token_response import CreateSubmissionDataRequestTokenResponse
from openapi_server.models.create_submission_response import CreateSubmissionResponse
from openapi_server.models.create_submission_response1 import CreateSubmissionResponse1
from openapi_server.models.create_template_from_upload_data import CreateTemplateFromUploadData
from openapi_server.models.error import Error
from openapi_server.models.folder import Folder
from openapi_server.models.full_template import FullTemplate
from openapi_server.models.invalid_request import InvalidRequest
from openapi_server.models.list_submissions_response import ListSubmissionsResponse
from openapi_server.models.move_folder_data import MoveFolderData
from openapi_server.models.move_template_data import MoveTemplateData
from openapi_server.models.pending_template import PendingTemplate
from openapi_server.models.rename_folder_data import RenameFolderData
from openapi_server.models.submission import Submission
from openapi_server.models.submission_batch import SubmissionBatch
from openapi_server.models.submission_batch_data import SubmissionBatchData
from openapi_server.models.submission_data import SubmissionData
from openapi_server.models.submission_data_request import SubmissionDataRequest
from openapi_server.models.template import Template
from openapi_server.models.template_schema import TemplateSchema
from openapi_server.models.update_data_request_response import UpdateDataRequestResponse
from openapi_server.models.update_submission_data_request_data import UpdateSubmissionDataRequestData
from openapi_server.models.update_template_data import UpdateTemplateData
from openapi_server.models.update_template_response import UpdateTemplateResponse
from openapi_server.models.upload_presign import UploadPresign


pytestmark = pytest.mark.asyncio

async def test_add_fields_to_template(client):
    """Test case for add_fields_to_template

    Add new fields to a Template
    """
    body = openapi_server.AddFieldsData()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/templates/{template_id}/add_fields'.format(template_id='tpl_000000000000000002'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_batch_generate_pdf_v1(client):
    """Test case for batch_generate_pdf_v1

    Generates multiple PDFs
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/templates/{template_id}/submissions/batch'.format(template_id='tpl_000000000000000001'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_batch_generate_pdfs(client):
    """Test case for batch_generate_pdfs

    Generates multiple PDFs
    """
    body = openapi_server.SubmissionBatchData()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/submissions/batches',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_combine_pdfs(client):
    """Test case for combine_pdfs

    Merge submission PDFs, template PDFs, or custom files
    """
    body = openapi_server.CombinePdfsData()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/combined_submissions?v=2',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_combine_submissions(client):
    """Test case for combine_submissions

    Merge generated PDFs together
    """
    body = openapi_server.CombinedSubmissionData()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/combined_submissions',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_copy_template(client):
    """Test case for copy_template

    Copy a Template
    """
    body = openapi_server.CopyTemplateData()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/templates/{template_id}/copy'.format(template_id='tpl_000000000000000001'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_custom_file_from_upload(client):
    """Test case for create_custom_file_from_upload

    Create a new custom file from a cached presign upload
    """
    body = openapi_server.CreateCustomFileData()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/custom_files',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_data_request_token(client):
    """Test case for create_data_request_token

    Creates a new data request token for form authentication
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/data_requests/{data_request_id}/tokens'.format(data_request_id='drq_000000000000000001'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_folder(client):
    """Test case for create_folder

    Create a folder
    """
    body = openapi_server.CreateFolderData()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/folders/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_html_template(client):
    """Test case for create_html_template

    Create a new HTML template
    """
    body = openapi_server.CreateHtmlTemplateData()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/templates?desc=html',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_create_pdf_template(client):
    """Test case for create_pdf_template

    Create a new PDF template with a form POST file upload
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = FormData()
    data.add_field('template_document', '/path/to/file')
    data.add_field('template_name', 'template_name_example')
    data.add_field('template_parent_folder_id', 'template_parent_folder_id_example')
    response = await client.request(
        method='POST',
        path='/api/v1/templates',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_pdf_template_from_upload(client):
    """Test case for create_pdf_template_from_upload

    Create a new PDF template from a cached presign upload
    """
    body = openapi_server.CreateTemplateFromUploadData()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/templates?desc=cached_upload',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_folder(client):
    """Test case for delete_folder

    Delete a folder
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/folders/{folder_id}'.format(folder_id='fld_000000000000000001'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_expire_combined_submission(client):
    """Test case for expire_combined_submission

    Expire a combined submission
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/combined_submissions/{combined_submission_id}'.format(combined_submission_id='com_000000000000000001'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_expire_submission(client):
    """Test case for expire_submission

    Expire a PDF submission
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/submissions/{submission_id}'.format(submission_id='sub_000000000000000001'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_pdf(client):
    """Test case for generate_pdf

    Generates a new PDF
    """
    body = openapi_server.SubmissionData()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/templates/{template_id}/submissions'.format(template_id='tpl_000000000000000001'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_combined_submission(client):
    """Test case for get_combined_submission

    Check the status of a combined submission (merged PDFs)
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/combined_submissions/{combined_submission_id}'.format(combined_submission_id='com_000000000000000001'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_data_request(client):
    """Test case for get_data_request

    Look up a submission data request
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/data_requests/{data_request_id}'.format(data_request_id='drq_000000000000000001'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_full_template(client):
    """Test case for get_full_template

    Fetch the full template attributes
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/templates/{template_idfulltru}'.format(template_id='tpl_000000000000000001'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_presign_url(client):
    """Test case for get_presign_url

    Get a presigned URL so that you can upload a file to our AWS S3 bucket
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/uploads/presign',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_submission(client):
    """Test case for get_submission

    Check the status of a PDF
    """
    params = [('include_data', true)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/submissions/{submission_id}'.format(submission_id='sub_000000000000000001'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_submission_batch(client):
    """Test case for get_submission_batch

    Check the status of a submission batch job
    """
    params = [('include_submissions', true)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/submissions/batches/{submission_batch_id}'.format(submission_batch_id='sbb_000000000000000001'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_template(client):
    """Test case for get_template

    Check the status of an uploaded template
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/templates/{template_id}'.format(template_id='tpl_000000000000000001'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_template_schema(client):
    """Test case for get_template_schema

    Fetch the JSON schema for a template
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/templates/{template_id}/schema'.format(template_id='tpl_000000000000000001'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_combined_submissions(client):
    """Test case for list_combined_submissions

    Get a list of all combined submissions
    """
    params = [('page', 2),
                    ('per_page', 1)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/combined_submissions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_folders(client):
    """Test case for list_folders

    Get a list of all folders
    """
    params = [('parent_folder_id', 'fld_000000000000000002')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/folders/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_submissions(client):
    """Test case for list_submissions

    List all submissions
    """
    params = [('cursor', 'sub_list_000012'),
                    ('limit', 3),
                    ('created_after', '2019-01-01T09:00:00-05:00'),
                    ('created_before', '2020-01-01T09:00:00-05:00'),
                    ('type', 'test'),
                    ('include_data', true)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/submissions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_templates(client):
    """Test case for list_templates

    Get a list of all templates
    """
    params = [('query', '2'),
                    ('parent_folder_id', 'fld_000000000000000001'),
                    ('page', 2),
                    ('per_page', 1)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/templates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_move_folder_to_folder(client):
    """Test case for move_folder_to_folder

    Move a folder
    """
    body = openapi_server.MoveFolderData()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/folders/{folder_id}/move'.format(folder_id='fld_000000000000000001'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_move_template_to_folder(client):
    """Test case for move_template_to_folder

    Move Template to folder
    """
    body = openapi_server.MoveTemplateData()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/templates/{template_id}/move'.format(template_id='tpl_000000000000000001'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rename_folder(client):
    """Test case for rename_folder

    Rename a folder
    """
    body = openapi_server.RenameFolderData()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/folders/{folder_id}/rename'.format(folder_id='fld_000000000000000001'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_templates_template_id_submissions_get(client):
    """Test case for templates_template_id_submissions_get

    List all submissions for a given template
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 3.4),
                    ('created_after', 'created_after_example'),
                    ('created_before', 'created_before_example'),
                    ('type', 'type_example'),
                    ('include_data', true)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/templates/{template_id}/submissions'.format(template_id='tpl_000000000000000002'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_test_authentication(client):
    """Test case for test_authentication

    Test Authentication
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/authentication',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_data_request(client):
    """Test case for update_data_request

    Update a submission data request
    """
    body = openapi_server.UpdateSubmissionDataRequestData()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/data_requests/{data_request_id}'.format(data_request_id='drq_000000000000000001'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_template(client):
    """Test case for update_template

    Update a Template
    """
    body = openapi_server.UpdateTemplateData()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/templates/{template_id}'.format(template_id='tpl_000000000000000003'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

