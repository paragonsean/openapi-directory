# MotaWordApi.PamApi

All URIs are relative to *https://api.motaword.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getClientProfileForPam**](PamApi.md#getClientProfileForPam) | **GET** /pam/profiles/client/{clientId} | Get the Pam profile of a client for this client ID
[**getProjectCompletionReportForPam**](PamApi.md#getProjectCompletionReportForPam) | **GET** /pam/projects/{projectId}/completion-report | Get completion report data of a project
[**postMessage**](PamApi.md#postMessage) | **POST** /pam/chat | Sends a message to chat



## getClientProfileForPam

> ClientProfile getClientProfileForPam(clientId)

Get the Pam profile of a client for this client ID

Get the Pam  profile of a client for this client ID

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.PamApi();
let clientId = 3707; // Number | Client ID
apiInstance.getClientProfileForPam(clientId, (error, data, response) => {
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
 **clientId** | **Number**| Client ID | 

### Return type

[**ClientProfile**](ClientProfile.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProjectCompletionReportForPam

> ProjectCompletionReport getProjectCompletionReportForPam(projectId)

Get completion report data of a project

Get completion report data of a project

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.PamApi();
let projectId = 74; // Number | Quote ID
apiInstance.getProjectCompletionReportForPam(projectId, (error, data, response) => {
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
 **projectId** | **Number**| Quote ID | 

### Return type

[**ProjectCompletionReport**](ProjectCompletionReport.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postMessage

> OperationStatus postMessage(opts)

Sends a message to chat

Sends a message to the channel.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.PamApi();
let opts = {
  'pamMessage': new MotaWordApi.PamMessage() // PamMessage | 
};
apiInstance.postMessage(opts, (error, data, response) => {
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
 **pamMessage** | [**PamMessage**](PamMessage.md)|  | [optional] 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

