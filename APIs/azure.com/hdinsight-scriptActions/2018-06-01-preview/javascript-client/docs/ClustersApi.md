# HdInsightManagementClient.ClustersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clustersExecuteScriptActions**](ClustersApi.md#clustersExecuteScriptActions) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}/executeScriptActions | 



## clustersExecuteScriptActions

> clustersExecuteScriptActions(subscriptionId, resourceGroupName, clusterName, apiVersion, parameters)



Executes script actions on the specified HDInsight cluster.

### Example

```javascript
import HdInsightManagementClient from 'hd_insight_management_client';
let defaultClient = HdInsightManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HdInsightManagementClient.ClustersApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let clusterName = "clusterName_example"; // String | The name of the cluster.
let apiVersion = "apiVersion_example"; // String | The HDInsight client API Version.
let parameters = new HdInsightManagementClient.ClustersExecuteScriptActionsRequest(); // ClustersExecuteScriptActionsRequest | The parameters for executing script actions.
apiInstance.clustersExecuteScriptActions(subscriptionId, resourceGroupName, clusterName, apiVersion, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| The HDInsight client API Version. | 
 **parameters** | [**ClustersExecuteScriptActionsRequest**](ClustersExecuteScriptActionsRequest.md)| The parameters for executing script actions. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

