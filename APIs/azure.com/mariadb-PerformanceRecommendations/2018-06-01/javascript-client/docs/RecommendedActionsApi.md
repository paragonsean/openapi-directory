# MariaDbManagementClient.RecommendedActionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recommendedActionsGet**](RecommendedActionsApi.md#recommendedActionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMariaDB/servers/{serverName}/advisors/{advisorName}/recommendedActions/{recommendedActionName} | 
[**recommendedActionsListByServer**](RecommendedActionsApi.md#recommendedActionsListByServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMariaDB/servers/{serverName}/advisors/{advisorName}/recommendedActions | 



## recommendedActionsGet

> RecommendationAction recommendedActionsGet(apiVersion, subscriptionId, resourceGroupName, serverName, advisorName, recommendedActionName)



Retrieve recommended actions from the advisor.

### Example

```javascript
import MariaDbManagementClient from 'maria_db_management_client';
let defaultClient = MariaDbManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MariaDbManagementClient.RecommendedActionsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let serverName = "serverName_example"; // String | The name of the server.
let advisorName = "advisorName_example"; // String | The advisor name for recommendation action.
let recommendedActionName = "recommendedActionName_example"; // String | The recommended action name.
apiInstance.recommendedActionsGet(apiVersion, subscriptionId, resourceGroupName, serverName, advisorName, recommendedActionName, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **serverName** | **String**| The name of the server. | 
 **advisorName** | **String**| The advisor name for recommendation action. | 
 **recommendedActionName** | **String**| The recommended action name. | 

### Return type

[**RecommendationAction**](RecommendationAction.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recommendedActionsListByServer

> RecommendationActionsResultList recommendedActionsListByServer(apiVersion, subscriptionId, resourceGroupName, serverName, advisorName, opts)



Retrieve recommended actions from the advisor.

### Example

```javascript
import MariaDbManagementClient from 'maria_db_management_client';
let defaultClient = MariaDbManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MariaDbManagementClient.RecommendedActionsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let serverName = "serverName_example"; // String | The name of the server.
let advisorName = "advisorName_example"; // String | The advisor name for recommendation action.
let opts = {
  'sessionId': "sessionId_example" // String | The recommendation action session identifier.
};
apiInstance.recommendedActionsListByServer(apiVersion, subscriptionId, resourceGroupName, serverName, advisorName, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **serverName** | **String**| The name of the server. | 
 **advisorName** | **String**| The advisor name for recommendation action. | 
 **sessionId** | **String**| The recommendation action session identifier. | [optional] 

### Return type

[**RecommendationActionsResultList**](RecommendationActionsResultList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

