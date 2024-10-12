# AppConfigurationManagementClient.OperationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**operationsCheckNameAvailability**](OperationsApi.md#operationsCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.AppConfiguration/checkNameAvailability | 
[**operationsList**](OperationsApi.md#operationsList) | **GET** /providers/Microsoft.AppConfiguration/operations | 



## operationsCheckNameAvailability

> NameAvailabilityStatus operationsCheckNameAvailability(subscriptionId, apiVersion, checkNameAvailabilityParameters)



Checks whether the configuration store name is available for use.

### Example

```javascript
import AppConfigurationManagementClient from 'app_configuration_management_client';
let defaultClient = AppConfigurationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppConfigurationManagementClient.OperationsApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
let checkNameAvailabilityParameters = new AppConfigurationManagementClient.CheckNameAvailabilityParameters(); // CheckNameAvailabilityParameters | The object containing information for the availability request.
apiInstance.operationsCheckNameAvailability(subscriptionId, apiVersion, checkNameAvailabilityParameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **apiVersion** | **String**| The client API version. | 
 **checkNameAvailabilityParameters** | [**CheckNameAvailabilityParameters**](CheckNameAvailabilityParameters.md)| The object containing information for the availability request. | 

### Return type

[**NameAvailabilityStatus**](NameAvailabilityStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## operationsList

> OperationDefinitionListResult operationsList(apiVersion, opts)



Lists the operations available from this provider.

### Example

```javascript
import AppConfigurationManagementClient from 'app_configuration_management_client';
let defaultClient = AppConfigurationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppConfigurationManagementClient.OperationsApi();
let apiVersion = "apiVersion_example"; // String | The client API version.
let opts = {
  'skipToken': "skipToken_example" // String | A skip token is used to continue retrieving items after an operation returns a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skipToken parameter that specifies a starting point to use for subsequent calls.
};
apiInstance.operationsList(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The client API version. | 
 **skipToken** | **String**| A skip token is used to continue retrieving items after an operation returns a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skipToken parameter that specifies a starting point to use for subsequent calls. | [optional] 

### Return type

[**OperationDefinitionListResult**](OperationDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

