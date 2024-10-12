# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_report import AccountReport
from openapi_server.models.article import Article
from openapi_server.models.article_complete import ArticleComplete
from openapi_server.models.article_complete_private import ArticleCompletePrivate
from openapi_server.models.article_confidentiality import ArticleConfidentiality
from openapi_server.models.article_create import ArticleCreate
from openapi_server.models.article_doi import ArticleDOI
from openapi_server.models.article_embargo import ArticleEmbargo
from openapi_server.models.article_embargo_updater import ArticleEmbargoUpdater
from openapi_server.models.article_handle import ArticleHandle
from openapi_server.models.article_search import ArticleSearch
from openapi_server.models.article_update import ArticleUpdate
from openapi_server.models.article_versions import ArticleVersions
from openapi_server.models.article_with_project import ArticleWithProject
from openapi_server.models.author import Author
from openapi_server.models.authors_creator import AuthorsCreator
from openapi_server.models.categories_creator import CategoriesCreator
from openapi_server.models.category import Category
from openapi_server.models.confidentiality_creator import ConfidentialityCreator
from openapi_server.models.error_message import ErrorMessage
from openapi_server.models.file_creator import FileCreator
from openapi_server.models.file_id import FileId
from openapi_server.models.location import Location
from openapi_server.models.location_warnings import LocationWarnings
from openapi_server.models.location_warnings_update import LocationWarningsUpdate
from openapi_server.models.private_article_search import PrivateArticleSearch
from openapi_server.models.private_file import PrivateFile
from openapi_server.models.private_link import PrivateLink
from openapi_server.models.private_link_creator import PrivateLinkCreator
from openapi_server.models.private_link_response import PrivateLinkResponse
from openapi_server.models.public_file import PublicFile
from openapi_server.models.resource import Resource


pytestmark = pytest.mark.asyncio

