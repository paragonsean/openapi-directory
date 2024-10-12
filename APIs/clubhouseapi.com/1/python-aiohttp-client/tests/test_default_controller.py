# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_call_phone_number_auth_post(client):
    """Test case for call_phone_number_auth_post

    Call phone number auth.
    """
    body = {}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/call_phone_number_auth',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_check_for_update_get(client):
    """Test case for check_for_update_get

    Clubhouse uses this to check for updates when app is not installed from App Store (eg TestFlight)
    """
    params = [('is_testflight', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/check_for_update',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_check_waitlist_status_post(client):
    """Test case for check_waitlist_status_post

    checks waitlist status.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/check_waitlist_status',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_complete_phone_number_auth_post(client):
    """Test case for complete_phone_number_auth_post

    Call phone number auth.
    """
    body = {"phone_number":"+1234567890","verification_code":"1234"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/complete_phone_number_auth',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_channel_post(client):
    """Test case for create_channel_post

    creates a channel
    """
    body = {"club_id":null,"event_id":null,"is_private":false,"is_social_mode":false,"topic":null,"user_ids":[]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/create_channel',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_follow_post(client):
    """Test case for follow_post

    follows a user
    """
    body = {"user_id":1234}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/follow',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_actionable_notifications_get(client):
    """Test case for get_actionable_notifications_get

    get actionable notifications (the bell again)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/get_actionable_notifications',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_topics_get(client):
    """Test case for get_all_topics_get

    gets all topics.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/get_all_topics',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_channels_get(client):
    """Test case for get_channels_get

    get all channels
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/get_channels',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_club_post(client):
    """Test case for get_club_post

    gets club by id
    """
    body = {"club_id":1234}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/get_club',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_clubs_for_topic_post(client):
    """Test case for get_clubs_for_topic_post

    looks up clubs by topic.
    """
    body = {"topic_id":140}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/get_clubs_for_topic',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_create_channel_targets_post(client):
    """Test case for get_create_channel_targets_post

    is fetched when you tap Create Room
    """
    body = {}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/get_create_channel_targets',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_events_get(client):
    """Test case for get_events_get

    the Upcoming for You page
    """
    params = [('is_filtered', true),
                    ('page_size', 25),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/get_events',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_following_post(client):
    """Test case for get_following_post

    get a list of the users and clubs that this user is following. Returned users have bios truncated to ~80 characters.
    """
    body = {"user_id":1234}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/get_following',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_notifications_get(client):
    """Test case for get_notifications_get

    get notifications (the bell icon)
    """
    params = [('page_size', 20),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/get_notifications',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_online_friends_post(client):
    """Test case for get_online_friends_post

    gets online friends on the app homepage.
    """
    body = {}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/get_online_friends',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_profile_post(client):
    """Test case for get_profile_post

    looks up user profile by ID.
    """
    body = {"user_id":4075733}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/get_profile',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_release_notes_post(client):
    """Test case for get_release_notes_post

    gets release notes.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/get_release_notes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_settings_get(client):
    """Test case for get_settings_get

    get notification settings
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/get_settings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_suggested_club_invites_post(client):
    """Test case for get_suggested_club_invites_post

    find users to invite to clubs based on phone number
    """
    body = {"contacts":[{"name":"aaa","phone_number":"+11234567890"}],"upload_contacts":true}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/get_suggested_club_invites',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_suggested_follows_all_get(client):
    """Test case for get_suggested_follows_all_get

    gets suggested follows during signup
    """
    params = [('in_onboarding', true),
                    ('page_size', 50),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/get_suggested_follows_all',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_suggested_follows_friends_only_post(client):
    """Test case for get_suggested_follows_friends_only_post

    find people to follow by uploading contacts during signup
    """
    body = {"club_id":null,"contacts":[],"upload_contacts":true}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/get_suggested_follows_friends_only',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_suggested_follows_similar_post(client):
    """Test case for get_suggested_follows_similar_post

    find similar users. (The Sparkles button on Clubhouse's profile page)
    """
    body = {"user_id":4}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/get_suggested_follows_similar',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_suggested_invites_post(client):
    """Test case for get_suggested_invites_post

    find users to invite based on phone number.
    """
    body = {"club_id":null,"contacts":[{"phone_number":"+11234567890"}],"upload_contacts":false}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/get_suggested_invites',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_suggested_speakers_post(client):
    """Test case for get_suggested_speakers_post

    gets suggested users when you start a private room
    """
    body = {"channel":null}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/get_suggested_speakers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_topic_post(client):
    """Test case for get_topic_post

    looks up topic by ID.
    """
    body = {"topic_id":140}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/get_topic',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users_for_topic_get(client):
    """Test case for get_users_for_topic_get

    looks up users by topic.
    """
    params = [('topic_id', 140),
                    ('page_size', 25),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/get_users_for_topic',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_welcome_channel_get(client):
    """Test case for get_welcome_channel_get

    called during signup
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/get_welcome_channel',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invite_from_waitlist_post(client):
    """Test case for invite_from_waitlist_post

    wave to another user on the waitlist to give them access
    """
    body = {"user_id":1234}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/invite_from_waitlist',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invite_to_app_post(client):
    """Test case for invite_to_app_post

    invite a user to the app, using one of your invites
    """
    body = {"message":null,"name":"John Smith","phone_number":"+11234567890"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/invite_to_app',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_join_channel_post(client):
    """Test case for join_channel_post

    join a channel.
    """
    body = {"attribution_details":"eyJpc19leHBsb3JlIjpmYWxzZSwicmFuayI6MX0=","attribution_source":"feed","channel":"abcdefgh"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/join_channel',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_leave_channel_post(client):
    """Test case for leave_channel_post

    leave a channel.
    """
    body = {"channel":"abcdefgh"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/leave_channel',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_me_post(client):
    """Test case for me_post

    gets user
    """
    body = {"return_blocked_ids":true,"return_following_ids":true,"timezone_identifier":"America/Los_Angeles"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/me',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_record_action_trails_post(client):
    """Test case for record_action_trails_post

    analytics
    """
    body = {"action_trails":[{"blob_data":{},"client_time_created":1612971962,"trail_type":"app_opened"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/record_action_trails',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_refresh_token_post(client):
    """Test case for refresh_token_post

    gets an access_token from a refresh_token.
    """
    body = {"refresh":"<refresh_token>"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/refresh_token',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resend_phone_number_auth_post(client):
    """Test case for resend_phone_number_auth_post

    Resend phone number auth.
    """
    body = {}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/resend_phone_number_auth',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_clubs_post(client):
    """Test case for search_clubs_post

    search clubs.
    """
    body = {"cofollows_only":false,"followers_only":false,"following_only":false,"query":"rohan"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/search_clubs',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_users_post(client):
    """Test case for search_users_post

    search for users
    """
    body = {"cofollows_only":false,"followers_only":false,"following_only":false,"query":"johnsmith"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/search_users',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_phone_number_auth_post(client):
    """Test case for start_phone_number_auth_post

    Starts phone number auth.
    """
    body = {"phone_number":"+11234567890"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/start_phone_number_auth',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_notifications_post(client):
    """Test case for update_notifications_post

    updates notification during signup.
    """
    body = {"apn_token":null,"enable_trending":-1,"frequency":-1,"is_sandbox":false,"pause_till":-1,"system_enabled":2}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/update_notifications',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_username_post(client):
    """Test case for update_username_post

    edits username.
    """
    body = {"username":"hipsterhouse"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/update_username',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

