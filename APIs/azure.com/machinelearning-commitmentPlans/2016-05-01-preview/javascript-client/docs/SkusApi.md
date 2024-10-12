# AzureMlCommitmentPlansManagementClient.SkusApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**skusList**](SkusApi.md#skusList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.MachineLearning/skus | 



## skusList

> SkuListResult skusList(subscriptionId, apiVersion)



Lists the available commitment plan SKUs.

### Example

```javascript
import AzureMlCommitmentPlansManagementClient from 'azure_ml_commitment_plans_management_client';

let apiInstance = new AzureMlCommitmentPlansManagementClient.SkusApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | The version of the Microsoft.MachineLearning resource provider API to use.
apiInstance.skusList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **apiVersion** | **String**| The version of the Microsoft.MachineLearning resource provider API to use. | 

### Return type

[**SkuListResult**](SkuListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

