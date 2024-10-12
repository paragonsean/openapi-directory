# KeycloakAdminRestApi.GroupsApi

All URIs are relative to *http://keycloak.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realmGroupsCountGet**](GroupsApi.md#realmGroupsCountGet) | **GET** /{realm}/groups/count | Returns the groups counts.
[**realmGroupsGet**](GroupsApi.md#realmGroupsGet) | **GET** /{realm}/groups | Get group hierarchy.
[**realmGroupsIdChildrenPost**](GroupsApi.md#realmGroupsIdChildrenPost) | **POST** /{realm}/groups/{id}/children | Set or create child.
[**realmGroupsIdDelete**](GroupsApi.md#realmGroupsIdDelete) | **DELETE** /{realm}/groups/{id} | 
[**realmGroupsIdGet**](GroupsApi.md#realmGroupsIdGet) | **GET** /{realm}/groups/{id} | 
[**realmGroupsIdManagementPermissionsGet**](GroupsApi.md#realmGroupsIdManagementPermissionsGet) | **GET** /{realm}/groups/{id}/management/permissions | Return object stating whether client Authorization permissions have been initialized or not and a reference
[**realmGroupsIdManagementPermissionsPut**](GroupsApi.md#realmGroupsIdManagementPermissionsPut) | **PUT** /{realm}/groups/{id}/management/permissions | Return object stating whether client Authorization permissions have been initialized or not and a reference
[**realmGroupsIdMembersGet**](GroupsApi.md#realmGroupsIdMembersGet) | **GET** /{realm}/groups/{id}/members | Get users   Returns a list of users, filtered according to query parameters
[**realmGroupsIdPut**](GroupsApi.md#realmGroupsIdPut) | **PUT** /{realm}/groups/{id} | Update group, ignores subgroups.
[**realmGroupsPost**](GroupsApi.md#realmGroupsPost) | **POST** /{realm}/groups | create or add a top level realm groupSet or create child.



## realmGroupsCountGet

> {String: Object} realmGroupsCountGet(realm, opts)

Returns the groups counts.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.GroupsApi();
let realm = "realm_example"; // String | realm name (not id!)
let opts = {
  'search': "search_example", // String | 
  'top': true // Boolean | 
};
apiInstance.realmGroupsCountGet(realm, opts, (error, data, response) => {
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
 **search** | **String**|  | [optional] 
 **top** | **Boolean**|  | [optional] 

### Return type

**{String: Object}**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmGroupsGet

> [GroupRepresentation] realmGroupsGet(realm, opts)

Get group hierarchy.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.GroupsApi();
let realm = "realm_example"; // String | realm name (not id!)
let opts = {
  'briefRepresentation': true, // Boolean | 
  'first': 56, // Number | 
  'max': 56, // Number | 
  'search': "search_example" // String | 
};
apiInstance.realmGroupsGet(realm, opts, (error, data, response) => {
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
 **briefRepresentation** | **Boolean**|  | [optional] 
 **first** | **Number**|  | [optional] 
 **max** | **Number**|  | [optional] 
 **search** | **String**|  | [optional] 

### Return type

[**[GroupRepresentation]**](GroupRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmGroupsIdChildrenPost

> realmGroupsIdChildrenPost(realm, id, groupRepresentation)

Set or create child.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.GroupsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | 
let groupRepresentation = new KeycloakAdminRestApi.GroupRepresentation(); // GroupRepresentation | 
apiInstance.realmGroupsIdChildrenPost(realm, id, groupRepresentation, (error, data, response) => {
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
 **groupRepresentation** | [**GroupRepresentation**](GroupRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmGroupsIdDelete

> realmGroupsIdDelete(realm, id)



### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.GroupsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | 
apiInstance.realmGroupsIdDelete(realm, id, (error, data, response) => {
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


## realmGroupsIdGet

> GroupRepresentation realmGroupsIdGet(realm, id)



### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.GroupsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | 
apiInstance.realmGroupsIdGet(realm, id, (error, data, response) => {
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

[**GroupRepresentation**](GroupRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmGroupsIdManagementPermissionsGet

> ManagementPermissionReference realmGroupsIdManagementPermissionsGet(realm, id)

Return object stating whether client Authorization permissions have been initialized or not and a reference

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.GroupsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | 
apiInstance.realmGroupsIdManagementPermissionsGet(realm, id, (error, data, response) => {
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

[**ManagementPermissionReference**](ManagementPermissionReference.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmGroupsIdManagementPermissionsPut

> ManagementPermissionReference realmGroupsIdManagementPermissionsPut(realm, id, managementPermissionReference)

Return object stating whether client Authorization permissions have been initialized or not and a reference

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.GroupsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | 
let managementPermissionReference = new KeycloakAdminRestApi.ManagementPermissionReference(); // ManagementPermissionReference | 
apiInstance.realmGroupsIdManagementPermissionsPut(realm, id, managementPermissionReference, (error, data, response) => {
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
 **managementPermissionReference** | [**ManagementPermissionReference**](ManagementPermissionReference.md)|  | 

### Return type

[**ManagementPermissionReference**](ManagementPermissionReference.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## realmGroupsIdMembersGet

> [UserRepresentation] realmGroupsIdMembersGet(realm, id, opts)

Get users   Returns a list of users, filtered according to query parameters

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.GroupsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | 
let opts = {
  'briefRepresentation': true, // Boolean | Only return basic information (only guaranteed to return id, username, created, first and last name,  email, enabled state, email verification state, federation link, and access.  Note that it means that namely user attributes, required actions, and not before are not returned.)
  'first': 56, // Number | Pagination offset
  'max': 56 // Number | Maximum results size (defaults to 100)
};
apiInstance.realmGroupsIdMembersGet(realm, id, opts, (error, data, response) => {
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
 **briefRepresentation** | **Boolean**| Only return basic information (only guaranteed to return id, username, created, first and last name,  email, enabled state, email verification state, federation link, and access.  Note that it means that namely user attributes, required actions, and not before are not returned.) | [optional] 
 **first** | **Number**| Pagination offset | [optional] 
 **max** | **Number**| Maximum results size (defaults to 100) | [optional] 

### Return type

[**[UserRepresentation]**](UserRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmGroupsIdPut

> realmGroupsIdPut(realm, id, groupRepresentation)

Update group, ignores subgroups.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.GroupsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | 
let groupRepresentation = new KeycloakAdminRestApi.GroupRepresentation(); // GroupRepresentation | 
apiInstance.realmGroupsIdPut(realm, id, groupRepresentation, (error, data, response) => {
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
 **groupRepresentation** | [**GroupRepresentation**](GroupRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmGroupsPost

> realmGroupsPost(realm, groupRepresentation)

create or add a top level realm groupSet or create child.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.GroupsApi();
let realm = "realm_example"; // String | realm name (not id!)
let groupRepresentation = new KeycloakAdminRestApi.GroupRepresentation(); // GroupRepresentation | 
apiInstance.realmGroupsPost(realm, groupRepresentation, (error, data, response) => {
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
 **groupRepresentation** | [**GroupRepresentation**](GroupRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

