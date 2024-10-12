# CostManagementClient.ReportsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reportsCreateOrUpdate**](ReportsApi.md#reportsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/reports/{reportName} | 
[**reportsCreateOrUpdateByBillingAccount**](ReportsApi.md#reportsCreateOrUpdateByBillingAccount) | **PUT** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/reports/{reportName} | 
[**reportsCreateOrUpdateByDepartment**](ReportsApi.md#reportsCreateOrUpdateByDepartment) | **PUT** /providers/Microsoft.Billing/departments/{departmentId}/providers/Microsoft.CostManagement/reports/{reportName} | 
[**reportsCreateOrUpdateByResourceGroupName**](ReportsApi.md#reportsCreateOrUpdateByResourceGroupName) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CostManagement/reports/{reportName} | 
[**reportsDelete**](ReportsApi.md#reportsDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/reports/{reportName} | 
[**reportsDeleteByBillingAccount**](ReportsApi.md#reportsDeleteByBillingAccount) | **DELETE** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/reports/{reportName} | 
[**reportsDeleteByDepartment**](ReportsApi.md#reportsDeleteByDepartment) | **DELETE** /providers/Microsoft.Billing/departments/{departmentId}/providers/Microsoft.CostManagement/reports/{reportName} | 
[**reportsDeleteByResourceGroupName**](ReportsApi.md#reportsDeleteByResourceGroupName) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CostManagement/reports/{reportName} | 
[**reportsExecute**](ReportsApi.md#reportsExecute) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/reports/{reportName}/run | 
[**reportsExecuteByBillingAccount**](ReportsApi.md#reportsExecuteByBillingAccount) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/reports/{reportName}/run | 
[**reportsExecuteByDepartment**](ReportsApi.md#reportsExecuteByDepartment) | **POST** /providers/Microsoft.Billing/departments/{departmentId}/providers/Microsoft.CostManagement/reports/{reportName}/run | 
[**reportsExecuteByResourceGroupName**](ReportsApi.md#reportsExecuteByResourceGroupName) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CostManagement/reports/{reportName}/run | 
[**reportsGet**](ReportsApi.md#reportsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/reports/{reportName} | 
[**reportsGetByBillingAccount**](ReportsApi.md#reportsGetByBillingAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/reports/{reportName} | 
[**reportsGetByDepartment**](ReportsApi.md#reportsGetByDepartment) | **GET** /providers/Microsoft.Billing/departments/{departmentId}/providers/Microsoft.CostManagement/reports/{reportName} | 
[**reportsGetByResourceGroupName**](ReportsApi.md#reportsGetByResourceGroupName) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CostManagement/reports/{reportName} | 
[**reportsGetExecutionHistory**](ReportsApi.md#reportsGetExecutionHistory) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/reports/{reportName}/runHistory | 
[**reportsGetExecutionHistoryByBillingAccount**](ReportsApi.md#reportsGetExecutionHistoryByBillingAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/reports/{reportName}/runHistory | 
[**reportsGetExecutionHistoryByDepartment**](ReportsApi.md#reportsGetExecutionHistoryByDepartment) | **GET** /providers/Microsoft.Billing/departments/{departmentId}/providers/Microsoft.CostManagement/reports/{reportName}/runHistory | 
[**reportsGetExecutionHistoryByResourceGroupName**](ReportsApi.md#reportsGetExecutionHistoryByResourceGroupName) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CostManagement/reports/{reportName}/runHistory | 
[**reportsList**](ReportsApi.md#reportsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/reports | 
[**reportsListByBillingAccount**](ReportsApi.md#reportsListByBillingAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/reports | 
[**reportsListByDepartment**](ReportsApi.md#reportsListByDepartment) | **GET** /providers/Microsoft.Billing/departments/{departmentId}/providers/Microsoft.CostManagement/reports | 
[**reportsListByResourceGroupName**](ReportsApi.md#reportsListByResourceGroupName) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CostManagement/reports | 



## reportsCreateOrUpdate

> Report reportsCreateOrUpdate(apiVersion, subscriptionId, reportName, parameters)



The operation to create or update a report. Update operation requires latest eTag to be set in the request mandatorily. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ReportsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let reportName = "reportName_example"; // String | Report Name.
let parameters = new CostManagementClient.Report(); // Report | Parameters supplied to the CreateOrUpdate Report operation.
apiInstance.reportsCreateOrUpdate(apiVersion, subscriptionId, reportName, parameters, (error, data, response) => {
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
 **reportName** | **String**| Report Name. | 
 **parameters** | [**Report**](Report.md)| Parameters supplied to the CreateOrUpdate Report operation. | 

### Return type

[**Report**](Report.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## reportsCreateOrUpdateByBillingAccount

> Report reportsCreateOrUpdateByBillingAccount(apiVersion, billingAccountId, reportName, parameters)



The operation to create or update a report for billingAccount. Update operation requires latest eTag to be set in the request mandatorily. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ReportsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let reportName = "reportName_example"; // String | Report Name.
let parameters = new CostManagementClient.Report(); // Report | Parameters supplied to the CreateOrUpdate Report operation.
apiInstance.reportsCreateOrUpdateByBillingAccount(apiVersion, billingAccountId, reportName, parameters, (error, data, response) => {
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
 **reportName** | **String**| Report Name. | 
 **parameters** | [**Report**](Report.md)| Parameters supplied to the CreateOrUpdate Report operation. | 

### Return type

[**Report**](Report.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## reportsCreateOrUpdateByDepartment

> Report reportsCreateOrUpdateByDepartment(apiVersion, departmentId, reportName, parameters)



The operation to create or update a report for department. Update operation requires latest eTag to be set in the request mandatorily. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ReportsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let departmentId = "departmentId_example"; // String | Department ID
let reportName = "reportName_example"; // String | Report Name.
let parameters = new CostManagementClient.Report(); // Report | Parameters supplied to the CreateOrUpdate Report operation.
apiInstance.reportsCreateOrUpdateByDepartment(apiVersion, departmentId, reportName, parameters, (error, data, response) => {
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
 **departmentId** | **String**| Department ID | 
 **reportName** | **String**| Report Name. | 
 **parameters** | [**Report**](Report.md)| Parameters supplied to the CreateOrUpdate Report operation. | 

### Return type

[**Report**](Report.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## reportsCreateOrUpdateByResourceGroupName

> Report reportsCreateOrUpdateByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, reportName, parameters)



The operation to create or update a report. Update operation requires latest eTag to be set in the request mandatorily. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ReportsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
let reportName = "reportName_example"; // String | Report Name.
let parameters = new CostManagementClient.Report(); // Report | Parameters supplied to the CreateOrUpdate Report operation.
apiInstance.reportsCreateOrUpdateByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, reportName, parameters, (error, data, response) => {
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
 **reportName** | **String**| Report Name. | 
 **parameters** | [**Report**](Report.md)| Parameters supplied to the CreateOrUpdate Report operation. | 

### Return type

[**Report**](Report.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## reportsDelete

> reportsDelete(apiVersion, subscriptionId, reportName)



The operation to delete a report.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ReportsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let reportName = "reportName_example"; // String | Report Name.
apiInstance.reportsDelete(apiVersion, subscriptionId, reportName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **reportName** | **String**| Report Name. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportsDeleteByBillingAccount

> reportsDeleteByBillingAccount(apiVersion, billingAccountId, reportName)



The operation to delete a report for billing account.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ReportsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let reportName = "reportName_example"; // String | Report Name.
apiInstance.reportsDeleteByBillingAccount(apiVersion, billingAccountId, reportName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | 
 **billingAccountId** | **String**| BillingAccount ID | 
 **reportName** | **String**| Report Name. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportsDeleteByDepartment

> reportsDeleteByDepartment(apiVersion, departmentId, reportName)



The operation to delete a report for department.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ReportsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let departmentId = "departmentId_example"; // String | Department ID
let reportName = "reportName_example"; // String | Report Name.
apiInstance.reportsDeleteByDepartment(apiVersion, departmentId, reportName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | 
 **departmentId** | **String**| Department ID | 
 **reportName** | **String**| Report Name. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportsDeleteByResourceGroupName

> reportsDeleteByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, reportName)



The operation to delete a report.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ReportsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
let reportName = "reportName_example"; // String | Report Name.
apiInstance.reportsDeleteByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, reportName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **resourceGroupName** | **String**| Azure Resource Group Name. | 
 **reportName** | **String**| Report Name. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportsExecute

> reportsExecute(apiVersion, subscriptionId, reportName)



The operation to execute a report.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ReportsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let reportName = "reportName_example"; // String | Report Name.
apiInstance.reportsExecute(apiVersion, subscriptionId, reportName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **reportName** | **String**| Report Name. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportsExecuteByBillingAccount

> reportsExecuteByBillingAccount(apiVersion, billingAccountId, reportName)



The operation to execute a report by billing account.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ReportsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let reportName = "reportName_example"; // String | Report Name.
apiInstance.reportsExecuteByBillingAccount(apiVersion, billingAccountId, reportName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | 
 **billingAccountId** | **String**| BillingAccount ID | 
 **reportName** | **String**| Report Name. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportsExecuteByDepartment

> reportsExecuteByDepartment(apiVersion, departmentId, reportName)



The operation to execute a report by department.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ReportsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let departmentId = "departmentId_example"; // String | Department ID
let reportName = "reportName_example"; // String | Report Name.
apiInstance.reportsExecuteByDepartment(apiVersion, departmentId, reportName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | 
 **departmentId** | **String**| Department ID | 
 **reportName** | **String**| Report Name. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportsExecuteByResourceGroupName

> reportsExecuteByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, reportName)



The operation to execute a report.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ReportsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
let reportName = "reportName_example"; // String | Report Name.
apiInstance.reportsExecuteByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, reportName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **resourceGroupName** | **String**| Azure Resource Group Name. | 
 **reportName** | **String**| Report Name. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportsGet

> Report reportsGet(apiVersion, subscriptionId, reportName)



Gets the report for a subscription by report name.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ReportsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let reportName = "reportName_example"; // String | Report Name.
apiInstance.reportsGet(apiVersion, subscriptionId, reportName, (error, data, response) => {
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
 **reportName** | **String**| Report Name. | 

### Return type

[**Report**](Report.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportsGetByBillingAccount

> Report reportsGetByBillingAccount(apiVersion, billingAccountId, reportName)



Gets the report for a billing account by report name.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ReportsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let reportName = "reportName_example"; // String | Report Name.
apiInstance.reportsGetByBillingAccount(apiVersion, billingAccountId, reportName, (error, data, response) => {
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
 **reportName** | **String**| Report Name. | 

### Return type

[**Report**](Report.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportsGetByDepartment

> Report reportsGetByDepartment(apiVersion, departmentId, reportName)



Gets the report for a department by report name.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ReportsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let departmentId = "departmentId_example"; // String | Department ID
let reportName = "reportName_example"; // String | Report Name.
apiInstance.reportsGetByDepartment(apiVersion, departmentId, reportName, (error, data, response) => {
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
 **departmentId** | **String**| Department ID | 
 **reportName** | **String**| Report Name. | 

### Return type

[**Report**](Report.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportsGetByResourceGroupName

> Report reportsGetByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, reportName)



Gets the report for a resource group under a subscription by report name.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ReportsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
let reportName = "reportName_example"; // String | Report Name.
apiInstance.reportsGetByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, reportName, (error, data, response) => {
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
 **reportName** | **String**| Report Name. | 

### Return type

[**Report**](Report.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportsGetExecutionHistory

> ReportExecutionListResult reportsGetExecutionHistory(apiVersion, subscriptionId, reportName)



Gets the execution history of a report for a subscription by report name.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ReportsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let reportName = "reportName_example"; // String | Report Name.
apiInstance.reportsGetExecutionHistory(apiVersion, subscriptionId, reportName, (error, data, response) => {
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
 **reportName** | **String**| Report Name. | 

### Return type

[**ReportExecutionListResult**](ReportExecutionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportsGetExecutionHistoryByBillingAccount

> ReportExecutionListResult reportsGetExecutionHistoryByBillingAccount(apiVersion, billingAccountId, reportName)



Gets the execution history of a report for a billing account by report name.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ReportsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let reportName = "reportName_example"; // String | Report Name.
apiInstance.reportsGetExecutionHistoryByBillingAccount(apiVersion, billingAccountId, reportName, (error, data, response) => {
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
 **reportName** | **String**| Report Name. | 

### Return type

[**ReportExecutionListResult**](ReportExecutionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportsGetExecutionHistoryByDepartment

> ReportExecutionListResult reportsGetExecutionHistoryByDepartment(apiVersion, departmentId, reportName)



Gets the execution history of a report for a department by report name.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ReportsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let departmentId = "departmentId_example"; // String | Department ID
let reportName = "reportName_example"; // String | Report Name.
apiInstance.reportsGetExecutionHistoryByDepartment(apiVersion, departmentId, reportName, (error, data, response) => {
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
 **departmentId** | **String**| Department ID | 
 **reportName** | **String**| Report Name. | 

### Return type

[**ReportExecutionListResult**](ReportExecutionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportsGetExecutionHistoryByResourceGroupName

> ReportExecutionListResult reportsGetExecutionHistoryByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, reportName)



Gets the execution history of a report for a resource group by report name.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ReportsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
let reportName = "reportName_example"; // String | Report Name.
apiInstance.reportsGetExecutionHistoryByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, reportName, (error, data, response) => {
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
 **reportName** | **String**| Report Name. | 

### Return type

[**ReportExecutionListResult**](ReportExecutionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportsList

> ReportListResult reportsList(apiVersion, subscriptionId)



Lists all reports for a subscription.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ReportsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
apiInstance.reportsList(apiVersion, subscriptionId, (error, data, response) => {
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

### Return type

[**ReportListResult**](ReportListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportsListByBillingAccount

> ReportListResult reportsListByBillingAccount(apiVersion, billingAccountId)



Lists all reports for a billing account.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ReportsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
apiInstance.reportsListByBillingAccount(apiVersion, billingAccountId, (error, data, response) => {
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

### Return type

[**ReportListResult**](ReportListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportsListByDepartment

> ReportListResult reportsListByDepartment(apiVersion, departmentId)



Lists all reports for a department.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ReportsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let departmentId = "departmentId_example"; // String | Department ID
apiInstance.reportsListByDepartment(apiVersion, departmentId, (error, data, response) => {
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
 **departmentId** | **String**| Department ID | 

### Return type

[**ReportListResult**](ReportListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportsListByResourceGroupName

> ReportListResult reportsListByResourceGroupName(apiVersion, subscriptionId, resourceGroupName)



Lists all reports for a resource group under a subscription.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ReportsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
apiInstance.reportsListByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, (error, data, response) => {
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

### Return type

[**ReportListResult**](ReportListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

