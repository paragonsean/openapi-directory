# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activity_list_public_events503_response import ActivityListPublicEvents503Response
from openapi_server.models.activity_list_repos_starred_by_user200_response import ActivityListReposStarredByUser200Response
from openapi_server.models.activity_list_stargazers_for_repo200_response import ActivityListStargazersForRepo200Response
from openapi_server.models.activity_mark_notifications_as_read202_response import ActivityMarkNotificationsAsRead202Response
from openapi_server.models.activity_mark_notifications_as_read_request import ActivityMarkNotificationsAsReadRequest
from openapi_server.models.activity_mark_repo_notifications_as_read_request import ActivityMarkRepoNotificationsAsReadRequest
from openapi_server.models.activity_set_repo_subscription_request import ActivitySetRepoSubscriptionRequest
from openapi_server.models.activity_set_thread_subscription_request import ActivitySetThreadSubscriptionRequest
from openapi_server.models.basic_error import BasicError
from openapi_server.models.enterprise_admin_update_org_name202_response import EnterpriseAdminUpdateOrgName202Response
from openapi_server.models.event import Event
from openapi_server.models.feed import Feed
from openapi_server.models.minimal_repository import MinimalRepository
from openapi_server.models.repository import Repository
from openapi_server.models.repository_subscription import RepositorySubscription
from openapi_server.models.simple_user import SimpleUser
from openapi_server.models.starred_repository import StarredRepository
from openapi_server.models.thread import Thread
from openapi_server.models.thread_subscription import ThreadSubscription
from openapi_server.models.validation_error import ValidationError


pytestmark = pytest.mark.asyncio

async def test_activity_check_repo_is_starred_by_authenticated_user(client):
    """Test case for activity_check_repo_is_starred_by_authenticated_user

    Check if a repository is starred by the authenticated user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/user/starred/{owner}/{repo}'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_delete_repo_subscription(client):
    """Test case for activity_delete_repo_subscription

    Delete a repository subscription
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/repos/{owner}/{repo}/subscription'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_delete_thread_subscription(client):
    """Test case for activity_delete_thread_subscription

    Delete a thread subscription
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/notifications/threads/{thread_id}/subscription'.format(thread_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_get_feeds(client):
    """Test case for activity_get_feeds

    Get feeds
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/feeds',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_get_repo_subscription(client):
    """Test case for activity_get_repo_subscription

    Get a repository subscription
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/subscription'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_get_thread(client):
    """Test case for activity_get_thread

    Get a thread
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/notifications/threads/{thread_id}'.format(thread_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_get_thread_subscription_for_authenticated_user(client):
    """Test case for activity_get_thread_subscription_for_authenticated_user

    Get a thread subscription for the authenticated user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/notifications/threads/{thread_id}/subscription'.format(thread_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_list_events_for_authenticated_user(client):
    """Test case for activity_list_events_for_authenticated_user

    List events for the authenticated user
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/users/{username}/events'.format(username='username_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_list_notifications_for_authenticated_user(client):
    """Test case for activity_list_notifications_for_authenticated_user

    List notifications for the authenticated user
    """
    params = [('all', False),
                    ('participating', False),
                    ('since', '2013-10-20T19:20:30+01:00'),
                    ('before', '2013-10-20T19:20:30+01:00'),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/notifications',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_list_org_events_for_authenticated_user(client):
    """Test case for activity_list_org_events_for_authenticated_user

    List organization events for the authenticated user
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/users/{username}/events/orgs/{org}'.format(username='username_example', org='org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_list_public_events(client):
    """Test case for activity_list_public_events

    List public events
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_list_public_events_for_repo_network(client):
    """Test case for activity_list_public_events_for_repo_network

    List public events for a network of repositories
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/networks/{owner}/{repo}/events'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_list_public_events_for_user(client):
    """Test case for activity_list_public_events_for_user

    List public events for a user
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/users/{username}/events/public'.format(username='username_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_list_public_org_events(client):
    """Test case for activity_list_public_org_events

    List public organization events
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/orgs/{org}/events'.format(org='org_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_list_received_events_for_user(client):
    """Test case for activity_list_received_events_for_user

    List events received by the authenticated user
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/users/{username}/received_events'.format(username='username_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_list_received_public_events_for_user(client):
    """Test case for activity_list_received_public_events_for_user

    List public events received by a user
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/users/{username}/received_events/public'.format(username='username_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_list_repo_events(client):
    """Test case for activity_list_repo_events

    List repository events
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/events'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_list_repo_notifications_for_authenticated_user(client):
    """Test case for activity_list_repo_notifications_for_authenticated_user

    List repository notifications for the authenticated user
    """
    params = [('all', False),
                    ('participating', False),
                    ('since', '2013-10-20T19:20:30+01:00'),
                    ('before', '2013-10-20T19:20:30+01:00'),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/notifications'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_list_repos_starred_by_authenticated_user(client):
    """Test case for activity_list_repos_starred_by_authenticated_user

    List repositories starred by the authenticated user
    """
    params = [('sort', created),
                    ('direction', desc),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/user/starred',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_list_repos_starred_by_user(client):
    """Test case for activity_list_repos_starred_by_user

    List repositories starred by a user
    """
    params = [('sort', created),
                    ('direction', desc),
                    ('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/users/{username}/starred'.format(username='username_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_list_repos_watched_by_user(client):
    """Test case for activity_list_repos_watched_by_user

    List repositories watched by a user
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/users/{username}/subscriptions'.format(username='username_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_list_stargazers_for_repo(client):
    """Test case for activity_list_stargazers_for_repo

    List stargazers
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/stargazers'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_list_watched_repos_for_authenticated_user(client):
    """Test case for activity_list_watched_repos_for_authenticated_user

    List repositories watched by the authenticated user
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/user/subscriptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_list_watchers_for_repo(client):
    """Test case for activity_list_watchers_for_repo

    List watchers
    """
    params = [('per_page', 30),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/repos/{owner}/{repo}/subscribers'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_mark_notifications_as_read(client):
    """Test case for activity_mark_notifications_as_read

    Mark notifications as read
    """
    body = {"last_read_at":"2022-06-10T00:00:00Z","read":true}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/notifications',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_mark_repo_notifications_as_read(client):
    """Test case for activity_mark_repo_notifications_as_read

    Mark repository notifications as read
    """
    body = openapi_server.ActivityMarkRepoNotificationsAsReadRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/repos/{owner}/{repo}/notifications'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_mark_thread_as_read(client):
    """Test case for activity_mark_thread_as_read

    Mark a thread as read
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/notifications/threads/{thread_id}'.format(thread_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_set_repo_subscription(client):
    """Test case for activity_set_repo_subscription

    Set a repository subscription
    """
    body = openapi_server.ActivitySetRepoSubscriptionRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/repos/{owner}/{repo}/subscription'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_set_thread_subscription(client):
    """Test case for activity_set_thread_subscription

    Set a thread subscription
    """
    body = {"ignored":false}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/notifications/threads/{thread_id}/subscription'.format(thread_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_star_repo_for_authenticated_user(client):
    """Test case for activity_star_repo_for_authenticated_user

    Star a repository for the authenticated user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/user/starred/{owner}/{repo}'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_activity_unstar_repo_for_authenticated_user(client):
    """Test case for activity_unstar_repo_for_authenticated_user

    Unstar a repository for the authenticated user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/user/starred/{owner}/{repo}'.format(owner='owner_example', repo='repo_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

