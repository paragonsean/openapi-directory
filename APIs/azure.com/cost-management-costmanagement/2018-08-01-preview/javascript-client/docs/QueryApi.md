# CostManagementClient.QueryApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**queryBillingAccount**](QueryApi.md#queryBillingAccount) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/Query | 
[**queryResourceGroup**](QueryApi.md#queryResourceGroup) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.CostManagement/Query | 
[**querySubscription**](QueryApi.md#querySubscription) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/Query | 



## queryBillingAccount

> QueryResult queryBillingAccount(apiVersion, billingAccountId, parameters)



Lists the usage data for billing account.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.QueryApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let parameters = new CostManagementClient.ReportDefinition(); // ReportDefinition | Parameters supplied to the CreateOrUpdate Report operation.
apiInstance.queryBillingAccount(apiVersion, billingAccountId, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | 
 **billingAccountId** | **String**| BillingAccount ID | 
 **parameters** | [**ReportDefinition**](ReportDefinition.md)| Parameters supplied to the CreateOrUpdate Report operation. | 

### Return type

[**QueryResult**](QueryResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## queryResourceGroup

> QueryResult queryResourceGroup(apiVersion, subscriptionId, resourceGroupName, parameters)



Lists the usage data for subscriptionId and resource group.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.QueryApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
let parameters = new CostManagementClient.ReportDefinition(); // ReportDefinition | Parameters supplied to the CreateOrUpdate Report operation.
apiInstance.queryResourceGroup(apiVersion, subscriptionId, resourceGroupName, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **resourceGroupName** | **String**| Azure Resource Group Name. | 
 **parameters** | [**ReportDefinition**](ReportDefinition.md)| Parameters supplied to the CreateOrUpdate Report operation. | 

### Return type

[**QueryResult**](QueryResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## querySubscription

> QueryResult querySubscription(apiVersion, subscriptionId, parameters)



Lists the usage data for subscriptionId.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.QueryApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let parameters = new CostManagementClient.ReportDefinition(); // ReportDefinition | Parameters supplied to the CreateOrUpdate Report operation.
apiInstance.querySubscription(apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **parameters** | [**ReportDefinition**](ReportDefinition.md)| Parameters supplied to the CreateOrUpdate Report operation. | 

### Return type

[**QueryResult**](QueryResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

