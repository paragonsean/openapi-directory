from typing import List, Dict
from aiohttp import web

from openapi_server.models.guardian import Guardian
from openapi_server.models.guardian_invitation import GuardianInvitation
from openapi_server.models.list_guardian_invitations_response import ListGuardianInvitationsResponse
from openapi_server.models.list_guardians_response import ListGuardiansResponse
from openapi_server.models.user_profile import UserProfile
from openapi_server import util


async def classroom_user_profiles_get(request: web.Request, user_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """classroom_user_profiles_get

    Returns a user profile. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to access this user profile, if no profile exists with the requested ID, or for access errors.

    :param user_id: Identifier of the profile to return. The identifier can be one of the following: * the numeric identifier for the user * the email address of the user * the string literal &#x60;\&quot;me\&quot;&#x60;, indicating the requesting user
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


async def classroom_user_profiles_guardian_invitations_create(request: web.Request, student_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """classroom_user_profiles_guardian_invitations_create

    Creates a guardian invitation, and sends an email to the guardian asking them to confirm that they are the student&#39;s guardian. Once the guardian accepts the invitation, their &#x60;state&#x60; will change to &#x60;COMPLETED&#x60; and they will start receiving guardian notifications. A &#x60;Guardian&#x60; resource will also be created to represent the active guardian. The request object must have the &#x60;student_id&#x60; and &#x60;invited_email_address&#x60; fields set. Failing to set these fields, or setting any other fields in the request, will result in an error. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the current user does not have permission to manage guardians, if the guardian in question has already rejected too many requests for that student, if guardians are not enabled for the domain in question, or for other access errors. * &#x60;RESOURCE_EXHAUSTED&#x60; if the student or guardian has exceeded the guardian link limit. * &#x60;INVALID_ARGUMENT&#x60; if the guardian email address is not valid (for example, if it is too long), or if the format of the student ID provided cannot be recognized (it is not an email address, nor a &#x60;user_id&#x60; from this API). This error will also be returned if read-only fields are set, or if the &#x60;state&#x60; field is set to to a value other than &#x60;PENDING&#x60;. * &#x60;NOT_FOUND&#x60; if the student ID provided is a valid student ID, but Classroom has no record of that student. * &#x60;ALREADY_EXISTS&#x60; if there is already a pending guardian invitation for the student and &#x60;invited_email_address&#x60; provided, or if the provided &#x60;invited_email_address&#x60; matches the Google account of an existing &#x60;Guardian&#x60; for this user.

    :param student_id: ID of the student (in standard format)
    :type student_id: str
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
    body = GuardianInvitation.from_dict(body)
    return web.Response(status=200)


async def classroom_user_profiles_guardian_invitations_get(request: web.Request, student_id, invitation_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """classroom_user_profiles_guardian_invitations_get

    Returns a specific guardian invitation. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to view guardian invitations for the student identified by the &#x60;student_id&#x60;, if guardians are not enabled for the domain in question, or for other access errors. * &#x60;INVALID_ARGUMENT&#x60; if a &#x60;student_id&#x60; is specified, but its format cannot be recognized (it is not an email address, nor a &#x60;student_id&#x60; from the API, nor the literal string &#x60;me&#x60;). * &#x60;NOT_FOUND&#x60; if Classroom cannot find any record of the given student or &#x60;invitation_id&#x60;. May also be returned if the student exists, but the requesting user does not have access to see that student.

    :param student_id: The ID of the student whose guardian invitation is being requested.
    :type student_id: str
    :param invitation_id: The &#x60;id&#x60; field of the &#x60;GuardianInvitation&#x60; being requested.
    :type invitation_id: str
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


async def classroom_user_profiles_guardian_invitations_list(request: web.Request, student_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, invited_email_address=None, page_size=None, page_token=None, states=None) -> web.Response:
    """classroom_user_profiles_guardian_invitations_list

    Returns a list of guardian invitations that the requesting user is permitted to view, filtered by the parameters provided. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if a &#x60;student_id&#x60; is specified, and the requesting user is not permitted to view guardian invitations for that student, if &#x60;\&quot;-\&quot;&#x60; is specified as the &#x60;student_id&#x60; and the user is not a domain administrator, if guardians are not enabled for the domain in question, or for other access errors. * &#x60;INVALID_ARGUMENT&#x60; if a &#x60;student_id&#x60; is specified, but its format cannot be recognized (it is not an email address, nor a &#x60;student_id&#x60; from the API, nor the literal string &#x60;me&#x60;). May also be returned if an invalid &#x60;page_token&#x60; or &#x60;state&#x60; is provided. * &#x60;NOT_FOUND&#x60; if a &#x60;student_id&#x60; is specified, and its format can be recognized, but Classroom has no record of that student.

    :param student_id: The ID of the student whose guardian invitations are to be returned. The identifier can be one of the following: * the numeric identifier for the user * the email address of the user * the string literal &#x60;\&quot;me\&quot;&#x60;, indicating the requesting user * the string literal &#x60;\&quot;-\&quot;&#x60;, indicating that results should be returned for all students that the requesting user is permitted to view guardian invitations.
    :type student_id: str
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
    :param invited_email_address: If specified, only results with the specified &#x60;invited_email_address&#x60; are returned.
    :type invited_email_address: str
    :param page_size: Maximum number of items to return. Zero or unspecified indicates that the server may assign a maximum. The server may return fewer than the specified number of results.
    :type page_size: int
    :param page_token: nextPageToken value returned from a previous list call, indicating that the subsequent page of results should be returned. The list request must be otherwise identical to the one that resulted in this token.
    :type page_token: str
    :param states: If specified, only results with the specified &#x60;state&#x60; values are returned. Otherwise, results with a &#x60;state&#x60; of &#x60;PENDING&#x60; are returned.
    :type states: List[str]

    """
    return web.Response(status=200)


async def classroom_user_profiles_guardian_invitations_patch(request: web.Request, student_id, invitation_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, update_mask=None, body=None) -> web.Response:
    """classroom_user_profiles_guardian_invitations_patch

    Modifies a guardian invitation. Currently, the only valid modification is to change the &#x60;state&#x60; from &#x60;PENDING&#x60; to &#x60;COMPLETE&#x60;. This has the effect of withdrawing the invitation. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the current user does not have permission to manage guardians, if guardians are not enabled for the domain in question or for other access errors. * &#x60;FAILED_PRECONDITION&#x60; if the guardian link is not in the &#x60;PENDING&#x60; state. * &#x60;INVALID_ARGUMENT&#x60; if the format of the student ID provided cannot be recognized (it is not an email address, nor a &#x60;user_id&#x60; from this API), or if the passed &#x60;GuardianInvitation&#x60; has a &#x60;state&#x60; other than &#x60;COMPLETE&#x60;, or if it modifies fields other than &#x60;state&#x60;. * &#x60;NOT_FOUND&#x60; if the student ID provided is a valid student ID, but Classroom has no record of that student, or if the &#x60;id&#x60; field does not refer to a guardian invitation known to Classroom.

    :param student_id: The ID of the student whose guardian invitation is to be modified.
    :type student_id: str
    :param invitation_id: The &#x60;id&#x60; field of the &#x60;GuardianInvitation&#x60; to be modified.
    :type invitation_id: str
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
    :param update_mask: Mask that identifies which fields on the course to update. This field is required to do an update. The update fails if invalid fields are specified. The following fields are valid: * &#x60;state&#x60; When set in a query parameter, this field should be specified as &#x60;updateMask&#x3D;,,...&#x60;
    :type update_mask: str
    :param body: 
    :type body: dict | bytes

    """
    body = GuardianInvitation.from_dict(body)
    return web.Response(status=200)


async def classroom_user_profiles_guardians_delete(request: web.Request, student_id, guardian_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """classroom_user_profiles_guardians_delete

    Deletes a guardian. The guardian will no longer receive guardian notifications and the guardian will no longer be accessible via the API. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if no user that matches the provided &#x60;student_id&#x60; is visible to the requesting user, if the requesting user is not permitted to manage guardians for the student identified by the &#x60;student_id&#x60;, if guardians are not enabled for the domain in question, or for other access errors. * &#x60;INVALID_ARGUMENT&#x60; if a &#x60;student_id&#x60; is specified, but its format cannot be recognized (it is not an email address, nor a &#x60;student_id&#x60; from the API). * &#x60;NOT_FOUND&#x60; if the requesting user is permitted to modify guardians for the requested &#x60;student_id&#x60;, but no &#x60;Guardian&#x60; record exists for that student with the provided &#x60;guardian_id&#x60;.

    :param student_id: The student whose guardian is to be deleted. One of the following: * the numeric identifier for the user * the email address of the user * the string literal &#x60;\&quot;me\&quot;&#x60;, indicating the requesting user
    :type student_id: str
    :param guardian_id: The &#x60;id&#x60; field from a &#x60;Guardian&#x60;.
    :type guardian_id: str
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


async def classroom_user_profiles_guardians_get(request: web.Request, student_id, guardian_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None) -> web.Response:
    """classroom_user_profiles_guardians_get

    Returns a specific guardian. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if no user that matches the provided &#x60;student_id&#x60; is visible to the requesting user, if the requesting user is not permitted to view guardian information for the student identified by the &#x60;student_id&#x60;, if guardians are not enabled for the domain in question, or for other access errors. * &#x60;INVALID_ARGUMENT&#x60; if a &#x60;student_id&#x60; is specified, but its format cannot be recognized (it is not an email address, nor a &#x60;student_id&#x60; from the API, nor the literal string &#x60;me&#x60;). * &#x60;NOT_FOUND&#x60; if the requesting user is permitted to view guardians for the requested &#x60;student_id&#x60;, but no &#x60;Guardian&#x60; record exists for that student that matches the provided &#x60;guardian_id&#x60;.

    :param student_id: The student whose guardian is being requested. One of the following: * the numeric identifier for the user * the email address of the user * the string literal &#x60;\&quot;me\&quot;&#x60;, indicating the requesting user
    :type student_id: str
    :param guardian_id: The &#x60;id&#x60; field from a &#x60;Guardian&#x60;.
    :type guardian_id: str
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


async def classroom_user_profiles_guardians_list(request: web.Request, student_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, invited_email_address=None, page_size=None, page_token=None) -> web.Response:
    """classroom_user_profiles_guardians_list

    Returns a list of guardians that the requesting user is permitted to view, restricted to those that match the request. To list guardians for any student that the requesting user may view guardians for, use the literal character &#x60;-&#x60; for the student ID. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if a &#x60;student_id&#x60; is specified, and the requesting user is not permitted to view guardian information for that student, if &#x60;\&quot;-\&quot;&#x60; is specified as the &#x60;student_id&#x60; and the user is not a domain administrator, if guardians are not enabled for the domain in question, if the &#x60;invited_email_address&#x60; filter is set by a user who is not a domain administrator, or for other access errors. * &#x60;INVALID_ARGUMENT&#x60; if a &#x60;student_id&#x60; is specified, but its format cannot be recognized (it is not an email address, nor a &#x60;student_id&#x60; from the API, nor the literal string &#x60;me&#x60;). May also be returned if an invalid &#x60;page_token&#x60; is provided. * &#x60;NOT_FOUND&#x60; if a &#x60;student_id&#x60; is specified, and its format can be recognized, but Classroom has no record of that student.

    :param student_id: Filter results by the student who the guardian is linked to. The identifier can be one of the following: * the numeric identifier for the user * the email address of the user * the string literal &#x60;\&quot;me\&quot;&#x60;, indicating the requesting user * the string literal &#x60;\&quot;-\&quot;&#x60;, indicating that results should be returned for all students that the requesting user has access to view.
    :type student_id: str
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
    :param invited_email_address: Filter results by the email address that the original invitation was sent to, resulting in this guardian link. This filter can only be used by domain administrators.
    :type invited_email_address: str
    :param page_size: Maximum number of items to return. Zero or unspecified indicates that the server may assign a maximum. The server may return fewer than the specified number of results.
    :type page_size: int
    :param page_token: nextPageToken value returned from a previous list call, indicating that the subsequent page of results should be returned. The list request must be otherwise identical to the one that resulted in this token.
    :type page_token: str

    """
    return web.Response(status=200)
