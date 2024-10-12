# AutomationManagement.SourceControlSyncJobApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sourceControlSyncJobCreate**](SourceControlSyncJobApi.md#sourceControlSyncJobCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/sourceControls/{sourceControlName}/sourceControlSyncJobs/{sourceControlSyncJobId} | 
[**sourceControlSyncJobGet**](SourceControlSyncJobApi.md#sourceControlSyncJobGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/sourceControls/{sourceControlName}/sourceControlSyncJobs/{sourceControlSyncJobId} | 
[**sourceControlSyncJobListByAutomationAccount**](SourceControlSyncJobApi.md#sourceControlSyncJobListByAutomationAccount) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/sourceControls/{sourceControlName}/sourceControlSyncJobs | 



## sourceControlSyncJobCreate

> SourceControlSyncJob sourceControlSyncJobCreate(resourceGroupName, automationAccountName, sourceControlName, sourceControlSyncJobId, subscriptionId, apiVersion, parameters)



Creates the sync job for a source control.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.SourceControlSyncJobApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let sourceControlName = "sourceControlName_example"; // String | The source control name.
let sourceControlSyncJobId = "sourceControlSyncJobId_example"; // String | The source control sync job id.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new AutomationManagement.SourceControlSyncJobCreateParameters(); // SourceControlSyncJobCreateParameters | The parameters supplied to the create source control sync job operation.
apiInstance.sourceControlSyncJobCreate(resourceGroupName, automationAccountName, sourceControlName, sourceControlSyncJobId, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **sourceControlName** | **String**| The source control name. | 
 **sourceControlSyncJobId** | **String**| The source control sync job id. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | 
 **parameters** | [**SourceControlSyncJobCreateParameters**](SourceControlSyncJobCreateParameters.md)| The parameters supplied to the create source control sync job operation. | 

### Return type

[**SourceControlSyncJob**](SourceControlSyncJob.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sourceControlSyncJobGet

> SourceControlSyncJobById sourceControlSyncJobGet(resourceGroupName, automationAccountName, sourceControlName, sourceControlSyncJobId, subscriptionId, apiVersion)



Retrieve the source control sync job identified by job id.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.SourceControlSyncJobApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let sourceControlName = "sourceControlName_example"; // String | The source control name.
let sourceControlSyncJobId = "sourceControlSyncJobId_example"; // String | The source control sync job id.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.sourceControlSyncJobGet(resourceGroupName, automationAccountName, sourceControlName, sourceControlSyncJobId, subscriptionId, apiVersion, (error, data, response) => {
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
 **sourceControlName** | **String**| The source control name. | 
 **sourceControlSyncJobId** | **String**| The source control sync job id. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**SourceControlSyncJobById**](SourceControlSyncJobById.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sourceControlSyncJobListByAutomationAccount

> SourceControlSyncJobListResult sourceControlSyncJobListByAutomationAccount(resourceGroupName, automationAccountName, sourceControlName, subscriptionId, apiVersion, opts)



Retrieve a list of source control sync jobs.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.SourceControlSyncJobApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let sourceControlName = "sourceControlName_example"; // String | The source control name.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the operation.
};
apiInstance.sourceControlSyncJobListByAutomationAccount(resourceGroupName, automationAccountName, sourceControlName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **sourceControlName** | **String**| The source control name. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| The filter to apply on the operation. | [optional] 

### Return type

[**SourceControlSyncJobListResult**](SourceControlSyncJobListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

