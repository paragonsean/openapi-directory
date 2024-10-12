from typing import List, Dict
from aiohttp import web

from openapi_server.models.big_decimal_dto import BigDecimalDTO
from openapi_server.models.custom_field_dto import CustomFieldDTO
from openapi_server.models.file_dto import FileDto
from openapi_server.models.files_archive_dto import FilesArchiveDto
from openapi_server.models.files_dto import FilesDto
from openapi_server.models.finance_dto import FinanceDTO
from openapi_server.models.job_dto import JobDto
from openapi_server.models.payable_create_dto import PayableCreateDTO
from openapi_server.models.payable_dto import PayableDTO
from openapi_server.models.project_file_dto import ProjectFileDto
from openapi_server.models.project_status_dto import ProjectStatusDTO
from openapi_server.models.quote_create_dto import QuoteCreateDTO
from openapi_server.models.quote_dtov2 import QuoteDTOv2
from openapi_server.models.receivable_create_dto import ReceivableCreateDTO
from openapi_server.models.receivable_dto import ReceivableDTO
from openapi_server.models.smart_contacts_dto import SmartContactsDTO
from openapi_server.models.smart_custom_field_dto import SmartCustomFieldDTO
from openapi_server.models.source_language_dto import SourceLanguageDTO
from openapi_server.models.specialization_dto import SpecializationDTO
from openapi_server.models.string_dto import StringDTO
from openapi_server.models.target_languages_dto import TargetLanguagesDTO
from openapi_server.models.time_dto import TimeDTO
from openapi_server import util


async def add_files2(request: web.Request, quote_id, body) -> web.Response:
    """Adds files to the quote as added by PM.

    Adds files to the quote as added by PM. The files have to be uploaded beforehand (see \&quot;POST v2/quotes/{quoteId}/files/upload\&quot; operation). The following properties can be specified for each file:&lt;ul&gt;&lt;li&gt;category (required, 400 Bad Request is returned otherwise)&lt;/li&gt;&lt;li&gt;languageIds – when the file category depends on a list of languages&lt;/li&gt;&lt;li&gt;languageCombinationIds – when the file category depends on a list of language combinations&lt;/li&gt;&lt;/ul&gt;

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str
    :param body: Added files to the quote as added by PM.
    :type body: dict | bytes

    """
    body = TimeDTO.from_dict(body)
    return web.Response(status=200)


async def archive1(request: web.Request, body) -> web.Response:
    """Prepares a ZIP archive that contains the specified files.

    Prepares a ZIP archive that contains the specified files.

    :param body: Prepared ZIP archive that contains the specified files.
    :type body: dict | bytes

    """
    body = FilesDto.from_dict(body)
    return web.Response(status=200)


async def change_status3(request: web.Request, quote_id, body) -> web.Response:
    """Changes quote status if possible (400 Bad Request is returned otherwise).

    Changes quote status if possible (400 Bad Request is returned otherwise). The status has to be specified using one of the following keys: &lt;ul&gt;&lt;li&gt;PENDING – available when the job has one of the following statuses: REQUESTED, REJECTED&lt;/li&gt;&lt;li&gt;SENT – available when the job has one of the following statuses: PENDING&lt;/li&gt;&lt;li&gt;APPROVED – available when the job has one of the following statuses: REQUESTED, PENDING, SENT, APPROVED_BY_CLIENT&lt;/li&gt;&lt;li&gt;REJECTED – available when the job has one of the following statuses: REQUESTED, PENDING, SENT&lt;/li&gt;&lt;/ul&gt;

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str
    :param body: Changed Quote status.
    :type body: dict | bytes

    """
    body = ProjectStatusDTO.from_dict(body)
    return web.Response(status=200)


async def create7(request: web.Request, body=None) -> web.Response:
    """Creates a new Smart Quote.

    Creates a new Smart Quote. If the specified service ID refers to Classic Quote, 400 Bad Request is returned instead.

    :param body: Project to create
    :type body: dict | bytes

    """
    body = QuoteCreateDTO.from_dict(body)
    return web.Response(status=200)


