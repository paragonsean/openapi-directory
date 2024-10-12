# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.crawl import Crawl
from openapi_server.models.crawl_read import CrawlRead
from openapi_server.models.crawl_read_details import CrawlReadDetails
from openapi_server.models.crawl_write import CrawlWrite


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_cancel_crawl_item(client):
    """Test case for cancel_crawl_item

    Creates a Crawl resource.
    """
    crawl = {"archived":True,"createdAt":"2000-01-23T04:56:07.000+00:00","currentConcurrency":5,"marking":["marking","marking"],"stats":["stats","stats"],"author":{"userOrganizations":[{"organization":"organization","id":"id","functionalRoles":["functionalRoles","functionalRoles"],"user":"user"},{"organization":"organization","id":"id","functionalRoles":["functionalRoles","functionalRoles"],"user":"user"}],"plainPasswordRepeat":"{}","defaultOrganization":{"userOrganizations":[{"organization":"organization","id":"id","functionalRoles":["functionalRoles","functionalRoles"],"user":"user"},{"organization":"organization","id":"id","functionalRoles":["functionalRoles","functionalRoles"],"user":"user"}],"createdAt":"2000-01-23T04:56:07.000+00:00","projects":[{"usersFlattened":[{"project":"project","functionalRoles":["functionalRoles","functionalRoles"],"user":"user"},{"project":"project","functionalRoles":["functionalRoles","functionalRoles"],"user":"user"}],"isPublishing":True,"configuration":["configuration","configuration"],"straightRulesCount":5,"onboardingCompletedDemos":["onboardingCompletedDemos","onboardingCompletedDemos"],"straightRulesUpdatedAt":"2000-01-23T04:56:07.000+00:00","currentVersion":{"createdAt":"2000-01-23T04:56:07.000+00:00","current":True,"mergedRulesCount":6,"publishedAt":"2000-01-23T04:56:07.000+00:00","name":"name","working":True,"id":"id","isSnapshot":True},"token":"token","workingVersion":{"createdAt":"2000-01-23T04:56:07.000+00:00","current":True,"mergedRulesCount":6,"publishedAt":"2000-01-23T04:56:07.000+00:00","name":"name","working":True,"id":"id","isSnapshot":True},"complexRulesCount":0,"createdAt":"2000-01-23T04:56:07.000+00:00","rulesHash":"rulesHash","ignoreProjectTypes":["ignoreProjectTypes","ignoreProjectTypes"],"userProjects":[{"project":"project","id":"id","functionalRoles":["functionalRoles","functionalRoles"],"user":"user"},{"project":"project","id":"id","functionalRoles":["functionalRoles","functionalRoles"],"user":"user"}],"name":"name","id":"id","complexRulesUpdatedAt":"2000-01-23T04:56:07.000+00:00","plan":1,"slug":"slug","updatedAt":"2000-01-23T04:56:07.000+00:00"},{"usersFlattened":[{"project":"project","functionalRoles":["functionalRoles","functionalRoles"],"user":"user"},{"project":"project","functionalRoles":["functionalRoles","functionalRoles"],"user":"user"}],"isPublishing":True,"configuration":["configuration","configuration"],"straightRulesCount":5,"onboardingCompletedDemos":["onboardingCompletedDemos","onboardingCompletedDemos"],"straightRulesUpdatedAt":"2000-01-23T04:56:07.000+00:00","currentVersion":{"createdAt":"2000-01-23T04:56:07.000+00:00","current":True,"mergedRulesCount":6,"publishedAt":"2000-01-23T04:56:07.000+00:00","name":"name","working":True,"id":"id","isSnapshot":True},"token":"token","workingVersion":{"createdAt":"2000-01-23T04:56:07.000+00:00","current":True,"mergedRulesCount":6,"publishedAt":"2000-01-23T04:56:07.000+00:00","name":"name","working":True,"id":"id","isSnapshot":True},"complexRulesCount":0,"createdAt":"2000-01-23T04:56:07.000+00:00","rulesHash":"rulesHash","ignoreProjectTypes":["ignoreProjectTypes","ignoreProjectTypes"],"userProjects":[{"project":"project","id":"id","functionalRoles":["functionalRoles","functionalRoles"],"user":"user"},{"project":"project","id":"id","functionalRoles":["functionalRoles","functionalRoles"],"user":"user"}],"name":"name","id":"id","complexRulesUpdatedAt":"2000-01-23T04:56:07.000+00:00","plan":1,"slug":"slug","updatedAt":"2000-01-23T04:56:07.000+00:00"}],"name":"name","id":"id","slug":"slug","updatedAt":"2000-01-23T04:56:07.000+00:00"},"newEmailTokenExpiredAt":"2000-01-23T04:56:07.000+00:00","currentPassword":"{}","password":"password","plainPassword":"plainPassword","userProjects":["userProjects","userProjects"],"name":"name","newEmail":"newEmail","id":"id","newEmailToken":"newEmailToken","superAdmin":True,"email":"email","projectsFlattened":["projectsFlattened","projectsFlattened"],"updatedAt":"2000-01-23T04:56:07.000+00:00"},"firstUrl":"firstUrl","id":"id","trigger":"trigger","error":"error","finishedAt":"2000-01-23T04:56:07.000+00:00","updatedAt":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/crawls/{id}/cancel'.format(id='id_example'),
        headers=headers,
        json=crawl,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_crawl_collection(client):
    """Test case for get_crawl_collection

    Retrieves the collection of Crawl resources.
    """
    params = [('projectId', 'project_id_example'),
                    ('firstUrl', 'first_url_example'),
                    ('sort[createdAt]', 'sort_created_at_example'),
                    ('page', 56)]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/crawls',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_crawl_item(client):
    """Test case for get_crawl_item

    Retrieves a Crawl resource.
    """
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/crawls/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_post_crawl_collection(client):
    """Test case for post_crawl_collection

    Creates a Crawl resource.
    """
    crawl = openapi_server.CrawlWrite()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ld+json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/crawls',
        headers=headers,
        json=crawl,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

