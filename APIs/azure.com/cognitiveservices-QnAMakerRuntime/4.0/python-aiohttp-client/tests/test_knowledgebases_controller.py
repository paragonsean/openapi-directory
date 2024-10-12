# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.feedback_records_dto import FeedbackRecordsDTO
from openapi_server.models.qn_a_search_result_list import QnASearchResultList
from openapi_server.models.query_dto import QueryDTO


pytestmark = pytest.mark.asyncio

async def test_runtime_generate_answer(client):
    """Test case for runtime_generate_answer

    GenerateAnswer call to query the knowledgebase.
    """
    generate_answer_payload = {"scoreThreshold":0.8008281904610115,"qnaId":"qnaId","question":"question","top":6,"isTest":True,"rankerType":"rankerType","context":"{}","strictFilters":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"userId":"userId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'auth_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/knowledgebases/{kb_id}/generateAnswer'.format(kb_id='kb_id_example'),
        headers=headers,
        json=generate_answer_payload,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_runtime_train(client):
    """Test case for runtime_train

    Train call to add suggestions to the knowledgebase.
    """
    train_payload = {"feedbackRecords":[{"qnaId":0,"userId":"userId","userQuestion":"userQuestion"},{"qnaId":0,"userId":"userId","userQuestion":"userQuestion"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'auth_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/knowledgebases/{kb_id}/train'.format(kb_id='kb_id_example'),
        headers=headers,
        json=train_payload,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

