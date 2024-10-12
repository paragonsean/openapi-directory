# MicrosoftResourceHealth.ChildAvailabilityStatusesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**childAvailabilityStatusesGetByResource**](ChildAvailabilityStatusesApi.md#childAvailabilityStatusesGetByResource) | **GET** /{resourceUri}/providers/Microsoft.ResourceHealth/childAvailabilityStatuses/current | 
[**childAvailabilityStatusesList**](ChildAvailabilityStatusesApi.md#childAvailabilityStatusesList) | **GET** /{resourceUri}/providers/Microsoft.ResourceHealth/childAvailabilityStatuses | 



## childAvailabilityStatusesGetByResource

> AvailabilityStatus childAvailabilityStatusesGetByResource(resourceUri, apiVersion, opts)



Gets current availability status for a single resource

### Example

```javascript
import MicrosoftResourceHealth from 'microsoft_resource_health';
let defaultClient = MicrosoftResourceHealth.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftResourceHealth.ChildAvailabilityStatusesApi();
let resourceUri = "resourceUri_example"; // String | The fully qualified ID of the resource, including the resource name and resource type. Currently the API only support one nesting level resource types : /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resource-provider-name}/{parentResourceType}/{parentResourceName}/{resourceType}/{resourceName}
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom=MSDN
  'expand': "expand_example" // String | Setting $expand=recommendedactions in url query expands the recommendedactions in the response.
};
apiInstance.childAvailabilityStatusesGetByResource(resourceUri, apiVersion, opts, (error, data, response) => {
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
 **resourceUri** | **String**| The fully qualified ID of the resource, including the resource name and resource type. Currently the API only support one nesting level resource types : /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resource-provider-name}/{parentResourceType}/{parentResourceName}/{resourceType}/{resourceName} | 
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


## childAvailabilityStatusesList

> AvailabilityStatusListResult childAvailabilityStatusesList(resourceUri, apiVersion, opts)



Lists the historical availability statuses for a single child resource. Use the nextLink property in the response to get the next page of availability status

### Example

```javascript
import MicrosoftResourceHealth from 'microsoft_resource_health';
let defaultClient = MicrosoftResourceHealth.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftResourceHealth.ChildAvailabilityStatusesApi();
let resourceUri = "resourceUri_example"; // String | The fully qualified ID of the resource, including the resource name and resource type. Currently the API only support one nesting level resource types : /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resource-provider-name}/{parentResourceType}/{parentResourceName}/{resourceType}/{resourceName}
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom=MSDN
  'expand': "expand_example" // String | Setting $expand=recommendedactions in url query expands the recommendedactions in the response.
};
apiInstance.childAvailabilityStatusesList(resourceUri, apiVersion, opts, (error, data, response) => {
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
 **resourceUri** | **String**| The fully qualified ID of the resource, including the resource name and resource type. Currently the API only support one nesting level resource types : /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resource-provider-name}/{parentResourceType}/{parentResourceName}/{resourceType}/{resourceName} | 
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

