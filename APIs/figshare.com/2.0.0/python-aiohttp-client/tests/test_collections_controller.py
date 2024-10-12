# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.article import Article
from openapi_server.models.articles_creator import ArticlesCreator
from openapi_server.models.author import Author
from openapi_server.models.authors_creator import AuthorsCreator
from openapi_server.models.categories_creator import CategoriesCreator
from openapi_server.models.category import Category
from openapi_server.models.collection import Collection
from openapi_server.models.collection_complete import CollectionComplete
from openapi_server.models.collection_complete_private import CollectionCompletePrivate
from openapi_server.models.collection_create import CollectionCreate
from openapi_server.models.collection_doi import CollectionDOI
from openapi_server.models.collection_handle import CollectionHandle
from openapi_server.models.collection_private_link_creator import CollectionPrivateLinkCreator
from openapi_server.models.collection_search import CollectionSearch
from openapi_server.models.collection_update import CollectionUpdate
from openapi_server.models.collection_versions import CollectionVersions
from openapi_server.models.error_message import ErrorMessage
from openapi_server.models.location import Location
from openapi_server.models.location_warnings import LocationWarnings
from openapi_server.models.location_warnings_update import LocationWarningsUpdate
from openapi_server.models.private_collection_search import PrivateCollectionSearch
from openapi_server.models.private_link import PrivateLink
from openapi_server.models.private_link_response import PrivateLinkResponse
from openapi_server.models.resource import Resource


pytestmark = pytest.mark.asyncio

