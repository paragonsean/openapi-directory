# UpdateManagement.SoftwareUpdateConfigurationRunApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**softwareUpdateConfigurationRunsGetById**](SoftwareUpdateConfigurationRunApi.md#softwareUpdateConfigurationRunsGetById) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/softwareUpdateConfigurationRuns/{softwareUpdateConfigurationRunId} | 
[**softwareUpdateConfigurationRunsList**](SoftwareUpdateConfigurationRunApi.md#softwareUpdateConfigurationRunsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/softwareUpdateConfigurationRuns | 



## softwareUpdateConfigurationRunsGetById

> SoftwareUpdateConfigurationRun softwareUpdateConfigurationRunsGetById(subscriptionId, resourceGroupName, automationAccountName, softwareUpdateConfigurationRunId, apiVersion, opts)



Get a single software update configuration Run by Id.

### Example

```javascript
import UpdateManagement from 'update_management';
let defaultClient = UpdateManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new UpdateManagement.SoftwareUpdateConfigurationRunApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let softwareUpdateConfigurationRunId = "softwareUpdateConfigurationRunId_example"; // String | The Id of the software update configuration run.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'clientRequestId': "clientRequestId_example" // String | Identifies this specific client request.
};
apiInstance.softwareUpdateConfigurationRunsGetById(subscriptionId, resourceGroupName, automationAccountName, softwareUpdateConfigurationRunId, apiVersion, opts, (error, data, response) => {
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
 **softwareUpdateConfigurationRunId** | **String**| The Id of the software update configuration run. | 
 **apiVersion** | **String**| Client Api Version. | 
 **clientRequestId** | **String**| Identifies this specific client request. | [optional] 

### Return type

[**SoftwareUpdateConfigurationRun**](SoftwareUpdateConfigurationRun.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## softwareUpdateConfigurationRunsList

> SoftwareUpdateConfigurationRunListResult softwareUpdateConfigurationRunsList(subscriptionId, resourceGroupName, automationAccountName, apiVersion, opts)



Return list of software update configuration runs

### Example

```javascript
import UpdateManagement from 'update_management';
let defaultClient = UpdateManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new UpdateManagement.SoftwareUpdateConfigurationRunApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'clientRequestId': "clientRequestId_example", // String | Identifies this specific client request.
  'filter': "filter_example", // String | The filter to apply on the operation. You can use the following filters: 'properties/osType', 'properties/status', 'properties/startTime', and 'properties/softwareUpdateConfiguration/name'
  'skip': "skip_example", // String | Number of entries you skip before returning results
  'top': "top_example" // String | Maximum number of entries returned in the results collection
};
apiInstance.softwareUpdateConfigurationRunsList(subscriptionId, resourceGroupName, automationAccountName, apiVersion, opts, (error, data, response) => {
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
 **filter** | **String**| The filter to apply on the operation. You can use the following filters: &#39;properties/osType&#39;, &#39;properties/status&#39;, &#39;properties/startTime&#39;, and &#39;properties/softwareUpdateConfiguration/name&#39; | [optional] 
 **skip** | **String**| Number of entries you skip before returning results | [optional] 
 **top** | **String**| Maximum number of entries returned in the results collection | [optional] 

### Return type

[**SoftwareUpdateConfigurationRunListResult**](SoftwareUpdateConfigurationRunListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

