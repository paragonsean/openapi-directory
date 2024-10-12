# DevTestLabsClient.OperationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsGet**](OperationsApi.md#operationsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DevTestLab/locations/{locationName}/operations/{name} | 



## operationsGet

> OperationResult operationsGet(subscriptionId, locationName, name, apiVersion)



Get operation.

### Example

```javascript
import DevTestLabsClient from 'dev_test_labs_client';
let defaultClient = DevTestLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DevTestLabsClient.OperationsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let locationName = "locationName_example"; // String | The name of the location.
let name = "name_example"; // String | The name of the operation.
let apiVersion = "'2018-09-15'"; // String | Client API version.
apiInstance.operationsGet(subscriptionId, locationName, name, apiVersion, (error, data, response) => {
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
 **name** | **String**| The name of the operation. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-09-15&#39;]

### Return type

[**OperationResult**](OperationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

