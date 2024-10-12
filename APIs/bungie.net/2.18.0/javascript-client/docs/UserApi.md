# BungieNetApi.UserApi

All URIs are relative to *https://www.bungie.net/Platform*

Method | HTTP request | Description
------------- | ------------- | -------------
[**userGetAvailableThemes**](UserApi.md#userGetAvailableThemes) | **GET** /User/GetAvailableThemes/ | 
[**userGetBungieNetUserById**](UserApi.md#userGetBungieNetUserById) | **GET** /User/GetBungieNetUserById/{id}/ | 
[**userGetCredentialTypesForTargetAccount**](UserApi.md#userGetCredentialTypesForTargetAccount) | **GET** /User/GetCredentialTypesForTargetAccount/{membershipId}/ | 
[**userGetMembershipDataById**](UserApi.md#userGetMembershipDataById) | **GET** /User/GetMembershipsById/{membershipId}/{membershipType}/ | 
[**userGetMembershipDataForCurrentUser**](UserApi.md#userGetMembershipDataForCurrentUser) | **GET** /User/GetMembershipsForCurrentUser/ | 
[**userGetMembershipFromHardLinkedCredential**](UserApi.md#userGetMembershipFromHardLinkedCredential) | **GET** /User/GetMembershipFromHardLinkedCredential/{crType}/{credential}/ | 
[**userGetSanitizedPlatformDisplayNames**](UserApi.md#userGetSanitizedPlatformDisplayNames) | **GET** /User/GetSanitizedPlatformDisplayNames/{membershipId}/ | 
[**userSearchByGlobalNamePost**](UserApi.md#userSearchByGlobalNamePost) | **POST** /User/Search/GlobalName/{page}/ | 
[**userSearchByGlobalNamePrefix**](UserApi.md#userSearchByGlobalNamePrefix) | **GET** /User/Search/Prefix/{displayNamePrefix}/{page}/ | 



## userGetAvailableThemes

> UserGetAvailableThemes200Response userGetAvailableThemes()



Returns a list of all available user themes.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.UserApi();
apiInstance.userGetAvailableThemes((error, data, response) => {
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

[**UserGetAvailableThemes200Response**](UserGetAvailableThemes200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## userGetBungieNetUserById

> UserGetBungieNetUserById200Response userGetBungieNetUserById(id)



Loads a bungienet user by membership id.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.UserApi();
let id = 789; // Number | The requested Bungie.net membership id.
apiInstance.userGetBungieNetUserById(id, (error, data, response) => {
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
 **id** | **Number**| The requested Bungie.net membership id. | 

### Return type

[**UserGetBungieNetUserById200Response**](UserGetBungieNetUserById200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## userGetCredentialTypesForTargetAccount

> UserGetCredentialTypesForTargetAccount200Response userGetCredentialTypesForTargetAccount(membershipId)



Returns a list of credential types attached to the requested account

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.UserApi();
let membershipId = 789; // Number | The user's membership id
apiInstance.userGetCredentialTypesForTargetAccount(membershipId, (error, data, response) => {
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
 **membershipId** | **Number**| The user&#39;s membership id | 

### Return type

[**UserGetCredentialTypesForTargetAccount200Response**](UserGetCredentialTypesForTargetAccount200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## userGetMembershipDataById

> UserGetMembershipDataById200Response userGetMembershipDataById(membershipId, membershipType)



Returns a list of accounts associated with the supplied membership ID and membership type. This will include all linked accounts (even when hidden) if supplied credentials permit it.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.UserApi();
let membershipId = 789; // Number | The membership ID of the target user.
let membershipType = 56; // Number | Type of the supplied membership ID.
apiInstance.userGetMembershipDataById(membershipId, membershipType, (error, data, response) => {
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
 **membershipId** | **Number**| The membership ID of the target user. | 
 **membershipType** | **Number**| Type of the supplied membership ID. | 

### Return type

[**UserGetMembershipDataById200Response**](UserGetMembershipDataById200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## userGetMembershipDataForCurrentUser

> UserGetMembershipDataById200Response userGetMembershipDataForCurrentUser()



Returns a list of accounts associated with signed in user. This is useful for OAuth implementations that do not give you access to the token response.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';
let defaultClient = BungieNetApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BungieNetApi.UserApi();
apiInstance.userGetMembershipDataForCurrentUser((error, data, response) => {
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

[**UserGetMembershipDataById200Response**](UserGetMembershipDataById200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## userGetMembershipFromHardLinkedCredential

> UserGetMembershipFromHardLinkedCredential200Response userGetMembershipFromHardLinkedCredential(credential, crType)



Gets any hard linked membership given a credential. Only works for credentials that are public (just SteamID64 right now). Cross Save aware.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.UserApi();
let credential = "credential_example"; // String | The credential to look up. Must be a valid SteamID64.
let crType = 56; // Number | The credential type. 'SteamId' is the only valid value at present.
apiInstance.userGetMembershipFromHardLinkedCredential(credential, crType, (error, data, response) => {
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
 **credential** | **String**| The credential to look up. Must be a valid SteamID64. | 
 **crType** | **Number**| The credential type. &#39;SteamId&#39; is the only valid value at present. | 

### Return type

[**UserGetMembershipFromHardLinkedCredential200Response**](UserGetMembershipFromHardLinkedCredential200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## userGetSanitizedPlatformDisplayNames

> GetAvailableLocales200Response userGetSanitizedPlatformDisplayNames(membershipId)



Gets a list of all display names linked to this membership id but sanitized (profanity filtered). Obeys all visibility rules of calling user and is heavily cached.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.UserApi();
let membershipId = 789; // Number | The requested membership id to load.
apiInstance.userGetSanitizedPlatformDisplayNames(membershipId, (error, data, response) => {
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
 **membershipId** | **Number**| The requested membership id to load. | 

### Return type

[**GetAvailableLocales200Response**](GetAvailableLocales200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## userSearchByGlobalNamePost

> UserSearchByGlobalNamePost200Response userSearchByGlobalNamePost(page)



Given the prefix of a global display name, returns all users who share that name.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.UserApi();
let page = 56; // Number | The zero-based page of results you desire.
apiInstance.userSearchByGlobalNamePost(page, (error, data, response) => {
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
 **page** | **Number**| The zero-based page of results you desire. | 

### Return type

[**UserSearchByGlobalNamePost200Response**](UserSearchByGlobalNamePost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## userSearchByGlobalNamePrefix

> UserSearchByGlobalNamePost200Response userSearchByGlobalNamePrefix(displayNamePrefix, page)



[OBSOLETE] Do not use this to search users, use SearchByGlobalNamePost instead.

### Example

```javascript
import BungieNetApi from 'bungie_net_api';

let apiInstance = new BungieNetApi.UserApi();
let displayNamePrefix = "displayNamePrefix_example"; // String | The display name prefix you're looking for.
let page = 56; // Number | The zero-based page of results you desire.
apiInstance.userSearchByGlobalNamePrefix(displayNamePrefix, page, (error, data, response) => {
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
 **displayNamePrefix** | **String**| The display name prefix you&#39;re looking for. | 
 **page** | **Number**| The zero-based page of results you desire. | 

### Return type

[**UserSearchByGlobalNamePost200Response**](UserSearchByGlobalNamePost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

