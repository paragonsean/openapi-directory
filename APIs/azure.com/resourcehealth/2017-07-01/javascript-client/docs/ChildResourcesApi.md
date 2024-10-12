# MicrosoftResourceHealth.ChildResourcesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**childResourcesList**](ChildResourcesApi.md#childResourcesList) | **GET** /{resourceUri}/providers/Microsoft.ResourceHealth/childResources | 



## childResourcesList

> AvailabilityStatusListResult childResourcesList(resourceUri, apiVersion, opts)



Lists the all the children and its current health status for a parent resource. Use the nextLink property in the response to get the next page of children current health

### Example

```javascript
import MicrosoftResourceHealth from 'microsoft_resource_health';
let defaultClient = MicrosoftResourceHealth.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftResourceHealth.ChildResourcesApi();
let resourceUri = "resourceUri_example"; // String | The fully qualified ID of the resource, including the resource name and resource type. Currently the API only support not nested parent resource type: /subscriptions/{subscriptionId}/resourceGroups/{resource-group-name}/providers/{resource-provider-name}/{resource-type}/{resource-name}
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation. For more information please see https://docs.microsoft.com/en-us/rest/api/apimanagement/apis?redirectedfrom=MSDN
  'expand': "expand_example" // String | Setting $expand=recommendedactions in url query expands the recommendedactions in the response.
};
apiInstance.childResourcesList(resourceUri, apiVersion, opts, (error, data, response) => {
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
 **resourceUri** | **String**| The fully qualified ID of the resource, including the resource name and resource type. Currently the API only support not nested parent resource type: /subscriptions/{subscriptionId}/resourceGroups/{resource-group-name}/providers/{resource-provider-name}/{resource-type}/{resource-name} | 
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

