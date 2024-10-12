# BillingManagementClient.BillingRoleAssignmentsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billingRoleAssignmentsAddByBillingAccountName**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsAddByBillingAccountName) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/providers/Microsoft.Billing/createBillingRoleAssignment | 
[**billingRoleAssignmentsAddByBillingProfileName**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsAddByBillingProfileName) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/providers/Microsoft.Billing/createBillingRoleAssignment | 
[**billingRoleAssignmentsAddByInvoiceSectionName**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsAddByInvoiceSectionName) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/providers/Microsoft.Billing/createBillingRoleAssignment | 
[**billingRoleAssignmentsDeleteByBillingAccountName**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsDeleteByBillingAccountName) | **DELETE** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/providers/Microsoft.Billing/billingRoleAssignments/{billingRoleAssignmentName} | 
[**billingRoleAssignmentsDeleteByBillingProfileName**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsDeleteByBillingProfileName) | **DELETE** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/providers/Microsoft.Billing/billingRoleAssignments/{billingRoleAssignmentName} | 
[**billingRoleAssignmentsDeleteByInvoiceSectionName**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsDeleteByInvoiceSectionName) | **DELETE** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/providers/Microsoft.Billing/billingRoleAssignments/{billingRoleAssignmentName} | 
[**billingRoleAssignmentsGetByBillingAccount**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsGetByBillingAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/providers/Microsoft.Billing/billingRoleAssignments/{billingRoleAssignmentName} | 
[**billingRoleAssignmentsGetByBillingProfileName**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsGetByBillingProfileName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/providers/Microsoft.Billing/billingRoleAssignments/{billingRoleAssignmentName} | 
[**billingRoleAssignmentsGetByInvoiceSectionName**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsGetByInvoiceSectionName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/providers/Microsoft.Billing/billingRoleAssignments/{billingRoleAssignmentName} | 
[**billingRoleAssignmentsListByBillingAccountName**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsListByBillingAccountName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/providers/Microsoft.Billing/billingRoleAssignments | 
[**billingRoleAssignmentsListByBillingProfileName**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsListByBillingProfileName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/providers/Microsoft.Billing/billingRoleAssignments | 
[**billingRoleAssignmentsListByInvoiceSectionName**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsListByInvoiceSectionName) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/providers/Microsoft.Billing/billingRoleAssignments | 



## billingRoleAssignmentsAddByBillingAccountName

> BillingRoleAssignmentListResult billingRoleAssignmentsAddByBillingAccountName(apiVersion, billingAccountName, parameters)



The operation to add a role assignment to a billing account.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleAssignmentsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let parameters = new BillingManagementClient.BillingRoleAssignmentPayload(); // BillingRoleAssignmentPayload | Parameters supplied to add a role assignment.
apiInstance.billingRoleAssignmentsAddByBillingAccountName(apiVersion, billingAccountName, parameters, (error, data, response) => {
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
 **parameters** | [**BillingRoleAssignmentPayload**](BillingRoleAssignmentPayload.md)| Parameters supplied to add a role assignment. | 

### Return type

[**BillingRoleAssignmentListResult**](BillingRoleAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## billingRoleAssignmentsAddByBillingProfileName

> BillingRoleAssignmentListResult billingRoleAssignmentsAddByBillingProfileName(apiVersion, billingAccountName, billingProfileName, parameters)



The operation to add a role assignment to a billing profile.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleAssignmentsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let parameters = new BillingManagementClient.BillingRoleAssignmentPayload(); // BillingRoleAssignmentPayload | Parameters supplied to add a role assignment.
apiInstance.billingRoleAssignmentsAddByBillingProfileName(apiVersion, billingAccountName, billingProfileName, parameters, (error, data, response) => {
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
 **parameters** | [**BillingRoleAssignmentPayload**](BillingRoleAssignmentPayload.md)| Parameters supplied to add a role assignment. | 

### Return type

[**BillingRoleAssignmentListResult**](BillingRoleAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## billingRoleAssignmentsAddByInvoiceSectionName

> BillingRoleAssignmentListResult billingRoleAssignmentsAddByInvoiceSectionName(apiVersion, billingAccountName, invoiceSectionName, parameters)



The operation to add a role assignment to a invoice Section.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleAssignmentsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
let parameters = new BillingManagementClient.BillingRoleAssignmentPayload(); // BillingRoleAssignmentPayload | Parameters supplied to add a role assignment.
apiInstance.billingRoleAssignmentsAddByInvoiceSectionName(apiVersion, billingAccountName, invoiceSectionName, parameters, (error, data, response) => {
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
 **parameters** | [**BillingRoleAssignmentPayload**](BillingRoleAssignmentPayload.md)| Parameters supplied to add a role assignment. | 

### Return type

[**BillingRoleAssignmentListResult**](BillingRoleAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## billingRoleAssignmentsDeleteByBillingAccountName

> BillingRoleAssignment billingRoleAssignmentsDeleteByBillingAccountName(apiVersion, billingAccountName, billingRoleAssignmentName)



Delete the role assignment on this billing account

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleAssignmentsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let billingRoleAssignmentName = "billingRoleAssignmentName_example"; // String | role assignment id.
apiInstance.billingRoleAssignmentsDeleteByBillingAccountName(apiVersion, billingAccountName, billingRoleAssignmentName, (error, data, response) => {
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
 **billingRoleAssignmentName** | **String**| role assignment id. | 

### Return type

[**BillingRoleAssignment**](BillingRoleAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingRoleAssignmentsDeleteByBillingProfileName

> BillingRoleAssignment billingRoleAssignmentsDeleteByBillingProfileName(apiVersion, billingAccountName, billingProfileName, billingRoleAssignmentName)



Delete the role assignment on this Billing Profile

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleAssignmentsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let billingRoleAssignmentName = "billingRoleAssignmentName_example"; // String | role assignment id.
apiInstance.billingRoleAssignmentsDeleteByBillingProfileName(apiVersion, billingAccountName, billingProfileName, billingRoleAssignmentName, (error, data, response) => {
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
 **billingRoleAssignmentName** | **String**| role assignment id. | 

### Return type

[**BillingRoleAssignment**](BillingRoleAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingRoleAssignmentsDeleteByInvoiceSectionName

> BillingRoleAssignment billingRoleAssignmentsDeleteByInvoiceSectionName(apiVersion, billingAccountName, invoiceSectionName, billingRoleAssignmentName)



Delete the role assignment on the invoice Section

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleAssignmentsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
let billingRoleAssignmentName = "billingRoleAssignmentName_example"; // String | role assignment id.
apiInstance.billingRoleAssignmentsDeleteByInvoiceSectionName(apiVersion, billingAccountName, invoiceSectionName, billingRoleAssignmentName, (error, data, response) => {
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
 **billingRoleAssignmentName** | **String**| role assignment id. | 

### Return type

[**BillingRoleAssignment**](BillingRoleAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingRoleAssignmentsGetByBillingAccount

> BillingRoleAssignment billingRoleAssignmentsGetByBillingAccount(apiVersion, billingAccountName, billingRoleAssignmentName)



Get the role assignment for the caller

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleAssignmentsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let billingRoleAssignmentName = "billingRoleAssignmentName_example"; // String | role assignment id.
apiInstance.billingRoleAssignmentsGetByBillingAccount(apiVersion, billingAccountName, billingRoleAssignmentName, (error, data, response) => {
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
 **billingRoleAssignmentName** | **String**| role assignment id. | 

### Return type

[**BillingRoleAssignment**](BillingRoleAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingRoleAssignmentsGetByBillingProfileName

> BillingRoleAssignment billingRoleAssignmentsGetByBillingProfileName(apiVersion, billingAccountName, billingProfileName, billingRoleAssignmentName)



Get the role assignment for the caller on the Billing Profile

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleAssignmentsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let billingRoleAssignmentName = "billingRoleAssignmentName_example"; // String | role assignment id.
apiInstance.billingRoleAssignmentsGetByBillingProfileName(apiVersion, billingAccountName, billingProfileName, billingRoleAssignmentName, (error, data, response) => {
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
 **billingRoleAssignmentName** | **String**| role assignment id. | 

### Return type

[**BillingRoleAssignment**](BillingRoleAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingRoleAssignmentsGetByInvoiceSectionName

> BillingRoleAssignment billingRoleAssignmentsGetByInvoiceSectionName(apiVersion, billingAccountName, invoiceSectionName, billingRoleAssignmentName)



Get the role assignment for the caller on the invoice Section

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleAssignmentsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
let billingRoleAssignmentName = "billingRoleAssignmentName_example"; // String | role assignment id.
apiInstance.billingRoleAssignmentsGetByInvoiceSectionName(apiVersion, billingAccountName, invoiceSectionName, billingRoleAssignmentName, (error, data, response) => {
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
 **billingRoleAssignmentName** | **String**| role assignment id. | 

### Return type

[**BillingRoleAssignment**](BillingRoleAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingRoleAssignmentsListByBillingAccountName

> BillingRoleAssignmentListResult billingRoleAssignmentsListByBillingAccountName(apiVersion, billingAccountName)



Get the role assignments on the Billing Account

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleAssignmentsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
apiInstance.billingRoleAssignmentsListByBillingAccountName(apiVersion, billingAccountName, (error, data, response) => {
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

### Return type

[**BillingRoleAssignmentListResult**](BillingRoleAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingRoleAssignmentsListByBillingProfileName

> BillingRoleAssignmentListResult billingRoleAssignmentsListByBillingProfileName(apiVersion, billingAccountName, billingProfileName)



Get the role assignments on the Billing Profile

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleAssignmentsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
apiInstance.billingRoleAssignmentsListByBillingProfileName(apiVersion, billingAccountName, billingProfileName, (error, data, response) => {
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

[**BillingRoleAssignmentListResult**](BillingRoleAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingRoleAssignmentsListByInvoiceSectionName

> BillingRoleAssignmentListResult billingRoleAssignmentsListByInvoiceSectionName(apiVersion, billingAccountName, invoiceSectionName)



Get the role assignments on the invoice Section

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleAssignmentsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-11-01-preview.
let billingAccountName = "billingAccountName_example"; // String | Billing Account Id.
let invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
apiInstance.billingRoleAssignmentsListByInvoiceSectionName(apiVersion, billingAccountName, invoiceSectionName, (error, data, response) => {
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

### Return type

[**BillingRoleAssignmentListResult**](BillingRoleAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

