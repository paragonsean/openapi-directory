# MicrosoftResourceHealth.ImpactedResourcesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**impactedResourcesListBySubscriptionId**](ImpactedResourcesApi.md#impactedResourcesListBySubscriptionId) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ResourceHealth/impactedResources | 



## impactedResourcesListBySubscriptionId

> ImpactedResourceListResult impactedResourcesListBySubscriptionId(apiVersion, subscriptionId, opts)



Lists the current availability status for impacted resources in the subscription.

### Example

```javascript
import MicrosoftResourceHealth from 'microsoft_resource_health';
let defaultClient = MicrosoftResourceHealth.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftResourceHealth.ImpactedResourcesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom=MSDN
};
apiInstance.impactedResourcesListBySubscriptionId(apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **filter** | **String**| The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom&#x3D;MSDN | [optional] 

### Return type

[**ImpactedResourceListResult**](ImpactedResourceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

