# AutomationManagement.RunbookDraftApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**runbookDraftGet**](RunbookDraftApi.md#runbookDraftGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/runbooks/{runbookName}/draft | 
[**runbookDraftGetContent**](RunbookDraftApi.md#runbookDraftGetContent) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/runbooks/{runbookName}/draft/content | 
[**runbookDraftPublish**](RunbookDraftApi.md#runbookDraftPublish) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/runbooks/{runbookName}/draft/publish | 
[**runbookDraftReplaceContent**](RunbookDraftApi.md#runbookDraftReplaceContent) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/runbooks/{runbookName}/draft/content | 
[**runbookDraftUndoEdit**](RunbookDraftApi.md#runbookDraftUndoEdit) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/runbooks/{runbookName}/draft/undoEdit | 



## runbookDraftGet

> RunbookDraft runbookDraftGet(subscriptionId, resourceGroupName, automationAccountName, runbookName, apiVersion)



Retrieve the runbook draft identified by runbook name.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.RunbookDraftApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let runbookName = "runbookName_example"; // String | The runbook name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.runbookDraftGet(subscriptionId, resourceGroupName, automationAccountName, runbookName, apiVersion, (error, data, response) => {
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

### Return type

[**RunbookDraft**](RunbookDraft.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## runbookDraftGetContent

> File runbookDraftGetContent(subscriptionId, resourceGroupName, automationAccountName, runbookName, apiVersion)



Retrieve the content of runbook draft identified by runbook name.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.RunbookDraftApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let runbookName = "runbookName_example"; // String | The runbook name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.runbookDraftGetContent(subscriptionId, resourceGroupName, automationAccountName, runbookName, apiVersion, (error, data, response) => {
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

### Return type

**File**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/powershell


## runbookDraftPublish

> runbookDraftPublish(subscriptionId, resourceGroupName, automationAccountName, runbookName, apiVersion)



Publish runbook draft.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.RunbookDraftApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let runbookName = "runbookName_example"; // String | The parameters supplied to the publish runbook operation.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.runbookDraftPublish(subscriptionId, resourceGroupName, automationAccountName, runbookName, apiVersion, (error, data, response) => {
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
 **runbookName** | **String**| The parameters supplied to the publish runbook operation. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## runbookDraftReplaceContent

> File runbookDraftReplaceContent(subscriptionId, resourceGroupName, automationAccountName, runbookName, apiVersion, runbookContent)



Replaces the runbook draft content.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.RunbookDraftApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let runbookName = "runbookName_example"; // String | The runbook name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let runbookContent = {key: null}; // Object | The runbook draft content.
apiInstance.runbookDraftReplaceContent(subscriptionId, resourceGroupName, automationAccountName, runbookName, apiVersion, runbookContent, (error, data, response) => {
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
 **runbookContent** | **Object**| The runbook draft content. | 

### Return type

**File**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: text/powershell
- **Accept**: application/json


## runbookDraftUndoEdit

> RunbookDraftUndoEditResult runbookDraftUndoEdit(subscriptionId, resourceGroupName, automationAccountName, runbookName, apiVersion)



Undo draft edit to last known published state identified by runbook name.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.RunbookDraftApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let runbookName = "runbookName_example"; // String | The runbook name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.runbookDraftUndoEdit(subscriptionId, resourceGroupName, automationAccountName, runbookName, apiVersion, (error, data, response) => {
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

### Return type

[**RunbookDraftUndoEditResult**](RunbookDraftUndoEditResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

