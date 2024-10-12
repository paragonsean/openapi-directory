# CostManagementClient.ForecastApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forecastUsageByBillingAccount**](ForecastApi.md#forecastUsageByBillingAccount) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/Forecast | 
[**forecastUsageByDepartment**](ForecastApi.md#forecastUsageByDepartment) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}/providers/Microsoft.CostManagement/Forecast | 
[**forecastUsageByEnrollmentAccount**](ForecastApi.md#forecastUsageByEnrollmentAccount) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}/providers/Microsoft.CostManagement/Forecast | 
[**forecastUsageByExternalBillingAccount**](ForecastApi.md#forecastUsageByExternalBillingAccount) | **POST** /providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}/Forecast | 
[**forecastUsageByManagementGroup**](ForecastApi.md#forecastUsageByManagementGroup) | **POST** /providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.CostManagement/Forecast | 
[**forecastUsageByResourceGroup**](ForecastApi.md#forecastUsageByResourceGroup) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.CostManagement/Forecast | 
[**forecastUsageBySubscription**](ForecastApi.md#forecastUsageBySubscription) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/Forecast | 



## forecastUsageByBillingAccount

> QueryResult forecastUsageByBillingAccount(apiVersion, billingAccountId, parameters)



Forecast the usage data for billing account.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ForecastApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let parameters = new CostManagementClient.ReportConfigDefinition(); // ReportConfigDefinition | Parameters supplied to the CreateOrUpdate Report Config operation.
apiInstance.forecastUsageByBillingAccount(apiVersion, billingAccountId, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-03-01-preview | 
 **billingAccountId** | **String**| BillingAccount ID | 
 **parameters** | [**ReportConfigDefinition**](ReportConfigDefinition.md)| Parameters supplied to the CreateOrUpdate Report Config operation. | 

### Return type

[**QueryResult**](QueryResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## forecastUsageByDepartment

> QueryResult forecastUsageByDepartment(apiVersion, billingAccountId, departmentId, parameters)



Forecast the usage data for department.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ForecastApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let departmentId = "departmentId_example"; // String | Department ID
let parameters = new CostManagementClient.ReportConfigDefinition(); // ReportConfigDefinition | Parameters supplied to the CreateOrUpdate Report Config operation.
apiInstance.forecastUsageByDepartment(apiVersion, billingAccountId, departmentId, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-03-01-preview | 
 **billingAccountId** | **String**| BillingAccount ID | 
 **departmentId** | **String**| Department ID | 
 **parameters** | [**ReportConfigDefinition**](ReportConfigDefinition.md)| Parameters supplied to the CreateOrUpdate Report Config operation. | 

### Return type

[**QueryResult**](QueryResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## forecastUsageByEnrollmentAccount

> QueryResult forecastUsageByEnrollmentAccount(apiVersion, billingAccountId, enrollmentAccountId, parameters)



Forecast the usage data for an enrollment account.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ForecastApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let enrollmentAccountId = "enrollmentAccountId_example"; // String | Enrollment Account ID
let parameters = new CostManagementClient.ReportConfigDefinition(); // ReportConfigDefinition | Parameters supplied to the CreateOrUpdate Report Config operation.
apiInstance.forecastUsageByEnrollmentAccount(apiVersion, billingAccountId, enrollmentAccountId, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-03-01-preview | 
 **billingAccountId** | **String**| BillingAccount ID | 
 **enrollmentAccountId** | **String**| Enrollment Account ID | 
 **parameters** | [**ReportConfigDefinition**](ReportConfigDefinition.md)| Parameters supplied to the CreateOrUpdate Report Config operation. | 

### Return type

[**QueryResult**](QueryResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## forecastUsageByExternalBillingAccount

> QueryResult forecastUsageByExternalBillingAccount(apiVersion, externalBillingAccountName, parameters)



Forecast the usage data for external billing account.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ForecastApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
let externalBillingAccountName = "externalBillingAccountName_example"; // String | External Billing Account Name. (eg 'aws-{PayerAccountId}')
let parameters = new CostManagementClient.ReportConfigDefinition(); // ReportConfigDefinition | Parameters supplied to the CreateOrUpdate Report Config operation.
apiInstance.forecastUsageByExternalBillingAccount(apiVersion, externalBillingAccountName, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-03-01-preview | 
 **externalBillingAccountName** | **String**| External Billing Account Name. (eg &#39;aws-{PayerAccountId}&#39;) | 
 **parameters** | [**ReportConfigDefinition**](ReportConfigDefinition.md)| Parameters supplied to the CreateOrUpdate Report Config operation. | 

### Return type

[**QueryResult**](QueryResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## forecastUsageByManagementGroup

> QueryResult forecastUsageByManagementGroup(apiVersion, managementGroupId, parameters)



Lists the usage data for management group.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ForecastApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
let managementGroupId = "managementGroupId_example"; // String | ManagementGroup ID
let parameters = new CostManagementClient.ReportConfigDefinition(); // ReportConfigDefinition | Parameters supplied to the CreateOrUpdate Report Config operation.
apiInstance.forecastUsageByManagementGroup(apiVersion, managementGroupId, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-03-01-preview | 
 **managementGroupId** | **String**| ManagementGroup ID | 
 **parameters** | [**ReportConfigDefinition**](ReportConfigDefinition.md)| Parameters supplied to the CreateOrUpdate Report Config operation. | 

### Return type

[**QueryResult**](QueryResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## forecastUsageByResourceGroup

> QueryResult forecastUsageByResourceGroup(apiVersion, subscriptionId, resourceGroupName, parameters)



Forecast the usage data for subscriptionId and resource group.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ForecastApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
let parameters = new CostManagementClient.ReportConfigDefinition(); // ReportConfigDefinition | Parameters supplied to the CreateOrUpdate Report Config operation.
apiInstance.forecastUsageByResourceGroup(apiVersion, subscriptionId, resourceGroupName, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-03-01-preview | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **resourceGroupName** | **String**| Azure Resource Group Name. | 
 **parameters** | [**ReportConfigDefinition**](ReportConfigDefinition.md)| Parameters supplied to the CreateOrUpdate Report Config operation. | 

### Return type

[**QueryResult**](QueryResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## forecastUsageBySubscription

> QueryResult forecastUsageBySubscription(apiVersion, subscriptionId, parameters)



Forecast the usage data for subscriptionId.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ForecastApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let parameters = new CostManagementClient.ReportConfigDefinition(); // ReportConfigDefinition | Parameters supplied to the CreateOrUpdate Report Config operation.
apiInstance.forecastUsageBySubscription(apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-03-01-preview | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **parameters** | [**ReportConfigDefinition**](ReportConfigDefinition.md)| Parameters supplied to the CreateOrUpdate Report Config operation. | 

### Return type

[**QueryResult**](QueryResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

