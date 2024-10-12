from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.bulk_action_request_body import BulkActionRequestBody
from openapi_server.models.clocking_records_clocking_record_id_put200_response import ClockingRecordsClockingRecordIdPut200Response
from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.companies_company_id_integration_settings_post_request import CompaniesCompanyIdIntegrationSettingsPostRequest
from openapi_server.models.create_success_response import CreateSuccessResponse
from openapi_server.models.empty_success_response import EmptySuccessResponse
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.forbidden_error import ForbiddenError
from openapi_server.models.projects_project_id_users_get200_response import ProjectsProjectIdUsersGet200Response
from openapi_server.models.projects_project_id_users_user_id_get200_response import ProjectsProjectIdUsersUserIdGet200Response
from openapi_server.models.users_post_request import UsersPostRequest
from openapi_server.models.users_resend_welcome_sms_get200_response import UsersResendWelcomeSmsGet200Response
from openapi_server.models.users_user_id_integration_settings_get200_response import UsersUserIdIntegrationSettingsGet200Response
from openapi_server.models.users_user_id_integration_settings_integration_settings_user_id_get200_response import UsersUserIdIntegrationSettingsIntegrationSettingsUserIdGet200Response
from openapi_server import util


async def users_bulk_activate(request: web.Request, body=None) -> web.Response:
    """Activate multiple users

    

    :param body: User ids
    :type body: dict | bytes

    """
    body = BulkActionRequestBody.from_dict(body)
    return web.Response(status=200)


async def users_bulk_deactivate(request: web.Request, body=None) -> web.Response:
    """Deactivate multiple users

    

    :param body: User ids
    :type body: dict | bytes

    """
    body = BulkActionRequestBody.from_dict(body)
    return web.Response(status=200)


async def users_get(request: web.Request, first_name=None, last_name=None, email=None, stock_location_id=None, is_active=None) -> web.Response:
    """Get list of users in company

    

    :param first_name: Used to filter on the &#x60;first_name&#x60; of the users
    :type first_name: str
    :param last_name: Used to filter on the &#x60;last_name&#x60; of the users
    :type last_name: str
    :param email: Used to filter on the &#x60;email&#x60; of the users
    :type email: str
    :param stock_location_id: Used to filter on the &#x60;stock_location_id&#x60; of the users
    :type stock_location_id: str
    :param is_active: Filters active/inactive users
    :type is_active: bool

    """
    return web.Response(status=200)


async def users_post(request: web.Request, body=None) -> web.Response:
    """Add user to company

    

    :param body: 
    :type body: dict | bytes

    """
    body = UsersPostRequest.from_dict(body)
    return web.Response(status=200)


async def users_resend_welcome_sms_get(request: web.Request, ) -> web.Response:
    """Resend Welcome SMS to the user

    


    """
    return web.Response(status=200)


async def users_user_id_delete(request: web.Request, user_id) -> web.Response:
    """Delete user

    

    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def users_user_id_get(request: web.Request, user_id) -> web.Response:
    """View user

    

    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def users_user_id_integration_settings_get(request: web.Request, user_id) -> web.Response:
    """Get a list of user integration settings

    

    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def users_user_id_integration_settings_integration_settings_user_id_delete(request: web.Request, user_id, integration_settings_user_id) -> web.Response:
    """Delete a user integration setting

    

    :param user_id: 
    :type user_id: str
    :param integration_settings_user_id: 
    :type integration_settings_user_id: str

    """
    return web.Response(status=200)


async def users_user_id_integration_settings_integration_settings_user_id_get(request: web.Request, user_id, integration_settings_user_id) -> web.Response:
    """Get a user integration setting

    

    :param user_id: 
    :type user_id: str
    :param integration_settings_user_id: 
    :type integration_settings_user_id: str

    """
    return web.Response(status=200)


async def users_user_id_integration_settings_integration_settings_user_id_put(request: web.Request, user_id, integration_settings_user_id) -> web.Response:
    """Edit a user integration setting

    

    :param user_id: 
    :type user_id: str
    :param integration_settings_user_id: 
    :type integration_settings_user_id: str

    """
    return web.Response(status=200)


async def users_user_id_integration_settings_post(request: web.Request, user_id, body=None) -> web.Response:
    """Add a user integration setting

    

    :param user_id: 
    :type user_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CompaniesCompanyIdIntegrationSettingsPostRequest.from_dict(body)
    return web.Response(status=200)


async def users_user_id_put(request: web.Request, user_id) -> web.Response:
    """Edit user

    

    :param user_id: 
    :type user_id: str

    """
    return web.Response(status=200)


async def users_user_id_upload_image_post(request: web.Request, user_id, image=None) -> web.Response:
    """Upload a new image to a user

    

    :param user_id: 
    :type user_id: str
    :param image: 
    :type image: str

    """
    return web.Response(status=200)
