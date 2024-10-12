# KeycloakAdminRestApi.RoleMapperApi

All URIs are relative to *http://keycloak.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realmGroupsIdRoleMappingsGet**](RoleMapperApi.md#realmGroupsIdRoleMappingsGet) | **GET** /{realm}/groups/{id}/role-mappings | Get role mappings
[**realmGroupsIdRoleMappingsRealmAvailableGet**](RoleMapperApi.md#realmGroupsIdRoleMappingsRealmAvailableGet) | **GET** /{realm}/groups/{id}/role-mappings/realm/available | Get realm-level roles that can be mapped
[**realmGroupsIdRoleMappingsRealmCompositeGet**](RoleMapperApi.md#realmGroupsIdRoleMappingsRealmCompositeGet) | **GET** /{realm}/groups/{id}/role-mappings/realm/composite | Get effective realm-level role mappings   This will recurse all composite roles to get the result.
[**realmGroupsIdRoleMappingsRealmDelete**](RoleMapperApi.md#realmGroupsIdRoleMappingsRealmDelete) | **DELETE** /{realm}/groups/{id}/role-mappings/realm | Delete realm-level role mappings
[**realmGroupsIdRoleMappingsRealmGet**](RoleMapperApi.md#realmGroupsIdRoleMappingsRealmGet) | **GET** /{realm}/groups/{id}/role-mappings/realm | Get realm-level role mappings
[**realmGroupsIdRoleMappingsRealmPost**](RoleMapperApi.md#realmGroupsIdRoleMappingsRealmPost) | **POST** /{realm}/groups/{id}/role-mappings/realm | Add realm-level role mappings to the user
[**realmUsersIdRoleMappingsGet**](RoleMapperApi.md#realmUsersIdRoleMappingsGet) | **GET** /{realm}/users/{id}/role-mappings | Get role mappings
[**realmUsersIdRoleMappingsRealmAvailableGet**](RoleMapperApi.md#realmUsersIdRoleMappingsRealmAvailableGet) | **GET** /{realm}/users/{id}/role-mappings/realm/available | Get realm-level roles that can be mapped
[**realmUsersIdRoleMappingsRealmCompositeGet**](RoleMapperApi.md#realmUsersIdRoleMappingsRealmCompositeGet) | **GET** /{realm}/users/{id}/role-mappings/realm/composite | Get effective realm-level role mappings   This will recurse all composite roles to get the result.
[**realmUsersIdRoleMappingsRealmDelete**](RoleMapperApi.md#realmUsersIdRoleMappingsRealmDelete) | **DELETE** /{realm}/users/{id}/role-mappings/realm | Delete realm-level role mappings
[**realmUsersIdRoleMappingsRealmGet**](RoleMapperApi.md#realmUsersIdRoleMappingsRealmGet) | **GET** /{realm}/users/{id}/role-mappings/realm | Get realm-level role mappings
[**realmUsersIdRoleMappingsRealmPost**](RoleMapperApi.md#realmUsersIdRoleMappingsRealmPost) | **POST** /{realm}/users/{id}/role-mappings/realm | Add realm-level role mappings to the user



## realmGroupsIdRoleMappingsGet

> MappingsRepresentation realmGroupsIdRoleMappingsGet(realm, id)

Get role mappings

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RoleMapperApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | 
apiInstance.realmGroupsIdRoleMappingsGet(realm, id, (error, data, response) => {
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

[**MappingsRepresentation**](MappingsRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmGroupsIdRoleMappingsRealmAvailableGet

> [RoleRepresentation] realmGroupsIdRoleMappingsRealmAvailableGet(realm, id)

Get realm-level roles that can be mapped

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RoleMapperApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | 
apiInstance.realmGroupsIdRoleMappingsRealmAvailableGet(realm, id, (error, data, response) => {
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

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmGroupsIdRoleMappingsRealmCompositeGet

> [RoleRepresentation] realmGroupsIdRoleMappingsRealmCompositeGet(realm, id)

Get effective realm-level role mappings   This will recurse all composite roles to get the result.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RoleMapperApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | 
apiInstance.realmGroupsIdRoleMappingsRealmCompositeGet(realm, id, (error, data, response) => {
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

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmGroupsIdRoleMappingsRealmDelete

> realmGroupsIdRoleMappingsRealmDelete(realm, id, roleRepresentation)

Delete realm-level role mappings

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RoleMapperApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | 
let roleRepresentation = [new KeycloakAdminRestApi.RoleRepresentation()]; // [RoleRepresentation] | 
apiInstance.realmGroupsIdRoleMappingsRealmDelete(realm, id, roleRepresentation, (error, data, response) => {
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
 **roleRepresentation** | [**[RoleRepresentation]**](RoleRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmGroupsIdRoleMappingsRealmGet

> [RoleRepresentation] realmGroupsIdRoleMappingsRealmGet(realm, id)

Get realm-level role mappings

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RoleMapperApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | 
apiInstance.realmGroupsIdRoleMappingsRealmGet(realm, id, (error, data, response) => {
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

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmGroupsIdRoleMappingsRealmPost

> realmGroupsIdRoleMappingsRealmPost(realm, id, roleRepresentation)

Add realm-level role mappings to the user

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RoleMapperApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | 
let roleRepresentation = [new KeycloakAdminRestApi.RoleRepresentation()]; // [RoleRepresentation] | Roles to add
apiInstance.realmGroupsIdRoleMappingsRealmPost(realm, id, roleRepresentation, (error, data, response) => {
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
 **roleRepresentation** | [**[RoleRepresentation]**](RoleRepresentation.md)| Roles to add | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmUsersIdRoleMappingsGet

> MappingsRepresentation realmUsersIdRoleMappingsGet(realm, id)

Get role mappings

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RoleMapperApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
apiInstance.realmUsersIdRoleMappingsGet(realm, id, (error, data, response) => {
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
 **id** | **String**| User id | 

### Return type

[**MappingsRepresentation**](MappingsRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmUsersIdRoleMappingsRealmAvailableGet

> [RoleRepresentation] realmUsersIdRoleMappingsRealmAvailableGet(realm, id)

Get realm-level roles that can be mapped

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RoleMapperApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
apiInstance.realmUsersIdRoleMappingsRealmAvailableGet(realm, id, (error, data, response) => {
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
 **id** | **String**| User id | 

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmUsersIdRoleMappingsRealmCompositeGet

> [RoleRepresentation] realmUsersIdRoleMappingsRealmCompositeGet(realm, id)

Get effective realm-level role mappings   This will recurse all composite roles to get the result.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RoleMapperApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
apiInstance.realmUsersIdRoleMappingsRealmCompositeGet(realm, id, (error, data, response) => {
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
 **id** | **String**| User id | 

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmUsersIdRoleMappingsRealmDelete

> realmUsersIdRoleMappingsRealmDelete(realm, id, roleRepresentation)

Delete realm-level role mappings

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RoleMapperApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
let roleRepresentation = [new KeycloakAdminRestApi.RoleRepresentation()]; // [RoleRepresentation] | 
apiInstance.realmUsersIdRoleMappingsRealmDelete(realm, id, roleRepresentation, (error, data, response) => {
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
 **id** | **String**| User id | 
 **roleRepresentation** | [**[RoleRepresentation]**](RoleRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmUsersIdRoleMappingsRealmGet

> [RoleRepresentation] realmUsersIdRoleMappingsRealmGet(realm, id)

Get realm-level role mappings

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RoleMapperApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
apiInstance.realmUsersIdRoleMappingsRealmGet(realm, id, (error, data, response) => {
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
 **id** | **String**| User id | 

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmUsersIdRoleMappingsRealmPost

> realmUsersIdRoleMappingsRealmPost(realm, id, roleRepresentation)

Add realm-level role mappings to the user

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RoleMapperApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
let roleRepresentation = [new KeycloakAdminRestApi.RoleRepresentation()]; // [RoleRepresentation] | Roles to add
apiInstance.realmUsersIdRoleMappingsRealmPost(realm, id, roleRepresentation, (error, data, response) => {
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
 **id** | **String**| User id | 
 **roleRepresentation** | [**[RoleRepresentation]**](RoleRepresentation.md)| Roles to add | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

