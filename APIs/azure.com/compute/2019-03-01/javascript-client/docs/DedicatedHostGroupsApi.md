# ComputeManagementClient.DedicatedHostGroupsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dedicatedHostGroupsCreateOrUpdate**](DedicatedHostGroupsApi.md#dedicatedHostGroupsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName} | 
[**dedicatedHostGroupsDelete**](DedicatedHostGroupsApi.md#dedicatedHostGroupsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName} | 
[**dedicatedHostGroupsGet**](DedicatedHostGroupsApi.md#dedicatedHostGroupsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName} | 
[**dedicatedHostGroupsListByResourceGroup**](DedicatedHostGroupsApi.md#dedicatedHostGroupsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups | 
[**dedicatedHostGroupsListBySubscription**](DedicatedHostGroupsApi.md#dedicatedHostGroupsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Compute/hostGroups | 
[**dedicatedHostGroupsUpdate**](DedicatedHostGroupsApi.md#dedicatedHostGroupsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName} | 



## dedicatedHostGroupsCreateOrUpdate

> DedicatedHostGroup dedicatedHostGroupsCreateOrUpdate(resourceGroupName, hostGroupName, apiVersion, subscriptionId, parameters)



Create or update a dedicated host group. For details of Dedicated Host and Dedicated Host Groups please see [Dedicated Host Documentation] (https://go.microsoft.com/fwlink/?linkid&#x3D;2082596)

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.DedicatedHostGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let hostGroupName = "hostGroupName_example"; // String | The name of the dedicated host group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ComputeManagementClient.DedicatedHostGroup(); // DedicatedHostGroup | Parameters supplied to the Create Dedicated Host Group.
apiInstance.dedicatedHostGroupsCreateOrUpdate(resourceGroupName, hostGroupName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **hostGroupName** | **String**| The name of the dedicated host group. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**DedicatedHostGroup**](DedicatedHostGroup.md)| Parameters supplied to the Create Dedicated Host Group. | 

### Return type

[**DedicatedHostGroup**](DedicatedHostGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dedicatedHostGroupsDelete

> dedicatedHostGroupsDelete(resourceGroupName, hostGroupName, apiVersion, subscriptionId)



Delete a dedicated host group.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.DedicatedHostGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let hostGroupName = "hostGroupName_example"; // String | The name of the dedicated host group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.dedicatedHostGroupsDelete(resourceGroupName, hostGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **hostGroupName** | **String**| The name of the dedicated host group. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## dedicatedHostGroupsGet

> DedicatedHostGroup dedicatedHostGroupsGet(resourceGroupName, hostGroupName, apiVersion, subscriptionId)



Retrieves information about a dedicated host group.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.DedicatedHostGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let hostGroupName = "hostGroupName_example"; // String | The name of the dedicated host group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.dedicatedHostGroupsGet(resourceGroupName, hostGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **hostGroupName** | **String**| The name of the dedicated host group. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**DedicatedHostGroup**](DedicatedHostGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dedicatedHostGroupsListByResourceGroup

> DedicatedHostGroupListResult dedicatedHostGroupsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Lists all of the dedicated host groups in the specified resource group. Use the nextLink property in the response to get the next page of dedicated host groups.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.DedicatedHostGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.dedicatedHostGroupsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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

[**DedicatedHostGroupListResult**](DedicatedHostGroupListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dedicatedHostGroupsListBySubscription

> DedicatedHostGroupListResult dedicatedHostGroupsListBySubscription(apiVersion, subscriptionId)



Lists all of the dedicated host groups in the subscription. Use the nextLink property in the response to get the next page of dedicated host groups.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.DedicatedHostGroupsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.dedicatedHostGroupsListBySubscription(apiVersion, subscriptionId, (error, data, response) => {
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

[**DedicatedHostGroupListResult**](DedicatedHostGroupListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dedicatedHostGroupsUpdate

> DedicatedHostGroup dedicatedHostGroupsUpdate(resourceGroupName, hostGroupName, apiVersion, subscriptionId, parameters)



Update an dedicated host group.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.DedicatedHostGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let hostGroupName = "hostGroupName_example"; // String | The name of the dedicated host group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ComputeManagementClient.DedicatedHostGroupUpdate(); // DedicatedHostGroupUpdate | Parameters supplied to the Update Dedicated Host Group operation.
apiInstance.dedicatedHostGroupsUpdate(resourceGroupName, hostGroupName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **hostGroupName** | **String**| The name of the dedicated host group. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**DedicatedHostGroupUpdate**](DedicatedHostGroupUpdate.md)| Parameters supplied to the Update Dedicated Host Group operation. | 

### Return type

[**DedicatedHostGroup**](DedicatedHostGroup.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

