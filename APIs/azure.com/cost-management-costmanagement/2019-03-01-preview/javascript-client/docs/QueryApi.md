# CostManagementClient.QueryApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**queryUsageByBillingAccount**](QueryApi.md#queryUsageByBillingAccount) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/Query | 
[**queryUsageByDepartment**](QueryApi.md#queryUsageByDepartment) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}/providers/Microsoft.CostManagement/Query | 
[**queryUsageByEnrollmentAccount**](QueryApi.md#queryUsageByEnrollmentAccount) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}/providers/Microsoft.CostManagement/Query | 
[**queryUsageByManagementGroup**](QueryApi.md#queryUsageByManagementGroup) | **POST** /providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.CostManagement/Query | 
[**queryUsageByResourceGroup**](QueryApi.md#queryUsageByResourceGroup) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.CostManagement/Query | 
[**queryUsageBySubscription**](QueryApi.md#queryUsageBySubscription) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/Query | 



## queryUsageByBillingAccount

> QueryResult queryUsageByBillingAccount(apiVersion, billingAccountId, parameters)



Query the usage data for billing account.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.QueryApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let parameters = new CostManagementClient.ReportConfigDefinition(); // ReportConfigDefinition | Parameters supplied to the CreateOrUpdate Report Config operation.
apiInstance.queryUsageByBillingAccount(apiVersion, billingAccountId, parameters, (error, data, response) => {
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


## queryUsageByDepartment

> QueryResult queryUsageByDepartment(apiVersion, billingAccountId, departmentId, parameters)



Query the usage data for department.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.QueryApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let departmentId = "departmentId_example"; // String | Department ID
let parameters = new CostManagementClient.ReportConfigDefinition(); // ReportConfigDefinition | Parameters supplied to the CreateOrUpdate Report Config operation.
apiInstance.queryUsageByDepartment(apiVersion, billingAccountId, departmentId, parameters, (error, data, response) => {
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


## queryUsageByEnrollmentAccount

> QueryResult queryUsageByEnrollmentAccount(apiVersion, billingAccountId, enrollmentAccountId, parameters)



Query the usage data for an enrollment account.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.QueryApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let enrollmentAccountId = "enrollmentAccountId_example"; // String | Enrollment Account ID
let parameters = new CostManagementClient.ReportConfigDefinition(); // ReportConfigDefinition | Parameters supplied to the CreateOrUpdate Report Config operation.
apiInstance.queryUsageByEnrollmentAccount(apiVersion, billingAccountId, enrollmentAccountId, parameters, (error, data, response) => {
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


## queryUsageByManagementGroup

> QueryResult queryUsageByManagementGroup(apiVersion, managementGroupId, parameters)



Lists the usage data for management group.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.QueryApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
let managementGroupId = "managementGroupId_example"; // String | ManagementGroup ID
let parameters = new CostManagementClient.ReportConfigDefinition(); // ReportConfigDefinition | Parameters supplied to the CreateOrUpdate Report Config operation.
apiInstance.queryUsageByManagementGroup(apiVersion, managementGroupId, parameters, (error, data, response) => {
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


## queryUsageByResourceGroup

> QueryResult queryUsageByResourceGroup(apiVersion, subscriptionId, resourceGroupName, parameters)



Query the usage data for subscriptionId and resource group.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.QueryApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
let parameters = new CostManagementClient.ReportConfigDefinition(); // ReportConfigDefinition | Parameters supplied to the CreateOrUpdate Report Config operation.
apiInstance.queryUsageByResourceGroup(apiVersion, subscriptionId, resourceGroupName, parameters, (error, data, response) => {
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


## queryUsageBySubscription

> QueryResult queryUsageBySubscription(apiVersion, subscriptionId, parameters)



Query the usage data for subscriptionId.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.QueryApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let parameters = new CostManagementClient.ReportConfigDefinition(); // ReportConfigDefinition | Parameters supplied to the CreateOrUpdate Report Config operation.
apiInstance.queryUsageBySubscription(apiVersion, subscriptionId, parameters, (error, data, response) => {
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

