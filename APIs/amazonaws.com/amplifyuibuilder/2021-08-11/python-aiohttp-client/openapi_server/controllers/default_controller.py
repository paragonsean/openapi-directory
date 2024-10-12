from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_component_request import CreateComponentRequest
from openapi_server.models.create_component_response import CreateComponentResponse
from openapi_server.models.create_form_request import CreateFormRequest
from openapi_server.models.create_form_response import CreateFormResponse
from openapi_server.models.create_theme_request import CreateThemeRequest
from openapi_server.models.create_theme_response import CreateThemeResponse
from openapi_server.models.exchange_code_for_token_request import ExchangeCodeForTokenRequest
from openapi_server.models.exchange_code_for_token_response import ExchangeCodeForTokenResponse
from openapi_server.models.export_components_response import ExportComponentsResponse
from openapi_server.models.export_forms_response import ExportFormsResponse
from openapi_server.models.export_themes_response import ExportThemesResponse
from openapi_server.models.get_codegen_job_response import GetCodegenJobResponse
from openapi_server.models.get_component_response import GetComponentResponse
from openapi_server.models.get_form_response import GetFormResponse
from openapi_server.models.get_metadata_response import GetMetadataResponse
from openapi_server.models.get_theme_response import GetThemeResponse
from openapi_server.models.list_codegen_jobs_response import ListCodegenJobsResponse
from openapi_server.models.list_components_response import ListComponentsResponse
from openapi_server.models.list_forms_response import ListFormsResponse
from openapi_server.models.list_themes_response import ListThemesResponse
from openapi_server.models.put_metadata_flag_request import PutMetadataFlagRequest
from openapi_server.models.refresh_token_request import RefreshTokenRequest
from openapi_server.models.refresh_token_response import RefreshTokenResponse
from openapi_server.models.start_codegen_job_request import StartCodegenJobRequest
from openapi_server.models.start_codegen_job_response import StartCodegenJobResponse
from openapi_server.models.update_component_request import UpdateComponentRequest
from openapi_server.models.update_component_response import UpdateComponentResponse
from openapi_server.models.update_form_request import UpdateFormRequest
from openapi_server.models.update_form_response import UpdateFormResponse
from openapi_server.models.update_theme_request import UpdateThemeRequest
from openapi_server.models.update_theme_response import UpdateThemeResponse
from openapi_server import util


async def create_component(request: web.Request, app_id, environment_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, client_token=None) -> web.Response:
    """create_component

    Creates a new component for an Amplify app.

    :param app_id: The unique ID of the Amplify app to associate with the component.
    :type app_id: str
    :param environment_name: The name of the backend environment that is a part of the Amplify app.
    :type environment_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param client_token: The unique client token.
    :type client_token: str

    """
    body = CreateComponentRequest.from_dict(body)
    return web.Response(status=200)


async def create_form(request: web.Request, app_id, environment_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, client_token=None) -> web.Response:
    """create_form

    Creates a new form for an Amplify app.

    :param app_id: The unique ID of the Amplify app to associate with the form.
    :type app_id: str
    :param environment_name: The name of the backend environment that is a part of the Amplify app.
    :type environment_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param client_token: The unique client token.
    :type client_token: str

    """
    body = CreateFormRequest.from_dict(body)
    return web.Response(status=200)


async def create_theme(request: web.Request, app_id, environment_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, client_token=None) -> web.Response:
    """create_theme

    Creates a theme to apply to the components in an Amplify app.

    :param app_id: The unique ID of the Amplify app associated with the theme.
    :type app_id: str
    :param environment_name: The name of the backend environment that is a part of the Amplify app.
    :type environment_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param client_token: The unique client token.
    :type client_token: str

    """
    body = CreateThemeRequest.from_dict(body)
    return web.Response(status=200)


