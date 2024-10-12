# BillingManagementClient.TransactionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transactionsGet**](TransactionsApi.md#transactionsGet) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/transactions/{transactionName} | 
[**transactionsListByBillingAccount**](TransactionsApi.md#transactionsListByBillingAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/transactions | 
[**transactionsListByBillingProfile**](TransactionsApi.md#transactionsListByBillingProfile) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/transactions | 
[**transactionsListByCustomer**](TransactionsApi.md#transactionsListByCustomer) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/customers/{customerName}/transactions | 
[**transactionsListByInvoiceSection**](TransactionsApi.md#transactionsListByInvoiceSection) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/transactions | 



## transactionsGet

> Transaction transactionsGet(billingAccountName, billingProfileName, transactionName, periodStartDate, periodEndDate, apiVersion)



Get the transaction.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.TransactionsApi();
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let transactionName = "transactionName_example"; // String | Transaction name.
let periodStartDate = "periodStartDate_example"; // String | Start date
let periodEndDate = "periodEndDate_example"; // String | End date
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
apiInstance.transactionsGet(billingAccountName, billingProfileName, transactionName, periodStartDate, periodEndDate, apiVersion, (error, data, response) => {
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
 **billingProfileName** | **String**| Billing Profile Id. | 
 **transactionName** | **String**| Transaction name. | 
 **periodStartDate** | **String**| Start date | 
 **periodEndDate** | **String**| End date | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transactionsListByBillingAccount

> TransactionListResult transactionsListByBillingAccount(billingAccountName, apiVersion, periodStartDate, periodEndDate, opts)



Lists the transactions by billing account name for given start and end date.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.TransactionsApi();
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let periodStartDate = "periodStartDate_example"; // String | Start date
let periodEndDate = "periodEndDate_example"; // String | End date
let opts = {
  'filter': "filter_example" // String | May be used to filter by transaction kind. The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is a key value pair string where key and value is separated by a colon (:).
};
apiInstance.transactionsListByBillingAccount(billingAccountName, apiVersion, periodStartDate, periodEndDate, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | 
 **periodStartDate** | **String**| Start date | 
 **periodEndDate** | **String**| End date | 
 **filter** | **String**| May be used to filter by transaction kind. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:). | [optional] 

### Return type

[**TransactionListResult**](TransactionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transactionsListByBillingProfile

> TransactionListResult transactionsListByBillingProfile(billingAccountName, billingProfileName, apiVersion, periodStartDate, periodEndDate, opts)



Lists the transactions by billing profile name for given start date and end date.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.TransactionsApi();
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let periodStartDate = "periodStartDate_example"; // String | Start date
let periodEndDate = "periodEndDate_example"; // String | End date
let opts = {
  'filter': "filter_example" // String | May be used to filter by transaction kind. The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is a key value pair string where key and value is separated by a colon (:).
};
apiInstance.transactionsListByBillingProfile(billingAccountName, billingProfileName, apiVersion, periodStartDate, periodEndDate, opts, (error, data, response) => {
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
 **billingProfileName** | **String**| Billing Profile Id. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | 
 **periodStartDate** | **String**| Start date | 
 **periodEndDate** | **String**| End date | 
 **filter** | **String**| May be used to filter by transaction kind. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:). | [optional] 

### Return type

[**TransactionListResult**](TransactionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transactionsListByCustomer

> TransactionListResult transactionsListByCustomer(billingAccountName, customerName, apiVersion, periodStartDate, periodEndDate, opts)



Lists the transactions by customer id for given start date and end date.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.TransactionsApi();
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let customerName = "customerName_example"; // String | Customer name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let periodStartDate = "periodStartDate_example"; // String | Start date
let periodEndDate = "periodEndDate_example"; // String | End date
let opts = {
  'filter': "filter_example" // String | May be used to filter by transaction kind. The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is a key value pair string where key and value is separated by a colon (:).
};
apiInstance.transactionsListByCustomer(billingAccountName, customerName, apiVersion, periodStartDate, periodEndDate, opts, (error, data, response) => {
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
 **customerName** | **String**| Customer name. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | 
 **periodStartDate** | **String**| Start date | 
 **periodEndDate** | **String**| End date | 
 **filter** | **String**| May be used to filter by transaction kind. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:). | [optional] 

### Return type

[**TransactionListResult**](TransactionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transactionsListByInvoiceSection

> TransactionListResult transactionsListByInvoiceSection(billingAccountName, billingProfileName, invoiceSectionName, apiVersion, periodStartDate, periodEndDate, opts)



Lists the transactions by invoice section name for given start date and end date.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.TransactionsApi();
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let periodStartDate = "periodStartDate_example"; // String | Start date
let periodEndDate = "periodEndDate_example"; // String | End date
let opts = {
  'filter': "filter_example" // String | May be used to filter by transaction kind. The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is a key value pair string where key and value is separated by a colon (:).
};
apiInstance.transactionsListByInvoiceSection(billingAccountName, billingProfileName, invoiceSectionName, apiVersion, periodStartDate, periodEndDate, opts, (error, data, response) => {
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
 **billingProfileName** | **String**| Billing Profile Id. | 
 **invoiceSectionName** | **String**| InvoiceSection Id. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | 
 **periodStartDate** | **String**| Start date | 
 **periodEndDate** | **String**| End date | 
 **filter** | **String**| May be used to filter by transaction kind. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:). | [optional] 

### Return type

[**TransactionListResult**](TransactionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

