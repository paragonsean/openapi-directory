# Signl4Api.TeamsMembershipsApi

All URIs are relative to *https://connect.signl4.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**teamsTeamIdMembershipsGet**](TeamsMembershipsApi.md#teamsTeamIdMembershipsGet) | **GET** /teams/{teamId}/memberships | Get all invites of a team.
[**teamsTeamIdMembershipsPost**](TeamsMembershipsApi.md#teamsTeamIdMembershipsPost) | **POST** /teams/{teamId}/memberships | Invite users to a team
[**teamsTeamIdMembershipsResendInviteMailPost**](TeamsMembershipsApi.md#teamsTeamIdMembershipsResendInviteMailPost) | **POST** /teams/{teamId}/memberships/resendInviteMail | Sends invite email again if an invite exists
[**teamsTeamIdMembershipsUserIdDelete**](TeamsMembershipsApi.md#teamsTeamIdMembershipsUserIdDelete) | **DELETE** /teams/{teamId}/memberships/{userId} | Removes a user or invitation from a team, and may delete the user if he is not in any team.
[**teamsTeamIdMembershipsUserIdPut**](TeamsMembershipsApi.md#teamsTeamIdMembershipsUserIdPut) | **PUT** /teams/{teamId}/memberships/{userId} | Update user&#39;s team membership.



## teamsTeamIdMembershipsGet

> [InvitedUserInfo] teamsTeamIdMembershipsGet(teamId)

Get all invites of a team.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.TeamsMembershipsApi();
let teamId = "teamId_example"; // String | Team ID of team you want to request.
apiInstance.teamsTeamIdMembershipsGet(teamId, (error, data, response) => {
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
 **teamId** | **String**| Team ID of team you want to request. | 

### Return type

[**[InvitedUserInfo]**](InvitedUserInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## teamsTeamIdMembershipsPost

> [UserInvitationResult] teamsTeamIdMembershipsPost(teamId, opts)

Invite users to a team

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.TeamsMembershipsApi();
let teamId = "teamId_example"; // String | Id of team the user should be invited to.
let opts = {
  'usersInvitation': new Signl4Api.UsersInvitation() // UsersInvitation | Information about user to invite and inviter id.
};
apiInstance.teamsTeamIdMembershipsPost(teamId, opts, (error, data, response) => {
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
 **teamId** | **String**| Id of team the user should be invited to. | 
 **usersInvitation** | [**UsersInvitation**](UsersInvitation.md)| Information about user to invite and inviter id. | [optional] 

### Return type

[**[UserInvitationResult]**](UserInvitationResult.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## teamsTeamIdMembershipsResendInviteMailPost

> String teamsTeamIdMembershipsResendInviteMailPost(teamId, opts)

Sends invite email again if an invite exists

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.TeamsMembershipsApi();
let teamId = "teamId_example"; // String | Team ID of team with invited user.
let opts = {
  'userInvitationInfo': new Signl4Api.UserInvitationInfo() // UserInvitationInfo | Information which user should be invited again.
};
apiInstance.teamsTeamIdMembershipsResendInviteMailPost(teamId, opts, (error, data, response) => {
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
 **teamId** | **String**| Team ID of team with invited user. | 
 **userInvitationInfo** | [**UserInvitationInfo**](UserInvitationInfo.md)| Information which user should be invited again. | [optional] 

### Return type

**String**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## teamsTeamIdMembershipsUserIdDelete

> String teamsTeamIdMembershipsUserIdDelete(teamId, userId, opts)

Removes a user or invitation from a team, and may delete the user if he is not in any team.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.TeamsMembershipsApi();
let teamId = "teamId_example"; // String | ID of the team the user should be deleted from
let userId = "userId_example"; // String | ID of the user that should be deleted
let opts = {
  'requesterUserId': "requesterUserId_example" // String | User ID of user which will remove the other user.
};
apiInstance.teamsTeamIdMembershipsUserIdDelete(teamId, userId, opts, (error, data, response) => {
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
 **teamId** | **String**| ID of the team the user should be deleted from | 
 **userId** | **String**| ID of the user that should be deleted | 
 **requesterUserId** | **String**| User ID of user which will remove the other user. | [optional] 

### Return type

**String**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## teamsTeamIdMembershipsUserIdPut

> UserInfo teamsTeamIdMembershipsUserIdPut(teamId, userId, opts)

Update user&#39;s team membership.

Updates the user&#39;s team membership. You can move the user to another team within the subscription  and/or change the user&#39;s role.

### Example

```javascript
import Signl4Api from 'signl4_api';
let defaultClient = Signl4Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Signl4Api.TeamsMembershipsApi();
let teamId = "teamId_example"; // String | Team the user you want to update belongs to at the moment.
let userId = "userId_example"; // String | User ID of user you want to update.
let opts = {
  'requesterUserId': "requesterUserId_example", // String | User ID of user which you want to change role with. This must be provided when using an api key. This user must have role administrator (for setting administrator role) or team administrator (for setting  rights.
  'userMembership': new Signl4Api.UserMembership() // UserMembership | Information about role id and target team id.
};
apiInstance.teamsTeamIdMembershipsUserIdPut(teamId, userId, opts, (error, data, response) => {
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
 **teamId** | **String**| Team the user you want to update belongs to at the moment. | 
 **userId** | **String**| User ID of user you want to update. | 
 **requesterUserId** | **String**| User ID of user which you want to change role with. This must be provided when using an api key. This user must have role administrator (for setting administrator role) or team administrator (for setting  rights. | [optional] 
 **userMembership** | [**UserMembership**](UserMembership.md)| Information about role id and target team id. | [optional] 

### Return type

[**UserInfo**](UserInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain

