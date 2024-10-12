# BillingManagementClient.EnrollmentAccountsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enrollmentAccountsGetByEnrollmentAccountId**](EnrollmentAccountsApi.md#enrollmentAccountsGetByEnrollmentAccountId) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/enrollmentAccounts/{enrollmentAccountName} | 
[**enrollmentAccountsListByBillingAccountName**](EnrollmentAccountsApi.md#enrollmentAccountsListByBillingAccountName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/enrollmentAccounts | 



## enrollmentAccountsGetByEnrollmentAccountId

> EnrollmentAccount enrollmentAccountsGetByEnrollmentAccountId(apiVersion, billingAccountName, enrollmentAccountName, opts)



Get the enrollment account by id.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.EnrollmentAccountsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let enrollmentAccountName = "enrollmentAccountName_example"; // String | Enrollment Account Id.
let opts = {
  'expand': "expand_example", // String | May be used to expand the Department.
  'filter': "filter_example" // String | The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is a key value pair string where key and value is separated by a colon (:).
};
apiInstance.enrollmentAccountsGetByEnrollmentAccountId(apiVersion, billingAccountName, enrollmentAccountName, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | 
 **billingAccountName** | **String**| Billing Account Id. | 
 **enrollmentAccountName** | **String**| Enrollment Account Id. | 
 **expand** | **String**| May be used to expand the Department. | [optional] 
 **filter** | **String**| The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:). | [optional] 

### Return type

[**EnrollmentAccount**](EnrollmentAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enrollmentAccountsListByBillingAccountName

> EnrollmentAccountListResult enrollmentAccountsListByBillingAccountName(apiVersion, billingAccountName, opts)



Lists all Enrollment Accounts for which a user has access.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.EnrollmentAccountsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let opts = {
  'expand': "expand_example", // String | May be used to expand the department.
  'filter': "filter_example" // String | The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is a key value pair string where key and value is separated by a colon (:).
};
apiInstance.enrollmentAccountsListByBillingAccountName(apiVersion, billingAccountName, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | 
 **billingAccountName** | **String**| Billing Account Id. | 
 **expand** | **String**| May be used to expand the department. | [optional] 
 **filter** | **String**| The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:). | [optional] 

### Return type

[**EnrollmentAccountListResult**](EnrollmentAccountListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

