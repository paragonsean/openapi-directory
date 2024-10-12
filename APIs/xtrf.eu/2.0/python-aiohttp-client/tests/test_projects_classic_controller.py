# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.classic_project_create_dto import ClassicProjectCreateDTO
from openapi_server.models.common_language_combination_dto import CommonLanguageCombinationDTO
from openapi_server.models.contacts_dto import ContactsDTO
from openapi_server.models.custom_field_dto import CustomFieldDTO
from openapi_server.models.finance_dto import FinanceDTO
from openapi_server.models.instructions_dto import InstructionsDTO
from openapi_server.models.payable_create_dto import PayableCreateDTO
from openapi_server.models.payable_dto import PayableDTO
from openapi_server.models.project_dtov1 import ProjectDTOv1
from openapi_server.models.project_dates_dto import ProjectDatesDTO
from openapi_server.models.receivable_create_dto import ReceivableCreateDTO
from openapi_server.models.receivable_dto import ReceivableDTO
from openapi_server.models.task_create_dto import TaskCreateDTO
from openapi_server.models.task_dto import TaskDTO


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json;charset&#x3D;UTF-8 not supported by Connexion")
async def test_create5(client):
    """Test case for create5

    Creates a new Classic Project.
    """
    body = /home-api/assets/examples/v1/projects/createProject.json#requestBody
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/projects',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_language_combination(client):
    """Test case for create_language_combination

    Creates a new language combination for a given project without creating a task.
    """
    body = {"sourceLanguageId":0,"targetLanguageId":6}
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/projects/{project_id}/languageCombinations'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_payable(client):
    """Test case for create_payable

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
        path='/home-api/projects/{project_id}/finance/payables'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_receivable(client):
    """Test case for create_receivable

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
        path='/home-api/projects/{project_id}/finance/receivables'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_task(client):
    """Test case for create_task

    Creates a new task for a given project.
    """
    body = {"instructions":{"internal":"internal","notes":"notes","forProvider":"forProvider","paymentNoteForCustomer":"paymentNoteForCustomer","fromCustomer":"fromCustomer","paymentNoteForVendor":"paymentNoteForVendor"},"name":"name","files":[{"name":"name","category":"WORKFILE","content":"content","url":"url","token":"token"},{"name":"name","category":"WORKFILE","content":"content","url":"url","token":"token"}],"languageCombination":{"sourceLanguageId":0,"targetLanguageId":6},"dates":{"actualDeliveryDate":{"value":6},"actualStartDate":{"value":6},"deadline":{"value":6},"startDate":{"value":6}},"specializationId":0,"people":{"customerContacts":{"sendBackToId":5,"primaryId":5,"additionalIds":[1,1]},"responsiblePersons":{"projectCoordinatorId":2,"projectManagerId":7}},"clientTaskPONumber":"clientTaskPONumber","workflowId":6}
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/projects/{project_id}/tasks'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete12(client):
    """Test case for delete12

    Removes a project.
    """
    headers = { 
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/home-api/projects/{project_id}'.format(project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_payable(client):
    """Test case for delete_payable

    Deletes a payable.
    """
    headers = { 
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/home-api/projects/{project_id}/finance/payables/{payable_id}'.format(project_id='project_id_example', payable_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_receivable(client):
    """Test case for delete_receivable

    Deletes a receivable.
    """
    headers = { 
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/home-api/projects/{project_id}/finance/receivables/{receivable_id}'.format(project_id='project_id_example', receivable_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_ids6(client):
    """Test case for get_all_ids6

    Returns projects' internal identifiers.
    """
    params = [('updatedSince', 56)]
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/projects/ids',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_by_id7(client):
    """Test case for get_by_id7

    Returns project details.
    """
    params = [('embed', 'embed_example')]
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/projects/{project_id}'.format(project_id='project_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_contacts(client):
    """Test case for get_contacts

    Returns contacts of a given project.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/projects/{project_id}/contacts'.format(project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_custom_fields5(client):
    """Test case for get_custom_fields5

    Returns custom fields of a given project.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/projects/{project_id}/customFields'.format(project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dates1(client):
    """Test case for get_dates1

    Returns dates of a given project.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/projects/{project_id}/dates'.format(project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_file_by_id(client):
    """Test case for get_file_by_id

    Downloads a file.
    """
    headers = { 
        'Accept': 'multipart/form-data',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/projects/files/{file_id}/download'.format(file_id='file_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_finance(client):
    """Test case for get_finance

    Returns finance of a given project.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/projects/{project_id}/finance'.format(project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_instructions(client):
    """Test case for get_instructions

    Returns instructions of a given project.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/projects/{project_id}/instructions'.format(project_id='project_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_contacts(client):
    """Test case for update_contacts

    Updates contacts of a given project.
    """
    body = {"sendBackToId":5,"primaryId":5,"additionalIds":[1,1]}
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/projects/{project_id}/contacts'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_custom_fields3(client):
    """Test case for update_custom_fields3

    Updates custom fields of a given project.
    """
    body = {"name":"name","type":"TEXT","value":"{}","key":"key"}
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/projects/{project_id}/customFields'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_dates1(client):
    """Test case for update_dates1

    Updates dates of a given project.
    """
    body = {"actualDeliveryDate":{"value":6},"actualStartDate":{"value":6},"deadline":{"value":6},"startDate":{"value":6}}
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/projects/{project_id}/dates'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_instructions1(client):
    """Test case for update_instructions1

    Updates instructions of a given project.
    """
    body = {"internal":"internal","notes":"notes","forProvider":"forProvider","paymentNoteForCustomer":"paymentNoteForCustomer","fromCustomer":"fromCustomer","paymentNoteForVendor":"paymentNoteForVendor"}
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/projects/{project_id}/instructions'.format(project_id='project_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_payable(client):
    """Test case for update_payable

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
        path='/home-api/projects/{project_id}/finance/payables/{payable_id}'.format(project_id='project_id_example', payable_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_receivable(client):
    """Test case for update_receivable

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
        path='/home-api/projects/{project_id}/finance/receivables/{receivable_id}'.format(project_id='project_id_example', receivable_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

