# HdInsightManagementClient.PromoteApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**scriptExecutionHistoryPromote**](PromoteApi.md#scriptExecutionHistoryPromote) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HDInsight/clusters/{clusterName}/scriptExecutionHistory/{scriptExecutionId}/promote | 



## scriptExecutionHistoryPromote

> scriptExecutionHistoryPromote(subscriptionId, resourceGroupName, clusterName, scriptExecutionId, apiVersion)



Promotes the specified ad-hoc script execution to a persisted script.

### Example

```javascript
import HdInsightManagementClient from 'hd_insight_management_client';
let defaultClient = HdInsightManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HdInsightManagementClient.PromoteApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let clusterName = "clusterName_example"; // String | The name of the cluster.
let scriptExecutionId = "scriptExecutionId_example"; // String | The script execution Id
let apiVersion = "apiVersion_example"; // String | The HDInsight client API Version.
apiInstance.scriptExecutionHistoryPromote(subscriptionId, resourceGroupName, clusterName, scriptExecutionId, apiVersion, (error, data, response) => {
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
 **scriptExecutionId** | **String**| The script execution Id | 
 **apiVersion** | **String**| The HDInsight client API Version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

