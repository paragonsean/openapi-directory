# GoogleClassroomApi.UserProfilesApi

All URIs are relative to *https://classroom.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**classroomUserProfilesGet**](UserProfilesApi.md#classroomUserProfilesGet) | **GET** /v1/userProfiles/{userId} | 
[**classroomUserProfilesGuardianInvitationsCreate**](UserProfilesApi.md#classroomUserProfilesGuardianInvitationsCreate) | **POST** /v1/userProfiles/{studentId}/guardianInvitations | 
[**classroomUserProfilesGuardianInvitationsGet**](UserProfilesApi.md#classroomUserProfilesGuardianInvitationsGet) | **GET** /v1/userProfiles/{studentId}/guardianInvitations/{invitationId} | 
[**classroomUserProfilesGuardianInvitationsList**](UserProfilesApi.md#classroomUserProfilesGuardianInvitationsList) | **GET** /v1/userProfiles/{studentId}/guardianInvitations | 
[**classroomUserProfilesGuardianInvitationsPatch**](UserProfilesApi.md#classroomUserProfilesGuardianInvitationsPatch) | **PATCH** /v1/userProfiles/{studentId}/guardianInvitations/{invitationId} | 
[**classroomUserProfilesGuardiansDelete**](UserProfilesApi.md#classroomUserProfilesGuardiansDelete) | **DELETE** /v1/userProfiles/{studentId}/guardians/{guardianId} | 
[**classroomUserProfilesGuardiansGet**](UserProfilesApi.md#classroomUserProfilesGuardiansGet) | **GET** /v1/userProfiles/{studentId}/guardians/{guardianId} | 
[**classroomUserProfilesGuardiansList**](UserProfilesApi.md#classroomUserProfilesGuardiansList) | **GET** /v1/userProfiles/{studentId}/guardians | 



## classroomUserProfilesGet

> UserProfile classroomUserProfilesGet(userId, opts)



Returns a user profile. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to access this user profile, if no profile exists with the requested ID, or for access errors.

### Example

```javascript
import GoogleClassroomApi from 'google_classroom_api';
let defaultClient = GoogleClassroomApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleClassroomApi.UserProfilesApi();
let userId = "userId_example"; // String | Identifier of the profile to return. The identifier can be one of the following: * the numeric identifier for the user * the email address of the user * the string literal `\"me\"`, indicating the requesting user
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.classroomUserProfilesGet(userId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userId** | **String**| Identifier of the profile to return. The identifier can be one of the following: * the numeric identifier for the user * the email address of the user * the string literal &#x60;\&quot;me\&quot;&#x60;, indicating the requesting user | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

[**UserProfile**](UserProfile.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## classroomUserProfilesGuardianInvitationsCreate

> GuardianInvitation classroomUserProfilesGuardianInvitationsCreate(studentId, opts)



Creates a guardian invitation, and sends an email to the guardian asking them to confirm that they are the student&#39;s guardian. Once the guardian accepts the invitation, their &#x60;state&#x60; will change to &#x60;COMPLETED&#x60; and they will start receiving guardian notifications. A &#x60;Guardian&#x60; resource will also be created to represent the active guardian. The request object must have the &#x60;student_id&#x60; and &#x60;invited_email_address&#x60; fields set. Failing to set these fields, or setting any other fields in the request, will result in an error. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the current user does not have permission to manage guardians, if the guardian in question has already rejected too many requests for that student, if guardians are not enabled for the domain in question, or for other access errors. * &#x60;RESOURCE_EXHAUSTED&#x60; if the student or guardian has exceeded the guardian link limit. * &#x60;INVALID_ARGUMENT&#x60; if the guardian email address is not valid (for example, if it is too long), or if the format of the student ID provided cannot be recognized (it is not an email address, nor a &#x60;user_id&#x60; from this API). This error will also be returned if read-only fields are set, or if the &#x60;state&#x60; field is set to to a value other than &#x60;PENDING&#x60;. * &#x60;NOT_FOUND&#x60; if the student ID provided is a valid student ID, but Classroom has no record of that student. * &#x60;ALREADY_EXISTS&#x60; if there is already a pending guardian invitation for the student and &#x60;invited_email_address&#x60; provided, or if the provided &#x60;invited_email_address&#x60; matches the Google account of an existing &#x60;Guardian&#x60; for this user.

### Example

```javascript
import GoogleClassroomApi from 'google_classroom_api';
let defaultClient = GoogleClassroomApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleClassroomApi.UserProfilesApi();
let studentId = "studentId_example"; // String | ID of the student (in standard format)
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'guardianInvitation': new GoogleClassroomApi.GuardianInvitation() // GuardianInvitation | 
};
apiInstance.classroomUserProfilesGuardianInvitationsCreate(studentId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studentId** | **String**| ID of the student (in standard format) | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **guardianInvitation** | [**GuardianInvitation**](GuardianInvitation.md)|  | [optional] 

### Return type

[**GuardianInvitation**](GuardianInvitation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## classroomUserProfilesGuardianInvitationsGet

> GuardianInvitation classroomUserProfilesGuardianInvitationsGet(studentId, invitationId, opts)



Returns a specific guardian invitation. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the requesting user is not permitted to view guardian invitations for the student identified by the &#x60;student_id&#x60;, if guardians are not enabled for the domain in question, or for other access errors. * &#x60;INVALID_ARGUMENT&#x60; if a &#x60;student_id&#x60; is specified, but its format cannot be recognized (it is not an email address, nor a &#x60;student_id&#x60; from the API, nor the literal string &#x60;me&#x60;). * &#x60;NOT_FOUND&#x60; if Classroom cannot find any record of the given student or &#x60;invitation_id&#x60;. May also be returned if the student exists, but the requesting user does not have access to see that student.

### Example

```javascript
import GoogleClassroomApi from 'google_classroom_api';
let defaultClient = GoogleClassroomApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleClassroomApi.UserProfilesApi();
let studentId = "studentId_example"; // String | The ID of the student whose guardian invitation is being requested.
let invitationId = "invitationId_example"; // String | The `id` field of the `GuardianInvitation` being requested.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.classroomUserProfilesGuardianInvitationsGet(studentId, invitationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studentId** | **String**| The ID of the student whose guardian invitation is being requested. | 
 **invitationId** | **String**| The &#x60;id&#x60; field of the &#x60;GuardianInvitation&#x60; being requested. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

[**GuardianInvitation**](GuardianInvitation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## classroomUserProfilesGuardianInvitationsList

> ListGuardianInvitationsResponse classroomUserProfilesGuardianInvitationsList(studentId, opts)



Returns a list of guardian invitations that the requesting user is permitted to view, filtered by the parameters provided. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if a &#x60;student_id&#x60; is specified, and the requesting user is not permitted to view guardian invitations for that student, if &#x60;\&quot;-\&quot;&#x60; is specified as the &#x60;student_id&#x60; and the user is not a domain administrator, if guardians are not enabled for the domain in question, or for other access errors. * &#x60;INVALID_ARGUMENT&#x60; if a &#x60;student_id&#x60; is specified, but its format cannot be recognized (it is not an email address, nor a &#x60;student_id&#x60; from the API, nor the literal string &#x60;me&#x60;). May also be returned if an invalid &#x60;page_token&#x60; or &#x60;state&#x60; is provided. * &#x60;NOT_FOUND&#x60; if a &#x60;student_id&#x60; is specified, and its format can be recognized, but Classroom has no record of that student.

### Example

```javascript
import GoogleClassroomApi from 'google_classroom_api';
let defaultClient = GoogleClassroomApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleClassroomApi.UserProfilesApi();
let studentId = "studentId_example"; // String | The ID of the student whose guardian invitations are to be returned. The identifier can be one of the following: * the numeric identifier for the user * the email address of the user * the string literal `\"me\"`, indicating the requesting user * the string literal `\"-\"`, indicating that results should be returned for all students that the requesting user is permitted to view guardian invitations.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'invitedEmailAddress': "invitedEmailAddress_example", // String | If specified, only results with the specified `invited_email_address` are returned.
  'pageSize': 56, // Number | Maximum number of items to return. Zero or unspecified indicates that the server may assign a maximum. The server may return fewer than the specified number of results.
  'pageToken': "pageToken_example", // String | nextPageToken value returned from a previous list call, indicating that the subsequent page of results should be returned. The list request must be otherwise identical to the one that resulted in this token.
  'states': ["null"] // [String] | If specified, only results with the specified `state` values are returned. Otherwise, results with a `state` of `PENDING` are returned.
};
apiInstance.classroomUserProfilesGuardianInvitationsList(studentId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studentId** | **String**| The ID of the student whose guardian invitations are to be returned. The identifier can be one of the following: * the numeric identifier for the user * the email address of the user * the string literal &#x60;\&quot;me\&quot;&#x60;, indicating the requesting user * the string literal &#x60;\&quot;-\&quot;&#x60;, indicating that results should be returned for all students that the requesting user is permitted to view guardian invitations. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **invitedEmailAddress** | **String**| If specified, only results with the specified &#x60;invited_email_address&#x60; are returned. | [optional] 
 **pageSize** | **Number**| Maximum number of items to return. Zero or unspecified indicates that the server may assign a maximum. The server may return fewer than the specified number of results. | [optional] 
 **pageToken** | **String**| nextPageToken value returned from a previous list call, indicating that the subsequent page of results should be returned. The list request must be otherwise identical to the one that resulted in this token. | [optional] 
 **states** | [**[String]**](String.md)| If specified, only results with the specified &#x60;state&#x60; values are returned. Otherwise, results with a &#x60;state&#x60; of &#x60;PENDING&#x60; are returned. | [optional] 

### Return type

[**ListGuardianInvitationsResponse**](ListGuardianInvitationsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## classroomUserProfilesGuardianInvitationsPatch

> GuardianInvitation classroomUserProfilesGuardianInvitationsPatch(studentId, invitationId, opts)



Modifies a guardian invitation. Currently, the only valid modification is to change the &#x60;state&#x60; from &#x60;PENDING&#x60; to &#x60;COMPLETE&#x60;. This has the effect of withdrawing the invitation. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if the current user does not have permission to manage guardians, if guardians are not enabled for the domain in question or for other access errors. * &#x60;FAILED_PRECONDITION&#x60; if the guardian link is not in the &#x60;PENDING&#x60; state. * &#x60;INVALID_ARGUMENT&#x60; if the format of the student ID provided cannot be recognized (it is not an email address, nor a &#x60;user_id&#x60; from this API), or if the passed &#x60;GuardianInvitation&#x60; has a &#x60;state&#x60; other than &#x60;COMPLETE&#x60;, or if it modifies fields other than &#x60;state&#x60;. * &#x60;NOT_FOUND&#x60; if the student ID provided is a valid student ID, but Classroom has no record of that student, or if the &#x60;id&#x60; field does not refer to a guardian invitation known to Classroom.

### Example

```javascript
import GoogleClassroomApi from 'google_classroom_api';
let defaultClient = GoogleClassroomApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleClassroomApi.UserProfilesApi();
let studentId = "studentId_example"; // String | The ID of the student whose guardian invitation is to be modified.
let invitationId = "invitationId_example"; // String | The `id` field of the `GuardianInvitation` to be modified.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'updateMask': "updateMask_example", // String | Mask that identifies which fields on the course to update. This field is required to do an update. The update fails if invalid fields are specified. The following fields are valid: * `state` When set in a query parameter, this field should be specified as `updateMask=,,...`
  'guardianInvitation': new GoogleClassroomApi.GuardianInvitation() // GuardianInvitation | 
};
apiInstance.classroomUserProfilesGuardianInvitationsPatch(studentId, invitationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studentId** | **String**| The ID of the student whose guardian invitation is to be modified. | 
 **invitationId** | **String**| The &#x60;id&#x60; field of the &#x60;GuardianInvitation&#x60; to be modified. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **updateMask** | **String**| Mask that identifies which fields on the course to update. This field is required to do an update. The update fails if invalid fields are specified. The following fields are valid: * &#x60;state&#x60; When set in a query parameter, this field should be specified as &#x60;updateMask&#x3D;,,...&#x60; | [optional] 
 **guardianInvitation** | [**GuardianInvitation**](GuardianInvitation.md)|  | [optional] 

### Return type

[**GuardianInvitation**](GuardianInvitation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## classroomUserProfilesGuardiansDelete

> Object classroomUserProfilesGuardiansDelete(studentId, guardianId, opts)



Deletes a guardian. The guardian will no longer receive guardian notifications and the guardian will no longer be accessible via the API. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if no user that matches the provided &#x60;student_id&#x60; is visible to the requesting user, if the requesting user is not permitted to manage guardians for the student identified by the &#x60;student_id&#x60;, if guardians are not enabled for the domain in question, or for other access errors. * &#x60;INVALID_ARGUMENT&#x60; if a &#x60;student_id&#x60; is specified, but its format cannot be recognized (it is not an email address, nor a &#x60;student_id&#x60; from the API). * &#x60;NOT_FOUND&#x60; if the requesting user is permitted to modify guardians for the requested &#x60;student_id&#x60;, but no &#x60;Guardian&#x60; record exists for that student with the provided &#x60;guardian_id&#x60;.

### Example

```javascript
import GoogleClassroomApi from 'google_classroom_api';
let defaultClient = GoogleClassroomApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleClassroomApi.UserProfilesApi();
let studentId = "studentId_example"; // String | The student whose guardian is to be deleted. One of the following: * the numeric identifier for the user * the email address of the user * the string literal `\"me\"`, indicating the requesting user
let guardianId = "guardianId_example"; // String | The `id` field from a `Guardian`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.classroomUserProfilesGuardiansDelete(studentId, guardianId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studentId** | **String**| The student whose guardian is to be deleted. One of the following: * the numeric identifier for the user * the email address of the user * the string literal &#x60;\&quot;me\&quot;&#x60;, indicating the requesting user | 
 **guardianId** | **String**| The &#x60;id&#x60; field from a &#x60;Guardian&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## classroomUserProfilesGuardiansGet

> Guardian classroomUserProfilesGuardiansGet(studentId, guardianId, opts)



Returns a specific guardian. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if no user that matches the provided &#x60;student_id&#x60; is visible to the requesting user, if the requesting user is not permitted to view guardian information for the student identified by the &#x60;student_id&#x60;, if guardians are not enabled for the domain in question, or for other access errors. * &#x60;INVALID_ARGUMENT&#x60; if a &#x60;student_id&#x60; is specified, but its format cannot be recognized (it is not an email address, nor a &#x60;student_id&#x60; from the API, nor the literal string &#x60;me&#x60;). * &#x60;NOT_FOUND&#x60; if the requesting user is permitted to view guardians for the requested &#x60;student_id&#x60;, but no &#x60;Guardian&#x60; record exists for that student that matches the provided &#x60;guardian_id&#x60;.

### Example

```javascript
import GoogleClassroomApi from 'google_classroom_api';
let defaultClient = GoogleClassroomApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleClassroomApi.UserProfilesApi();
let studentId = "studentId_example"; // String | The student whose guardian is being requested. One of the following: * the numeric identifier for the user * the email address of the user * the string literal `\"me\"`, indicating the requesting user
let guardianId = "guardianId_example"; // String | The `id` field from a `Guardian`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.classroomUserProfilesGuardiansGet(studentId, guardianId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studentId** | **String**| The student whose guardian is being requested. One of the following: * the numeric identifier for the user * the email address of the user * the string literal &#x60;\&quot;me\&quot;&#x60;, indicating the requesting user | 
 **guardianId** | **String**| The &#x60;id&#x60; field from a &#x60;Guardian&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

[**Guardian**](Guardian.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## classroomUserProfilesGuardiansList

> ListGuardiansResponse classroomUserProfilesGuardiansList(studentId, opts)



Returns a list of guardians that the requesting user is permitted to view, restricted to those that match the request. To list guardians for any student that the requesting user may view guardians for, use the literal character &#x60;-&#x60; for the student ID. This method returns the following error codes: * &#x60;PERMISSION_DENIED&#x60; if a &#x60;student_id&#x60; is specified, and the requesting user is not permitted to view guardian information for that student, if &#x60;\&quot;-\&quot;&#x60; is specified as the &#x60;student_id&#x60; and the user is not a domain administrator, if guardians are not enabled for the domain in question, if the &#x60;invited_email_address&#x60; filter is set by a user who is not a domain administrator, or for other access errors. * &#x60;INVALID_ARGUMENT&#x60; if a &#x60;student_id&#x60; is specified, but its format cannot be recognized (it is not an email address, nor a &#x60;student_id&#x60; from the API, nor the literal string &#x60;me&#x60;). May also be returned if an invalid &#x60;page_token&#x60; is provided. * &#x60;NOT_FOUND&#x60; if a &#x60;student_id&#x60; is specified, and its format can be recognized, but Classroom has no record of that student.

### Example

```javascript
import GoogleClassroomApi from 'google_classroom_api';
let defaultClient = GoogleClassroomApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleClassroomApi.UserProfilesApi();
let studentId = "studentId_example"; // String | Filter results by the student who the guardian is linked to. The identifier can be one of the following: * the numeric identifier for the user * the email address of the user * the string literal `\"me\"`, indicating the requesting user * the string literal `\"-\"`, indicating that results should be returned for all students that the requesting user has access to view.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'invitedEmailAddress': "invitedEmailAddress_example", // String | Filter results by the email address that the original invitation was sent to, resulting in this guardian link. This filter can only be used by domain administrators.
  'pageSize': 56, // Number | Maximum number of items to return. Zero or unspecified indicates that the server may assign a maximum. The server may return fewer than the specified number of results.
  'pageToken': "pageToken_example" // String | nextPageToken value returned from a previous list call, indicating that the subsequent page of results should be returned. The list request must be otherwise identical to the one that resulted in this token.
};
apiInstance.classroomUserProfilesGuardiansList(studentId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studentId** | **String**| Filter results by the student who the guardian is linked to. The identifier can be one of the following: * the numeric identifier for the user * the email address of the user * the string literal &#x60;\&quot;me\&quot;&#x60;, indicating the requesting user * the string literal &#x60;\&quot;-\&quot;&#x60;, indicating that results should be returned for all students that the requesting user has access to view. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **invitedEmailAddress** | **String**| Filter results by the email address that the original invitation was sent to, resulting in this guardian link. This filter can only be used by domain administrators. | [optional] 
 **pageSize** | **Number**| Maximum number of items to return. Zero or unspecified indicates that the server may assign a maximum. The server may return fewer than the specified number of results. | [optional] 
 **pageToken** | **String**| nextPageToken value returned from a previous list call, indicating that the subsequent page of results should be returned. The list request must be otherwise identical to the one that resulted in this token. | [optional] 

### Return type

[**ListGuardiansResponse**](ListGuardiansResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

