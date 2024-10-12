# AzureBotService.ListServiceProvidersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**botConnectionListServiceProviders**](ListServiceProvidersApi.md#botConnectionListServiceProviders) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.BotService/listAuthServiceProviders | 



## botConnectionListServiceProviders

> ServiceProviderResponseList botConnectionListServiceProviders(apiVersion, subscriptionId)



Lists the available Service Providers for creating Connection Settings

### Example

```javascript
import AzureBotService from 'azure_bot_service';

let apiInstance = new AzureBotService.ListServiceProvidersApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
apiInstance.botConnectionListServiceProviders(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 

### Return type

[**ServiceProviderResponseList**](ServiceProviderResponseList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

