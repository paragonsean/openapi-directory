# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.experiment_model import ExperimentModel
from openapi_server.models.message_model import MessageModel


pytestmark = pytest.mark.asyncio

async def test_create_experiment_using_post(client):
    """Test case for create_experiment_using_post

    createExperiment
    """
    body = {"measurementsEsQuery":"measurementsEsQuery","endDate":"2000-01-23T04:56:07.000+00:00","publishedStages":["publishedStages","publishedStages"],"percentHash":"percentHash","name":"name","active":True,"id":0,"complete":True,"config":{"playerMongoQuery":"playerMongoQuery","playerQuery":"playerQuery","variants":"variants"},"changedFieldsAndInitialValues":"{}","startDate":"2000-01-23T04:56:07.000+00:00","measurements":"measurements"}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/restv2/game/{api_key}/manage/experiments'.format(api_key='api_key_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_experiment_using_delete(client):
    """Test case for delete_experiment_using_delete

    deleteExperiment
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='DELETE',
        path='/restv2/game/{api_key}/manage/experiments/{id}'.format(api_key='api_key_example', id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_do_action_experiment_using_post(client):
    """Test case for do_action_experiment_using_post

    doActionExperiment
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='POST',
        path='/restv2/game/{api_key}/manage/experiments/{id}/{action}'.format(api_key='api_key_example', id=56, action='action_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_experiment_using_get(client):
    """Test case for get_experiment_using_get

    getExperiment
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/restv2/game/{api_key}/manage/experiments/{id}'.format(api_key='api_key_example', id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_experiments_using_get(client):
    """Test case for get_experiments_using_get

    getExperiments
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/restv2/game/{api_key}/manage/experiments'.format(api_key='api_key_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_experiment_using_put(client):
    """Test case for update_experiment_using_put

    updateExperiment
    """
    body = {"measurementsEsQuery":"measurementsEsQuery","endDate":"2000-01-23T04:56:07.000+00:00","publishedStages":["publishedStages","publishedStages"],"percentHash":"percentHash","name":"name","active":True,"id":0,"complete":True,"config":{"playerMongoQuery":"playerMongoQuery","playerQuery":"playerQuery","variants":"variants"},"changedFieldsAndInitialValues":"{}","startDate":"2000-01-23T04:56:07.000+00:00","measurements":"measurements"}
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/restv2/game/{api_key}/manage/experiments/{id}'.format(api_key='api_key_example', id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

