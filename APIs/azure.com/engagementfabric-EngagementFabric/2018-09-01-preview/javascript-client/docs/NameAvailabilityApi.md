# EngagementFabric.NameAvailabilityApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkNameAvailability**](NameAvailabilityApi.md#checkNameAvailability) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EngagementFabric/checkNameAvailability | Check availability of EngagementFabric resource



## checkNameAvailability

> CheckNameAvailabilityResult checkNameAvailability(subscriptionId, resourceGroupName, apiVersion, parameters)

Check availability of EngagementFabric resource

### Example

```javascript
import EngagementFabric from 'engagement_fabric';

let apiInstance = new EngagementFabric.NameAvailabilityApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | Resource Group Name
let apiVersion = "apiVersion_example"; // String | API version
let parameters = new EngagementFabric.CheckNameAvailabilityParameter(); // CheckNameAvailabilityParameter | Parameter describing the name to be checked
apiInstance.checkNameAvailability(subscriptionId, resourceGroupName, apiVersion, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| Resource Group Name | 
 **apiVersion** | **String**| API version | 
 **parameters** | [**CheckNameAvailabilityParameter**](CheckNameAvailabilityParameter.md)| Parameter describing the name to be checked | 

### Return type

[**CheckNameAvailabilityResult**](CheckNameAvailabilityResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

