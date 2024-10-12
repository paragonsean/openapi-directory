# ComputeManagementClient.ProximityPlacementGroupsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**proximityPlacementGroupsCreateOrUpdate**](ProximityPlacementGroupsApi.md#proximityPlacementGroupsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/proximityPlacementGroups/{proximityPlacementGroupName} | 
[**proximityPlacementGroupsDelete**](ProximityPlacementGroupsApi.md#proximityPlacementGroupsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/proximityPlacementGroups/{proximityPlacementGroupName} | 
[**proximityPlacementGroupsGet**](ProximityPlacementGroupsApi.md#proximityPlacementGroupsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/proximityPlacementGroups/{proximityPlacementGroupName} | 
[**proximityPlacementGroupsListByResourceGroup**](ProximityPlacementGroupsApi.md#proximityPlacementGroupsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/proximityPlacementGroups | 
[**proximityPlacementGroupsListBySubscription**](ProximityPlacementGroupsApi.md#proximityPlacementGroupsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/proximityPlacementGroups | 
[**proximityPlacementGroupsUpdate**](ProximityPlacementGroupsApi.md#proximityPlacementGroupsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/proximityPlacementGroups/{proximityPlacementGroupName} | 



## proximityPlacementGroupsCreateOrUpdate

> ProximityPlacementGroup proximityPlacementGroupsCreateOrUpdate(resourceGroupName, proximityPlacementGroupName, apiVersion, subscriptionId, parameters)



Create or update a proximity placement group.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.ProximityPlacementGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let proximityPlacementGroupName = "proximityPlacementGroupName_example"; // String | The name of the proximity placement group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ComputeManagementClient.ProximityPlacementGroup(); // ProximityPlacementGroup | Parameters supplied to the Create Proximity Placement Group operation.
apiInstance.proximityPlacementGroupsCreateOrUpdate(resourceGroupName, proximityPlacementGroupName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **proximityPlacementGroupName** | **String**| The name of the proximity placement group. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**ProximityPlacementGroup**](ProximityPlacementGroup.md)| Parameters supplied to the Create Proximity Placement Group operation. | 

### Return type

[**ProximityPlacementGroup**](ProximityPlacementGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## proximityPlacementGroupsDelete

> proximityPlacementGroupsDelete(resourceGroupName, proximityPlacementGroupName, apiVersion, subscriptionId)



Delete a proximity placement group.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.ProximityPlacementGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let proximityPlacementGroupName = "proximityPlacementGroupName_example"; // String | The name of the proximity placement group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.proximityPlacementGroupsDelete(resourceGroupName, proximityPlacementGroupName, apiVersion, subscriptionId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceGroupName** | **String**| The name of the resource group. | 
 **proximityPlacementGroupName** | **String**| The name of the proximity placement group. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## proximityPlacementGroupsGet

> ProximityPlacementGroup proximityPlacementGroupsGet(resourceGroupName, proximityPlacementGroupName, apiVersion, subscriptionId)



Retrieves information about a proximity placement group .

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.ProximityPlacementGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let proximityPlacementGroupName = "proximityPlacementGroupName_example"; // String | The name of the proximity placement group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.proximityPlacementGroupsGet(resourceGroupName, proximityPlacementGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **proximityPlacementGroupName** | **String**| The name of the proximity placement group. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ProximityPlacementGroup**](ProximityPlacementGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## proximityPlacementGroupsListByResourceGroup

> ProximityPlacementGroupListResult proximityPlacementGroupsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Lists all proximity placement groups in a resource group.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.ProximityPlacementGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.proximityPlacementGroupsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ProximityPlacementGroupListResult**](ProximityPlacementGroupListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## proximityPlacementGroupsListBySubscription

> ProximityPlacementGroupListResult proximityPlacementGroupsListBySubscription(apiVersion, subscriptionId)



Lists all proximity placement groups in a subscription.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.ProximityPlacementGroupsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.proximityPlacementGroupsListBySubscription(apiVersion, subscriptionId, (error, data, response) => {
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

### Return type

[**ProximityPlacementGroupListResult**](ProximityPlacementGroupListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## proximityPlacementGroupsUpdate

> ProximityPlacementGroup proximityPlacementGroupsUpdate(resourceGroupName, proximityPlacementGroupName, apiVersion, subscriptionId, parameters)



Update a proximity placement group.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.ProximityPlacementGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let proximityPlacementGroupName = "proximityPlacementGroupName_example"; // String | The name of the proximity placement group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ComputeManagementClient.ProximityPlacementGroupUpdate(); // ProximityPlacementGroupUpdate | Parameters supplied to the Update Proximity Placement Group operation.
apiInstance.proximityPlacementGroupsUpdate(resourceGroupName, proximityPlacementGroupName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **proximityPlacementGroupName** | **String**| The name of the proximity placement group. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**ProximityPlacementGroupUpdate**](ProximityPlacementGroupUpdate.md)| Parameters supplied to the Update Proximity Placement Group operation. | 

### Return type

[**ProximityPlacementGroup**](ProximityPlacementGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