async def test_account_article_report(client):
    """Test case for account_article_report

    Account Article Report
    """
    params = [('group_id', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/articles/export',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_article_report_generate(client):
    """Test case for account_article_report_generate

    Initiate a new Report
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/articles/export',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_details(client):
    """Test case for article_details

    View article details
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/articles/{article_id}'.format(article_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_file_details(client):
    """Test case for article_file_details

    Article file details
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/articles/{article_id}/files/{file_id}'.format(article_id=56, file_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_files(client):
    """Test case for article_files

    List article files
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/articles/{article_id}/files'.format(article_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_version_confidentiality(client):
    """Test case for article_version_confidentiality

    Public Article Confidentiality for article version
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/articles/{article_id}/versions/{v_number}/confidentiality'.format(article_id=56, v_number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_version_details(client):
    """Test case for article_version_details

    Article details for version
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/articles/{article_id}/versions/{v_number}'.format(article_id=56, v_number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_version_embargo(client):
    """Test case for article_version_embargo

    Public Article Embargo for article version
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/articles/{article_id}/versions/{v_number}/embargo'.format(article_id=56, v_number=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_version_update(client):
    """Test case for article_version_update

    Update article version
    """
    body = {"categories_by_source_id":["300204","400207"],"custom_fields_list":[{"name":"key","value":"value"},{"name":"key","value":"value"}],"funding":"","keywords":["tag1","tag2"],"references":["http://figshare.com","http://api.figshare.com"],"custom_fields":{"defined_key":"value for it"},"description":"Test description of article","handle":"","title":"Test article title","tags":["tag1","tag2"],"defined_type":"media","funding_list":[{"id":0,"title":"title"},{"id":0,"title":"title"}],"license":1,"group_id":0,"resource_doi":"","resource_title":"","is_metadata_record":True,"timeline":{"firstOnline":"2015-12-31","publisherAcceptance":"2015-12-31","publisherPublication":"2015-12-31"},"metadata_reason":"hosted somewhere else","categories":[1,10,11],"authors":[{"name":"John Doe"},{"id":1000008}],"doi":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/account/articles/{article_id}/versions/{version_id}'.format(article_id=56, version_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_version_update_thumb(client):
    """Test case for article_version_update_thumb

    Update article version thumbnail
    """
    body = {"file_id":123}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/account/articles/{article_id}/versions/{version_id}/update_thumb'.format(article_id=56, version_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_article_versions(client):
    """Test case for article_versions

    List article versions
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/articles/{article_id}/versions'.format(article_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_articles_list(client):
    """Test case for articles_list

    Public Articles
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
                    ('item_type', 56),
                    ('doi', 'doi_example'),
                    ('handle', 'handle_example')]
    headers = { 
        'Accept': 'application/json',
        'x_cursor': 'x_cursor_example',
    }
    response = await client.request(
        method='GET',
        path='/v2/articles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_articles_search(client):
    """Test case for articles_search

    Public Articles Search
    """
    body = {"project_id":1,"item_type":1,"resource_doi":"10.6084/m9.figshare.1407024","handle":"111084/m9.figshare.14074","doi":"10.6084/m9.figshare.1407024","order":"published_date"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_cursor': 'x_cursor_example',
    }
    response = await client.request(
        method='POST',
        path='/v2/articles/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_article_author_delete(client):
    """Test case for private_article_author_delete

    Delete article author
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/account/articles/{article_id}/authors/{author_id}'.format(article_id=56, author_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_article_authors_add(client):
    """Test case for private_article_authors_add

    Add article authors
    """
    body = {"authors":[{"id":12121},{"id":34345},{"name":"John Doe"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/articles/{article_id}/authors'.format(article_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_article_authors_list(client):
    """Test case for private_article_authors_list

    List article authors
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/articles/{article_id}/authors'.format(article_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_article_authors_replace(client):
    """Test case for private_article_authors_replace

    Replace article authors
    """
    body = {"authors":[{"id":12121},{"id":34345},{"name":"John Doe"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/account/articles/{article_id}/authors'.format(article_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_article_categories_add(client):
    """Test case for private_article_categories_add

    Add article categories
    """
    body = {"categories":[1,10,11]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/articles/{article_id}/categories'.format(article_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_article_categories_list(client):
    """Test case for private_article_categories_list

    List article categories
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/articles/{article_id}/categories'.format(article_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_article_categories_replace(client):
    """Test case for private_article_categories_replace

    Replace article categories
    """
    body = {"categories":[1,10,11]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/account/articles/{article_id}/categories'.format(article_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_article_category_delete(client):
    """Test case for private_article_category_delete

    Delete article category
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/account/articles/{article_id}/categories/{category_id}'.format(article_id=56, category_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_article_confidentiality_delete(client):
    """Test case for private_article_confidentiality_delete

    Delete article confidentiality
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/account/articles/{article_id}/confidentiality'.format(article_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_article_confidentiality_details(client):
    """Test case for private_article_confidentiality_details

    Article confidentiality details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/articles/{article_id}/confidentiality'.format(article_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_article_confidentiality_update(client):
    """Test case for private_article_confidentiality_update

    Update article confidentiality
    """
    body = {"reason":"reason"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/account/articles/{article_id}/confidentiality'.format(article_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_article_create(client):
    """Test case for private_article_create

    Create new Article
    """
    body = {"categories_by_source_id":["300204","400207"],"custom_fields_list":[{"name":"key","value":"value"},{"name":"key","value":"value"}],"funding":"","keywords":["tag1","tag2"],"references":["http://figshare.com","http://api.figshare.com"],"custom_fields":{"defined_key":"value for it"},"description":"Test description of article","handle":"","title":"Test article title","tags":["tag1","tag2"],"defined_type":"media","funding_list":[{"id":0,"title":"title"},{"id":0,"title":"title"}],"license":1,"group_id":6,"resource_doi":"","resource_title":"","is_metadata_record":True,"timeline":{"firstOnline":"2015-12-31","publisherAcceptance":"2015-12-31","publisherPublication":"2015-12-31"},"metadata_reason":"hosted somewhere else","categories":[1,10,11],"authors":[{"name":"John Doe"},{"id":1000008}],"doi":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/articles',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_article_delete(client):
    """Test case for private_article_delete

    Delete article
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/account/articles/{article_id}'.format(article_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_article_details(client):
    """Test case for private_article_details

    Article details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/articles/{article_id}'.format(article_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_article_embargo_delete(client):
    """Test case for private_article_embargo_delete

    Delete Article Embargo
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/account/articles/{article_id}/embargo'.format(article_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_article_embargo_details(client):
    """Test case for private_article_embargo_details

    Article Embargo Details
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/articles/{article_id}/embargo'.format(article_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_article_embargo_update(client):
    """Test case for private_article_embargo_update

    Update Article Embargo
    """
    body = {"embargo_type":"file","is_embargoed":True,"embargo_date":"2018-05-22T04:04:04","embargo_title":"File(s) under embargo","embargo_reason":"","embargo_options":[{"id":1321},{"id":3345},{"group_ids":[4332,5433,678],"id":54621}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/account/articles/{article_id}/embargo'.format(article_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_article_file(client):
    """Test case for private_article_file

    Single File
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/articles/{article_id}/files/{file_id}'.format(article_id=56, file_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_article_file_delete(client):
    """Test case for private_article_file_delete

    File Delete
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/account/articles/{article_id}/files/{file_id}'.format(article_id=56, file_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_article_files_list(client):
    """Test case for private_article_files_list

    List article files
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/articles/{article_id}/files'.format(article_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_article_private_link(client):
    """Test case for private_article_private_link

    List private links
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/articles/{article_id}/private_links'.format(article_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_article_private_link_create(client):
    """Test case for private_article_private_link_create

    Create private link
    """
    body = {"read_only":True,"expires_date":"2018-02-22 22:22:22"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/articles/{article_id}/private_links'.format(article_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_article_private_link_delete(client):
    """Test case for private_article_private_link_delete

    Disable private link
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/account/articles/{article_id}/private_links/{link_id}'.format(article_id=56, link_id='link_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_article_private_link_update(client):
    """Test case for private_article_private_link_update

    Update private link
    """
    body = {"read_only":True,"expires_date":"2018-02-22 22:22:22"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/account/articles/{article_id}/private_links/{link_id}'.format(article_id=56, link_id='link_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_article_publish(client):
    """Test case for private_article_publish

    Private Article Publish
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/articles/{article_id}/publish'.format(article_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_article_reserve_doi(client):
    """Test case for private_article_reserve_doi

    Private Article Reserve DOI
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/articles/{article_id}/reserve_doi'.format(article_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_article_reserve_handle(client):
    """Test case for private_article_reserve_handle

    Private Article Reserve Handle
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/articles/{article_id}/reserve_handle'.format(article_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_article_resource(client):
    """Test case for private_article_resource

    Private Article Resource
    """
    body = {"link":"https://docs.figshare.com","id":"aaaa23512","title":"Test title","version":1,"doi":"","status":"frozen"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/articles/{article_id}/resource'.format(article_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_article_update(client):
    """Test case for private_article_update

    Update article
    """
    body = {"categories_by_source_id":["300204","400207"],"custom_fields_list":[{"name":"key","value":"value"},{"name":"key","value":"value"}],"funding":"","keywords":["tag1","tag2"],"references":["http://figshare.com","http://api.figshare.com"],"custom_fields":{"defined_key":"value for it"},"description":"Test description of article","handle":"","title":"Test article title","tags":["tag1","tag2"],"defined_type":"media","funding_list":[{"id":0,"title":"title"},{"id":0,"title":"title"}],"license":1,"group_id":0,"resource_doi":"","resource_title":"","is_metadata_record":True,"timeline":{"firstOnline":"2015-12-31","publisherAcceptance":"2015-12-31","publisherPublication":"2015-12-31"},"metadata_reason":"hosted somewhere else","categories":[1,10,11],"authors":[{"name":"John Doe"},{"id":1000008}],"doi":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/account/articles/{article_id}'.format(article_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_article_upload_complete(client):
    """Test case for private_article_upload_complete

    Complete Upload
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/articles/{article_id}/files/{file_id}'.format(article_id=56, file_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_article_upload_initiate(client):
    """Test case for private_article_upload_initiate

    Initiate Upload
    """
    body = {"size":70,"link":"http://figshare.com/file.txt","name":"test.py","md5":"6c16e6e7d7587bd078e5117dda01d565"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/articles/{article_id}/files'.format(article_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_articles_list(client):
    """Test case for private_articles_list

    Private Articles
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
        path='/v2/account/articles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_articles_search(client):
    """Test case for private_articles_search

    Private Articles search
    """
    body = {"resource_id":"1407024"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/articles/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

