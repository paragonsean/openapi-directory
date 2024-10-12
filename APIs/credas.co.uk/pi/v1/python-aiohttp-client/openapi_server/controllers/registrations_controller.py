from typing import List, Dict
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
from openapi_server import util


async def add_instant_registration(request: web.Request, apikey, body=None) -> web.Response:
    """Creates new registration record, adds an ID document and optional selfie image in one go.

    It&#39;s designed to provide a quick integration path for external systems which capture these details.

    :param apikey: ApiKey supplied.
    :type apikey: str
    :param body: The Credas.Api.Models.Registrations.AddInstantRegistrationRequest object containing required data.
    :type body: dict | bytes

    """
    body = CredasApiModelsRegistrationsAddInstantRegistrationRequest.from_dict(body)
    return web.Response(status=200)


async def add_registration(request: web.Request, apikey, body=None) -> web.Response:
    """Creates new registration.

    

    :param apikey: ApiKey supplied.
    :type apikey: str
    :param body: Object containing registration details.
    :type body: dict | bytes

    """
    body = CredasApiModelsRegistrationsAddRegistrationRequest.from_dict(body)
    return web.Response(status=200)


async def api_registrations_id_pdf_export_sections_get(request: web.Request, id, apikey, comments=None, contact_details=None, standard_checks=None, pep_sanction_checks=None, proof_of_ownership=None, bank_account_check=None, credit_status_check=None, liveness=None, exclude_selfie=None, exclude_id_documents=None, diatf_section=None) -> web.Response:
    """Returns a PDF report for a given registration containing specified sections

    

    :param id: Id of the registration.
    :type id: str
    :type id: str
    :param apikey: ApiKey supplied.
    :type apikey: str
    :param comments: 
    :type comments: bool
    :param contact_details: 
    :type contact_details: bool
    :param standard_checks: 
    :type standard_checks: bool
    :param pep_sanction_checks: 
    :type pep_sanction_checks: bool
    :param proof_of_ownership: 
    :type proof_of_ownership: bool
    :param bank_account_check: 
    :type bank_account_check: bool
    :param credit_status_check: 
    :type credit_status_check: bool
    :param liveness: 
    :type liveness: bool
    :param exclude_selfie: 
    :type exclude_selfie: bool
    :param exclude_id_documents: 
    :type exclude_id_documents: bool
    :param diatf_section: 
    :type diatf_section: bool

    """
    return web.Response(status=200)


async def check_submitted_id_documents(request: web.Request, id, apikey) -> web.Response:
    """Checks if submitted documents are sufficient to complete registration.

    

    :param id: Id of the registration.
    :type id: str
    :type id: str
    :param apikey: ApiKey supplied.
    :type apikey: str

    """
    return web.Response(status=200)


async def get_registration_pdf_export(request: web.Request, id, apikey) -> web.Response:
    """Returns PDF export for a given registration.

    

    :param id: Id of the registration.
    :type id: str
    :type id: str
    :param apikey: ApiKey supplied.
    :type apikey: str

    """
    return web.Response(status=200)


async def get_registration_search(request: web.Request, apikey, page_num=None, page_size=None, forename=None, surname=None, email=None, dob=None) -> web.Response:
    """Gets paged registration list by search criteria or nothing if there are no matching fields.  Optional parameters may be appended to the query string.  Maximum page size is 50.

    

    :param apikey: ApiKey supplied.
    :type apikey: str
    :param page_num: Zero-based page number to retrieve.
    :type page_num: int
    :param page_size: Number of records to return on each request (Maximum value is 50).
    :type page_size: int
    :param forename: Search by forename.
    :type forename: str
    :param surname: Search by surname.
    :type surname: str
    :param email: Search by user email.
    :type email: str
    :param dob: Date of birth in (yyyy-MM-dd) format
    :type dob: str

    """
    return web.Response(status=200)


