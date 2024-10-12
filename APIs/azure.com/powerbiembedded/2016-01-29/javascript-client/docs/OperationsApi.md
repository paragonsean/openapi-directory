# PowerBiEmbeddedManagementClient.OperationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAvailableOperations**](OperationsApi.md#getAvailableOperations) | **GET** /providers/Microsoft.PowerBI/operations | 



## getAvailableOperations

> OperationList getAvailableOperations(apiVersion)



Indicates which operations can be performed by the Power BI Resource Provider.

### Example

```javascript
import PowerBiEmbeddedManagementClient from 'power_bi_embedded_management_client';

let apiInstance = new PowerBiEmbeddedManagementClient.OperationsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.getAvailableOperations(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**OperationList**](OperationList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

