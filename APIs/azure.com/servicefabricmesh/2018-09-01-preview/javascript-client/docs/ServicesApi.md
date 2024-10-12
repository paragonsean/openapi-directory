# SeaBreezeManagementClient.ServicesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serviceGet**](ServicesApi.md#serviceGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/applications/{applicationResourceName}/services/{serviceResourceName} | Gets the service resource with the given name.
[**serviceList**](ServicesApi.md#serviceList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabricMesh/applications/{applicationResourceName}/services | Lists all the service resources.



## serviceGet

> ServiceResourceDescription serviceGet(subscriptionId, apiVersion, resourceGroupName, applicationResourceName, serviceResourceName)

Gets the service resource with the given name.

Gets the information about the service resource with the given name. The information include the description and other properties of the service.

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.ServicesApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-09-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let applicationResourceName = "applicationResourceName_example"; // String | The identity of the application.
let serviceResourceName = "serviceResourceName_example"; // String | The identity of the service.
apiInstance.serviceGet(subscriptionId, apiVersion, resourceGroupName, applicationResourceName, serviceResourceName, (error, data, response) => {
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
 **subscriptionId** | **String**| The customer subscription identifier | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;. | [default to &#39;2018-09-01-preview&#39;]
 **resourceGroupName** | **String**| Azure resource group name | 
 **applicationResourceName** | **String**| The identity of the application. | 
 **serviceResourceName** | **String**| The identity of the service. | 

### Return type

[**ServiceResourceDescription**](ServiceResourceDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceList

> ServiceResourceDescriptionList serviceList(subscriptionId, apiVersion, resourceGroupName, applicationResourceName)

Lists all the service resources.

Gets the information about all services of an application resource. The information include the description and other properties of the Service.

### Example

```javascript
import SeaBreezeManagementClient from 'sea_breeze_management_client';
let defaultClient = SeaBreezeManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeaBreezeManagementClient.ServicesApi();
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let apiVersion = "'2018-09-01-preview'"; // String | The version of the API. This parameter is required and its value must be `2018-09-01-preview`.
let resourceGroupName = "resourceGroupName_example"; // String | Azure resource group name
let applicationResourceName = "applicationResourceName_example"; // String | The identity of the application.
apiInstance.serviceList(subscriptionId, apiVersion, resourceGroupName, applicationResourceName, (error, data, response) => {
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
 **subscriptionId** | **String**| The customer subscription identifier | 
 **apiVersion** | **String**| The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;. | [default to &#39;2018-09-01-preview&#39;]
 **resourceGroupName** | **String**| Azure resource group name | 
 **applicationResourceName** | **String**| The identity of the application. | 

### Return type

[**ServiceResourceDescriptionList**](ServiceResourceDescriptionList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

