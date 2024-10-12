# BillingClient.InvoicesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoicesGet**](InvoicesApi.md#invoicesGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Billing/invoices/{invoiceName} | 
[**invoicesGetLatest**](InvoicesApi.md#invoicesGetLatest) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Billing/invoices/latest | 
[**invoicesList**](InvoicesApi.md#invoicesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Billing/invoices | 



## invoicesGet

> Invoice invoicesGet(subscriptionId, invoiceName, apiVersion)



Gets a named invoice resource. When getting a single invoice, the downloadUrl property is expanded automatically.

### Example

```javascript
import BillingClient from 'billing_client';
let defaultClient = BillingClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingClient.InvoicesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let invoiceName = "invoiceName_example"; // String | The name of an invoice resource.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2017-02-27-preview.
apiInstance.invoicesGet(subscriptionId, invoiceName, apiVersion, (error, data, response) => {
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
 **invoiceName** | **String**| The name of an invoice resource. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2017-02-27-preview. | 

### Return type

[**Invoice**](Invoice.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoicesGetLatest

> Invoice invoicesGetLatest(subscriptionId, apiVersion)



Gets the most recent invoice. When getting a single invoice, the downloadUrl property is expanded automatically.

### Example

```javascript
import BillingClient from 'billing_client';
let defaultClient = BillingClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingClient.InvoicesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2017-02-27-preview.
apiInstance.invoicesGetLatest(subscriptionId, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2017-02-27-preview. | 

### Return type

[**Invoice**](Invoice.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoicesList

> InvoicesListResult invoicesList(subscriptionId, apiVersion, opts)



Lists the available invoices for a subscription in reverse chronological order beginning with the most recent invoice. In preview, invoices are available via this API only for invoice periods which end December 1, 2016 or later

### Example

```javascript
import BillingClient from 'billing_client';
let defaultClient = BillingClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingClient.InvoicesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2017-02-27-preview.
let opts = {
  'expand': "expand_example", // String | May be used to expand the downloadUrl property within a list of invoices. This enables download links to be generated for multiple invoices at once. By default, downloadURLs are not included when listing invoices.
  'filter': "filter_example", // String | May be used to filter invoices by invoicePeriodEndDate. The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'
  'skiptoken': "skiptoken_example", // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
  'top': 56 // Number | May be used to limit the number of results to the most recent N invoices.
};
apiInstance.invoicesList(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2017-02-27-preview. | 
 **expand** | **String**| May be used to expand the downloadUrl property within a list of invoices. This enables download links to be generated for multiple invoices at once. By default, downloadURLs are not included when listing invoices. | [optional] 
 **filter** | **String**| May be used to filter invoices by invoicePeriodEndDate. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39; | [optional] 
 **skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] 
 **top** | **Number**| May be used to limit the number of results to the most recent N invoices. | [optional] 

### Return type

[**InvoicesListResult**](InvoicesListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

