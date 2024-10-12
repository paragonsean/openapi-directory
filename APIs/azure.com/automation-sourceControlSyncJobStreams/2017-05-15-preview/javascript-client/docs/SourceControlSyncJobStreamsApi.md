# AutomationManagement.SourceControlSyncJobStreamsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sourceControlSyncJobStreamsGet**](SourceControlSyncJobStreamsApi.md#sourceControlSyncJobStreamsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/sourceControls/{sourceControlName}/sourceControlSyncJobs/{sourceControlSyncJobId}/streams/{streamId} | 
[**sourceControlSyncJobStreamsListBySyncJob**](SourceControlSyncJobStreamsApi.md#sourceControlSyncJobStreamsListBySyncJob) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/sourceControls/{sourceControlName}/sourceControlSyncJobs/{sourceControlSyncJobId}/streams | 



## sourceControlSyncJobStreamsGet

> SourceControlSyncJobStreamById sourceControlSyncJobStreamsGet(resourceGroupName, automationAccountName, sourceControlName, sourceControlSyncJobId, streamId, subscriptionId, apiVersion)



Retrieve a sync job stream identified by stream id.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.SourceControlSyncJobStreamsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let sourceControlName = "sourceControlName_example"; // String | The source control name.
let sourceControlSyncJobId = "sourceControlSyncJobId_example"; // String | The source control sync job id.
let streamId = "streamId_example"; // String | The id of the sync job stream.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.sourceControlSyncJobStreamsGet(resourceGroupName, automationAccountName, sourceControlName, sourceControlSyncJobId, streamId, subscriptionId, apiVersion, (error, data, response) => {
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
 **streamId** | **String**| The id of the sync job stream. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**SourceControlSyncJobStreamById**](SourceControlSyncJobStreamById.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sourceControlSyncJobStreamsListBySyncJob

> SourceControlSyncJobStreamsListBySyncJob sourceControlSyncJobStreamsListBySyncJob(resourceGroupName, automationAccountName, sourceControlName, sourceControlSyncJobId, subscriptionId, apiVersion, opts)



Retrieve a list of sync job streams identified by sync job id.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.SourceControlSyncJobStreamsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let sourceControlName = "sourceControlName_example"; // String | The source control name.
let sourceControlSyncJobId = "sourceControlSyncJobId_example"; // String | The source control sync job id.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the operation.
};
apiInstance.sourceControlSyncJobStreamsListBySyncJob(resourceGroupName, automationAccountName, sourceControlName, sourceControlSyncJobId, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **filter** | **String**| The filter to apply on the operation. | [optional] 

### Return type

[**SourceControlSyncJobStreamsListBySyncJob**](SourceControlSyncJobStreamsListBySyncJob.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

