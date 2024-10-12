# KeycloakAdminRestApi.RolesApi

All URIs are relative to *http://keycloak.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realmClientsIdRolesGet**](RolesApi.md#realmClientsIdRolesGet) | **GET** /{realm}/clients/{id}/roles | Get all roles for the realm or client
[**realmClientsIdRolesPost**](RolesApi.md#realmClientsIdRolesPost) | **POST** /{realm}/clients/{id}/roles | Create a new role for the realm or client
[**realmClientsIdRolesRoleNameCompositesClientsClientGet**](RolesApi.md#realmClientsIdRolesRoleNameCompositesClientsClientGet) | **GET** /{realm}/clients/{id}/roles/{role-name}/composites/clients/{client} | An app-level roles for the specified app for the role’s composite
[**realmClientsIdRolesRoleNameCompositesDelete**](RolesApi.md#realmClientsIdRolesRoleNameCompositesDelete) | **DELETE** /{realm}/clients/{id}/roles/{role-name}/composites | Remove roles from the role’s composite
[**realmClientsIdRolesRoleNameCompositesGet**](RolesApi.md#realmClientsIdRolesRoleNameCompositesGet) | **GET** /{realm}/clients/{id}/roles/{role-name}/composites | Get composites of the role
[**realmClientsIdRolesRoleNameCompositesPost**](RolesApi.md#realmClientsIdRolesRoleNameCompositesPost) | **POST** /{realm}/clients/{id}/roles/{role-name}/composites | Add a composite to the role
[**realmClientsIdRolesRoleNameCompositesRealmGet**](RolesApi.md#realmClientsIdRolesRoleNameCompositesRealmGet) | **GET** /{realm}/clients/{id}/roles/{role-name}/composites/realm | Get realm-level roles of the role’s composite
[**realmClientsIdRolesRoleNameDelete**](RolesApi.md#realmClientsIdRolesRoleNameDelete) | **DELETE** /{realm}/clients/{id}/roles/{role-name} | Delete a role by name
[**realmClientsIdRolesRoleNameGet**](RolesApi.md#realmClientsIdRolesRoleNameGet) | **GET** /{realm}/clients/{id}/roles/{role-name} | Get a role by name
[**realmClientsIdRolesRoleNameGroupsGet**](RolesApi.md#realmClientsIdRolesRoleNameGroupsGet) | **GET** /{realm}/clients/{id}/roles/{role-name}/groups | Return List of Groups that have the specified role name
[**realmClientsIdRolesRoleNameManagementPermissionsGet**](RolesApi.md#realmClientsIdRolesRoleNameManagementPermissionsGet) | **GET** /{realm}/clients/{id}/roles/{role-name}/management/permissions | Return object stating whether role Authoirzation permissions have been initialized or not and a reference
[**realmClientsIdRolesRoleNameManagementPermissionsPut**](RolesApi.md#realmClientsIdRolesRoleNameManagementPermissionsPut) | **PUT** /{realm}/clients/{id}/roles/{role-name}/management/permissions | Return object stating whether role Authoirzation permissions have been initialized or not and a reference
[**realmClientsIdRolesRoleNamePut**](RolesApi.md#realmClientsIdRolesRoleNamePut) | **PUT** /{realm}/clients/{id}/roles/{role-name} | Update a role by name
[**realmClientsIdRolesRoleNameUsersGet**](RolesApi.md#realmClientsIdRolesRoleNameUsersGet) | **GET** /{realm}/clients/{id}/roles/{role-name}/users | Return List of Users that have the specified role name
[**realmRolesGet**](RolesApi.md#realmRolesGet) | **GET** /{realm}/roles | Get all roles for the realm or client
[**realmRolesPost**](RolesApi.md#realmRolesPost) | **POST** /{realm}/roles | Create a new role for the realm or client
[**realmRolesRoleNameCompositesClientsClientGet**](RolesApi.md#realmRolesRoleNameCompositesClientsClientGet) | **GET** /{realm}/roles/{role-name}/composites/clients/{client} | An app-level roles for the specified app for the role’s composite
[**realmRolesRoleNameCompositesDelete**](RolesApi.md#realmRolesRoleNameCompositesDelete) | **DELETE** /{realm}/roles/{role-name}/composites | Remove roles from the role’s composite
[**realmRolesRoleNameCompositesGet**](RolesApi.md#realmRolesRoleNameCompositesGet) | **GET** /{realm}/roles/{role-name}/composites | Get composites of the role
[**realmRolesRoleNameCompositesPost**](RolesApi.md#realmRolesRoleNameCompositesPost) | **POST** /{realm}/roles/{role-name}/composites | Add a composite to the role
[**realmRolesRoleNameCompositesRealmGet**](RolesApi.md#realmRolesRoleNameCompositesRealmGet) | **GET** /{realm}/roles/{role-name}/composites/realm | Get realm-level roles of the role’s composite
[**realmRolesRoleNameDelete**](RolesApi.md#realmRolesRoleNameDelete) | **DELETE** /{realm}/roles/{role-name} | Delete a role by name
[**realmRolesRoleNameGet**](RolesApi.md#realmRolesRoleNameGet) | **GET** /{realm}/roles/{role-name} | Get a role by name
[**realmRolesRoleNameGroupsGet**](RolesApi.md#realmRolesRoleNameGroupsGet) | **GET** /{realm}/roles/{role-name}/groups | Return List of Groups that have the specified role name
[**realmRolesRoleNameManagementPermissionsGet**](RolesApi.md#realmRolesRoleNameManagementPermissionsGet) | **GET** /{realm}/roles/{role-name}/management/permissions | Return object stating whether role Authoirzation permissions have been initialized or not and a reference
[**realmRolesRoleNameManagementPermissionsPut**](RolesApi.md#realmRolesRoleNameManagementPermissionsPut) | **PUT** /{realm}/roles/{role-name}/management/permissions | Return object stating whether role Authoirzation permissions have been initialized or not and a reference
[**realmRolesRoleNamePut**](RolesApi.md#realmRolesRoleNamePut) | **PUT** /{realm}/roles/{role-name} | Update a role by name
[**realmRolesRoleNameUsersGet**](RolesApi.md#realmRolesRoleNameUsersGet) | **GET** /{realm}/roles/{role-name}/users | Return List of Users that have the specified role name



## realmClientsIdRolesGet

> [RoleRepresentation] realmClientsIdRolesGet(realm, id, opts)

Get all roles for the realm or client

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let opts = {
  'briefRepresentation': true, // Boolean | 
  'first': 56, // Number | 
  'max': 56, // Number | 
  'search': "search_example" // String | 
};
apiInstance.realmClientsIdRolesGet(realm, id, opts, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 
 **briefRepresentation** | **Boolean**|  | [optional] 
 **first** | **Number**|  | [optional] 
 **max** | **Number**|  | [optional] 
 **search** | **String**|  | [optional] 

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdRolesPost

> realmClientsIdRolesPost(realm, id, roleRepresentation)

Create a new role for the realm or client

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let roleRepresentation = new KeycloakAdminRestApi.RoleRepresentation(); // RoleRepresentation | 
apiInstance.realmClientsIdRolesPost(realm, id, roleRepresentation, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 
 **roleRepresentation** | [**RoleRepresentation**](RoleRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmClientsIdRolesRoleNameCompositesClientsClientGet

> [RoleRepresentation] realmClientsIdRolesRoleNameCompositesClientsClientGet(realm, id, roleName, client)

An app-level roles for the specified app for the role’s composite

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let roleName = "roleName_example"; // String | role’s name (not id!)
let client = "client_example"; // String | 
apiInstance.realmClientsIdRolesRoleNameCompositesClientsClientGet(realm, id, roleName, client, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 
 **roleName** | **String**| role’s name (not id!) | 
 **client** | **String**|  | 

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdRolesRoleNameCompositesDelete

> realmClientsIdRolesRoleNameCompositesDelete(realm, id, roleName, roleRepresentation)

Remove roles from the role’s composite

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let roleName = "roleName_example"; // String | role’s name (not id!)
let roleRepresentation = [new KeycloakAdminRestApi.RoleRepresentation()]; // [RoleRepresentation] | roles to remove
apiInstance.realmClientsIdRolesRoleNameCompositesDelete(realm, id, roleName, roleRepresentation, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 
 **roleName** | **String**| role’s name (not id!) | 
 **roleRepresentation** | [**[RoleRepresentation]**](RoleRepresentation.md)| roles to remove | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmClientsIdRolesRoleNameCompositesGet

> [RoleRepresentation] realmClientsIdRolesRoleNameCompositesGet(realm, id, roleName)

Get composites of the role

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let roleName = "roleName_example"; // String | role’s name (not id!)
apiInstance.realmClientsIdRolesRoleNameCompositesGet(realm, id, roleName, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 
 **roleName** | **String**| role’s name (not id!) | 

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdRolesRoleNameCompositesPost

> realmClientsIdRolesRoleNameCompositesPost(realm, id, roleName, roleRepresentation)

Add a composite to the role

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let roleName = "roleName_example"; // String | role’s name (not id!)
let roleRepresentation = [new KeycloakAdminRestApi.RoleRepresentation()]; // [RoleRepresentation] | 
apiInstance.realmClientsIdRolesRoleNameCompositesPost(realm, id, roleName, roleRepresentation, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 
 **roleName** | **String**| role’s name (not id!) | 
 **roleRepresentation** | [**[RoleRepresentation]**](RoleRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmClientsIdRolesRoleNameCompositesRealmGet

> [RoleRepresentation] realmClientsIdRolesRoleNameCompositesRealmGet(realm, id, roleName)

Get realm-level roles of the role’s composite

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let roleName = "roleName_example"; // String | role’s name (not id!)
apiInstance.realmClientsIdRolesRoleNameCompositesRealmGet(realm, id, roleName, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 
 **roleName** | **String**| role’s name (not id!) | 

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdRolesRoleNameDelete

> realmClientsIdRolesRoleNameDelete(realm, id, roleName)

Delete a role by name

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let roleName = "roleName_example"; // String | role’s name (not id!)
apiInstance.realmClientsIdRolesRoleNameDelete(realm, id, roleName, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 
 **roleName** | **String**| role’s name (not id!) | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmClientsIdRolesRoleNameGet

> RoleRepresentation realmClientsIdRolesRoleNameGet(realm, id, roleName)

Get a role by name

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let roleName = "roleName_example"; // String | role’s name (not id!)
apiInstance.realmClientsIdRolesRoleNameGet(realm, id, roleName, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 
 **roleName** | **String**| role’s name (not id!) | 

### Return type

[**RoleRepresentation**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdRolesRoleNameGroupsGet

> [GroupRepresentation] realmClientsIdRolesRoleNameGroupsGet(realm, id, roleName, opts)

Return List of Groups that have the specified role name

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let roleName = "roleName_example"; // String | 
let opts = {
  'briefRepresentation': true, // Boolean | if false, return a full representation of the GroupRepresentation objects
  'first': 56, // Number | 
  'max': 56 // Number | 
};
apiInstance.realmClientsIdRolesRoleNameGroupsGet(realm, id, roleName, opts, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 
 **roleName** | **String**|  | 
 **briefRepresentation** | **Boolean**| if false, return a full representation of the GroupRepresentation objects | [optional] 
 **first** | **Number**|  | [optional] 
 **max** | **Number**|  | [optional] 

### Return type

[**[GroupRepresentation]**](GroupRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdRolesRoleNameManagementPermissionsGet

> ManagementPermissionReference realmClientsIdRolesRoleNameManagementPermissionsGet(realm, id, roleName)

Return object stating whether role Authoirzation permissions have been initialized or not and a reference

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let roleName = "roleName_example"; // String | 
apiInstance.realmClientsIdRolesRoleNameManagementPermissionsGet(realm, id, roleName, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 
 **roleName** | **String**|  | 

### Return type

[**ManagementPermissionReference**](ManagementPermissionReference.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdRolesRoleNameManagementPermissionsPut

> ManagementPermissionReference realmClientsIdRolesRoleNameManagementPermissionsPut(realm, id, roleName, managementPermissionReference)

Return object stating whether role Authoirzation permissions have been initialized or not and a reference

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let roleName = "roleName_example"; // String | 
let managementPermissionReference = new KeycloakAdminRestApi.ManagementPermissionReference(); // ManagementPermissionReference | 
apiInstance.realmClientsIdRolesRoleNameManagementPermissionsPut(realm, id, roleName, managementPermissionReference, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 
 **roleName** | **String**|  | 
 **managementPermissionReference** | [**ManagementPermissionReference**](ManagementPermissionReference.md)|  | 

### Return type

[**ManagementPermissionReference**](ManagementPermissionReference.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## realmClientsIdRolesRoleNamePut

> realmClientsIdRolesRoleNamePut(realm, id, roleName, roleRepresentation)

Update a role by name

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let roleName = "roleName_example"; // String | role’s name (not id!)
let roleRepresentation = new KeycloakAdminRestApi.RoleRepresentation(); // RoleRepresentation | 
apiInstance.realmClientsIdRolesRoleNamePut(realm, id, roleName, roleRepresentation, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 
 **roleName** | **String**| role’s name (not id!) | 
 **roleRepresentation** | [**RoleRepresentation**](RoleRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmClientsIdRolesRoleNameUsersGet

> [UserRepresentation] realmClientsIdRolesRoleNameUsersGet(realm, id, roleName, opts)

Return List of Users that have the specified role name

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let roleName = "roleName_example"; // String | 
let opts = {
  'first': 56, // Number | 
  'max': 56 // Number | 
};
apiInstance.realmClientsIdRolesRoleNameUsersGet(realm, id, roleName, opts, (error, data, response) => {
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
 **id** | **String**| id of client (not client-id) | 
 **roleName** | **String**|  | 
 **first** | **Number**|  | [optional] 
 **max** | **Number**|  | [optional] 

### Return type

[**[UserRepresentation]**](UserRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmRolesGet

> [RoleRepresentation] realmRolesGet(realm, opts)

Get all roles for the realm or client

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesApi();
let realm = "realm_example"; // String | realm name (not id!)
let opts = {
  'briefRepresentation': true, // Boolean | 
  'first': 56, // Number | 
  'max': 56, // Number | 
  'search': "search_example" // String | 
};
apiInstance.realmRolesGet(realm, opts, (error, data, response) => {
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

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmRolesPost

> realmRolesPost(realm, roleRepresentation)

Create a new role for the realm or client

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesApi();
let realm = "realm_example"; // String | realm name (not id!)
let roleRepresentation = new KeycloakAdminRestApi.RoleRepresentation(); // RoleRepresentation | 
apiInstance.realmRolesPost(realm, roleRepresentation, (error, data, response) => {
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
 **roleRepresentation** | [**RoleRepresentation**](RoleRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmRolesRoleNameCompositesClientsClientGet

> [RoleRepresentation] realmRolesRoleNameCompositesClientsClientGet(realm, roleName, client)

An app-level roles for the specified app for the role’s composite

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesApi();
let realm = "realm_example"; // String | realm name (not id!)
let roleName = "roleName_example"; // String | role’s name (not id!)
let client = "client_example"; // String | 
apiInstance.realmRolesRoleNameCompositesClientsClientGet(realm, roleName, client, (error, data, response) => {
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
 **roleName** | **String**| role’s name (not id!) | 
 **client** | **String**|  | 

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmRolesRoleNameCompositesDelete

> realmRolesRoleNameCompositesDelete(realm, roleName, roleRepresentation)

Remove roles from the role’s composite

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesApi();
let realm = "realm_example"; // String | realm name (not id!)
let roleName = "roleName_example"; // String | role’s name (not id!)
let roleRepresentation = [new KeycloakAdminRestApi.RoleRepresentation()]; // [RoleRepresentation] | roles to remove
apiInstance.realmRolesRoleNameCompositesDelete(realm, roleName, roleRepresentation, (error, data, response) => {
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
 **roleName** | **String**| role’s name (not id!) | 
 **roleRepresentation** | [**[RoleRepresentation]**](RoleRepresentation.md)| roles to remove | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmRolesRoleNameCompositesGet

> [RoleRepresentation] realmRolesRoleNameCompositesGet(realm, roleName)

Get composites of the role

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesApi();
let realm = "realm_example"; // String | realm name (not id!)
let roleName = "roleName_example"; // String | role’s name (not id!)
apiInstance.realmRolesRoleNameCompositesGet(realm, roleName, (error, data, response) => {
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
 **roleName** | **String**| role’s name (not id!) | 

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmRolesRoleNameCompositesPost

> realmRolesRoleNameCompositesPost(realm, roleName, roleRepresentation)

Add a composite to the role

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesApi();
let realm = "realm_example"; // String | realm name (not id!)
let roleName = "roleName_example"; // String | role’s name (not id!)
let roleRepresentation = [new KeycloakAdminRestApi.RoleRepresentation()]; // [RoleRepresentation] | 
apiInstance.realmRolesRoleNameCompositesPost(realm, roleName, roleRepresentation, (error, data, response) => {
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
 **roleName** | **String**| role’s name (not id!) | 
 **roleRepresentation** | [**[RoleRepresentation]**](RoleRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmRolesRoleNameCompositesRealmGet

> [RoleRepresentation] realmRolesRoleNameCompositesRealmGet(realm, roleName)

Get realm-level roles of the role’s composite

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesApi();
let realm = "realm_example"; // String | realm name (not id!)
let roleName = "roleName_example"; // String | role’s name (not id!)
apiInstance.realmRolesRoleNameCompositesRealmGet(realm, roleName, (error, data, response) => {
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
 **roleName** | **String**| role’s name (not id!) | 

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmRolesRoleNameDelete

> realmRolesRoleNameDelete(realm, roleName)

Delete a role by name

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesApi();
let realm = "realm_example"; // String | realm name (not id!)
let roleName = "roleName_example"; // String | role’s name (not id!)
apiInstance.realmRolesRoleNameDelete(realm, roleName, (error, data, response) => {
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
 **roleName** | **String**| role’s name (not id!) | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmRolesRoleNameGet

> RoleRepresentation realmRolesRoleNameGet(realm, roleName)

Get a role by name

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesApi();
let realm = "realm_example"; // String | realm name (not id!)
let roleName = "roleName_example"; // String | role’s name (not id!)
apiInstance.realmRolesRoleNameGet(realm, roleName, (error, data, response) => {
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
 **roleName** | **String**| role’s name (not id!) | 

### Return type

[**RoleRepresentation**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmRolesRoleNameGroupsGet

> [GroupRepresentation] realmRolesRoleNameGroupsGet(realm, roleName, opts)

Return List of Groups that have the specified role name

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesApi();
let realm = "realm_example"; // String | realm name (not id!)
let roleName = "roleName_example"; // String | 
let opts = {
  'briefRepresentation': true, // Boolean | if false, return a full representation of the GroupRepresentation objects
  'first': 56, // Number | 
  'max': 56 // Number | 
};
apiInstance.realmRolesRoleNameGroupsGet(realm, roleName, opts, (error, data, response) => {
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
 **roleName** | **String**|  | 
 **briefRepresentation** | **Boolean**| if false, return a full representation of the GroupRepresentation objects | [optional] 
 **first** | **Number**|  | [optional] 
 **max** | **Number**|  | [optional] 

### Return type

[**[GroupRepresentation]**](GroupRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmRolesRoleNameManagementPermissionsGet

> ManagementPermissionReference realmRolesRoleNameManagementPermissionsGet(realm, roleName)

Return object stating whether role Authoirzation permissions have been initialized or not and a reference

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesApi();
let realm = "realm_example"; // String | realm name (not id!)
let roleName = "roleName_example"; // String | 
apiInstance.realmRolesRoleNameManagementPermissionsGet(realm, roleName, (error, data, response) => {
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
 **roleName** | **String**|  | 

### Return type

[**ManagementPermissionReference**](ManagementPermissionReference.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmRolesRoleNameManagementPermissionsPut

> ManagementPermissionReference realmRolesRoleNameManagementPermissionsPut(realm, roleName, managementPermissionReference)

Return object stating whether role Authoirzation permissions have been initialized or not and a reference

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesApi();
let realm = "realm_example"; // String | realm name (not id!)
let roleName = "roleName_example"; // String | 
let managementPermissionReference = new KeycloakAdminRestApi.ManagementPermissionReference(); // ManagementPermissionReference | 
apiInstance.realmRolesRoleNameManagementPermissionsPut(realm, roleName, managementPermissionReference, (error, data, response) => {
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
 **roleName** | **String**|  | 
 **managementPermissionReference** | [**ManagementPermissionReference**](ManagementPermissionReference.md)|  | 

### Return type

[**ManagementPermissionReference**](ManagementPermissionReference.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## realmRolesRoleNamePut

> realmRolesRoleNamePut(realm, roleName, roleRepresentation)

Update a role by name

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesApi();
let realm = "realm_example"; // String | realm name (not id!)
let roleName = "roleName_example"; // String | role’s name (not id!)
let roleRepresentation = new KeycloakAdminRestApi.RoleRepresentation(); // RoleRepresentation | 
apiInstance.realmRolesRoleNamePut(realm, roleName, roleRepresentation, (error, data, response) => {
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
 **roleName** | **String**| role’s name (not id!) | 
 **roleRepresentation** | [**RoleRepresentation**](RoleRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmRolesRoleNameUsersGet

> [UserRepresentation] realmRolesRoleNameUsersGet(realm, roleName, opts)

Return List of Users that have the specified role name

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.RolesApi();
let realm = "realm_example"; // String | realm name (not id!)
let roleName = "roleName_example"; // String | 
let opts = {
  'first': 56, // Number | 
  'max': 56 // Number | 
};
apiInstance.realmRolesRoleNameUsersGet(realm, roleName, opts, (error, data, response) => {
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
 **roleName** | **String**|  | 
 **first** | **Number**|  | [optional] 
 **max** | **Number**|  | [optional] 

### Return type

[**[UserRepresentation]**](UserRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

