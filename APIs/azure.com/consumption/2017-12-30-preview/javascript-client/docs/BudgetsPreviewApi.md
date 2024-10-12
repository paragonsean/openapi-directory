# ConsumptionManagementClient.BudgetsPreviewApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**budgetsCreateOrUpdate**](BudgetsPreviewApi.md#budgetsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Consumption/budgets/{name} | 
[**budgetsDelete**](BudgetsPreviewApi.md#budgetsDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Consumption/budgets/{name} | 
[**budgetsGet**](BudgetsPreviewApi.md#budgetsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Consumption/budgets/{name} | 
[**budgetsList**](BudgetsPreviewApi.md#budgetsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Consumption/budgets | 



## budgetsCreateOrUpdate

> Budget budgetsCreateOrUpdate(apiVersion, subscriptionId, name, parameters)



The operation to create or update a budget. Update operation requires latest eTag to be set in the request mandatorily. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.BudgetsPreviewApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2017-12-30-preview.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let name = "name_example"; // String | Budget name.
let parameters = new ConsumptionManagementClient.Budget(); // Budget | Parameters supplied to the Create Budget operation.
apiInstance.budgetsCreateOrUpdate(apiVersion, subscriptionId, name, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2017-12-30-preview. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **name** | **String**| Budget name. | 
 **parameters** | [**Budget**](Budget.md)| Parameters supplied to the Create Budget operation. | 

### Return type

[**Budget**](Budget.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## budgetsDelete

> budgetsDelete(apiVersion, subscriptionId, name)



The operation to delete a budget.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.BudgetsPreviewApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2017-12-30-preview.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let name = "name_example"; // String | Budget name.
apiInstance.budgetsDelete(apiVersion, subscriptionId, name, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2017-12-30-preview. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **name** | **String**| Budget name. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## budgetsGet

> Budget budgetsGet(apiVersion, subscriptionId, name)



Gets the budget for a subscription by budget name.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.BudgetsPreviewApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2017-12-30-preview.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let name = "name_example"; // String | Budget name.
apiInstance.budgetsGet(apiVersion, subscriptionId, name, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2017-12-30-preview. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **name** | **String**| Budget name. | 

### Return type

[**Budget**](Budget.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## budgetsList

> BudgetsListResult budgetsList(apiVersion, subscriptionId)



Lists all budgets for a subscription.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.BudgetsPreviewApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2017-12-30-preview.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
apiInstance.budgetsList(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2017-12-30-preview. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 

### Return type

[**BudgetsListResult**](BudgetsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

