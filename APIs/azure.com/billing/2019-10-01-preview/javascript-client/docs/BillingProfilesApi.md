# BillingManagementClient.BillingProfilesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billingProfilesCreate**](BillingProfilesApi.md#billingProfilesCreate) | **PUT** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName} | 
[**billingProfilesGet**](BillingProfilesApi.md#billingProfilesGet) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName} | 
[**billingProfilesListByBillingAccount**](BillingProfilesApi.md#billingProfilesListByBillingAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles | 
[**billingProfilesUpdate**](BillingProfilesApi.md#billingProfilesUpdate) | **PATCH** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName} | 



## billingProfilesCreate

> BillingProfile billingProfilesCreate(apiVersion, billingAccountName, billingProfileName, parameters)



The operation to create a BillingProfile.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingProfilesApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let parameters = new BillingManagementClient.BillingProfileCreationRequest(); // BillingProfileCreationRequest | Request parameters supplied to the Create BillingProfile operation.
apiInstance.billingProfilesCreate(apiVersion, billingAccountName, billingProfileName, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | 
 **billingAccountName** | **String**| billing Account Id. | 
 **billingProfileName** | **String**| Billing Profile Id. | 
 **parameters** | [**BillingProfileCreationRequest**](BillingProfileCreationRequest.md)| Request parameters supplied to the Create BillingProfile operation. | 

### Return type

[**BillingProfile**](BillingProfile.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## billingProfilesGet

> BillingProfile billingProfilesGet(apiVersion, billingAccountName, billingProfileName, opts)



Get the billing profile by id.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingProfilesApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let opts = {
  'expand': "expand_example" // String | May be used to expand the invoiceSections.
};
apiInstance.billingProfilesGet(apiVersion, billingAccountName, billingProfileName, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | 
 **billingAccountName** | **String**| billing Account Id. | 
 **billingProfileName** | **String**| Billing Profile Id. | 
 **expand** | **String**| May be used to expand the invoiceSections. | [optional] 

### Return type

[**BillingProfile**](BillingProfile.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingProfilesListByBillingAccount

> BillingProfileListResult billingProfilesListByBillingAccount(apiVersion, billingAccountName, opts)



Lists all billing profiles for a user which that user has access to.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingProfilesApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let opts = {
  'expand': "expand_example" // String | May be used to expand the invoiceSections.
};
apiInstance.billingProfilesListByBillingAccount(apiVersion, billingAccountName, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | 
 **billingAccountName** | **String**| billing Account Id. | 
 **expand** | **String**| May be used to expand the invoiceSections. | [optional] 

### Return type

[**BillingProfileListResult**](BillingProfileListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingProfilesUpdate

> BillingProfile billingProfilesUpdate(apiVersion, billingAccountName, billingProfileName, parameters)



The operation to update a billing profile.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingProfilesApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let parameters = new BillingManagementClient.BillingProfile(); // BillingProfile | Request parameters supplied to the update billing profile operation.
apiInstance.billingProfilesUpdate(apiVersion, billingAccountName, billingProfileName, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | 
 **billingAccountName** | **String**| billing Account Id. | 
 **billingProfileName** | **String**| Billing Profile Id. | 
 **parameters** | [**BillingProfile**](BillingProfile.md)| Request parameters supplied to the update billing profile operation. | 

### Return type

[**BillingProfile**](BillingProfile.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

