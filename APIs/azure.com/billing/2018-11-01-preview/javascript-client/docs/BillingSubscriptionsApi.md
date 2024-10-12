# BillingManagementClient.BillingSubscriptionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billingSubscriptionsGet**](BillingSubscriptionsApi.md#billingSubscriptionsGet) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/billingSubscriptions/{billingSubscriptionName} | 
[**billingSubscriptionsGetByCustomerName**](BillingSubscriptionsApi.md#billingSubscriptionsGetByCustomerName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/customers/{customerName}/billingSubscriptions/{billingSubscriptionName} | 
[**billingSubscriptionsListByBillingAccountName**](BillingSubscriptionsApi.md#billingSubscriptionsListByBillingAccountName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingSubscriptions | 
[**billingSubscriptionsListByBillingProfileName**](BillingSubscriptionsApi.md#billingSubscriptionsListByBillingProfileName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/billingSubscriptions | 
[**billingSubscriptionsListByCustomerName**](BillingSubscriptionsApi.md#billingSubscriptionsListByCustomerName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/customers/{customerName}/billingSubscriptions | 
[**billingSubscriptionsListByInvoiceSectionName**](BillingSubscriptionsApi.md#billingSubscriptionsListByInvoiceSectionName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/billingSubscriptions | 



## billingSubscriptionsGet

> BillingSubscriptionSummary billingSubscriptionsGet(billingAccountName, invoiceSectionName, billingSubscriptionName, apiVersion)



Get a single billing subscription by name.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingSubscriptionsApi();
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
let billingSubscriptionName = "billingSubscriptionName_example"; // String | Billing Subscription Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
apiInstance.billingSubscriptionsGet(billingAccountName, invoiceSectionName, billingSubscriptionName, apiVersion, (error, data, response) => {
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
 **billingAccountName** | **String**| Billing Account Id. | 
 **invoiceSectionName** | **String**| InvoiceSection Id. | 
 **billingSubscriptionName** | **String**| Billing Subscription Id. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | 

### Return type

[**BillingSubscriptionSummary**](BillingSubscriptionSummary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingSubscriptionsGetByCustomerName

> BillingSubscriptionSummary billingSubscriptionsGetByCustomerName(billingAccountName, customerName, billingSubscriptionName, apiVersion)



Get a single billing subscription by name.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingSubscriptionsApi();
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let customerName = "customerName_example"; // String | Customer Id.
let billingSubscriptionName = "billingSubscriptionName_example"; // String | Billing Subscription Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
apiInstance.billingSubscriptionsGetByCustomerName(billingAccountName, customerName, billingSubscriptionName, apiVersion, (error, data, response) => {
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
 **billingAccountName** | **String**| Billing Account Id. | 
 **customerName** | **String**| Customer Id. | 
 **billingSubscriptionName** | **String**| Billing Subscription Id. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | 

### Return type

[**BillingSubscriptionSummary**](BillingSubscriptionSummary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingSubscriptionsListByBillingAccountName

> BillingSubscriptionsListResult billingSubscriptionsListByBillingAccountName(billingAccountName, apiVersion)



Lists billing subscriptions by billing account name.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingSubscriptionsApi();
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
apiInstance.billingSubscriptionsListByBillingAccountName(billingAccountName, apiVersion, (error, data, response) => {
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
 **billingAccountName** | **String**| Billing Account Id. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | 

### Return type

[**BillingSubscriptionsListResult**](BillingSubscriptionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingSubscriptionsListByBillingProfileName

> BillingSubscriptionsListResult billingSubscriptionsListByBillingProfileName(billingAccountName, billingProfileName, apiVersion)



Lists billing subscriptions by billing profile name.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingSubscriptionsApi();
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
apiInstance.billingSubscriptionsListByBillingProfileName(billingAccountName, billingProfileName, apiVersion, (error, data, response) => {
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
 **billingAccountName** | **String**| Billing Account Id. | 
 **billingProfileName** | **String**| Billing Profile Id. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | 

### Return type

[**BillingSubscriptionsListResult**](BillingSubscriptionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingSubscriptionsListByCustomerName

> BillingSubscriptionsListResult billingSubscriptionsListByCustomerName(billingAccountName, customerName, apiVersion)



Lists billing subscription by customer name.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingSubscriptionsApi();
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let customerName = "customerName_example"; // String | Customer Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
apiInstance.billingSubscriptionsListByCustomerName(billingAccountName, customerName, apiVersion, (error, data, response) => {
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
 **billingAccountName** | **String**| Billing Account Id. | 
 **customerName** | **String**| Customer Id. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | 

### Return type

[**BillingSubscriptionsListResult**](BillingSubscriptionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingSubscriptionsListByInvoiceSectionName

> BillingSubscriptionsListResult billingSubscriptionsListByInvoiceSectionName(billingAccountName, invoiceSectionName, apiVersion)



Lists billing subscription by invoice section name.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingSubscriptionsApi();
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
apiInstance.billingSubscriptionsListByInvoiceSectionName(billingAccountName, invoiceSectionName, apiVersion, (error, data, response) => {
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
 **billingAccountName** | **String**| Billing Account Id. | 
 **invoiceSectionName** | **String**| InvoiceSection Id. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-11-01-preview. | 

### Return type

[**BillingSubscriptionsListResult**](BillingSubscriptionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

