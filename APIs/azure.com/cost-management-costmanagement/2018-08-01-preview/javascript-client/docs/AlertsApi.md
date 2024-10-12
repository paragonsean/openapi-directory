# CostManagementClient.AlertsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**alertsGetAlertByManagementGroups**](AlertsApi.md#alertsGetAlertByManagementGroups) | **GET** /providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.CostManagement/alerts/{alertId} | 
[**alertsGetByAccount**](AlertsApi.md#alertsGetByAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}/providers/Microsoft.CostManagement/alerts/{alertId} | 
[**alertsGetByDepartment**](AlertsApi.md#alertsGetByDepartment) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}/providers/Microsoft.CostManagement/alerts/{alertId} | 
[**alertsGetByEnrollment**](AlertsApi.md#alertsGetByEnrollment) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/alerts/{alertId} | 
[**alertsGetByResourceGroupName**](AlertsApi.md#alertsGetByResourceGroupName) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CostManagement/alerts/{alertId} | 
[**alertsGetBySubscription**](AlertsApi.md#alertsGetBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/alerts/{alertId} | 
[**alertsList**](AlertsApi.md#alertsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/alerts | 
[**alertsListByAccount**](AlertsApi.md#alertsListByAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}/providers/Microsoft.CostManagement/alerts | 
[**alertsListByDepartment**](AlertsApi.md#alertsListByDepartment) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}/providers/Microsoft.CostManagement/alerts | 
[**alertsListByEnrollment**](AlertsApi.md#alertsListByEnrollment) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/alerts | 
[**alertsListByManagementGroups**](AlertsApi.md#alertsListByManagementGroups) | **GET** /providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.CostManagement/alerts | 
[**alertsListByResourceGroupName**](AlertsApi.md#alertsListByResourceGroupName) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CostManagement/alerts | 
[**alertsUpdateBillingAccountAlertStatus**](AlertsApi.md#alertsUpdateBillingAccountAlertStatus) | **PATCH** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/alerts/{alertId}/updateStatus | 
[**alertsUpdateDepartmentsAlertStatus**](AlertsApi.md#alertsUpdateDepartmentsAlertStatus) | **PATCH** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}/providers/Microsoft.CostManagement/alerts/{alertId}/updateStatus | 
[**alertsUpdateEnrollmentAccountAlertStatus**](AlertsApi.md#alertsUpdateEnrollmentAccountAlertStatus) | **PATCH** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}/providers/Microsoft.CostManagement/alerts/{alertId}/updateStatus | 
[**alertsUpdateManagementGroupAlertStatus**](AlertsApi.md#alertsUpdateManagementGroupAlertStatus) | **PATCH** /providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.CostManagement/alerts/{alertId}/UpdateStatus | 
[**alertsUpdateResourceGroupNameAlertStatus**](AlertsApi.md#alertsUpdateResourceGroupNameAlertStatus) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CostManagement/alerts/{alertId}/updateStatus | 
[**alertsUpdateSubscriptionAlertStatus**](AlertsApi.md#alertsUpdateSubscriptionAlertStatus) | **PATCH** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/alerts/{alertId}/updateStatus | 



## alertsGetAlertByManagementGroups

> Alert alertsGetAlertByManagementGroups(apiVersion, managementGroupId, alertId)



Gets an alert for Management Groups by alert ID.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.AlertsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let managementGroupId = "managementGroupId_example"; // String | Management Group ID
let alertId = "alertId_example"; // String | Alert ID.
apiInstance.alertsGetAlertByManagementGroups(apiVersion, managementGroupId, alertId, (error, data, response) => {
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
 **managementGroupId** | **String**| Management Group ID | 
 **alertId** | **String**| Alert ID. | 

### Return type

[**Alert**](Alert.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alertsGetByAccount

> Alert alertsGetByAccount(apiVersion, billingAccountId, enrollmentAccountId, alertId)



Gets the alert for an account by alert ID.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.AlertsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let enrollmentAccountId = "enrollmentAccountId_example"; // String | Enrollment Account Id
let alertId = "alertId_example"; // String | Alert ID.
apiInstance.alertsGetByAccount(apiVersion, billingAccountId, enrollmentAccountId, alertId, (error, data, response) => {
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
 **enrollmentAccountId** | **String**| Enrollment Account Id | 
 **alertId** | **String**| Alert ID. | 

### Return type

[**Alert**](Alert.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alertsGetByDepartment

> Alert alertsGetByDepartment(apiVersion, billingAccountId, departmentId, alertId)



Gets the alert for a department by alert ID.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.AlertsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let departmentId = "departmentId_example"; // String | Department ID
let alertId = "alertId_example"; // String | Alert ID.
apiInstance.alertsGetByDepartment(apiVersion, billingAccountId, departmentId, alertId, (error, data, response) => {
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
 **departmentId** | **String**| Department ID | 
 **alertId** | **String**| Alert ID. | 

### Return type

[**Alert**](Alert.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alertsGetByEnrollment

> Alert alertsGetByEnrollment(apiVersion, billingAccountId, alertId)



Gets the alert for an enrollment by alert ID.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.AlertsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let alertId = "alertId_example"; // String | Alert ID.
apiInstance.alertsGetByEnrollment(apiVersion, billingAccountId, alertId, (error, data, response) => {
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
 **alertId** | **String**| Alert ID. | 

### Return type

[**Alert**](Alert.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alertsGetByResourceGroupName

> Alert alertsGetByResourceGroupName(subscriptionId, resourceGroupName, apiVersion, alertId)



Gets the alert for a resource group under a subscription by alert ID.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.AlertsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let alertId = "alertId_example"; // String | Alert ID.
apiInstance.alertsGetByResourceGroupName(subscriptionId, resourceGroupName, apiVersion, alertId, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **resourceGroupName** | **String**| Azure Resource Group Name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | 
 **alertId** | **String**| Alert ID. | 

### Return type

[**Alert**](Alert.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alertsGetBySubscription

> Alert alertsGetBySubscription(apiVersion, subscriptionId, alertId)



Gets the alert for a subscription by alert ID.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.AlertsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let alertId = "alertId_example"; // String | Alert ID.
apiInstance.alertsGetBySubscription(apiVersion, subscriptionId, alertId, (error, data, response) => {
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
 **alertId** | **String**| Alert ID. | 

### Return type

[**Alert**](Alert.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alertsList

> AlertListResult alertsList(apiVersion, subscriptionId, opts)



List all alerts for a subscription.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.AlertsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let opts = {
  'filter': "filter_example", // String | May be used to filter alerts by properties/definition/type, properties/definition/category, properties/definition/criteria, properties/costEntityId, properties/creationTime, properties/closeTime, properties/status, properties/source. Supported operators are 'eq','lt', 'gt', 'le', 'ge'.
  'skiptoken': "skiptoken_example", // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
  'top': 56 // Number | May be used to limit the number of results to the most recent N alerts.
};
apiInstance.alertsList(apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **filter** | **String**| May be used to filter alerts by properties/definition/type, properties/definition/category, properties/definition/criteria, properties/costEntityId, properties/creationTime, properties/closeTime, properties/status, properties/source. Supported operators are &#39;eq&#39;,&#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;. | [optional] 
 **skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] 
 **top** | **Number**| May be used to limit the number of results to the most recent N alerts. | [optional] 

### Return type

[**AlertListResult**](AlertListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alertsListByAccount

> AlertListResult alertsListByAccount(apiVersion, billingAccountId, enrollmentAccountId, opts)



List all alerts for an account.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.AlertsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let enrollmentAccountId = "enrollmentAccountId_example"; // String | Enrollment Account Id
let opts = {
  'filter': "filter_example", // String | May be used to filter alerts by properties/definition/type, properties/definition/category, properties/definition/criteria, properties/costEntityId, properties/creationTime, properties/closeTime, properties/status, properties/source. Supported operators are 'eq','lt', 'gt', 'le', 'ge'.
  'skiptoken': "skiptoken_example", // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
  'top': 56 // Number | May be used to limit the number of results to the most recent N alerts.
};
apiInstance.alertsListByAccount(apiVersion, billingAccountId, enrollmentAccountId, opts, (error, data, response) => {
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
 **enrollmentAccountId** | **String**| Enrollment Account Id | 
 **filter** | **String**| May be used to filter alerts by properties/definition/type, properties/definition/category, properties/definition/criteria, properties/costEntityId, properties/creationTime, properties/closeTime, properties/status, properties/source. Supported operators are &#39;eq&#39;,&#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;. | [optional] 
 **skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] 
 **top** | **Number**| May be used to limit the number of results to the most recent N alerts. | [optional] 

### Return type

[**AlertListResult**](AlertListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alertsListByDepartment

> AlertListResult alertsListByDepartment(apiVersion, billingAccountId, departmentId, opts)



List all alerts for a department.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.AlertsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let departmentId = "departmentId_example"; // String | Department ID
let opts = {
  'filter': "filter_example", // String | May be used to filter alerts by properties/definition/type, properties/definition/category, properties/definition/criteria, properties/costEntityId, properties/creationTime, properties/closeTime, properties/status, properties/source. Supported operators are 'eq','lt', 'gt', 'le', 'ge'.
  'skiptoken': "skiptoken_example", // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
  'top': 56 // Number | May be used to limit the number of results to the most recent N alerts.
};
apiInstance.alertsListByDepartment(apiVersion, billingAccountId, departmentId, opts, (error, data, response) => {
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
 **departmentId** | **String**| Department ID | 
 **filter** | **String**| May be used to filter alerts by properties/definition/type, properties/definition/category, properties/definition/criteria, properties/costEntityId, properties/creationTime, properties/closeTime, properties/status, properties/source. Supported operators are &#39;eq&#39;,&#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;. | [optional] 
 **skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] 
 **top** | **Number**| May be used to limit the number of results to the most recent N alerts. | [optional] 

### Return type

[**AlertListResult**](AlertListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alertsListByEnrollment

> AlertListResult alertsListByEnrollment(apiVersion, billingAccountId, opts)



List all alerts for an enrollment.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.AlertsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let opts = {
  'filter': "filter_example", // String | May be used to filter alerts by properties/definition/type, properties/definition/category, properties/definition/criteria, properties/costEntityId, properties/creationTime, properties/closeTime, properties/status, properties/source. Supported operators are 'eq','lt', 'gt', 'le', 'ge'.
  'skiptoken': "skiptoken_example", // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
  'top': 56 // Number | May be used to limit the number of results to the most recent N alerts.
};
apiInstance.alertsListByEnrollment(apiVersion, billingAccountId, opts, (error, data, response) => {
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
 **filter** | **String**| May be used to filter alerts by properties/definition/type, properties/definition/category, properties/definition/criteria, properties/costEntityId, properties/creationTime, properties/closeTime, properties/status, properties/source. Supported operators are &#39;eq&#39;,&#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;. | [optional] 
 **skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] 
 **top** | **Number**| May be used to limit the number of results to the most recent N alerts. | [optional] 

### Return type

[**AlertListResult**](AlertListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alertsListByManagementGroups

> AlertListResult alertsListByManagementGroups(apiVersion, managementGroupId, opts)



List all alerts for Management Groups.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.AlertsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let managementGroupId = "managementGroupId_example"; // String | Management Group ID
let opts = {
  'filter': "filter_example", // String | May be used to filter alerts by properties/definition/type, properties/definition/category, properties/definition/criteria, properties/costEntityId, properties/creationTime, properties/closeTime, properties/status, properties/source. Supported operators are 'eq','lt', 'gt', 'le', 'ge'.
  'skiptoken': "skiptoken_example", // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
  'top': 56 // Number | May be used to limit the number of results to the most recent N alerts.
};
apiInstance.alertsListByManagementGroups(apiVersion, managementGroupId, opts, (error, data, response) => {
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
 **managementGroupId** | **String**| Management Group ID | 
 **filter** | **String**| May be used to filter alerts by properties/definition/type, properties/definition/category, properties/definition/criteria, properties/costEntityId, properties/creationTime, properties/closeTime, properties/status, properties/source. Supported operators are &#39;eq&#39;,&#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;. | [optional] 
 **skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] 
 **top** | **Number**| May be used to limit the number of results to the most recent N alerts. | [optional] 

### Return type

[**AlertListResult**](AlertListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alertsListByResourceGroupName

> AlertListResult alertsListByResourceGroupName(subscriptionId, resourceGroupName, apiVersion, opts)



List all alerts for a resource group under a subscription.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.AlertsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let opts = {
  'filter': "filter_example", // String | May be used to filter alerts by properties/definition/type, properties/definition/category, properties/definition/criteria, properties/costEntityId, properties/creationTime, properties/closeTime, properties/status, properties/source. Supported operators are 'eq','lt', 'gt', 'le', 'ge'.
  'skiptoken': "skiptoken_example", // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
  'top': 56 // Number | May be used to limit the number of results to the most recent N alerts.
};
apiInstance.alertsListByResourceGroupName(subscriptionId, resourceGroupName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **resourceGroupName** | **String**| Azure Resource Group Name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | 
 **filter** | **String**| May be used to filter alerts by properties/definition/type, properties/definition/category, properties/definition/criteria, properties/costEntityId, properties/creationTime, properties/closeTime, properties/status, properties/source. Supported operators are &#39;eq&#39;,&#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;. | [optional] 
 **skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] 
 **top** | **Number**| May be used to limit the number of results to the most recent N alerts. | [optional] 

### Return type

[**AlertListResult**](AlertListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alertsUpdateBillingAccountAlertStatus

> Alert alertsUpdateBillingAccountAlertStatus(apiVersion, billingAccountId, alertId, parameters)



Update alerts status for billing account.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.AlertsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let alertId = "alertId_example"; // String | Alert ID.
let parameters = new CostManagementClient.Alert(); // Alert | Parameters supplied to the update alerts status operation.
apiInstance.alertsUpdateBillingAccountAlertStatus(apiVersion, billingAccountId, alertId, parameters, (error, data, response) => {
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
 **alertId** | **String**| Alert ID. | 
 **parameters** | [**Alert**](Alert.md)| Parameters supplied to the update alerts status operation. | 

### Return type

[**Alert**](Alert.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## alertsUpdateDepartmentsAlertStatus

> Alert alertsUpdateDepartmentsAlertStatus(apiVersion, billingAccountId, departmentId, alertId, parameters)



Update alerts status for a department.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.AlertsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let departmentId = "departmentId_example"; // String | Department ID
let alertId = "alertId_example"; // String | Alert ID.
let parameters = new CostManagementClient.Alert(); // Alert | Parameters supplied to the update alerts status operation.
apiInstance.alertsUpdateDepartmentsAlertStatus(apiVersion, billingAccountId, departmentId, alertId, parameters, (error, data, response) => {
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
 **departmentId** | **String**| Department ID | 
 **alertId** | **String**| Alert ID. | 
 **parameters** | [**Alert**](Alert.md)| Parameters supplied to the update alerts status operation. | 

### Return type

[**Alert**](Alert.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## alertsUpdateEnrollmentAccountAlertStatus

> Alert alertsUpdateEnrollmentAccountAlertStatus(apiVersion, billingAccountId, enrollmentAccountId, alertId, parameters)



Update alerts status for an enrollment account.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.AlertsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let enrollmentAccountId = "enrollmentAccountId_example"; // String | Enrollment Account Id
let alertId = "alertId_example"; // String | Alert ID.
let parameters = new CostManagementClient.Alert(); // Alert | Parameters supplied to the update alerts status operation.
apiInstance.alertsUpdateEnrollmentAccountAlertStatus(apiVersion, billingAccountId, enrollmentAccountId, alertId, parameters, (error, data, response) => {
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
 **enrollmentAccountId** | **String**| Enrollment Account Id | 
 **alertId** | **String**| Alert ID. | 
 **parameters** | [**Alert**](Alert.md)| Parameters supplied to the update alerts status operation. | 

### Return type

[**Alert**](Alert.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## alertsUpdateManagementGroupAlertStatus

> Alert alertsUpdateManagementGroupAlertStatus(apiVersion, managementGroupId, alertId, parameters)



Update alerts status for management group.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.AlertsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let managementGroupId = "managementGroupId_example"; // String | Management Group ID
let alertId = "alertId_example"; // String | Alert ID.
let parameters = new CostManagementClient.Alert(); // Alert | Parameters supplied to the update alerts status operation.
apiInstance.alertsUpdateManagementGroupAlertStatus(apiVersion, managementGroupId, alertId, parameters, (error, data, response) => {
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
 **managementGroupId** | **String**| Management Group ID | 
 **alertId** | **String**| Alert ID. | 
 **parameters** | [**Alert**](Alert.md)| Parameters supplied to the update alerts status operation. | 

### Return type

[**Alert**](Alert.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## alertsUpdateResourceGroupNameAlertStatus

> Alert alertsUpdateResourceGroupNameAlertStatus(subscriptionId, resourceGroupName, alertId, apiVersion, parameters)



Update alerts status for a resource group under a subscription.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.AlertsApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
let alertId = "alertId_example"; // String | Alert ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let parameters = new CostManagementClient.Alert(); // Alert | Parameters supplied to the update alerts status operation.
apiInstance.alertsUpdateResourceGroupNameAlertStatus(subscriptionId, resourceGroupName, alertId, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **resourceGroupName** | **String**| Azure Resource Group Name. | 
 **alertId** | **String**| Alert ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-08-01-preview. | 
 **parameters** | [**Alert**](Alert.md)| Parameters supplied to the update alerts status operation. | 

### Return type

[**Alert**](Alert.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## alertsUpdateSubscriptionAlertStatus

> Alert alertsUpdateSubscriptionAlertStatus(apiVersion, subscriptionId, alertId, parameters)



Update alerts status for a subscription.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.AlertsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-08-01-preview.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let alertId = "alertId_example"; // String | Alert ID.
let parameters = new CostManagementClient.Alert(); // Alert | Parameters supplied to the update alerts status operation.
apiInstance.alertsUpdateSubscriptionAlertStatus(apiVersion, subscriptionId, alertId, parameters, (error, data, response) => {
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
 **alertId** | **String**| Alert ID. | 
 **parameters** | [**Alert**](Alert.md)| Parameters supplied to the update alerts status operation. | 

### Return type

[**Alert**](Alert.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