async def create_payable3(request: web.Request, quote_id, body) -> web.Response:
    """Adds a payable to a quote.

    Adds a payable to a quote.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PayableCreateDTO.from_dict(body)
    return web.Response(status=200)


async def create_receivable3(request: web.Request, quote_id, body) -> web.Response:
    """Adds a receivable to a quote.

    Adds a receivable to a quote.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReceivableCreateDTO.from_dict(body)
    return web.Response(status=200)


async def delete_payable3(request: web.Request, quote_id, payable_id) -> web.Response:
    """Deletes a payable.

    Deletes a payable.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str
    :param payable_id: payable&#39;s internal identifier
    :type payable_id: int

    """
    return web.Response(status=200)


async def delete_receivable3(request: web.Request, quote_id, receivable_id) -> web.Response:
    """Deletes a receivable.

    Deletes a receivable.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str
    :param receivable_id: receivable&#39;s internal identifier
    :type receivable_id: int

    """
    return web.Response(status=200)


async def get_by_id10(request: web.Request, quote_id) -> web.Response:
    """Returns quote details.

    Returns quote details. If the specified quote ID refers to Classic Quote, 400 Bad Request is returned instead.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str

    """
    return web.Response(status=200)


async def get_contacts3(request: web.Request, quote_id) -> web.Response:
    """Returns Client Contacts information for a quote.

    Returns Client Contacts information for a quote.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str

    """
    return web.Response(status=200)


async def get_custom_fields9(request: web.Request, quote_id) -> web.Response:
    """Returns a list of custom field keys and values for a project.

    Returns a list of custom field keys and values for a project.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str

    """
    return web.Response(status=200)


async def get_file_by_id3(request: web.Request, file_id) -> web.Response:
    """Returns details of a file.

    Returns details of a file.

    :param file_id: file&#39;s internal identifier
    :type file_id: str

    """
    return web.Response(status=200)


async def get_file_content_by_id1(request: web.Request, file_id, file_name) -> web.Response:
    """Downloads a file content.

    Downloads a file content.

    :param file_id: file&#39;s internal identifier
    :type file_id: str
    :param file_name: file&#39;s name
    :type file_name: str

    """
    return web.Response(status=200)


async def get_files1(request: web.Request, quote_id) -> web.Response:
    """Returns list of files in a quote.

    Returns list of files in a quote. Only files added to the quote (i.e. files that have assigned category and languages) are listed.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str

    """
    return web.Response(status=200)


async def get_finance3(request: web.Request, quote_id) -> web.Response:
    """Returns finance information for a quote.

    Returns finance information for a quote.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str

    """
    return web.Response(status=200)


async def get_jobs1(request: web.Request, quote_id) -> web.Response:
    """Returns list of jobs in a quote.

    Returns list of jobs in a quote.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str

    """
    return web.Response(status=200)


async def update_business_days(request: web.Request, quote_id, body) -> web.Response:
    """Updates Business Days for a quote.

    Updates Business Days for a quote.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str
    :param body: Updated Business Days for a quote.
    :type body: int

    """
    return web.Response(status=200)


async def update_client_notes1(request: web.Request, quote_id, body) -> web.Response:
    """Updates Client Notes for a quote.

    Updates Client Notes for a quote.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str
    :param body: Updated Client Notes for a quote.
    :type body: dict | bytes

    """
    body = StringDTO.from_dict(body)
    return web.Response(status=200)


async def update_client_reference_number1(request: web.Request, quote_id, body) -> web.Response:
    """Updates Client Reference Number for a quote.

    Updates Client Reference Number for a quote.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str
    :param body: Updated Client Reference Number for a quote.
    :type body: dict | bytes

    """
    body = StringDTO.from_dict(body)
    return web.Response(status=200)


async def update_contacts3(request: web.Request, quote_id, body) -> web.Response:
    """Updates Client Contacts for a quote.

    Updates Client Contacts for a quote.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str
    :param body: Updated Client Contacts for a quote.
    :type body: dict | bytes

    """
    body = SmartContactsDTO.from_dict(body)
    return web.Response(status=200)


