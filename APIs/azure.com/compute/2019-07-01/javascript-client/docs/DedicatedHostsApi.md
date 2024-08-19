# ComputeManagementClient.DedicatedHostsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dedicatedHostsCreateOrUpdate**](DedicatedHostsApi.md#dedicatedHostsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName}/hosts/{hostName} | 
[**dedicatedHostsDelete**](DedicatedHostsApi.md#dedicatedHostsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName}/hosts/{hostName} | 
[**dedicatedHostsGet**](DedicatedHostsApi.md#dedicatedHostsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName}/hosts/{hostName} | 
[**dedicatedHostsUpdate**](DedicatedHostsApi.md#dedicatedHostsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName}/hosts/{hostName} | 



## dedicatedHostsCreateOrUpdate

> DedicatedHost dedicatedHostsCreateOrUpdate(resourceGroupName, hostGroupName, hostName, apiVersion, subscriptionId, parameters)



Create or update a dedicated host .

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.DedicatedHostsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let hostGroupName = "hostGroupName_example"; // String | The name of the dedicated host group.
let hostName = "hostName_example"; // String | The name of the dedicated host .
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ComputeManagementClient.DedicatedHost(); // DedicatedHost | Parameters supplied to the Create Dedicated Host.
apiInstance.dedicatedHostsCreateOrUpdate(resourceGroupName, hostGroupName, hostName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **hostName** | **String**| The name of the dedicated host . | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**DedicatedHost**](DedicatedHost.md)| Parameters supplied to the Create Dedicated Host. | 

### Return type

[**DedicatedHost**](DedicatedHost.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dedicatedHostsDelete

> dedicatedHostsDelete(resourceGroupName, hostGroupName, hostName, apiVersion, subscriptionId)



Delete a dedicated host.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.DedicatedHostsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let hostGroupName = "hostGroupName_example"; // String | The name of the dedicated host group.
let hostName = "hostName_example"; // String | The name of the dedicated host.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.dedicatedHostsDelete(resourceGroupName, hostGroupName, hostName, apiVersion, subscriptionId, (error, data, response) => {
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
 **hostName** | **String**| The name of the dedicated host. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## dedicatedHostsGet

> DedicatedHost dedicatedHostsGet(resourceGroupName, hostGroupName, hostName, apiVersion, subscriptionId, opts)



Retrieves information about a dedicated host.

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.DedicatedHostsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let hostGroupName = "hostGroupName_example"; // String | The name of the dedicated host group.
let hostName = "hostName_example"; // String | The name of the dedicated host.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'expand': "expand_example" // String | The expand expression to apply on the operation.
};
apiInstance.dedicatedHostsGet(resourceGroupName, hostGroupName, hostName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **hostName** | **String**| The name of the dedicated host. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **expand** | **String**| The expand expression to apply on the operation. | [optional] 

### Return type

[**DedicatedHost**](DedicatedHost.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dedicatedHostsUpdate

> DedicatedHost dedicatedHostsUpdate(resourceGroupName, hostGroupName, hostName, apiVersion, subscriptionId, parameters)



Update an dedicated host .

### Example

```javascript
import ComputeManagementClient from 'compute_management_client';
let defaultClient = ComputeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ComputeManagementClient.DedicatedHostsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let hostGroupName = "hostGroupName_example"; // String | The name of the dedicated host group.
let hostName = "hostName_example"; // String | The name of the dedicated host .
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ComputeManagementClient.DedicatedHostUpdate(); // DedicatedHostUpdate | Parameters supplied to the Update Dedicated Host operation.
apiInstance.dedicatedHostsUpdate(resourceGroupName, hostGroupName, hostName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **hostName** | **String**| The name of the dedicated host . | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**DedicatedHostUpdate**](DedicatedHostUpdate.md)| Parameters supplied to the Update Dedicated Host operation. | 

### Return type

[**DedicatedHost**](DedicatedHost.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

