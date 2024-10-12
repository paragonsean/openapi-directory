from typing import List, Dict
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
from openapi_server import util


async def classroom_courses_aliases_create(request: web.Request, course_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """classroom_courses_aliases_create

    Creates an alias for a course. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to create the alias or for access errors. * &#x60;NOT_FOUND&#x60; if the course does not exist. * &#x60;ALREADY_EXISTS&#x60; if the alias already exists. * &#x60;FAILED_PRECONDITION&#x60; if the alias requested does not make sense for the requesting user or course (for example, if a user not in a domain attempts to access a domain-scoped alias).

    :param course_id: Identifier of the course to alias. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = CourseAlias.from_dict(body)
    return web.Response(status=200)


async def classroom_courses_aliases_delete(request: web.Request, course_id, alias, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """classroom_courses_aliases_delete

    Deletes an alias of a course. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to remove the alias or for access errors. * &#x60;NOT_FOUND&#x60; if the alias does not exist. * &#x60;FAILED_PRECONDITION&#x60; if the alias requested does not make sense for the requesting user or course (for example, if a user not in a domain attempts to delete a domain-scoped alias).

    :param course_id: Identifier of the course whose alias should be deleted. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param alias: Alias to delete. This may not be the Classroom-assigned identifier.
    :type alias: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def classroom_courses_aliases_list(request: web.Request, course_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """classroom_courses_aliases_list

    Returns a list of aliases for a course. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to access the course or for access errors. * &#x60;NOT_FOUND&#x60; if the course does not exist.

    :param course_id: The identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param page_size: Maximum number of items to return. Zero or unspecified indicates that the server may assign a maximum. The server may return fewer than the specified number of results.
    :type page_size: int
    :param page_token: nextPageToken value returned from a previous list call, indicating that the subsequent page of results should be returned. The list request must be otherwise identical to the one that resulted in this token.
    :type page_token: str

    """
    return web.Response(status=200)


async def classroom_courses_announcements_create(request: web.Request, course_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """classroom_courses_announcements_create

    Creates an announcement. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to access the requested course, create announcements in the requested course, share a Drive attachment, or for access errors. * &#x60;INVALID_ARGUMENT&#x60; if the request is malformed. * &#x60;NOT_FOUND&#x60; if the requested course does not exist. * &#x60;FAILED_PRECONDITION&#x60; for the following request error: * AttachmentNotVisible

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = Announcement.from_dict(body)
    return web.Response(status=200)


async def classroom_courses_announcements_delete(request: web.Request, course_id, id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """classroom_courses_announcements_delete

    Deletes an announcement. This request must be made by the Developer Console project of the [OAuth client ID](https://support.google.com/cloud/answer/6158849) used to create the corresponding announcement item. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting developer project did not create the corresponding announcement, if the requesting user is not permitted to delete the requested course or for access errors. * &#x60;FAILED_PRECONDITION&#x60; if the requested announcement has already been deleted. * &#x60;NOT_FOUND&#x60; if no course exists with the requested ID.

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param id: Identifier of the announcement to delete. This identifier is a Classroom-assigned identifier.
    :type id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def classroom_courses_announcements_get(request: web.Request, course_id, id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """classroom_courses_announcements_get

    Returns an announcement. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to access the requested course or announcement, or for access errors. * &#x60;INVALID_ARGUMENT&#x60; if the request is malformed. * &#x60;NOT_FOUND&#x60; if the requested course or announcement does not exist.

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param id: Identifier of the announcement.
    :type id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def classroom_courses_announcements_list(request: web.Request, course_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, announcement_states=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """classroom_courses_announcements_list

    Returns a list of announcements that the requester is permitted to view. Course students may only view &#x60;PUBLISHED&#x60; announcements. Course teachers and domain administrators may view all announcements. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to access the requested course or for access errors. * &#x60;INVALID_ARGUMENT&#x60; if the request is malformed. * &#x60;NOT_FOUND&#x60; if the requested course does not exist.

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param announcement_states: Restriction on the &#x60;state&#x60; of announcements returned. If this argument is left unspecified, the default value is &#x60;PUBLISHED&#x60;.
    :type announcement_states: List[str]
    :param order_by: Optional sort ordering for results. A comma-separated list of fields with an optional sort direction keyword. Supported field is &#x60;updateTime&#x60;. Supported direction keywords are &#x60;asc&#x60; and &#x60;desc&#x60;. If not specified, &#x60;updateTime desc&#x60; is the default behavior. Examples: &#x60;updateTime asc&#x60;, &#x60;updateTime&#x60;
    :type order_by: str
    :param page_size: Maximum number of items to return. Zero or unspecified indicates that the server may assign a maximum. The server may return fewer than the specified number of results.
    :type page_size: int
    :param page_token: nextPageToken value returned from a previous list call, indicating that the subsequent page of results should be returned. The list request must be otherwise identical to the one that resulted in this token.
    :type page_token: str

    """
    return web.Response(status=200)


async def classroom_courses_announcements_modify_assignees(request: web.Request, course_id, id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """classroom_courses_announcements_modify_assignees

    Modifies assignee mode and options of an announcement. Only a teacher of the course that contains the announcement may call this method. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to access the requested course or course work or for access errors. * &#x60;INVALID_ARGUMENT&#x60; if the request is malformed. * &#x60;NOT_FOUND&#x60; if the requested course or course work does not exist.

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param id: Identifier of the announcement.
    :type id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = ModifyAnnouncementAssigneesRequest.from_dict(body)
    return web.Response(status=200)


async def classroom_courses_announcements_patch(request: web.Request, course_id, id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """classroom_courses_announcements_patch

    Updates one or more fields of an announcement. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting developer project did not create the corresponding announcement or for access errors. * &#x60;INVALID_ARGUMENT&#x60; if the request is malformed. * &#x60;FAILED_PRECONDITION&#x60; if the requested announcement has already been deleted. * &#x60;NOT_FOUND&#x60; if the requested course or announcement does not exist

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param id: Identifier of the announcement.
    :type id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param update_mask: Mask that identifies which fields on the announcement to update. This field is required to do an update. The update fails if invalid fields are specified. If a field supports empty values, it can be cleared by specifying it in the update mask and not in the Announcement object. If a field that does not support empty values is included in the update mask and not set in the Announcement object, an &#x60;INVALID_ARGUMENT&#x60; error is returned. The following fields may be specified by teachers: * &#x60;text&#x60; * &#x60;state&#x60; * &#x60;scheduled_time&#x60;
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = Announcement.from_dict(body)
    return web.Response(status=200)


async def classroom_courses_course_work_create(request: web.Request, course_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """classroom_courses_course_work_create

    Creates course work. The resulting course work (and corresponding student submissions) are associated with the Developer Console project of the [OAuth client ID](https://support.google.com/cloud/answer/6158849) used to make the request. Classroom API requests to modify course work and student submissions must be made with an OAuth client ID from the associated Developer Console project. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to access the requested course, create course work in the requested course, share a Drive attachment, or for access errors. * &#x60;INVALID_ARGUMENT&#x60; if the request is malformed. * &#x60;NOT_FOUND&#x60; if the requested course does not exist. * &#x60;FAILED_PRECONDITION&#x60; for the following request error: * AttachmentNotVisible

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = CourseWork.from_dict(body)
    return web.Response(status=200)


async def classroom_courses_course_work_delete(request: web.Request, course_id, id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """classroom_courses_course_work_delete

    Deletes a course work. This request must be made by the Developer Console project of the [OAuth client ID](https://support.google.com/cloud/answer/6158849) used to create the corresponding course work item. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting developer project did not create the corresponding course work, if the requesting user is not permitted to delete the requested course or for access errors. * &#x60;FAILED_PRECONDITION&#x60; if the requested course work has already been deleted. * &#x60;NOT_FOUND&#x60; if no course exists with the requested ID.

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param id: Identifier of the course work to delete. This identifier is a Classroom-assigned identifier.
    :type id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def classroom_courses_course_work_get(request: web.Request, course_id, id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """classroom_courses_course_work_get

    Returns course work. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to access the requested course or course work, or for access errors. * &#x60;INVALID_ARGUMENT&#x60; if the request is malformed. * &#x60;NOT_FOUND&#x60; if the requested course or course work does not exist.

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param id: Identifier of the course work.
    :type id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def classroom_courses_course_work_list(request: web.Request, course_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, course_work_states=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """classroom_courses_course_work_list

    Returns a list of course work that the requester is permitted to view. Course students may only view &#x60;PUBLISHED&#x60; course work. Course teachers and domain administrators may view all course work. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to access the requested course or for access errors. * &#x60;INVALID_ARGUMENT&#x60; if the request is malformed. * &#x60;NOT_FOUND&#x60; if the requested course does not exist.

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param course_work_states: Restriction on the work status to return. Only courseWork that matches is returned. If unspecified, items with a work status of &#x60;PUBLISHED&#x60; is returned.
    :type course_work_states: List[str]
    :param order_by: Optional sort ordering for results. A comma-separated list of fields with an optional sort direction keyword. Supported fields are &#x60;updateTime&#x60; and &#x60;dueDate&#x60;. Supported direction keywords are &#x60;asc&#x60; and &#x60;desc&#x60;. If not specified, &#x60;updateTime desc&#x60; is the default behavior. Examples: &#x60;dueDate asc,updateTime desc&#x60;, &#x60;updateTime,dueDate desc&#x60;
    :type order_by: str
    :param page_size: Maximum number of items to return. Zero or unspecified indicates that the server may assign a maximum. The server may return fewer than the specified number of results.
    :type page_size: int
    :param page_token: nextPageToken value returned from a previous list call, indicating that the subsequent page of results should be returned. The list request must be otherwise identical to the one that resulted in this token.
    :type page_token: str

    """
    return web.Response(status=200)


async def classroom_courses_course_work_materials_create(request: web.Request, course_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """classroom_courses_course_work_materials_create

    Creates a course work material. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to access the requested course, create course work material in the requested course, share a Drive attachment, or for access errors. * &#x60;INVALID_ARGUMENT&#x60; if the request is malformed or if more than 20 * materials are provided. * &#x60;NOT_FOUND&#x60; if the requested course does not exist. * &#x60;FAILED_PRECONDITION&#x60; for the following request error: * AttachmentNotVisible

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = CourseWorkMaterial.from_dict(body)
    return web.Response(status=200)


async def classroom_courses_course_work_materials_delete(request: web.Request, course_id, id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """classroom_courses_course_work_materials_delete

    Deletes a course work material. This request must be made by the Developer Console project of the [OAuth client ID](https://support.google.com/cloud/answer/6158849) used to create the corresponding course work material item. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting developer project did not create the corresponding course work material, if the requesting user is not permitted to delete the requested course or for access errors. * &#x60;FAILED_PRECONDITION&#x60; if the requested course work material has already been deleted. * &#x60;NOT_FOUND&#x60; if no course exists with the requested ID.

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param id: Identifier of the course work material to delete. This identifier is a Classroom-assigned identifier.
    :type id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def classroom_courses_course_work_materials_get(request: web.Request, course_id, id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """classroom_courses_course_work_materials_get

    Returns a course work material. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to access the requested course or course work material, or for access errors. * &#x60;INVALID_ARGUMENT&#x60; if the request is malformed. * &#x60;NOT_FOUND&#x60; if the requested course or course work material does not exist.

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param id: Identifier of the course work material.
    :type id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def classroom_courses_course_work_materials_list(request: web.Request, course_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, course_work_material_states=None, material_drive_id=None, material_link=None, order_by=None, page_size=None, page_token=None) -> web.Response:
    """classroom_courses_course_work_materials_list

    Returns a list of course work material that the requester is permitted to view. Course students may only view &#x60;PUBLISHED&#x60; course work material. Course teachers and domain administrators may view all course work material. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to access the requested course or for access errors. * &#x60;INVALID_ARGUMENT&#x60; if the request is malformed. * &#x60;NOT_FOUND&#x60; if the requested course does not exist.

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param course_work_material_states: Restriction on the work status to return. Only course work material that matches is returned. If unspecified, items with a work status of &#x60;PUBLISHED&#x60; is returned.
    :type course_work_material_states: List[str]
    :param material_drive_id: Optional filtering for course work material with at least one Drive material whose ID matches the provided string. If &#x60;material_link&#x60; is also specified, course work material must have materials matching both filters.
    :type material_drive_id: str
    :param material_link: Optional filtering for course work material with at least one link material whose URL partially matches the provided string.
    :type material_link: str
    :param order_by: Optional sort ordering for results. A comma-separated list of fields with an optional sort direction keyword. Supported field is &#x60;updateTime&#x60;. Supported direction keywords are &#x60;asc&#x60; and &#x60;desc&#x60;. If not specified, &#x60;updateTime desc&#x60; is the default behavior. Examples: &#x60;updateTime asc&#x60;, &#x60;updateTime&#x60;
    :type order_by: str
    :param page_size: Maximum number of items to return. Zero or unspecified indicates that the server may assign a maximum. The server may return fewer than the specified number of results.
    :type page_size: int
    :param page_token: nextPageToken value returned from a previous list call, indicating that the subsequent page of results should be returned. The list request must be otherwise identical to the one that resulted in this token.
    :type page_token: str

    """
    return web.Response(status=200)


async def classroom_courses_course_work_materials_patch(request: web.Request, course_id, id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """classroom_courses_course_work_materials_patch

    Updates one or more fields of a course work material. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting developer project for access errors. * &#x60;INVALID_ARGUMENT&#x60; if the request is malformed. * &#x60;FAILED_PRECONDITION&#x60; if the requested course work material has already been deleted. * &#x60;NOT_FOUND&#x60; if the requested course or course work material does not exist

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param id: Identifier of the course work material.
    :type id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param update_mask: Mask that identifies which fields on the course work material to update. This field is required to do an update. The update fails if invalid fields are specified. If a field supports empty values, it can be cleared by specifying it in the update mask and not in the course work material object. If a field that does not support empty values is included in the update mask and not set in the course work material object, an &#x60;INVALID_ARGUMENT&#x60; error is returned. The following fields may be specified by teachers: * &#x60;title&#x60; * &#x60;description&#x60; * &#x60;state&#x60; * &#x60;scheduled_time&#x60; * &#x60;topic_id&#x60;
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = CourseWorkMaterial.from_dict(body)
    return web.Response(status=200)


async def classroom_courses_course_work_modify_assignees(request: web.Request, course_id, id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """classroom_courses_course_work_modify_assignees

    Modifies assignee mode and options of a coursework. Only a teacher of the course that contains the coursework may call this method. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to access the requested course or course work or for access errors. * &#x60;INVALID_ARGUMENT&#x60; if the request is malformed. * &#x60;NOT_FOUND&#x60; if the requested course or course work does not exist.

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param id: Identifier of the coursework.
    :type id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = ModifyCourseWorkAssigneesRequest.from_dict(body)
    return web.Response(status=200)


async def classroom_courses_course_work_patch(request: web.Request, course_id, id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """classroom_courses_course_work_patch

    Updates one or more fields of a course work. See google.classroom.v1.CourseWork for details of which fields may be updated and who may change them. This request must be made by the Developer Console project of the [OAuth client ID](https://support.google.com/cloud/answer/6158849) used to create the corresponding course work item. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting developer project did not create the corresponding course work, if the user is not permitted to make the requested modification to the student submission, or for access errors. * &#x60;INVALID_ARGUMENT&#x60; if the request is malformed. * &#x60;FAILED_PRECONDITION&#x60; if the requested course work has already been deleted. * &#x60;NOT_FOUND&#x60; if the requested course, course work, or student submission does not exist.

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param id: Identifier of the course work.
    :type id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param update_mask: Mask that identifies which fields on the course work to update. This field is required to do an update. The update fails if invalid fields are specified. If a field supports empty values, it can be cleared by specifying it in the update mask and not in the &#x60;CourseWork&#x60; object. If a field that does not support empty values is included in the update mask and not set in the &#x60;CourseWork&#x60; object, an &#x60;INVALID_ARGUMENT&#x60; error is returned. The following fields may be specified by teachers: * &#x60;title&#x60; * &#x60;description&#x60; * &#x60;state&#x60; * &#x60;due_date&#x60; * &#x60;due_time&#x60; * &#x60;max_points&#x60; * &#x60;scheduled_time&#x60; * &#x60;submission_modification_mode&#x60; * &#x60;topic_id&#x60;
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = CourseWork.from_dict(body)
    return web.Response(status=200)


async def classroom_courses_course_work_student_submissions_get(request: web.Request, course_id, course_work_id, id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """classroom_courses_course_work_student_submissions_get

    Returns a student submission. * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to access the requested course, course work, or student submission or for access errors. * &#x60;INVALID_ARGUMENT&#x60; if the request is malformed. * &#x60;NOT_FOUND&#x60; if the requested course, course work, or student submission does not exist.

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param course_work_id: Identifier of the course work.
    :type course_work_id: str
    :param id: Identifier of the student submission.
    :type id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def classroom_courses_course_work_student_submissions_list(request: web.Request, course_id, course_work_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, late=None, page_size=None, page_token=None, states=None, user_id=None) -> web.Response:
    """classroom_courses_course_work_student_submissions_list

    Returns a list of student submissions that the requester is permitted to view, factoring in the OAuth scopes of the request. &#x60;-&#x60; may be specified as the &#x60;course_work_id&#x60; to include student submissions for multiple course work items. Course students may only view their own work. Course teachers and domain administrators may view all student submissions. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to access the requested course or course work, or for access errors. * &#x60;INVALID_ARGUMENT&#x60; if the request is malformed. * &#x60;NOT_FOUND&#x60; if the requested course does not exist.

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param course_work_id: Identifier of the student work to request. This may be set to the string literal &#x60;\&quot;-\&quot;&#x60; to request student work for all course work in the specified course.
    :type course_work_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param late: Requested lateness value. If specified, returned student submissions are restricted by the requested value. If unspecified, submissions are returned regardless of &#x60;late&#x60; value.
    :type late: str
    :param page_size: Maximum number of items to return. Zero or unspecified indicates that the server may assign a maximum. The server may return fewer than the specified number of results.
    :type page_size: int
    :param page_token: nextPageToken value returned from a previous list call, indicating that the subsequent page of results should be returned. The list request must be otherwise identical to the one that resulted in this token.
    :type page_token: str
    :param states: Requested submission states. If specified, returned student submissions match one of the specified submission states.
    :type states: List[str]
    :param user_id: Optional argument to restrict returned student work to those owned by the student with the specified identifier. The identifier can be one of the following: * the numeric identifier for the user * the email address of the user * the string literal &#x60;\&quot;me\&quot;&#x60;, indicating the requesting user
    :type user_id: str

    """
    return web.Response(status=200)


async def classroom_courses_course_work_student_submissions_modify_attachments(request: web.Request, course_id, course_work_id, id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """classroom_courses_course_work_student_submissions_modify_attachments

    Modifies attachments of student submission. Attachments may only be added to student submissions belonging to course work objects with a &#x60;workType&#x60; of &#x60;ASSIGNMENT&#x60;. This request must be made by the Developer Console project of the [OAuth client ID](https://support.google.com/cloud/answer/6158849) used to create the corresponding course work item. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to access the requested course or course work, if the user is not permitted to modify attachments on the requested student submission, or for access errors. * &#x60;INVALID_ARGUMENT&#x60; if the request is malformed. * &#x60;NOT_FOUND&#x60; if the requested course, course work, or student submission does not exist.

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param course_work_id: Identifier of the course work.
    :type course_work_id: str
    :param id: Identifier of the student submission.
    :type id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = ModifyAttachmentsRequest.from_dict(body)
    return web.Response(status=200)


async def classroom_courses_course_work_student_submissions_patch(request: web.Request, course_id, course_work_id, id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """classroom_courses_course_work_student_submissions_patch

    Updates one or more fields of a student submission. See google.classroom.v1.StudentSubmission for details of which fields may be updated and who may change them. This request must be made by the Developer Console project of the [OAuth client ID](https://support.google.com/cloud/answer/6158849) used to create the corresponding course work item. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting developer project did not create the corresponding course work, if the user is not permitted to make the requested modification to the student submission, or for access errors. * &#x60;INVALID_ARGUMENT&#x60; if the request is malformed. * &#x60;NOT_FOUND&#x60; if the requested course, course work, or student submission does not exist.

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param course_work_id: Identifier of the course work.
    :type course_work_id: str
    :param id: Identifier of the student submission.
    :type id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param update_mask: Mask that identifies which fields on the student submission to update. This field is required to do an update. The update fails if invalid fields are specified. The following fields may be specified by teachers: * &#x60;draft_grade&#x60; * &#x60;assigned_grade&#x60;
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = StudentSubmission.from_dict(body)
    return web.Response(status=200)


async def classroom_courses_course_work_student_submissions_reclaim(request: web.Request, course_id, course_work_id, id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """classroom_courses_course_work_student_submissions_reclaim

    Reclaims a student submission on behalf of the student that owns it. Reclaiming a student submission transfers ownership of attached Drive files to the student and updates the submission state. Only the student that owns the requested student submission may call this method, and only for a student submission that has been turned in. This request must be made by the Developer Console project of the [OAuth client ID](https://support.google.com/cloud/answer/6158849) used to create the corresponding course work item. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to access the requested course or course work, unsubmit the requested student submission, or for access errors. * &#x60;FAILED_PRECONDITION&#x60; if the student submission has not been turned in. * &#x60;INVALID_ARGUMENT&#x60; if the request is malformed. * &#x60;NOT_FOUND&#x60; if the requested course, course work, or student submission does not exist.

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param course_work_id: Identifier of the course work.
    :type course_work_id: str
    :param id: Identifier of the student submission.
    :type id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def classroom_courses_course_work_student_submissions_return(request: web.Request, course_id, course_work_id, id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """classroom_courses_course_work_student_submissions_return

    Returns a student submission. Returning a student submission transfers ownership of attached Drive files to the student and may also update the submission state. Unlike the Classroom application, returning a student submission does not set assignedGrade to the draftGrade value. Only a teacher of the course that contains the requested student submission may call this method. This request must be made by the Developer Console project of the [OAuth client ID](https://support.google.com/cloud/answer/6158849) used to create the corresponding course work item. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to access the requested course or course work, return the requested student submission, or for access errors. * &#x60;INVALID_ARGUMENT&#x60; if the request is malformed. * &#x60;NOT_FOUND&#x60; if the requested course, course work, or student submission does not exist.

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param course_work_id: Identifier of the course work.
    :type course_work_id: str
    :param id: Identifier of the student submission.
    :type id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def classroom_courses_course_work_student_submissions_turn_in(request: web.Request, course_id, course_work_id, id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """classroom_courses_course_work_student_submissions_turn_in

    Turns in a student submission. Turning in a student submission transfers ownership of attached Drive files to the teacher and may also update the submission state. This may only be called by the student that owns the specified student submission. This request must be made by the Developer Console project of the [OAuth client ID](https://support.google.com/cloud/answer/6158849) used to create the corresponding course work item. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to access the requested course or course work, turn in the requested student submission, or for access errors. * &#x60;INVALID_ARGUMENT&#x60; if the request is malformed. * &#x60;NOT_FOUND&#x60; if the requested course, course work, or student submission does not exist.

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param course_work_id: Identifier of the course work.
    :type course_work_id: str
    :param id: Identifier of the student submission.
    :type id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def classroom_courses_create(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """classroom_courses_create

    Creates a course. The user specified in &#x60;ownerId&#x60; is the owner of the created course and added as a teacher. A non-admin requesting user can only create a course with themselves as the owner. Domain admins can create courses owned by any user within their domain. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to create courses or for access errors. * &#x60;NOT_FOUND&#x60; if the primary teacher is not a valid user. * &#x60;FAILED_PRECONDITION&#x60; if the course owner&#39;s account is disabled or for the following request errors: * UserCannotOwnCourse * UserGroupsMembershipLimitReached * &#x60;ALREADY_EXISTS&#x60; if an alias was specified in the &#x60;id&#x60; and already exists.

    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = Course.from_dict(body)
    return web.Response(status=200)


async def classroom_courses_delete(request: web.Request, id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """classroom_courses_delete

    Deletes a course. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to delete the requested course or for access errors. * &#x60;NOT_FOUND&#x60; if no course exists with the requested ID.

    :param id: Identifier of the course to delete. This identifier can be either the Classroom-assigned identifier or an alias.
    :type id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def classroom_courses_get(request: web.Request, id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """classroom_courses_get

    Returns a course. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to access the requested course or for access errors. * &#x60;NOT_FOUND&#x60; if no course exists with the requested ID.

    :param id: Identifier of the course to return. This identifier can be either the Classroom-assigned identifier or an alias.
    :type id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def classroom_courses_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, course_states=None, page_size=None, page_token=None, student_id=None, teacher_id=None) -> web.Response:
    """classroom_courses_list

    Returns a list of courses that the requesting user is permitted to view, restricted to those that match the request. Returned courses are ordered by creation time, with the most recently created coming first. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; for access errors. * &#x60;INVALID_ARGUMENT&#x60; if the query argument is malformed. * &#x60;NOT_FOUND&#x60; if any users specified in the query arguments do not exist.

    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param course_states: Restricts returned courses to those in one of the specified states The default value is ACTIVE, ARCHIVED, PROVISIONED, DECLINED.
    :type course_states: List[str]
    :param page_size: Maximum number of items to return. Zero or unspecified indicates that the server may assign a maximum. The server may return fewer than the specified number of results.
    :type page_size: int
    :param page_token: nextPageToken value returned from a previous list call, indicating that the subsequent page of results should be returned. The list request must be otherwise identical to the one that resulted in this token.
    :type page_token: str
    :param student_id: Restricts returned courses to those having a student with the specified identifier. The identifier can be one of the following: * the numeric identifier for the user * the email address of the user * the string literal &#x60;\&quot;me\&quot;&#x60;, indicating the requesting user
    :type student_id: str
    :param teacher_id: Restricts returned courses to those having a teacher with the specified identifier. The identifier can be one of the following: * the numeric identifier for the user * the email address of the user * the string literal &#x60;\&quot;me\&quot;&#x60;, indicating the requesting user
    :type teacher_id: str

    """
    return web.Response(status=200)


async def classroom_courses_patch(request: web.Request, id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """classroom_courses_patch

    Updates one or more fields in a course. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to modify the requested course or for access errors. * &#x60;NOT_FOUND&#x60; if no course exists with the requested ID. * &#x60;INVALID_ARGUMENT&#x60; if invalid fields are specified in the update mask or if no update mask is supplied. * &#x60;FAILED_PRECONDITION&#x60; for the following request errors: * CourseNotModifiable * InactiveCourseOwner * IneligibleOwner

    :param id: Identifier of the course to update. This identifier can be either the Classroom-assigned identifier or an alias.
    :type id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param update_mask: Mask that identifies which fields on the course to update. This field is required to do an update. The update will fail if invalid fields are specified. The following fields are valid: * &#x60;name&#x60; * &#x60;section&#x60; * &#x60;descriptionHeading&#x60; * &#x60;description&#x60; * &#x60;room&#x60; * &#x60;courseState&#x60; * &#x60;ownerId&#x60; Note: patches to ownerId are treated as being effective immediately, but in practice it may take some time for the ownership transfer of all affected resources to complete. When set in a query parameter, this field should be specified as &#x60;updateMask&#x3D;,,...&#x60;
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = Course.from_dict(body)
    return web.Response(status=200)


async def classroom_courses_students_create(request: web.Request, course_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, enrollment_code=None, body=None) -> web.Response:
    """classroom_courses_students_create

    Adds a user as a student of a course. Domain administrators are permitted to [directly add](https://developers.google.com/classroom/guides/manage-users) users within their domain as students to courses within their domain. Students are permitted to add themselves to a course using an enrollment code. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to create students in this course or for access errors. * &#x60;NOT_FOUND&#x60; if the requested course ID does not exist. * &#x60;FAILED_PRECONDITION&#x60; if the requested user&#39;s account is disabled, for the following request errors: * CourseMemberLimitReached * CourseNotModifiable * UserGroupsMembershipLimitReached * InactiveCourseOwner * &#x60;ALREADY_EXISTS&#x60; if the user is already a student or teacher in the course.

    :param course_id: Identifier of the course to create the student in. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param enrollment_code: Enrollment code of the course to create the student in. This code is required if userId corresponds to the requesting user; it may be omitted if the requesting user has administrative permissions to create students for any user.
    :type enrollment_code: str
    :param body: 
    :type body: dict | bytes

    """
    body = Student.from_dict(body)
    return web.Response(status=200)


async def classroom_courses_students_delete(request: web.Request, course_id, user_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """classroom_courses_students_delete

    Deletes a student of a course. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to delete students of this course or for access errors. * &#x60;NOT_FOUND&#x60; if no student of this course has the requested ID or if the course does not exist.

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param user_id: Identifier of the student to delete. The identifier can be one of the following: * the numeric identifier for the user * the email address of the user * the string literal &#x60;\&quot;me\&quot;&#x60;, indicating the requesting user
    :type user_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def classroom_courses_students_get(request: web.Request, course_id, user_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """classroom_courses_students_get

    Returns a student of a course. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to view students of this course or for access errors. * &#x60;NOT_FOUND&#x60; if no student of this course has the requested ID or if the course does not exist.

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param user_id: Identifier of the student to return. The identifier can be one of the following: * the numeric identifier for the user * the email address of the user * the string literal &#x60;\&quot;me\&quot;&#x60;, indicating the requesting user
    :type user_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def classroom_courses_students_list(request: web.Request, course_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """classroom_courses_students_list

    Returns a list of students of this course that the requester is permitted to view. This method returns the following error codes: * &#x60;NOT_FOUND&#x60; if the course does not exist. * &#x60;PERMISSION_DENIED&#x60; for access errors.

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param page_size: Maximum number of items to return. The default is 30 if unspecified or &#x60;0&#x60;. The server may return fewer than the specified number of results.
    :type page_size: int
    :param page_token: nextPageToken value returned from a previous list call, indicating that the subsequent page of results should be returned. The list request must be otherwise identical to the one that resulted in this token.
    :type page_token: str

    """
    return web.Response(status=200)


async def classroom_courses_teachers_create(request: web.Request, course_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """classroom_courses_teachers_create

    Creates a teacher of a course. Domain administrators are permitted to [directly add](https://developers.google.com/classroom/guides/manage-users) users within their domain as teachers to courses within their domain. Non-admin users should send an Invitation instead. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to create teachers in this course or for access errors. * &#x60;NOT_FOUND&#x60; if the requested course ID does not exist. * &#x60;FAILED_PRECONDITION&#x60; if the requested user&#39;s account is disabled, for the following request errors: * CourseMemberLimitReached * CourseNotModifiable * CourseTeacherLimitReached * UserGroupsMembershipLimitReached * InactiveCourseOwner * &#x60;ALREADY_EXISTS&#x60; if the user is already a teacher or student in the course.

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = Teacher.from_dict(body)
    return web.Response(status=200)


async def classroom_courses_teachers_delete(request: web.Request, course_id, user_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """classroom_courses_teachers_delete

    Removes the specified teacher from the specified course. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to delete teachers of this course or for access errors. * &#x60;NOT_FOUND&#x60; if no teacher of this course has the requested ID or if the course does not exist. * &#x60;FAILED_PRECONDITION&#x60; if the requested ID belongs to the primary teacher of this course. * &#x60;FAILED_PRECONDITION&#x60; if the requested ID belongs to the owner of the course Drive folder. * &#x60;FAILED_PRECONDITION&#x60; if the course no longer has an active owner.

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param user_id: Identifier of the teacher to delete. The identifier can be one of the following: * the numeric identifier for the user * the email address of the user * the string literal &#x60;\&quot;me\&quot;&#x60;, indicating the requesting user
    :type user_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def classroom_courses_teachers_get(request: web.Request, course_id, user_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """classroom_courses_teachers_get

    Returns a teacher of a course. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to view teachers of this course or for access errors. * &#x60;NOT_FOUND&#x60; if no teacher of this course has the requested ID or if the course does not exist.

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param user_id: Identifier of the teacher to return. The identifier can be one of the following: * the numeric identifier for the user * the email address of the user * the string literal &#x60;\&quot;me\&quot;&#x60;, indicating the requesting user
    :type user_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def classroom_courses_teachers_list(request: web.Request, course_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """classroom_courses_teachers_list

    Returns a list of teachers of this course that the requester is permitted to view. This method returns the following error codes: * &#x60;NOT_FOUND&#x60; if the course does not exist. * &#x60;PERMISSION_DENIED&#x60; for access errors.

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param page_size: Maximum number of items to return. The default is 30 if unspecified or &#x60;0&#x60;. The server may return fewer than the specified number of results.
    :type page_size: int
    :param page_token: nextPageToken value returned from a previous list call, indicating that the subsequent page of results should be returned. The list request must be otherwise identical to the one that resulted in this token.
    :type page_token: str

    """
    return web.Response(status=200)


async def classroom_courses_topics_create(request: web.Request, course_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """classroom_courses_topics_create

    Creates a topic. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to access the requested course, create a topic in the requested course, or for access errors. * &#x60;INVALID_ARGUMENT&#x60; if the request is malformed. * &#x60;NOT_FOUND&#x60; if the requested course does not exist.

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = Topic.from_dict(body)
    return web.Response(status=200)


async def classroom_courses_topics_delete(request: web.Request, course_id, id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """classroom_courses_topics_delete

    Deletes a topic. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not allowed to delete the requested topic or for access errors. * &#x60;FAILED_PRECONDITION&#x60; if the requested topic has already been deleted. * &#x60;NOT_FOUND&#x60; if no course or topic exists with the requested ID.

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param id: Identifier of the topic to delete.
    :type id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def classroom_courses_topics_get(request: web.Request, course_id, id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """classroom_courses_topics_get

    Returns a topic. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to access the requested course or topic, or for access errors. * &#x60;INVALID_ARGUMENT&#x60; if the request is malformed. * &#x60;NOT_FOUND&#x60; if the requested course or topic does not exist.

    :param course_id: Identifier of the course.
    :type course_id: str
    :param id: Identifier of the topic.
    :type id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str

    """
    return web.Response(status=200)


async def classroom_courses_topics_list(request: web.Request, course_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, page_size=None, page_token=None) -> web.Response:
    """classroom_courses_topics_list

    Returns the list of topics that the requester is permitted to view. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to access the requested course or for access errors. * &#x60;INVALID_ARGUMENT&#x60; if the request is malformed. * &#x60;NOT_FOUND&#x60; if the requested course does not exist.

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param page_size: Maximum number of items to return. Zero or unspecified indicates that the server may assign a maximum. The server may return fewer than the specified number of results.
    :type page_size: int
    :param page_token: nextPageToken value returned from a previous list call, indicating that the subsequent page of results should be returned. The list request must be otherwise identical to the one that resulted in this token.
    :type page_token: str

    """
    return web.Response(status=200)


async def classroom_courses_topics_patch(request: web.Request, course_id, id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """classroom_courses_topics_patch

    Updates one or more fields of a topic. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting developer project did not create the corresponding topic or for access errors. * &#x60;INVALID_ARGUMENT&#x60; if the request is malformed. * &#x60;NOT_FOUND&#x60; if the requested course or topic does not exist

    :param course_id: Identifier of the course. This identifier can be either the Classroom-assigned identifier or an alias.
    :type course_id: str
    :param id: Identifier of the topic.
    :type id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param update_mask: Mask that identifies which fields on the topic to update. This field is required to do an update. The update fails if invalid fields are specified. If a field supports empty values, it can be cleared by specifying it in the update mask and not in the Topic object. If a field that does not support empty values is included in the update mask and not set in the Topic object, an &#x60;INVALID_ARGUMENT&#x60; error is returned. The following fields may be specified: * &#x60;name&#x60;
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = Topic.from_dict(body)
    return web.Response(status=200)


async def classroom_courses_update(request: web.Request, id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """classroom_courses_update

    Updates a course. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to modify the requested course or for access errors. * &#x60;NOT_FOUND&#x60; if no course exists with the requested ID. * &#x60;FAILED_PRECONDITION&#x60; for the following request errors: * CourseNotModifiable

    :param id: Identifier of the course to update. This identifier can be either the Classroom-assigned identifier or an alias.
    :type id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param body: 
    :type body: dict | bytes

    """
    body = Course.from_dict(body)
    return web.Response(status=200)
