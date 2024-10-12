# AutomationManagement.TestJobStreamApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**testJobStreamsGet**](TestJobStreamApi.md#testJobStreamsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/runbooks/{runbookName}/draft/testJob/streams/{jobStreamId} | 
[**testJobStreamsListByTestJob**](TestJobStreamApi.md#testJobStreamsListByTestJob) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/runbooks/{runbookName}/draft/testJob/streams | 



## testJobStreamsGet

> TestJobStreamsListByTestJob200ResponseValueInner testJobStreamsGet(subscriptionId, resourceGroupName, automationAccountName, runbookName, jobStreamId, apiVersion)



Retrieve a test job stream of the test job identified by runbook name and stream id.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.TestJobStreamApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let runbookName = "runbookName_example"; // String | The runbook name.
let jobStreamId = "jobStreamId_example"; // String | The job stream id.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.testJobStreamsGet(subscriptionId, resourceGroupName, automationAccountName, runbookName, jobStreamId, apiVersion, (error, data, response) => {
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
 **runbookName** | **String**| The runbook name. | 
 **jobStreamId** | **String**| The job stream id. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**TestJobStreamsListByTestJob200ResponseValueInner**](TestJobStreamsListByTestJob200ResponseValueInner.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## testJobStreamsListByTestJob

> TestJobStreamsListByTestJob200Response testJobStreamsListByTestJob(subscriptionId, resourceGroupName, automationAccountName, runbookName, apiVersion, opts)



Retrieve a list of test job streams identified by runbook name.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.TestJobStreamApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let runbookName = "runbookName_example"; // String | The runbook name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the operation.
};
apiInstance.testJobStreamsListByTestJob(subscriptionId, resourceGroupName, automationAccountName, runbookName, apiVersion, opts, (error, data, response) => {
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
 **runbookName** | **String**| The runbook name. | 
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| The filter to apply on the operation. | [optional] 

### Return type

[**TestJobStreamsListByTestJob200Response**](TestJobStreamsListByTestJob200Response.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

