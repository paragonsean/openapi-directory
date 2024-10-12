# MySqlManagementClient.LocationBasedRecommendedActionSessionsOperationStatusApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locationBasedRecommendedActionSessionsOperationStatusGet**](LocationBasedRecommendedActionSessionsOperationStatusApi.md#locationBasedRecommendedActionSessionsOperationStatusGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DBforMySQL/locations/{locationName}/recommendedActionSessionsAzureAsyncOperation/{operationId} | 



## locationBasedRecommendedActionSessionsOperationStatusGet

> RecommendedActionSessionsOperationStatus locationBasedRecommendedActionSessionsOperationStatusGet(apiVersion, subscriptionId, locationName, operationId)



Recommendation action session operation status.

### Example

```javascript
import MySqlManagementClient from 'my_sql_management_client';
let defaultClient = MySqlManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MySqlManagementClient.LocationBasedRecommendedActionSessionsOperationStatusApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let locationName = "locationName_example"; // String | The name of the location.
let operationId = "operationId_example"; // String | The operation identifier.
apiInstance.locationBasedRecommendedActionSessionsOperationStatusGet(apiVersion, subscriptionId, locationName, operationId, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for the request. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **locationName** | **String**| The name of the location. | 
 **operationId** | **String**| The operation identifier. | 

### Return type

[**RecommendedActionSessionsOperationStatus**](RecommendedActionSessionsOperationStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

