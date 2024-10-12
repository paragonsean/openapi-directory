# BillingManagementClient.BillingRoleAssignmentsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billingRoleAssignmentsAddByBillingAccount**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsAddByBillingAccount) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/createBillingRoleAssignment | 
[**billingRoleAssignmentsAddByBillingProfile**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsAddByBillingProfile) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/createBillingRoleAssignment | 
[**billingRoleAssignmentsAddByInvoiceSection**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsAddByInvoiceSection) | **POST** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/createBillingRoleAssignment | 
[**billingRoleAssignmentsDeleteByBillingAccount**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsDeleteByBillingAccount) | **DELETE** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingRoleAssignments/{billingRoleAssignmentName} | 
[**billingRoleAssignmentsDeleteByBillingProfile**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsDeleteByBillingProfile) | **DELETE** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/billingRoleAssignments/{billingRoleAssignmentName} | 
[**billingRoleAssignmentsDeleteByInvoiceSection**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsDeleteByInvoiceSection) | **DELETE** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/billingRoleAssignments/{billingRoleAssignmentName} | 
[**billingRoleAssignmentsGetByBillingAccount**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsGetByBillingAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingRoleAssignments/{billingRoleAssignmentName} | 
[**billingRoleAssignmentsGetByBillingProfile**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsGetByBillingProfile) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/billingRoleAssignments/{billingRoleAssignmentName} | 
[**billingRoleAssignmentsGetByInvoiceSection**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsGetByInvoiceSection) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/billingRoleAssignments/{billingRoleAssignmentName} | 
[**billingRoleAssignmentsListByBillingAccount**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsListByBillingAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingRoleAssignments | 
[**billingRoleAssignmentsListByBillingProfile**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsListByBillingProfile) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/billingRoleAssignments | 
[**billingRoleAssignmentsListByInvoiceSection**](BillingRoleAssignmentsApi.md#billingRoleAssignmentsListByInvoiceSection) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/billingProfiles/{billingProfileName}/invoiceSections/{invoiceSectionName}/billingRoleAssignments | 



## billingRoleAssignmentsAddByBillingAccount

> BillingRoleAssignmentListResult billingRoleAssignmentsAddByBillingAccount(apiVersion, billingAccountName, parameters)



The operation to add a role assignment to a billing account.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleAssignmentsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let parameters = new BillingManagementClient.BillingRoleAssignmentPayload(); // BillingRoleAssignmentPayload | Parameters supplied to add a role assignment.
apiInstance.billingRoleAssignmentsAddByBillingAccount(apiVersion, billingAccountName, parameters, (error, data, response) => {
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
 **parameters** | [**BillingRoleAssignmentPayload**](BillingRoleAssignmentPayload.md)| Parameters supplied to add a role assignment. | 

### Return type

[**BillingRoleAssignmentListResult**](BillingRoleAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## billingRoleAssignmentsAddByBillingProfile

> BillingRoleAssignmentListResult billingRoleAssignmentsAddByBillingProfile(apiVersion, billingAccountName, billingProfileName, parameters)



The operation to add a role assignment to a billing profile.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleAssignmentsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let parameters = new BillingManagementClient.BillingRoleAssignmentPayload(); // BillingRoleAssignmentPayload | Parameters supplied to add a role assignment.
apiInstance.billingRoleAssignmentsAddByBillingProfile(apiVersion, billingAccountName, billingProfileName, parameters, (error, data, response) => {
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
 **parameters** | [**BillingRoleAssignmentPayload**](BillingRoleAssignmentPayload.md)| Parameters supplied to add a role assignment. | 

### Return type

[**BillingRoleAssignmentListResult**](BillingRoleAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## billingRoleAssignmentsAddByInvoiceSection

> BillingRoleAssignmentListResult billingRoleAssignmentsAddByInvoiceSection(apiVersion, billingAccountName, billingProfileName, invoiceSectionName, parameters)



The operation to add a role assignment to a invoice Section.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleAssignmentsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
let parameters = new BillingManagementClient.BillingRoleAssignmentPayload(); // BillingRoleAssignmentPayload | Parameters supplied to add a role assignment.
apiInstance.billingRoleAssignmentsAddByInvoiceSection(apiVersion, billingAccountName, billingProfileName, invoiceSectionName, parameters, (error, data, response) => {
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
 **parameters** | [**BillingRoleAssignmentPayload**](BillingRoleAssignmentPayload.md)| Parameters supplied to add a role assignment. | 

### Return type

[**BillingRoleAssignmentListResult**](BillingRoleAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## billingRoleAssignmentsDeleteByBillingAccount

> BillingRoleAssignment billingRoleAssignmentsDeleteByBillingAccount(apiVersion, billingAccountName, billingRoleAssignmentName)



Delete the role assignment on this billing account

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleAssignmentsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingRoleAssignmentName = "billingRoleAssignmentName_example"; // String | role assignment id.
apiInstance.billingRoleAssignmentsDeleteByBillingAccount(apiVersion, billingAccountName, billingRoleAssignmentName, (error, data, response) => {
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
 **billingRoleAssignmentName** | **String**| role assignment id. | 

### Return type

[**BillingRoleAssignment**](BillingRoleAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingRoleAssignmentsDeleteByBillingProfile

> BillingRoleAssignment billingRoleAssignmentsDeleteByBillingProfile(apiVersion, billingAccountName, billingProfileName, billingRoleAssignmentName)



Delete the role assignment on this Billing Profile

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleAssignmentsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let billingRoleAssignmentName = "billingRoleAssignmentName_example"; // String | role assignment id.
apiInstance.billingRoleAssignmentsDeleteByBillingProfile(apiVersion, billingAccountName, billingProfileName, billingRoleAssignmentName, (error, data, response) => {
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
 **billingRoleAssignmentName** | **String**| role assignment id. | 

### Return type

[**BillingRoleAssignment**](BillingRoleAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingRoleAssignmentsDeleteByInvoiceSection

> BillingRoleAssignment billingRoleAssignmentsDeleteByInvoiceSection(apiVersion, billingAccountName, billingProfileName, invoiceSectionName, billingRoleAssignmentName)



Delete the role assignment on the invoice Section

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleAssignmentsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
let billingRoleAssignmentName = "billingRoleAssignmentName_example"; // String | role assignment id.
apiInstance.billingRoleAssignmentsDeleteByInvoiceSection(apiVersion, billingAccountName, billingProfileName, invoiceSectionName, billingRoleAssignmentName, (error, data, response) => {
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
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | 
 **billingAccountName** | **String**| billing Account Id. | 
 **billingRoleAssignmentName** | **String**| role assignment id. | 

### Return type

[**BillingRoleAssignment**](BillingRoleAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingRoleAssignmentsGetByBillingProfile

> BillingRoleAssignment billingRoleAssignmentsGetByBillingProfile(apiVersion, billingAccountName, billingProfileName, billingRoleAssignmentName)



Get the role assignment for the caller on the Billing Profile

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleAssignmentsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let billingRoleAssignmentName = "billingRoleAssignmentName_example"; // String | role assignment id.
apiInstance.billingRoleAssignmentsGetByBillingProfile(apiVersion, billingAccountName, billingProfileName, billingRoleAssignmentName, (error, data, response) => {
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
 **billingRoleAssignmentName** | **String**| role assignment id. | 

### Return type

[**BillingRoleAssignment**](BillingRoleAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingRoleAssignmentsGetByInvoiceSection

> BillingRoleAssignment billingRoleAssignmentsGetByInvoiceSection(apiVersion, billingAccountName, billingProfileName, invoiceSectionName, billingRoleAssignmentName)



Get the role assignment for the caller on the invoice Section

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleAssignmentsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
let billingRoleAssignmentName = "billingRoleAssignmentName_example"; // String | role assignment id.
apiInstance.billingRoleAssignmentsGetByInvoiceSection(apiVersion, billingAccountName, billingProfileName, invoiceSectionName, billingRoleAssignmentName, (error, data, response) => {
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
 **billingRoleAssignmentName** | **String**| role assignment id. | 

### Return type

[**BillingRoleAssignment**](BillingRoleAssignment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingRoleAssignmentsListByBillingAccount

> BillingRoleAssignmentListResult billingRoleAssignmentsListByBillingAccount(apiVersion, billingAccountName)



Get the role assignments on the Billing Account

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleAssignmentsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
apiInstance.billingRoleAssignmentsListByBillingAccount(apiVersion, billingAccountName, (error, data, response) => {
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

[**BillingRoleAssignmentListResult**](BillingRoleAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingRoleAssignmentsListByBillingProfile

> BillingRoleAssignmentListResult billingRoleAssignmentsListByBillingProfile(apiVersion, billingAccountName, billingProfileName)



Get the role assignments on the Billing Profile

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleAssignmentsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
apiInstance.billingRoleAssignmentsListByBillingProfile(apiVersion, billingAccountName, billingProfileName, (error, data, response) => {
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

[**BillingRoleAssignmentListResult**](BillingRoleAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## billingRoleAssignmentsListByInvoiceSection

> BillingRoleAssignmentListResult billingRoleAssignmentsListByInvoiceSection(apiVersion, billingAccountName, billingProfileName, invoiceSectionName)



Get the role assignments on the invoice Section

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.BillingRoleAssignmentsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let billingProfileName = "billingProfileName_example"; // String | Billing Profile Id.
let invoiceSectionName = "invoiceSectionName_example"; // String | InvoiceSection Id.
apiInstance.billingRoleAssignmentsListByInvoiceSection(apiVersion, billingAccountName, billingProfileName, invoiceSectionName, (error, data, response) => {
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

[**BillingRoleAssignmentListResult**](BillingRoleAssignmentListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

