# KustoManagementClient.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clustersListSkus**](DefaultApi.md#clustersListSkus) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Kusto/skus | 



## clustersListSkus

> ListSkusResult clustersListSkus(apiVersion, subscriptionId)



Lists eligible SKUs for Kusto resource provider.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.DefaultApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.clustersListSkus(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ListSkusResult**](ListSkusResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

