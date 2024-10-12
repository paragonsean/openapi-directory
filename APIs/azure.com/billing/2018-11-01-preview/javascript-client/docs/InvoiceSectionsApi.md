# BillingManagementClient.InvoiceSectionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoiceSectionsCreate**](InvoiceSectionsApi.md#invoiceSectionsCreate) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections | 
[**invoiceSectionsElevateToBillingProfile**](InvoiceSectionsApi.md#invoiceSectionsElevateToBillingProfile) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/elevate | 
[**invoiceSectionsGet**](InvoiceSectionsApi.md#invoiceSectionsGet) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName} | 
[**invoiceSectionsListByBillingAccountName**](InvoiceSectionsApi.md#invoiceSectionsListByBillingAccountName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections | 
[**invoiceSectionsListByBillingProfileName**](InvoiceSectionsApi.md#invoiceSectionsListByBillingProfileName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections | 
[**invoiceSectionsListByCreateSubscriptionPermission**](InvoiceSectionsApi.md#invoiceSectionsListByCreateSubscriptionPermission) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/listInvoiceSectionsWithCreateSubscriptionPermission | 
[**invoiceSectionsUpdate**](InvoiceSectionsApi.md#invoiceSectionsUpdate) | **PUT** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName} | 



## invoiceSectionsCreate

> InvoiceSection invoiceSectionsCreate(apiVersion, billingAccountName, parameters)



The operation to create a InvoiceSection.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.InvoiceSectionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let parameters = new BillingManagementClient.InvoiceSectionCreationRequest(); // InvoiceSectionCreationRequest | Parameters supplied to the Create InvoiceSection operation.
apiInstance.invoiceSectionsCreate(apiVersion, billingAccountName, parameters, (error, data, response) => {
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
 **parameters** | [**InvoiceSectionCreationRequest**](InvoiceSectionCreationRequest.md)| Parameters supplied to the Create InvoiceSection operation. | 

### Return type

[**InvoiceSection**](InvoiceSection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## invoiceSectionsElevateToBillingProfile

> invoiceSectionsElevateToBillingProfile(billingAccountName, invoiceSectionName)



Elevates the caller&#39;s access to match their billing profile access.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.InvoiceSectionsApi();
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
apiInstance.invoiceSectionsElevateToBillingProfile(billingAccountName, invoiceSectionName, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billingAccountName** | **String**| Billing Account Id. | 
 **invoiceSectionName** | **String**| InvoiceSection Id. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoiceSectionsGet

> InvoiceSection invoiceSectionsGet(apiVersion, billingAccountName, invoiceSectionName, opts)



Get the InvoiceSection by id.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.InvoiceSectionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
let opts = {
  'expand': "expand_example" // String | May be used to expand the billingProfiles.
};
apiInstance.invoiceSectionsGet(apiVersion, billingAccountName, invoiceSectionName, opts, (error, data, response) => {
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
 **invoiceSectionName** | **String**| InvoiceSection Id. | 
 **expand** | **String**| May be used to expand the billingProfiles. | [optional] 

### Return type

[**InvoiceSection**](InvoiceSection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoiceSectionsListByBillingAccountName

> InvoiceSectionListResult invoiceSectionsListByBillingAccountName(apiVersion, billingAccountName, opts)



Lists all invoice sections for which a user has access.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.InvoiceSectionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let opts = {
  'expand': "expand_example" // String | May be used to expand the billingProfiles.
};
apiInstance.invoiceSectionsListByBillingAccountName(apiVersion, billingAccountName, opts, (error, data, response) => {
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
 **expand** | **String**| May be used to expand the billingProfiles. | [optional] 

### Return type

[**InvoiceSectionListResult**](InvoiceSectionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoiceSectionsListByBillingProfileName

> InvoiceSectionListResult invoiceSectionsListByBillingProfileName(apiVersion, billingAccountName, billingProfileName)



Lists all invoice sections under a billing profile for which a user has access.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.InvoiceSectionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
apiInstance.invoiceSectionsListByBillingProfileName(apiVersion, billingAccountName, billingProfileName, (error, data, response) => {
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
 **billingProfileName** | **String**| Billing Profile Id. | 

### Return type

[**InvoiceSectionListResult**](InvoiceSectionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoiceSectionsListByCreateSubscriptionPermission

> InvoiceSectionListResult invoiceSectionsListByCreateSubscriptionPermission(apiVersion, billingAccountName, opts)



Lists all invoiceSections with create subscription permission for a user.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.InvoiceSectionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let opts = {
  'expand': "expand_example" // String | May be used to expand the billingProfiles.
};
apiInstance.invoiceSectionsListByCreateSubscriptionPermission(apiVersion, billingAccountName, opts, (error, data, response) => {
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
 **expand** | **String**| May be used to expand the billingProfiles. | [optional] 

### Return type

[**InvoiceSectionListResult**](InvoiceSectionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoiceSectionsUpdate

> InvoiceSection invoiceSectionsUpdate(apiVersion, billingAccountName, invoiceSectionName, parameters)



The operation to update a InvoiceSection.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.InvoiceSectionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
let parameters = new BillingManagementClient.InvoiceSection(); // InvoiceSection | Parameters supplied to the Create InvoiceSection operation.
apiInstance.invoiceSectionsUpdate(apiVersion, billingAccountName, invoiceSectionName, parameters, (error, data, response) => {
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
 **invoiceSectionName** | **String**| InvoiceSection Id. | 
 **parameters** | [**InvoiceSection**](InvoiceSection.md)| Parameters supplied to the Create InvoiceSection operation. | 

### Return type

[**InvoiceSection**](InvoiceSection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

