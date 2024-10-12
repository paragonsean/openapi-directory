from typing import List, Dict
from aiohttp import web

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
from openapi_server import util


async def add_fields_to_template(request: web.Request, template_id, body) -> web.Response:
    """Add new fields to a Template

    

    :param template_id: 
    :type template_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddFieldsData.from_dict(body)
    return web.Response(status=200)


async def batch_generate_pdf_v1(request: web.Request, template_id, body) -> web.Response:
    """Generates multiple PDFs

    

    :param template_id: 
    :type template_id: str
    :param body: 

    """
    return web.Response(status=200)


async def batch_generate_pdfs(request: web.Request, body) -> web.Response:
    """Generates multiple PDFs

    

    :param body: 
    :type body: dict | bytes

    """
    body = SubmissionBatchData.from_dict(body)
    return web.Response(status=200)


async def combine_pdfs(request: web.Request, body) -> web.Response:
    """Merge submission PDFs, template PDFs, or custom files

    

    :param body: 
    :type body: dict | bytes

    """
    body = CombinePdfsData.from_dict(body)
    return web.Response(status=200)


async def combine_submissions(request: web.Request, body) -> web.Response:
    """Merge generated PDFs together

    

    :param body: 
    :type body: dict | bytes

    """
    body = CombinedSubmissionData.from_dict(body)
    return web.Response(status=200)


async def copy_template(request: web.Request, template_id, body=None) -> web.Response:
    """Copy a Template

    

    :param template_id: 
    :type template_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CopyTemplateData.from_dict(body)
    return web.Response(status=200)


async def create_custom_file_from_upload(request: web.Request, body) -> web.Response:
    """Create a new custom file from a cached presign upload

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateCustomFileData.from_dict(body)
    return web.Response(status=200)


async def create_data_request_token(request: web.Request, data_request_id) -> web.Response:
    """Creates a new data request token for form authentication

    

    :param data_request_id: 
    :type data_request_id: str

    """
    return web.Response(status=200)


async def create_folder(request: web.Request, body) -> web.Response:
    """Create a folder

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateFolderData.from_dict(body)
    return web.Response(status=200)


async def create_html_template(request: web.Request, body) -> web.Response:
    """Create a new HTML template

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateHtmlTemplateData.from_dict(body)
    return web.Response(status=200)


async def create_pdf_template(request: web.Request, template_document, template_name, template_parent_folder_id=None) -> web.Response:
    """Create a new PDF template with a form POST file upload

    

    :param template_document: 
    :type template_document: str
    :param template_name: 
    :type template_name: str
    :param template_parent_folder_id: 
    :type template_parent_folder_id: str

    """
    return web.Response(status=200)


async def create_pdf_template_from_upload(request: web.Request, body) -> web.Response:
    """Create a new PDF template from a cached presign upload

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateTemplateFromUploadData.from_dict(body)
    return web.Response(status=200)


async def delete_folder(request: web.Request, folder_id) -> web.Response:
    """Delete a folder

    

    :param folder_id: 
    :type folder_id: str

    """
    return web.Response(status=200)


async def expire_combined_submission(request: web.Request, combined_submission_id) -> web.Response:
    """Expire a combined submission

    

    :param combined_submission_id: 
    :type combined_submission_id: str

    """
    return web.Response(status=200)


async def expire_submission(request: web.Request, submission_id) -> web.Response:
    """Expire a PDF submission

    

    :param submission_id: 
    :type submission_id: str

    """
    return web.Response(status=200)


