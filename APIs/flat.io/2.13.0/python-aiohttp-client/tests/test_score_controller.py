# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.assignment_submission import AssignmentSubmission
from openapi_server.models.flat_error_response import FlatErrorResponse
from openapi_server.models.resource_collaborator import ResourceCollaborator
from openapi_server.models.resource_collaborator_creation import ResourceCollaboratorCreation
from openapi_server.models.score_comment import ScoreComment
from openapi_server.models.score_comment_creation import ScoreCommentCreation
from openapi_server.models.score_comment_update import ScoreCommentUpdate
from openapi_server.models.score_creation import ScoreCreation
from openapi_server.models.score_details import ScoreDetails
from openapi_server.models.score_fork import ScoreFork
from openapi_server.models.score_modification import ScoreModification
from openapi_server.models.score_revision import ScoreRevision
from openapi_server.models.score_revision_creation import ScoreRevisionCreation
from openapi_server.models.score_track import ScoreTrack
from openapi_server.models.score_track_creation import ScoreTrackCreation
from openapi_server.models.score_track_update import ScoreTrackUpdate


pytestmark = pytest.mark.asyncio

async def test_add_score_collaborator(client):
    """Test case for add_score_collaborator

    Add a new collaborator
    """
    body = {"aclAdmin":False,"aclRead":True,"aclWrite":True,"userEmail":"jdoe@flat.io"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/scores/{score}/collaborators'.format(score='score_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_score_track(client):
    """Test case for add_score_track

    Add a new video or audio track to the score
    """
    body = {"default":True,"state":"draft","synchronizationPoints":[{"measureUuid":"5132a788-69e6-d0c6-84ec-4bd858658d7c","time":0,"type":"measure"},{"time":213,"type":"end"}],"title":"Rick Astley - Never Gonna Give You Up","url":"https://www.youtube.com/watch?v=dQw4w9WgXcQ"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/scores/{score}/tracks'.format(score='score_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_score(client):
    """Test case for create_score

    Create a new score
    """
    body = {"data":"<score-partwise version=\"3.0\"></score-partwise>","googleDriveFolder":"0B-0000000000000000","privacy":"private","title":"My new score"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/scores',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_score_revision(client):
    """Test case for create_score_revision

    Create a new revision
    """
    body = {"autosave":True,"data":"<score-partwise version=\"3.0\"></score-partwise>","description":"New revision","history":[{"args":{"measureUuid":"0be9f739-3213-f312-bb0a-00ad0c787ef7","previousUuid":"888cb742-2110-a050-ba71-28300ba6d61f"},"fnc":"action.AddMeasure","id":"b278ad43-2e99-4e60-a782-ac119b294ab8","userId":"000000000000000000000010"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/scores/{score}/revisions'.format(score='score_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_score(client):
    """Test case for delete_score

    Delete a score
    """
    params = [('now', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/scores/{score}'.format(score='score_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_score_comment(client):
    """Test case for delete_score_comment

    Delete a comment
    """
    params = [('sharingKey', 'sharing_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/scores/{score}/comments/{comment}'.format(score='score_example', comment='comment_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_score_track(client):
    """Test case for delete_score_track

    Remove an audio or video track linked to the score
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/scores/{score}/tracks/{track}'.format(score='score_example', track='track_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_edit_score(client):
    """Test case for edit_score

    Edit a score's metadata
    """
    body = {"privacy":"private"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/scores/{score}'.format(score='score_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fork_score(client):
    """Test case for fork_score

    Fork a score
    """
    body = {"collection":"root"}
    params = [('sharingKey', 'sharing_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/scores/{score}/fork'.format(score='score_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_ger_user_likes_0(client):
    """Test case for ger_user_likes_0

    List liked scores
    """
    params = [('ids', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/users/{user}/likes'.format(user='user_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_group_scores_0(client):
    """Test case for get_group_scores_0

    List group's scores
    """
    params = [('parent', 'parent_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/groups/{group}/scores'.format(group='group_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_score(client):
    """Test case for get_score

    Get a score's metadata
    """
    params = [('sharingKey', 'sharing_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/scores/{score}'.format(score='score_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_score_collaborator(client):
    """Test case for get_score_collaborator

    Get a collaborator
    """
    params = [('sharingKey', 'sharing_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/scores/{score}/collaborators/{collaborator}'.format(score='score_example', collaborator='collaborator_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_score_collaborators(client):
    """Test case for get_score_collaborators

    List the collaborators
    """
    params = [('sharingKey', 'sharing_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/scores/{score}/collaborators'.format(score='score_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_score_comments(client):
    """Test case for get_score_comments

    List comments
    """
    params = [('sharingKey', 'sharing_key_example'),
                    ('type', 'type_example'),
                    ('sort', 'sort_example'),
                    ('direction', 'direction_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/scores/{score}/comments'.format(score='score_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_score_revision(client):
    """Test case for get_score_revision

    Get a score revision
    """
    params = [('sharingKey', 'sharing_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/scores/{score}/revisions/{revision}'.format(score='score_example', revision='revision_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_score_revision_data(client):
    """Test case for get_score_revision_data

    Get a score revision data
    """
    params = [('sharingKey', 'sharing_key_example'),
                    ('parts', 'parts_example'),
                    ('onlyCached', True),
                    ('url', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/scores/{score}/revisions/{revision}/{format}'.format(score='score_example', revision='revision_example', format='format_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_score_revisions(client):
    """Test case for get_score_revisions

    List the revisions
    """
    params = [('sharingKey', 'sharing_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/scores/{score}/revisions'.format(score='score_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_score_submissions(client):
    """Test case for get_score_submissions

    List submissions related to the score
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/scores/{score}/submissions'.format(score='score_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_score_track(client):
    """Test case for get_score_track

    Retrieve the details of an audio or video track linked to a score
    """
    params = [('sharingKey', 'sharing_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/scores/{score}/tracks/{track}'.format(score='score_example', track='track_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_scores_0(client):
    """Test case for get_user_scores_0

    List user's scores
    """
    params = [('parent', 'parent_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/users/{user}/scores'.format(user='user_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_score_tracks(client):
    """Test case for list_score_tracks

    List the audio or video tracks linked to a score
    """
    params = [('sharingKey', 'sharing_key_example'),
                    ('assignment', 'assignment_example'),
                    ('listAutoTrack', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/scores/{score}/tracks'.format(score='score_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mark_score_comment_resolved(client):
    """Test case for mark_score_comment_resolved

    Mark the comment as resolved
    """
    params = [('sharingKey', 'sharing_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/scores/{score}/comments/{comment}/resolved'.format(score='score_example', comment='comment_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_mark_score_comment_unresolved(client):
    """Test case for mark_score_comment_unresolved

    Mark the comment as unresolved
    """
    params = [('sharingKey', 'sharing_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/scores/{score}/comments/{comment}/resolved'.format(score='score_example', comment='comment_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_score_comment(client):
    """Test case for post_score_comment

    Post a new comment
    """
    body = {"comment":"@[000000000000000000000000:flat] Great work!","context":{"measureUuids":["e6a6a60b-8710-f819-9a49-e907b19c6f1f","da83d93c-e3a6-3c73-1bbe-15e5131d6437","056ec5eb-9213-df56-6ae8-d9b99673dc48"],"partUuid":"91982db7-2e6d-285e-7a19-76b4bd005b8b","staffUuid":"9395d8f3-f42b-47b6-8c5d-6ba704961ec0","startDpq":1,"startTimePos":2,"stopDpq":1,"stopTimePos":3},"mentions":["000000000000000000000000"],"rawComment":"@flat: Great work!","replyTo":"000000000000000000000000","revision":"000000000000000000000010"}
    params = [('sharingKey', 'sharing_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/scores/{score}/comments'.format(score='score_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_score_collaborator(client):
    """Test case for remove_score_collaborator

    Delete a collaborator
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/scores/{score}/collaborators/{collaborator}'.format(score='score_example', collaborator='collaborator_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_untrash_score(client):
    """Test case for untrash_score

    Untrash a score
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/scores/{score}/untrash'.format(score='score_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_score_comment(client):
    """Test case for update_score_comment

    Update an existing comment
    """
    body = {"comment":"@[000000000000000000000000:flat] Great work!","context":{"measureUuids":["e6a6a60b-8710-f819-9a49-e907b19c6f1f","da83d93c-e3a6-3c73-1bbe-15e5131d6437","056ec5eb-9213-df56-6ae8-d9b99673dc48"],"partUuid":"91982db7-2e6d-285e-7a19-76b4bd005b8b","staffUuid":"9395d8f3-f42b-47b6-8c5d-6ba704961ec0","startDpq":1,"startTimePos":2,"stopDpq":1,"stopTimePos":3},"mentions":["000000000000000000000000"],"rawComment":"@flat: Great work!","replyTo":"000000000000000000000000","revision":"000000000000000000000011"}
    params = [('sharingKey', 'sharing_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/scores/{score}/comments/{comment}'.format(score='score_example', comment='comment_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_score_track(client):
    """Test case for update_score_track

    Update an audio or video track linked to a score
    """
    body = {"default":True,"state":"draft","synchronizationPoints":[{"measureUuid":"5132a788-69e6-d0c6-84ec-4bd858658d7c","time":0,"type":"measure"},{"time":213,"type":"end"}],"title":"Rick Astley - Never Gonna Give You Up","url":"https://www.youtube.com/watch?v=dQw4w9WgXcQ"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/scores/{score}/tracks/{track}'.format(score='score_example', track='track_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

