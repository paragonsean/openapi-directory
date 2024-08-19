# TrafficManagerManagementClient.EndpointsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**endpointsCreateOrUpdate**](EndpointsApi.md#endpointsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficmanagerprofiles/{profileName}/{endpointType}/{endpointName} | 
[**endpointsDelete**](EndpointsApi.md#endpointsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficmanagerprofiles/{profileName}/{endpointType}/{endpointName} | 
[**endpointsGet**](EndpointsApi.md#endpointsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficmanagerprofiles/{profileName}/{endpointType}/{endpointName} | 
[**endpointsUpdate**](EndpointsApi.md#endpointsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficmanagerprofiles/{profileName}/{endpointType}/{endpointName} | 



## endpointsCreateOrUpdate

> Endpoint endpointsCreateOrUpdate(resourceGroupName, profileName, endpointType, endpointName, apiVersion, subscriptionId, parameters)



Create or update a Traffic Manager endpoint.

### Example

```javascript
import TrafficManagerManagementClient from 'traffic_manager_management_client';
let defaultClient = TrafficManagerManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TrafficManagerManagementClient.EndpointsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Traffic Manager endpoint to be created or updated.
let profileName = "profileName_example"; // String | The name of the Traffic Manager profile.
let endpointType = "endpointType_example"; // String | The type of the Traffic Manager endpoint to be created or updated.
let endpointName = "endpointName_example"; // String | The name of the Traffic Manager endpoint to be created or updated.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new TrafficManagerManagementClient.Endpoint(); // Endpoint | The Traffic Manager endpoint parameters supplied to the CreateOrUpdate operation.
apiInstance.endpointsCreateOrUpdate(resourceGroupName, profileName, endpointType, endpointName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the Traffic Manager endpoint to be created or updated. | 
 **profileName** | **String**| The name of the Traffic Manager profile. | 
 **endpointType** | **String**| The type of the Traffic Manager endpoint to be created or updated. | 
 **endpointName** | **String**| The name of the Traffic Manager endpoint to be created or updated. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**Endpoint**](Endpoint.md)| The Traffic Manager endpoint parameters supplied to the CreateOrUpdate operation. | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## endpointsDelete

> DeleteOperationResult endpointsDelete(resourceGroupName, profileName, endpointType, endpointName, apiVersion, subscriptionId)



Deletes a Traffic Manager endpoint.

### Example

```javascript
import TrafficManagerManagementClient from 'traffic_manager_management_client';
let defaultClient = TrafficManagerManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TrafficManagerManagementClient.EndpointsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Traffic Manager endpoint to be deleted.
let profileName = "profileName_example"; // String | The name of the Traffic Manager profile.
let endpointType = "endpointType_example"; // String | The type of the Traffic Manager endpoint to be deleted.
let endpointName = "endpointName_example"; // String | The name of the Traffic Manager endpoint to be deleted.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.endpointsDelete(resourceGroupName, profileName, endpointType, endpointName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the Traffic Manager endpoint to be deleted. | 
 **profileName** | **String**| The name of the Traffic Manager profile. | 
 **endpointType** | **String**| The type of the Traffic Manager endpoint to be deleted. | 
 **endpointName** | **String**| The name of the Traffic Manager endpoint to be deleted. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**DeleteOperationResult**](DeleteOperationResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## endpointsGet

> Endpoint endpointsGet(resourceGroupName, profileName, endpointType, endpointName, apiVersion, subscriptionId)



Gets a Traffic Manager endpoint.

### Example

```javascript
import TrafficManagerManagementClient from 'traffic_manager_management_client';
let defaultClient = TrafficManagerManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TrafficManagerManagementClient.EndpointsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Traffic Manager endpoint.
let profileName = "profileName_example"; // String | The name of the Traffic Manager profile.
let endpointType = "endpointType_example"; // String | The type of the Traffic Manager endpoint.
let endpointName = "endpointName_example"; // String | The name of the Traffic Manager endpoint.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.endpointsGet(resourceGroupName, profileName, endpointType, endpointName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the Traffic Manager endpoint. | 
 **profileName** | **String**| The name of the Traffic Manager profile. | 
 **endpointType** | **String**| The type of the Traffic Manager endpoint. | 
 **endpointName** | **String**| The name of the Traffic Manager endpoint. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## endpointsUpdate

> Endpoint endpointsUpdate(resourceGroupName, profileName, endpointType, endpointName, apiVersion, subscriptionId, parameters)



Update a Traffic Manager endpoint.

### Example

```javascript
import TrafficManagerManagementClient from 'traffic_manager_management_client';
let defaultClient = TrafficManagerManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new TrafficManagerManagementClient.EndpointsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Traffic Manager endpoint to be updated.
let profileName = "profileName_example"; // String | The name of the Traffic Manager profile.
let endpointType = "endpointType_example"; // String | The type of the Traffic Manager endpoint to be updated.
let endpointName = "endpointName_example"; // String | The name of the Traffic Manager endpoint to be updated.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new TrafficManagerManagementClient.Endpoint(); // Endpoint | The Traffic Manager endpoint parameters supplied to the Update operation.
apiInstance.endpointsUpdate(resourceGroupName, profileName, endpointType, endpointName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the Traffic Manager endpoint to be updated. | 
 **profileName** | **String**| The name of the Traffic Manager profile. | 
 **endpointType** | **String**| The type of the Traffic Manager endpoint to be updated. | 
 **endpointName** | **String**| The name of the Traffic Manager endpoint to be updated. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**Endpoint**](Endpoint.md)| The Traffic Manager endpoint parameters supplied to the Update operation. | 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