async def get_registration_settings(request: web.Request, id, apikey) -> web.Response:
    """Gets registration settings or nothing if there are no settings associated with the registration.

    

    :param id: Id of the registration.
    :type id: str
    :type id: str
    :param apikey: ApiKey supplied.
    :type apikey: str

    """
    return web.Response(status=200)


async def get_registration_summaries_by_reference_id(request: web.Request, reference_id, apikey) -> web.Response:
    """Finds registrations by the ReferenceId.

    

    :param reference_id: ReferenceId - from external system to match Registrations on.
    :type reference_id: str
    :param apikey: ApiKey supplied.
    :type apikey: str

    """
    return web.Response(status=200)


async def get_registration_summary(request: web.Request, id, apikey) -> web.Response:
    """Finds a registration by the Id.

    

    :param id: Id of the registration.
    :type id: str
    :type id: str
    :param apikey: ApiKey supplied.
    :type apikey: str

    """
    return web.Response(status=200)


async def get_registration_summary_by_reg_code(request: web.Request, reg_code, apikey) -> web.Response:
    """Finds a registration by the RegCode.

    

    :param reg_code: RegCode - short unique identifier.
    :type reg_code: str
    :param apikey: ApiKey supplied.
    :type apikey: str

    """
    return web.Response(status=200)


async def get_registration_supported_id_documents(request: web.Request, id, apikey) -> web.Response:
    """Get a list of supported id document for the specified registration id.

    

    :param id: Id of the registration.
    :type id: str
    :type id: str
    :param apikey: ApiKey supplied.
    :type apikey: str

    """
    return web.Response(status=200)


async def get_share_code_pdf_export(request: web.Request, id, apikey) -> web.Response:
    """Returns settlement status PDF (Share Code) for a given registration.

    

    :param id: Id of the registration.
    :type id: str
    :type id: str
    :param apikey: ApiKey supplied.
    :type apikey: str

    """
    return web.Response(status=200)


async def override_check_status(request: web.Request, id, apikey, body=None) -> web.Response:
    """Sets an override for a specific check on the registration.

    

    :param id: Id of the registration.
    :type id: str
    :type id: str
    :param apikey: ApiKey supplied.
    :type apikey: str
    :param body: Request data.
    :type body: dict | bytes

    """
    body = CredasApiModelsStatusOverridesOverrideCheckStatusRequest.from_dict(body)
    return web.Response(status=200)


async def resend_invitation(request: web.Request, id, apikey) -> web.Response:
    """Resends any invitation for the specified registration.

    

    :param id: Id of the registration.
    :type id: str
    :type id: str
    :param apikey: ApiKey supplied.
    :type apikey: str

    """
    return web.Response(status=200)


async def update_contact_details(request: web.Request, id, apikey, body=None) -> web.Response:
    """Updates a registration&#39;s contact details.

    

    :param id: Id of the registration.
    :type id: str
    :type id: str
    :param apikey: ApiKey supplied.
    :type apikey: str
    :param body: Object containing contact details.
    :type body: dict | bytes

    """
    body = CredasApiModelsRegistrationsUpdateContactDetailsRequest.from_dict(body)
    return web.Response(status=200)


async def update_registration_settings(request: web.Request, id, apikey, body=None) -> web.Response:
    """Updates registration settings.

    

    :param id: Id of the registration.
    :type id: str
    :type id: str
    :param apikey: ApiKey supplied.
    :type apikey: str
    :param body: Object containing registration settings.
    :type body: dict | bytes

    """
    body = CredasApiModelsRegistrationsRegistrationSettings.from_dict(body)
    return web.Response(status=200)


async def update_registration_status(request: web.Request, id, apikey, body=None) -> web.Response:
    """Updates the status of the registration to one specified in the request.

    

    :param id: Id of the registration.
    :type id: str
    :type id: str
    :param apikey: ApiKey supplied.
    :type apikey: str
    :param body: Request object containing the details.
    :type body: dict | bytes

    """
    body = CredasApiModelsRegistrationsUpdateRegistrationStatusRequest.from_dict(body)
    return web.Response(status=200)
