# KeycloakAdminRestApi.ClientScopesApi

All URIs are relative to *http://keycloak.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realmClientScopesGet**](ClientScopesApi.md#realmClientScopesGet) | **GET** /{realm}/client-scopes | Get client scopes belonging to the realm   Returns a list of client scopes belonging to the realm
[**realmClientScopesIdDelete**](ClientScopesApi.md#realmClientScopesIdDelete) | **DELETE** /{realm}/client-scopes/{id} | Delete the client scope
[**realmClientScopesIdGet**](ClientScopesApi.md#realmClientScopesIdGet) | **GET** /{realm}/client-scopes/{id} | Get representation of the client scope
[**realmClientScopesIdPut**](ClientScopesApi.md#realmClientScopesIdPut) | **PUT** /{realm}/client-scopes/{id} | Update the client scope
[**realmClientScopesPost**](ClientScopesApi.md#realmClientScopesPost) | **POST** /{realm}/client-scopes | Create a new client scope   Client Scope’s name must be unique!



## realmClientScopesGet

> [ClientScopeRepresentation] realmClientScopesGet(realm)

Get client scopes belonging to the realm   Returns a list of client scopes belonging to the realm

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientScopesApi();
let realm = "realm_example"; // String | realm name (not id!)
apiInstance.realmClientScopesGet(realm, (error, data, response) => {
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

### Return type

[**[ClientScopeRepresentation]**](ClientScopeRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientScopesIdDelete

> realmClientScopesIdDelete(realm, id)

Delete the client scope

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientScopesApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client scope (not name)
apiInstance.realmClientScopesIdDelete(realm, id, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmClientScopesIdGet

> ClientScopeRepresentation realmClientScopesIdGet(realm, id)

Get representation of the client scope

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientScopesApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client scope (not name)
apiInstance.realmClientScopesIdGet(realm, id, (error, data, response) => {
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

[**ClientScopeRepresentation**](ClientScopeRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientScopesIdPut

> realmClientScopesIdPut(realm, id, clientScopeRepresentation)

Update the client scope

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientScopesApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client scope (not name)
let clientScopeRepresentation = new KeycloakAdminRestApi.ClientScopeRepresentation(); // ClientScopeRepresentation | 
apiInstance.realmClientScopesIdPut(realm, id, clientScopeRepresentation, (error, data, response) => {
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
 **clientScopeRepresentation** | [**ClientScopeRepresentation**](ClientScopeRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmClientScopesPost

> realmClientScopesPost(realm, clientScopeRepresentation)

Create a new client scope   Client Scope’s name must be unique!

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ClientScopesApi();
let realm = "realm_example"; // String | realm name (not id!)
let clientScopeRepresentation = new KeycloakAdminRestApi.ClientScopeRepresentation(); // ClientScopeRepresentation | 
apiInstance.realmClientScopesPost(realm, clientScopeRepresentation, (error, data, response) => {
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
 **clientScopeRepresentation** | [**ClientScopeRepresentation**](ClientScopeRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

