# MonitorManagementClient.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autoscaleSettingsUpdate**](DefaultApi.md#autoscaleSettingsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/microsoft.insights/autoscalesettings/{autoscaleSettingName} | 



## autoscaleSettingsUpdate

> AutoscaleSettingResource autoscaleSettingsUpdate(subscriptionId, resourceGroupName, autoscaleSettingName, apiVersion, autoscaleSettingResource)



Updates an existing AutoscaleSettingsResource. To update other fields use the CreateOrUpdate method.

### Example

```javascript
import MonitorManagementClient from 'monitor_management_client';
let defaultClient = MonitorManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MonitorManagementClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let autoscaleSettingName = "autoscaleSettingName_example"; // String | The autoscale setting name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let autoscaleSettingResource = new MonitorManagementClient.AutoscaleSettingResourcePatch(); // AutoscaleSettingResourcePatch | Parameters supplied to the operation.
apiInstance.autoscaleSettingsUpdate(subscriptionId, resourceGroupName, autoscaleSettingName, apiVersion, autoscaleSettingResource, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription Id. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **autoscaleSettingName** | **String**| The autoscale setting name. | 
 **apiVersion** | **String**| Client Api Version. | 
 **autoscaleSettingResource** | [**AutoscaleSettingResourcePatch**](AutoscaleSettingResourcePatch.md)| Parameters supplied to the operation. | 

### Return type

[**AutoscaleSettingResource**](AutoscaleSettingResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