async def update_custom_field3(request: web.Request, quote_id, key, body) -> web.Response:
    """Updates a custom field with a specified key in a quote.

    Updates a custom field with a specified key in a quote.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str
    :param key: custom field&#39;s key
    :type key: str
    :param body: Updated custom field with a specified key in a quote.
    :type body: dict | bytes

    """
    body = SmartCustomFieldDTO.from_dict(body)
    return web.Response(status=200)


async def update_expected_delivery_date(request: web.Request, quote_id, body) -> web.Response:
    """Updates Expected Delivery Date for a quote.

    Updates Expected Delivery Date for a quote.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str
    :param body: Updated Expected Delivery Date for a quote.
    :type body: dict | bytes

    """
    body = TimeDTO.from_dict(body)
    return web.Response(status=200)


async def update_internal_notes1(request: web.Request, quote_id, body) -> web.Response:
    """Updates Internal Notes for a quote.

    Updates Internal Notes for a quote.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str
    :param body: Updated Internal Notes for a quote.
    :type body: dict | bytes

    """
    body = StringDTO.from_dict(body)
    return web.Response(status=200)


async def update_payable3(request: web.Request, quote_id, payable_id, body) -> web.Response:
    """Updates a payable.

    Updates a payable.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str
    :param payable_id: payable&#39;s internal identifier
    :type payable_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PayableDTO.from_dict(body)
    return web.Response(status=200)


async def update_quote_expiry(request: web.Request, quote_id, body) -> web.Response:
    """Updates Quote Expiry Date for a quote.

    Updates Quote Expiry Date for a quote.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str
    :param body: Updated Quote Expiry Date for a quote.
    :type body: dict | bytes

    """
    body = TimeDTO.from_dict(body)
    return web.Response(status=200)


async def update_receivable3(request: web.Request, quote_id, receivable_id, body) -> web.Response:
    """Updates a receivable.

    Updates a receivable.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str
    :param receivable_id: receivable&#39;s internal identifier
    :type receivable_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ReceivableDTO.from_dict(body)
    return web.Response(status=200)


async def update_source_language1(request: web.Request, quote_id, body) -> web.Response:
    """Updates source language for a quote.

    Updates source language for a quote.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str
    :param body: Updated source language for a quote.
    :type body: dict | bytes

    """
    body = SourceLanguageDTO.from_dict(body)
    return web.Response(status=200)


async def update_specialization1(request: web.Request, quote_id, body) -> web.Response:
    """Updates specialization for a quote.

    Updates specialization for a quote.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str
    :param body: Updated specialization for a quote.
    :type body: dict | bytes

    """
    body = SpecializationDTO.from_dict(body)
    return web.Response(status=200)


async def update_target_languages1(request: web.Request, quote_id, body) -> web.Response:
    """Updates target languages for a quote.

    Updates target languages for a quote.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str
    :param body: Updated target languages for a quote.
    :type body: dict | bytes

    """
    body = TargetLanguagesDTO.from_dict(body)
    return web.Response(status=200)


async def update_vendor_instructions1(request: web.Request, quote_id, body) -> web.Response:
    """Updates instructions for all vendors performing the jobs in a quote.

    Updates instructions for all vendors performing the jobs in a quote. See also \&quot;PUT /jobs/{jobId}/instructions\&quot; for updating instructions for a specific job in a project or quote.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str
    :param body: Updated instructions for all vendors performing the jobs in a quote.
    :type body: dict | bytes

    """
    body = StringDTO.from_dict(body)
    return web.Response(status=200)


async def update_volume1(request: web.Request, quote_id, body) -> web.Response:
    """Updates volume for a quote.

    Updates volume for a quote.

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str
    :param body: Updated volume for a quote.
    :type body: dict | bytes

    """
    body = BigDecimalDTO.from_dict(body)
    return web.Response(status=200)


async def upload_file3(request: web.Request, quote_id, file=None) -> web.Response:
    """Uploads file to the quote as a file uploaded by PM.

    Uploads file to the quote as a file uploaded by PM. Only one file can be uploaded at once. When the upload is finished the file has to be added by specifying its category and languages (see \&quot;PUT /v2/quotes/{quoteId}/files/add\&quot; operation).

    :param quote_id: quote&#39;s internal identifier
    :type quote_id: str
    :param file: 
    :type file: str

    """
    return web.Response(status=200)
