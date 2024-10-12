# SqlManagementClient.DatabaseRecommendedActionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**databaseRecommendedActionsGet**](DatabaseRecommendedActionsApi.md#databaseRecommendedActionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/advisors/{advisorName}/recommendedActions/{recommendedActionName} | 
[**databaseRecommendedActionsListByDatabaseAdvisor**](DatabaseRecommendedActionsApi.md#databaseRecommendedActionsListByDatabaseAdvisor) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/advisors/{advisorName}/recommendedActions | 
[**databaseRecommendedActionsUpdate**](DatabaseRecommendedActionsApi.md#databaseRecommendedActionsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/advisors/{advisorName}/recommendedActions/{recommendedActionName} | 



## databaseRecommendedActionsGet

> RecommendedAction databaseRecommendedActionsGet(resourceGroupName, serverName, databaseName, advisorName, recommendedActionName, subscriptionId, apiVersion)



Gets a database recommended action.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.DatabaseRecommendedActionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database.
let advisorName = "advisorName_example"; // String | The name of the Database Advisor.
let recommendedActionName = "recommendedActionName_example"; // String | The name of Database Recommended Action.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.databaseRecommendedActionsGet(resourceGroupName, serverName, databaseName, advisorName, recommendedActionName, subscriptionId, apiVersion, (error, data, response) => {
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
 **advisorName** | **String**| The name of the Database Advisor. | 
 **recommendedActionName** | **String**| The name of Database Recommended Action. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**RecommendedAction**](RecommendedAction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseRecommendedActionsListByDatabaseAdvisor

> [RecommendedAction] databaseRecommendedActionsListByDatabaseAdvisor(resourceGroupName, serverName, databaseName, advisorName, subscriptionId, apiVersion)



Gets list of Database Recommended Actions.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.DatabaseRecommendedActionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database.
let advisorName = "advisorName_example"; // String | The name of the Database Advisor.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.databaseRecommendedActionsListByDatabaseAdvisor(resourceGroupName, serverName, databaseName, advisorName, subscriptionId, apiVersion, (error, data, response) => {
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
 **advisorName** | **String**| The name of the Database Advisor. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**[RecommendedAction]**](RecommendedAction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseRecommendedActionsUpdate

> RecommendedAction databaseRecommendedActionsUpdate(resourceGroupName, serverName, databaseName, advisorName, recommendedActionName, subscriptionId, apiVersion, parameters)



Updates a database recommended action.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.DatabaseRecommendedActionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database.
let advisorName = "advisorName_example"; // String | The name of the Database Advisor.
let recommendedActionName = "recommendedActionName_example"; // String | The name of Database Recommended Action.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let parameters = new SqlManagementClient.RecommendedAction(); // RecommendedAction | The requested recommended action resource state.
apiInstance.databaseRecommendedActionsUpdate(resourceGroupName, serverName, databaseName, advisorName, recommendedActionName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **advisorName** | **String**| The name of the Database Advisor. | 
 **recommendedActionName** | **String**| The name of Database Recommended Action. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **parameters** | [**RecommendedAction**](RecommendedAction.md)| The requested recommended action resource state. | 

### Return type

[**RecommendedAction**](RecommendedAction.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

