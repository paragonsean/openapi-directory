# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.assignment import Assignment
from openapi_server.models.assignment_copy import AssignmentCopy
from openapi_server.models.assignment_creation import AssignmentCreation
from openapi_server.models.assignment_submission import AssignmentSubmission
from openapi_server.models.assignment_submission_comment import AssignmentSubmissionComment
from openapi_server.models.assignment_submission_comment_creation import AssignmentSubmissionCommentCreation
from openapi_server.models.assignment_submission_history import AssignmentSubmissionHistory
from openapi_server.models.assignment_submission_update import AssignmentSubmissionUpdate
from openapi_server.models.class_creation import ClassCreation
from openapi_server.models.class_details import ClassDetails
from openapi_server.models.class_update import ClassUpdate
from openapi_server.models.flat_error_response import FlatErrorResponse
from openapi_server.models.score_details import ScoreDetails
from openapi_server.models.score_fork import ScoreFork


pytestmark = pytest.mark.asyncio

async def test_activate_class(client):
    """Test case for activate_class

    Activate the class
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/classes/{_class}/activate'.format(_class='_class_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_class_user(client):
    """Test case for add_class_user

    Add a user to the class
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/classes/{_class}/users/{user}'.format(_class='_class_example', user='user_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_archive_assignment(client):
    """Test case for archive_assignment

    Archive the assignment
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/classes/{_class}/assignments/{assignment}/archive'.format(_class='_class_example', assignment='assignment_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_archive_class(client):
    """Test case for archive_class

    Archive the class
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/classes/{_class}/archive'.format(_class='_class_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_copy_assignment(client):
    """Test case for copy_assignment

    Copy an assignment
    """
    body = {"classroom":"0000000000000000"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/classes/{_class}/assignments/{assignment}/copy'.format(_class='_class_example', assignment='assignment_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_assignment(client):
    """Test case for create_assignment

    Assignment creation
    """
    body = {"attachments":[{"score":"0000000000000000","type":"flat"},{"type":"link","url":"https://flat.io/developers"}],"description":"Get started with Flat","dueDate":"2017-07-12T13:56:19.613000Z","maxPoints":100,"scheduledDate":"2017-06-20T13:56:19.613000Z","title":"First assignment"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/classes/{_class}/assignments'.format(_class='_class_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_class(client):
    """Test case for create_class

    Create a new class
    """
    body = {"name":"Music Theory Course","section":"Music Theory 101"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/classes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_submission(client):
    """Test case for create_submission

    Create or edit a submission
    """
    body = {"attachments":[{"score":"58c4955a226ffff257211a8d","title":"Hello - Student","type":"flat"}],"submit":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/classes/{_class}/assignments/{assignment}/submissions'.format(_class='_class_example', assignment='assignment_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_class_user(client):
    """Test case for delete_class_user

    Remove a user from the class
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/classes/{_class}/users/{user}'.format(_class='_class_example', user='user_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_submission(client):
    """Test case for delete_submission

    Delete a submission
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/classes/{_class}/assignments/{assignment}/submissions/{submission}'.format(_class='_class_example', assignment='assignment_example', submission='submission_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_submission_comment(client):
    """Test case for delete_submission_comment

    Delete a feedback comment to a submission
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/classes/{_class}/assignments/{assignment}/submissions/{submission}/comments/{comment}'.format(_class='_class_example', assignment='assignment_example', submission='submission_example', comment='comment_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_edit_submission(client):
    """Test case for edit_submission

    Edit a submission
    """
    body = {"attachments":[{"score":"58c4955a226ffff257211a8d","title":"Hello - Student","type":"flat"}],"submit":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/classes/{_class}/assignments/{assignment}/submissions/{submission}'.format(_class='_class_example', assignment='assignment_example', submission='submission_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enroll_class(client):
    """Test case for enroll_class

    Join a class
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/classes/enroll/{enrollment_code}'.format(enrollment_code='enrollment_code_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_submissions_reviews_as_csv(client):
    """Test case for export_submissions_reviews_as_csv

    CSV Grades exports
    """
    headers = { 
        'Accept': 'text/csv',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/classes/{_class}/assignments/{assignment}/submissions/csv'.format(_class='_class_example', assignment='assignment_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_submissions_reviews_as_excel(client):
    """Test case for export_submissions_reviews_as_excel

    Excel Grades exports
    """
    headers = { 
        'Accept': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/classes/{_class}/assignments/{assignment}/submissions/excel'.format(_class='_class_example', assignment='assignment_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fork_score_0(client):
    """Test case for fork_score_0

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

async def test_get_class(client):
    """Test case for get_class

    Get the details of a single class
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/classes/{_class}'.format(_class='_class_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_score_submissions_0(client):
    """Test case for get_score_submissions_0

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

async def test_get_submission(client):
    """Test case for get_submission

    Get a student submission
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/classes/{_class}/assignments/{assignment}/submissions/{submission}'.format(_class='_class_example', assignment='assignment_example', submission='submission_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_submission_comments(client):
    """Test case for get_submission_comments

    List the feedback comments of a submission
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/classes/{_class}/assignments/{assignment}/submissions/{submission}/comments'.format(_class='_class_example', assignment='assignment_example', submission='submission_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_submission_history(client):
    """Test case for get_submission_history

    Get the history of the submission
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/classes/{_class}/assignments/{assignment}/submissions/{submission}/history'.format(_class='_class_example', assignment='assignment_example', submission='submission_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_submissions(client):
    """Test case for get_submissions

    List the students' submissions
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/classes/{_class}/assignments/{assignment}/submissions'.format(_class='_class_example', assignment='assignment_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_assignments(client):
    """Test case for list_assignments

    Assignments listing
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/classes/{_class}/assignments'.format(_class='_class_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_class_student_submissions(client):
    """Test case for list_class_student_submissions

    List the submissions for a student
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/classes/{_class}/students/{user}/submissions'.format(_class='_class_example', user='user_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_classes(client):
    """Test case for list_classes

    List the classes available for the current user
    """
    params = [('state', active)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/classes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_submission_comment(client):
    """Test case for post_submission_comment

    Add a feedback comment to a submission
    """
    body = {"comment":"comment"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/classes/{_class}/assignments/{assignment}/submissions/{submission}/comments'.format(_class='_class_example', assignment='assignment_example', submission='submission_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unarchive_assignment(client):
    """Test case for unarchive_assignment

    Unarchive the assignment.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/classes/{_class}/assignments/{assignment}/archive'.format(_class='_class_example', assignment='assignment_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unarchive_class(client):
    """Test case for unarchive_class

    Unarchive the class
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/classes/{_class}/archive'.format(_class='_class_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_class(client):
    """Test case for update_class

    Update the class
    """
    body = {"name":"Music Theory Course","section":"Music Theory 101"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/classes/{_class}'.format(_class='_class_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_submission_comment(client):
    """Test case for update_submission_comment

    Update a feedback comment to a submission
    """
    body = {"comment":"comment"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/classes/{_class}/assignments/{assignment}/submissions/{submission}/comments/{comment}'.format(_class='_class_example', assignment='assignment_example', submission='submission_example', comment='comment_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

