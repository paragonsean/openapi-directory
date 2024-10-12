# DispatchApi.DefaultApi

All URIs are relative to *https://api.nexmo.com/v0.1/dispatch*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createWorkflow**](DefaultApi.md#createWorkflow) | **POST** / | Create a workflow



## createWorkflow

> Response createWorkflow(createWorkflow)

Create a workflow

### Example

```javascript
import DispatchApi from 'dispatch_api';
let defaultClient = DispatchApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new DispatchApi.DefaultApi();
let createWorkflow = new DispatchApi.CreateWorkflow(); // CreateWorkflow | Please note that last message does not have failover attribute inside it. All other messages must contain a failover attribute.
apiInstance.createWorkflow(createWorkflow, (error, data, response) => {
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
 **createWorkflow** | [**CreateWorkflow**](CreateWorkflow.md)| Please note that last message does not have failover attribute inside it. All other messages must contain a failover attribute. | 

### Return type

[**Response**](Response.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

