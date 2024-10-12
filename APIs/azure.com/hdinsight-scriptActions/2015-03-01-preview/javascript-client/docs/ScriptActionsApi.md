# HdInsightManagementClient.ScriptActionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scriptActionsDelete**](ScriptActionsApi.md#scriptActionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}/scriptActions/{scriptName} | 
[**scriptActionsListPersistedScripts**](ScriptActionsApi.md#scriptActionsListPersistedScripts) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}/scriptActions | 



## scriptActionsDelete

> scriptActionsDelete(subscriptionId, resourceGroupName, clusterName, scriptName, apiVersion)



Deletes a specified persisted script action of the cluster.

### Example

```javascript
import HdInsightManagementClient from 'hd_insight_management_client';
let defaultClient = HdInsightManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HdInsightManagementClient.ScriptActionsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let clusterName = "clusterName_example"; // String | The name of the cluster.
let scriptName = "scriptName_example"; // String | The name of the script.
let apiVersion = "apiVersion_example"; // String | The HDInsight client API Version.
apiInstance.scriptActionsDelete(subscriptionId, resourceGroupName, clusterName, scriptName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **clusterName** | **String**| The name of the cluster. | 
 **scriptName** | **String**| The name of the script. | 
 **apiVersion** | **String**| The HDInsight client API Version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## scriptActionsListPersistedScripts

> ScriptActionsList scriptActionsListPersistedScripts(subscriptionId, resourceGroupName, clusterName, apiVersion)



Lists all the persisted script actions for the specified cluster.

### Example

```javascript
import HdInsightManagementClient from 'hd_insight_management_client';
let defaultClient = HdInsightManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HdInsightManagementClient.ScriptActionsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let clusterName = "clusterName_example"; // String | The name of the cluster.
let apiVersion = "apiVersion_example"; // String | The HDInsight client API Version.
apiInstance.scriptActionsListPersistedScripts(subscriptionId, resourceGroupName, clusterName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **clusterName** | **String**| The name of the cluster. | 
 **apiVersion** | **String**| The HDInsight client API Version. | 

### Return type

[**ScriptActionsList**](ScriptActionsList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

