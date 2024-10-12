# BillingManagementClient.InvoicesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoicesGet**](InvoicesApi.md#invoicesGet) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoices/{invoiceName} | 
[**invoicesGetById**](InvoicesApi.md#invoicesGetById) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingSubscriptions/{billingSubscriptionName}/invoices/{invoiceName} | 
[**invoicesListByBillingAccount**](InvoicesApi.md#invoicesListByBillingAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoices | 
[**invoicesListByBillingProfile**](InvoicesApi.md#invoicesListByBillingProfile) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoices | 
[**invoicesListByBillingSubscription**](InvoicesApi.md#invoicesListByBillingSubscription) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingSubscriptions/{billingSubscriptionName}/invoices | 



## invoicesGet

> Invoice invoicesGet(apiVersion, billingAccountName, billingProfileName, invoiceName)



Get the invoice by name.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.InvoicesApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let invoiceName = "invoiceName_example"; // String | Invoice Id.
apiInstance.invoicesGet(apiVersion, billingAccountName, billingProfileName, invoiceName, (error, data, response) => {
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
 **invoiceName** | **String**| Invoice Id. | 

### Return type

[**Invoice**](Invoice.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoicesGetById

> Invoice invoicesGetById(billingAccountName, billingSubscriptionName, invoiceName, apiVersion)



Gets the invoice by name.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.InvoicesApi();
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingSubscriptionName = "billingSubscriptionName_example"; // String | Billing Subscription Id.
let invoiceName = "invoiceName_example"; // String | Invoice Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
apiInstance.invoicesGetById(billingAccountName, billingSubscriptionName, invoiceName, apiVersion, (error, data, response) => {
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
 **billingAccountName** | **String**| billing Account Id. | 
 **billingSubscriptionName** | **String**| Billing Subscription Id. | 
 **invoiceName** | **String**| Invoice Id. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | 

### Return type

[**Invoice**](Invoice.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoicesListByBillingAccount

> InvoiceListResult invoicesListByBillingAccount(apiVersion, billingAccountName, periodStartDate, periodEndDate)



List of invoices for a billing account.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.InvoicesApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let periodStartDate = "periodStartDate_example"; // String | Invoice period start date.
let periodEndDate = "periodEndDate_example"; // String | Invoice period end date.
apiInstance.invoicesListByBillingAccount(apiVersion, billingAccountName, periodStartDate, periodEndDate, (error, data, response) => {
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
 **periodStartDate** | **String**| Invoice period start date. | 
 **periodEndDate** | **String**| Invoice period end date. | 

### Return type

[**InvoiceListResult**](InvoiceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoicesListByBillingProfile

> InvoiceListResult invoicesListByBillingProfile(apiVersion, billingAccountName, billingProfileName, periodStartDate, periodEndDate)



List of invoices for a billing profile.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.InvoicesApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let periodStartDate = "periodStartDate_example"; // String | Invoice period start date.
let periodEndDate = "periodEndDate_example"; // String | Invoice period end date.
apiInstance.invoicesListByBillingProfile(apiVersion, billingAccountName, billingProfileName, periodStartDate, periodEndDate, (error, data, response) => {
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
 **periodStartDate** | **String**| Invoice period start date. | 
 **periodEndDate** | **String**| Invoice period end date. | 

### Return type

[**InvoiceListResult**](InvoiceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoicesListByBillingSubscription

> InvoiceListResult invoicesListByBillingSubscription(billingAccountName, billingSubscriptionName, periodStartDate, periodEndDate, apiVersion)



Lists invoices by billing subscriptions name.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.InvoicesApi();
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingSubscriptionName = "billingSubscriptionName_example"; // String | Billing Subscription Id.
let periodStartDate = "periodStartDate_example"; // String | Invoice period start date.
let periodEndDate = "periodEndDate_example"; // String | Invoice period end date.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
apiInstance.invoicesListByBillingSubscription(billingAccountName, billingSubscriptionName, periodStartDate, periodEndDate, apiVersion, (error, data, response) => {
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
 **billingAccountName** | **String**| billing Account Id. | 
 **billingSubscriptionName** | **String**| Billing Subscription Id. | 
 **periodStartDate** | **String**| Invoice period start date. | 
 **periodEndDate** | **String**| Invoice period end date. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | 

### Return type

[**InvoiceListResult**](InvoiceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

