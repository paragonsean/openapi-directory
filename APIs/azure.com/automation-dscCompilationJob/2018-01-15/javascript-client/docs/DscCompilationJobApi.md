# AutomationManagement.DscCompilationJobApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dscCompilationJobCreate**](DscCompilationJobApi.md#dscCompilationJobCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/compilationjobs/{compilationJobName} | 
[**dscCompilationJobGet**](DscCompilationJobApi.md#dscCompilationJobGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/compilationjobs/{compilationJobName} | 
[**dscCompilationJobGetStream**](DscCompilationJobApi.md#dscCompilationJobGetStream) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/compilationjobs/{jobId}/streams/{jobStreamId} | 
[**dscCompilationJobListByAutomationAccount**](DscCompilationJobApi.md#dscCompilationJobListByAutomationAccount) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/compilationjobs | 
[**dscCompilationJobStreamListByJob**](DscCompilationJobApi.md#dscCompilationJobStreamListByJob) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/compilationjobs/{jobId}/streams | 



## dscCompilationJobCreate

> DscCompilationJob dscCompilationJobCreate(resourceGroupName, automationAccountName, compilationJobName, subscriptionId, apiVersion, parameters)



Creates the Dsc compilation job of the configuration.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.DscCompilationJobApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let compilationJobName = "compilationJobName_example"; // String | The DSC configuration Id.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new AutomationManagement.DscCompilationJobCreateParameters(); // DscCompilationJobCreateParameters | The parameters supplied to the create compilation job operation.
apiInstance.dscCompilationJobCreate(resourceGroupName, automationAccountName, compilationJobName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **compilationJobName** | **String**| The DSC configuration Id. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | 
 **parameters** | [**DscCompilationJobCreateParameters**](DscCompilationJobCreateParameters.md)| The parameters supplied to the create compilation job operation. | 

### Return type

[**DscCompilationJob**](DscCompilationJob.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dscCompilationJobGet

> DscCompilationJob dscCompilationJobGet(resourceGroupName, automationAccountName, compilationJobName, subscriptionId, apiVersion)



Retrieve the Dsc configuration compilation job identified by job id.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.DscCompilationJobApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let compilationJobName = "compilationJobName_example"; // String | The DSC configuration Id.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.dscCompilationJobGet(resourceGroupName, automationAccountName, compilationJobName, subscriptionId, apiVersion, (error, data, response) => {
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
 **compilationJobName** | **String**| The DSC configuration Id. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**DscCompilationJob**](DscCompilationJob.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dscCompilationJobGetStream

> JobStream dscCompilationJobGetStream(resourceGroupName, automationAccountName, jobId, jobStreamId, subscriptionId, apiVersion)



Retrieve the job stream identified by job stream id.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.DscCompilationJobApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let jobId = "jobId_example"; // String | The job id.
let jobStreamId = "jobStreamId_example"; // String | The job stream id.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.dscCompilationJobGetStream(resourceGroupName, automationAccountName, jobId, jobStreamId, subscriptionId, apiVersion, (error, data, response) => {
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
 **jobId** | **String**| The job id. | 
 **jobStreamId** | **String**| The job stream id. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**JobStream**](JobStream.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dscCompilationJobListByAutomationAccount

> DscCompilationJobListResult dscCompilationJobListByAutomationAccount(resourceGroupName, automationAccountName, subscriptionId, apiVersion, opts)



Retrieve a list of dsc compilation jobs.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.DscCompilationJobApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the operation.
};
apiInstance.dscCompilationJobListByAutomationAccount(resourceGroupName, automationAccountName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| The filter to apply on the operation. | [optional] 

### Return type

[**DscCompilationJobListResult**](DscCompilationJobListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dscCompilationJobStreamListByJob

> JobStreamListResult dscCompilationJobStreamListByJob(resourceGroupName, automationAccountName, jobId, subscriptionId, apiVersion)



Retrieve all the job streams for the compilation Job.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.DscCompilationJobApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let jobId = "jobId_example"; // String | The job id.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.dscCompilationJobStreamListByJob(resourceGroupName, automationAccountName, jobId, subscriptionId, apiVersion, (error, data, response) => {
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
 **jobId** | **String**| The job id. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**JobStreamListResult**](JobStreamListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

