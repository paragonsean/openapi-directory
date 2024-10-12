# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.account_create import AccountCreate
from openapi_server.models.account_update import AccountUpdate
from openapi_server.models.article import Article
from openapi_server.models.category import Category
from openapi_server.models.curation import Curation
from openapi_server.models.curation_comment import CurationComment
from openapi_server.models.curation_comment_create import CurationCommentCreate
from openapi_server.models.curation_detail import CurationDetail
from openapi_server.models.error_message import ErrorMessage
from openapi_server.models.group import Group
from openapi_server.models.group_embargo_options import GroupEmbargoOptions
from openapi_server.models.institution import Institution
from openapi_server.models.institution_accounts_search import InstitutionAccountsSearch
from openapi_server.models.response_message import ResponseMessage
from openapi_server.models.role import Role
from openapi_server.models.short_account import ShortAccount
from openapi_server.models.short_custom_field import ShortCustomField
from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_account_institution_curation(client):
    """Test case for account_institution_curation

    Institution Curation Review
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/institution/review/{curation_id}'.format(curation_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_institution_curation_comments(client):
    """Test case for account_institution_curation_comments

    Institution Curation Review Comments
    """
    params = [('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/institution/review/{curation_id}/comments'.format(curation_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_institution_curations(client):
    """Test case for account_institution_curations

    Institution Curation Reviews
    """
    params = [('group_id', 56),
                    ('article_id', 56),
                    ('status', 'status_example'),
                    ('limit', 56),
                    ('offset', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/institution/reviews',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_institution_review_curation_id_comments_post(client):
    """Test case for account_institution_review_curation_id_comments_post

    POST Institution Curation Review Comment
    """
    body = {"text":"text"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/institution/review/{curation_id}/comments'.format(curation_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_fields_list(client):
    """Test case for custom_fields_list

    Private account institution group custom fields
    """
    params = [('group_id', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/institution/custom_fields',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_custom_fields_upload(client):
    """Test case for custom_fields_upload

    Custom fields values files upload
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('external_file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/v2/account/institution/custom_fields/{custom_field_id}/items/upload'.format(custom_field_id=56),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_institution_articles(client):
    """Test case for institution_articles

    Public Licenses
    """
    params = [('resource_id', 'resource_id_example'),
                    ('filename', 'filename_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/institutions/{institution_string_id}/articles/filter-by'.format(institution_string_id='institution_string_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_institution_hrfeed_upload(client):
    """Test case for institution_hrfeed_upload

    Private Institution HRfeed Upload
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('hrfeed', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/v2/institution/hrfeed/upload',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_account_institution_user(client):
    """Test case for private_account_institution_user

    Private Account Institution User
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/institution/users/{account_id}'.format(account_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_categories_list(client):
    """Test case for private_categories_list

    Private Account Categories
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/categories',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_group_embargo_options_details(client):
    """Test case for private_group_embargo_options_details

    Private Account Institution Group Embargo Options
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/institution/groups/{group_id}/embargo_options'.format(group_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_institution_account_group_role_delete(client):
    """Test case for private_institution_account_group_role_delete

    Delete Institution Account Group Role
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/account/institution/roles/{account_id}/{group_id}/{role_id}'.format(account_id=56, group_id=56, role_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_institution_account_group_roles(client):
    """Test case for private_institution_account_group_roles

    List Institution Account Group Roles
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/institution/roles/{account_id}'.format(account_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_institution_account_group_roles_create(client):
    """Test case for private_institution_account_group_roles_create

    Add Institution Account Group Roles
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/institution/roles/{account_id}'.format(account_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_institution_accounts_create(client):
    """Test case for private_institution_accounts_create

    Create new Institution Account
    """
    body = {"is_active":True,"group_id":0,"institution_user_id":"johndoe","quota":1000,"last_name":"Doe","first_name":"John","email":"johndoe@example.com","symplectic_user_id":"johndoe"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/institution/accounts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_institution_accounts_list(client):
    """Test case for private_institution_accounts_list

    Private Account Institution Accounts
    """
    params = [('page', 56),
                    ('page_size', 10),
                    ('limit', 56),
                    ('offset', 56),
                    ('is_active', 56),
                    ('institution_user_id', 'institution_user_id_example'),
                    ('email', 'email_example'),
                    ('id_lte', 56),
                    ('id_gte', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/institution/accounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_institution_accounts_search(client):
    """Test case for private_institution_accounts_search

    Private Account Institution Accounts Search
    """
    body = {"is_active":0,"offset":0,"institution_user_id":"alan","limit":10,"page":1,"email":"alan@institution.com","search_for":"figshare","page_size":10}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/account/institution/accounts/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_institution_accounts_update(client):
    """Test case for private_institution_accounts_update

    Update Institution Account
    """
    body = {"is_active":True,"group_id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/account/institution/accounts/{account_id}'.format(account_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_institution_articles(client):
    """Test case for private_institution_articles

    Private Institution Articles
    """
    params = [('page', 56),
                    ('page_size', 10),
                    ('limit', 56),
                    ('offset', 56),
                    ('order', published_date),
                    ('order_direction', desc),
                    ('published_since', 'published_since_example'),
                    ('modified_since', 'modified_since_example'),
                    ('status', 56),
                    ('resource_doi', 'resource_doi_example'),
                    ('item_type', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/institution/articles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_institution_details(client):
    """Test case for private_institution_details

    Private Account Institutions
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/institution',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_institution_embargo_options_details(client):
    """Test case for private_institution_embargo_options_details

    Private Account Institution embargo options
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/institution/embargo_options',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_institution_groups_list(client):
    """Test case for private_institution_groups_list

    Private Account Institution Groups
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/institution/groups',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_private_institution_roles_list(client):
    """Test case for private_institution_roles_list

    Private Account Institution Roles
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/account/institution/roles',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

