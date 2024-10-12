# SqlManagementClient.SubscriptionUsagesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscriptionUsagesGet**](SubscriptionUsagesApi.md#subscriptionUsagesGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationName}/usages/{usageName} | 
[**subscriptionUsagesListByLocation**](SubscriptionUsagesApi.md#subscriptionUsagesListByLocation) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Sql/locations/{locationName}/usages | 



## subscriptionUsagesGet

> SubscriptionUsage subscriptionUsagesGet(locationName, usageName, subscriptionId, apiVersion)



Gets a subscription usage metric.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.SubscriptionUsagesApi();
let locationName = "locationName_example"; // String | The name of the region where the resource is located.
let usageName = "usageName_example"; // String | Name of usage metric to return.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.subscriptionUsagesGet(locationName, usageName, subscriptionId, apiVersion, (error, data, response) => {
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
 **locationName** | **String**| The name of the region where the resource is located. | 
 **usageName** | **String**| Name of usage metric to return. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**SubscriptionUsage**](SubscriptionUsage.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## subscriptionUsagesListByLocation

> SubscriptionUsageListResult subscriptionUsagesListByLocation(locationName, subscriptionId, apiVersion)



Gets all subscription usage metrics in a given location.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.SubscriptionUsagesApi();
let locationName = "locationName_example"; // String | The name of the region where the resource is located.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.subscriptionUsagesListByLocation(locationName, subscriptionId, apiVersion, (error, data, response) => {
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
 **locationName** | **String**| The name of the region where the resource is located. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**SubscriptionUsageListResult**](SubscriptionUsageListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

