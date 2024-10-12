# KeycloakAdminRestApi.UserStorageProviderApi

All URIs are relative to *http://keycloak.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**idNameGet**](UserStorageProviderApi.md#idNameGet) | **GET** /{id}/name | Need this for admin console to display simple name of provider when displaying client detail   KEYCLOAK-4328
[**realmUserStorageIdNameGet**](UserStorageProviderApi.md#realmUserStorageIdNameGet) | **GET** /{realm}/user-storage/{id}/name | Need this for admin console to display simple name of provider when displaying user detail   KEYCLOAK-4328
[**realmUserStorageIdRemoveImportedUsersPost**](UserStorageProviderApi.md#realmUserStorageIdRemoveImportedUsersPost) | **POST** /{realm}/user-storage/{id}/remove-imported-users | Remove imported users
[**realmUserStorageIdSyncPost**](UserStorageProviderApi.md#realmUserStorageIdSyncPost) | **POST** /{realm}/user-storage/{id}/sync | Trigger sync of users   Action can be \&quot;triggerFullSync\&quot; or \&quot;triggerChangedUsersSync\&quot;
[**realmUserStorageIdUnlinkUsersPost**](UserStorageProviderApi.md#realmUserStorageIdUnlinkUsersPost) | **POST** /{realm}/user-storage/{id}/unlink-users | Unlink imported users from a storage provider
[**realmUserStorageParentIdMappersIdSyncPost**](UserStorageProviderApi.md#realmUserStorageParentIdMappersIdSyncPost) | **POST** /{realm}/user-storage/{parentId}/mappers/{id}/sync | Trigger sync of mapper data related to ldap mapper (roles, groups, …​)   direction is \&quot;fedToKeycloak\&quot; or \&quot;keycloakToFed\&quot;



## idNameGet

> {String: Object} idNameGet(id)

Need this for admin console to display simple name of provider when displaying client detail   KEYCLOAK-4328

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UserStorageProviderApi();
let id = "id_example"; // String | 
apiInstance.idNameGet(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

**{String: Object}**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmUserStorageIdNameGet

> {String: Object} realmUserStorageIdNameGet(realm, id)

Need this for admin console to display simple name of provider when displaying user detail   KEYCLOAK-4328

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UserStorageProviderApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | 
apiInstance.realmUserStorageIdNameGet(realm, id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

**{String: Object}**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmUserStorageIdRemoveImportedUsersPost

> realmUserStorageIdRemoveImportedUsersPost(realm, id)

Remove imported users

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UserStorageProviderApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | 
apiInstance.realmUserStorageIdRemoveImportedUsersPost(realm, id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmUserStorageIdSyncPost

> SynchronizationResult realmUserStorageIdSyncPost(realm, id, opts)

Trigger sync of users   Action can be \&quot;triggerFullSync\&quot; or \&quot;triggerChangedUsersSync\&quot;

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UserStorageProviderApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | 
let opts = {
  'action': "action_example" // String | 
};
apiInstance.realmUserStorageIdSyncPost(realm, id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **action** | **String**|  | [optional] 

### Return type

[**SynchronizationResult**](SynchronizationResult.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmUserStorageIdUnlinkUsersPost

> realmUserStorageIdUnlinkUsersPost(realm, id)

Unlink imported users from a storage provider

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UserStorageProviderApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | 
apiInstance.realmUserStorageIdUnlinkUsersPost(realm, id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmUserStorageParentIdMappersIdSyncPost

> SynchronizationResult realmUserStorageParentIdMappersIdSyncPost(realm, parentId, id, opts)

Trigger sync of mapper data related to ldap mapper (roles, groups, …​)   direction is \&quot;fedToKeycloak\&quot; or \&quot;keycloakToFed\&quot;

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.UserStorageProviderApi();
let realm = "realm_example"; // String | realm name (not id!)
let parentId = "parentId_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'direction': "direction_example" // String | 
};
apiInstance.realmUserStorageParentIdMappersIdSyncPost(realm, parentId, id, opts, (error, data, response) => {
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
 **parentId** | **String**|  | 
 **id** | **String**|  | 
 **direction** | **String**|  | [optional] 

### Return type

[**SynchronizationResult**](SynchronizationResult.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

