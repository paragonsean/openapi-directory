# AutomationManagement.NodeReportsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nodeReportsGet**](NodeReportsApi.md#nodeReportsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/nodes/{nodeId}/reports/{reportId} | 
[**nodeReportsGetContent**](NodeReportsApi.md#nodeReportsGetContent) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/nodes/{nodeId}/reports/{reportId}/content | 
[**nodeReportsListByNode**](NodeReportsApi.md#nodeReportsListByNode) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Automation/automationAccounts/{automationAccountName}/nodes/{nodeId}/reports | 



## nodeReportsGet

> DscNodeReport nodeReportsGet(resourceGroupName, automationAccountName, nodeId, reportId, subscriptionId, apiVersion)



Retrieve the Dsc node report data by node id and report id.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.NodeReportsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let nodeId = "nodeId_example"; // String | The Dsc node id.
let reportId = "reportId_example"; // String | The report id.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.nodeReportsGet(resourceGroupName, automationAccountName, nodeId, reportId, subscriptionId, apiVersion, (error, data, response) => {
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
 **nodeId** | **String**| The Dsc node id. | 
 **reportId** | **String**| The report id. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**DscNodeReport**](DscNodeReport.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nodeReportsGetContent

> Object nodeReportsGetContent(resourceGroupName, automationAccountName, nodeId, reportId, subscriptionId, apiVersion)



Retrieve the Dsc node reports by node id and report id.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.NodeReportsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let nodeId = "nodeId_example"; // String | The Dsc node id.
let reportId = "reportId_example"; // String | The report id.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.nodeReportsGetContent(resourceGroupName, automationAccountName, nodeId, reportId, subscriptionId, apiVersion, (error, data, response) => {
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
 **nodeId** | **String**| The Dsc node id. | 
 **reportId** | **String**| The report id. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## nodeReportsListByNode

> DscNodeReportListResult nodeReportsListByNode(resourceGroupName, automationAccountName, nodeId, subscriptionId, apiVersion, opts)



Retrieve the Dsc node report list by node id.

### Example

```javascript
import AutomationManagement from 'automation_management';
let defaultClient = AutomationManagement.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AutomationManagement.NodeReportsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of an Azure Resource group.
let automationAccountName = "automationAccountName_example"; // String | The name of the automation account.
let nodeId = "nodeId_example"; // String | The parameters supplied to the list operation.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the operation.
};
apiInstance.nodeReportsListByNode(resourceGroupName, automationAccountName, nodeId, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **nodeId** | **String**| The parameters supplied to the list operation. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| The filter to apply on the operation. | [optional] 

### Return type

[**DscNodeReportListResult**](DscNodeReportListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

