# TradematicCloudApi.ClientAPIApi

All URIs are relative to *https://api.tradematic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clientApikeysGet**](ClientAPIApi.md#clientApikeysGet) | **GET** /client/apikeys | Get API keys
[**clientApikeysKeyidDelete**](ClientAPIApi.md#clientApikeysKeyidDelete) | **DELETE** /client/apikeys/{keyid} | Delete API key
[**clientApikeysPost**](ClientAPIApi.md#clientApikeysPost) | **POST** /client/apikeys | Create new API key
[**clientUsersGet**](ClientAPIApi.md#clientUsersGet) | **GET** /client/users | Get users list
[**clientUsersLoginPost**](ClientAPIApi.md#clientUsersLoginPost) | **POST** /client/users/login | Logs user into the system
[**clientUsersRegisterPost**](ClientAPIApi.md#clientUsersRegisterPost) | **POST** /client/users/register | Register a new user
[**clientUsersUseridGet**](ClientAPIApi.md#clientUsersUseridGet) | **GET** /client/users/{userid} | Get user by ID



## clientApikeysGet

> [APIKey] clientApikeysGet()

Get API keys

Get API keys

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.ClientAPIApi();
apiInstance.clientApikeysGet((error, data, response) => {
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

[**[APIKey]**](APIKey.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clientApikeysKeyidDelete

> ClientApikeysKeyidDelete200Response clientApikeysKeyidDelete(keyid)

Delete API key

Delete API key

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.ClientAPIApi();
let keyid = 789; // Number | 
apiInstance.clientApikeysKeyidDelete(keyid, (error, data, response) => {
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
 **keyid** | **Number**|  | 

### Return type

[**ClientApikeysKeyidDelete200Response**](ClientApikeysKeyidDelete200Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clientApikeysPost

> ClientApikeysPost200Response clientApikeysPost()

Create new API key

Create new API key

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.ClientAPIApi();
apiInstance.clientApikeysPost((error, data, response) => {
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

[**ClientApikeysPost200Response**](ClientApikeysPost200Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clientUsersGet

> [User] clientUsersGet()

Get users list

Get users list

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.ClientAPIApi();
apiInstance.clientUsersGet((error, data, response) => {
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

[**[User]**](User.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clientUsersLoginPost

> ClientUsersLoginPost200Response clientUsersLoginPost()

Logs user into the system

Logs user into the system

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.ClientAPIApi();
apiInstance.clientUsersLoginPost((error, data, response) => {
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

[**ClientUsersLoginPost200Response**](ClientUsersLoginPost200Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clientUsersRegisterPost

> ClientUsersRegisterPost200Response clientUsersRegisterPost(body)

Register a new user

Register a new user

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.ClientAPIApi();
let body = new TradematicCloudApi.ClientUsersRegisterPostRequest(); // ClientUsersRegisterPostRequest | 
apiInstance.clientUsersRegisterPost(body, (error, data, response) => {
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
 **body** | [**ClientUsersRegisterPostRequest**](ClientUsersRegisterPostRequest.md)|  | 

### Return type

[**ClientUsersRegisterPost200Response**](ClientUsersRegisterPost200Response.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## clientUsersUseridGet

> User clientUsersUseridGet(userid)

Get user by ID

Get user by ID

### Example

```javascript
import TradematicCloudApi from 'tradematic_cloud_api';
let defaultClient = TradematicCloudApi.ApiClient.instance;
// Configure API key authorization: Secured
let Secured = defaultClient.authentications['Secured'];
Secured.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Secured.apiKeyPrefix = 'Token';

let apiInstance = new TradematicCloudApi.ClientAPIApi();
let userid = 789; // Number | 
apiInstance.clientUsersUseridGet(userid, (error, data, response) => {
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
 **userid** | **Number**|  | 

### Return type

[**User**](User.md)

### Authorization

[Secured](../README.md#Secured)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

