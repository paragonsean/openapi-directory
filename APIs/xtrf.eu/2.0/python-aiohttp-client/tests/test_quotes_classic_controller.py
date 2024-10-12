# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.common_language_combination_dto import CommonLanguageCombinationDTO
from openapi_server.models.custom_field_dto import CustomFieldDTO
from openapi_server.models.finance_dto import FinanceDTO
from openapi_server.models.instructions_dto import InstructionsDTO
from openapi_server.models.payable_create_dto import PayableCreateDTO
from openapi_server.models.payable_dto import PayableDTO
from openapi_server.models.quote_dtov1 import QuoteDTOv1
from openapi_server.models.quote_dates_dto import QuoteDatesDTO
from openapi_server.models.receivable_create_dto import ReceivableCreateDTO
from openapi_server.models.receivable_dto import ReceivableDTO
from openapi_server.models.task_dto import TaskDTO


pytestmark = pytest.mark.asyncio

async def test_create_language_combination1(client):
    """Test case for create_language_combination1

    Creates a new language combination for a given quote without creating a task.
    """
    body = {"sourceLanguageId":0,"targetLanguageId":6}
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/quotes/{quote_id}/languageCombinations'.format(quote_id='quote_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_payable1(client):
    """Test case for create_payable1

    Adds a payable.
    """
    body = {"rateOrigin":"PRICE_PROFILE","quantity":2.3021358869347655,"catLogFile":{"name":"name","content":"content","url":"url","token":"token"},"description":"description","type":"SIMPLE","ignoreMinimumCharge":True,"jobId":"{}","languageCombinationIdNumber":"languageCombinationIdNumber","total":9.301444243932576,"calculationUnitId":0,"rate":7.061401241503109,"minimumCharge":5.637376656633329,"languageCombination":{"sourceLanguageId":5,"targetLanguageId":2},"invoiceId":"invoiceId","id":1,"currencyId":6,"jobTypeId":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/quotes/{quote_id}/finance/payables'.format(quote_id='quote_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_receivable1(client):
    """Test case for create_receivable1

    Adds a receivable.
    """
    body = {"rateOrigin":"PRICE_PROFILE","quantity":2.3021358869347655,"catLogFile":{"name":"name","content":"content","url":"url","token":"token"},"description":"description","type":"SIMPLE","ignoreMinimumCharge":True,"languageCombinationIdNumber":"languageCombinationIdNumber","total":3.616076749251911,"calculationUnitId":0,"rate":7.061401241503109,"minimumCharge":5.637376656633329,"languageCombination":{"sourceLanguageId":5,"targetLanguageId":2},"invoiceId":"invoiceId","id":1,"currencyId":6,"jobTypeId":5,"taskId":9}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/quotes/{quote_id}/finance/receivables'.format(quote_id='quote_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_task1(client):
    """Test case for create_task1

    Creates a new task for a given quote.
    """
    body = {"instructions":{"internal":"internal","notes":"notes","forProvider":"forProvider","paymentNoteForCustomer":"paymentNoteForCustomer","fromCustomer":"fromCustomer","paymentNoteForVendor":"paymentNoteForVendor"},"customFields":[{"name":"name","type":"TEXT","value":"{}","key":"key"},{"name":"name","type":"TEXT","value":"{}","key":"key"}],"jobs":{"jobIds":[1,1],"jobCount":6},"dates":{"actualDeliveryDate":{"value":6},"actualStartDate":{"value":6},"deadline":{"value":6},"startDate":{"value":6}},"idNumber":"idNumber","people":{"customerContacts":{"sendBackToId":5,"primaryId":5,"additionalIds":[1,1]},"responsiblePersons":{"projectCoordinatorId":2,"projectManagerId":7}},"clientTaskPONumber":"clientTaskPONumber","quoteId":5,"name":"name","languageCombination":{"sourceLanguageId":0,"targetLanguageId":6},"id":0,"projectId":5,"finance":{"invoiceable":True}}
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/quotes/{quote_id}/tasks'.format(quote_id='quote_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete13(client):
    """Test case for delete13

    Removes a quote.
    """
    headers = { 
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/home-api/quotes/{quote_id}'.format(quote_id='quote_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_payable1(client):
    """Test case for delete_payable1

    Deletes a payable.
    """
    headers = { 
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/home-api/quotes/{quote_id}/finance/payables/{payable_id}'.format(quote_id='quote_id_example', payable_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_receivable1(client):
    """Test case for delete_receivable1

    Deletes a receivable.
    """
    headers = { 
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/home-api/quotes/{quote_id}/finance/receivables/{receivable_id}'.format(quote_id='quote_id_example', receivable_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_ids7(client):
    """Test case for get_all_ids7

    Returns quotes' internal identifiers.
    """
    params = [('updatedSince', 56)]
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/quotes/ids',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_by_id8(client):
    """Test case for get_by_id8

    Returns quote details.
    """
    params = [('embed', 'embed_example')]
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/quotes/{quote_id}'.format(quote_id='quote_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_custom_fields6(client):
    """Test case for get_custom_fields6

    Returns custom fields of a given quote.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/quotes/{quote_id}/customFields'.format(quote_id='quote_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dates2(client):
    """Test case for get_dates2

    Returns dates of a given quote.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/quotes/{quote_id}/dates'.format(quote_id='quote_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_finance1(client):
    """Test case for get_finance1

    Returns finance of a given quote.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/quotes/{quote_id}/finance'.format(quote_id='quote_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_instructions1(client):
    """Test case for get_instructions1

    Returns instructions of a given quote.
    """
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/home-api/quotes/{quote_id}/instructions'.format(quote_id='quote_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send1(client):
    """Test case for send1

    Sends a quote for customer confirmation.
    """
    headers = { 
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/quotes/{quote_id}/confirmation/send'.format(quote_id='quote_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start(client):
    """Test case for start

    Starts a quote.
    """
    headers = { 
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/home-api/quotes/{quote_id}/start'.format(quote_id='quote_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_custom_fields4(client):
    """Test case for update_custom_fields4

    Updates custom fields of a given quote.
    """
    body = {"name":"name","type":"TEXT","value":"{}","key":"key"}
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/quotes/{quote_id}/customFields'.format(quote_id='quote_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_instructions2(client):
    """Test case for update_instructions2

    Updates instructions of a given quote.
    """
    body = {"internal":"internal","notes":"notes","forProvider":"forProvider","paymentNoteForCustomer":"paymentNoteForCustomer","fromCustomer":"fromCustomer","paymentNoteForVendor":"paymentNoteForVendor"}
    headers = { 
        'Accept': 'application/vnd.xtrf-v1+json;charset=UTF-8',
        'Content-Type': 'application/json',
        'X-AUTH-ACCESS-TOKEN': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/home-api/quotes/{quote_id}/instructions'.format(quote_id='quote_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_payable1(client):
    """Test case for update_payable1

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
        path='/home-api/quotes/{quote_id}/finance/payables/{payable_id}'.format(quote_id='quote_id_example', payable_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_receivable1(client):
    """Test case for update_receivable1

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
        path='/home-api/quotes/{quote_id}/finance/receivables/{receivable_id}'.format(quote_id='quote_id_example', receivable_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

