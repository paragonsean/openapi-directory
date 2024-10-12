# EtherpadApi.SessionApi

All URIs are relative to *http://etherpad.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSessionUsingGET**](SessionApi.md#createSessionUsingGET) | **GET** /createSession | creates a new session. validUntil is an unix timestamp in seconds
[**createSessionUsingPOST**](SessionApi.md#createSessionUsingPOST) | **POST** /createSession | creates a new session. validUntil is an unix timestamp in seconds
[**deleteSessionUsingGET**](SessionApi.md#deleteSessionUsingGET) | **GET** /deleteSession | deletes a session
[**deleteSessionUsingPOST**](SessionApi.md#deleteSessionUsingPOST) | **POST** /deleteSession | deletes a session
[**getSessionInfoUsingGET**](SessionApi.md#getSessionInfoUsingGET) | **GET** /getSessionInfo | returns informations about a session
[**getSessionInfoUsingPOST**](SessionApi.md#getSessionInfoUsingPOST) | **POST** /getSessionInfo | returns informations about a session



## createSessionUsingGET

> CreateSessionUsingGET200Response createSessionUsingGET(opts)

creates a new session. validUntil is an unix timestamp in seconds

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.SessionApi();
let opts = {
  'groupID': "groupID_example", // String | 
  'authorID': "authorID_example", // String | 
  'validUntil': "validUntil_example" // String | 
};
apiInstance.createSessionUsingGET(opts, (error, data, response) => {
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
 **groupID** | **String**|  | [optional] 
 **authorID** | **String**|  | [optional] 
 **validUntil** | **String**|  | [optional] 

### Return type

[**CreateSessionUsingGET200Response**](CreateSessionUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createSessionUsingPOST

> CreateSessionUsingGET200Response createSessionUsingPOST(opts)

creates a new session. validUntil is an unix timestamp in seconds

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.SessionApi();
let opts = {
  'groupID': "groupID_example", // String | 
  'authorID': "authorID_example", // String | 
  'validUntil': "validUntil_example" // String | 
};
apiInstance.createSessionUsingPOST(opts, (error, data, response) => {
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
 **groupID** | **String**|  | [optional] 
 **authorID** | **String**|  | [optional] 
 **validUntil** | **String**|  | [optional] 

### Return type

[**CreateSessionUsingGET200Response**](CreateSessionUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteSessionUsingGET

> AppendChatMessageUsingGET200Response deleteSessionUsingGET(opts)

deletes a session

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.SessionApi();
let opts = {
  'sessionID': "sessionID_example" // String | 
};
apiInstance.deleteSessionUsingGET(opts, (error, data, response) => {
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
 **sessionID** | **String**|  | [optional] 

### Return type

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteSessionUsingPOST

> AppendChatMessageUsingGET200Response deleteSessionUsingPOST(opts)

deletes a session

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.SessionApi();
let opts = {
  'sessionID': "sessionID_example" // String | 
};
apiInstance.deleteSessionUsingPOST(opts, (error, data, response) => {
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
 **sessionID** | **String**|  | [optional] 

### Return type

[**AppendChatMessageUsingGET200Response**](AppendChatMessageUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSessionInfoUsingGET

> GetSessionInfoUsingGET200Response getSessionInfoUsingGET(opts)

returns informations about a session

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.SessionApi();
let opts = {
  'sessionID': "sessionID_example" // String | 
};
apiInstance.getSessionInfoUsingGET(opts, (error, data, response) => {
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
 **sessionID** | **String**|  | [optional] 

### Return type

[**GetSessionInfoUsingGET200Response**](GetSessionInfoUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSessionInfoUsingPOST

> GetSessionInfoUsingGET200Response getSessionInfoUsingPOST(opts)

returns informations about a session

### Example

```javascript
import EtherpadApi from 'etherpad_api';
let defaultClient = EtherpadApi.ApiClient.instance;
// Configure API key authorization: ApiKey
let ApiKey = defaultClient.authentications['ApiKey'];
ApiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKey.apiKeyPrefix = 'Token';

let apiInstance = new EtherpadApi.SessionApi();
let opts = {
  'sessionID': "sessionID_example" // String | 
};
apiInstance.getSessionInfoUsingPOST(opts, (error, data, response) => {
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
 **sessionID** | **String**|  | [optional] 

### Return type

[**GetSessionInfoUsingGET200Response**](GetSessionInfoUsingGET200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

