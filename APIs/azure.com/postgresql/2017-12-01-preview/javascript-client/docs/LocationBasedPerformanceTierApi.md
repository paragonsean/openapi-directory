# PostgreSqlManagementClient.LocationBasedPerformanceTierApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**locationBasedPerformanceTierList**](LocationBasedPerformanceTierApi.md#locationBasedPerformanceTierList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DBforPostgreSQL/locations/{locationName}/performanceTiers | 



## locationBasedPerformanceTierList

> PerformanceTierListResult locationBasedPerformanceTierList(apiVersion, subscriptionId, locationName)



List all the performance tiers at specified location in a given subscription.

### Example

```javascript
import PostgreSqlManagementClient from 'postgre_sql_management_client';
let defaultClient = PostgreSqlManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PostgreSqlManagementClient.LocationBasedPerformanceTierApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let locationName = "locationName_example"; // String | The name of the location.
apiInstance.locationBasedPerformanceTierList(apiVersion, subscriptionId, locationName, (error, data, response) => {
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

### Return type

[**PerformanceTierListResult**](PerformanceTierListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

