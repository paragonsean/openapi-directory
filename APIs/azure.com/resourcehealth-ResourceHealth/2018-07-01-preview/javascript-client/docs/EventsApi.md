# MicrosoftResourceHealth.EventsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eventsListBySingleResource**](EventsApi.md#eventsListBySingleResource) | **GET** /{resourceUri}/providers/Microsoft.ResourceHealth/events | 
[**eventsListBySubscriptionId**](EventsApi.md#eventsListBySubscriptionId) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ResourceHealth/events | 



## eventsListBySingleResource

> Events eventsListBySingleResource(resourceUri, apiVersion, opts)



Lists current service health events for given resource.

### Example

```javascript
import MicrosoftResourceHealth from 'microsoft_resource_health';
let defaultClient = MicrosoftResourceHealth.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftResourceHealth.EventsApi();
let resourceUri = "resourceUri_example"; // String | The fully qualified ID of the resource, including the resource name and resource type. Currently the API support not nested and one nesting level resource types : /subscriptions/{subscriptionId}/resourceGroups/{resource-group-name}/providers/{resource-provider-name}/{resource-type}/{resource-name} and /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resource-provider-name}/{parentResourceType}/{parentResourceName}/{resourceType}/{resourceName}
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom=MSDN
};
apiInstance.eventsListBySingleResource(resourceUri, apiVersion, opts, (error, data, response) => {
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
 **resourceUri** | **String**| The fully qualified ID of the resource, including the resource name and resource type. Currently the API support not nested and one nesting level resource types : /subscriptions/{subscriptionId}/resourceGroups/{resource-group-name}/providers/{resource-provider-name}/{resource-type}/{resource-name} and /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resource-provider-name}/{parentResourceType}/{parentResourceName}/{resourceType}/{resourceName} | 
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom&#x3D;MSDN | [optional] 

### Return type

[**Events**](Events.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## eventsListBySubscriptionId

> Events eventsListBySubscriptionId(apiVersion, subscriptionId, opts)



Lists current service health events in the subscription.

### Example

```javascript
import MicrosoftResourceHealth from 'microsoft_resource_health';
let defaultClient = MicrosoftResourceHealth.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftResourceHealth.EventsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom=MSDN
};
apiInstance.eventsListBySubscriptionId(apiVersion, subscriptionId, opts, (error, data, response) => {
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

[**Events**](Events.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

