# MariaDbManagementClient.RecommendedActionSessionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createRecommendedActionSession**](RecommendedActionSessionsApi.md#createRecommendedActionSession) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMariaDB/servers/{serverName}/advisors/{advisorName}/createRecommendedActionSession | 



## createRecommendedActionSession

> createRecommendedActionSession(apiVersion, subscriptionId, resourceGroupName, serverName, advisorName, databaseName)



Create recommendation action session for the advisor.

### Example

```javascript
import MariaDbManagementClient from 'maria_db_management_client';
let defaultClient = MariaDbManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MariaDbManagementClient.RecommendedActionSessionsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let serverName = "serverName_example"; // String | The name of the server.
let advisorName = "advisorName_example"; // String | The advisor name for recommendation action.
let databaseName = "databaseName_example"; // String | The name of the database.
apiInstance.createRecommendedActionSession(apiVersion, subscriptionId, resourceGroupName, serverName, advisorName, databaseName, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **serverName** | **String**| The name of the server. | 
 **advisorName** | **String**| The advisor name for recommendation action. | 
 **databaseName** | **String**| The name of the database. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

