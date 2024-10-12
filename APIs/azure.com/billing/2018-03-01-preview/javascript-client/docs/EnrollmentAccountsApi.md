# BillingManagementClient.EnrollmentAccountsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enrollmentAccountsGet**](EnrollmentAccountsApi.md#enrollmentAccountsGet) | **GET** /providers/Microsoft.Billing/enrollmentAccounts/{name} | 
[**enrollmentAccountsList**](EnrollmentAccountsApi.md#enrollmentAccountsList) | **GET** /providers/Microsoft.Billing/enrollmentAccounts | 



## enrollmentAccountsGet

> EnrollmentAccount enrollmentAccountsGet(name, apiVersion)



Gets a enrollment account by name.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.EnrollmentAccountsApi();
let name = "name_example"; // String | Enrollment Account name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-03-01-preview.
apiInstance.enrollmentAccountsGet(name, apiVersion, (error, data, response) => {
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
 **name** | **String**| Enrollment Account name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-03-01-preview. | 

### Return type

[**EnrollmentAccount**](EnrollmentAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enrollmentAccountsList

> EnrollmentAccountListResult enrollmentAccountsList(apiVersion)



Lists the enrollment accounts the caller has access to.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.EnrollmentAccountsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-03-01-preview.
apiInstance.enrollmentAccountsList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-03-01-preview. | 

### Return type

[**EnrollmentAccountListResult**](EnrollmentAccountListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

