# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_find_slice_data(client):
    """Test case for find_slice_data

    
    """
    params = [('branch', 'branch_example'),
                    ('id', 'id_example'),
                    ('direction', 'around'),
                    ('size', 50)]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fe/commit-graph-v1/slice/{repository}'.format(repository='repository_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_repositories(client):
    """Test case for get_all_repositories

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fe/repositories-v1',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_changeset(client):
    """Test case for get_changeset

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fe/revisionData-v1/changeset/{repository}/{csid}'.format(csid='csid_example', repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_changeset_details(client):
    """Test case for get_changeset_details

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service-fe/commit-graph-v1/details/{repository}'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_changesets_for_text(client):
    """Test case for get_changesets_for_text

    
    """
    params = [('rep', 'rep_example'),
                    ('path', 'path_example'),
                    ('committer', 'committer_example'),
                    ('comment', 'comment_example'),
                    ('p4JobFixed', 'p4_job_fixed_example'),
                    ('expand', 'expand_example'),
                    ('beforeCsid', 'before_csid_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fe/changeset-v1/listChangesets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_cross_repository_query(client):
    """Test case for get_cross_repository_query

    
    """
    params = [('query', 'query_example'),
                    ('repository', 'repository_example'),
                    ('expand', 'expand_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fe/search-v1/crossRepositoryQuery',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_path_list(client):
    """Test case for get_path_list

    
    """
    params = [('path', 'path_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fe/revisionData-v1/pathList/{repository}'.format(repository='repository_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_query(client):
    """Test case for get_query

    
    """
    params = [('query', 'query_example'),
                    ('maxReturn', 'max_return_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fe/search-v1/query/{repository}'.format(repository='repository_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_query_as_rows(client):
    """Test case for get_query_as_rows

    
    """
    params = [('query', 'query_example'),
                    ('maxReturn', 'max_return_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fe/search-v1/queryAsRows/{repository}'.format(repository='repository_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_repository_info(client):
    """Test case for get_repository_info

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fe/repositories-v1/{repository}'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_reviews_for_changeset(client):
    """Test case for get_reviews_for_changeset

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service-fe/search-v1/reviewsForChangeset/{repository}'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_reviews_for_changesets(client):
    """Test case for get_reviews_for_changesets

    
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/context/rest-service-fe/search-v1/reviewsForChangesets/{repository}'.format(repository='repository_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_revision_info(client):
    """Test case for get_revision_info

    
    """
    params = [('path', 'path_example'),
                    ('revision', 'revision_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fe/revisionData-v1/revisionInfo/{repository}'.format(repository='repository_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_changesets(client):
    """Test case for list_changesets

    
    """
    params = [('path', 'path_example'),
                    ('start', 'start_example'),
                    ('end', 'end_example'),
                    ('maxReturn', 'max_return_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fe/revisionData-v1/changesetList/{repository}'.format(repository='repository_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_path_history(client):
    """Test case for list_path_history

    
    """
    params = [('path', 'path_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fe/revisionData-v1/pathHistory/{repository}'.format(repository='repository_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_tags_for_revision(client):
    """Test case for list_tags_for_revision

    
    """
    params = [('path', 'path_example'),
                    ('revision', 'revision_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/context/rest-service-fe/revisionData-v1/revisionTags/{repository}'.format(repository='repository_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

