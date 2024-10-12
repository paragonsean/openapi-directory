# EngagementFabric.SkusApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sKUsList**](SkusApi.md#sKUsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.EngagementFabric/skus | List available SKUs of EngagementFabric resource



## sKUsList

> SkuDescriptionList sKUsList(subscriptionId, apiVersion)

List available SKUs of EngagementFabric resource

### Example

```javascript
import EngagementFabric from 'engagement_fabric';

let apiInstance = new EngagementFabric.SkusApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription ID
let apiVersion = "apiVersion_example"; // String | API version
apiInstance.sKUsList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription ID | 
 **apiVersion** | **String**| API version | 

### Return type

[**SkuDescriptionList**](SkuDescriptionList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

