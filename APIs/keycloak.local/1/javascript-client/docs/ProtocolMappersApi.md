# KeycloakAdminRestApi.ProtocolMappersApi

All URIs are relative to *http://keycloak.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**realmClientScopesId1ProtocolMappersModelsId2Delete**](ProtocolMappersApi.md#realmClientScopesId1ProtocolMappersModelsId2Delete) | **DELETE** /{realm}/client-scopes/{id1}/protocol-mappers/models/{id2} | Delete the mapper
[**realmClientScopesId1ProtocolMappersModelsId2Get**](ProtocolMappersApi.md#realmClientScopesId1ProtocolMappersModelsId2Get) | **GET** /{realm}/client-scopes/{id1}/protocol-mappers/models/{id2} | Get mapper by id
[**realmClientScopesId1ProtocolMappersModelsId2Put**](ProtocolMappersApi.md#realmClientScopesId1ProtocolMappersModelsId2Put) | **PUT** /{realm}/client-scopes/{id1}/protocol-mappers/models/{id2} | Update the mapper
[**realmClientScopesIdProtocolMappersAddModelsPost**](ProtocolMappersApi.md#realmClientScopesIdProtocolMappersAddModelsPost) | **POST** /{realm}/client-scopes/{id}/protocol-mappers/add-models | Create multiple mappers
[**realmClientScopesIdProtocolMappersModelsGet**](ProtocolMappersApi.md#realmClientScopesIdProtocolMappersModelsGet) | **GET** /{realm}/client-scopes/{id}/protocol-mappers/models | Get mappers
[**realmClientScopesIdProtocolMappersModelsPost**](ProtocolMappersApi.md#realmClientScopesIdProtocolMappersModelsPost) | **POST** /{realm}/client-scopes/{id}/protocol-mappers/models | Create a mapper
[**realmClientScopesIdProtocolMappersProtocolProtocolGet**](ProtocolMappersApi.md#realmClientScopesIdProtocolMappersProtocolProtocolGet) | **GET** /{realm}/client-scopes/{id}/protocol-mappers/protocol/{protocol} | Get mappers by name for a specific protocol
[**realmClientsId1ProtocolMappersModelsId2Delete**](ProtocolMappersApi.md#realmClientsId1ProtocolMappersModelsId2Delete) | **DELETE** /{realm}/clients/{id1}/protocol-mappers/models/{id2} | Delete the mapper
[**realmClientsId1ProtocolMappersModelsId2Get**](ProtocolMappersApi.md#realmClientsId1ProtocolMappersModelsId2Get) | **GET** /{realm}/clients/{id1}/protocol-mappers/models/{id2} | Get mapper by id
[**realmClientsId1ProtocolMappersModelsId2Put**](ProtocolMappersApi.md#realmClientsId1ProtocolMappersModelsId2Put) | **PUT** /{realm}/clients/{id1}/protocol-mappers/models/{id2} | Update the mapper
[**realmClientsIdProtocolMappersAddModelsPost**](ProtocolMappersApi.md#realmClientsIdProtocolMappersAddModelsPost) | **POST** /{realm}/clients/{id}/protocol-mappers/add-models | Create multiple mappers
[**realmClientsIdProtocolMappersModelsGet**](ProtocolMappersApi.md#realmClientsIdProtocolMappersModelsGet) | **GET** /{realm}/clients/{id}/protocol-mappers/models | Get mappers
[**realmClientsIdProtocolMappersModelsPost**](ProtocolMappersApi.md#realmClientsIdProtocolMappersModelsPost) | **POST** /{realm}/clients/{id}/protocol-mappers/models | Create a mapper
[**realmClientsIdProtocolMappersProtocolProtocolGet**](ProtocolMappersApi.md#realmClientsIdProtocolMappersProtocolProtocolGet) | **GET** /{realm}/clients/{id}/protocol-mappers/protocol/{protocol} | Get mappers by name for a specific protocol



## realmClientScopesId1ProtocolMappersModelsId2Delete

> realmClientScopesId1ProtocolMappersModelsId2Delete(realm, id1, id2)

Delete the mapper

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ProtocolMappersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id1 = "id1_example"; // String | 
let id2 = "id2_example"; // String | 
apiInstance.realmClientScopesId1ProtocolMappersModelsId2Delete(realm, id1, id2, (error, data, response) => {
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
 **id1** | **String**|  | 
 **id2** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmClientScopesId1ProtocolMappersModelsId2Get

> ProtocolMapperRepresentation realmClientScopesId1ProtocolMappersModelsId2Get(realm, id1, id2)

Get mapper by id

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ProtocolMappersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id1 = "id1_example"; // String | 
let id2 = "id2_example"; // String | 
apiInstance.realmClientScopesId1ProtocolMappersModelsId2Get(realm, id1, id2, (error, data, response) => {
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
 **id1** | **String**|  | 
 **id2** | **String**|  | 

### Return type

[**ProtocolMapperRepresentation**](ProtocolMapperRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientScopesId1ProtocolMappersModelsId2Put

> realmClientScopesId1ProtocolMappersModelsId2Put(realm, id1, id2, protocolMapperRepresentation)

Update the mapper

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ProtocolMappersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id1 = "id1_example"; // String | 
let id2 = "id2_example"; // String | 
let protocolMapperRepresentation = new KeycloakAdminRestApi.ProtocolMapperRepresentation(); // ProtocolMapperRepresentation | 
apiInstance.realmClientScopesId1ProtocolMappersModelsId2Put(realm, id1, id2, protocolMapperRepresentation, (error, data, response) => {
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
 **id1** | **String**|  | 
 **id2** | **String**|  | 
 **protocolMapperRepresentation** | [**ProtocolMapperRepresentation**](ProtocolMapperRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmClientScopesIdProtocolMappersAddModelsPost

> realmClientScopesIdProtocolMappersAddModelsPost(realm, id, protocolMapperRepresentation)

Create multiple mappers

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ProtocolMappersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client scope (not name)
let protocolMapperRepresentation = [new KeycloakAdminRestApi.ProtocolMapperRepresentation()]; // [ProtocolMapperRepresentation] | 
apiInstance.realmClientScopesIdProtocolMappersAddModelsPost(realm, id, protocolMapperRepresentation, (error, data, response) => {
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
 **protocolMapperRepresentation** | [**[ProtocolMapperRepresentation]**](ProtocolMapperRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmClientScopesIdProtocolMappersModelsGet

> [ProtocolMapperRepresentation] realmClientScopesIdProtocolMappersModelsGet(realm, id)

Get mappers

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ProtocolMappersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client scope (not name)
apiInstance.realmClientScopesIdProtocolMappersModelsGet(realm, id, (error, data, response) => {
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

[**[ProtocolMapperRepresentation]**](ProtocolMapperRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientScopesIdProtocolMappersModelsPost

> realmClientScopesIdProtocolMappersModelsPost(realm, id, protocolMapperRepresentation)

Create a mapper

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ProtocolMappersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client scope (not name)
let protocolMapperRepresentation = new KeycloakAdminRestApi.ProtocolMapperRepresentation(); // ProtocolMapperRepresentation | 
apiInstance.realmClientScopesIdProtocolMappersModelsPost(realm, id, protocolMapperRepresentation, (error, data, response) => {
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
 **protocolMapperRepresentation** | [**ProtocolMapperRepresentation**](ProtocolMapperRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmClientScopesIdProtocolMappersProtocolProtocolGet

> [ProtocolMapperRepresentation] realmClientScopesIdProtocolMappersProtocolProtocolGet(realm, id, protocol)

Get mappers by name for a specific protocol

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ProtocolMappersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client scope (not name)
let protocol = "protocol_example"; // String | 
apiInstance.realmClientScopesIdProtocolMappersProtocolProtocolGet(realm, id, protocol, (error, data, response) => {
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
 **protocol** | **String**|  | 

### Return type

[**[ProtocolMapperRepresentation]**](ProtocolMapperRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsId1ProtocolMappersModelsId2Delete

> realmClientsId1ProtocolMappersModelsId2Delete(realm, id1, id2)

Delete the mapper

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ProtocolMappersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id1 = "id1_example"; // String | 
let id2 = "id2_example"; // String | 
apiInstance.realmClientsId1ProtocolMappersModelsId2Delete(realm, id1, id2, (error, data, response) => {
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
 **id1** | **String**|  | 
 **id2** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## realmClientsId1ProtocolMappersModelsId2Get

> ProtocolMapperRepresentation realmClientsId1ProtocolMappersModelsId2Get(realm, id1, id2)

Get mapper by id

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ProtocolMappersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id1 = "id1_example"; // String | 
let id2 = "id2_example"; // String | 
apiInstance.realmClientsId1ProtocolMappersModelsId2Get(realm, id1, id2, (error, data, response) => {
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
 **id1** | **String**|  | 
 **id2** | **String**|  | 

### Return type

[**ProtocolMapperRepresentation**](ProtocolMapperRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsId1ProtocolMappersModelsId2Put

> realmClientsId1ProtocolMappersModelsId2Put(realm, id1, id2, protocolMapperRepresentation)

Update the mapper

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ProtocolMappersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id1 = "id1_example"; // String | 
let id2 = "id2_example"; // String | 
let protocolMapperRepresentation = new KeycloakAdminRestApi.ProtocolMapperRepresentation(); // ProtocolMapperRepresentation | 
apiInstance.realmClientsId1ProtocolMappersModelsId2Put(realm, id1, id2, protocolMapperRepresentation, (error, data, response) => {
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
 **id1** | **String**|  | 
 **id2** | **String**|  | 
 **protocolMapperRepresentation** | [**ProtocolMapperRepresentation**](ProtocolMapperRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmClientsIdProtocolMappersAddModelsPost

> realmClientsIdProtocolMappersAddModelsPost(realm, id, protocolMapperRepresentation)

Create multiple mappers

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ProtocolMappersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let protocolMapperRepresentation = [new KeycloakAdminRestApi.ProtocolMapperRepresentation()]; // [ProtocolMapperRepresentation] | 
apiInstance.realmClientsIdProtocolMappersAddModelsPost(realm, id, protocolMapperRepresentation, (error, data, response) => {
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
 **protocolMapperRepresentation** | [**[ProtocolMapperRepresentation]**](ProtocolMapperRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmClientsIdProtocolMappersModelsGet

> [ProtocolMapperRepresentation] realmClientsIdProtocolMappersModelsGet(realm, id)

Get mappers

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ProtocolMappersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
apiInstance.realmClientsIdProtocolMappersModelsGet(realm, id, (error, data, response) => {
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

[**[ProtocolMapperRepresentation]**](ProtocolMapperRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## realmClientsIdProtocolMappersModelsPost

> realmClientsIdProtocolMappersModelsPost(realm, id, protocolMapperRepresentation)

Create a mapper

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ProtocolMappersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let protocolMapperRepresentation = new KeycloakAdminRestApi.ProtocolMapperRepresentation(); // ProtocolMapperRepresentation | 
apiInstance.realmClientsIdProtocolMappersModelsPost(realm, id, protocolMapperRepresentation, (error, data, response) => {
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
 **protocolMapperRepresentation** | [**ProtocolMapperRepresentation**](ProtocolMapperRepresentation.md)|  | 

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## realmClientsIdProtocolMappersProtocolProtocolGet

> [ProtocolMapperRepresentation] realmClientsIdProtocolMappersProtocolProtocolGet(realm, id, protocol)

Get mappers by name for a specific protocol

### Example

```javascript
import KeycloakAdminRestApi from 'keycloak_admin_rest_api';
let defaultClient = KeycloakAdminRestApi.ApiClient.instance;
// Configure Bearer access token for authorization: access_token
let access_token = defaultClient.authentications['access_token'];
access_token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new KeycloakAdminRestApi.ProtocolMappersApi();
let realm = "realm_example"; // String | realm name (not id!)
let id = "id_example"; // String | id of client (not client-id)
let protocol = "protocol_example"; // String | 
apiInstance.realmClientsIdProtocolMappersProtocolProtocolGet(realm, id, protocol, (error, data, response) => {
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
 **protocol** | **String**|  | 

### Return type

[**[ProtocolMapperRepresentation]**](ProtocolMapperRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

