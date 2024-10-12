# AzureBridgeAdminClient.ActivationsApi

All URIs are relative to *https://adminmanagement.local.azurestack.external*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activationsCreateOrUpdate**](ActivationsApi.md#activationsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroup}/providers/Microsoft.AzureBridge.Admin/activations/{activationName} | 
[**activationsDelete**](ActivationsApi.md#activationsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroup}/providers/Microsoft.AzureBridge.Admin/activations/{activationName} | 
[**activationsGet**](ActivationsApi.md#activationsGet) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroup}/providers/Microsoft.AzureBridge.Admin/activations/{activationName} | 
[**activationsList**](ActivationsApi.md#activationsList) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroup}/providers/Microsoft.AzureBridge.Admin/activations | 



## activationsCreateOrUpdate

> ActivationResource activationsCreateOrUpdate(subscriptionId, resourceGroup, activationName, apiVersion, activation)



Create a new activation.

### Example

```javascript
import AzureBridgeAdminClient from 'azure_bridge_admin_client';
let defaultClient = AzureBridgeAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureBridgeAdminClient.ActivationsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let resourceGroup = "resourceGroup_example"; // String | The resource group the resource is located under.
let activationName = "activationName_example"; // String | Name of the activation.
let apiVersion = "'2016-01-01'"; // String | Client Api Version.
let activation = new AzureBridgeAdminClient.Activation(); // Activation | new activation.
apiInstance.activationsCreateOrUpdate(subscriptionId, resourceGroup, activationName, apiVersion, activation, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | 
 **resourceGroup** | **String**| The resource group the resource is located under. | 
 **activationName** | **String**| Name of the activation. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2016-01-01&#39;]
 **activation** | [**Activation**](Activation.md)| new activation. | 

### Return type

[**ActivationResource**](ActivationResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## activationsDelete

> ActivationResource activationsDelete(subscriptionId, resourceGroup, activationName, apiVersion)



Delete an activation.

### Example

```javascript
import AzureBridgeAdminClient from 'azure_bridge_admin_client';
let defaultClient = AzureBridgeAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureBridgeAdminClient.ActivationsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let resourceGroup = "resourceGroup_example"; // String | The resource group the resource is located under.
let activationName = "activationName_example"; // String | Name of the activation.
let apiVersion = "'2016-01-01'"; // String | Client Api Version.
apiInstance.activationsDelete(subscriptionId, resourceGroup, activationName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | 
 **resourceGroup** | **String**| The resource group the resource is located under. | 
 **activationName** | **String**| Name of the activation. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2016-01-01&#39;]

### Return type

[**ActivationResource**](ActivationResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## activationsGet

> ActivationResource activationsGet(subscriptionId, resourceGroup, activationName, apiVersion)



Returns activation name.

### Example

```javascript
import AzureBridgeAdminClient from 'azure_bridge_admin_client';
let defaultClient = AzureBridgeAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureBridgeAdminClient.ActivationsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let resourceGroup = "resourceGroup_example"; // String | The resource group the resource is located under.
let activationName = "activationName_example"; // String | Name of the activation.
let apiVersion = "'2016-01-01'"; // String | Client Api Version.
apiInstance.activationsGet(subscriptionId, resourceGroup, activationName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | 
 **resourceGroup** | **String**| The resource group the resource is located under. | 
 **activationName** | **String**| Name of the activation. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2016-01-01&#39;]

### Return type

[**ActivationResource**](ActivationResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## activationsList

> ActivationResourcesPage activationsList(subscriptionId, resourceGroup, apiVersion)



Returns the list of activations.

### Example

```javascript
import AzureBridgeAdminClient from 'azure_bridge_admin_client';
let defaultClient = AzureBridgeAdminClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureBridgeAdminClient.ActivationsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call.
let resourceGroup = "resourceGroup_example"; // String | The resource group the resource is located under.
let apiVersion = "'2016-01-01'"; // String | Client Api Version.
apiInstance.activationsList(subscriptionId, resourceGroup, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription credentials which uniquely identify Microsoft Azure subscription.The subscription ID forms part of the URI for every service call. | 
 **resourceGroup** | **String**| The resource group the resource is located under. | 
 **apiVersion** | **String**| Client Api Version. | [default to &#39;2016-01-01&#39;]

### Return type

[**ActivationResourcesPage**](ActivationResourcesPage.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

