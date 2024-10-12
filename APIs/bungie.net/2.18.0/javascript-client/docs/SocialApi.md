# BungieNetApi.SocialApi

All URIs are relative to *https://www.bungie.net/Platform*

Method | HTTP request | Description
------------- | ------------- | -------------
[**socialAcceptFriendRequest**](SocialApi.md#socialAcceptFriendRequest) | **POST** /Social/Friends/Requests/Accept/{membershipId}/ | 
[**socialDeclineFriendRequest**](SocialApi.md#socialDeclineFriendRequest) | **POST** /Social/Friends/Requests/Decline/{membershipId}/ | 
[**socialGetFriendList**](SocialApi.md#socialGetFriendList) | **GET** /Social/Friends/ | 
[**socialGetFriendRequestList**](SocialApi.md#socialGetFriendRequestList) | **GET** /Social/Friends/Requests/ | 
[**socialGetPlatformFriendList**](SocialApi.md#socialGetPlatformFriendList) | **GET** /Social/PlatformFriends/{friendPlatform}/{page}/ | 
[**socialIssueFriendRequest**](SocialApi.md#socialIssueFriendRequest) | **POST** /Social/Friends/Add/{membershipId}/ | 
[**socialRemoveFriend**](SocialApi.md#socialRemoveFriend) | **POST** /Social/Friends/Remove/{membershipId}/ | 
[**socialRemoveFriendRequest**](SocialApi.md#socialRemoveFriendRequest) | **POST** /Social/Friends/Requests/Remove/{membershipId}/ | 



## socialAcceptFriendRequest

> GroupV2GetUserClanInviteSetting200Response socialAcceptFriendRequest(membershipId)



Accepts a friend relationship with the target user. The user must be on your incoming friend request list, though no error will occur if they are not.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.SocialApi();
let membershipId = "membershipId_example"; // String | The membership id of the user you wish to accept.
apiInstance.socialAcceptFriendRequest(membershipId, (error, data, response) => {
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
 **membershipId** | **String**| The membership id of the user you wish to accept. | 

### Return type

[**GroupV2GetUserClanInviteSetting200Response**](GroupV2GetUserClanInviteSetting200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## socialDeclineFriendRequest

> GroupV2GetUserClanInviteSetting200Response socialDeclineFriendRequest(membershipId)



Declines a friend relationship with the target user. The user must be on your incoming friend request list, though no error will occur if they are not.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.SocialApi();
let membershipId = "membershipId_example"; // String | The membership id of the user you wish to decline.
apiInstance.socialDeclineFriendRequest(membershipId, (error, data, response) => {
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
 **membershipId** | **String**| The membership id of the user you wish to decline. | 

### Return type

[**GroupV2GetUserClanInviteSetting200Response**](GroupV2GetUserClanInviteSetting200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## socialGetFriendList

> SocialGetFriendList200Response socialGetFriendList()



Returns your Bungie Friend list

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.SocialApi();
apiInstance.socialGetFriendList((error, data, response) => {
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

[**SocialGetFriendList200Response**](SocialGetFriendList200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## socialGetFriendRequestList

> SocialGetFriendRequestList200Response socialGetFriendRequestList()



Returns your friend request queue.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.SocialApi();
apiInstance.socialGetFriendRequestList((error, data, response) => {
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

[**SocialGetFriendRequestList200Response**](SocialGetFriendRequestList200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## socialGetPlatformFriendList

> SocialGetPlatformFriendList200Response socialGetPlatformFriendList(friendPlatform, page)



Gets the platform friend of the requested type, with additional information if they have Bungie accounts. Must have a recent login session with said platform.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.SocialApi();
let friendPlatform = 56; // Number | The platform friend type.
let page = "page_example"; // String | The zero based page to return. Page size is 100.
apiInstance.socialGetPlatformFriendList(friendPlatform, page, (error, data, response) => {
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
 **friendPlatform** | **Number**| The platform friend type. | 
 **page** | **String**| The zero based page to return. Page size is 100. | 

### Return type

[**SocialGetPlatformFriendList200Response**](SocialGetPlatformFriendList200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## socialIssueFriendRequest

> GroupV2GetUserClanInviteSetting200Response socialIssueFriendRequest(membershipId)



Requests a friend relationship with the target user. Any of the target user&#39;s linked membership ids are valid inputs.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.SocialApi();
let membershipId = "membershipId_example"; // String | The membership id of the user you wish to add.
apiInstance.socialIssueFriendRequest(membershipId, (error, data, response) => {
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
 **membershipId** | **String**| The membership id of the user you wish to add. | 

### Return type

[**GroupV2GetUserClanInviteSetting200Response**](GroupV2GetUserClanInviteSetting200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## socialRemoveFriend

> GroupV2GetUserClanInviteSetting200Response socialRemoveFriend(membershipId)



Remove a friend relationship with the target user. The user must be on your friend list, though no error will occur if they are not.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.SocialApi();
let membershipId = "membershipId_example"; // String | The membership id of the user you wish to remove.
apiInstance.socialRemoveFriend(membershipId, (error, data, response) => {
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
 **membershipId** | **String**| The membership id of the user you wish to remove. | 

### Return type

[**GroupV2GetUserClanInviteSetting200Response**](GroupV2GetUserClanInviteSetting200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## socialRemoveFriendRequest

> GroupV2GetUserClanInviteSetting200Response socialRemoveFriendRequest(membershipId)



Remove a friend relationship with the target user. The user must be on your outgoing request friend list, though no error will occur if they are not.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.SocialApi();
let membershipId = "membershipId_example"; // String | The membership id of the user you wish to remove.
apiInstance.socialRemoveFriendRequest(membershipId, (error, data, response) => {
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
 **membershipId** | **String**| The membership id of the user you wish to remove. | 

### Return type

[**GroupV2GetUserClanInviteSetting200Response**](GroupV2GetUserClanInviteSetting200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

