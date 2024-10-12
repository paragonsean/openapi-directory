# BillingManagementClient.ProductsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productsGet**](ProductsApi.md#productsGet) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/products/{productName} | 
[**productsGetByCustomer**](ProductsApi.md#productsGetByCustomer) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/customers/{customerName}/products/{productName} | 
[**productsListByBillingAccount**](ProductsApi.md#productsListByBillingAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/products | 
[**productsListByCustomer**](ProductsApi.md#productsListByCustomer) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/customers/{customerName}/products | 
[**productsListByInvoiceSection**](ProductsApi.md#productsListByInvoiceSection) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/products | 
[**productsTransfer**](ProductsApi.md#productsTransfer) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/products/{productName}/transfer | 
[**productsUpdateAutoRenewByInvoiceSection**](ProductsApi.md#productsUpdateAutoRenewByInvoiceSection) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/products/{productName}/updateAutoRenew | 



## productsGet

> Product productsGet(billingAccountName, billingProfileName, invoiceSectionName, productName, apiVersion)



Get a single product by name.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.ProductsApi();
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
let productName = "productName_example"; // String | Invoice Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
apiInstance.productsGet(billingAccountName, billingProfileName, invoiceSectionName, productName, apiVersion, (error, data, response) => {
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
 **productName** | **String**| Invoice Id. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | 

### Return type

[**Product**](Product.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsGetByCustomer

> Product productsGetByCustomer(billingAccountName, customerName, productName, apiVersion)



Get a customer&#39;s product by name.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.ProductsApi();
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let customerName = "customerName_example"; // String | Customer name.
let productName = "productName_example"; // String | Invoice Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
apiInstance.productsGetByCustomer(billingAccountName, customerName, productName, apiVersion, (error, data, response) => {
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
 **productName** | **String**| Invoice Id. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | 

### Return type

[**Product**](Product.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsListByBillingAccount

> ProductsListResult productsListByBillingAccount(billingAccountName, apiVersion, opts)



Lists products by billing account name.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.ProductsApi();
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let opts = {
  'filter': "filter_example" // String | May be used to filter by product type. The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is a key value pair string where key and value is separated by a colon (:).
};
apiInstance.productsListByBillingAccount(billingAccountName, apiVersion, opts, (error, data, response) => {
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
 **filter** | **String**| May be used to filter by product type. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:). | [optional] 

### Return type

[**ProductsListResult**](ProductsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsListByCustomer

> ProductsListResult productsListByCustomer(billingAccountName, customerName, apiVersion, opts)



Lists products by customer id.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.ProductsApi();
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let customerName = "customerName_example"; // String | Customer name.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let opts = {
  'filter': "filter_example" // String | May be used to filter by product type. The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is a key value pair string where key and value is separated by a colon (:).
};
apiInstance.productsListByCustomer(billingAccountName, customerName, apiVersion, opts, (error, data, response) => {
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
 **filter** | **String**| May be used to filter by product type. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:). | [optional] 

### Return type

[**ProductsListResult**](ProductsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsListByInvoiceSection

> ProductsListResult productsListByInvoiceSection(billingAccountName, billingProfileName, invoiceSectionName, apiVersion, opts)



Lists products by invoice section name.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.ProductsApi();
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let opts = {
  'filter': "filter_example" // String | May be used to filter by product type. The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is a key value pair string where key and value is separated by a colon (:).
};
apiInstance.productsListByInvoiceSection(billingAccountName, billingProfileName, invoiceSectionName, apiVersion, opts, (error, data, response) => {
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
 **filter** | **String**| May be used to filter by product type. The filter supports &#39;eq&#39;, &#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;, and &#39;and&#39;. It does not currently support &#39;ne&#39;, &#39;or&#39;, or &#39;not&#39;. Tag filter is a key value pair string where key and value is separated by a colon (:). | [optional] 

### Return type

[**ProductsListResult**](ProductsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsTransfer

> Product productsTransfer(billingAccountName, billingProfileName, invoiceSectionName, productName, apiVersion, parameters)



The operation to transfer a Product to another invoice section.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.ProductsApi();
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
let productName = "productName_example"; // String | Invoice Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let parameters = new BillingManagementClient.TransferProductRequestProperties(); // TransferProductRequestProperties | Parameters supplied to the Transfer Product operation.
apiInstance.productsTransfer(billingAccountName, billingProfileName, invoiceSectionName, productName, apiVersion, parameters, (error, data, response) => {
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
 **productName** | **String**| Invoice Id. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | 
 **parameters** | [**TransferProductRequestProperties**](TransferProductRequestProperties.md)| Parameters supplied to the Transfer Product operation. | 

### Return type

[**Product**](Product.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## productsUpdateAutoRenewByInvoiceSection

> UpdateAutoRenewOperation productsUpdateAutoRenewByInvoiceSection(billingAccountName, billingProfileName, invoiceSectionName, productName, apiVersion, body)



Cancel auto renew for product by product id and invoice section name

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.ProductsApi();
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
let productName = "productName_example"; // String | Invoice Id.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let body = new BillingManagementClient.UpdateAutoRenewRequest(); // UpdateAutoRenewRequest | Update auto renew request parameters.
apiInstance.productsUpdateAutoRenewByInvoiceSection(billingAccountName, billingProfileName, invoiceSectionName, productName, apiVersion, body, (error, data, response) => {
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
 **productName** | **String**| Invoice Id. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | 
 **body** | [**UpdateAutoRenewRequest**](UpdateAutoRenewRequest.md)| Update auto renew request parameters. | 

### Return type

[**UpdateAutoRenewOperation**](UpdateAutoRenewOperation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

