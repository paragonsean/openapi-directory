# SignalRManagementClient.SignalRApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsList**](SignalRApi.md#operationsList) | **GET** /providers/Microsoft.SignalRService/operations | 
[**signalRCheckNameAvailability**](SignalRApi.md#signalRCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.SignalRService/locations/{location}/checkNameAvailability | 
[**signalRCreateOrUpdate**](SignalRApi.md#signalRCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.SignalRService/signalR/{resourceName} | 
[**signalRDelete**](SignalRApi.md#signalRDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.SignalRService/signalR/{resourceName} | 
[**signalRGet**](SignalRApi.md#signalRGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.SignalRService/signalR/{resourceName} | 
[**signalRListByResourceGroup**](SignalRApi.md#signalRListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.SignalRService/SignalR | 
[**signalRListBySubscription**](SignalRApi.md#signalRListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.SignalRService/SignalR | 
[**signalRListKeys**](SignalRApi.md#signalRListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.SignalRService/SignalR/{resourceName}/listKeys | 
[**signalRRegenerateKey**](SignalRApi.md#signalRRegenerateKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.SignalRService/SignalR/{resourceName}/regenerateKey | 
[**signalRRestart**](SignalRApi.md#signalRRestart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.SignalRService/signalR/{resourceName}/restart | 
[**signalRUpdate**](SignalRApi.md#signalRUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.SignalRService/signalR/{resourceName} | 
[**usagesList**](SignalRApi.md#usagesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.SignalRService/locations/{location}/usages | 



## operationsList

> OperationList operationsList(apiVersion)



Lists all of the available REST API operations of the Microsoft.SignalRService provider.

### Example

```javascript
import SignalRManagementClient from 'signal_r_management_client';
let defaultClient = SignalRManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SignalRManagementClient.SignalRApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.operationsList(apiVersion, (error, data, response) => {
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

### Return type

[**OperationList**](OperationList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## signalRCheckNameAvailability

> NameAvailability signalRCheckNameAvailability(location, apiVersion, subscriptionId, opts)



Checks that the SignalR name is valid and is not already in use.

### Example

```javascript
import SignalRManagementClient from 'signal_r_management_client';
let defaultClient = SignalRManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SignalRManagementClient.SignalRApi();
let location = "location_example"; // String | the region
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'parameters': new SignalRManagementClient.NameAvailabilityParameters() // NameAvailabilityParameters | Parameters supplied to the operation.
};
apiInstance.signalRCheckNameAvailability(location, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **location** | **String**| the region | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**NameAvailabilityParameters**](NameAvailabilityParameters.md)| Parameters supplied to the operation. | [optional] 

### Return type

[**NameAvailability**](NameAvailability.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## signalRCreateOrUpdate

> SignalRResource signalRCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, opts)



Create a new SignalR service and update an exiting SignalR service.

### Example

```javascript
import SignalRManagementClient from 'signal_r_management_client';
let defaultClient = SignalRManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SignalRManagementClient.SignalRApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let resourceName = "resourceName_example"; // String | The name of the SignalR resource.
let opts = {
  'parameters': new SignalRManagementClient.SignalRCreateParameters() // SignalRCreateParameters | Parameters for the create or update operation
};
apiInstance.signalRCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **resourceName** | **String**| The name of the SignalR resource. | 
 **parameters** | [**SignalRCreateParameters**](SignalRCreateParameters.md)| Parameters for the create or update operation | [optional] 

### Return type

[**SignalRResource**](SignalRResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## signalRDelete

> signalRDelete(apiVersion, subscriptionId, resourceGroupName, resourceName)



Operation to delete a SignalR service.

### Example

```javascript
import SignalRManagementClient from 'signal_r_management_client';
let defaultClient = SignalRManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SignalRManagementClient.SignalRApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let resourceName = "resourceName_example"; // String | The name of the SignalR resource.
apiInstance.signalRDelete(apiVersion, subscriptionId, resourceGroupName, resourceName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **resourceName** | **String**| The name of the SignalR resource. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## signalRGet

> SignalRResource signalRGet(apiVersion, subscriptionId, resourceGroupName, resourceName)



Get the SignalR service and its properties.

### Example

```javascript
import SignalRManagementClient from 'signal_r_management_client';
let defaultClient = SignalRManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SignalRManagementClient.SignalRApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let resourceName = "resourceName_example"; // String | The name of the SignalR resource.
apiInstance.signalRGet(apiVersion, subscriptionId, resourceGroupName, resourceName, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **resourceName** | **String**| The name of the SignalR resource. | 

### Return type

[**SignalRResource**](SignalRResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## signalRListByResourceGroup

> SignalRResourceList signalRListByResourceGroup(apiVersion, subscriptionId, resourceGroupName)



Handles requests to list all resources in a resource group.

### Example

```javascript
import SignalRManagementClient from 'signal_r_management_client';
let defaultClient = SignalRManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SignalRManagementClient.SignalRApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
apiInstance.signalRListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 

### Return type

[**SignalRResourceList**](SignalRResourceList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## signalRListBySubscription

> SignalRResourceList signalRListBySubscription(apiVersion, subscriptionId)



Handles requests to list all resources in a subscription.

### Example

```javascript
import SignalRManagementClient from 'signal_r_management_client';
let defaultClient = SignalRManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SignalRManagementClient.SignalRApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.signalRListBySubscription(apiVersion, subscriptionId, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**SignalRResourceList**](SignalRResourceList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## signalRListKeys

> SignalRKeys signalRListKeys(apiVersion, subscriptionId, resourceGroupName, resourceName)



Get the access keys of the SignalR resource.

### Example

```javascript
import SignalRManagementClient from 'signal_r_management_client';
let defaultClient = SignalRManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SignalRManagementClient.SignalRApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let resourceName = "resourceName_example"; // String | The name of the SignalR resource.
apiInstance.signalRListKeys(apiVersion, subscriptionId, resourceGroupName, resourceName, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **resourceName** | **String**| The name of the SignalR resource. | 

### Return type

[**SignalRKeys**](SignalRKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## signalRRegenerateKey

> SignalRKeys signalRRegenerateKey(apiVersion, subscriptionId, resourceGroupName, resourceName, opts)



Regenerate SignalR service access key. PrimaryKey and SecondaryKey cannot be regenerated at the same time.

### Example

```javascript
import SignalRManagementClient from 'signal_r_management_client';
let defaultClient = SignalRManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SignalRManagementClient.SignalRApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let resourceName = "resourceName_example"; // String | The name of the SignalR resource.
let opts = {
  'parameters': new SignalRManagementClient.RegenerateKeyParameters() // RegenerateKeyParameters | Parameter that describes the Regenerate Key Operation.
};
apiInstance.signalRRegenerateKey(apiVersion, subscriptionId, resourceGroupName, resourceName, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **resourceName** | **String**| The name of the SignalR resource. | 
 **parameters** | [**RegenerateKeyParameters**](RegenerateKeyParameters.md)| Parameter that describes the Regenerate Key Operation. | [optional] 

### Return type

[**SignalRKeys**](SignalRKeys.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## signalRRestart

> signalRRestart(apiVersion, subscriptionId, resourceGroupName, resourceName)



Operation to restart a SignalR service.

### Example

```javascript
import SignalRManagementClient from 'signal_r_management_client';
let defaultClient = SignalRManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SignalRManagementClient.SignalRApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let resourceName = "resourceName_example"; // String | The name of the SignalR resource.
apiInstance.signalRRestart(apiVersion, subscriptionId, resourceGroupName, resourceName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **resourceName** | **String**| The name of the SignalR resource. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## signalRUpdate

> SignalRResource signalRUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, opts)



Operation to update an exiting SignalR service.

### Example

```javascript
import SignalRManagementClient from 'signal_r_management_client';
let defaultClient = SignalRManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SignalRManagementClient.SignalRApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let resourceName = "resourceName_example"; // String | The name of the SignalR resource.
let opts = {
  'parameters': new SignalRManagementClient.SignalRUpdateParameters() // SignalRUpdateParameters | Parameters for the update operation
};
apiInstance.signalRUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **resourceName** | **String**| The name of the SignalR resource. | 
 **parameters** | [**SignalRUpdateParameters**](SignalRUpdateParameters.md)| Parameters for the update operation | [optional] 

### Return type

[**SignalRResource**](SignalRResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## usagesList

> SignalRUsageList usagesList(location, apiVersion, subscriptionId)



List usage quotas for Azure SignalR service by location.

### Example

```javascript
import SignalRManagementClient from 'signal_r_management_client';
let defaultClient = SignalRManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SignalRManagementClient.SignalRApi();
let location = "location_example"; // String | the location like \"eastus\"
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.usagesList(location, apiVersion, subscriptionId, (error, data, response) => {
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
 **location** | **String**| the location like \&quot;eastus\&quot; | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription Id which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**SignalRUsageList**](SignalRUsageList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

