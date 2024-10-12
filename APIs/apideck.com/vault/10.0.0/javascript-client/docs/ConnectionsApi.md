# VaultApi.ConnectionsApi

All URIs are relative to *https://unify.apideck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connectionSettingsAll**](ConnectionsApi.md#connectionSettingsAll) | **GET** /vault/connections/{unified_api}/{service_id}/{resource}/config | Get resource settings
[**connectionSettingsUpdate**](ConnectionsApi.md#connectionSettingsUpdate) | **PATCH** /vault/connections/{unified_api}/{service_id}/{resource}/config | Update settings
[**connectionsAdd**](ConnectionsApi.md#connectionsAdd) | **POST** /vault/connections/{unified_api}/{service_id} | Create connection
[**connectionsAll**](ConnectionsApi.md#connectionsAll) | **GET** /vault/connections | Get all connections
[**connectionsAuthorize**](ConnectionsApi.md#connectionsAuthorize) | **GET** /vault/authorize/{service_id}/{application_id} | Authorize
[**connectionsCallback**](ConnectionsApi.md#connectionsCallback) | **GET** /vault/callback | Callback
[**connectionsDelete**](ConnectionsApi.md#connectionsDelete) | **DELETE** /vault/connections/{unified_api}/{service_id} | Deletes a connection
[**connectionsImport**](ConnectionsApi.md#connectionsImport) | **POST** /vault/connections/{unified_api}/{service_id}/import | Import connection
[**connectionsOne**](ConnectionsApi.md#connectionsOne) | **GET** /vault/connections/{unified_api}/{service_id} | Get connection
[**connectionsRevoke**](ConnectionsApi.md#connectionsRevoke) | **GET** /vault/revoke/{service_id}/{application_id} | Revoke connection
[**connectionsToken**](ConnectionsApi.md#connectionsToken) | **POST** /vault/connections/{unified_api}/{service_id}/token | Get Access Token
[**connectionsUpdate**](ConnectionsApi.md#connectionsUpdate) | **PATCH** /vault/connections/{unified_api}/{service_id} | Update connection
[**customFieldsAll**](ConnectionsApi.md#customFieldsAll) | **GET** /vault/connections/{unified_api}/{service_id}/{resource}/custom-fields | Get resource custom fields



## connectionSettingsAll

> GetConnectionResponse connectionSettingsAll(xApideckConsumerId, xApideckAppId, unifiedApi, serviceId, resource)

Get resource settings

This endpoint returns custom settings and their defaults required by connection for a given resource. 

### Example

```javascript
import VaultApi from 'vault_api';
let defaultClient = VaultApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new VaultApi.ConnectionsApi();
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let unifiedApi = "crm"; // String | Unified API
let serviceId = "pipedrive"; // String | Service ID of the resource to return
let resource = "leads"; // String | Name of the resource (plural)
apiInstance.connectionSettingsAll(xApideckConsumerId, xApideckAppId, unifiedApi, serviceId, resource, (error, data, response) => {
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
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **unifiedApi** | **String**| Unified API | 
 **serviceId** | **String**| Service ID of the resource to return | 
 **resource** | **String**| Name of the resource (plural) | 

### Return type

[**GetConnectionResponse**](GetConnectionResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## connectionSettingsUpdate

> UpdateConnectionResponse connectionSettingsUpdate(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, resource, connection)

Update settings

Update default values for a connection&#39;s resource settings

### Example

```javascript
import VaultApi from 'vault_api';
let defaultClient = VaultApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new VaultApi.ConnectionsApi();
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let serviceId = "pipedrive"; // String | Service ID of the resource to return
let unifiedApi = "crm"; // String | Unified API
let resource = "leads"; // String | Name of the resource (plural)
let connection = new VaultApi.Connection(); // Connection | Fields that need to be updated on the resource
apiInstance.connectionSettingsUpdate(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, resource, connection, (error, data, response) => {
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
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **serviceId** | **String**| Service ID of the resource to return | 
 **unifiedApi** | **String**| Unified API | 
 **resource** | **String**| Name of the resource (plural) | 
 **connection** | [**Connection**](Connection.md)| Fields that need to be updated on the resource | 

### Return type

[**UpdateConnectionResponse**](UpdateConnectionResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## connectionsAdd

> CreateConnectionResponse connectionsAdd(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, connection)

Create connection

Create an authorized connection 

### Example

```javascript
import VaultApi from 'vault_api';
let defaultClient = VaultApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new VaultApi.ConnectionsApi();
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let serviceId = "pipedrive"; // String | Service ID of the resource to return
let unifiedApi = "crm"; // String | Unified API
let connection = new VaultApi.Connection(); // Connection | Fields that need to be persisted on the resource
apiInstance.connectionsAdd(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, connection, (error, data, response) => {
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
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **serviceId** | **String**| Service ID of the resource to return | 
 **unifiedApi** | **String**| Unified API | 
 **connection** | [**Connection**](Connection.md)| Fields that need to be persisted on the resource | 

### Return type

[**CreateConnectionResponse**](CreateConnectionResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## connectionsAll

> GetConnectionsResponse connectionsAll(xApideckConsumerId, xApideckAppId, opts)

Get all connections

This endpoint includes all the configured integrations and contains the required assets to build an integrations page where your users can install integrations. OAuth2 supported integrations will contain authorize and revoke links to handle the authentication flows. 

### Example

```javascript
import VaultApi from 'vault_api';
let defaultClient = VaultApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new VaultApi.ConnectionsApi();
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let opts = {
  'api': "crm", // String | Scope results to Unified API
  'configured': true // Boolean | Scopes results to connections that have been configured or not
};
apiInstance.connectionsAll(xApideckConsumerId, xApideckAppId, opts, (error, data, response) => {
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
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **api** | **String**| Scope results to Unified API | [optional] 
 **configured** | **Boolean**| Scopes results to connections that have been configured or not | [optional] 

### Return type

[**GetConnectionsResponse**](GetConnectionsResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## connectionsAuthorize

> UnexpectedErrorResponse connectionsAuthorize(serviceId, applicationId, state, redirectUri, opts)

Authorize

__In most cases the authorize link is provided in the &#x60;&#x60;/connections&#x60;&#x60; endpoint. Normally you don&#39;t need to manually generate these links.__  Use this endpoint to authenticate a user with a connector. It will return a 301 redirect to the downstream connector endpoints.  Auth links will have a state parameter included to verify the validity of the request. This is the url your users will use to activate OAuth supported integration providers.  Vault handles the complete Authorization Code Grant Type Flow for you and will redirect you to the dynamic redirect uri you have appended to the url in case this is missing the default redirect uri you have configured for your Unify application. 

### Example

```javascript
import VaultApi from 'vault_api';

let apiInstance = new VaultApi.ConnectionsApi();
let serviceId = "pipedrive"; // String | Service ID of the resource to return
let applicationId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | Application ID of the resource to return
let state = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb25zdW1lcl9pZCI6InRlc3RfdXNlcl9pZCIsInVuaWZpZWRfYXBpIjoiZGVmYXVsdCIsInNlcnZpY2VfaWQiOiJ0ZWFtbGVhZGVyIiwiYXBwbGljYXRpb25faWQiOiIxMTExIiwiaWF0IjoxNjIyMTI2Nzg3fQ.97_pn1UAXc7mctXBdr15czUNO1jjdQ9sJUOIE_Myzbk"; // String | An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks.
let redirectUri = "http://example.com/integrations"; // String | URL to redirect back to after authorization. When left empty the default configured redirect uri will be used.
let opts = {
  'scope': ["null"] // [String] | One or more OAuth scopes to request from the connector. OAuth scopes control the set of resources and operations that are allowed after authorization. Refer to the connector's documentation for the available scopes.
};
apiInstance.connectionsAuthorize(serviceId, applicationId, state, redirectUri, opts, (error, data, response) => {
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
 **serviceId** | **String**| Service ID of the resource to return | 
 **applicationId** | **String**| Application ID of the resource to return | 
 **state** | **String**| An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks. | 
 **redirectUri** | **String**| URL to redirect back to after authorization. When left empty the default configured redirect uri will be used. | 
 **scope** | [**[String]**](String.md)| One or more OAuth scopes to request from the connector. OAuth scopes control the set of resources and operations that are allowed after authorization. Refer to the connector&#39;s documentation for the available scopes. | [optional] 

### Return type

[**UnexpectedErrorResponse**](UnexpectedErrorResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## connectionsCallback

> UnexpectedErrorResponse connectionsCallback(state, code)

Callback

This endpoint gets called after the triggering the authorize flow.  Callback links need a state and code parameter to verify the validity of the request. 

### Example

```javascript
import VaultApi from 'vault_api';

let apiInstance = new VaultApi.ConnectionsApi();
let state = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb25zdW1lcl9pZCI6InRlc3RfdXNlcl9pZCIsInVuaWZpZWRfYXBpIjoiZGVmYXVsdCIsInNlcnZpY2VfaWQiOiJ0ZWFtbGVhZGVyIiwiYXBwbGljYXRpb25faWQiOiIxMTExIiwiaWF0IjoxNjIyMTI2Nzg3fQ.97_pn1UAXc7mctXBdr15czUNO1jjdQ9sJUOIE_Myzbk"; // String | An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks.
let code = "g0ZGZmNjVmOWI"; // String | An authorization code from the connector which Apideck Vault will later exchange for an access token.
apiInstance.connectionsCallback(state, code, (error, data, response) => {
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
 **state** | **String**| An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks. | 
 **code** | **String**| An authorization code from the connector which Apideck Vault will later exchange for an access token. | 

### Return type

[**UnexpectedErrorResponse**](UnexpectedErrorResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## connectionsDelete

> connectionsDelete(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi)

Deletes a connection

Deletes a connection

### Example

```javascript
import VaultApi from 'vault_api';
let defaultClient = VaultApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new VaultApi.ConnectionsApi();
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let serviceId = "pipedrive"; // String | Service ID of the resource to return
let unifiedApi = "crm"; // String | Unified API
apiInstance.connectionsDelete(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, (error, data, response) => {
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
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **serviceId** | **String**| Service ID of the resource to return | 
 **unifiedApi** | **String**| Unified API | 

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## connectionsImport

> CreateConnectionResponse connectionsImport(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, connectionImportData)

Import connection

Import an authorized connection. 

### Example

```javascript
import VaultApi from 'vault_api';
let defaultClient = VaultApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new VaultApi.ConnectionsApi();
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let serviceId = "pipedrive"; // String | Service ID of the resource to return
let unifiedApi = "crm"; // String | Unified API
let connectionImportData = new VaultApi.ConnectionImportData(); // ConnectionImportData | Fields that need to be persisted on the resource
apiInstance.connectionsImport(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, connectionImportData, (error, data, response) => {
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
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **serviceId** | **String**| Service ID of the resource to return | 
 **unifiedApi** | **String**| Unified API | 
 **connectionImportData** | [**ConnectionImportData**](ConnectionImportData.md)| Fields that need to be persisted on the resource | 

### Return type

[**CreateConnectionResponse**](CreateConnectionResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## connectionsOne

> GetConnectionResponse connectionsOne(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi)

Get connection

Get a connection

### Example

```javascript
import VaultApi from 'vault_api';
let defaultClient = VaultApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new VaultApi.ConnectionsApi();
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let serviceId = "pipedrive"; // String | Service ID of the resource to return
let unifiedApi = "crm"; // String | Unified API
apiInstance.connectionsOne(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, (error, data, response) => {
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
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **serviceId** | **String**| Service ID of the resource to return | 
 **unifiedApi** | **String**| Unified API | 

### Return type

[**GetConnectionResponse**](GetConnectionResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## connectionsRevoke

> UnexpectedErrorResponse connectionsRevoke(serviceId, applicationId, state, redirectUri)

Revoke connection

__In most cases the authorize link is provided in the &#x60;&#x60;/connections&#x60;&#x60; endpoint. Normally you don&#39;t need to manually generate these links.__  Use this endpoint to revoke an existing OAuth connector.  Auth links will have a state parameter included to verify the validity of the request. This is the url your users will use to activate OAuth supported integration providers.  Vault handles the complete revoke flow for you and will redirect you to the dynamic redirect uri you have appended to the url in case this is missing the default redirect uri you have configured for your Unify application. 

### Example

```javascript
import VaultApi from 'vault_api';

let apiInstance = new VaultApi.ConnectionsApi();
let serviceId = "pipedrive"; // String | Service ID of the resource to return
let applicationId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | Application ID of the resource to return
let state = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb25zdW1lcl9pZCI6InRlc3RfdXNlcl9pZCIsInVuaWZpZWRfYXBpIjoiZGVmYXVsdCIsInNlcnZpY2VfaWQiOiJ0ZWFtbGVhZGVyIiwiYXBwbGljYXRpb25faWQiOiIxMTExIiwiaWF0IjoxNjIyMTI2Nzg3fQ.97_pn1UAXc7mctXBdr15czUNO1jjdQ9sJUOIE_Myzbk"; // String | An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks.
let redirectUri = "http://example.com/integrations"; // String | URL to redirect back to after authorization. When left empty the default configured redirect uri will be used.
apiInstance.connectionsRevoke(serviceId, applicationId, state, redirectUri, (error, data, response) => {
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
 **serviceId** | **String**| Service ID of the resource to return | 
 **applicationId** | **String**| Application ID of the resource to return | 
 **state** | **String**| An opaque value the applications adds to the initial request that the authorization server includes when redirecting the back to the application. This value must be used by the application to prevent CSRF attacks. | 
 **redirectUri** | **String**| URL to redirect back to after authorization. When left empty the default configured redirect uri will be used. | 

### Return type

[**UnexpectedErrorResponse**](UnexpectedErrorResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## connectionsToken

> GetConnectionResponse connectionsToken(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, opts)

Get Access Token

Get an access token for a connection and store it in Vault. Currently only supported for connections with the client_credentials OAuth grant type.  Note that the access token will not be returned in the response. A 200 response code indicates a valid access token was stored on the connection. 

### Example

```javascript
import VaultApi from 'vault_api';
let defaultClient = VaultApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new VaultApi.ConnectionsApi();
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let serviceId = "pipedrive"; // String | Service ID of the resource to return
let unifiedApi = "crm"; // String | Unified API
let opts = {
  'body': {key: null} // Object | 
};
apiInstance.connectionsToken(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, opts, (error, data, response) => {
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
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **serviceId** | **String**| Service ID of the resource to return | 
 **unifiedApi** | **String**| Unified API | 
 **body** | **Object**|  | [optional] 

### Return type

[**GetConnectionResponse**](GetConnectionResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## connectionsUpdate

> UpdateConnectionResponse connectionsUpdate(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, connection)

Update connection

Update a connection

### Example

```javascript
import VaultApi from 'vault_api';
let defaultClient = VaultApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new VaultApi.ConnectionsApi();
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let serviceId = "pipedrive"; // String | Service ID of the resource to return
let unifiedApi = "crm"; // String | Unified API
let connection = new VaultApi.Connection(); // Connection | Fields that need to be updated on the resource
apiInstance.connectionsUpdate(xApideckConsumerId, xApideckAppId, serviceId, unifiedApi, connection, (error, data, response) => {
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
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **serviceId** | **String**| Service ID of the resource to return | 
 **unifiedApi** | **String**| Unified API | 
 **connection** | [**Connection**](Connection.md)| Fields that need to be updated on the resource | 

### Return type

[**UpdateConnectionResponse**](UpdateConnectionResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## customFieldsAll

> GetCustomFieldsResponse customFieldsAll(xApideckConsumerId, xApideckAppId, unifiedApi, serviceId, resource)

Get resource custom fields

This endpoint returns an custom fields on a connection resource. 

### Example

```javascript
import VaultApi from 'vault_api';
let defaultClient = VaultApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new VaultApi.ConnectionsApi();
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let unifiedApi = "crm"; // String | Unified API
let serviceId = "pipedrive"; // String | Service ID of the resource to return
let resource = "leads"; // String | Name of the resource (plural)
apiInstance.customFieldsAll(xApideckConsumerId, xApideckAppId, unifiedApi, serviceId, resource, (error, data, response) => {
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
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **unifiedApi** | **String**| Unified API | 
 **serviceId** | **String**| Service ID of the resource to return | 
 **resource** | **String**| Name of the resource (plural) | 

### Return type

[**GetCustomFieldsResponse**](GetCustomFieldsResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

