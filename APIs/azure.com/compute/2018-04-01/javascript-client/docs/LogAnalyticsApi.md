# ComputeManagementClient.LogAnalyticsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**logAnalyticsExportRequestRateByInterval**](LogAnalyticsApi.md#logAnalyticsExportRequestRateByInterval) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/logAnalytics/apiAccess/getRequestRateByInterval | 
[**logAnalyticsExportThrottledRequests**](LogAnalyticsApi.md#logAnalyticsExportThrottledRequests) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/logAnalytics/apiAccess/getThrottledRequests | 



## logAnalyticsExportRequestRateByInterval

> LogAnalyticsOperationResult logAnalyticsExportRequestRateByInterval(location, apiVersion, subscriptionId, parameters)



Export logs that show Api requests made by this subscription in the given time window to show throttling activities.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.LogAnalyticsApi();
let location = "location_example"; // String | The location upon which virtual-machine-sizes is queried.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ComputeManagementClient.RequestRateByIntervalInput(); // RequestRateByIntervalInput | Parameters supplied to the LogAnalytics getRequestRateByInterval Api.
apiInstance.logAnalyticsExportRequestRateByInterval(location, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **location** | **String**| The location upon which virtual-machine-sizes is queried. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**RequestRateByIntervalInput**](RequestRateByIntervalInput.md)| Parameters supplied to the LogAnalytics getRequestRateByInterval Api. | 

### Return type

[**LogAnalyticsOperationResult**](LogAnalyticsOperationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## logAnalyticsExportThrottledRequests

> LogAnalyticsOperationResult logAnalyticsExportThrottledRequests(location, apiVersion, subscriptionId, parameters)



Export logs that show total throttled Api requests for this subscription in the given time window.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.LogAnalyticsApi();
let location = "location_example"; // String | The location upon which virtual-machine-sizes is queried.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ComputeManagementClient.ThrottledRequestsInput(); // ThrottledRequestsInput | Parameters supplied to the LogAnalytics getThrottledRequests Api.
apiInstance.logAnalyticsExportThrottledRequests(location, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **location** | **String**| The location upon which virtual-machine-sizes is queried. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**ThrottledRequestsInput**](ThrottledRequestsInput.md)| Parameters supplied to the LogAnalytics getThrottledRequests Api. | 

### Return type

[**LogAnalyticsOperationResult**](LogAnalyticsOperationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