async def test_collection_articles(client):
    """Test case for collection_articles

    Public Collection Articles
    """
    params = [('page', 56),
                    ('page_size', 10),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/collections/{collection_id}/articles'.format(collection_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collection_details(client):
    """Test case for collection_details

    Collection details
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/collections/{collection_id}'.format(collection_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collection_version_details(client):
    """Test case for collection_version_details

    Collection Version details
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/collections/{collection_id}/versions/{version_id}'.format(collection_id=56, version_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collection_versions(client):
    """Test case for collection_versions

    Collection Versions list
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/collections/{collection_id}/versions'.format(collection_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_list(client):
    """Test case for collections_list

    Public Collections
    """
    params = [('page', 56),
                    ('page_size', 10),
                    ('limit', 56),
                    ('offset', 56),
                    ('order', published_date),
                    ('order_direction', desc),
                    ('institution', 56),
                    ('published_since', 'published_since_example'),
                    ('modified_since', 'modified_since_example'),
                    ('group', 56),
                    ('resource_doi', 'resource_doi_example'),
                    ('doi', 'doi_example'),
                    ('handle', 'handle_example')]
    headers = { 
        'Accept': 'application/json',
        'x_cursor': 'x_cursor_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/collections',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_search(client):
    """Test case for collections_search

    Public Collections Search
    """
    body = {"resource_doi":"10.6084/m9.figshare.1407024","handle":"10084/figshare.1407024","doi":"10.6084/m9.figshare.1407024","order":"published_date"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_cursor': 'x_cursor_example',
    }
    response = await client.request(
        method='POST',
        path='/v2/collections/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_collection_article_delete(client):
    """Test case for private_collection_article_delete

    Delete collection article
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/account/collections/{collection_id}/articles/{article_id}'.format(collection_id=56, article_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_collection_articles_add(client):
    """Test case for private_collection_articles_add

    Add collection articles
    """
    body = {"articles":[2000003,2000004]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/collections/{collection_id}/articles'.format(collection_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_collection_articles_list(client):
    """Test case for private_collection_articles_list

    List collection articles
    """
    params = [('page', 56),
                    ('page_size', 10),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/collections/{collection_id}/articles'.format(collection_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_collection_articles_replace(client):
    """Test case for private_collection_articles_replace

    Replace collection articles
    """
    body = {"articles":[2000003,2000004]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/account/collections/{collection_id}/articles'.format(collection_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_collection_author_delete(client):
    """Test case for private_collection_author_delete

    Delete collection author
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/account/collections/{collection_id}/authors/{author_id}'.format(collection_id=56, author_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_collection_authors_add(client):
    """Test case for private_collection_authors_add

    Add collection authors
    """
    body = {"authors":[{"id":12121},{"id":34345},{"name":"John Doe"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/collections/{collection_id}/authors'.format(collection_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_collection_authors_list(client):
    """Test case for private_collection_authors_list

    List collection authors
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/collections/{collection_id}/authors'.format(collection_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_collection_authors_replace(client):
    """Test case for private_collection_authors_replace

    Replace collection authors
    """
    body = {"authors":[{"id":12121},{"id":34345},{"name":"John Doe"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/account/collections/{collection_id}/authors'.format(collection_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_collection_categories_add(client):
    """Test case for private_collection_categories_add

    Add collection categories
    """
    body = {"categories":[1,10,11]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/collections/{collection_id}/categories'.format(collection_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_collection_categories_list(client):
    """Test case for private_collection_categories_list

    List collection categories
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/collections/{collection_id}/categories'.format(collection_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_collection_categories_replace(client):
    """Test case for private_collection_categories_replace

    Replace collection categories
    """
    body = {"categories":[1,10,11]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/account/collections/{collection_id}/categories'.format(collection_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_collection_category_delete(client):
    """Test case for private_collection_category_delete

    Delete collection category
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/account/collections/{collection_id}/categories/{category_id}'.format(collection_id=56, category_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_collection_create(client):
    """Test case for private_collection_create

    Create collection
    """
    body = {"categories_by_source_id":["300204","400207"],"custom_fields_list":[{"name":"key","value":"value"},{"name":"key","value":"value"}],"funding":"","keywords":["tag1","tag2"],"references":["http://figshare.com","http://api.figshare.com"],"custom_fields":{"defined_key":"value for it"},"description":"Test description of article","handle":"","title":"Test collection title","resource_version":6,"tags":["tag1","tag2"],"funding_list":[{"id":0,"title":"title"},{"id":0,"title":"title"}],"resource_link":"resource_link","group_id":0,"resource_doi":"","resource_title":"","resource_id":"resource_id","timeline":{"firstOnline":"2015-12-31","publisherAcceptance":"2015-12-31","publisherPublication":"2015-12-31"},"categories":[1,10,11],"articles":[2000001,2000005],"authors":[{"name":"John Doe"},{"id":20005}],"doi":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/collections',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_collection_delete(client):
    """Test case for private_collection_delete

    Delete collection
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/account/collections/{collection_id}'.format(collection_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_collection_details(client):
    """Test case for private_collection_details

    Collection details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/collections/{collection_id}'.format(collection_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_collection_private_link_create(client):
    """Test case for private_collection_private_link_create

    Create collection private link
    """
    body = {"read_only":True,"expires_date":"2018-02-22 22:22:22"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/collections/{collection_id}/private_links'.format(collection_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_collection_private_link_delete(client):
    """Test case for private_collection_private_link_delete

    Disable private link
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/account/collections/{collection_id}/private_links/{link_id}'.format(collection_id=56, link_id='link_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_collection_private_link_update(client):
    """Test case for private_collection_private_link_update

    Update collection private link
    """
    body = {"read_only":True,"expires_date":"2018-02-22 22:22:22"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/account/collections/{collection_id}/private_links/{link_id}'.format(collection_id=56, link_id='link_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_collection_private_links_list(client):
    """Test case for private_collection_private_links_list

    List collection private links
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/collections/{collection_id}/private_links'.format(collection_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_collection_publish(client):
    """Test case for private_collection_publish

    Private Collection Publish
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/collections/{collection_id}/publish'.format(collection_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_collection_reserve_doi(client):
    """Test case for private_collection_reserve_doi

    Private Collection Reserve DOI
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/collections/{collection_id}/reserve_doi'.format(collection_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_collection_reserve_handle(client):
    """Test case for private_collection_reserve_handle

    Private Collection Reserve Handle
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/collections/{collection_id}/reserve_handle'.format(collection_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_collection_resource(client):
    """Test case for private_collection_resource

    Private Collection Resource
    """
    body = {"link":"https://docs.figshare.com","id":"aaaa23512","title":"Test title","version":1,"doi":"","status":"frozen"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/collections/{collection_id}/resource'.format(collection_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_collection_update(client):
    """Test case for private_collection_update

    Update collection
    """
    body = {"categories_by_source_id":["300204","400207"],"custom_fields_list":[{"name":"key","value":"value"},{"name":"key","value":"value"}],"funding":"","keywords":["tag1","tag2"],"references":["http://figshare.com","http://api.figshare.com"],"custom_fields":{"defined_key":"value for it"},"description":"Test description of collection","handle":"","title":"Test collection title","resource_version":6,"tags":["tag1","tag2"],"funding_list":[{"id":0,"title":"title"},{"id":0,"title":"title"}],"resource_link":"resource_link","group_id":0,"resource_doi":"","resource_title":"","resource_id":"resource_id","timeline":{"firstOnline":"2015-12-31","publisherAcceptance":"2015-12-31","publisherPublication":"2015-12-31"},"categories":[1,10,11],"articles":[2000001,2000005],"authors":[{"name":"John Doe"},{"id":20005}],"doi":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/account/collections/{collection_id}'.format(collection_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_collections_list(client):
    """Test case for private_collections_list

    Private Collections List
    """
    params = [('page', 56),
                    ('page_size', 10),
                    ('limit', 56),
                    ('offset', 56),
                    ('order', published_date),
                    ('order_direction', desc)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/collections',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_collections_search(client):
    """Test case for private_collections_search

    Private Collections Search
    """
    body = {"resource_id":"1407024"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/collections/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

