# BillingManagementClient.BillingRoleDefinitionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billingRoleDefinitionsGetByBillingAccount**](BillingRoleDefinitionsApi.md#billingRoleDefinitionsGetByBillingAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingRoleDefinitions/{billingRoleDefinitionName} | 
[**billingRoleDefinitionsGetByBillingProfile**](BillingRoleDefinitionsApi.md#billingRoleDefinitionsGetByBillingProfile) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/billingRoleDefinitions/{billingRoleDefinitionName} | 
[**billingRoleDefinitionsGetByInvoiceSection**](BillingRoleDefinitionsApi.md#billingRoleDefinitionsGetByInvoiceSection) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/billingRoleDefinitions/{billingRoleDefinitionName} | 
[**billingRoleDefinitionsListByBillingAccount**](BillingRoleDefinitionsApi.md#billingRoleDefinitionsListByBillingAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingRoleDefinitions | 
[**billingRoleDefinitionsListByBillingProfile**](BillingRoleDefinitionsApi.md#billingRoleDefinitionsListByBillingProfile) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/billingRoleDefinitions | 
[**billingRoleDefinitionsListByInvoiceSection**](BillingRoleDefinitionsApi.md#billingRoleDefinitionsListByInvoiceSection) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/billingRoleDefinitions | 



## billingRoleDefinitionsGetByBillingAccount

> BillingRoleDefinition billingRoleDefinitionsGetByBillingAccount(apiVersion, billingAccountName, billingRoleDefinitionName)



Gets the role definition for a role

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleDefinitionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingRoleDefinitionName = "billingRoleDefinitionName_example"; // String | role definition id.
apiInstance.billingRoleDefinitionsGetByBillingAccount(apiVersion, billingAccountName, billingRoleDefinitionName, (error, data, response) => {
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
 **billingRoleDefinitionName** | **String**| role definition id. | 

### Return type

[**BillingRoleDefinition**](BillingRoleDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingRoleDefinitionsGetByBillingProfile

> BillingRoleDefinition billingRoleDefinitionsGetByBillingProfile(apiVersion, billingAccountName, billingProfileName, billingRoleDefinitionName)



Gets the role definition for a role

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleDefinitionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let billingRoleDefinitionName = "billingRoleDefinitionName_example"; // String | role definition id.
apiInstance.billingRoleDefinitionsGetByBillingProfile(apiVersion, billingAccountName, billingProfileName, billingRoleDefinitionName, (error, data, response) => {
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
 **billingRoleDefinitionName** | **String**| role definition id. | 

### Return type

[**BillingRoleDefinition**](BillingRoleDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingRoleDefinitionsGetByInvoiceSection

> BillingRoleDefinition billingRoleDefinitionsGetByInvoiceSection(apiVersion, billingAccountName, billingProfileName, invoiceSectionName, billingRoleDefinitionName)



Gets the role definition for a role

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleDefinitionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
let billingRoleDefinitionName = "billingRoleDefinitionName_example"; // String | role definition id.
apiInstance.billingRoleDefinitionsGetByInvoiceSection(apiVersion, billingAccountName, billingProfileName, invoiceSectionName, billingRoleDefinitionName, (error, data, response) => {
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
 **invoiceSectionName** | **String**| InvoiceSection Id. | 
 **billingRoleDefinitionName** | **String**| role definition id. | 

### Return type

[**BillingRoleDefinition**](BillingRoleDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingRoleDefinitionsListByBillingAccount

> BillingRoleDefinitionListResult billingRoleDefinitionsListByBillingAccount(apiVersion, billingAccountName)



Lists the role definition for a billing account

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleDefinitionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
apiInstance.billingRoleDefinitionsListByBillingAccount(apiVersion, billingAccountName, (error, data, response) => {
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

### Return type

[**BillingRoleDefinitionListResult**](BillingRoleDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingRoleDefinitionsListByBillingProfile

> BillingRoleDefinitionListResult billingRoleDefinitionsListByBillingProfile(apiVersion, billingAccountName, billingProfileName)



Lists the role definition for a Billing Profile

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleDefinitionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
apiInstance.billingRoleDefinitionsListByBillingProfile(apiVersion, billingAccountName, billingProfileName, (error, data, response) => {
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

### Return type

[**BillingRoleDefinitionListResult**](BillingRoleDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingRoleDefinitionsListByInvoiceSection

> BillingRoleDefinitionListResult billingRoleDefinitionsListByInvoiceSection(apiVersion, billingAccountName, billingProfileName, invoiceSectionName)



Lists the role definition for an invoice Section

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleDefinitionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
apiInstance.billingRoleDefinitionsListByInvoiceSection(apiVersion, billingAccountName, billingProfileName, invoiceSectionName, (error, data, response) => {
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
 **invoiceSectionName** | **String**| InvoiceSection Id. | 

### Return type

[**BillingRoleDefinitionListResult**](BillingRoleDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

