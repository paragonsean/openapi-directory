# MarketplaceRpService.IsPrivateClientApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**privateStoreClientGet**](IsPrivateClientApi.md#privateStoreClientGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Marketplace/privateStoreClient/isPrivateClient | 



## privateStoreClientGet

> privateStoreClientGet(apiVersion, subscriptionId)



Check if client is private or not.

### Example

```javascript
import MarketplaceRpService from 'marketplace_rp_service';

let apiInstance = new MarketplaceRpService.IsPrivateClientApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription ID.
apiInstance.privateStoreClientGet(apiVersion, subscriptionId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiVersion** | **String**| The API version to use for the request. | 
 **subscriptionId** | **String**| The Azure subscription ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

