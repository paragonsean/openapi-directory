# ServiceBusManagementClient.RegionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**regionsListBySku**](RegionsApi.md#regionsListBySku) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ServiceBus/sku/{sku}/regions | 



## regionsListBySku

> PremiumMessagingRegionsListResult regionsListBySku(apiVersion, subscriptionId, sku)



Gets the available Regions for a given sku

### Example

```javascript
import ServiceBusManagementClient from 'service_bus_management_client';
let defaultClient = ServiceBusManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBusManagementClient.RegionsApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let sku = "sku_example"; // String | The sku type.
apiInstance.regionsListBySku(apiVersion, subscriptionId, sku, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **sku** | **String**| The sku type. | 

### Return type

[**PremiumMessagingRegionsListResult**](PremiumMessagingRegionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

