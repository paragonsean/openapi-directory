# AzureDedicatedHsmResourceProvider.DedicatedHsmsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dedicatedHsmCreateOrUpdate**](DedicatedHsmsApi.md#dedicatedHsmCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HardwareSecurityModules/dedicatedHSMs/{name} | 
[**dedicatedHsmDelete**](DedicatedHsmsApi.md#dedicatedHsmDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HardwareSecurityModules/dedicatedHSMs/{name} | 
[**dedicatedHsmGet**](DedicatedHsmsApi.md#dedicatedHsmGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HardwareSecurityModules/dedicatedHSMs/{name} | 
[**dedicatedHsmListByResourceGroup**](DedicatedHsmsApi.md#dedicatedHsmListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HardwareSecurityModules/dedicatedHSMs | 
[**dedicatedHsmListBySubscription**](DedicatedHsmsApi.md#dedicatedHsmListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.HardwareSecurityModules/dedicatedHSMs | 
[**dedicatedHsmUpdate**](DedicatedHsmsApi.md#dedicatedHsmUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HardwareSecurityModules/dedicatedHSMs/{name} | 



## dedicatedHsmCreateOrUpdate

> DedicatedHsm dedicatedHsmCreateOrUpdate(resourceGroupName, name, apiVersion, subscriptionId, parameters)



Create or Update a dedicated HSM in the specified subscription.

### Example

```javascript
import AzureDedicatedHsmResourceProvider from 'azure_dedicated_hsm_resource_provider';
let defaultClient = AzureDedicatedHsmResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDedicatedHsmResourceProvider.DedicatedHsmsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the resource belongs.
let name = "name_example"; // String | Name of the dedicated Hsm
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new AzureDedicatedHsmResourceProvider.DedicatedHsm(); // DedicatedHsm | Parameters to create or update the dedicated hsm
apiInstance.dedicatedHsmCreateOrUpdate(resourceGroupName, name, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Resource Group to which the resource belongs. | 
 **name** | **String**| Name of the dedicated Hsm | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**DedicatedHsm**](DedicatedHsm.md)| Parameters to create or update the dedicated hsm | 

### Return type

[**DedicatedHsm**](DedicatedHsm.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dedicatedHsmDelete

> dedicatedHsmDelete(resourceGroupName, name, apiVersion, subscriptionId)



Deletes the specified Azure Dedicated HSM.

### Example

```javascript
import AzureDedicatedHsmResourceProvider from 'azure_dedicated_hsm_resource_provider';
let defaultClient = AzureDedicatedHsmResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDedicatedHsmResourceProvider.DedicatedHsmsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the dedicated HSM belongs.
let name = "name_example"; // String | The name of the dedicated HSM to delete
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.dedicatedHsmDelete(resourceGroupName, name, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Resource Group to which the dedicated HSM belongs. | 
 **name** | **String**| The name of the dedicated HSM to delete | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dedicatedHsmGet

> DedicatedHsm dedicatedHsmGet(resourceGroupName, name, apiVersion, subscriptionId)



Gets the specified Azure dedicated HSM.

### Example

```javascript
import AzureDedicatedHsmResourceProvider from 'azure_dedicated_hsm_resource_provider';
let defaultClient = AzureDedicatedHsmResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDedicatedHsmResourceProvider.DedicatedHsmsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the dedicated hsm belongs.
let name = "name_example"; // String | The name of the dedicated HSM.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.dedicatedHsmGet(resourceGroupName, name, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Resource Group to which the dedicated hsm belongs. | 
 **name** | **String**| The name of the dedicated HSM. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**DedicatedHsm**](DedicatedHsm.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dedicatedHsmListByResourceGroup

> DedicatedHsmListResult dedicatedHsmListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, opts)



The List operation gets information about the dedicated hsms associated with the subscription and within the specified resource group.

### Example

```javascript
import AzureDedicatedHsmResourceProvider from 'azure_dedicated_hsm_resource_provider';
let defaultClient = AzureDedicatedHsmResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDedicatedHsmResourceProvider.DedicatedHsmsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the dedicated HSM belongs.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'top': 56 // Number | Maximum number of results to return.
};
apiInstance.dedicatedHsmListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Resource Group to which the dedicated HSM belongs. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **top** | **Number**| Maximum number of results to return. | [optional] 

### Return type

[**DedicatedHsmListResult**](DedicatedHsmListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dedicatedHsmListBySubscription

> DedicatedHsmListResult dedicatedHsmListBySubscription(apiVersion, subscriptionId, opts)



The List operation gets information about the dedicated HSMs associated with the subscription.

### Example

```javascript
import AzureDedicatedHsmResourceProvider from 'azure_dedicated_hsm_resource_provider';
let defaultClient = AzureDedicatedHsmResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDedicatedHsmResourceProvider.DedicatedHsmsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'top': 56 // Number | Maximum number of results to return.
};
apiInstance.dedicatedHsmListBySubscription(apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **top** | **Number**| Maximum number of results to return. | [optional] 

### Return type

[**DedicatedHsmListResult**](DedicatedHsmListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dedicatedHsmUpdate

> DedicatedHsm dedicatedHsmUpdate(resourceGroupName, name, apiVersion, subscriptionId, parameters)



Update a dedicated HSM in the specified subscription.

### Example

```javascript
import AzureDedicatedHsmResourceProvider from 'azure_dedicated_hsm_resource_provider';
let defaultClient = AzureDedicatedHsmResourceProvider.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureDedicatedHsmResourceProvider.DedicatedHsmsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Resource Group to which the server belongs.
let name = "name_example"; // String | Name of the dedicated HSM
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new AzureDedicatedHsmResourceProvider.DedicatedHsmPatchParameters(); // DedicatedHsmPatchParameters | Parameters to patch the dedicated HSM
apiInstance.dedicatedHsmUpdate(resourceGroupName, name, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Resource Group to which the server belongs. | 
 **name** | **String**| Name of the dedicated HSM | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**DedicatedHsmPatchParameters**](DedicatedHsmPatchParameters.md)| Parameters to patch the dedicated HSM | 

### Return type

[**DedicatedHsm**](DedicatedHsm.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

