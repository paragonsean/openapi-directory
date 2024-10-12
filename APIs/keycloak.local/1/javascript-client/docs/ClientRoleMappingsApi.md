# KeycloakAdminRestApi.ClientRoleMappingsApi

All URIs are relative to *http://keycloak.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realmGroupsIdRoleMappingsClientsClientAvailableGet**](ClientRoleMappingsApi.md#realmGroupsIdRoleMappingsClientsClientAvailableGet) | **GET** /{realm}/groups/{id}/role-mappings/clients/{client}/available | Get available client-level roles that can be mapped to the user
[**realmGroupsIdRoleMappingsClientsClientCompositeGet**](ClientRoleMappingsApi.md#realmGroupsIdRoleMappingsClientsClientCompositeGet) | **GET** /{realm}/groups/{id}/role-mappings/clients/{client}/composite | Get effective client-level role mappings   This recurses any composite roles
[**realmGroupsIdRoleMappingsClientsClientDelete**](ClientRoleMappingsApi.md#realmGroupsIdRoleMappingsClientsClientDelete) | **DELETE** /{realm}/groups/{id}/role-mappings/clients/{client} | Delete client-level roles from user role mapping
[**realmGroupsIdRoleMappingsClientsClientGet**](ClientRoleMappingsApi.md#realmGroupsIdRoleMappingsClientsClientGet) | **GET** /{realm}/groups/{id}/role-mappings/clients/{client} | Get client-level role mappings for the user, and the app
[**realmGroupsIdRoleMappingsClientsClientPost**](ClientRoleMappingsApi.md#realmGroupsIdRoleMappingsClientsClientPost) | **POST** /{realm}/groups/{id}/role-mappings/clients/{client} | Add client-level roles to the user role mapping
[**realmUsersIdRoleMappingsClientsClientAvailableGet**](ClientRoleMappingsApi.md#realmUsersIdRoleMappingsClientsClientAvailableGet) | **GET** /{realm}/users/{id}/role-mappings/clients/{client}/available | Get available client-level roles that can be mapped to the user
[**realmUsersIdRoleMappingsClientsClientCompositeGet**](ClientRoleMappingsApi.md#realmUsersIdRoleMappingsClientsClientCompositeGet) | **GET** /{realm}/users/{id}/role-mappings/clients/{client}/composite | Get effective client-level role mappings   This recurses any composite roles
[**realmUsersIdRoleMappingsClientsClientDelete**](ClientRoleMappingsApi.md#realmUsersIdRoleMappingsClientsClientDelete) | **DELETE** /{realm}/users/{id}/role-mappings/clients/{client} | Delete client-level roles from user role mapping
[**realmUsersIdRoleMappingsClientsClientGet**](ClientRoleMappingsApi.md#realmUsersIdRoleMappingsClientsClientGet) | **GET** /{realm}/users/{id}/role-mappings/clients/{client} | Get client-level role mappings for the user, and the app
[**realmUsersIdRoleMappingsClientsClientPost**](ClientRoleMappingsApi.md#realmUsersIdRoleMappingsClientsClientPost) | **POST** /{realm}/users/{id}/role-mappings/clients/{client} | Add client-level roles to the user role mapping



## realmGroupsIdRoleMappingsClientsClientAvailableGet

> [RoleRepresentation] realmGroupsIdRoleMappingsClientsClientAvailableGet(realm, id, client)

Get available client-level roles that can be mapped to the user

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientRoleMappingsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | 
let client = "client_example"; // String | 
apiInstance.realmGroupsIdRoleMappingsClientsClientAvailableGet(realm, id, client, (error, data, response) => {
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
 **client** | **String**|  | 

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmGroupsIdRoleMappingsClientsClientCompositeGet

> [RoleRepresentation] realmGroupsIdRoleMappingsClientsClientCompositeGet(realm, id, client)

Get effective client-level role mappings   This recurses any composite roles

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientRoleMappingsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | 
let client = "client_example"; // String | 
apiInstance.realmGroupsIdRoleMappingsClientsClientCompositeGet(realm, id, client, (error, data, response) => {
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
 **client** | **String**|  | 

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmGroupsIdRoleMappingsClientsClientDelete

> realmGroupsIdRoleMappingsClientsClientDelete(realm, id, client, roleRepresentation)

Delete client-level roles from user role mapping

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientRoleMappingsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | 
let client = "client_example"; // String | 
let roleRepresentation = [new KeycloakAdminRestApi.RoleRepresentation()]; // [RoleRepresentation] | 
apiInstance.realmGroupsIdRoleMappingsClientsClientDelete(realm, id, client, roleRepresentation, (error, data, response) => {
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
 **client** | **String**|  | 
 **roleRepresentation** | [**[RoleRepresentation]**](RoleRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmGroupsIdRoleMappingsClientsClientGet

> [RoleRepresentation] realmGroupsIdRoleMappingsClientsClientGet(realm, id, client)

Get client-level role mappings for the user, and the app

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientRoleMappingsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | 
let client = "client_example"; // String | 
apiInstance.realmGroupsIdRoleMappingsClientsClientGet(realm, id, client, (error, data, response) => {
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
 **client** | **String**|  | 

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmGroupsIdRoleMappingsClientsClientPost

> realmGroupsIdRoleMappingsClientsClientPost(realm, id, client, roleRepresentation)

Add client-level roles to the user role mapping

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientRoleMappingsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | 
let client = "client_example"; // String | 
let roleRepresentation = [new KeycloakAdminRestApi.RoleRepresentation()]; // [RoleRepresentation] | 
apiInstance.realmGroupsIdRoleMappingsClientsClientPost(realm, id, client, roleRepresentation, (error, data, response) => {
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
 **client** | **String**|  | 
 **roleRepresentation** | [**[RoleRepresentation]**](RoleRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmUsersIdRoleMappingsClientsClientAvailableGet

> [RoleRepresentation] realmUsersIdRoleMappingsClientsClientAvailableGet(realm, id, client)

Get available client-level roles that can be mapped to the user

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientRoleMappingsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
let client = "client_example"; // String | 
apiInstance.realmUsersIdRoleMappingsClientsClientAvailableGet(realm, id, client, (error, data, response) => {
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
 **client** | **String**|  | 

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmUsersIdRoleMappingsClientsClientCompositeGet

> [RoleRepresentation] realmUsersIdRoleMappingsClientsClientCompositeGet(realm, id, client)

Get effective client-level role mappings   This recurses any composite roles

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientRoleMappingsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
let client = "client_example"; // String | 
apiInstance.realmUsersIdRoleMappingsClientsClientCompositeGet(realm, id, client, (error, data, response) => {
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
 **client** | **String**|  | 

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmUsersIdRoleMappingsClientsClientDelete

> realmUsersIdRoleMappingsClientsClientDelete(realm, id, client, roleRepresentation)

Delete client-level roles from user role mapping

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientRoleMappingsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
let client = "client_example"; // String | 
let roleRepresentation = [new KeycloakAdminRestApi.RoleRepresentation()]; // [RoleRepresentation] | 
apiInstance.realmUsersIdRoleMappingsClientsClientDelete(realm, id, client, roleRepresentation, (error, data, response) => {
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
 **client** | **String**|  | 
 **roleRepresentation** | [**[RoleRepresentation]**](RoleRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmUsersIdRoleMappingsClientsClientGet

> [RoleRepresentation] realmUsersIdRoleMappingsClientsClientGet(realm, id, client)

Get client-level role mappings for the user, and the app

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientRoleMappingsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
let client = "client_example"; // String | 
apiInstance.realmUsersIdRoleMappingsClientsClientGet(realm, id, client, (error, data, response) => {
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
 **client** | **String**|  | 

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmUsersIdRoleMappingsClientsClientPost

> realmUsersIdRoleMappingsClientsClientPost(realm, id, client, roleRepresentation)

Add client-level roles to the user role mapping

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientRoleMappingsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | User id
let client = "client_example"; // String | 
let roleRepresentation = [new KeycloakAdminRestApi.RoleRepresentation()]; // [RoleRepresentation] | 
apiInstance.realmUsersIdRoleMappingsClientsClientPost(realm, id, client, roleRepresentation, (error, data, response) => {
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
 **client** | **String**|  | 
 **roleRepresentation** | [**[RoleRepresentation]**](RoleRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

