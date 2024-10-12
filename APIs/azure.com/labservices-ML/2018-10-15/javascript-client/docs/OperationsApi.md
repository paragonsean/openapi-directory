# ManagedLabsClient.OperationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsGet**](OperationsApi.md#operationsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.LabServices/locations/{locationName}/operations/{operationName} | 



## operationsGet

> OperationResult operationsGet(subscriptionId, locationName, operationName, apiVersion)



Get operation

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.OperationsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let locationName = "locationName_example"; // String | The name of the location.
let operationName = "operationName_example"; // String | The name of the operation.
let apiVersion = "'2018-10-15'"; // String | Client API version.
apiInstance.operationsGet(subscriptionId, locationName, operationName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **locationName** | **String**| The name of the location. | 
 **operationName** | **String**| The name of the operation. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]

### Return type

[**OperationResult**](OperationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

