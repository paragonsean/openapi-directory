# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.announcement import Announcement
from openapi_server.models.course import Course
from openapi_server.models.course_alias import CourseAlias
from openapi_server.models.course_work import CourseWork
from openapi_server.models.course_work_material import CourseWorkMaterial
from openapi_server.models.list_announcements_response import ListAnnouncementsResponse
from openapi_server.models.list_course_aliases_response import ListCourseAliasesResponse
from openapi_server.models.list_course_work_material_response import ListCourseWorkMaterialResponse
from openapi_server.models.list_course_work_response import ListCourseWorkResponse
from openapi_server.models.list_courses_response import ListCoursesResponse
from openapi_server.models.list_student_submissions_response import ListStudentSubmissionsResponse
from openapi_server.models.list_students_response import ListStudentsResponse
from openapi_server.models.list_teachers_response import ListTeachersResponse
from openapi_server.models.list_topic_response import ListTopicResponse
from openapi_server.models.modify_announcement_assignees_request import ModifyAnnouncementAssigneesRequest
from openapi_server.models.modify_attachments_request import ModifyAttachmentsRequest
from openapi_server.models.modify_course_work_assignees_request import ModifyCourseWorkAssigneesRequest
from openapi_server.models.student import Student
from openapi_server.models.student_submission import StudentSubmission
from openapi_server.models.teacher import Teacher
from openapi_server.models.topic import Topic


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_aliases_create(client):
    """Test case for classroom_courses_aliases_create

    
    """
    body = {"alias":"alias"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/courses/{course_id}/aliases'.format(course_id='course_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_aliases_delete(client):
    """Test case for classroom_courses_aliases_delete

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/courses/{course_id}/aliases/{alias}'.format(course_id='course_id_example', alias='alias_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_aliases_list(client):
    """Test case for classroom_courses_aliases_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/courses/{course_id}/aliases'.format(course_id='course_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_announcements_create(client):
    """Test case for classroom_courses_announcements_create

    
    """
    body = {"creatorUserId":"creatorUserId","scheduledTime":"scheduledTime","creationTime":"creationTime","materials":[{"form":{"responseUrl":"responseUrl","formUrl":"formUrl","title":"title","thumbnailUrl":"thumbnailUrl"},"link":{"title":"title","url":"url","thumbnailUrl":"thumbnailUrl"},"driveFile":{"shareMode":"UNKNOWN_SHARE_MODE","driveFile":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}},"youtubeVideo":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}},{"form":{"responseUrl":"responseUrl","formUrl":"formUrl","title":"title","thumbnailUrl":"thumbnailUrl"},"link":{"title":"title","url":"url","thumbnailUrl":"thumbnailUrl"},"driveFile":{"shareMode":"UNKNOWN_SHARE_MODE","driveFile":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}},"youtubeVideo":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}}],"alternateLink":"alternateLink","updateTime":"updateTime","id":"id","state":"ANNOUNCEMENT_STATE_UNSPECIFIED","text":"text","assigneeMode":"ASSIGNEE_MODE_UNSPECIFIED","courseId":"courseId","individualStudentsOptions":{"studentIds":["studentIds","studentIds"]}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/courses/{course_id}/announcements'.format(course_id='course_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_announcements_delete(client):
    """Test case for classroom_courses_announcements_delete

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/courses/{course_id}/announcements/{id}'.format(course_id='course_id_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_announcements_get(client):
    """Test case for classroom_courses_announcements_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/courses/{course_id}/announcements/{id}'.format(course_id='course_id_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_announcements_list(client):
    """Test case for classroom_courses_announcements_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('announcementStates', ['announcement_states_example']),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/courses/{course_id}/announcements'.format(course_id='course_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_announcements_modify_assignees(client):
    """Test case for classroom_courses_announcements_modify_assignees

    
    """
    body = {"modifyIndividualStudentsOptions":{"removeStudentIds":["removeStudentIds","removeStudentIds"],"addStudentIds":["addStudentIds","addStudentIds"]},"assigneeMode":"ASSIGNEE_MODE_UNSPECIFIED"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/courses/{course_id}/announcements/{idmodify_assignee}'.format(course_id='course_id_example', id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_announcements_patch(client):
    """Test case for classroom_courses_announcements_patch

    
    """
    body = {"creatorUserId":"creatorUserId","scheduledTime":"scheduledTime","creationTime":"creationTime","materials":[{"form":{"responseUrl":"responseUrl","formUrl":"formUrl","title":"title","thumbnailUrl":"thumbnailUrl"},"link":{"title":"title","url":"url","thumbnailUrl":"thumbnailUrl"},"driveFile":{"shareMode":"UNKNOWN_SHARE_MODE","driveFile":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}},"youtubeVideo":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}},{"form":{"responseUrl":"responseUrl","formUrl":"formUrl","title":"title","thumbnailUrl":"thumbnailUrl"},"link":{"title":"title","url":"url","thumbnailUrl":"thumbnailUrl"},"driveFile":{"shareMode":"UNKNOWN_SHARE_MODE","driveFile":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}},"youtubeVideo":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}}],"alternateLink":"alternateLink","updateTime":"updateTime","id":"id","state":"ANNOUNCEMENT_STATE_UNSPECIFIED","text":"text","assigneeMode":"ASSIGNEE_MODE_UNSPECIFIED","courseId":"courseId","individualStudentsOptions":{"studentIds":["studentIds","studentIds"]}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/courses/{course_id}/announcements/{id}'.format(course_id='course_id_example', id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_course_work_create(client):
    """Test case for classroom_courses_course_work_create

    
    """
    body = {"creatorUserId":"creatorUserId","scheduledTime":"scheduledTime","creationTime":"creationTime","multipleChoiceQuestion":{"choices":["choices","choices"]},"submissionModificationMode":"SUBMISSION_MODIFICATION_MODE_UNSPECIFIED","assignment":{"studentWorkFolder":{"alternateLink":"alternateLink","id":"id","title":"title"}},"dueDate":{"month":6,"year":1,"day":0},"description":"description","updateTime":"updateTime","dueTime":{"hours":5,"seconds":7,"nanos":2,"minutes":5},"title":"title","topicId":"topicId","materials":[{"form":{"responseUrl":"responseUrl","formUrl":"formUrl","title":"title","thumbnailUrl":"thumbnailUrl"},"link":{"title":"title","url":"url","thumbnailUrl":"thumbnailUrl"},"driveFile":{"shareMode":"UNKNOWN_SHARE_MODE","driveFile":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}},"youtubeVideo":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}},{"form":{"responseUrl":"responseUrl","formUrl":"formUrl","title":"title","thumbnailUrl":"thumbnailUrl"},"link":{"title":"title","url":"url","thumbnailUrl":"thumbnailUrl"},"driveFile":{"shareMode":"UNKNOWN_SHARE_MODE","driveFile":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}},"youtubeVideo":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}}],"maxPoints":9.301444243932576,"workType":"COURSE_WORK_TYPE_UNSPECIFIED","alternateLink":"alternateLink","id":"id","state":"COURSE_WORK_STATE_UNSPECIFIED","assigneeMode":"ASSIGNEE_MODE_UNSPECIFIED","courseId":"courseId","gradeCategory":{"defaultGradeDenominator":0,"name":"name","weight":6,"id":"id"},"associatedWithDeveloper":True,"individualStudentsOptions":{"studentIds":["studentIds","studentIds"]}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/courses/{course_id}/courseWork'.format(course_id='course_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_course_work_delete(client):
    """Test case for classroom_courses_course_work_delete

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/courses/{course_id}/courseWork/{id}'.format(course_id='course_id_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_course_work_get(client):
    """Test case for classroom_courses_course_work_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/courses/{course_id}/courseWork/{id}'.format(course_id='course_id_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_course_work_list(client):
    """Test case for classroom_courses_course_work_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('courseWorkStates', ['course_work_states_example']),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/courses/{course_id}/courseWork'.format(course_id='course_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_course_work_materials_create(client):
    """Test case for classroom_courses_course_work_materials_create

    
    """
    body = {"creatorUserId":"creatorUserId","scheduledTime":"scheduledTime","creationTime":"creationTime","description":"description","updateTime":"updateTime","title":"title","topicId":"topicId","materials":[{"form":{"responseUrl":"responseUrl","formUrl":"formUrl","title":"title","thumbnailUrl":"thumbnailUrl"},"link":{"title":"title","url":"url","thumbnailUrl":"thumbnailUrl"},"driveFile":{"shareMode":"UNKNOWN_SHARE_MODE","driveFile":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}},"youtubeVideo":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}},{"form":{"responseUrl":"responseUrl","formUrl":"formUrl","title":"title","thumbnailUrl":"thumbnailUrl"},"link":{"title":"title","url":"url","thumbnailUrl":"thumbnailUrl"},"driveFile":{"shareMode":"UNKNOWN_SHARE_MODE","driveFile":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}},"youtubeVideo":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}}],"alternateLink":"alternateLink","id":"id","state":"COURSEWORK_MATERIAL_STATE_UNSPECIFIED","assigneeMode":"ASSIGNEE_MODE_UNSPECIFIED","courseId":"courseId","individualStudentsOptions":{"studentIds":["studentIds","studentIds"]}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/courses/{course_id}/courseWorkMaterials'.format(course_id='course_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_course_work_materials_delete(client):
    """Test case for classroom_courses_course_work_materials_delete

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/courses/{course_id}/courseWorkMaterials/{id}'.format(course_id='course_id_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_course_work_materials_get(client):
    """Test case for classroom_courses_course_work_materials_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/courses/{course_id}/courseWorkMaterials/{id}'.format(course_id='course_id_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_course_work_materials_list(client):
    """Test case for classroom_courses_course_work_materials_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('courseWorkMaterialStates', ['course_work_material_states_example']),
                    ('materialDriveId', 'material_drive_id_example'),
                    ('materialLink', 'material_link_example'),
                    ('orderBy', 'order_by_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/courses/{course_id}/courseWorkMaterials'.format(course_id='course_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_course_work_materials_patch(client):
    """Test case for classroom_courses_course_work_materials_patch

    
    """
    body = {"creatorUserId":"creatorUserId","scheduledTime":"scheduledTime","creationTime":"creationTime","description":"description","updateTime":"updateTime","title":"title","topicId":"topicId","materials":[{"form":{"responseUrl":"responseUrl","formUrl":"formUrl","title":"title","thumbnailUrl":"thumbnailUrl"},"link":{"title":"title","url":"url","thumbnailUrl":"thumbnailUrl"},"driveFile":{"shareMode":"UNKNOWN_SHARE_MODE","driveFile":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}},"youtubeVideo":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}},{"form":{"responseUrl":"responseUrl","formUrl":"formUrl","title":"title","thumbnailUrl":"thumbnailUrl"},"link":{"title":"title","url":"url","thumbnailUrl":"thumbnailUrl"},"driveFile":{"shareMode":"UNKNOWN_SHARE_MODE","driveFile":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}},"youtubeVideo":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}}],"alternateLink":"alternateLink","id":"id","state":"COURSEWORK_MATERIAL_STATE_UNSPECIFIED","assigneeMode":"ASSIGNEE_MODE_UNSPECIFIED","courseId":"courseId","individualStudentsOptions":{"studentIds":["studentIds","studentIds"]}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/courses/{course_id}/courseWorkMaterials/{id}'.format(course_id='course_id_example', id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_course_work_modify_assignees(client):
    """Test case for classroom_courses_course_work_modify_assignees

    
    """
    body = {"modifyIndividualStudentsOptions":{"removeStudentIds":["removeStudentIds","removeStudentIds"],"addStudentIds":["addStudentIds","addStudentIds"]},"assigneeMode":"ASSIGNEE_MODE_UNSPECIFIED"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/courses/{course_id}/courseWork/{idmodify_assignee}'.format(course_id='course_id_example', id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_course_work_patch(client):
    """Test case for classroom_courses_course_work_patch

    
    """
    body = {"creatorUserId":"creatorUserId","scheduledTime":"scheduledTime","creationTime":"creationTime","multipleChoiceQuestion":{"choices":["choices","choices"]},"submissionModificationMode":"SUBMISSION_MODIFICATION_MODE_UNSPECIFIED","assignment":{"studentWorkFolder":{"alternateLink":"alternateLink","id":"id","title":"title"}},"dueDate":{"month":6,"year":1,"day":0},"description":"description","updateTime":"updateTime","dueTime":{"hours":5,"seconds":7,"nanos":2,"minutes":5},"title":"title","topicId":"topicId","materials":[{"form":{"responseUrl":"responseUrl","formUrl":"formUrl","title":"title","thumbnailUrl":"thumbnailUrl"},"link":{"title":"title","url":"url","thumbnailUrl":"thumbnailUrl"},"driveFile":{"shareMode":"UNKNOWN_SHARE_MODE","driveFile":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}},"youtubeVideo":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}},{"form":{"responseUrl":"responseUrl","formUrl":"formUrl","title":"title","thumbnailUrl":"thumbnailUrl"},"link":{"title":"title","url":"url","thumbnailUrl":"thumbnailUrl"},"driveFile":{"shareMode":"UNKNOWN_SHARE_MODE","driveFile":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}},"youtubeVideo":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}}],"maxPoints":9.301444243932576,"workType":"COURSE_WORK_TYPE_UNSPECIFIED","alternateLink":"alternateLink","id":"id","state":"COURSE_WORK_STATE_UNSPECIFIED","assigneeMode":"ASSIGNEE_MODE_UNSPECIFIED","courseId":"courseId","gradeCategory":{"defaultGradeDenominator":0,"name":"name","weight":6,"id":"id"},"associatedWithDeveloper":True,"individualStudentsOptions":{"studentIds":["studentIds","studentIds"]}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/courses/{course_id}/courseWork/{id}'.format(course_id='course_id_example', id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_course_work_student_submissions_get(client):
    """Test case for classroom_courses_course_work_student_submissions_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/courses/{course_id}/courseWork/{course_work_id}/studentSubmissions/{id}'.format(course_id='course_id_example', course_work_id='course_work_id_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_course_work_student_submissions_list(client):
    """Test case for classroom_courses_course_work_student_submissions_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('late', 'late_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('states', ['states_example']),
                    ('userId', 'user_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/courses/{course_id}/courseWork/{course_work_id}/studentSubmissions'.format(course_id='course_id_example', course_work_id='course_work_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_course_work_student_submissions_modify_attachments(client):
    """Test case for classroom_courses_course_work_student_submissions_modify_attachments

    
    """
    body = {"addAttachments":[{"youTubeVideo":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"},"form":{"responseUrl":"responseUrl","formUrl":"formUrl","title":"title","thumbnailUrl":"thumbnailUrl"},"link":{"title":"title","url":"url","thumbnailUrl":"thumbnailUrl"},"driveFile":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}},{"youTubeVideo":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"},"form":{"responseUrl":"responseUrl","formUrl":"formUrl","title":"title","thumbnailUrl":"thumbnailUrl"},"link":{"title":"title","url":"url","thumbnailUrl":"thumbnailUrl"},"driveFile":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}}]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/courses/{course_id}/courseWork/{course_work_id}/studentSubmissions/{idmodify_attachment}'.format(course_id='course_id_example', course_work_id='course_work_id_example', id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_course_work_student_submissions_patch(client):
    """Test case for classroom_courses_course_work_student_submissions_patch

    
    """
    body = {"creationTime":"creationTime","multipleChoiceSubmission":{"answer":"answer"},"updateTime":"updateTime","courseWorkId":"courseWorkId","userId":"userId","courseWorkType":"COURSE_WORK_TYPE_UNSPECIFIED","draftGrade":6.027456183070403,"shortAnswerSubmission":{"answer":"answer"},"late":True,"assignedGrade":0.8008281904610115,"alternateLink":"alternateLink","id":"id","state":"SUBMISSION_STATE_UNSPECIFIED","submissionHistory":[{"stateHistory":{"actorUserId":"actorUserId","stateTimestamp":"stateTimestamp","state":"STATE_UNSPECIFIED"},"gradeHistory":{"gradeTimestamp":"gradeTimestamp","actorUserId":"actorUserId","pointsEarned":5.962133916683182,"maxPoints":1.4658129805029452,"gradeChangeType":"UNKNOWN_GRADE_CHANGE_TYPE"}},{"stateHistory":{"actorUserId":"actorUserId","stateTimestamp":"stateTimestamp","state":"STATE_UNSPECIFIED"},"gradeHistory":{"gradeTimestamp":"gradeTimestamp","actorUserId":"actorUserId","pointsEarned":5.962133916683182,"maxPoints":1.4658129805029452,"gradeChangeType":"UNKNOWN_GRADE_CHANGE_TYPE"}}],"courseId":"courseId","assignmentSubmission":{"attachments":[{"youTubeVideo":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"},"form":{"responseUrl":"responseUrl","formUrl":"formUrl","title":"title","thumbnailUrl":"thumbnailUrl"},"link":{"title":"title","url":"url","thumbnailUrl":"thumbnailUrl"},"driveFile":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}},{"youTubeVideo":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"},"form":{"responseUrl":"responseUrl","formUrl":"formUrl","title":"title","thumbnailUrl":"thumbnailUrl"},"link":{"title":"title","url":"url","thumbnailUrl":"thumbnailUrl"},"driveFile":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}}]},"associatedWithDeveloper":True}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/courses/{course_id}/courseWork/{course_work_id}/studentSubmissions/{id}'.format(course_id='course_id_example', course_work_id='course_work_id_example', id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_course_work_student_submissions_reclaim(client):
    """Test case for classroom_courses_course_work_student_submissions_reclaim

    
    """
    body = None
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/courses/{course_id}/courseWork/{course_work_id}/studentSubmissions/{idreclai}'.format(course_id='course_id_example', course_work_id='course_work_id_example', id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_course_work_student_submissions_return(client):
    """Test case for classroom_courses_course_work_student_submissions_return

    
    """
    body = None
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/courses/{course_id}/courseWork/{course_work_id}/studentSubmissions/{idretur}'.format(course_id='course_id_example', course_work_id='course_work_id_example', id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_course_work_student_submissions_turn_in(client):
    """Test case for classroom_courses_course_work_student_submissions_turn_in

    
    """
    body = None
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/courses/{course_id}/courseWork/{course_work_id}/studentSubmissions/{idturn_i}'.format(course_id='course_id_example', course_work_id='course_work_id_example', id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_create(client):
    """Test case for classroom_courses_create

    
    """
    body = {"courseGroupEmail":"courseGroupEmail","creationTime":"creationTime","courseMaterialSets":[{"materials":[{"youTubeVideo":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"},"form":{"responseUrl":"responseUrl","formUrl":"formUrl","title":"title","thumbnailUrl":"thumbnailUrl"},"link":{"title":"title","url":"url","thumbnailUrl":"thumbnailUrl"},"driveFile":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}},{"youTubeVideo":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"},"form":{"responseUrl":"responseUrl","formUrl":"formUrl","title":"title","thumbnailUrl":"thumbnailUrl"},"link":{"title":"title","url":"url","thumbnailUrl":"thumbnailUrl"},"driveFile":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}}],"title":"title"},{"materials":[{"youTubeVideo":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"},"form":{"responseUrl":"responseUrl","formUrl":"formUrl","title":"title","thumbnailUrl":"thumbnailUrl"},"link":{"title":"title","url":"url","thumbnailUrl":"thumbnailUrl"},"driveFile":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}},{"youTubeVideo":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"},"form":{"responseUrl":"responseUrl","formUrl":"formUrl","title":"title","thumbnailUrl":"thumbnailUrl"},"link":{"title":"title","url":"url","thumbnailUrl":"thumbnailUrl"},"driveFile":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}}],"title":"title"}],"description":"description","guardiansEnabled":True,"section":"section","updateTime":"updateTime","enrollmentCode":"enrollmentCode","ownerId":"ownerId","room":"room","descriptionHeading":"descriptionHeading","calendarId":"calendarId","courseState":"COURSE_STATE_UNSPECIFIED","name":"name","teacherGroupEmail":"teacherGroupEmail","alternateLink":"alternateLink","id":"id","gradebookSettings":{"calculationType":"CALCULATION_TYPE_UNSPECIFIED","displaySetting":"DISPLAY_SETTING_UNSPECIFIED","gradeCategories":[{"defaultGradeDenominator":0,"name":"name","weight":6,"id":"id"},{"defaultGradeDenominator":0,"name":"name","weight":6,"id":"id"}]},"teacherFolder":{"alternateLink":"alternateLink","id":"id","title":"title"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/courses',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_delete(client):
    """Test case for classroom_courses_delete

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/courses/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_get(client):
    """Test case for classroom_courses_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/courses/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_list(client):
    """Test case for classroom_courses_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('courseStates', ['course_states_example']),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example'),
                    ('studentId', 'student_id_example'),
                    ('teacherId', 'teacher_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/courses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_patch(client):
    """Test case for classroom_courses_patch

    
    """
    body = {"courseGroupEmail":"courseGroupEmail","creationTime":"creationTime","courseMaterialSets":[{"materials":[{"youTubeVideo":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"},"form":{"responseUrl":"responseUrl","formUrl":"formUrl","title":"title","thumbnailUrl":"thumbnailUrl"},"link":{"title":"title","url":"url","thumbnailUrl":"thumbnailUrl"},"driveFile":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}},{"youTubeVideo":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"},"form":{"responseUrl":"responseUrl","formUrl":"formUrl","title":"title","thumbnailUrl":"thumbnailUrl"},"link":{"title":"title","url":"url","thumbnailUrl":"thumbnailUrl"},"driveFile":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}}],"title":"title"},{"materials":[{"youTubeVideo":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"},"form":{"responseUrl":"responseUrl","formUrl":"formUrl","title":"title","thumbnailUrl":"thumbnailUrl"},"link":{"title":"title","url":"url","thumbnailUrl":"thumbnailUrl"},"driveFile":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}},{"youTubeVideo":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"},"form":{"responseUrl":"responseUrl","formUrl":"formUrl","title":"title","thumbnailUrl":"thumbnailUrl"},"link":{"title":"title","url":"url","thumbnailUrl":"thumbnailUrl"},"driveFile":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}}],"title":"title"}],"description":"description","guardiansEnabled":True,"section":"section","updateTime":"updateTime","enrollmentCode":"enrollmentCode","ownerId":"ownerId","room":"room","descriptionHeading":"descriptionHeading","calendarId":"calendarId","courseState":"COURSE_STATE_UNSPECIFIED","name":"name","teacherGroupEmail":"teacherGroupEmail","alternateLink":"alternateLink","id":"id","gradebookSettings":{"calculationType":"CALCULATION_TYPE_UNSPECIFIED","displaySetting":"DISPLAY_SETTING_UNSPECIFIED","gradeCategories":[{"defaultGradeDenominator":0,"name":"name","weight":6,"id":"id"},{"defaultGradeDenominator":0,"name":"name","weight":6,"id":"id"}]},"teacherFolder":{"alternateLink":"alternateLink","id":"id","title":"title"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/courses/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_students_create(client):
    """Test case for classroom_courses_students_create

    
    """
    body = {"profile":{"photoUrl":"photoUrl","emailAddress":"emailAddress","permissions":[{"permission":"PERMISSION_UNSPECIFIED"},{"permission":"PERMISSION_UNSPECIFIED"}],"name":{"familyName":"familyName","givenName":"givenName","fullName":"fullName"},"id":"id","verifiedTeacher":True},"studentWorkFolder":{"alternateLink":"alternateLink","id":"id","title":"title"},"courseId":"courseId","userId":"userId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('enrollmentCode', 'enrollment_code_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/courses/{course_id}/students'.format(course_id='course_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_students_delete(client):
    """Test case for classroom_courses_students_delete

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/courses/{course_id}/students/{user_id}'.format(course_id='course_id_example', user_id='user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_students_get(client):
    """Test case for classroom_courses_students_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/courses/{course_id}/students/{user_id}'.format(course_id='course_id_example', user_id='user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_students_list(client):
    """Test case for classroom_courses_students_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/courses/{course_id}/students'.format(course_id='course_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_teachers_create(client):
    """Test case for classroom_courses_teachers_create

    
    """
    body = {"profile":{"photoUrl":"photoUrl","emailAddress":"emailAddress","permissions":[{"permission":"PERMISSION_UNSPECIFIED"},{"permission":"PERMISSION_UNSPECIFIED"}],"name":{"familyName":"familyName","givenName":"givenName","fullName":"fullName"},"id":"id","verifiedTeacher":True},"courseId":"courseId","userId":"userId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/courses/{course_id}/teachers'.format(course_id='course_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_teachers_delete(client):
    """Test case for classroom_courses_teachers_delete

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/courses/{course_id}/teachers/{user_id}'.format(course_id='course_id_example', user_id='user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_teachers_get(client):
    """Test case for classroom_courses_teachers_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/courses/{course_id}/teachers/{user_id}'.format(course_id='course_id_example', user_id='user_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_teachers_list(client):
    """Test case for classroom_courses_teachers_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/courses/{course_id}/teachers'.format(course_id='course_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_topics_create(client):
    """Test case for classroom_courses_topics_create

    
    """
    body = {"topicId":"topicId","name":"name","updateTime":"updateTime","courseId":"courseId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/courses/{course_id}/topics'.format(course_id='course_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_topics_delete(client):
    """Test case for classroom_courses_topics_delete

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/courses/{course_id}/topics/{id}'.format(course_id='course_id_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_topics_get(client):
    """Test case for classroom_courses_topics_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/courses/{course_id}/topics/{id}'.format(course_id='course_id_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_topics_list(client):
    """Test case for classroom_courses_topics_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/courses/{course_id}/topics'.format(course_id='course_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_topics_patch(client):
    """Test case for classroom_courses_topics_patch

    
    """
    body = {"topicId":"topicId","name":"name","updateTime":"updateTime","courseId":"courseId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/courses/{course_id}/topics/{id}'.format(course_id='course_id_example', id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_classroom_courses_update(client):
    """Test case for classroom_courses_update

    
    """
    body = {"courseGroupEmail":"courseGroupEmail","creationTime":"creationTime","courseMaterialSets":[{"materials":[{"youTubeVideo":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"},"form":{"responseUrl":"responseUrl","formUrl":"formUrl","title":"title","thumbnailUrl":"thumbnailUrl"},"link":{"title":"title","url":"url","thumbnailUrl":"thumbnailUrl"},"driveFile":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}},{"youTubeVideo":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"},"form":{"responseUrl":"responseUrl","formUrl":"formUrl","title":"title","thumbnailUrl":"thumbnailUrl"},"link":{"title":"title","url":"url","thumbnailUrl":"thumbnailUrl"},"driveFile":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}}],"title":"title"},{"materials":[{"youTubeVideo":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"},"form":{"responseUrl":"responseUrl","formUrl":"formUrl","title":"title","thumbnailUrl":"thumbnailUrl"},"link":{"title":"title","url":"url","thumbnailUrl":"thumbnailUrl"},"driveFile":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}},{"youTubeVideo":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"},"form":{"responseUrl":"responseUrl","formUrl":"formUrl","title":"title","thumbnailUrl":"thumbnailUrl"},"link":{"title":"title","url":"url","thumbnailUrl":"thumbnailUrl"},"driveFile":{"alternateLink":"alternateLink","id":"id","title":"title","thumbnailUrl":"thumbnailUrl"}}],"title":"title"}],"description":"description","guardiansEnabled":True,"section":"section","updateTime":"updateTime","enrollmentCode":"enrollmentCode","ownerId":"ownerId","room":"room","descriptionHeading":"descriptionHeading","calendarId":"calendarId","courseState":"COURSE_STATE_UNSPECIFIED","name":"name","teacherGroupEmail":"teacherGroupEmail","alternateLink":"alternateLink","id":"id","gradebookSettings":{"calculationType":"CALCULATION_TYPE_UNSPECIFIED","displaySetting":"DISPLAY_SETTING_UNSPECIFIED","gradeCategories":[{"defaultGradeDenominator":0,"name":"name","weight":6,"id":"id"},{"defaultGradeDenominator":0,"name":"name","weight":6,"id":"id"}]},"teacherFolder":{"alternateLink":"alternateLink","id":"id","title":"title"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/courses/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