async def generate_pdf(request: web.Request, template_id, body) -> web.Response:
    """Generates a new PDF

    

    :param template_id: 
    :type template_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SubmissionData.from_dict(body)
    return web.Response(status=200)


async def get_combined_submission(request: web.Request, combined_submission_id) -> web.Response:
    """Check the status of a combined submission (merged PDFs)

    

    :param combined_submission_id: 
    :type combined_submission_id: str

    """
    return web.Response(status=200)


async def get_data_request(request: web.Request, data_request_id) -> web.Response:
    """Look up a submission data request

    

    :param data_request_id: 
    :type data_request_id: str

    """
    return web.Response(status=200)


async def get_full_template(request: web.Request, template_id) -> web.Response:
    """Fetch the full template attributes

    

    :param template_id: 
    :type template_id: str

    """
    return web.Response(status=200)


async def get_presign_url(request: web.Request, ) -> web.Response:
    """Get a presigned URL so that you can upload a file to our AWS S3 bucket

    


    """
    return web.Response(status=200)


async def get_submission(request: web.Request, submission_id, include_data=None) -> web.Response:
    """Check the status of a PDF

    

    :param submission_id: 
    :type submission_id: str
    :param include_data: 
    :type include_data: bool

    """
    return web.Response(status=200)


async def get_submission_batch(request: web.Request, submission_batch_id, include_submissions=None) -> web.Response:
    """Check the status of a submission batch job

    

    :param submission_batch_id: 
    :type submission_batch_id: str
    :param include_submissions: 
    :type include_submissions: bool

    """
    return web.Response(status=200)


async def get_template(request: web.Request, template_id) -> web.Response:
    """Check the status of an uploaded template

    

    :param template_id: 
    :type template_id: str

    """
    return web.Response(status=200)


async def get_template_schema(request: web.Request, template_id) -> web.Response:
    """Fetch the JSON schema for a template

    

    :param template_id: 
    :type template_id: str

    """
    return web.Response(status=200)


async def list_combined_submissions(request: web.Request, page=None, per_page=None) -> web.Response:
    """Get a list of all combined submissions

    

    :param page: Default: 1
    :type page: int
    :param per_page: Default: 50
    :type per_page: int

    """
    return web.Response(status=200)


async def list_folders(request: web.Request, parent_folder_id=None) -> web.Response:
    """Get a list of all folders

    

    :param parent_folder_id: Filter By Folder Id
    :type parent_folder_id: str

    """
    return web.Response(status=200)


async def list_submissions(request: web.Request, cursor=None, limit=None, created_after=None, created_before=None, type=None, include_data=None) -> web.Response:
    """List all submissions

    

    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: 
    :param created_after: 
    :type created_after: str
    :param created_before: 
    :type created_before: str
    :param type: 
    :type type: str
    :param include_data: 
    :type include_data: bool

    """
    return web.Response(status=200)


async def list_templates(request: web.Request, query=None, parent_folder_id=None, page=None, per_page=None) -> web.Response:
    """Get a list of all templates

    

    :param query: Search By Name
    :type query: str
    :param parent_folder_id: Filter By Folder Id
    :type parent_folder_id: str
    :param page: Default: 1
    :type page: int
    :param per_page: Default: 50
    :type per_page: int

    """
    return web.Response(status=200)


async def move_folder_to_folder(request: web.Request, folder_id, body) -> web.Response:
    """Move a folder

    

    :param folder_id: 
    :type folder_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = MoveFolderData.from_dict(body)
    return web.Response(status=200)


async def move_template_to_folder(request: web.Request, template_id, body) -> web.Response:
    """Move Template to folder

    

    :param template_id: 
    :type template_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = MoveTemplateData.from_dict(body)
    return web.Response(status=200)


async def rename_folder(request: web.Request, folder_id, body) -> web.Response:
    """Rename a folder

    

    :param folder_id: 
    :type folder_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = RenameFolderData.from_dict(body)
    return web.Response(status=200)


async def templates_template_id_submissions_get(request: web.Request, template_id, cursor=None, limit=None, created_after=None, created_before=None, type=None, include_data=None) -> web.Response:
    """List all submissions for a given template

    

    :param template_id: 
    :type template_id: str
    :param cursor: 
    :type cursor: str
    :param limit: 
    :type limit: 
    :param created_after: 
    :type created_after: str
    :param created_before: 
    :type created_before: str
    :param type: 
    :type type: str
    :param include_data: 
    :type include_data: bool

    """
    return web.Response(status=200)


async def test_authentication(request: web.Request, ) -> web.Response:
    """Test Authentication

    


    """
    return web.Response(status=200)


async def update_data_request(request: web.Request, data_request_id, body) -> web.Response:
    """Update a submission data request

    

    :param data_request_id: 
    :type data_request_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateSubmissionDataRequestData.from_dict(body)
    return web.Response(status=200)


async def update_template(request: web.Request, template_id, body) -> web.Response:
    """Update a Template

    

    :param template_id: 
    :type template_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateTemplateData.from_dict(body)
    return web.Response(status=200)
