# KeycloakAdminRestApi.AttackDetectionApi

All URIs are relative to *http://keycloak.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realmAttackDetectionBruteForceUsersDelete**](AttackDetectionApi.md#realmAttackDetectionBruteForceUsersDelete) | **DELETE** /{realm}/attack-detection/brute-force/users | Clear any user login failures for all users   This can release temporary disabled users
[**realmAttackDetectionBruteForceUsersUserIdDelete**](AttackDetectionApi.md#realmAttackDetectionBruteForceUsersUserIdDelete) | **DELETE** /{realm}/attack-detection/brute-force/users/{userId} | Clear any user login failures for the user   This can release temporary disabled user
[**realmAttackDetectionBruteForceUsersUserIdGet**](AttackDetectionApi.md#realmAttackDetectionBruteForceUsersUserIdGet) | **GET** /{realm}/attack-detection/brute-force/users/{userId} | Get status of a username in brute force detection



## realmAttackDetectionBruteForceUsersDelete

> realmAttackDetectionBruteForceUsersDelete(realm)

Clear any user login failures for all users   This can release temporary disabled users

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AttackDetectionApi();
let realm = "realm_example"; // String | realm name (not id!)
apiInstance.realmAttackDetectionBruteForceUsersDelete(realm, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **String**| realm name (not id!) | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmAttackDetectionBruteForceUsersUserIdDelete

> realmAttackDetectionBruteForceUsersUserIdDelete(realm, userId)

Clear any user login failures for the user   This can release temporary disabled user

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AttackDetectionApi();
let realm = "realm_example"; // String | realm name (not id!)
let userId = "userId_example"; // String | 
apiInstance.realmAttackDetectionBruteForceUsersUserIdDelete(realm, userId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **realm** | **String**| realm name (not id!) | 
 **userId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmAttackDetectionBruteForceUsersUserIdGet

> {String: Object} realmAttackDetectionBruteForceUsersUserIdGet(realm, userId)

Get status of a username in brute force detection

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.AttackDetectionApi();
let realm = "realm_example"; // String | realm name (not id!)
let userId = "userId_example"; // String | 
apiInstance.realmAttackDetectionBruteForceUsersUserIdGet(realm, userId, (error, data, response) => {
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
 **realm** | **String**| realm name (not id!) | 
 **userId** | **String**|  | 

### Return type

**{String: Object}**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

