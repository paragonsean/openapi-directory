# KeycloakAdminRestApi.RolesByIDApi

All URIs are relative to *http://keycloak.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realmRolesByIdRoleIdCompositesClientsClientGet**](RolesByIDApi.md#realmRolesByIdRoleIdCompositesClientsClientGet) | **GET** /{realm}/roles-by-id/{role-id}/composites/clients/{client} | Get client-level roles for the client that are in the role’s composite
[**realmRolesByIdRoleIdCompositesDelete**](RolesByIDApi.md#realmRolesByIdRoleIdCompositesDelete) | **DELETE** /{realm}/roles-by-id/{role-id}/composites | Remove a set of roles from the role’s composite
[**realmRolesByIdRoleIdCompositesGet**](RolesByIDApi.md#realmRolesByIdRoleIdCompositesGet) | **GET** /{realm}/roles-by-id/{role-id}/composites | Get role’s children   Returns a set of role’s children provided the role is a composite.
[**realmRolesByIdRoleIdCompositesPost**](RolesByIDApi.md#realmRolesByIdRoleIdCompositesPost) | **POST** /{realm}/roles-by-id/{role-id}/composites | Make the role a composite role by associating some child roles
[**realmRolesByIdRoleIdCompositesRealmGet**](RolesByIDApi.md#realmRolesByIdRoleIdCompositesRealmGet) | **GET** /{realm}/roles-by-id/{role-id}/composites/realm | Get realm-level roles that are in the role’s composite
[**realmRolesByIdRoleIdDelete**](RolesByIDApi.md#realmRolesByIdRoleIdDelete) | **DELETE** /{realm}/roles-by-id/{role-id} | Delete the role
[**realmRolesByIdRoleIdGet**](RolesByIDApi.md#realmRolesByIdRoleIdGet) | **GET** /{realm}/roles-by-id/{role-id} | Get a specific role’s representation
[**realmRolesByIdRoleIdManagementPermissionsGet**](RolesByIDApi.md#realmRolesByIdRoleIdManagementPermissionsGet) | **GET** /{realm}/roles-by-id/{role-id}/management/permissions | Return object stating whether role Authoirzation permissions have been initialized or not and a reference
[**realmRolesByIdRoleIdManagementPermissionsPut**](RolesByIDApi.md#realmRolesByIdRoleIdManagementPermissionsPut) | **PUT** /{realm}/roles-by-id/{role-id}/management/permissions | Return object stating whether role Authoirzation permissions have been initialized or not and a reference
[**realmRolesByIdRoleIdPut**](RolesByIDApi.md#realmRolesByIdRoleIdPut) | **PUT** /{realm}/roles-by-id/{role-id} | Update the role



## realmRolesByIdRoleIdCompositesClientsClientGet

> [RoleRepresentation] realmRolesByIdRoleIdCompositesClientsClientGet(realm, roleId, client)

Get client-level roles for the client that are in the role’s composite

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesByIDApi();
let realm = "realm_example"; // String | realm name (not id!)
let roleId = "roleId_example"; // String | 
let client = "client_example"; // String | 
apiInstance.realmRolesByIdRoleIdCompositesClientsClientGet(realm, roleId, client, (error, data, response) => {
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
 **roleId** | **String**|  | 
 **client** | **String**|  | 

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmRolesByIdRoleIdCompositesDelete

> realmRolesByIdRoleIdCompositesDelete(realm, roleId, roleRepresentation)

Remove a set of roles from the role’s composite

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesByIDApi();
let realm = "realm_example"; // String | realm name (not id!)
let roleId = "roleId_example"; // String | Role id
let roleRepresentation = [new KeycloakAdminRestApi.RoleRepresentation()]; // [RoleRepresentation] | A set of roles to be removed
apiInstance.realmRolesByIdRoleIdCompositesDelete(realm, roleId, roleRepresentation, (error, data, response) => {
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
 **roleId** | **String**| Role id | 
 **roleRepresentation** | [**[RoleRepresentation]**](RoleRepresentation.md)| A set of roles to be removed | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmRolesByIdRoleIdCompositesGet

> [RoleRepresentation] realmRolesByIdRoleIdCompositesGet(realm, roleId)

Get role’s children   Returns a set of role’s children provided the role is a composite.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesByIDApi();
let realm = "realm_example"; // String | realm name (not id!)
let roleId = "roleId_example"; // String | Role id
apiInstance.realmRolesByIdRoleIdCompositesGet(realm, roleId, (error, data, response) => {
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
 **roleId** | **String**| Role id | 

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmRolesByIdRoleIdCompositesPost

> realmRolesByIdRoleIdCompositesPost(realm, roleId, roleRepresentation)

Make the role a composite role by associating some child roles

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesByIDApi();
let realm = "realm_example"; // String | realm name (not id!)
let roleId = "roleId_example"; // String | Role id
let roleRepresentation = [new KeycloakAdminRestApi.RoleRepresentation()]; // [RoleRepresentation] | 
apiInstance.realmRolesByIdRoleIdCompositesPost(realm, roleId, roleRepresentation, (error, data, response) => {
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
 **roleId** | **String**| Role id | 
 **roleRepresentation** | [**[RoleRepresentation]**](RoleRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmRolesByIdRoleIdCompositesRealmGet

> [RoleRepresentation] realmRolesByIdRoleIdCompositesRealmGet(realm, roleId)

Get realm-level roles that are in the role’s composite

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesByIDApi();
let realm = "realm_example"; // String | realm name (not id!)
let roleId = "roleId_example"; // String | 
apiInstance.realmRolesByIdRoleIdCompositesRealmGet(realm, roleId, (error, data, response) => {
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
 **roleId** | **String**|  | 

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmRolesByIdRoleIdDelete

> realmRolesByIdRoleIdDelete(realm, roleId)

Delete the role

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesByIDApi();
let realm = "realm_example"; // String | realm name (not id!)
let roleId = "roleId_example"; // String | id of role
apiInstance.realmRolesByIdRoleIdDelete(realm, roleId, (error, data, response) => {
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
 **roleId** | **String**| id of role | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmRolesByIdRoleIdGet

> RoleRepresentation realmRolesByIdRoleIdGet(realm, roleId)

Get a specific role’s representation

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesByIDApi();
let realm = "realm_example"; // String | realm name (not id!)
let roleId = "roleId_example"; // String | id of role
apiInstance.realmRolesByIdRoleIdGet(realm, roleId, (error, data, response) => {
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
 **roleId** | **String**| id of role | 

### Return type

[**RoleRepresentation**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmRolesByIdRoleIdManagementPermissionsGet

> ManagementPermissionReference realmRolesByIdRoleIdManagementPermissionsGet(realm, roleId)

Return object stating whether role Authoirzation permissions have been initialized or not and a reference

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesByIDApi();
let realm = "realm_example"; // String | realm name (not id!)
let roleId = "roleId_example"; // String | 
apiInstance.realmRolesByIdRoleIdManagementPermissionsGet(realm, roleId, (error, data, response) => {
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
 **roleId** | **String**|  | 

### Return type

[**ManagementPermissionReference**](ManagementPermissionReference.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmRolesByIdRoleIdManagementPermissionsPut

> ManagementPermissionReference realmRolesByIdRoleIdManagementPermissionsPut(realm, roleId, managementPermissionReference)

Return object stating whether role Authoirzation permissions have been initialized or not and a reference

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesByIDApi();
let realm = "realm_example"; // String | realm name (not id!)
let roleId = "roleId_example"; // String | 
let managementPermissionReference = new KeycloakAdminRestApi.ManagementPermissionReference(); // ManagementPermissionReference | 
apiInstance.realmRolesByIdRoleIdManagementPermissionsPut(realm, roleId, managementPermissionReference, (error, data, response) => {
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
 **roleId** | **String**|  | 
 **managementPermissionReference** | [**ManagementPermissionReference**](ManagementPermissionReference.md)|  | 

### Return type

[**ManagementPermissionReference**](ManagementPermissionReference.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## realmRolesByIdRoleIdPut

> realmRolesByIdRoleIdPut(realm, roleId, roleRepresentation)

Update the role

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesByIDApi();
let realm = "realm_example"; // String | realm name (not id!)
let roleId = "roleId_example"; // String | id of role
let roleRepresentation = new KeycloakAdminRestApi.RoleRepresentation(); // RoleRepresentation | 
apiInstance.realmRolesByIdRoleIdPut(realm, roleId, roleRepresentation, (error, data, response) => {
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
 **roleId** | **String**| id of role | 
 **roleRepresentation** | [**RoleRepresentation**](RoleRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

