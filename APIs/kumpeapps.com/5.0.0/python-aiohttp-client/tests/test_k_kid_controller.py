# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_user_response import AddUserResponse
from openapi_server.models.allowance import Allowance
from openapi_server.models.chorelist import Chorelist
from openapi_server.models.model201_share import Model201Share
from openapi_server.models.model405 import Model405
from openapi_server.models.model412 import Model412
from openapi_server.models.nodata import Nodata
from openapi_server.models.success import Success
from openapi_server.models.userlist import Userlist
from openapi_server.models.wishlist import Wishlist


pytestmark = pytest.mark.asyncio

async def test_kkid_allowance_get(client):
    """Test case for kkid_allowance_get

    returns allowance balance and allowance transactions
    """
    params = [('kidUserId', 56),
                    ('transactionDays', 56)]
    headers = { 
        'Accept': 'application/json',
        'auth_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v5/kkid/allowance',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_kkid_allowance_post(client):
    """Test case for kkid_allowance_post

    adds new allowance transaction to kidUserID
    """
    params = [('kidUserId', 56),
                    ('amount', 3.4),
                    ('description', 'description_example'),
                    ('transactionType', 'transaction_type_example')]
    headers = { 
        'Accept': 'application/json',
        'auth_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v5/kkid/allowance',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_kkid_apns_post(client):
    """Test case for kkid_apns_post

    subscribes/unsubscribes/registers for apns push notifications
    """
    params = [('kidUserId', 56),
                    ('tool', 'tool_example'),
                    ('token', 'token_example'),
                    ('devicename', 'devicename_example'),
                    ('title', 'title_example'),
                    ('message', 'message_example'),
                    ('badge', 56),
                    ('sound', 'sound_example'),
                    ('section', 'section_example'),
                    ('priority', 'priority_example')]
    headers = { 
        'Accept': 'application/json',
        'auth_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v5/kkid/apns',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_kkid_chorelist_delete(client):
    """Test case for kkid_chorelist_delete

    deletes chore for given chore id
    """
    params = [('idChoreList', 56)]
    headers = { 
        'Accept': 'application/json',
        'auth_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v5/kkid/chorelist',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_kkid_chorelist_get(client):
    """Test case for kkid_chorelist_get

    returns list of chores for given user
    """
    params = [('kidUsername', 'kid_username_example'),
                    ('day', 'day_example'),
                    ('status', 'status_example'),
                    ('blockDash', True),
                    ('optional', True),
                    ('canSteal', True),
                    ('includeCalendar', True)]
    headers = { 
        'Accept': 'application/json',
        'auth_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v5/kkid/chorelist',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_kkid_chorelist_post(client):
    """Test case for kkid_chorelist_post

    adds chore for given user
    """
    params = [('kidUsername', 'kid_username_example'),
                    ('day', 'day_example'),
                    ('nfcTag', 'nfc_tag_example'),
                    ('status', 'status_example'),
                    ('choreName', 'chore_name_example'),
                    ('choreDescription', 'chore_description_example'),
                    ('choreNumber', 56),
                    ('blockDash', True),
                    ('oneTime', True),
                    ('extraAllowance', 56),
                    ('optional', True),
                    ('reassignable', True),
                    ('canSteal', True),
                    ('startDate', 'start_date_example'),
                    ('notes', 'notes_example'),
                    ('requireObjectDetection', True),
                    ('objectDetectionTag', 'object_detection_tag_example'),
                    ('updatedByAutomation', True),
                    ('aiIcon', 'ai_icon_example'),
                    ('isCalendar', True)]
    headers = { 
        'Accept': 'application/json',
        'auth_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v5/kkid/chorelist',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_kkid_chorelist_put(client):
    """Test case for kkid_chorelist_put

    updates chore for given chore id
    """
    params = [('idChoreList', 56),
                    ('status', 'status_example'),
                    ('stolen', True),
                    ('stolenBy', 'stolen_by_example'),
                    ('nfcTag', 'nfc_tag_example'),
                    ('notes', 'notes_example'),
                    ('latitude', 56),
                    ('longitude', 56),
                    ('altitude', 56),
                    ('updatedByAutomation', True),
                    ('whereDay', 'where_day_example'),
                    ('whereStatus', 'where_status_example'),
                    ('whereName', 'where_name_example')]
    headers = { 
        'Accept': 'application/json',
        'auth_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v5/kkid/chorelist',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_kkid_masteruser_post(client):
    """Test case for kkid_masteruser_post

    adds new master user account
    """
    params = [('username', 'username_example'),
                    ('password', 'password_example'),
                    ('email', 'email_example'),
                    ('firstName', 'first_name_example'),
                    ('lastName', 'last_name_example')]
    headers = { 
        'Accept': 'application/json',
        'app_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v5/kkid/masteruser',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_kkid_share_get(client):
    """Test case for kkid_share_get

    Create Share Link
    """
    params = [('linkUserId', 'link_user_id_example'),
                    ('link', 'link_example'),
                    ('scope', 'scope_example'),
                    ('scope2', 'scope2_example'),
                    ('scope3', 'scope3_example'),
                    ('scope4', 'scope4_example')]
    headers = { 
        'Accept': 'application/json',
        'auth_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v5/kkid/share',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_kkid_user_get(client):
    """Test case for kkid_user_get

    Gets user info
    """
    params = [('enableBool', True)]
    headers = { 
        'Accept': 'application/json',
        'auth_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v5/kkid/user',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_kkid_userlist_delete(client):
    """Test case for kkid_userlist_delete

    deletes user
    """
    params = [('userID', 56)]
    headers = { 
        'Accept': 'application/json',
        'auth_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v5/kkid/userlist',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_kkid_userlist_get(client):
    """Test case for kkid_userlist_get

    returns list of users
    """
    params = [('isChild', True),
                    ('isActive', True),
                    ('isAdmin', True),
                    ('enableAllowance', True),
                    ('enableChores', True),
                    ('userID', 56),
                    ('username', 'username_example'),
                    ('email', 'email_example')]
    headers = { 
        'Accept': 'application/json',
        'auth_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v5/kkid/userlist',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_kkid_userlist_post(client):
    """Test case for kkid_userlist_post

    adds new child user
    """
    params = [('username', 'username_example'),
                    ('password', 'password_example'),
                    ('email', 'email_example'),
                    ('firstName', 'first_name_example'),
                    ('lastName', 'last_name_example')]
    headers = { 
        'Accept': 'application/json',
        'auth_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v5/kkid/userlist',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_kkid_userlist_put(client):
    """Test case for kkid_userlist_put

    updates user
    """
    params = [('userID', 56),
                    ('username', 'username_example'),
                    ('email', 'email_example'),
                    ('firstName', 'first_name_example'),
                    ('lastName', 'last_name_example'),
                    ('emoji', 'emoji_example'),
                    ('tmdbKey', 'tmdb_key_example'),
                    ('enableWishList', True),
                    ('enableChores', True),
                    ('enableAllowance', True),
                    ('enableAdmin', True),
                    ('enableTmdb', True),
                    ('enableObjectDetection', True)]
    headers = { 
        'Accept': 'application/json',
        'auth_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v5/kkid/userlist',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_kkid_wishlist_delete(client):
    """Test case for kkid_wishlist_delete

    Delete item from wishlist
    """
    params = [('wishId', 56)]
    headers = { 
        'Accept': 'application/json',
        'auth_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v5/kkid/wishlist',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_kkid_wishlist_get(client):
    """Test case for kkid_wishlist_get

    Get list of wishlist items
    """
    params = [('kidUserId', 56)]
    headers = { 
        'Accept': 'application/json',
        'auth_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v5/kkid/wishlist',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_kkid_wishlist_post(client):
    """Test case for kkid_wishlist_post

    Add item to kid's wishlist
    """
    params = [('kidUserId', 56),
                    ('title', 'title_example'),
                    ('description', 'description_example'),
                    ('priority', 56),
                    ('link', 'link_example')]
    headers = { 
        'Accept': 'application/json',
        'auth_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v5/kkid/wishlist',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_kkid_wishlist_put(client):
    """Test case for kkid_wishlist_put

    Update item on kid's wishlist
    """
    params = [('wishId', 56),
                    ('title', 'title_example'),
                    ('description', 'description_example'),
                    ('priority', 56),
                    ('link', 'link_example')]
    headers = { 
        'Accept': 'application/json',
        'auth_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v5/kkid/wishlist',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

