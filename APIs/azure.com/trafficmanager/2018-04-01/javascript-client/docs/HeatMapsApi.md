# TrafficManagerManagementClient.HeatMapsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**heatMapGet**](HeatMapsApi.md#heatMapGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficmanagerprofiles/{profileName}/heatMaps/{heatMapType} | 



## heatMapGet

> HeatMapModel heatMapGet(subscriptionId, resourceGroupName, profileName, heatMapType, apiVersion, opts)



Gets latest heatmap for Traffic Manager profile.

### Example

```javascript
import TrafficManagerManagementClient from 'traffic_manager_management_client';
let defaultClient = TrafficManagerManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TrafficManagerManagementClient.HeatMapsApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Traffic Manager endpoint.
let profileName = "profileName_example"; // String | The name of the Traffic Manager profile.
let heatMapType = "heatMapType_example"; // String | The type of HeatMap for the Traffic Manager profile.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'topLeft': [null], // [Number] | The top left latitude,longitude pair of the rectangular viewport to query for.
  'botRight': [null] // [Number] | The bottom right latitude,longitude pair of the rectangular viewport to query for.
};
apiInstance.heatMapGet(subscriptionId, resourceGroupName, profileName, heatMapType, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group containing the Traffic Manager endpoint. | 
 **profileName** | **String**| The name of the Traffic Manager profile. | 
 **heatMapType** | **String**| The type of HeatMap for the Traffic Manager profile. | 
 **apiVersion** | **String**| Client Api Version. | 
 **topLeft** | [**[Number]**](Number.md)| The top left latitude,longitude pair of the rectangular viewport to query for. | [optional] 
 **botRight** | [**[Number]**](Number.md)| The bottom right latitude,longitude pair of the rectangular viewport to query for. | [optional] 

### Return type

[**HeatMapModel**](HeatMapModel.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

