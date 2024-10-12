# SqlManagementClient.InstanceFailoverGroupsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instanceFailoverGroupsCreateOrUpdate**](InstanceFailoverGroupsApi.md#instanceFailoverGroupsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/locations/{locationName}/instanceFailoverGroups/{failoverGroupName} | 
[**instanceFailoverGroupsDelete**](InstanceFailoverGroupsApi.md#instanceFailoverGroupsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/locations/{locationName}/instanceFailoverGroups/{failoverGroupName} | 
[**instanceFailoverGroupsFailover**](InstanceFailoverGroupsApi.md#instanceFailoverGroupsFailover) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/locations/{locationName}/instanceFailoverGroups/{failoverGroupName}/failover | 
[**instanceFailoverGroupsForceFailoverAllowDataLoss**](InstanceFailoverGroupsApi.md#instanceFailoverGroupsForceFailoverAllowDataLoss) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/locations/{locationName}/instanceFailoverGroups/{failoverGroupName}/forceFailoverAllowDataLoss | 
[**instanceFailoverGroupsGet**](InstanceFailoverGroupsApi.md#instanceFailoverGroupsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/locations/{locationName}/instanceFailoverGroups/{failoverGroupName} | 
[**instanceFailoverGroupsListByLocation**](InstanceFailoverGroupsApi.md#instanceFailoverGroupsListByLocation) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/locations/{locationName}/instanceFailoverGroups | 



## instanceFailoverGroupsCreateOrUpdate

> InstanceFailoverGroup instanceFailoverGroupsCreateOrUpdate(resourceGroupName, locationName, failoverGroupName, subscriptionId, apiVersion, parameters)



Creates or updates a failover group.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.InstanceFailoverGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let locationName = "locationName_example"; // String | The name of the region where the resource is located.
let failoverGroupName = "failoverGroupName_example"; // String | The name of the failover group.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let parameters = new SqlManagementClient.InstanceFailoverGroup(); // InstanceFailoverGroup | The failover group parameters.
apiInstance.instanceFailoverGroupsCreateOrUpdate(resourceGroupName, locationName, failoverGroupName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **locationName** | **String**| The name of the region where the resource is located. | 
 **failoverGroupName** | **String**| The name of the failover group. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **parameters** | [**InstanceFailoverGroup**](InstanceFailoverGroup.md)| The failover group parameters. | 

### Return type

[**InstanceFailoverGroup**](InstanceFailoverGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## instanceFailoverGroupsDelete

> instanceFailoverGroupsDelete(resourceGroupName, locationName, failoverGroupName, subscriptionId, apiVersion)



Deletes a failover group.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.InstanceFailoverGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let locationName = "locationName_example"; // String | The name of the region where the resource is located.
let failoverGroupName = "failoverGroupName_example"; // String | The name of the failover group.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.instanceFailoverGroupsDelete(resourceGroupName, locationName, failoverGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **locationName** | **String**| The name of the region where the resource is located. | 
 **failoverGroupName** | **String**| The name of the failover group. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## instanceFailoverGroupsFailover

> InstanceFailoverGroup instanceFailoverGroupsFailover(resourceGroupName, locationName, failoverGroupName, subscriptionId, apiVersion)



Fails over from the current primary managed instance to this managed instance.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.InstanceFailoverGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let locationName = "locationName_example"; // String | The name of the region where the resource is located.
let failoverGroupName = "failoverGroupName_example"; // String | The name of the failover group.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.instanceFailoverGroupsFailover(resourceGroupName, locationName, failoverGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **locationName** | **String**| The name of the region where the resource is located. | 
 **failoverGroupName** | **String**| The name of the failover group. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**InstanceFailoverGroup**](InstanceFailoverGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## instanceFailoverGroupsForceFailoverAllowDataLoss

> InstanceFailoverGroup instanceFailoverGroupsForceFailoverAllowDataLoss(resourceGroupName, locationName, failoverGroupName, subscriptionId, apiVersion)



Fails over from the current primary managed instance to this managed instance. This operation might result in data loss.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.InstanceFailoverGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let locationName = "locationName_example"; // String | The name of the region where the resource is located.
let failoverGroupName = "failoverGroupName_example"; // String | The name of the failover group.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.instanceFailoverGroupsForceFailoverAllowDataLoss(resourceGroupName, locationName, failoverGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **locationName** | **String**| The name of the region where the resource is located. | 
 **failoverGroupName** | **String**| The name of the failover group. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**InstanceFailoverGroup**](InstanceFailoverGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## instanceFailoverGroupsGet

> InstanceFailoverGroup instanceFailoverGroupsGet(resourceGroupName, locationName, failoverGroupName, subscriptionId, apiVersion)



Gets a failover group.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.InstanceFailoverGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let locationName = "locationName_example"; // String | The name of the region where the resource is located.
let failoverGroupName = "failoverGroupName_example"; // String | The name of the failover group.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.instanceFailoverGroupsGet(resourceGroupName, locationName, failoverGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **locationName** | **String**| The name of the region where the resource is located. | 
 **failoverGroupName** | **String**| The name of the failover group. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**InstanceFailoverGroup**](InstanceFailoverGroup.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## instanceFailoverGroupsListByLocation

> InstanceFailoverGroupListResult instanceFailoverGroupsListByLocation(resourceGroupName, locationName, subscriptionId, apiVersion)



Lists the failover groups in a location.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.InstanceFailoverGroupsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let locationName = "locationName_example"; // String | The name of the region where the resource is located.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.instanceFailoverGroupsListByLocation(resourceGroupName, locationName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **locationName** | **String**| The name of the region where the resource is located. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**InstanceFailoverGroupListResult**](InstanceFailoverGroupListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

