# TrafficManagerManagementClient.RealUserMetricsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trafficManagerUserMetricsKeysCreateOrUpdate**](RealUserMetricsApi.md#trafficManagerUserMetricsKeysCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Network/trafficManagerUserMetricsKeys/default | 
[**trafficManagerUserMetricsKeysDelete**](RealUserMetricsApi.md#trafficManagerUserMetricsKeysDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Network/trafficManagerUserMetricsKeys/default | 
[**trafficManagerUserMetricsKeysGet**](RealUserMetricsApi.md#trafficManagerUserMetricsKeysGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/trafficManagerUserMetricsKeys/default | 



## trafficManagerUserMetricsKeysCreateOrUpdate

> UserMetricsModel trafficManagerUserMetricsKeysCreateOrUpdate(apiVersion, subscriptionId)



Create or update a subscription-level key used for Real User Metrics collection.

### Example

```javascript
import TrafficManagerManagementClient from 'traffic_manager_management_client';
let defaultClient = TrafficManagerManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TrafficManagerManagementClient.RealUserMetricsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.trafficManagerUserMetricsKeysCreateOrUpdate(apiVersion, subscriptionId, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**UserMetricsModel**](UserMetricsModel.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trafficManagerUserMetricsKeysDelete

> DeleteOperationResult trafficManagerUserMetricsKeysDelete(apiVersion, subscriptionId)



Delete a subscription-level key used for Real User Metrics collection.

### Example

```javascript
import TrafficManagerManagementClient from 'traffic_manager_management_client';
let defaultClient = TrafficManagerManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TrafficManagerManagementClient.RealUserMetricsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.trafficManagerUserMetricsKeysDelete(apiVersion, subscriptionId, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**DeleteOperationResult**](DeleteOperationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trafficManagerUserMetricsKeysGet

> UserMetricsModel trafficManagerUserMetricsKeysGet(apiVersion, subscriptionId)



Get the subscription-level key used for Real User Metrics collection.

### Example

```javascript
import TrafficManagerManagementClient from 'traffic_manager_management_client';
let defaultClient = TrafficManagerManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TrafficManagerManagementClient.RealUserMetricsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.trafficManagerUserMetricsKeysGet(apiVersion, subscriptionId, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**UserMetricsModel**](UserMetricsModel.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

