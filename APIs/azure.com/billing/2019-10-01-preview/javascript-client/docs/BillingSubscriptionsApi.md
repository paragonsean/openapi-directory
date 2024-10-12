# BillingManagementClient.BillingSubscriptionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billingSubscriptionsGet**](BillingSubscriptionsApi.md#billingSubscriptionsGet) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/billingSubscriptions/{billingSubscriptionName} | 
[**billingSubscriptionsGetByCustomer**](BillingSubscriptionsApi.md#billingSubscriptionsGetByCustomer) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/customers/{customerName}/billingSubscriptions/{billingSubscriptionName} | 
[**billingSubscriptionsListByBillingAccount**](BillingSubscriptionsApi.md#billingSubscriptionsListByBillingAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingSubscriptions | 
[**billingSubscriptionsListByBillingProfile**](BillingSubscriptionsApi.md#billingSubscriptionsListByBillingProfile) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/billingSubscriptions | 
[**billingSubscriptionsListByCustomer**](BillingSubscriptionsApi.md#billingSubscriptionsListByCustomer) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/customers/{customerName}/billingSubscriptions | 
[**billingSubscriptionsListByInvoiceSection**](BillingSubscriptionsApi.md#billingSubscriptionsListByInvoiceSection) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/billingSubscriptions | 



## billingSubscriptionsGet

> BillingSubscription billingSubscriptionsGet(billingAccountName, billingProfileName, invoiceSectionName, billingSubscriptionName, apiVersion)



Get a single billing subscription by name.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingSubscriptionsApi();
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
let billingSubscriptionName = "billingSubscriptionName_example"; // String | Billing Subscription Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
apiInstance.billingSubscriptionsGet(billingAccountName, billingProfileName, invoiceSectionName, billingSubscriptionName, apiVersion, (error, data, response) => {
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
 **billingSubscriptionName** | **String**| Billing Subscription Id. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | 

### Return type

[**BillingSubscription**](BillingSubscription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingSubscriptionsGetByCustomer

> BillingSubscription billingSubscriptionsGetByCustomer(billingAccountName, customerName, billingSubscriptionName, apiVersion)



Get a single billing subscription by id.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingSubscriptionsApi();
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let customerName = "customerName_example"; // String | Customer name.
let billingSubscriptionName = "billingSubscriptionName_example"; // String | Billing Subscription Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
apiInstance.billingSubscriptionsGetByCustomer(billingAccountName, customerName, billingSubscriptionName, apiVersion, (error, data, response) => {
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
 **billingSubscriptionName** | **String**| Billing Subscription Id. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | 

### Return type

[**BillingSubscription**](BillingSubscription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingSubscriptionsListByBillingAccount

> BillingSubscriptionsListResult billingSubscriptionsListByBillingAccount(billingAccountName, apiVersion)



Lists billing subscriptions by billing account name.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingSubscriptionsApi();
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
apiInstance.billingSubscriptionsListByBillingAccount(billingAccountName, apiVersion, (error, data, response) => {
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

### Return type

[**BillingSubscriptionsListResult**](BillingSubscriptionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingSubscriptionsListByBillingProfile

> BillingSubscriptionsListResult billingSubscriptionsListByBillingProfile(billingAccountName, billingProfileName, apiVersion)



Lists billing subscriptions by billing profile name.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingSubscriptionsApi();
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
apiInstance.billingSubscriptionsListByBillingProfile(billingAccountName, billingProfileName, apiVersion, (error, data, response) => {
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

### Return type

[**BillingSubscriptionsListResult**](BillingSubscriptionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingSubscriptionsListByCustomer

> BillingSubscriptionsListResult billingSubscriptionsListByCustomer(billingAccountName, customerName, apiVersion)



Lists billing subscription by customer id.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingSubscriptionsApi();
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let customerName = "customerName_example"; // String | Customer name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
apiInstance.billingSubscriptionsListByCustomer(billingAccountName, customerName, apiVersion, (error, data, response) => {
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

### Return type

[**BillingSubscriptionsListResult**](BillingSubscriptionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingSubscriptionsListByInvoiceSection

> BillingSubscriptionsListResult billingSubscriptionsListByInvoiceSection(billingAccountName, billingProfileName, invoiceSectionName, apiVersion)



Lists billing subscription by invoice section name.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingSubscriptionsApi();
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
apiInstance.billingSubscriptionsListByInvoiceSection(billingAccountName, billingProfileName, invoiceSectionName, apiVersion, (error, data, response) => {
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

### Return type

[**BillingSubscriptionsListResult**](BillingSubscriptionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

