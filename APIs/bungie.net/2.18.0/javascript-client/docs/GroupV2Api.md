# BungieNetApi.GroupV2Api

All URIs are relative to *https://www.bungie.net/Platform*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groupV2AbdicateFoundership**](GroupV2Api.md#groupV2AbdicateFoundership) | **POST** /GroupV2/{groupId}/Admin/AbdicateFoundership/{membershipType}/{founderIdNew}/ | 
[**groupV2AddOptionalConversation**](GroupV2Api.md#groupV2AddOptionalConversation) | **POST** /GroupV2/{groupId}/OptionalConversations/Add/ | 
[**groupV2ApproveAllPending**](GroupV2Api.md#groupV2ApproveAllPending) | **POST** /GroupV2/{groupId}/Members/ApproveAll/ | 
[**groupV2ApprovePending**](GroupV2Api.md#groupV2ApprovePending) | **POST** /GroupV2/{groupId}/Members/Approve/{membershipType}/{membershipId}/ | 
[**groupV2ApprovePendingForList**](GroupV2Api.md#groupV2ApprovePendingForList) | **POST** /GroupV2/{groupId}/Members/ApproveList/ | 
[**groupV2BanMember**](GroupV2Api.md#groupV2BanMember) | **POST** /GroupV2/{groupId}/Members/{membershipType}/{membershipId}/Ban/ | 
[**groupV2DenyAllPending**](GroupV2Api.md#groupV2DenyAllPending) | **POST** /GroupV2/{groupId}/Members/DenyAll/ | 
[**groupV2DenyPendingForList**](GroupV2Api.md#groupV2DenyPendingForList) | **POST** /GroupV2/{groupId}/Members/DenyList/ | 
[**groupV2EditClanBanner**](GroupV2Api.md#groupV2EditClanBanner) | **POST** /GroupV2/{groupId}/EditClanBanner/ | 
[**groupV2EditFounderOptions**](GroupV2Api.md#groupV2EditFounderOptions) | **POST** /GroupV2/{groupId}/EditFounderOptions/ | 
[**groupV2EditGroup**](GroupV2Api.md#groupV2EditGroup) | **POST** /GroupV2/{groupId}/Edit/ | 
[**groupV2EditGroupMembership**](GroupV2Api.md#groupV2EditGroupMembership) | **POST** /GroupV2/{groupId}/Members/{membershipType}/{membershipId}/SetMembershipType/{memberType}/ | 
[**groupV2EditOptionalConversation**](GroupV2Api.md#groupV2EditOptionalConversation) | **POST** /GroupV2/{groupId}/OptionalConversations/Edit/{conversationId}/ | 
[**groupV2GetAdminsAndFounderOfGroup**](GroupV2Api.md#groupV2GetAdminsAndFounderOfGroup) | **GET** /GroupV2/{groupId}/AdminsAndFounder/ | 
[**groupV2GetAvailableAvatars**](GroupV2Api.md#groupV2GetAvailableAvatars) | **GET** /GroupV2/GetAvailableAvatars/ | 
[**groupV2GetAvailableThemes**](GroupV2Api.md#groupV2GetAvailableThemes) | **GET** /GroupV2/GetAvailableThemes/ | 
[**groupV2GetBannedMembersOfGroup**](GroupV2Api.md#groupV2GetBannedMembersOfGroup) | **GET** /GroupV2/{groupId}/Banned/ | 
[**groupV2GetGroup**](GroupV2Api.md#groupV2GetGroup) | **GET** /GroupV2/{groupId}/ | 
[**groupV2GetGroupByName**](GroupV2Api.md#groupV2GetGroupByName) | **GET** /GroupV2/Name/{groupName}/{groupType}/ | 
[**groupV2GetGroupByNameV2**](GroupV2Api.md#groupV2GetGroupByNameV2) | **POST** /GroupV2/NameV2/ | 
[**groupV2GetGroupOptionalConversations**](GroupV2Api.md#groupV2GetGroupOptionalConversations) | **GET** /GroupV2/{groupId}/OptionalConversations/ | 
[**groupV2GetGroupsForMember**](GroupV2Api.md#groupV2GetGroupsForMember) | **GET** /GroupV2/User/{membershipType}/{membershipId}/{filter}/{groupType}/ | 
[**groupV2GetInvitedIndividuals**](GroupV2Api.md#groupV2GetInvitedIndividuals) | **GET** /GroupV2/{groupId}/Members/InvitedIndividuals/ | 
[**groupV2GetMembersOfGroup**](GroupV2Api.md#groupV2GetMembersOfGroup) | **GET** /GroupV2/{groupId}/Members/ | 
[**groupV2GetPendingMemberships**](GroupV2Api.md#groupV2GetPendingMemberships) | **GET** /GroupV2/{groupId}/Members/Pending/ | 
[**groupV2GetPotentialGroupsForMember**](GroupV2Api.md#groupV2GetPotentialGroupsForMember) | **GET** /GroupV2/User/Potential/{membershipType}/{membershipId}/{filter}/{groupType}/ | 
[**groupV2GetRecommendedGroups**](GroupV2Api.md#groupV2GetRecommendedGroups) | **POST** /GroupV2/Recommended/{groupType}/{createDateRange}/ | 
[**groupV2GetUserClanInviteSetting**](GroupV2Api.md#groupV2GetUserClanInviteSetting) | **GET** /GroupV2/GetUserClanInviteSetting/{mType}/ | 
[**groupV2GroupSearch**](GroupV2Api.md#groupV2GroupSearch) | **POST** /GroupV2/Search/ | 
[**groupV2IndividualGroupInvite**](GroupV2Api.md#groupV2IndividualGroupInvite) | **POST** /GroupV2/{groupId}/Members/IndividualInvite/{membershipType}/{membershipId}/ | 
[**groupV2IndividualGroupInviteCancel**](GroupV2Api.md#groupV2IndividualGroupInviteCancel) | **POST** /GroupV2/{groupId}/Members/IndividualInviteCancel/{membershipType}/{membershipId}/ | 
[**groupV2KickMember**](GroupV2Api.md#groupV2KickMember) | **POST** /GroupV2/{groupId}/Members/{membershipType}/{membershipId}/Kick/ | 
[**groupV2RecoverGroupForFounder**](GroupV2Api.md#groupV2RecoverGroupForFounder) | **GET** /GroupV2/Recover/{membershipType}/{membershipId}/{groupType}/ | 
[**groupV2UnbanMember**](GroupV2Api.md#groupV2UnbanMember) | **POST** /GroupV2/{groupId}/Members/{membershipType}/{membershipId}/Unban/ | 



## groupV2AbdicateFoundership

> GroupV2GetUserClanInviteSetting200Response groupV2AbdicateFoundership(founderIdNew, groupId, membershipType)



An administrative method to allow the founder of a group or clan to give up their position to another admin permanently.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.GroupV2Api();
let founderIdNew = 789; // Number | The new founder for this group. Must already be a group admin.
let groupId = 789; // Number | The target group id.
let membershipType = 56; // Number | Membership type of the provided founderIdNew.
apiInstance.groupV2AbdicateFoundership(founderIdNew, groupId, membershipType, (error, data, response) => {
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
 **founderIdNew** | **Number**| The new founder for this group. Must already be a group admin. | 
 **groupId** | **Number**| The target group id. | 
 **membershipType** | **Number**| Membership type of the provided founderIdNew. | 

### Return type

[**GroupV2GetUserClanInviteSetting200Response**](GroupV2GetUserClanInviteSetting200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2AddOptionalConversation

> ForumGetTopicForContent200Response groupV2AddOptionalConversation(groupId)



Add a new optional conversation/chat channel. Requires admin permissions to the group.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.GroupV2Api();
let groupId = 789; // Number | Group ID of the group to edit.
apiInstance.groupV2AddOptionalConversation(groupId, (error, data, response) => {
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
 **groupId** | **Number**| Group ID of the group to edit. | 

### Return type

[**ForumGetTopicForContent200Response**](ForumGetTopicForContent200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2ApproveAllPending

> GroupV2ApproveAllPending200Response groupV2ApproveAllPending(groupId)



Approve all of the pending users for the given group.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.GroupV2Api();
let groupId = 789; // Number | ID of the group.
apiInstance.groupV2ApproveAllPending(groupId, (error, data, response) => {
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
 **groupId** | **Number**| ID of the group. | 

### Return type

[**GroupV2ApproveAllPending200Response**](GroupV2ApproveAllPending200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2ApprovePending

> GroupV2GetUserClanInviteSetting200Response groupV2ApprovePending(groupId, membershipId, membershipType)



Approve the given membershipId to join the group/clan as long as they have applied.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.GroupV2Api();
let groupId = 789; // Number | ID of the group.
let membershipId = 789; // Number | The membership id being approved.
let membershipType = 56; // Number | Membership type of the supplied membership ID.
apiInstance.groupV2ApprovePending(groupId, membershipId, membershipType, (error, data, response) => {
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
 **groupId** | **Number**| ID of the group. | 
 **membershipId** | **Number**| The membership id being approved. | 
 **membershipType** | **Number**| Membership type of the supplied membership ID. | 

### Return type

[**GroupV2GetUserClanInviteSetting200Response**](GroupV2GetUserClanInviteSetting200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2ApprovePendingForList

> GroupV2ApproveAllPending200Response groupV2ApprovePendingForList(groupId)



Approve all of the pending users for the given group.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.GroupV2Api();
let groupId = 789; // Number | ID of the group.
apiInstance.groupV2ApprovePendingForList(groupId, (error, data, response) => {
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
 **groupId** | **Number**| ID of the group. | 

### Return type

[**GroupV2ApproveAllPending200Response**](GroupV2ApproveAllPending200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2BanMember

> Destiny2EquipItem200Response groupV2BanMember(groupId, membershipId, membershipType)



Bans the requested member from the requested group for the specified period of time.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.GroupV2Api();
let groupId = 789; // Number | Group ID that has the member to ban.
let membershipId = 789; // Number | Membership ID of the member to ban from the group.
let membershipType = 56; // Number | Membership type of the provided membership ID.
apiInstance.groupV2BanMember(groupId, membershipId, membershipType, (error, data, response) => {
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
 **groupId** | **Number**| Group ID that has the member to ban. | 
 **membershipId** | **Number**| Membership ID of the member to ban from the group. | 
 **membershipType** | **Number**| Membership type of the provided membership ID. | 

### Return type

[**Destiny2EquipItem200Response**](Destiny2EquipItem200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2DenyAllPending

> GroupV2ApproveAllPending200Response groupV2DenyAllPending(groupId)



Deny all of the pending users for the given group.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.GroupV2Api();
let groupId = 789; // Number | ID of the group.
apiInstance.groupV2DenyAllPending(groupId, (error, data, response) => {
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
 **groupId** | **Number**| ID of the group. | 

### Return type

[**GroupV2ApproveAllPending200Response**](GroupV2ApproveAllPending200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2DenyPendingForList

> GroupV2ApproveAllPending200Response groupV2DenyPendingForList(groupId)



Deny all of the pending users for the given group that match the passed-in .

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.GroupV2Api();
let groupId = 789; // Number | ID of the group.
apiInstance.groupV2DenyPendingForList(groupId, (error, data, response) => {
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
 **groupId** | **Number**| ID of the group. | 

### Return type

[**GroupV2ApproveAllPending200Response**](GroupV2ApproveAllPending200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2EditClanBanner

> Destiny2EquipItem200Response groupV2EditClanBanner(groupId)



Edit an existing group&#39;s clan banner. You must have suitable permissions in the group to perform this operation. All fields are required.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.GroupV2Api();
let groupId = 789; // Number | Group ID of the group to edit.
apiInstance.groupV2EditClanBanner(groupId, (error, data, response) => {
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
 **groupId** | **Number**| Group ID of the group to edit. | 

### Return type

[**Destiny2EquipItem200Response**](Destiny2EquipItem200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2EditFounderOptions

> Destiny2EquipItem200Response groupV2EditFounderOptions(groupId)



Edit group options only available to a founder. You must have suitable permissions in the group to perform this operation.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.GroupV2Api();
let groupId = 789; // Number | Group ID of the group to edit.
apiInstance.groupV2EditFounderOptions(groupId, (error, data, response) => {
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
 **groupId** | **Number**| Group ID of the group to edit. | 

### Return type

[**Destiny2EquipItem200Response**](Destiny2EquipItem200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2EditGroup

> Destiny2EquipItem200Response groupV2EditGroup(groupId)



Edit an existing group. You must have suitable permissions in the group to perform this operation. This latest revision will only edit the fields you pass in - pass null for properties you want to leave unaltered.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.GroupV2Api();
let groupId = 789; // Number | Group ID of the group to edit.
apiInstance.groupV2EditGroup(groupId, (error, data, response) => {
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
 **groupId** | **Number**| Group ID of the group to edit. | 

### Return type

[**Destiny2EquipItem200Response**](Destiny2EquipItem200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2EditGroupMembership

> Destiny2EquipItem200Response groupV2EditGroupMembership(groupId, membershipId, membershipType, memberType)



Edit the membership type of a given member. You must have suitable permissions in the group to perform this operation.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.GroupV2Api();
let groupId = 789; // Number | ID of the group to which the member belongs.
let membershipId = 789; // Number | Membership ID to modify.
let membershipType = 56; // Number | Membership type of the provide membership ID.
let memberType = 56; // Number | New membertype for the specified member.
apiInstance.groupV2EditGroupMembership(groupId, membershipId, membershipType, memberType, (error, data, response) => {
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
 **groupId** | **Number**| ID of the group to which the member belongs. | 
 **membershipId** | **Number**| Membership ID to modify. | 
 **membershipType** | **Number**| Membership type of the provide membership ID. | 
 **memberType** | **Number**| New membertype for the specified member. | 

### Return type

[**Destiny2EquipItem200Response**](Destiny2EquipItem200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2EditOptionalConversation

> ForumGetTopicForContent200Response groupV2EditOptionalConversation(conversationId, groupId)



Edit the settings of an optional conversation/chat channel. Requires admin permissions to the group.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.GroupV2Api();
let conversationId = 789; // Number | Conversation Id of the channel being edited.
let groupId = 789; // Number | Group ID of the group to edit.
apiInstance.groupV2EditOptionalConversation(conversationId, groupId, (error, data, response) => {
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
 **conversationId** | **Number**| Conversation Id of the channel being edited. | 
 **groupId** | **Number**| Group ID of the group to edit. | 

### Return type

[**ForumGetTopicForContent200Response**](ForumGetTopicForContent200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2GetAdminsAndFounderOfGroup

> GroupV2GetAdminsAndFounderOfGroup200Response groupV2GetAdminsAndFounderOfGroup(currentpage, groupId)



Get the list of members in a given group who are of admin level or higher.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.GroupV2Api();
let currentpage = 56; // Number | Page number (starting with 1). Each page has a fixed size of 50 items per page.
let groupId = 789; // Number | The ID of the group.
apiInstance.groupV2GetAdminsAndFounderOfGroup(currentpage, groupId, (error, data, response) => {
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
 **currentpage** | **Number**| Page number (starting with 1). Each page has a fixed size of 50 items per page. | 
 **groupId** | **Number**| The ID of the group. | 

### Return type

[**GroupV2GetAdminsAndFounderOfGroup200Response**](GroupV2GetAdminsAndFounderOfGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2GetAvailableAvatars

> GetAvailableLocales200Response groupV2GetAvailableAvatars()



Returns a list of all available group avatars for the signed-in user.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.GroupV2Api();
apiInstance.groupV2GetAvailableAvatars((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAvailableLocales200Response**](GetAvailableLocales200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2GetAvailableThemes

> GroupV2GetAvailableThemes200Response groupV2GetAvailableThemes()



Returns a list of all available group themes.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.GroupV2Api();
apiInstance.groupV2GetAvailableThemes((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GroupV2GetAvailableThemes200Response**](GroupV2GetAvailableThemes200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2GetBannedMembersOfGroup

> GroupV2GetBannedMembersOfGroup200Response groupV2GetBannedMembersOfGroup(currentpage, groupId)



Get the list of banned members in a given group. Only accessible to group Admins and above. Not applicable to all groups. Check group features.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.GroupV2Api();
let currentpage = 56; // Number | Page number (starting with 1). Each page has a fixed size of 50 entries.
let groupId = 789; // Number | Group ID whose banned members you are fetching
apiInstance.groupV2GetBannedMembersOfGroup(currentpage, groupId, (error, data, response) => {
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
 **currentpage** | **Number**| Page number (starting with 1). Each page has a fixed size of 50 entries. | 
 **groupId** | **Number**| Group ID whose banned members you are fetching | 

### Return type

[**GroupV2GetBannedMembersOfGroup200Response**](GroupV2GetBannedMembersOfGroup200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2GetGroup

> GroupV2GetGroupByName200Response groupV2GetGroup(groupId)



Get information about a specific group of the given ID.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.GroupV2Api();
let groupId = 789; // Number | Requested group's id.
apiInstance.groupV2GetGroup(groupId, (error, data, response) => {
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
 **groupId** | **Number**| Requested group&#39;s id. | 

### Return type

[**GroupV2GetGroupByName200Response**](GroupV2GetGroupByName200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2GetGroupByName

> GroupV2GetGroupByName200Response groupV2GetGroupByName(groupName, groupType)



Get information about a specific group with the given name and type.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.GroupV2Api();
let groupName = "groupName_example"; // String | Exact name of the group to find.
let groupType = 56; // Number | Type of group to find.
apiInstance.groupV2GetGroupByName(groupName, groupType, (error, data, response) => {
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
 **groupName** | **String**| Exact name of the group to find. | 
 **groupType** | **Number**| Type of group to find. | 

### Return type

[**GroupV2GetGroupByName200Response**](GroupV2GetGroupByName200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2GetGroupByNameV2

> GroupV2GetGroupByName200Response groupV2GetGroupByNameV2()



Get information about a specific group with the given name and type. The POST version.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.GroupV2Api();
apiInstance.groupV2GetGroupByNameV2((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GroupV2GetGroupByName200Response**](GroupV2GetGroupByName200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2GetGroupOptionalConversations

> GroupV2GetGroupOptionalConversations200Response groupV2GetGroupOptionalConversations(groupId)



Gets a list of available optional conversation channels and their settings.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.GroupV2Api();
let groupId = 789; // Number | Requested group's id.
apiInstance.groupV2GetGroupOptionalConversations(groupId, (error, data, response) => {
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
 **groupId** | **Number**| Requested group&#39;s id. | 

### Return type

[**GroupV2GetGroupOptionalConversations200Response**](GroupV2GetGroupOptionalConversations200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2GetGroupsForMember

> GroupV2GetGroupsForMember200Response groupV2GetGroupsForMember(filter, groupType, membershipId, membershipType)



Get information about the groups that a given member has joined.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.GroupV2Api();
let filter = 56; // Number | Filter apply to list of joined groups.
let groupType = 56; // Number | Type of group the supplied member founded.
let membershipId = 789; // Number | Membership ID to for which to find founded groups.
let membershipType = 56; // Number | Membership type of the supplied membership ID.
apiInstance.groupV2GetGroupsForMember(filter, groupType, membershipId, membershipType, (error, data, response) => {
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
 **filter** | **Number**| Filter apply to list of joined groups. | 
 **groupType** | **Number**| Type of group the supplied member founded. | 
 **membershipId** | **Number**| Membership ID to for which to find founded groups. | 
 **membershipType** | **Number**| Membership type of the supplied membership ID. | 

### Return type

[**GroupV2GetGroupsForMember200Response**](GroupV2GetGroupsForMember200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2GetInvitedIndividuals

> GroupV2GetInvitedIndividuals200Response groupV2GetInvitedIndividuals(currentpage, groupId)



Get the list of users who have been invited into the group.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.GroupV2Api();
let currentpage = 56; // Number | Page number (starting with 1). Each page has a fixed size of 50 items per page.
let groupId = 789; // Number | ID of the group.
apiInstance.groupV2GetInvitedIndividuals(currentpage, groupId, (error, data, response) => {
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
 **currentpage** | **Number**| Page number (starting with 1). Each page has a fixed size of 50 items per page. | 
 **groupId** | **Number**| ID of the group. | 

### Return type

[**GroupV2GetInvitedIndividuals200Response**](GroupV2GetInvitedIndividuals200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2GetMembersOfGroup

> GroupV2GetAdminsAndFounderOfGroup200Response groupV2GetMembersOfGroup(currentpage, groupId, opts)



Get the list of members in a given group.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.GroupV2Api();
let currentpage = 56; // Number | Page number (starting with 1). Each page has a fixed size of 50 items per page.
let groupId = 789; // Number | The ID of the group.
let opts = {
  'memberType': 56, // Number | Filter out other member types. Use None for all members.
  'nameSearch': "nameSearch_example" // String | The name fragment upon which a search should be executed for members with matching display or unique names.
};
apiInstance.groupV2GetMembersOfGroup(currentpage, groupId, opts, (error, data, response) => {
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
 **currentpage** | **Number**| Page number (starting with 1). Each page has a fixed size of 50 items per page. | 
 **groupId** | **Number**| The ID of the group. | 
 **memberType** | **Number**| Filter out other member types. Use None for all members. | [optional] 
 **nameSearch** | **String**| The name fragment upon which a search should be executed for members with matching display or unique names. | [optional] 

### Return type

[**GroupV2GetAdminsAndFounderOfGroup200Response**](GroupV2GetAdminsAndFounderOfGroup200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2GetPendingMemberships

> GroupV2GetInvitedIndividuals200Response groupV2GetPendingMemberships(currentpage, groupId)



Get the list of users who are awaiting a decision on their application to join a given group. Modified to include application info.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.GroupV2Api();
let currentpage = 56; // Number | Page number (starting with 1). Each page has a fixed size of 50 items per page.
let groupId = 789; // Number | ID of the group.
apiInstance.groupV2GetPendingMemberships(currentpage, groupId, (error, data, response) => {
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
 **currentpage** | **Number**| Page number (starting with 1). Each page has a fixed size of 50 items per page. | 
 **groupId** | **Number**| ID of the group. | 

### Return type

[**GroupV2GetInvitedIndividuals200Response**](GroupV2GetInvitedIndividuals200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2GetPotentialGroupsForMember

> GroupV2GetPotentialGroupsForMember200Response groupV2GetPotentialGroupsForMember(filter, groupType, membershipId, membershipType)



Get information about the groups that a given member has applied to or been invited to.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.GroupV2Api();
let filter = 56; // Number | Filter apply to list of potential joined groups.
let groupType = 56; // Number | Type of group the supplied member applied.
let membershipId = 789; // Number | Membership ID to for which to find applied groups.
let membershipType = 56; // Number | Membership type of the supplied membership ID.
apiInstance.groupV2GetPotentialGroupsForMember(filter, groupType, membershipId, membershipType, (error, data, response) => {
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
 **filter** | **Number**| Filter apply to list of potential joined groups. | 
 **groupType** | **Number**| Type of group the supplied member applied. | 
 **membershipId** | **Number**| Membership ID to for which to find applied groups. | 
 **membershipType** | **Number**| Membership type of the supplied membership ID. | 

### Return type

[**GroupV2GetPotentialGroupsForMember200Response**](GroupV2GetPotentialGroupsForMember200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2GetRecommendedGroups

> GroupV2GetRecommendedGroups200Response groupV2GetRecommendedGroups(createDateRange, groupType)



Gets groups recommended for you based on the groups to whom those you follow belong.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.GroupV2Api();
let createDateRange = 56; // Number | Requested range in which to pull recommended groups
let groupType = 56; // Number | Type of groups requested
apiInstance.groupV2GetRecommendedGroups(createDateRange, groupType, (error, data, response) => {
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
 **createDateRange** | **Number**| Requested range in which to pull recommended groups | 
 **groupType** | **Number**| Type of groups requested | 

### Return type

[**GroupV2GetRecommendedGroups200Response**](GroupV2GetRecommendedGroups200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2GetUserClanInviteSetting

> GroupV2GetUserClanInviteSetting200Response groupV2GetUserClanInviteSetting(mType)



Gets the state of the user&#39;s clan invite preferences for a particular membership type - true if they wish to be invited to clans, false otherwise.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.GroupV2Api();
let mType = 56; // Number | The Destiny membership type of the account we wish to access settings.
apiInstance.groupV2GetUserClanInviteSetting(mType, (error, data, response) => {
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
 **mType** | **Number**| The Destiny membership type of the account we wish to access settings. | 

### Return type

[**GroupV2GetUserClanInviteSetting200Response**](GroupV2GetUserClanInviteSetting200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2GroupSearch

> GroupV2GroupSearch200Response groupV2GroupSearch()



Search for Groups.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.GroupV2Api();
apiInstance.groupV2GroupSearch((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GroupV2GroupSearch200Response**](GroupV2GroupSearch200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2IndividualGroupInvite

> GroupV2IndividualGroupInvite200Response groupV2IndividualGroupInvite(groupId, membershipId, membershipType)



Invite a user to join this group.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.GroupV2Api();
let groupId = 789; // Number | ID of the group you would like to join.
let membershipId = 789; // Number | Membership id of the account being invited.
let membershipType = 56; // Number | MembershipType of the account being invited.
apiInstance.groupV2IndividualGroupInvite(groupId, membershipId, membershipType, (error, data, response) => {
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
 **groupId** | **Number**| ID of the group you would like to join. | 
 **membershipId** | **Number**| Membership id of the account being invited. | 
 **membershipType** | **Number**| MembershipType of the account being invited. | 

### Return type

[**GroupV2IndividualGroupInvite200Response**](GroupV2IndividualGroupInvite200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2IndividualGroupInviteCancel

> GroupV2IndividualGroupInvite200Response groupV2IndividualGroupInviteCancel(groupId, membershipId, membershipType)



Cancels a pending invitation to join a group.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.GroupV2Api();
let groupId = 789; // Number | ID of the group you would like to join.
let membershipId = 789; // Number | Membership id of the account being cancelled.
let membershipType = 56; // Number | MembershipType of the account being cancelled.
apiInstance.groupV2IndividualGroupInviteCancel(groupId, membershipId, membershipType, (error, data, response) => {
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
 **groupId** | **Number**| ID of the group you would like to join. | 
 **membershipId** | **Number**| Membership id of the account being cancelled. | 
 **membershipType** | **Number**| MembershipType of the account being cancelled. | 

### Return type

[**GroupV2IndividualGroupInvite200Response**](GroupV2IndividualGroupInvite200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2KickMember

> GroupV2KickMember200Response groupV2KickMember(groupId, membershipId, membershipType)



Kick a member from the given group, forcing them to reapply if they wish to re-join the group. You must have suitable permissions in the group to perform this operation.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.GroupV2Api();
let groupId = 789; // Number | Group ID to kick the user from.
let membershipId = 789; // Number | Membership ID to kick.
let membershipType = 56; // Number | Membership type of the provided membership ID.
apiInstance.groupV2KickMember(groupId, membershipId, membershipType, (error, data, response) => {
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
 **groupId** | **Number**| Group ID to kick the user from. | 
 **membershipId** | **Number**| Membership ID to kick. | 
 **membershipType** | **Number**| Membership type of the provided membership ID. | 

### Return type

[**GroupV2KickMember200Response**](GroupV2KickMember200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2RecoverGroupForFounder

> GroupV2RecoverGroupForFounder200Response groupV2RecoverGroupForFounder(groupType, membershipId, membershipType)



Allows a founder to manually recover a group they can see in game but not on bungie.net

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.GroupV2Api();
let groupType = 56; // Number | Type of group the supplied member founded.
let membershipId = 789; // Number | Membership ID to for which to find founded groups.
let membershipType = 56; // Number | Membership type of the supplied membership ID.
apiInstance.groupV2RecoverGroupForFounder(groupType, membershipId, membershipType, (error, data, response) => {
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
 **groupType** | **Number**| Type of group the supplied member founded. | 
 **membershipId** | **Number**| Membership ID to for which to find founded groups. | 
 **membershipType** | **Number**| Membership type of the supplied membership ID. | 

### Return type

[**GroupV2RecoverGroupForFounder200Response**](GroupV2RecoverGroupForFounder200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## groupV2UnbanMember

> Destiny2EquipItem200Response groupV2UnbanMember(groupId, membershipId, membershipType)



Unbans the requested member, allowing them to re-apply for membership.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.GroupV2Api();
let groupId = 789; // Number | 
let membershipId = 789; // Number | Membership ID of the member to unban from the group
let membershipType = 56; // Number | Membership type of the provided membership ID.
apiInstance.groupV2UnbanMember(groupId, membershipId, membershipType, (error, data, response) => {
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
 **groupId** | **Number**|  | 
 **membershipId** | **Number**| Membership ID of the member to unban from the group | 
 **membershipType** | **Number**| Membership type of the provided membership ID. | 

### Return type

[**Destiny2EquipItem200Response**](Destiny2EquipItem200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

