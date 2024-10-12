# KeycloakAdminRestApi.ScopeMappingsApi

All URIs are relative to *http://keycloak.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realmClientScopesIdScopeMappingsClientsClientAvailableGet**](ScopeMappingsApi.md#realmClientScopesIdScopeMappingsClientsClientAvailableGet) | **GET** /{realm}/client-scopes/{id}/scope-mappings/clients/{client}/available | The available client-level roles   Returns the roles for the client that can be associated with the client’s scope
[**realmClientScopesIdScopeMappingsClientsClientCompositeGet**](ScopeMappingsApi.md#realmClientScopesIdScopeMappingsClientsClientCompositeGet) | **GET** /{realm}/client-scopes/{id}/scope-mappings/clients/{client}/composite | Get effective client roles   Returns the roles for the client that are associated with the client’s scope.
[**realmClientScopesIdScopeMappingsClientsClientDelete**](ScopeMappingsApi.md#realmClientScopesIdScopeMappingsClientsClientDelete) | **DELETE** /{realm}/client-scopes/{id}/scope-mappings/clients/{client} | Remove client-level roles from the client’s scope.
[**realmClientScopesIdScopeMappingsClientsClientGet**](ScopeMappingsApi.md#realmClientScopesIdScopeMappingsClientsClientGet) | **GET** /{realm}/client-scopes/{id}/scope-mappings/clients/{client} | Get the roles associated with a client’s scope   Returns roles for the client.
[**realmClientScopesIdScopeMappingsClientsClientPost**](ScopeMappingsApi.md#realmClientScopesIdScopeMappingsClientsClientPost) | **POST** /{realm}/client-scopes/{id}/scope-mappings/clients/{client} | Add client-level roles to the client’s scope
[**realmClientScopesIdScopeMappingsGet**](ScopeMappingsApi.md#realmClientScopesIdScopeMappingsGet) | **GET** /{realm}/client-scopes/{id}/scope-mappings | Get all scope mappings for the client
[**realmClientScopesIdScopeMappingsRealmAvailableGet**](ScopeMappingsApi.md#realmClientScopesIdScopeMappingsRealmAvailableGet) | **GET** /{realm}/client-scopes/{id}/scope-mappings/realm/available | Get realm-level roles that are available to attach to this client’s scope
[**realmClientScopesIdScopeMappingsRealmCompositeGet**](ScopeMappingsApi.md#realmClientScopesIdScopeMappingsRealmCompositeGet) | **GET** /{realm}/client-scopes/{id}/scope-mappings/realm/composite | Get effective realm-level roles associated with the client’s scope   What this does is recurse  any composite roles associated with the client’s scope and adds the roles to this lists.
[**realmClientScopesIdScopeMappingsRealmDelete**](ScopeMappingsApi.md#realmClientScopesIdScopeMappingsRealmDelete) | **DELETE** /{realm}/client-scopes/{id}/scope-mappings/realm | Remove a set of realm-level roles from the client’s scope
[**realmClientScopesIdScopeMappingsRealmGet**](ScopeMappingsApi.md#realmClientScopesIdScopeMappingsRealmGet) | **GET** /{realm}/client-scopes/{id}/scope-mappings/realm | Get realm-level roles associated with the client’s scope
[**realmClientScopesIdScopeMappingsRealmPost**](ScopeMappingsApi.md#realmClientScopesIdScopeMappingsRealmPost) | **POST** /{realm}/client-scopes/{id}/scope-mappings/realm | Add a set of realm-level roles to the client’s scope
[**realmClientsIdScopeMappingsClientsClientAvailableGet**](ScopeMappingsApi.md#realmClientsIdScopeMappingsClientsClientAvailableGet) | **GET** /{realm}/clients/{id}/scope-mappings/clients/{client}/available | The available client-level roles   Returns the roles for the client that can be associated with the client’s scope
[**realmClientsIdScopeMappingsClientsClientCompositeGet**](ScopeMappingsApi.md#realmClientsIdScopeMappingsClientsClientCompositeGet) | **GET** /{realm}/clients/{id}/scope-mappings/clients/{client}/composite | Get effective client roles   Returns the roles for the client that are associated with the client’s scope.
[**realmClientsIdScopeMappingsClientsClientDelete**](ScopeMappingsApi.md#realmClientsIdScopeMappingsClientsClientDelete) | **DELETE** /{realm}/clients/{id}/scope-mappings/clients/{client} | Remove client-level roles from the client’s scope.
[**realmClientsIdScopeMappingsClientsClientGet**](ScopeMappingsApi.md#realmClientsIdScopeMappingsClientsClientGet) | **GET** /{realm}/clients/{id}/scope-mappings/clients/{client} | Get the roles associated with a client’s scope   Returns roles for the client.
[**realmClientsIdScopeMappingsClientsClientPost**](ScopeMappingsApi.md#realmClientsIdScopeMappingsClientsClientPost) | **POST** /{realm}/clients/{id}/scope-mappings/clients/{client} | Add client-level roles to the client’s scope
[**realmClientsIdScopeMappingsGet**](ScopeMappingsApi.md#realmClientsIdScopeMappingsGet) | **GET** /{realm}/clients/{id}/scope-mappings | Get all scope mappings for the client
[**realmClientsIdScopeMappingsRealmAvailableGet**](ScopeMappingsApi.md#realmClientsIdScopeMappingsRealmAvailableGet) | **GET** /{realm}/clients/{id}/scope-mappings/realm/available | Get realm-level roles that are available to attach to this client’s scope
[**realmClientsIdScopeMappingsRealmCompositeGet**](ScopeMappingsApi.md#realmClientsIdScopeMappingsRealmCompositeGet) | **GET** /{realm}/clients/{id}/scope-mappings/realm/composite | Get effective realm-level roles associated with the client’s scope   What this does is recurse  any composite roles associated with the client’s scope and adds the roles to this lists.
[**realmClientsIdScopeMappingsRealmDelete**](ScopeMappingsApi.md#realmClientsIdScopeMappingsRealmDelete) | **DELETE** /{realm}/clients/{id}/scope-mappings/realm | Remove a set of realm-level roles from the client’s scope
[**realmClientsIdScopeMappingsRealmGet**](ScopeMappingsApi.md#realmClientsIdScopeMappingsRealmGet) | **GET** /{realm}/clients/{id}/scope-mappings/realm | Get realm-level roles associated with the client’s scope
[**realmClientsIdScopeMappingsRealmPost**](ScopeMappingsApi.md#realmClientsIdScopeMappingsRealmPost) | **POST** /{realm}/clients/{id}/scope-mappings/realm | Add a set of realm-level roles to the client’s scope



## realmClientScopesIdScopeMappingsClientsClientAvailableGet

> [RoleRepresentation] realmClientScopesIdScopeMappingsClientsClientAvailableGet(realm, id, client)

The available client-level roles   Returns the roles for the client that can be associated with the client’s scope

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ScopeMappingsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client scope (not name)
let client = "client_example"; // String | 
apiInstance.realmClientScopesIdScopeMappingsClientsClientAvailableGet(realm, id, client, (error, data, response) => {
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
 **id** | **String**| id of client scope (not name) | 
 **client** | **String**|  | 

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientScopesIdScopeMappingsClientsClientCompositeGet

> [RoleRepresentation] realmClientScopesIdScopeMappingsClientsClientCompositeGet(realm, id, client)

Get effective client roles   Returns the roles for the client that are associated with the client’s scope.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ScopeMappingsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client scope (not name)
let client = "client_example"; // String | 
apiInstance.realmClientScopesIdScopeMappingsClientsClientCompositeGet(realm, id, client, (error, data, response) => {
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
 **id** | **String**| id of client scope (not name) | 
 **client** | **String**|  | 

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientScopesIdScopeMappingsClientsClientDelete

> realmClientScopesIdScopeMappingsClientsClientDelete(realm, id, client, roleRepresentation)

Remove client-level roles from the client’s scope.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ScopeMappingsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client scope (not name)
let client = "client_example"; // String | 
let roleRepresentation = [new KeycloakAdminRestApi.RoleRepresentation()]; // [RoleRepresentation] | 
apiInstance.realmClientScopesIdScopeMappingsClientsClientDelete(realm, id, client, roleRepresentation, (error, data, response) => {
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
 **id** | **String**| id of client scope (not name) | 
 **client** | **String**|  | 
 **roleRepresentation** | [**[RoleRepresentation]**](RoleRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmClientScopesIdScopeMappingsClientsClientGet

> [RoleRepresentation] realmClientScopesIdScopeMappingsClientsClientGet(realm, id, client)

Get the roles associated with a client’s scope   Returns roles for the client.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ScopeMappingsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client scope (not name)
let client = "client_example"; // String | 
apiInstance.realmClientScopesIdScopeMappingsClientsClientGet(realm, id, client, (error, data, response) => {
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
 **id** | **String**| id of client scope (not name) | 
 **client** | **String**|  | 

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientScopesIdScopeMappingsClientsClientPost

> realmClientScopesIdScopeMappingsClientsClientPost(realm, id, client, roleRepresentation)

Add client-level roles to the client’s scope

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ScopeMappingsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client scope (not name)
let client = "client_example"; // String | 
let roleRepresentation = [new KeycloakAdminRestApi.RoleRepresentation()]; // [RoleRepresentation] | 
apiInstance.realmClientScopesIdScopeMappingsClientsClientPost(realm, id, client, roleRepresentation, (error, data, response) => {
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
 **id** | **String**| id of client scope (not name) | 
 **client** | **String**|  | 
 **roleRepresentation** | [**[RoleRepresentation]**](RoleRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmClientScopesIdScopeMappingsGet

> MappingsRepresentation realmClientScopesIdScopeMappingsGet(realm, id)

Get all scope mappings for the client

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ScopeMappingsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client scope (not name)
apiInstance.realmClientScopesIdScopeMappingsGet(realm, id, (error, data, response) => {
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
 **id** | **String**| id of client scope (not name) | 

### Return type

[**MappingsRepresentation**](MappingsRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientScopesIdScopeMappingsRealmAvailableGet

> [RoleRepresentation] realmClientScopesIdScopeMappingsRealmAvailableGet(realm, id)

Get realm-level roles that are available to attach to this client’s scope

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ScopeMappingsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client scope (not name)
apiInstance.realmClientScopesIdScopeMappingsRealmAvailableGet(realm, id, (error, data, response) => {
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
 **id** | **String**| id of client scope (not name) | 

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientScopesIdScopeMappingsRealmCompositeGet

> [RoleRepresentation] realmClientScopesIdScopeMappingsRealmCompositeGet(realm, id)

Get effective realm-level roles associated with the client’s scope   What this does is recurse  any composite roles associated with the client’s scope and adds the roles to this lists.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ScopeMappingsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client scope (not name)
apiInstance.realmClientScopesIdScopeMappingsRealmCompositeGet(realm, id, (error, data, response) => {
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
 **id** | **String**| id of client scope (not name) | 

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientScopesIdScopeMappingsRealmDelete

> realmClientScopesIdScopeMappingsRealmDelete(realm, id, roleRepresentation)

Remove a set of realm-level roles from the client’s scope

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ScopeMappingsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client scope (not name)
let roleRepresentation = [new KeycloakAdminRestApi.RoleRepresentation()]; // [RoleRepresentation] | 
apiInstance.realmClientScopesIdScopeMappingsRealmDelete(realm, id, roleRepresentation, (error, data, response) => {
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
 **id** | **String**| id of client scope (not name) | 
 **roleRepresentation** | [**[RoleRepresentation]**](RoleRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmClientScopesIdScopeMappingsRealmGet

> [RoleRepresentation] realmClientScopesIdScopeMappingsRealmGet(realm, id)

Get realm-level roles associated with the client’s scope

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ScopeMappingsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client scope (not name)
apiInstance.realmClientScopesIdScopeMappingsRealmGet(realm, id, (error, data, response) => {
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
 **id** | **String**| id of client scope (not name) | 

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientScopesIdScopeMappingsRealmPost

> realmClientScopesIdScopeMappingsRealmPost(realm, id, roleRepresentation)

Add a set of realm-level roles to the client’s scope

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ScopeMappingsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client scope (not name)
let roleRepresentation = [new KeycloakAdminRestApi.RoleRepresentation()]; // [RoleRepresentation] | 
apiInstance.realmClientScopesIdScopeMappingsRealmPost(realm, id, roleRepresentation, (error, data, response) => {
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
 **id** | **String**| id of client scope (not name) | 
 **roleRepresentation** | [**[RoleRepresentation]**](RoleRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmClientsIdScopeMappingsClientsClientAvailableGet

> [RoleRepresentation] realmClientsIdScopeMappingsClientsClientAvailableGet(realm, id, client)

The available client-level roles   Returns the roles for the client that can be associated with the client’s scope

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ScopeMappingsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let client = "client_example"; // String | 
apiInstance.realmClientsIdScopeMappingsClientsClientAvailableGet(realm, id, client, (error, data, response) => {
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
 **client** | **String**|  | 

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdScopeMappingsClientsClientCompositeGet

> [RoleRepresentation] realmClientsIdScopeMappingsClientsClientCompositeGet(realm, id, client)

Get effective client roles   Returns the roles for the client that are associated with the client’s scope.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ScopeMappingsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let client = "client_example"; // String | 
apiInstance.realmClientsIdScopeMappingsClientsClientCompositeGet(realm, id, client, (error, data, response) => {
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
 **client** | **String**|  | 

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdScopeMappingsClientsClientDelete

> realmClientsIdScopeMappingsClientsClientDelete(realm, id, client, roleRepresentation)

Remove client-level roles from the client’s scope.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ScopeMappingsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let client = "client_example"; // String | 
let roleRepresentation = [new KeycloakAdminRestApi.RoleRepresentation()]; // [RoleRepresentation] | 
apiInstance.realmClientsIdScopeMappingsClientsClientDelete(realm, id, client, roleRepresentation, (error, data, response) => {
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
 **client** | **String**|  | 
 **roleRepresentation** | [**[RoleRepresentation]**](RoleRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmClientsIdScopeMappingsClientsClientGet

> [RoleRepresentation] realmClientsIdScopeMappingsClientsClientGet(realm, id, client)

Get the roles associated with a client’s scope   Returns roles for the client.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ScopeMappingsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let client = "client_example"; // String | 
apiInstance.realmClientsIdScopeMappingsClientsClientGet(realm, id, client, (error, data, response) => {
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
 **client** | **String**|  | 

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdScopeMappingsClientsClientPost

> realmClientsIdScopeMappingsClientsClientPost(realm, id, client, roleRepresentation)

Add client-level roles to the client’s scope

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ScopeMappingsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let client = "client_example"; // String | 
let roleRepresentation = [new KeycloakAdminRestApi.RoleRepresentation()]; // [RoleRepresentation] | 
apiInstance.realmClientsIdScopeMappingsClientsClientPost(realm, id, client, roleRepresentation, (error, data, response) => {
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
 **client** | **String**|  | 
 **roleRepresentation** | [**[RoleRepresentation]**](RoleRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmClientsIdScopeMappingsGet

> MappingsRepresentation realmClientsIdScopeMappingsGet(realm, id)

Get all scope mappings for the client

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ScopeMappingsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
apiInstance.realmClientsIdScopeMappingsGet(realm, id, (error, data, response) => {
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

### Return type

[**MappingsRepresentation**](MappingsRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdScopeMappingsRealmAvailableGet

> [RoleRepresentation] realmClientsIdScopeMappingsRealmAvailableGet(realm, id)

Get realm-level roles that are available to attach to this client’s scope

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ScopeMappingsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
apiInstance.realmClientsIdScopeMappingsRealmAvailableGet(realm, id, (error, data, response) => {
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

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdScopeMappingsRealmCompositeGet

> [RoleRepresentation] realmClientsIdScopeMappingsRealmCompositeGet(realm, id)

Get effective realm-level roles associated with the client’s scope   What this does is recurse  any composite roles associated with the client’s scope and adds the roles to this lists.

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ScopeMappingsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
apiInstance.realmClientsIdScopeMappingsRealmCompositeGet(realm, id, (error, data, response) => {
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

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdScopeMappingsRealmDelete

> realmClientsIdScopeMappingsRealmDelete(realm, id, roleRepresentation)

Remove a set of realm-level roles from the client’s scope

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ScopeMappingsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let roleRepresentation = [new KeycloakAdminRestApi.RoleRepresentation()]; // [RoleRepresentation] | 
apiInstance.realmClientsIdScopeMappingsRealmDelete(realm, id, roleRepresentation, (error, data, response) => {
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
 **roleRepresentation** | [**[RoleRepresentation]**](RoleRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmClientsIdScopeMappingsRealmGet

> [RoleRepresentation] realmClientsIdScopeMappingsRealmGet(realm, id)

Get realm-level roles associated with the client’s scope

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ScopeMappingsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
apiInstance.realmClientsIdScopeMappingsRealmGet(realm, id, (error, data, response) => {
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

### Return type

[**[RoleRepresentation]**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdScopeMappingsRealmPost

> realmClientsIdScopeMappingsRealmPost(realm, id, roleRepresentation)

Add a set of realm-level roles to the client’s scope

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ScopeMappingsApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let roleRepresentation = [new KeycloakAdminRestApi.RoleRepresentation()]; // [RoleRepresentation] | 
apiInstance.realmClientsIdScopeMappingsRealmPost(realm, id, roleRepresentation, (error, data, response) => {
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
 **roleRepresentation** | [**[RoleRepresentation]**](RoleRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

