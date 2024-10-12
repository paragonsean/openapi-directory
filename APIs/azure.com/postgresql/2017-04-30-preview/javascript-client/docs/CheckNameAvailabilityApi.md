# PostgreSqlManagementClient.CheckNameAvailabilityApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkNameAvailabilityExecute**](CheckNameAvailabilityApi.md#checkNameAvailabilityExecute) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DBforPostgreSQL/checkNameAvailability | 



## checkNameAvailabilityExecute

> NameAvailability checkNameAvailabilityExecute(apiVersion, subscriptionId, nameAvailabilityRequest)



Check the availability of name for resource

### Example

```javascript
import PostgreSqlManagementClient from 'postgre_sql_management_client';
let defaultClient = PostgreSqlManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PostgreSqlManagementClient.CheckNameAvailabilityApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let nameAvailabilityRequest = new PostgreSqlManagementClient.NameAvailabilityRequest(); // NameAvailabilityRequest | The required parameters for checking if resource name is available.
apiInstance.checkNameAvailabilityExecute(apiVersion, subscriptionId, nameAvailabilityRequest, (error, data, response) => {
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
 **nameAvailabilityRequest** | [**NameAvailabilityRequest**](NameAvailabilityRequest.md)| The required parameters for checking if resource name is available. | 

### Return type

[**NameAvailability**](NameAvailability.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

