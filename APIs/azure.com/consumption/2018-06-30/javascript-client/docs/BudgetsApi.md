# ConsumptionManagementClient.BudgetsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**budgetsCreateOrUpdate**](BudgetsApi.md#budgetsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Consumption/budgets/{budgetName} | 
[**budgetsCreateOrUpdateByResourceGroupName**](BudgetsApi.md#budgetsCreateOrUpdateByResourceGroupName) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Consumption/budgets/{budgetName} | 
[**budgetsDelete**](BudgetsApi.md#budgetsDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Consumption/budgets/{budgetName} | 
[**budgetsDeleteByResourceGroupName**](BudgetsApi.md#budgetsDeleteByResourceGroupName) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Consumption/budgets/{budgetName} | 
[**budgetsGet**](BudgetsApi.md#budgetsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Consumption/budgets/{budgetName} | 
[**budgetsGetByResourceGroupName**](BudgetsApi.md#budgetsGetByResourceGroupName) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Consumption/budgets/{budgetName} | 
[**budgetsList**](BudgetsApi.md#budgetsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Consumption/budgets | 
[**budgetsListByResourceGroupName**](BudgetsApi.md#budgetsListByResourceGroupName) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Consumption/budgets | 



## budgetsCreateOrUpdate

> Budget budgetsCreateOrUpdate(apiVersion, subscriptionId, budgetName, parameters)



The operation to create or update a budget. Update operation requires latest eTag to be set in the request mandatorily. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.BudgetsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-06-30.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let budgetName = "budgetName_example"; // String | Budget Name.
let parameters = new ConsumptionManagementClient.Budget(); // Budget | Parameters supplied to the Create Budget operation.
apiInstance.budgetsCreateOrUpdate(apiVersion, subscriptionId, budgetName, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-06-30. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **budgetName** | **String**| Budget Name. | 
 **parameters** | [**Budget**](Budget.md)| Parameters supplied to the Create Budget operation. | 

### Return type

[**Budget**](Budget.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## budgetsCreateOrUpdateByResourceGroupName

> Budget budgetsCreateOrUpdateByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, budgetName, parameters)



The operation to create or update a budget. Update operation requires latest eTag to be set in the request mandatorily. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.BudgetsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-06-30.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
let budgetName = "budgetName_example"; // String | Budget Name.
let parameters = new ConsumptionManagementClient.Budget(); // Budget | Parameters supplied to the Create Budget operation.
apiInstance.budgetsCreateOrUpdateByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, budgetName, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-06-30. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **resourceGroupName** | **String**| Azure Resource Group Name. | 
 **budgetName** | **String**| Budget Name. | 
 **parameters** | [**Budget**](Budget.md)| Parameters supplied to the Create Budget operation. | 

### Return type

[**Budget**](Budget.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## budgetsDelete

> budgetsDelete(apiVersion, subscriptionId, budgetName)



The operation to delete a budget.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.BudgetsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-06-30.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let budgetName = "budgetName_example"; // String | Budget Name.
apiInstance.budgetsDelete(apiVersion, subscriptionId, budgetName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-06-30. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **budgetName** | **String**| Budget Name. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## budgetsDeleteByResourceGroupName

> budgetsDeleteByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, budgetName)



The operation to delete a budget.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.BudgetsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-06-30.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
let budgetName = "budgetName_example"; // String | Budget Name.
apiInstance.budgetsDeleteByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, budgetName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-06-30. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **resourceGroupName** | **String**| Azure Resource Group Name. | 
 **budgetName** | **String**| Budget Name. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## budgetsGet

> Budget budgetsGet(apiVersion, subscriptionId, budgetName)



Gets the budget for a subscription by budget name.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.BudgetsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-06-30.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let budgetName = "budgetName_example"; // String | Budget Name.
apiInstance.budgetsGet(apiVersion, subscriptionId, budgetName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-06-30. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **budgetName** | **String**| Budget Name. | 

### Return type

[**Budget**](Budget.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## budgetsGetByResourceGroupName

> Budget budgetsGetByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, budgetName)



Gets the budget for a resource group under a subscription by budget name.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.BudgetsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-06-30.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
let budgetName = "budgetName_example"; // String | Budget Name.
apiInstance.budgetsGetByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, budgetName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-06-30. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **resourceGroupName** | **String**| Azure Resource Group Name. | 
 **budgetName** | **String**| Budget Name. | 

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

let apiInstance = new ConsumptionManagementClient.BudgetsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-06-30.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-06-30. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 

### Return type

[**BudgetsListResult**](BudgetsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## budgetsListByResourceGroupName

> BudgetsListResult budgetsListByResourceGroupName(apiVersion, subscriptionId, resourceGroupName)



Lists all budgets for a resource group under a subscription.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.BudgetsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-06-30.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
apiInstance.budgetsListByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-06-30. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **resourceGroupName** | **String**| Azure Resource Group Name. | 

### Return type

[**BudgetsListResult**](BudgetsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

