# UpdateManagement.SoftwareUpdateConfigurationApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**softwareUpdateConfigurationsCreate**](SoftwareUpdateConfigurationApi.md#softwareUpdateConfigurationsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/softwareUpdateConfigurations/{softwareUpdateConfigurationName} | 
[**softwareUpdateConfigurationsDelete**](SoftwareUpdateConfigurationApi.md#softwareUpdateConfigurationsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/softwareUpdateConfigurations/{softwareUpdateConfigurationName} | 
[**softwareUpdateConfigurationsGetByName**](SoftwareUpdateConfigurationApi.md#softwareUpdateConfigurationsGetByName) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/softwareUpdateConfigurations/{softwareUpdateConfigurationName} | 
[**softwareUpdateConfigurationsList**](SoftwareUpdateConfigurationApi.md#softwareUpdateConfigurationsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/softwareUpdateConfigurations | 



## softwareUpdateConfigurationsCreate

> SoftwareUpdateConfiguration softwareUpdateConfigurationsCreate(subscriptionId, resourceGroupName, automationAccountName, softwareUpdateConfigurationName, apiVersion, parameters, opts)



Create a new software update configuration with the name given in the URI.

### Example

```javascript
import UpdateManagement from 'update_management';
let defaultClient = UpdateManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new UpdateManagement.SoftwareUpdateConfigurationApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let softwareUpdateConfigurationName = "softwareUpdateConfigurationName_example"; // String | The name of the software update configuration to be created.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new UpdateManagement.SoftwareUpdateConfiguration(); // SoftwareUpdateConfiguration | Request body.
let opts = {
  'clientRequestId': "clientRequestId_example" // String | Identifies this specific client request.
};
apiInstance.softwareUpdateConfigurationsCreate(subscriptionId, resourceGroupName, automationAccountName, softwareUpdateConfigurationName, apiVersion, parameters, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of an Azure Resource group. | 
 **automationAccountName** | **String**| The name of the automation account. | 
 **softwareUpdateConfigurationName** | **String**| The name of the software update configuration to be created. | 
 **apiVersion** | **String**| Client Api Version. | 
 **parameters** | [**SoftwareUpdateConfiguration**](SoftwareUpdateConfiguration.md)| Request body. | 
 **clientRequestId** | **String**| Identifies this specific client request. | [optional] 

### Return type

[**SoftwareUpdateConfiguration**](SoftwareUpdateConfiguration.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## softwareUpdateConfigurationsDelete

> softwareUpdateConfigurationsDelete(subscriptionId, resourceGroupName, automationAccountName, softwareUpdateConfigurationName, apiVersion, opts)



delete a specific software update configuration.

### Example

```javascript
import UpdateManagement from 'update_management';
let defaultClient = UpdateManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new UpdateManagement.SoftwareUpdateConfigurationApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let softwareUpdateConfigurationName = "softwareUpdateConfigurationName_example"; // String | The name of the software update configuration to be created.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'clientRequestId': "clientRequestId_example" // String | Identifies this specific client request.
};
apiInstance.softwareUpdateConfigurationsDelete(subscriptionId, resourceGroupName, automationAccountName, softwareUpdateConfigurationName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of an Azure Resource group. | 
 **automationAccountName** | **String**| The name of the automation account. | 
 **softwareUpdateConfigurationName** | **String**| The name of the software update configuration to be created. | 
 **apiVersion** | **String**| Client Api Version. | 
 **clientRequestId** | **String**| Identifies this specific client request. | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## softwareUpdateConfigurationsGetByName

> SoftwareUpdateConfiguration softwareUpdateConfigurationsGetByName(subscriptionId, resourceGroupName, automationAccountName, softwareUpdateConfigurationName, apiVersion, opts)



Get a single software update configuration by name.

### Example

```javascript
import UpdateManagement from 'update_management';
let defaultClient = UpdateManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new UpdateManagement.SoftwareUpdateConfigurationApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let softwareUpdateConfigurationName = "softwareUpdateConfigurationName_example"; // String | The name of the software update configuration to be created.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'clientRequestId': "clientRequestId_example" // String | Identifies this specific client request.
};
apiInstance.softwareUpdateConfigurationsGetByName(subscriptionId, resourceGroupName, automationAccountName, softwareUpdateConfigurationName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of an Azure Resource group. | 
 **automationAccountName** | **String**| The name of the automation account. | 
 **softwareUpdateConfigurationName** | **String**| The name of the software update configuration to be created. | 
 **apiVersion** | **String**| Client Api Version. | 
 **clientRequestId** | **String**| Identifies this specific client request. | [optional] 

### Return type

[**SoftwareUpdateConfiguration**](SoftwareUpdateConfiguration.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## softwareUpdateConfigurationsList

> SoftwareUpdateConfigurationListResult softwareUpdateConfigurationsList(subscriptionId, resourceGroupName, automationAccountName, apiVersion, opts)



Get all software update configurations for the account.

### Example

```javascript
import UpdateManagement from 'update_management';
let defaultClient = UpdateManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new UpdateManagement.SoftwareUpdateConfigurationApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'clientRequestId': "clientRequestId_example", // String | Identifies this specific client request.
  'filter': "filter_example" // String | The filter to apply on the operation.
};
apiInstance.softwareUpdateConfigurationsList(subscriptionId, resourceGroupName, automationAccountName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| Name of an Azure Resource group. | 
 **automationAccountName** | **String**| The name of the automation account. | 
 **apiVersion** | **String**| Client Api Version. | 
 **clientRequestId** | **String**| Identifies this specific client request. | [optional] 
 **filter** | **String**| The filter to apply on the operation. | [optional] 

### Return type

[**SoftwareUpdateConfigurationListResult**](SoftwareUpdateConfigurationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

