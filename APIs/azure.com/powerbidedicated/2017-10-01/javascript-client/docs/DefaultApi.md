# PowerBiDedicated.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**capacitiesListSkus**](DefaultApi.md#capacitiesListSkus) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.PowerBIDedicated/skus | 



## capacitiesListSkus

> SkuEnumerationForNewResourceResult capacitiesListSkus(apiVersion, subscriptionId)



Lists eligible SKUs for PowerBI Dedicated resource provider.

### Example

```javascript
import PowerBiDedicated from 'power_bi_dedicated';
let defaultClient = PowerBiDedicated.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PowerBiDedicated.DefaultApi();
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.capacitiesListSkus(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| A unique identifier for a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**SkuEnumerationForNewResourceResult**](SkuEnumerationForNewResourceResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

