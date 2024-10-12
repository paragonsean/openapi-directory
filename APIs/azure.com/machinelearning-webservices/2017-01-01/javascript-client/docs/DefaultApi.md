# AzureMlWebServicesManagementClient.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsList**](DefaultApi.md#operationsList) | **GET** /providers/Microsoft.MachineLearning/operations | 



## operationsList

> OperationEntityListResult operationsList(apiVersion)



Lists all the available REST API operations.

### Example

```javascript
import AzureMlWebServicesManagementClient from 'azure_ml_web_services_management_client';

let apiInstance = new AzureMlWebServicesManagementClient.DefaultApi();
let apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
apiInstance.operationsList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the Microsoft.MachineLearning resource provider API to use. | 

### Return type

[**OperationEntityListResult**](OperationEntityListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

