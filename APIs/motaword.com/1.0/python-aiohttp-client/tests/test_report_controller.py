# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.filter_contents import FilterContents
from openapi_server.models.filter_dates import FilterDates
from openapi_server.models.language_pairs_report import LanguagePairsReport
from openapi_server.models.project_list import ProjectList
from openapi_server.models.qa_filter import QaFilter
from openapi_server.models.qa_warnings import QaWarnings
from openapi_server.models.report_filter import ReportFilter
from openapi_server.models.users_report import UsersReport


pytestmark = pytest.mark.asyncio

async def test_generate_qa_report(client):
    """Test case for generate_qa_report

    Generate a QA report for given filter
    """
    body = {"budget_codes":["budget_codes","budget_codes"],"target_languages":["target_languages","target_languages"],"clients":[0.8008281904610115,0.8008281904610115],"projects":[1.4658129805029452,1.4658129805029452],"documents":[6.027456183070403,6.027456183070403],"subjects":["subjects","subjects"],"source_languages":["source_languages","source_languages"],"categories":["categories","categories"],"date_to":"2000-01-23T04:56:07.000+00:00","vendors":[5.962133916683182,5.962133916683182],"date_from":"2000-01-23T04:56:07.000+00:00","severities":["severities","severities"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/reports/qa',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_filter_contents(client):
    """Test case for get_filter_contents

    Returns available options for selected timeframe.
    """
    body = {"date_to":"2000-01-23T04:56:07.000+00:00","date_from":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/reports/filter',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_language_pairs_report(client):
    """Test case for get_language_pairs_report

    Language pairs report
    """
    body = {"target_languages":["target_languages","target_languages"],"budget_code":"budget_code","source_languages":["source_languages","source_languages"],"date_to":"2000-01-23T04:56:07.000+00:00","users":[0,0],"date_from":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/reports/language-pairs',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_projects_report(client):
    """Test case for get_projects_report

    Projects report
    """
    body = {"target_languages":["target_languages","target_languages"],"budget_code":"budget_code","source_languages":["source_languages","source_languages"],"date_to":"2000-01-23T04:56:07.000+00:00","users":[0,0],"date_from":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/reports/projects',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users_report(client):
    """Test case for get_users_report

    Company users report
    """
    body = {"target_languages":["target_languages","target_languages"],"budget_code":"budget_code","source_languages":["source_languages","source_languages"],"date_to":"2000-01-23T04:56:07.000+00:00","users":[0,0],"date_from":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/reports/users',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

