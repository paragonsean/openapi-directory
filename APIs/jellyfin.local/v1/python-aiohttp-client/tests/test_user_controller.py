# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.authenticate_user_by_name import AuthenticateUserByName
from openapi_server.models.authentication_result import AuthenticationResult
from openapi_server.models.create_user_by_name import CreateUserByName
from openapi_server.models.forgot_password_dto import ForgotPasswordDto
from openapi_server.models.forgot_password_result import ForgotPasswordResult
from openapi_server.models.pin_redeem_result import PinRedeemResult
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.quick_connect_dto import QuickConnectDto
from openapi_server.models.update_user_easy_password import UpdateUserEasyPassword
from openapi_server.models.update_user_password import UpdateUserPassword
from openapi_server.models.user_configuration import UserConfiguration
from openapi_server.models.user_dto import UserDto
from openapi_server.models.user_policy import UserPolicy


pytestmark = pytest.mark.asyncio

async def test_authenticate_user(client):
    """Test case for authenticate_user

    Authenticates a user.
    """
    params = [('pw', 'pw_example'),
                    ('password', 'password_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/Users/{user_id}/Authenticate'.format(user_id='user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_authenticate_user_by_name(client):
    """Test case for authenticate_user_by_name

    Authenticates a user by name.
    """
    body = {"Username":"Username","Pw":"Pw","Password":"Password"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
    }
    response = await client.request(
        method='POST',
        path='/Users/AuthenticateByName',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_authenticate_with_quick_connect(client):
    """Test case for authenticate_with_quick_connect

    Authenticates a user with quick connect.
    """
    body = {"Token":"Token"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
    }
    response = await client.request(
        method='POST',
        path='/Users/AuthenticateWithQuickConnect',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_user_by_name(client):
    """Test case for create_user_by_name

    Creates a user.
    """
    body = {"Name":"Name","Password":"Password"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Users/New',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_user(client):
    """Test case for delete_user

    Deletes a user.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/Users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_forgot_password(client):
    """Test case for forgot_password

    Initiates the forgot password process for a local user.
    """
    body = {"EnteredUsername":"EnteredUsername"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
    }
    response = await client.request(
        method='POST',
        path='/Users/ForgotPassword',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_forgot_password_pin(client):
    """Test case for forgot_password_pin

    Redeems a forgot password pin.
    """
    body = 'body_example'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
    }
    response = await client.request(
        method='POST',
        path='/Users/ForgotPassword/Pin',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_current_user(client):
    """Test case for get_current_user

    Gets the user based on auth token.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Users/Me',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_public_users(client):
    """Test case for get_public_users

    Gets a list of publicly visible users for display on a login screen.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Users/Public',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_by_id(client):
    """Test case for get_user_by_id

    Gets a user by Id.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users(client):
    """Test case for get_users

    Gets a list of users.
    """
    params = [('isHidden', True),
                    ('isDisabled', True)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_user(client):
    """Test case for update_user

    Updates a user.
    """
    body = {"Policy":{"EnableContentDeletion":True,"EnableContentDeletionFromFolders":["EnableContentDeletionFromFolders","EnableContentDeletionFromFolders"],"BlockedMediaFolders":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"EnablePlaybackRemuxing":True,"EnabledFolders":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"LoginAttemptsBeforeLockout":5,"IsDisabled":True,"MaxParentalRating":7,"EnablePublicSharing":True,"AccessSchedules":[{"DayOfWeek":"Sunday","StartHour":1.4658129805029452,"UserId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","EndHour":0.8008281904610115,"Id":6},{"DayOfWeek":"Sunday","StartHour":1.4658129805029452,"UserId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","EndHour":0.8008281904610115,"Id":6}],"EnableContentDownloading":True,"ForceRemoteSourceTranscoding":True,"SyncPlayAccess":"CreateAndJoinGroups","IsAdministrator":True,"BlockedChannels":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"EnableAllDevices":True,"EnabledChannels":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"MaxActiveSessions":2,"EnableMediaConversion":True,"InvalidLoginAttemptCount":5,"EnableLiveTvAccess":True,"EnableAllFolders":True,"EnableRemoteAccess":True,"EnableSharedDeviceControl":True,"IsHidden":True,"EnableLiveTvManagement":True,"BlockUnratedItems":["Movie","Movie"],"EnableMediaPlayback":True,"EnableVideoPlaybackTranscoding":True,"EnableAllChannels":True,"AuthenticationProviderId":"AuthenticationProviderId","EnableUserPreferenceAccess":True,"BlockedTags":["BlockedTags","BlockedTags"],"EnabledDevices":["EnabledDevices","EnabledDevices"],"EnableRemoteControlOfOtherUsers":True,"PasswordResetProviderId":"PasswordResetProviderId","EnableAudioPlaybackTranscoding":True,"EnableSyncTranscoding":True,"RemoteClientBitrateLimit":9},"HasConfiguredEasyPassword":True,"EnableAutoLogin":True,"Configuration":{"EnableNextEpisodeAutoPlay":True,"SubtitleLanguagePreference":"SubtitleLanguagePreference","DisplayMissingEpisodes":True,"OrderedViews":["OrderedViews","OrderedViews"],"LatestItemsExcludes":["LatestItemsExcludes","LatestItemsExcludes"],"SubtitleMode":"Default","HidePlayedInLatest":True,"EnableLocalPassword":True,"RememberSubtitleSelections":True,"AudioLanguagePreference":"AudioLanguagePreference","DisplayCollectionsView":True,"GroupedFolders":["GroupedFolders","GroupedFolders"],"PlayDefaultAudioTrack":True,"MyMediaExcludes":["MyMediaExcludes","MyMediaExcludes"],"RememberAudioSelections":True},"LastLoginDate":"2000-01-23T04:56:07.000+00:00","PrimaryImageTag":"PrimaryImageTag","Name":"Name","HasConfiguredPassword":True,"ServerId":"ServerId","ServerName":"ServerName","LastActivityDate":"2000-01-23T04:56:07.000+00:00","PrimaryImageAspectRatio":3.616076749251911,"Id":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","HasPassword":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_user_configuration(client):
    """Test case for update_user_configuration

    Updates a user configuration.
    """
    body = {"EnableNextEpisodeAutoPlay":True,"SubtitleLanguagePreference":"SubtitleLanguagePreference","DisplayMissingEpisodes":True,"OrderedViews":["OrderedViews","OrderedViews"],"LatestItemsExcludes":["LatestItemsExcludes","LatestItemsExcludes"],"SubtitleMode":"Default","HidePlayedInLatest":True,"EnableLocalPassword":True,"RememberSubtitleSelections":True,"AudioLanguagePreference":"AudioLanguagePreference","DisplayCollectionsView":True,"GroupedFolders":["GroupedFolders","GroupedFolders"],"PlayDefaultAudioTrack":True,"MyMediaExcludes":["MyMediaExcludes","MyMediaExcludes"],"RememberAudioSelections":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Users/{user_id}/Configuration'.format(user_id='user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_user_easy_password(client):
    """Test case for update_user_easy_password

    Updates a user's easy password.
    """
    body = {"NewPassword":"NewPassword","ResetPassword":True,"NewPw":"NewPw"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Users/{user_id}/EasyPassword'.format(user_id='user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_user_password(client):
    """Test case for update_user_password

    Updates a user's password.
    """
    body = {"ResetPassword":True,"CurrentPw":"CurrentPw","CurrentPassword":"CurrentPassword","NewPw":"NewPw"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Users/{user_id}/Password'.format(user_id='user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_user_policy(client):
    """Test case for update_user_policy

    Updates a user policy.
    """
    body = {"EnableContentDeletion":True,"EnableContentDeletionFromFolders":["EnableContentDeletionFromFolders","EnableContentDeletionFromFolders"],"BlockedMediaFolders":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"EnablePlaybackRemuxing":True,"EnabledFolders":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"LoginAttemptsBeforeLockout":5,"IsDisabled":True,"MaxParentalRating":7,"EnablePublicSharing":True,"AccessSchedules":[{"DayOfWeek":"Sunday","StartHour":1.4658129805029452,"UserId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","EndHour":0.8008281904610115,"Id":6},{"DayOfWeek":"Sunday","StartHour":1.4658129805029452,"UserId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","EndHour":0.8008281904610115,"Id":6}],"EnableContentDownloading":True,"ForceRemoteSourceTranscoding":True,"SyncPlayAccess":"CreateAndJoinGroups","IsAdministrator":True,"BlockedChannels":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"EnableAllDevices":True,"EnabledChannels":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"MaxActiveSessions":2,"EnableMediaConversion":True,"InvalidLoginAttemptCount":5,"EnableLiveTvAccess":True,"EnableAllFolders":True,"EnableRemoteAccess":True,"EnableSharedDeviceControl":True,"IsHidden":True,"EnableLiveTvManagement":True,"BlockUnratedItems":["Movie","Movie"],"EnableMediaPlayback":True,"EnableVideoPlaybackTranscoding":True,"EnableAllChannels":True,"AuthenticationProviderId":"AuthenticationProviderId","EnableUserPreferenceAccess":True,"BlockedTags":["BlockedTags","BlockedTags"],"EnabledDevices":["EnabledDevices","EnabledDevices"],"EnableRemoteControlOfOtherUsers":True,"PasswordResetProviderId":"PasswordResetProviderId","EnableAudioPlaybackTranscoding":True,"EnableSyncTranscoding":True,"RemoteClientBitrateLimit":9}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Users/{user_id}/Policy'.format(user_id='user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

