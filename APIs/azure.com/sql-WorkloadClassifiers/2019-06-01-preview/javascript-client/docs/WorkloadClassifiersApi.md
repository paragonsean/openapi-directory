# SqlManagementClient.WorkloadClassifiersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**workloadClassifiersCreateOrUpdate**](WorkloadClassifiersApi.md#workloadClassifiersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/workloadGroups/{workloadGroupName}/workloadClassifiers/{workloadClassifierName} | 
[**workloadClassifiersDelete**](WorkloadClassifiersApi.md#workloadClassifiersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/workloadGroups/{workloadGroupName}/workloadClassifiers/{workloadClassifierName} | 
[**workloadClassifiersGet**](WorkloadClassifiersApi.md#workloadClassifiersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/workloadGroups/{workloadGroupName}/workloadClassifiers/{workloadClassifierName} | 
[**workloadClassifiersListByWorkloadGroup**](WorkloadClassifiersApi.md#workloadClassifiersListByWorkloadGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/workloadGroups/{workloadGroupName}/workloadClassifiers | 



## workloadClassifiersCreateOrUpdate

> WorkloadClassifier workloadClassifiersCreateOrUpdate(resourceGroupName, serverName, databaseName, workloadGroupName, workloadClassifierName, subscriptionId, apiVersion, parameters)



Creates or updates a workload classifier.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.WorkloadClassifiersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database.
let workloadGroupName = "workloadGroupName_example"; // String | The name of the workload group from which to receive the classifier from.
let workloadClassifierName = "workloadClassifierName_example"; // String | The name of the workload classifier to create/update.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let parameters = new SqlManagementClient.WorkloadClassifier(); // WorkloadClassifier | The properties of the workload classifier.
apiInstance.workloadClassifiersCreateOrUpdate(resourceGroupName, serverName, databaseName, workloadGroupName, workloadClassifierName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **databaseName** | **String**| The name of the database. | 
 **workloadGroupName** | **String**| The name of the workload group from which to receive the classifier from. | 
 **workloadClassifierName** | **String**| The name of the workload classifier to create/update. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **parameters** | [**WorkloadClassifier**](WorkloadClassifier.md)| The properties of the workload classifier. | 

### Return type

[**WorkloadClassifier**](WorkloadClassifier.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## workloadClassifiersDelete

> workloadClassifiersDelete(resourceGroupName, serverName, databaseName, workloadGroupName, workloadClassifierName, subscriptionId, apiVersion)



Deletes a workload classifier.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.WorkloadClassifiersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database.
let workloadGroupName = "workloadGroupName_example"; // String | The name of the workload group from which to receive the classifier from.
let workloadClassifierName = "workloadClassifierName_example"; // String | The name of the workload classifier to delete.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.workloadClassifiersDelete(resourceGroupName, serverName, databaseName, workloadGroupName, workloadClassifierName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **databaseName** | **String**| The name of the database. | 
 **workloadGroupName** | **String**| The name of the workload group from which to receive the classifier from. | 
 **workloadClassifierName** | **String**| The name of the workload classifier to delete. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## workloadClassifiersGet

> WorkloadClassifier workloadClassifiersGet(resourceGroupName, serverName, databaseName, workloadGroupName, workloadClassifierName, subscriptionId, apiVersion)



Gets a workload classifier

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.WorkloadClassifiersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database.
let workloadGroupName = "workloadGroupName_example"; // String | The name of the workload group from which to receive the classifier from.
let workloadClassifierName = "workloadClassifierName_example"; // String | The name of the workload classifier.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.workloadClassifiersGet(resourceGroupName, serverName, databaseName, workloadGroupName, workloadClassifierName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **databaseName** | **String**| The name of the database. | 
 **workloadGroupName** | **String**| The name of the workload group from which to receive the classifier from. | 
 **workloadClassifierName** | **String**| The name of the workload classifier. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**WorkloadClassifier**](WorkloadClassifier.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workloadClassifiersListByWorkloadGroup

> WorkloadClassifierListResult workloadClassifiersListByWorkloadGroup(resourceGroupName, serverName, databaseName, workloadGroupName, subscriptionId, apiVersion)



Gets the list of workload classifiers for a workload group

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.WorkloadClassifiersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database.
let workloadGroupName = "workloadGroupName_example"; // String | The name of the workload group from which to receive the classifiers from.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.workloadClassifiersListByWorkloadGroup(resourceGroupName, serverName, databaseName, workloadGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **databaseName** | **String**| The name of the database. | 
 **workloadGroupName** | **String**| The name of the workload group from which to receive the classifiers from. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**WorkloadClassifierListResult**](WorkloadClassifierListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

