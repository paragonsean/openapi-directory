# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.hyperparameter_model import HyperparameterModel


pytestmark = pytest.mark.asyncio

async def test_hyperparameter_get(client):
    """Test case for hyperparameter_get

    Get hyperparameters
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
    }
    response = await client.request(
        method='GET',
        path='/hyperparameter',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_hyperparameter_post(client):
    """Test case for hyperparameter_post

    Set hyperparameters
    """
    body = {"abcClassificationThresholdC":0.95,"discardData":False,"errorType":"MeanAbsolutePercentageError","periodicity":12,"xyzClassificationThresholdZ":0.6,"xyzClassificationThresholdX":0.3,"xyzClassificationThresholdY":0.6,"noFcst":18,"abcClassificationThresholdA":0.8,"abcClassificationThresholdB":0.95,"holdOutPeriod":4,"outlierDetection":True}
    headers = { 
        'Content-Type': 'application/*+json',
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/hyperparameter',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

