# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_kb_dto import CreateKbDTO
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.knowledgebase_dto import KnowledgebaseDTO
from openapi_server.models.knowledgebases_dto import KnowledgebasesDTO
from openapi_server.models.operation import Operation
from openapi_server.models.qn_a_documents_dto import QnADocumentsDTO
from openapi_server.models.replace_kb_dto import ReplaceKbDTO
from openapi_server.models.update_kb_operation_dto import UpdateKbOperationDTO


pytestmark = pytest.mark.asyncio

async def test_knowledgebase_create(client):
    """Test case for knowledgebase_create

    Asynchronous operation to create a new knowledgebase.
    """
    create_kb_payload = {"enableHierarchicalExtraction":True,"qnaList":[{"metadata":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"answer":"answer","context":"{}","questions":["questions","questions"],"id":0,"source":"source"},{"metadata":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"answer":"answer","context":"{}","questions":["questions","questions"],"id":0,"source":"source"}],"urls":["urls","urls"],"name":"name","files":[{"fileName":"fileName","fileUri":"fileUri"},{"fileName":"fileName","fileUri":"fileUri"}],"language":"language","defaultAnswerUsedForExtraction":"defaultAnswerUsedForExtraction"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/knowledgebases/create',
        headers=headers,
        json=create_kb_payload,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_knowledgebase_delete(client):
    """Test case for knowledgebase_delete

    Deletes the knowledgebase and all its data.
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/knowledgebases/{kb_id}'.format(kb_id='kb_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_knowledgebase_download(client):
    """Test case for knowledgebase_download

    Download the knowledgebase.
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/knowledgebases/{kb_id}/{environment}/qna'.format(kb_id='kb_id_example', environment='environment_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_knowledgebase_get_details(client):
    """Test case for knowledgebase_get_details

    Gets details of a specific knowledgebase.
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/knowledgebases/{kb_id}'.format(kb_id='kb_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_knowledgebase_list_all(client):
    """Test case for knowledgebase_list_all

    Gets all knowledgebases for a user.
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/knowledgebases',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_knowledgebase_publish(client):
    """Test case for knowledgebase_publish

    Publishes all changes in test index of a knowledgebase to its prod index.
    """
    headers = { 
        'Accept': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/knowledgebases/{kb_id}'.format(kb_id='kb_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_knowledgebase_replace(client):
    """Test case for knowledgebase_replace

    Replace knowledgebase contents.
    """
    replace_kb = {"qnAList":[{"metadata":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"answer":"answer","context":"{}","questions":["questions","questions"],"id":0,"source":"source"},{"metadata":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"answer":"answer","context":"{}","questions":["questions","questions"],"id":0,"source":"source"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/knowledgebases/{kb_id}'.format(kb_id='kb_id_example'),
        headers=headers,
        json=replace_kb,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_knowledgebase_update(client):
    """Test case for knowledgebase_update

    Asynchronous operation to modify a knowledgebase.
    """
    update_kb = {"add":"{}","enableHierarchicalExtraction":True,"update":"{}","defaultAnswerUsedForExtraction":"defaultAnswerUsedForExtraction","delete":"{}"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apim_key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/knowledgebases/{kb_id}'.format(kb_id='kb_id_example'),
        headers=headers,
        json=update_kb,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

