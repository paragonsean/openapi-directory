# AutomationManagement.JobStreamApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jobStreamGet**](JobStreamApi.md#jobStreamGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/jobs/{jobName}/streams/{jobStreamId} | 
[**jobStreamListByJob**](JobStreamApi.md#jobStreamListByJob) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/jobs/{jobName}/streams | 



## jobStreamGet

> JobStream jobStreamGet(subscriptionId, resourceGroupName, automationAccountName, jobName, jobStreamId, apiVersion, opts)



Retrieve the job stream identified by job stream id.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.JobStreamApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let jobName = "jobName_example"; // String | The job name.
let jobStreamId = "jobStreamId_example"; // String | The job stream id.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'clientRequestId': "clientRequestId_example" // String | Identifies this specific client request.
};
apiInstance.jobStreamGet(subscriptionId, resourceGroupName, automationAccountName, jobName, jobStreamId, apiVersion, opts, (error, data, response) => {
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
 **jobName** | **String**| The job name. | 
 **jobStreamId** | **String**| The job stream id. | 
 **apiVersion** | **String**| Client Api Version. | 
 **clientRequestId** | **String**| Identifies this specific client request. | [optional] 

### Return type

[**JobStream**](JobStream.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jobStreamListByJob

> JobStreamListResult jobStreamListByJob(resourceGroupName, automationAccountName, jobName, subscriptionId, apiVersion, opts)



Retrieve a list of jobs streams identified by job name.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.JobStreamApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let jobName = "jobName_example"; // String | The job name.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | The filter to apply on the operation.
  'clientRequestId': "clientRequestId_example" // String | Identifies this specific client request.
};
apiInstance.jobStreamListByJob(resourceGroupName, automationAccountName, jobName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of an Azure Resource group. | 
 **automationAccountName** | **String**| The name of the automation account. | 
 **jobName** | **String**| The job name. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| The filter to apply on the operation. | [optional] 
 **clientRequestId** | **String**| Identifies this specific client request. | [optional] 

### Return type

[**JobStreamListResult**](JobStreamListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