async def delete_component(request: web.Request, app_id, environment_name, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_component

    Deletes a component from an Amplify app.

    :param app_id: The unique ID of the Amplify app associated with the component to delete.
    :type app_id: str
    :param environment_name: The name of the backend environment that is a part of the Amplify app.
    :type environment_name: str
    :param id: The unique ID of the component to delete.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_form(request: web.Request, app_id, environment_name, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_form

    Deletes a form from an Amplify app.

    :param app_id: The unique ID of the Amplify app associated with the form to delete.
    :type app_id: str
    :param environment_name: The name of the backend environment that is a part of the Amplify app.
    :type environment_name: str
    :param id: The unique ID of the form to delete.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def delete_theme(request: web.Request, app_id, environment_name, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_theme

    Deletes a theme from an Amplify app.

    :param app_id: The unique ID of the Amplify app associated with the theme to delete.
    :type app_id: str
    :param environment_name: The name of the backend environment that is a part of the Amplify app.
    :type environment_name: str
    :param id: The unique ID of the theme to delete.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def exchange_code_for_token(request: web.Request, provider, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """exchange_code_for_token

    Exchanges an access code for a token.

    :param provider: The third-party provider for the token. The only valid value is &lt;code&gt;figma&lt;/code&gt;.
    :type provider: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = ExchangeCodeForTokenRequest.from_dict(body)
    return web.Response(status=200)


async def export_components(request: web.Request, app_id, environment_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """export_components

    Exports component configurations to code that is ready to integrate into an Amplify app.

    :param app_id: The unique ID of the Amplify app to export components to.
    :type app_id: str
    :param environment_name: The name of the backend environment that is a part of the Amplify app.
    :type environment_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token to request the next page of results.
    :type next_token: str

    """
    return web.Response(status=200)


async def export_forms(request: web.Request, app_id, environment_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """export_forms

    Exports form configurations to code that is ready to integrate into an Amplify app.

    :param app_id: The unique ID of the Amplify app to export forms to.
    :type app_id: str
    :param environment_name: The name of the backend environment that is a part of the Amplify app.
    :type environment_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token to request the next page of results.
    :type next_token: str

    """
    return web.Response(status=200)


async def export_themes(request: web.Request, app_id, environment_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """export_themes

    Exports theme configurations to code that is ready to integrate into an Amplify app.

    :param app_id: The unique ID of the Amplify app to export the themes to.
    :type app_id: str
    :param environment_name: The name of the backend environment that is part of the Amplify app.
    :type environment_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token to request the next page of results.
    :type next_token: str

    """
    return web.Response(status=200)


async def get_codegen_job(request: web.Request, app_id, environment_name, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_codegen_job

    Returns an existing code generation job.

    :param app_id: The unique ID of the Amplify app associated with the code generation job.
    :type app_id: str
    :param environment_name: The name of the backend environment that is a part of the Amplify app associated with the code generation job.
    :type environment_name: str
    :param id: The unique ID of the code generation job.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_component(request: web.Request, app_id, environment_name, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_component

    Returns an existing component for an Amplify app.

    :param app_id: The unique ID of the Amplify app.
    :type app_id: str
    :param environment_name: The name of the backend environment that is part of the Amplify app.
    :type environment_name: str
    :param id: The unique ID of the component.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_form(request: web.Request, app_id, environment_name, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_form

    Returns an existing form for an Amplify app.

    :param app_id: The unique ID of the Amplify app.
    :type app_id: str
    :param environment_name: The name of the backend environment that is part of the Amplify app.
    :type environment_name: str
    :param id: The unique ID of the form.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_metadata(request: web.Request, app_id, environment_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_metadata

    Returns existing metadata for an Amplify app.

    :param app_id: The unique ID of the Amplify app.
    :type app_id: str
    :param environment_name: The name of the backend environment that is part of the Amplify app.
    :type environment_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def get_theme(request: web.Request, app_id, environment_name, id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """get_theme

    Returns an existing theme for an Amplify app.

    :param app_id: The unique ID of the Amplify app.
    :type app_id: str
    :param environment_name: The name of the backend environment that is part of the Amplify app.
    :type environment_name: str
    :param id: The unique ID for the theme.
    :type id: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def list_codegen_jobs(request: web.Request, app_id, environment_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_codegen_jobs

    Retrieves a list of code generation jobs for a specified Amplify app and backend environment.

    :param app_id: The unique ID for the Amplify app.
    :type app_id: str
    :param environment_name: The name of the backend environment that is a part of the Amplify app.
    :type environment_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token to request the next page of results.
    :type next_token: str
    :param max_results: The maximum number of jobs to retrieve.
    :type max_results: int

    """
    return web.Response(status=200)


async def list_components(request: web.Request, app_id, environment_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_components

    Retrieves a list of components for a specified Amplify app and backend environment.

    :param app_id: The unique ID for the Amplify app.
    :type app_id: str
    :param environment_name: The name of the backend environment that is a part of the Amplify app.
    :type environment_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token to request the next page of results.
    :type next_token: str
    :param max_results: The maximum number of components to retrieve.
    :type max_results: int

    """
    return web.Response(status=200)


async def list_forms(request: web.Request, app_id, environment_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_forms

    Retrieves a list of forms for a specified Amplify app and backend environment.

    :param app_id: The unique ID for the Amplify app.
    :type app_id: str
    :param environment_name: The name of the backend environment that is a part of the Amplify app.
    :type environment_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token to request the next page of results.
    :type next_token: str
    :param max_results: The maximum number of forms to retrieve.
    :type max_results: int

    """
    return web.Response(status=200)


async def list_themes(request: web.Request, app_id, environment_name, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_themes

    Retrieves a list of themes for a specified Amplify app and backend environment.

    :param app_id: The unique ID for the Amplify app.
    :type app_id: str
    :param environment_name: The name of the backend environment that is a part of the Amplify app.
    :type environment_name: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: The token to request the next page of results.
    :type next_token: str
    :param max_results: The maximum number of theme results to return in the response.
    :type max_results: int

    """
    return web.Response(status=200)


async def put_metadata_flag(request: web.Request, app_id, environment_name, feature_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_metadata_flag

    Stores the metadata information about a feature on a form.

    :param app_id: The unique ID for the Amplify app.
    :type app_id: str
    :param environment_name: The name of the backend environment that is part of the Amplify app.
    :type environment_name: str
    :param feature_name: The name of the feature associated with the metadata.
    :type feature_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = PutMetadataFlagRequest.from_dict(body)
    return web.Response(status=200)


async def refresh_token(request: web.Request, provider, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """refresh_token

    Refreshes a previously issued access token that might have expired.

    :param provider: The third-party provider for the token. The only valid value is &lt;code&gt;figma&lt;/code&gt;.
    :type provider: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    body = RefreshTokenRequest.from_dict(body)
    return web.Response(status=200)


async def start_codegen_job(request: web.Request, app_id, environment_name, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, client_token=None) -> web.Response:
    """start_codegen_job

    Starts a code generation job for a specified Amplify app and backend environment.

    :param app_id: The unique ID for the Amplify app.
    :type app_id: str
    :param environment_name: The name of the backend environment that is a part of the Amplify app.
    :type environment_name: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param client_token: The idempotency token used to ensure that the code generation job request completes only once.
    :type client_token: str

    """
    body = StartCodegenJobRequest.from_dict(body)
    return web.Response(status=200)


async def update_component(request: web.Request, app_id, environment_name, id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, client_token=None) -> web.Response:
    """update_component

    Updates an existing component.

    :param app_id: The unique ID for the Amplify app.
    :type app_id: str
    :param environment_name: The name of the backend environment that is part of the Amplify app.
    :type environment_name: str
    :param id: The unique ID for the component.
    :type id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param client_token: The unique client token.
    :type client_token: str

    """
    body = UpdateComponentRequest.from_dict(body)
    return web.Response(status=200)


async def update_form(request: web.Request, app_id, environment_name, id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, client_token=None) -> web.Response:
    """update_form

    Updates an existing form.

    :param app_id: The unique ID for the Amplify app.
    :type app_id: str
    :param environment_name: The name of the backend environment that is part of the Amplify app.
    :type environment_name: str
    :param id: The unique ID for the form.
    :type id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param client_token: The unique client token.
    :type client_token: str

    """
    body = UpdateFormRequest.from_dict(body)
    return web.Response(status=200)


async def update_theme(request: web.Request, app_id, environment_name, id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, client_token=None) -> web.Response:
    """update_theme

    Updates an existing theme.

    :param app_id: The unique ID for the Amplify app.
    :type app_id: str
    :param environment_name: The name of the backend environment that is part of the Amplify app.
    :type environment_name: str
    :param id: The unique ID for the theme.
    :type id: str
    :param body: 
    :type body: dict | bytes
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param client_token: The unique client token.
    :type client_token: str

    """
    body = UpdateThemeRequest.from_dict(body)
    return web.Response(status=200)
