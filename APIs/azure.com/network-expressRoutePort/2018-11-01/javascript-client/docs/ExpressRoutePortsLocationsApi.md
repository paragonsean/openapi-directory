# NetworkManagementClient.ExpressRoutePortsLocationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expressRoutePortsLocationsGet**](ExpressRoutePortsLocationsApi.md#expressRoutePortsLocationsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/ExpressRoutePortsLocations/{locationName} | 
[**expressRoutePortsLocationsList**](ExpressRoutePortsLocationsApi.md#expressRoutePortsLocationsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/ExpressRoutePortsLocations | 



## expressRoutePortsLocationsGet

> ExpressRoutePortsLocation expressRoutePortsLocationsGet(subscriptionId, apiVersion, locationName)



Retrieves a single ExpressRoutePort peering location, including the list of available bandwidths available at said peering location.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ExpressRoutePortsLocationsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version.
let locationName = "locationName_example"; // String | Name of the requested ExpressRoutePort peering location.
apiInstance.expressRoutePortsLocationsGet(subscriptionId, apiVersion, locationName, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API version. | 
 **locationName** | **String**| Name of the requested ExpressRoutePort peering location. | 

### Return type

[**ExpressRoutePortsLocation**](ExpressRoutePortsLocation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expressRoutePortsLocationsList

> ExpressRoutePortsLocationListResult expressRoutePortsLocationsList(subscriptionId, apiVersion)



Retrieves all ExpressRoutePort peering locations. Does not return available bandwidths for each location. Available bandwidths can only be obtained when retrieving a specific peering location.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ExpressRoutePortsLocationsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version.
apiInstance.expressRoutePortsLocationsList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API version. | 

### Return type

[**ExpressRoutePortsLocationListResult**](ExpressRoutePortsLocationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

