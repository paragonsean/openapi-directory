# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

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


pytestmark = pytest.mark.asyncio

async def test_add_files2(client):
    """Test case for add_files2

    Adds files to the quote as added by PM.
    """
    body = {"value":6}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/quotes/{quote_id}/files/add'.format(quote_id='quote_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json;charset&#x3D;UTF-8 not supported by Connexion")
async def test_archive1(client):
    """Test case for archive1

    Prepares a ZIP archive that contains the specified files.
    """
    body = /home-api/assets/examples/v2/quotes/archive.json#requestBody
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/v2/quotes/files/archive',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_status3(client):
    """Test case for change_status3

    Changes quote status if possible (400 Bad Request is returned otherwise).
    """
    body = {"status":"status"}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/quotes/{quote_id}/status'.format(quote_id='quote_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create7(client):
    """Test case for create7

    Creates a new Smart Quote.
    """
    body = {"opportunityOfferId":6,"clientId":0,"name":"name","serviceId":1}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/v2/quotes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_payable3(client):
    """Test case for create_payable3

    Adds a payable to a quote.
    """
    body = {"rateOrigin":"PRICE_PROFILE","quantity":2.3021358869347655,"catLogFile":{"name":"name","content":"content","url":"url","token":"token"},"description":"description","type":"SIMPLE","ignoreMinimumCharge":True,"jobId":"{}","languageCombinationIdNumber":"languageCombinationIdNumber","total":9.301444243932576,"calculationUnitId":0,"rate":7.061401241503109,"minimumCharge":5.637376656633329,"languageCombination":{"sourceLanguageId":5,"targetLanguageId":2},"invoiceId":"invoiceId","id":1,"currencyId":6,"jobTypeId":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/v2/quotes/{quote_id}/finance/payables'.format(quote_id='quote_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_receivable3(client):
    """Test case for create_receivable3

    Adds a receivable to a quote.
    """
    body = {"rateOrigin":"PRICE_PROFILE","quantity":2.3021358869347655,"catLogFile":{"name":"name","content":"content","url":"url","token":"token"},"description":"description","type":"SIMPLE","ignoreMinimumCharge":True,"languageCombinationIdNumber":"languageCombinationIdNumber","total":3.616076749251911,"calculationUnitId":0,"rate":7.061401241503109,"minimumCharge":5.637376656633329,"languageCombination":{"sourceLanguageId":5,"targetLanguageId":2},"invoiceId":"invoiceId","id":1,"currencyId":6,"jobTypeId":5,"taskId":9}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/v2/quotes/{quote_id}/finance/receivables'.format(quote_id='quote_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_payable3(client):
    """Test case for delete_payable3

    Deletes a payable.
    """
    headers = { 
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/home-api/v2/quotes/{quote_id}/finance/payables/{payable_id}'.format(quote_id='quote_id_example', payable_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_receivable3(client):
    """Test case for delete_receivable3

    Deletes a receivable.
    """
    headers = { 
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/home-api/v2/quotes/{quote_id}/finance/receivables/{receivable_id}'.format(quote_id='quote_id_example', receivable_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_by_id10(client):
    """Test case for get_by_id10

    Returns quote details.
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/v2/quotes/{quote_id}'.format(quote_id='quote_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_contacts3(client):
    """Test case for get_contacts3

    Returns Client Contacts information for a quote.
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/v2/quotes/{quote_id}/clientContacts'.format(quote_id='quote_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_custom_fields9(client):
    """Test case for get_custom_fields9

    Returns a list of custom field keys and values for a project.
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/v2/quotes/{quote_id}/customFields'.format(quote_id='quote_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_file_by_id3(client):
    """Test case for get_file_by_id3

    Returns details of a file.
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/v2/quotes/files/{file_id}'.format(file_id='file_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_file_content_by_id1(client):
    """Test case for get_file_content_by_id1

    Downloads a file content.
    """
    headers = { 
        'Accept': 'multipart/form-data',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/v2/quotes/files/{file_id}/download/{file_name}'.format(file_id='file_id_example', file_name='file_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_files1(client):
    """Test case for get_files1

    Returns list of files in a quote.
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/v2/quotes/{quote_id}/files'.format(quote_id='quote_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_finance3(client):
    """Test case for get_finance3

    Returns finance information for a quote.
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/v2/quotes/{quote_id}/finance'.format(quote_id='quote_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_jobs1(client):
    """Test case for get_jobs1

    Returns list of jobs in a quote.
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/v2/quotes/{quote_id}/jobs'.format(quote_id='quote_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_business_days(client):
    """Test case for update_business_days

    Updates Business Days for a quote.
    """
    body = /home-api/assets/examples/v2/quotes/updateBusinessDays.json#requestBody
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/quotes/{quote_id}/businessDays'.format(quote_id='quote_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_client_notes1(client):
    """Test case for update_client_notes1

    Updates Client Notes for a quote.
    """
    body = {"value":"value"}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/quotes/{quote_id}/clientNotes'.format(quote_id='quote_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_client_reference_number1(client):
    """Test case for update_client_reference_number1

    Updates Client Reference Number for a quote.
    """
    body = {"value":"value"}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/quotes/{quote_id}/clientReferenceNumber'.format(quote_id='quote_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json;charset&#x3D;UTF-8 not supported by Connexion")
async def test_update_contacts3(client):
    """Test case for update_contacts3

    Updates Client Contacts for a quote.
    """
    body = /home-api/assets/examples/v2/quotes/updateClientContacts.json#requestBody
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/quotes/{quote_id}/clientContacts'.format(quote_id='quote_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_custom_field3(client):
    """Test case for update_custom_field3

    Updates a custom field with a specified key in a quote.
    """
    body = {"value":"{}"}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/quotes/{quote_id}/customFields/{key}'.format(quote_id='quote_id_example', key='key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_expected_delivery_date(client):
    """Test case for update_expected_delivery_date

    Updates Expected Delivery Date for a quote.
    """
    body = {"value":6}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/quotes/{quote_id}/expectedDeliveryDate'.format(quote_id='quote_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_internal_notes1(client):
    """Test case for update_internal_notes1

    Updates Internal Notes for a quote.
    """
    body = {"value":"value"}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/quotes/{quote_id}/internalNotes'.format(quote_id='quote_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_payable3(client):
    """Test case for update_payable3

    Updates a payable.
    """
    body = {"rateOrigin":"PRICE_PROFILE","quantity":9.301444243932576,"description":"description","type":"SIMPLE","ignoreMinimumCharge":True,"jobId":"{}","languageCombinationIdNumber":"languageCombinationIdNumber","total":2.027123023002322,"calculationUnitId":0,"rate":3.616076749251911,"minimumCharge":7.061401241503109,"languageCombination":{"sourceLanguageId":5,"targetLanguageId":2},"invoiceId":"invoiceId","id":1,"currencyId":6,"jobTypeId":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/quotes/{quote_id}/finance/payables/{payable_id}'.format(quote_id='quote_id_example', payable_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_quote_expiry(client):
    """Test case for update_quote_expiry

    Updates Quote Expiry Date for a quote.
    """
    body = {"value":6}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/quotes/{quote_id}/quoteExpiry'.format(quote_id='quote_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_receivable3(client):
    """Test case for update_receivable3

    Updates a receivable.
    """
    body = {"rateOrigin":"PRICE_PROFILE","quantity":2.3021358869347655,"description":"description","type":"SIMPLE","ignoreMinimumCharge":True,"languageCombinationIdNumber":"languageCombinationIdNumber","total":3.616076749251911,"calculationUnitId":0,"rate":7.061401241503109,"minimumCharge":5.637376656633329,"languageCombination":{"sourceLanguageId":5,"targetLanguageId":2},"invoiceId":"invoiceId","id":1,"currencyId":6,"jobTypeId":5,"taskId":9}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/quotes/{quote_id}/finance/receivables/{receivable_id}'.format(quote_id='quote_id_example', receivable_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_source_language1(client):
    """Test case for update_source_language1

    Updates source language for a quote.
    """
    body = {"sourceLanguageId":0}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/quotes/{quote_id}/sourceLanguage'.format(quote_id='quote_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_specialization1(client):
    """Test case for update_specialization1

    Updates specialization for a quote.
    """
    body = {"specializationId":0}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/quotes/{quote_id}/specialization'.format(quote_id='quote_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_target_languages1(client):
    """Test case for update_target_languages1

    Updates target languages for a quote.
    """
    body = {"targetLanguageIds":[0,0]}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/quotes/{quote_id}/targetLanguages'.format(quote_id='quote_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_vendor_instructions1(client):
    """Test case for update_vendor_instructions1

    Updates instructions for all vendors performing the jobs in a quote.
    """
    body = {"value":"value"}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/quotes/{quote_id}/vendorInstructions'.format(quote_id='quote_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_volume1(client):
    """Test case for update_volume1

    Updates volume for a quote.
    """
    body = {"value":0.8008281904610115}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/quotes/{quote_id}/volume'.format(quote_id='quote_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_upload_file3(client):
    """Test case for upload_file3

    Uploads file to the quote as a file uploaded by PM.
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'multipart/form-data',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/home-api/v2/quotes/{quote_id}/files/upload'.format(quote_id='quote_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

