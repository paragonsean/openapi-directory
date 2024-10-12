# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.by_country import ByCountry
from openapi_server.models.pageview_article import PageviewArticle
from openapi_server.models.pageview_project import PageviewProject
from openapi_server.models.pageview_tops import PageviewTops
from openapi_server.models.problem import Problem


pytestmark = pytest.mark.asyncio

async def test_metrics_pageviews_aggregate_project_access_agent_granularity_start_end_get(client):
    """Test case for metrics_pageviews_aggregate_project_access_agent_granularity_start_end_get

    Get pageview counts for a project.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest_v1/metrics/pageviews/aggregate/{project}/{access}/{agent}/{granularity}/{start}/{end}'.format(project='project_example', access='access_example', agent='agent_example', granularity='granularity_example', start='start_example', end='end_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metrics_pageviews_per_article_project_access_agent_article_granularity_start_end_get(client):
    """Test case for metrics_pageviews_per_article_project_access_agent_article_granularity_start_end_get

    Get pageview counts for a page.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest_v1/metrics/pageviews/per-article/{project}/{access}/{agent}/{article}/{granularity}/{start}/{end}'.format(project='project_example', access='access_example', agent='agent_example', article='article_example', granularity='granularity_example', start='start_example', end='end_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metrics_pageviews_top_by_country_project_access_year_month_get(client):
    """Test case for metrics_pageviews_top_by_country_project_access_year_month_get

    Get pageviews by country and access method.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest_v1/metrics/pageviews/top-by-country/{project}/{access}/{year}/{month}'.format(project='project_example', access='access_example', year='year_example', month='month_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_metrics_pageviews_top_project_access_year_month_day_get(client):
    """Test case for metrics_pageviews_top_project_access_year_month_day_get

    Get the most viewed articles for a project.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest_v1/metrics/pageviews/top/{project}/{access}/{year}/{month}/{day}'.format(project='project_example', access='access_example', year='year_example', month='month_example', day='day_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

