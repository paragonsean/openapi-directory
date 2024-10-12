# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.big_decimal_dto import BigDecimalDTO
from openapi_server.models.cat_tool_project_dto import CATToolProjectDTO
from openapi_server.models.custom_field_dto import CustomFieldDTO
from openapi_server.models.external_file_dto import ExternalFileDto
from openapi_server.models.file_categorizations_dto import FileCategorizationsDto
from openapi_server.models.file_dto import FileDto
from openapi_server.models.file_link_categorizations_dto import FileLinkCategorizationsDto
from openapi_server.models.files_archive_dto import FilesArchiveDto
from openapi_server.models.files_dto import FilesDto
from openapi_server.models.finance_dto import FinanceDTO
from openapi_server.models.job_dto import JobDto
from openapi_server.models.payable_create_dto import PayableCreateDTO
from openapi_server.models.payable_dto import PayableDTO
from openapi_server.models.project_create_dto import ProjectCreateDTO
from openapi_server.models.project_dtov2 import ProjectDTOv2
from openapi_server.models.project_file_dto import ProjectFileDto
from openapi_server.models.project_status_dto import ProjectStatusDTO
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

async def test_add_external_file_links(client):
    """Test case for add_external_file_links

    
    """
    body = {"filename":"filename","languageCombinationIds":[{"sourceLanguageId":1,"targetLanguageId":5},{"sourceLanguageId":1,"targetLanguageId":5}],"externalInfo":{"key":"externalInfo"},"languageIds":[0,0],"category":"category"}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/v2/projects/{project_id}/files/addExternalLink'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_file_links1(client):
    """Test case for add_file_links1

    Adds file links to the project as added by PM.
    """
    body = {"fileLinks":[{"filename":"filename","toBeGenerated":True,"languageCombinationIds":[{"sourceLanguageId":1,"targetLanguageId":5},{"sourceLanguageId":1,"targetLanguageId":5}],"externalInfo":{"key":"externalInfo"},"languageIds":[0,0],"category":"category","url":"url"},{"filename":"filename","toBeGenerated":True,"languageCombinationIds":[{"sourceLanguageId":1,"targetLanguageId":5},{"sourceLanguageId":1,"targetLanguageId":5}],"externalInfo":{"key":"externalInfo"},"languageIds":[0,0],"category":"category","url":"url"}]}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/v2/projects/{project_id}/files/addLink'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_files1(client):
    """Test case for add_files1

    Adds files to the project as added by PM.
    """
    body = {"files":[{"languageCombinationIds":[{"sourceLanguageId":1,"targetLanguageId":5},{"sourceLanguageId":1,"targetLanguageId":5}],"languageIds":[0,0],"category":"category","fileId":"fileId"},{"languageCombinationIds":[{"sourceLanguageId":1,"targetLanguageId":5},{"sourceLanguageId":1,"targetLanguageId":5}],"languageIds":[0,0],"category":"category","fileId":"fileId"}]}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/projects/{project_id}/files/add'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_job_to_process(client):
    """Test case for add_job_to_process

    Returns process id.
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/v2/projects/{project_id}/addJob'.format(project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_archive(client):
    """Test case for archive

    Prepares a ZIP archive that contains the specified files.
    """
    body = {"files":["files","files"]}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/v2/projects/files/archive',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_status2(client):
    """Test case for change_status2

    Changes project status if possible (400 Bad Request is returned otherwise).
    """
    body = {"status":"status"}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/projects/{project_id}/status'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create6(client):
    """Test case for create6

    Creates a new Smart Project.
    """
    body = {"clientId":0,"name":"name","externalId":"externalId","serviceId":6}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/v2/projects',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_payable2(client):
    """Test case for create_payable2

    Adds a payable to a project.
    """
    body = {"rateOrigin":"PRICE_PROFILE","quantity":2.3021358869347655,"catLogFile":{"name":"name","content":"content","url":"url","token":"token"},"description":"description","type":"SIMPLE","ignoreMinimumCharge":True,"jobId":"{}","languageCombinationIdNumber":"languageCombinationIdNumber","total":9.301444243932576,"calculationUnitId":0,"rate":7.061401241503109,"minimumCharge":5.637376656633329,"languageCombination":{"sourceLanguageId":5,"targetLanguageId":2},"invoiceId":"invoiceId","id":1,"currencyId":6,"jobTypeId":5}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/v2/projects/{project_id}/finance/payables'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_receivable2(client):
    """Test case for create_receivable2

    Adds a receivable to a project.
    """
    body = {"rateOrigin":"PRICE_PROFILE","quantity":2.3021358869347655,"catLogFile":{"name":"name","content":"content","url":"url","token":"token"},"description":"description","type":"SIMPLE","ignoreMinimumCharge":True,"languageCombinationIdNumber":"languageCombinationIdNumber","total":3.616076749251911,"calculationUnitId":0,"rate":7.061401241503109,"minimumCharge":5.637376656633329,"languageCombination":{"sourceLanguageId":5,"targetLanguageId":2},"invoiceId":"invoiceId","id":1,"currencyId":6,"jobTypeId":5,"taskId":9}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/v2/projects/{project_id}/finance/receivables'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_payable2(client):
    """Test case for delete_payable2

    Deletes a payable.
    """
    headers = { 
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/home-api/v2/projects/{project_id}/finance/payables/{payable_id}'.format(project_id='project_id_example', payable_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_receivable2(client):
    """Test case for delete_receivable2

    Deletes a receivable.
    """
    headers = { 
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/home-api/v2/projects/{project_id}/finance/receivables/{receivable_id}'.format(project_id='project_id_example', receivable_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_by_external_id1(client):
    """Test case for get_by_external_id1

    Returns project details.
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/v2/projects/for-external-id/{external_project_id}'.format(external_project_id='external_project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_by_id9(client):
    """Test case for get_by_id9

    Returns project details.
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/v2/projects/{project_id}'.format(project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cat_tool_project_info(client):
    """Test case for get_cat_tool_project_info

    Returns if cat tool project is created or queued.
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/v2/projects/{project_id}/catToolProject'.format(project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_contacts2(client):
    """Test case for get_contacts2

    Returns Client Contacts information for a project.
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/v2/projects/{project_id}/clientContacts'.format(project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_custom_fields8(client):
    """Test case for get_custom_fields8

    Returns a list of custom field keys and values for a project.
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/v2/projects/{project_id}/customFields'.format(project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_deliverable_files(client):
    """Test case for get_deliverable_files

    Returns list of files in a project, that are ready to be delivered to client.
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/v2/projects/{project_id}/files/deliverable'.format(project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_file_by_id2(client):
    """Test case for get_file_by_id2

    Returns details of a file.
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/v2/projects/files/{file_id}'.format(file_id='file_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_file_content_by_id(client):
    """Test case for get_file_content_by_id

    Downloads a file content.
    """
    headers = { 
        'Accept': 'multipart/form-data',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/v2/projects/files/{file_id}/download/{file_name}'.format(file_id='file_id_example', file_name='file_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_files(client):
    """Test case for get_files

    Returns list of files in a project.
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/v2/projects/{project_id}/files'.format(project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_finance2(client):
    """Test case for get_finance2

    Returns finance information for a project.
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/v2/projects/{project_id}/finance'.format(project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_jobs(client):
    """Test case for get_jobs

    Returns list of jobs in a project.
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/v2/projects/{project_id}/jobs'.format(project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_process_id(client):
    """Test case for get_process_id

    Returns process id.
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/v2/projects/{project_id}/process'.format(project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_client_deadline(client):
    """Test case for update_client_deadline

    Updates Client Deadline for a project.
    """
    body = {"value":6}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/projects/{project_id}/clientDeadline'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_client_notes(client):
    """Test case for update_client_notes

    Updates Client Notes for a project.
    """
    body = {"value":"value"}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/projects/{project_id}/clientNotes'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_client_reference_number(client):
    """Test case for update_client_reference_number

    Updates Client Reference Number for a project.
    """
    body = {"value":"value"}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/projects/{project_id}/clientReferenceNumber'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_contacts2(client):
    """Test case for update_contacts2

    Updates Client Contacts for a project.
    """
    body = {"primaryId":6,"additionalIds":[0,0]}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/projects/{project_id}/clientContacts'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_custom_field2(client):
    """Test case for update_custom_field2

    Updates a custom field with a specified key in a project
    """
    body = {"value":"{}"}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/projects/{project_id}/customFields/{key}'.format(project_id='project_id_example', key='key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_internal_notes(client):
    """Test case for update_internal_notes

    Updates Internal Notes for a project.
    """
    body = {"value":"value"}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/projects/{project_id}/internalNotes'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_ordered_on(client):
    """Test case for update_ordered_on

    Updates Order Date for a project.
    """
    body = {"value":6}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/projects/{project_id}/orderDate'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_payable2(client):
    """Test case for update_payable2

    Updates a payable.
    """
    body = {"rateOrigin":"PRICE_PROFILE","quantity":9.301444243932576,"description":"description","type":"SIMPLE","ignoreMinimumCharge":True,"jobId":"{}","languageCombinationIdNumber":"languageCombinationIdNumber","total":2.027123023002322,"calculationUnitId":0,"rate":3.616076749251911,"minimumCharge":7.061401241503109,"languageCombination":{"sourceLanguageId":5,"targetLanguageId":2},"invoiceId":"invoiceId","id":1,"currencyId":6,"jobTypeId":5}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/projects/{project_id}/finance/payables/{payable_id}'.format(project_id='project_id_example', payable_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_receivable2(client):
    """Test case for update_receivable2

    Updates a receivable.
    """
    body = {"rateOrigin":"PRICE_PROFILE","quantity":2.3021358869347655,"description":"description","type":"SIMPLE","ignoreMinimumCharge":True,"languageCombinationIdNumber":"languageCombinationIdNumber","total":3.616076749251911,"calculationUnitId":0,"rate":7.061401241503109,"minimumCharge":5.637376656633329,"languageCombination":{"sourceLanguageId":5,"targetLanguageId":2},"invoiceId":"invoiceId","id":1,"currencyId":6,"jobTypeId":5,"taskId":9}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/projects/{project_id}/finance/receivables/{receivable_id}'.format(project_id='project_id_example', receivable_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_source_language(client):
    """Test case for update_source_language

    Updates source language for a project.
    """
    body = {"sourceLanguageId":0}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/projects/{project_id}/sourceLanguage'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_specialization(client):
    """Test case for update_specialization

    Updates specialization for a project.
    """
    body = {"specializationId":0}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/projects/{project_id}/specialization'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_target_languages(client):
    """Test case for update_target_languages

    Updates target languages for a project.
    """
    body = {"targetLanguageIds":[0,0]}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/projects/{project_id}/targetLanguages'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_vendor_instructions(client):
    """Test case for update_vendor_instructions

    Updates instructions for all vendors performing the jobs in a project.
    """
    body = {"value":"value"}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/projects/{project_id}/vendorInstructions'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_volume(client):
    """Test case for update_volume

    Updates volume for a project.
    """
    body = {"value":0.8008281904610115}
    headers = { 
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/v2/projects/{project_id}/volume'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_upload_file2(client):
    """Test case for upload_file2

    Uploads file to the project as a file uploaded by PM.
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
        path='/home-api/v2/projects/{project_id}/files/upload'.format(project_id='project_id_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

