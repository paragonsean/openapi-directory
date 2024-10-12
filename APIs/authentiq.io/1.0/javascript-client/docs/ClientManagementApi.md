# AuthentiqConnectApi.ClientManagementApi

All URIs are relative to *https://connect.authentiq.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**client**](ClientManagementApi.md#client) | **GET** /client | List clients
[**clientClientId**](ClientManagementApi.md#clientClientId) | **DELETE** /client/{client_id} | Delete a client
[**createClient**](ClientManagementApi.md#createClient) | **POST** /client | Register a client
[**getClient**](ClientManagementApi.md#getClient) | **GET** /client/{client_id} | View a client
[**updateClient**](ClientManagementApi.md#updateClient) | **PUT** /client/{client_id} | Update a client



## client

> [Client] client()

List clients

Retrieve a list of clients. 

### Example

```javascript
import AuthentiqConnectApi from 'authentiq_connect_api';
let defaultClient = AuthentiqConnectApi.ApiClient.instance;
// Configure API key authorization: client_registration_token
let client_registration_token = defaultClient.authentications['client_registration_token'];
client_registration_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//client_registration_token.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth_code
let oauth_code = defaultClient.authentications['oauth_code'];
oauth_code.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth_implicit
let oauth_implicit = defaultClient.authentications['oauth_implicit'];
oauth_implicit.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthentiqConnectApi.ClientManagementApi();
apiInstance.client((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Client]**](Client.md)

### Authorization

[client_registration_token](../README.md#client_registration_token), [oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json, application/x-www-form-urlencoded, text/html


## clientClientId

> clientClientId(clientId)

Delete a client

Delete a previously registered client. 

### Example

```javascript
import AuthentiqConnectApi from 'authentiq_connect_api';
let defaultClient = AuthentiqConnectApi.ApiClient.instance;
// Configure API key authorization: client_registration_token
let client_registration_token = defaultClient.authentications['client_registration_token'];
client_registration_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//client_registration_token.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth_code
let oauth_code = defaultClient.authentications['oauth_code'];
oauth_code.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth_implicit
let oauth_implicit = defaultClient.authentications['oauth_implicit'];
oauth_implicit.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthentiqConnectApi.ClientManagementApi();
let clientId = "clientId_example"; // String | Client identifier
apiInstance.clientClientId(clientId, (error, data, response) => {
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
 **clientId** | **String**| Client identifier | 

### Return type

null (empty response body)

### Authorization

[client_registration_token](../README.md#client_registration_token), [oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json, application/x-www-form-urlencoded, text/html


## createClient

> createClient(client)

Register a client

Register a new client with this Authentiq Connect provider.  This endpoint is compatible with [OIDC&#39;s Client Registration](http://openid.net/specs/openid-connect-registration-1_0.html) extension. 

### Example

```javascript
import AuthentiqConnectApi from 'authentiq_connect_api';
let defaultClient = AuthentiqConnectApi.ApiClient.instance;
// Configure API key authorization: client_registration_token
let client_registration_token = defaultClient.authentications['client_registration_token'];
client_registration_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//client_registration_token.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth_code
let oauth_code = defaultClient.authentications['oauth_code'];
oauth_code.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth_implicit
let oauth_implicit = defaultClient.authentications['oauth_implicit'];
oauth_implicit.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthentiqConnectApi.ClientManagementApi();
let client = new AuthentiqConnectApi.Client(); // Client | Client Object
apiInstance.createClient(client, (error, data, response) => {
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
 **client** | [**Client**](Client.md)| Client Object | 

### Return type

null (empty response body)

### Authorization

[client_registration_token](../README.md#client_registration_token), [oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json, application/problem+json, application/x-www-form-urlencoded, text/html


## getClient

> Client getClient(clientId)

View a client

Retrieve the configuration of a previously registered client. 

### Example

```javascript
import AuthentiqConnectApi from 'authentiq_connect_api';
let defaultClient = AuthentiqConnectApi.ApiClient.instance;
// Configure API key authorization: client_registration_token
let client_registration_token = defaultClient.authentications['client_registration_token'];
client_registration_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//client_registration_token.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth_code
let oauth_code = defaultClient.authentications['oauth_code'];
oauth_code.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth_implicit
let oauth_implicit = defaultClient.authentications['oauth_implicit'];
oauth_implicit.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthentiqConnectApi.ClientManagementApi();
let clientId = "clientId_example"; // String | Client identifier
apiInstance.getClient(clientId, (error, data, response) => {
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
 **clientId** | **String**| Client identifier | 

### Return type

[**Client**](Client.md)

### Authorization

[client_registration_token](../README.md#client_registration_token), [oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/problem+json, application/x-www-form-urlencoded, text/html


## updateClient

> Client updateClient(clientId, client)

Update a client

Update the configuration of a previously registered client. 

### Example

```javascript
import AuthentiqConnectApi from 'authentiq_connect_api';
let defaultClient = AuthentiqConnectApi.ApiClient.instance;
// Configure API key authorization: client_registration_token
let client_registration_token = defaultClient.authentications['client_registration_token'];
client_registration_token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//client_registration_token.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: oauth_code
let oauth_code = defaultClient.authentications['oauth_code'];
oauth_code.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth_implicit
let oauth_implicit = defaultClient.authentications['oauth_implicit'];
oauth_implicit.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AuthentiqConnectApi.ClientManagementApi();
let clientId = "clientId_example"; // String | Client identifier
let client = new AuthentiqConnectApi.Client(); // Client | Client Object
apiInstance.updateClient(clientId, client, (error, data, response) => {
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
 **clientId** | **String**| Client identifier | 
 **client** | [**Client**](Client.md)| Client Object | 

### Return type

[**Client**](Client.md)

### Authorization

[client_registration_token](../README.md#client_registration_token), [oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json, application/problem+json, application/x-www-form-urlencoded, text/html

