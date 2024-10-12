# MachineLearningComputeManagementClient.MachineLearningComputeOperationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**machineLearningComputeListAvailableOperations**](MachineLearningComputeOperationsApi.md#machineLearningComputeListAvailableOperations) | **GET** /providers/Microsoft.MachineLearningCompute/operations | 



## machineLearningComputeListAvailableOperations

> AvailableOperations machineLearningComputeListAvailableOperations(apiVersion)



Gets all available operations.

### Example

```javascript
import MachineLearningComputeManagementClient from 'machine_learning_compute_management_client';

let apiInstance = new MachineLearningComputeManagementClient.MachineLearningComputeOperationsApi();
let apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearningCompute resource provider API to use.
apiInstance.machineLearningComputeListAvailableOperations(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the Microsoft.MachineLearningCompute resource provider API to use. | 

### Return type

[**AvailableOperations**](AvailableOperations.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

