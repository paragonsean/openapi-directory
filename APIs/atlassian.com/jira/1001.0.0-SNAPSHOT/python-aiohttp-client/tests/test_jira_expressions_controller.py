# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_collection import ErrorCollection
from openapi_server.models.jira_expression_eval_request_bean import JiraExpressionEvalRequestBean
from openapi_server.models.jira_expression_for_analysis import JiraExpressionForAnalysis
from openapi_server.models.jira_expression_result import JiraExpressionResult
from openapi_server.models.jira_expressions_analysis import JiraExpressionsAnalysis


pytestmark = pytest.mark.asyncio

async def test_analyse_expression(client):
    """Test case for analyse_expression

    Analyse Jira expression
    """
    body = {"contextVariables":{"key":"contextVariables"},"expressions":"issues.map(issue => issue.properties['property_key'])"}
    params = [('check', syntax)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/expression/analyse',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_evaluate_jira_expression(client):
    """Test case for evaluate_jira_expression

    Evaluate Jira expression
    """
    body = {"expression":"{ key: issue.key, type: issue.issueType.name, links: issue.links.map(link => link.linkedIssue.id) }","context":""}
    params = [('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/rest/api/3/expression/eval',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

