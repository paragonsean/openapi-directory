# ServiceBusManagementClient.PremiumMessagingRegionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**premiumMessagingRegionsList**](PremiumMessagingRegionsApi.md#premiumMessagingRegionsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ServiceBus/premiumMessagingRegions | 



## premiumMessagingRegionsList

> PremiumMessagingRegionsListResult premiumMessagingRegionsList(apiVersion, subscriptionId)



Gets the available premium messaging regions for servicebus 

### Example

```javascript
import ServiceBusManagementClient from 'service_bus_management_client';
let defaultClient = ServiceBusManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBusManagementClient.PremiumMessagingRegionsApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials that uniquely identify a Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.premiumMessagingRegionsList(apiVersion, subscriptionId, (error, data, response) => {
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

### Return type

[**PremiumMessagingRegionsListResult**](PremiumMessagingRegionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

