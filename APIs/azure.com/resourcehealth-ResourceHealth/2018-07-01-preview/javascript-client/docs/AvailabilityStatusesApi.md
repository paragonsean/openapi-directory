# MicrosoftResourceHealth.AvailabilityStatusesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**availabilityStatusesGetByResource**](AvailabilityStatusesApi.md#availabilityStatusesGetByResource) | **GET** /{resourceUri}/providers/Microsoft.ResourceHealth/availabilityStatuses/current | 
[**availabilityStatusesList**](AvailabilityStatusesApi.md#availabilityStatusesList) | **GET** /{resourceUri}/providers/Microsoft.ResourceHealth/availabilityStatuses | 
[**availabilityStatusesListByResourceGroup**](AvailabilityStatusesApi.md#availabilityStatusesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ResourceHealth/availabilityStatuses | 
[**availabilityStatusesListBySubscriptionId**](AvailabilityStatusesApi.md#availabilityStatusesListBySubscriptionId) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.ResourceHealth/availabilityStatuses | 



## availabilityStatusesGetByResource

> AvailabilityStatus availabilityStatusesGetByResource(resourceUri, apiVersion, opts)



Gets current availability status for a single resource

### Example

```javascript
import MicrosoftResourceHealth from 'microsoft_resource_health';
let defaultClient = MicrosoftResourceHealth.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftResourceHealth.AvailabilityStatusesApi();
let resourceUri = "resourceUri_example"; // String | The fully qualified ID of the resource, including the resource name and resource type. Currently the API support not nested and one nesting level resource types : /subscriptions/{subscriptionId}/resourceGroups/{resource-group-name}/providers/{resource-provider-name}/{resource-type}/{resource-name} and /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resource-provider-name}/{parentResourceType}/{parentResourceName}/{resourceType}/{resourceName}
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom=MSDN
  'expand': "expand_example" // String | Setting $expand=recommendedactions in url query expands the recommendedactions in the response.
};
apiInstance.availabilityStatusesGetByResource(resourceUri, apiVersion, opts, (error, data, response) => {
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
 **expand** | **String**| Setting $expand&#x3D;recommendedactions in url query expands the recommendedactions in the response. | [optional] 

### Return type

[**AvailabilityStatus**](AvailabilityStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## availabilityStatusesList

> AvailabilityStatusListResult availabilityStatusesList(resourceUri, apiVersion, opts)



Lists all historical availability transitions and impacting events for a single resource.

### Example

```javascript
import MicrosoftResourceHealth from 'microsoft_resource_health';
let defaultClient = MicrosoftResourceHealth.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftResourceHealth.AvailabilityStatusesApi();
let resourceUri = "resourceUri_example"; // String | The fully qualified ID of the resource, including the resource name and resource type. Currently the API support not nested and one nesting level resource types : /subscriptions/{subscriptionId}/resourceGroups/{resource-group-name}/providers/{resource-provider-name}/{resource-type}/{resource-name} and /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resource-provider-name}/{parentResourceType}/{parentResourceName}/{resourceType}/{resourceName}
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom=MSDN
  'expand': "expand_example" // String | Setting $expand=recommendedactions in url query expands the recommendedactions in the response.
};
apiInstance.availabilityStatusesList(resourceUri, apiVersion, opts, (error, data, response) => {
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
 **expand** | **String**| Setting $expand&#x3D;recommendedactions in url query expands the recommendedactions in the response. | [optional] 

### Return type

[**AvailabilityStatusListResult**](AvailabilityStatusListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## availabilityStatusesListByResourceGroup

> AvailabilityStatusListResult availabilityStatusesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts)



Lists the current availability status for all the resources in the resource group.

### Example

```javascript
import MicrosoftResourceHealth from 'microsoft_resource_health';
let defaultClient = MicrosoftResourceHealth.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftResourceHealth.AvailabilityStatusesApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom=MSDN
  'expand': "expand_example" // String | Setting $expand=recommendedactions in url query expands the recommendedactions in the response.
};
apiInstance.availabilityStatusesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom&#x3D;MSDN | [optional] 
 **expand** | **String**| Setting $expand&#x3D;recommendedactions in url query expands the recommendedactions in the response. | [optional] 

### Return type

[**AvailabilityStatusListResult**](AvailabilityStatusListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## availabilityStatusesListBySubscriptionId

> AvailabilityStatusListResult availabilityStatusesListBySubscriptionId(apiVersion, subscriptionId, opts)



Lists the current availability status for all the resources in the subscription.

### Example

```javascript
import MicrosoftResourceHealth from 'microsoft_resource_health';
let defaultClient = MicrosoftResourceHealth.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftResourceHealth.AvailabilityStatusesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom=MSDN
  'expand': "expand_example" // String | Setting $expand=recommendedactions in url query expands the recommendedactions in the response.
};
apiInstance.availabilityStatusesListBySubscriptionId(apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **expand** | **String**| Setting $expand&#x3D;recommendedactions in url query expands the recommendedactions in the response. | [optional] 

### Return type

[**AvailabilityStatusListResult**](AvailabilityStatusListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

