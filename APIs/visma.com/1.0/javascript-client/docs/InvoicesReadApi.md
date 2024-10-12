# SeveraPublicRestApiDocumentation.InvoicesReadApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**finvoicesGetFinvoiceByInvoiceGuid**](InvoicesReadApi.md#finvoicesGetFinvoiceByInvoiceGuid) | **GET** /v1/invoices/{invoiceGuid}/finvoice | 
[**finvoicesGetFinvoicesByInvoiceStatus**](InvoicesReadApi.md#finvoicesGetFinvoicesByInvoiceStatus) | **GET** /v1/invoicestatuses/{invoiceStatusGuid}/finvoices | 
[**invoiceRowsGetInvoiceRow**](InvoicesReadApi.md#invoiceRowsGetInvoiceRow) | **GET** /v1/invoicerows/{guid} | Get invoice row by ID
[**invoiceRowsGetInvoiceRows**](InvoicesReadApi.md#invoiceRowsGetInvoiceRows) | **GET** /v1/invoicerows | Get invoice rows
[**invoiceRowsGetInvoiceRowsForInvoice**](InvoicesReadApi.md#invoiceRowsGetInvoiceRowsForInvoice) | **GET** /v1/invoices/{invoiceGuid}/invoicerows | Get Invoice rows for an invoice.
[**invoiceSettingsGetInvoiceSettings**](InvoicesReadApi.md#invoiceSettingsGetInvoiceSettings) | **GET** /v1/invoices/{invoiceGuid}/invoicesettings | Get invoice settings by invoice GUID
[**invoicesGetInvoice**](InvoicesReadApi.md#invoicesGetInvoice) | **GET** /v1/invoices/{guid} | Get invoice by ID
[**invoicesGetInvoices**](InvoicesReadApi.md#invoicesGetInvoices) | **GET** /v1/invoices | Get Invoices
[**projectFeesGetInvoiceProjectFees**](InvoicesReadApi.md#projectFeesGetInvoiceProjectFees) | **GET** /v1/invoices/{invoiceGuid}/projectfees | Get all the project fees on an invoice
[**projectFeesGetInvoiceRowProjectFees**](InvoicesReadApi.md#projectFeesGetInvoiceRowProjectFees) | **GET** /v1/invoicerows/{invoiceRowGuid}/projectfees | Get all the project fees on an invoice row
[**projectFeesGetUninvoicedProjectFeesForInvoice**](InvoicesReadApi.md#projectFeesGetUninvoicedProjectFeesForInvoice) | **GET** /v1/invoices/{invoiceGuid}/uninvoicedprojectfees | Get uninvoiced project fees available for invoice
[**projectInvoiceSettingsGetProjectInvoiceSetting**](InvoicesReadApi.md#projectInvoiceSettingsGetProjectInvoiceSetting) | **GET** /v1/projectinvoicesettings/{guid} | Get project invoice settings by ID.
[**projectInvoiceSettingsGetProjectInvoiceSettings**](InvoicesReadApi.md#projectInvoiceSettingsGetProjectInvoiceSettings) | **GET** /v1/projects/{projectGuid}/projectinvoicesettings | Get project invoice settings by project ID.
[**projectTravelExpensesGetInvoiceProjectTravelExpenses**](InvoicesReadApi.md#projectTravelExpensesGetInvoiceProjectTravelExpenses) | **GET** /v1/invoices/{invoiceGuid}/projecttravelexpenses | Get all the project travel expenses on an invoice
[**projectTravelExpensesGetInvoiceRowProjectTravelExpenses**](InvoicesReadApi.md#projectTravelExpensesGetInvoiceRowProjectTravelExpenses) | **GET** /v1/invoicerows/{invoiceRowGuid}/projecttravelexpenses | Get all the project travel expenses on an invoice row
[**projectTravelExpensesGetUninvoicedProjectTravelExpensesForInvoice**](InvoicesReadApi.md#projectTravelExpensesGetUninvoicedProjectTravelExpensesForInvoice) | **GET** /v1/invoices/{invoiceGuid}/uninvoicedprojecttravelexpenses | Get uninvoiced project travel expenses available for invoice
[**reimbursedProjectFeesGetInvoiceReimbursedProjectFees**](InvoicesReadApi.md#reimbursedProjectFeesGetInvoiceReimbursedProjectFees) | **GET** /v1/invoices/{invoiceGuid}/reimbursedprojectfees | Get all the project fees on an invoice
[**reimbursedProjectFeesGetInvoiceRowReimbursedProjectFees**](InvoicesReadApi.md#reimbursedProjectFeesGetInvoiceRowReimbursedProjectFees) | **GET** /v1/invoicerows/{invoiceRowGuid}/reimbursedprojectfees | Get all the project fees on an invoice row
[**reimbursedProjectTravelExpensesGetInvoiceProjectTravelExpenses**](InvoicesReadApi.md#reimbursedProjectTravelExpensesGetInvoiceProjectTravelExpenses) | **GET** /v1/invoices/{invoiceGuid}/reimbursedprojecttravelexpenses | Get all the project travel expenses on an invoice.
[**reimbursedProjectTravelExpensesGetInvoiceRowProjectTravelExpenses**](InvoicesReadApi.md#reimbursedProjectTravelExpensesGetInvoiceRowProjectTravelExpenses) | **GET** /v1/invoicerows/{invoiceRowGuid}/reimbursedprojecttravelexpenses | Get all the project travel expenses on an invoice row.
[**reimbursedWorkHoursGetInvoiceReimbursedWorkHours**](InvoicesReadApi.md#reimbursedWorkHoursGetInvoiceReimbursedWorkHours) | **GET** /v1/invoices/{invoiceGuid}/reimbursedworkhours | Get all reimbursed hours on an invoice.
[**reimbursedWorkHoursGetInvoiceRowReimbursedWorkHours**](InvoicesReadApi.md#reimbursedWorkHoursGetInvoiceRowReimbursedWorkHours) | **GET** /v1/invoicerows/{invoiceRowGuid}/reimbursedworkhours | Get all reimbursed hours on an invoice row.
[**workHoursGetInvoiceRowWorkHours**](InvoicesReadApi.md#workHoursGetInvoiceRowWorkHours) | **GET** /v1/invoicerows/{invoiceRowGuid}/workhours | Get all the work hours on an invoice row
[**workHoursGetInvoiceWorkHours**](InvoicesReadApi.md#workHoursGetInvoiceWorkHours) | **GET** /v1/invoices/{invoiceGuid}/workhours | Get all the work hours on an invoice
[**workHoursGetUninvoicedWorkHoursForInvoice**](InvoicesReadApi.md#workHoursGetUninvoicedWorkHoursForInvoice) | **GET** /v1/invoices/{invoiceGuid}/uninvoicedworkhours | Get uninvoiced work hours available for invoice



## finvoicesGetFinvoiceByInvoiceGuid

> File finvoicesGetFinvoiceByInvoiceGuid(invoiceGuid)



### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesReadApi();
let invoiceGuid = "invoiceGuid_example"; // String | 
apiInstance.finvoicesGetFinvoiceByInvoiceGuid(invoiceGuid, (error, data, response) => {
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
 **invoiceGuid** | **String**|  | 

### Return type

**File**

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/soap+xml, application/json


## finvoicesGetFinvoicesByInvoiceStatus

> File finvoicesGetFinvoicesByInvoiceStatus(invoiceStatusGuid)



### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesReadApi();
let invoiceStatusGuid = "invoiceStatusGuid_example"; // String | 
apiInstance.finvoicesGetFinvoicesByInvoiceStatus(invoiceStatusGuid, (error, data, response) => {
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
 **invoiceStatusGuid** | **String**|  | 

### Return type

**File**

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json


## invoiceRowsGetInvoiceRow

> InvoiceRowOutputModel invoiceRowsGetInvoiceRow(guid)

Get invoice row by ID

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesReadApi();
let guid = "guid_example"; // String | GUID of the invoice row.
apiInstance.invoiceRowsGetInvoiceRow(guid, (error, data, response) => {
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
 **guid** | **String**| GUID of the invoice row. | 

### Return type

[**InvoiceRowOutputModel**](InvoiceRowOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoiceRowsGetInvoiceRows

> [InvoiceRowOutputModel] invoiceRowsGetInvoiceRows(opts)

Get invoice rows

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesReadApi();
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'changedSince': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: Get invoice rows that have been added or changed after this date time (greater or equal).
};
apiInstance.invoiceRowsGetInvoiceRows(opts, (error, data, response) => {
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
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **changedSince** | **Date**| Optional: Get invoice rows that have been added or changed after this date time (greater or equal). | [optional] 

### Return type

[**[InvoiceRowOutputModel]**](InvoiceRowOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoiceRowsGetInvoiceRowsForInvoice

> [InvoiceRowOutputModel] invoiceRowsGetInvoiceRowsForInvoice(invoiceGuid, opts)

Get Invoice rows for an invoice.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesReadApi();
let invoiceGuid = "invoiceGuid_example"; // String | ID of the invoice.
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'rowType': new SeveraPublicRestApiDocumentation.InvoiceRowType() // InvoiceRowType | Optional: Type of the row. Either Hours or ProjectFees, Default all.
};
apiInstance.invoiceRowsGetInvoiceRowsForInvoice(invoiceGuid, opts, (error, data, response) => {
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
 **invoiceGuid** | **String**| ID of the invoice. | 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **rowType** | [**InvoiceRowType**](.md)| Optional: Type of the row. Either Hours or ProjectFees, Default all. | [optional] 

### Return type

[**[InvoiceRowOutputModel]**](InvoiceRowOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoiceSettingsGetInvoiceSettings

> InvoiceSettingsOutputModel invoiceSettingsGetInvoiceSettings(invoiceGuid)

Get invoice settings by invoice GUID

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesReadApi();
let invoiceGuid = "invoiceGuid_example"; // String | Invoice GUID used to get the invoice settings.
apiInstance.invoiceSettingsGetInvoiceSettings(invoiceGuid, (error, data, response) => {
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
 **invoiceGuid** | **String**| Invoice GUID used to get the invoice settings. | 

### Return type

[**InvoiceSettingsOutputModel**](InvoiceSettingsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoicesGetInvoice

> InvoiceOutputModel invoicesGetInvoice(guid)

Get invoice by ID

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesReadApi();
let guid = "guid_example"; // String | GUID of the invoice.
apiInstance.invoicesGetInvoice(guid, (error, data, response) => {
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
 **guid** | **String**| GUID of the invoice. | 

### Return type

[**InvoiceOutputModel**](InvoiceOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoicesGetInvoices

> [InvoiceOutputModel] invoicesGetInvoices(opts)

Get Invoices

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesReadApi();
let opts = {
  'rowCount': 56, // Number | Optional: Number of rows to fetch.
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'paymentDateStart': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: Get only invoices paid at this date or later. Default: Get invoices regardless of payment date.
  'invoiceStatusGuids': ["null"], // [String] | Optional: Get invoices with this status only. Default: all statuses.
  'projectGuids': ["null"], // [String] | Optional: ID of the project to get the invoices. If not provided, returns for all projects. Default all.
  'projectOwnerGuids': ["null"], // [String] | Optional: ID of the project manager to get the invoices for. If not provided, returns for all project managers. Default all.
  'projectBusinessUnitGuids': ["null"], // [String] | Optional: ID of the business unit of the project. If not provided, returns for all business units. Default all.
  'customerGuids': ["null"], // [String] | Optional: List of customer IDs. Get invoices for these customers.
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: starting date from which to get the invoices. Default all.
  'endDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: end date from which to get the invoices. Default all.
  'minimumTotalExcludingTax': 3.4, // Number | Optional: specifies minimum value for invoice total in organization currency.
  'maximumTotalExcludingTax': 3.4, // Number | Optional: specifies maximum value for invoice total in organization currency.
  'referenceNumbers': ["null"], // [String] | Optional: Invoice reference number. If not provided, returns invoices with any invoice reference number.
  'numbers': [null], // [Number] | Optional: Invoice number. If not provided, returns invoices with any invoice number.
  'changedSince': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: Get invoices that have been added or changed after this date time (greater or equal).
  'salesPersonGuids': ["null"], // [String] | Optional: ID of the salesperson to get the invoices for. If not provided, returns for all sales persons.
  'createdByUserGuids': ["null"] // [String] | Optional: ID of the user who created the invoice. If not provided, returns for all users.
};
apiInstance.invoicesGetInvoices(opts, (error, data, response) => {
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
 **rowCount** | **Number**| Optional: Number of rows to fetch. | [optional] 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **paymentDateStart** | **Date**| Optional: Get only invoices paid at this date or later. Default: Get invoices regardless of payment date. | [optional] 
 **invoiceStatusGuids** | [**[String]**](String.md)| Optional: Get invoices with this status only. Default: all statuses. | [optional] 
 **projectGuids** | [**[String]**](String.md)| Optional: ID of the project to get the invoices. If not provided, returns for all projects. Default all. | [optional] 
 **projectOwnerGuids** | [**[String]**](String.md)| Optional: ID of the project manager to get the invoices for. If not provided, returns for all project managers. Default all. | [optional] 
 **projectBusinessUnitGuids** | [**[String]**](String.md)| Optional: ID of the business unit of the project. If not provided, returns for all business units. Default all. | [optional] 
 **customerGuids** | [**[String]**](String.md)| Optional: List of customer IDs. Get invoices for these customers. | [optional] 
 **startDate** | **Date**| Optional: starting date from which to get the invoices. Default all. | [optional] 
 **endDate** | **Date**| Optional: end date from which to get the invoices. Default all. | [optional] 
 **minimumTotalExcludingTax** | **Number**| Optional: specifies minimum value for invoice total in organization currency. | [optional] 
 **maximumTotalExcludingTax** | **Number**| Optional: specifies maximum value for invoice total in organization currency. | [optional] 
 **referenceNumbers** | [**[String]**](String.md)| Optional: Invoice reference number. If not provided, returns invoices with any invoice reference number. | [optional] 
 **numbers** | [**[Number]**](Number.md)| Optional: Invoice number. If not provided, returns invoices with any invoice number. | [optional] 
 **changedSince** | **Date**| Optional: Get invoices that have been added or changed after this date time (greater or equal). | [optional] 
 **salesPersonGuids** | [**[String]**](String.md)| Optional: ID of the salesperson to get the invoices for. If not provided, returns for all sales persons. | [optional] 
 **createdByUserGuids** | [**[String]**](String.md)| Optional: ID of the user who created the invoice. If not provided, returns for all users. | [optional] 

### Return type

[**[InvoiceOutputModel]**](InvoiceOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectFeesGetInvoiceProjectFees

> [ProjectFeeOutputModel] projectFeesGetInvoiceProjectFees(invoiceGuid, opts)

Get all the project fees on an invoice

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesReadApi();
let invoiceGuid = "invoiceGuid_example"; // String | ID of the invoice.
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: Number of rows to fetch.
  'productType': new SeveraPublicRestApiDocumentation.ProductType() // ProductType | Optional: ProjectFee's product type. if given, it filters the projectFees by the given type. FixedFees (Own work), Materials (Products), Subcontracting
};
apiInstance.projectFeesGetInvoiceProjectFees(invoiceGuid, opts, (error, data, response) => {
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
 **invoiceGuid** | **String**| ID of the invoice. | 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: Number of rows to fetch. | [optional] 
 **productType** | [**ProductType**](.md)| Optional: ProjectFee&#39;s product type. if given, it filters the projectFees by the given type. FixedFees (Own work), Materials (Products), Subcontracting | [optional] 

### Return type

[**[ProjectFeeOutputModel]**](ProjectFeeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectFeesGetInvoiceRowProjectFees

> [ProjectFeeOutputModel] projectFeesGetInvoiceRowProjectFees(invoiceRowGuid, opts)

Get all the project fees on an invoice row

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesReadApi();
let invoiceRowGuid = "invoiceRowGuid_example"; // String | ID of the invoice row.
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: Number of rows to fetch.
  'productType': new SeveraPublicRestApiDocumentation.ProductType() // ProductType | Optional: ProjectFee's product type. if given, it filters the projectFees by the given type. FixedFees (Own work), Materials (Products), Subcontracting
};
apiInstance.projectFeesGetInvoiceRowProjectFees(invoiceRowGuid, opts, (error, data, response) => {
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
 **invoiceRowGuid** | **String**| ID of the invoice row. | 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: Number of rows to fetch. | [optional] 
 **productType** | [**ProductType**](.md)| Optional: ProjectFee&#39;s product type. if given, it filters the projectFees by the given type. FixedFees (Own work), Materials (Products), Subcontracting | [optional] 

### Return type

[**[ProjectFeeOutputModel]**](ProjectFeeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectFeesGetUninvoicedProjectFeesForInvoice

> [ProjectFeeOutputModel] projectFeesGetUninvoicedProjectFeesForInvoice(invoiceGuid, opts)

Get uninvoiced project fees available for invoice

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesReadApi();
let invoiceGuid = "invoiceGuid_example"; // String | ID of the invoice.
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: Number of rows to fetch.
  'isBillable': true // Boolean | Optional: Filter the project fees. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null.
};
apiInstance.projectFeesGetUninvoicedProjectFeesForInvoice(invoiceGuid, opts, (error, data, response) => {
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
 **invoiceGuid** | **String**| ID of the invoice. | 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: Number of rows to fetch. | [optional] 
 **isBillable** | **Boolean**| Optional: Filter the project fees. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null. | [optional] 

### Return type

[**[ProjectFeeOutputModel]**](ProjectFeeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectInvoiceSettingsGetProjectInvoiceSetting

> ProjectInvoiceSettingsOutputModel projectInvoiceSettingsGetProjectInvoiceSetting(guid)

Get project invoice settings by ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesReadApi();
let guid = "guid_example"; // String | ID of the project invoice settings.
apiInstance.projectInvoiceSettingsGetProjectInvoiceSetting(guid, (error, data, response) => {
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
 **guid** | **String**| ID of the project invoice settings. | 

### Return type

[**ProjectInvoiceSettingsOutputModel**](ProjectInvoiceSettingsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectInvoiceSettingsGetProjectInvoiceSettings

> [ProjectInvoiceSettingsOutputModel] projectInvoiceSettingsGetProjectInvoiceSettings(projectGuid)

Get project invoice settings by project ID.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesReadApi();
let projectGuid = "projectGuid_example"; // String | ID of the project.
apiInstance.projectInvoiceSettingsGetProjectInvoiceSettings(projectGuid, (error, data, response) => {
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
 **projectGuid** | **String**| ID of the project. | 

### Return type

[**[ProjectInvoiceSettingsOutputModel]**](ProjectInvoiceSettingsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectTravelExpensesGetInvoiceProjectTravelExpenses

> [ProjectTravelExpenseOutputModel] projectTravelExpensesGetInvoiceProjectTravelExpenses(invoiceGuid, opts)

Get all the project travel expenses on an invoice

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesReadApi();
let invoiceGuid = "invoiceGuid_example"; // String | ID of the invoice.
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'expenseClass': new SeveraPublicRestApiDocumentation.ExpensesClass() // ExpensesClass | Optional: Class of the expense. Mileage, DailyAllowance or OtherTravelExpense
};
apiInstance.projectTravelExpensesGetInvoiceProjectTravelExpenses(invoiceGuid, opts, (error, data, response) => {
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
 **invoiceGuid** | **String**| ID of the invoice. | 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **expenseClass** | [**ExpensesClass**](.md)| Optional: Class of the expense. Mileage, DailyAllowance or OtherTravelExpense | [optional] 

### Return type

[**[ProjectTravelExpenseOutputModel]**](ProjectTravelExpenseOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectTravelExpensesGetInvoiceRowProjectTravelExpenses

> [ProjectTravelExpenseOutputModel] projectTravelExpensesGetInvoiceRowProjectTravelExpenses(invoiceRowGuid, opts)

Get all the project travel expenses on an invoice row

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesReadApi();
let invoiceRowGuid = "invoiceRowGuid_example"; // String | ID of the invoice row.
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'expenseClass': new SeveraPublicRestApiDocumentation.ExpensesClass() // ExpensesClass | Optional: Class of the expense. Mileage, DailyAllowance or OtherTravelExpense
};
apiInstance.projectTravelExpensesGetInvoiceRowProjectTravelExpenses(invoiceRowGuid, opts, (error, data, response) => {
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
 **invoiceRowGuid** | **String**| ID of the invoice row. | 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **expenseClass** | [**ExpensesClass**](.md)| Optional: Class of the expense. Mileage, DailyAllowance or OtherTravelExpense | [optional] 

### Return type

[**[ProjectTravelExpenseOutputModel]**](ProjectTravelExpenseOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectTravelExpensesGetUninvoicedProjectTravelExpensesForInvoice

> [ProjectTravelExpenseOutputModel] projectTravelExpensesGetUninvoicedProjectTravelExpensesForInvoice(invoiceGuid, opts)

Get uninvoiced project travel expenses available for invoice

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesReadApi();
let invoiceGuid = "invoiceGuid_example"; // String | ID of the invoice.
let opts = {
  'isBillable': true, // Boolean | Optional: Filter the travel expenses. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null.
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'expenseClass': new SeveraPublicRestApiDocumentation.ExpensesClass() // ExpensesClass | Optional: Class of the expense. Mileage, DailyAllowance or OtherTravelExpense
};
apiInstance.projectTravelExpensesGetUninvoicedProjectTravelExpensesForInvoice(invoiceGuid, opts, (error, data, response) => {
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
 **invoiceGuid** | **String**| ID of the invoice. | 
 **isBillable** | **Boolean**| Optional: Filter the travel expenses. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null. | [optional] 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **expenseClass** | [**ExpensesClass**](.md)| Optional: Class of the expense. Mileage, DailyAllowance or OtherTravelExpense | [optional] 

### Return type

[**[ProjectTravelExpenseOutputModel]**](ProjectTravelExpenseOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reimbursedProjectFeesGetInvoiceReimbursedProjectFees

> [ReimbursedProjectFeeOutputModel] reimbursedProjectFeesGetInvoiceReimbursedProjectFees(invoiceGuid, opts)

Get all the project fees on an invoice

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesReadApi();
let invoiceGuid = "invoiceGuid_example"; // String | ID of the invoice.
let opts = {
  'rowCount': 56, // Number | Optional: Number of rows to fetch
  'pageToken': "pageToken_example" // String | Optional: page token to fetch the next page.
};
apiInstance.reimbursedProjectFeesGetInvoiceReimbursedProjectFees(invoiceGuid, opts, (error, data, response) => {
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
 **invoiceGuid** | **String**| ID of the invoice. | 
 **rowCount** | **Number**| Optional: Number of rows to fetch | [optional] 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 

### Return type

[**[ReimbursedProjectFeeOutputModel]**](ReimbursedProjectFeeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reimbursedProjectFeesGetInvoiceRowReimbursedProjectFees

> [ReimbursedProjectFeeOutputModel] reimbursedProjectFeesGetInvoiceRowReimbursedProjectFees(invoiceRowGuid, opts)

Get all the project fees on an invoice row

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesReadApi();
let invoiceRowGuid = "invoiceRowGuid_example"; // String | ID of the invoice row.
let opts = {
  'rowCount': 56, // Number | Optional: Number of rows to fetch
  'pageToken': "pageToken_example" // String | Optional: page token to fetch the next page.
};
apiInstance.reimbursedProjectFeesGetInvoiceRowReimbursedProjectFees(invoiceRowGuid, opts, (error, data, response) => {
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
 **invoiceRowGuid** | **String**| ID of the invoice row. | 
 **rowCount** | **Number**| Optional: Number of rows to fetch | [optional] 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 

### Return type

[**[ReimbursedProjectFeeOutputModel]**](ReimbursedProjectFeeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reimbursedProjectTravelExpensesGetInvoiceProjectTravelExpenses

> [ReimbursedProjectTravelExpenseOutputModel] reimbursedProjectTravelExpensesGetInvoiceProjectTravelExpenses(invoiceGuid, opts)

Get all the project travel expenses on an invoice.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesReadApi();
let invoiceGuid = "invoiceGuid_example"; // String | ID of the invoice.
let opts = {
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default all.
  'textToSearch': "''", // String | Searched string: part of name or description.
  'calculateRowCount': false, // Boolean | Optional. If true, calculates the total count of project fees. Default false.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()] // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=Name&sortings[0].value=Desc&sortings[1].key=Number&sortings[1].value=Asc\".
};
apiInstance.reimbursedProjectTravelExpensesGetInvoiceProjectTravelExpenses(invoiceGuid, opts, (error, data, response) => {
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
 **invoiceGuid** | **String**| ID of the invoice. | 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default all. | [optional] 
 **textToSearch** | **String**| Searched string: part of name or description. | [optional] [default to &#39;&#39;]
 **calculateRowCount** | **Boolean**| Optional. If true, calculates the total count of project fees. Default false. | [optional] [default to false]
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc&amp;sortings[1].key&#x3D;Number&amp;sortings[1].value&#x3D;Asc\&quot;. | [optional] 

### Return type

[**[ReimbursedProjectTravelExpenseOutputModel]**](ReimbursedProjectTravelExpenseOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reimbursedProjectTravelExpensesGetInvoiceRowProjectTravelExpenses

> [ReimbursedProjectTravelExpenseOutputModel] reimbursedProjectTravelExpensesGetInvoiceRowProjectTravelExpenses(invoiceRowGuid, opts)

Get all the project travel expenses on an invoice row.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesReadApi();
let invoiceRowGuid = "invoiceRowGuid_example"; // String | ID of the invoice row.
let opts = {
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default all.
  'textToSearch': "''", // String | Searched string: part of name or description.
  'calculateRowCount': false, // Boolean | Optional. If true, calculates the total count of project fees. Default false.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()] // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=Name&sortings[0].value=Desc&sortings[1].key=Number&sortings[1].value=Asc\".
};
apiInstance.reimbursedProjectTravelExpensesGetInvoiceRowProjectTravelExpenses(invoiceRowGuid, opts, (error, data, response) => {
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
 **invoiceRowGuid** | **String**| ID of the invoice row. | 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default all. | [optional] 
 **textToSearch** | **String**| Searched string: part of name or description. | [optional] [default to &#39;&#39;]
 **calculateRowCount** | **Boolean**| Optional. If true, calculates the total count of project fees. Default false. | [optional] [default to false]
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc&amp;sortings[1].key&#x3D;Number&amp;sortings[1].value&#x3D;Asc\&quot;. | [optional] 

### Return type

[**[ReimbursedProjectTravelExpenseOutputModel]**](ReimbursedProjectTravelExpenseOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reimbursedWorkHoursGetInvoiceReimbursedWorkHours

> [ReimbursedWorkHourOutputModel] reimbursedWorkHoursGetInvoiceReimbursedWorkHours(invoiceGuid, opts)

Get all reimbursed hours on an invoice.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesReadApi();
let invoiceGuid = "invoiceGuid_example"; // String | ID of the invoice.
let opts = {
  'firstRow': 56, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''", // String | Optional: Text to search from description or invoice description.
  'calculateRowCount': false, // Boolean | Optional: Calculate total number of rows.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()] // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=DueDate&sortings[0].value=Asc&sortings[1].key=TotalIncludingTax&sortings[1].value=Desc\".
};
apiInstance.reimbursedWorkHoursGetInvoiceReimbursedWorkHours(invoiceGuid, opts, (error, data, response) => {
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
 **invoiceGuid** | **String**| ID of the invoice. | 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from description or invoice description. | [optional] [default to &#39;&#39;]
 **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false]
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;DueDate&amp;sortings[0].value&#x3D;Asc&amp;sortings[1].key&#x3D;TotalIncludingTax&amp;sortings[1].value&#x3D;Desc\&quot;. | [optional] 

### Return type

[**[ReimbursedWorkHourOutputModel]**](ReimbursedWorkHourOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reimbursedWorkHoursGetInvoiceRowReimbursedWorkHours

> [ReimbursedWorkHourOutputModel] reimbursedWorkHoursGetInvoiceRowReimbursedWorkHours(invoiceRowGuid, opts)

Get all reimbursed hours on an invoice row.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesReadApi();
let invoiceRowGuid = "invoiceRowGuid_example"; // String | ID of the invoice row.
let opts = {
  'firstRow': 56, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''", // String | Optional: Text to search from description or invoice description.
  'calculateRowCount': false, // Boolean | Optional: Calculate total number of rows.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()] // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=DueDate&sortings[0].value=Asc&sortings[1].key=TotalIncludingTax&sortings[1].value=Desc\".
};
apiInstance.reimbursedWorkHoursGetInvoiceRowReimbursedWorkHours(invoiceRowGuid, opts, (error, data, response) => {
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
 **invoiceRowGuid** | **String**| ID of the invoice row. | 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from description or invoice description. | [optional] [default to &#39;&#39;]
 **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false]
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;DueDate&amp;sortings[0].value&#x3D;Asc&amp;sortings[1].key&#x3D;TotalIncludingTax&amp;sortings[1].value&#x3D;Desc\&quot;. | [optional] 

### Return type

[**[ReimbursedWorkHourOutputModel]**](ReimbursedWorkHourOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workHoursGetInvoiceRowWorkHours

> [WorkHourOutputModel] workHoursGetInvoiceRowWorkHours(invoiceRowGuid, opts)

Get all the work hours on an invoice row

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesReadApi();
let invoiceRowGuid = "invoiceRowGuid_example"; // String | ID of the invoice row.
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56 // Number | Optional: How many rows to fetch, Default 20, maximum 100.
};
apiInstance.workHoursGetInvoiceRowWorkHours(invoiceRowGuid, opts, (error, data, response) => {
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
 **invoiceRowGuid** | **String**| ID of the invoice row. | 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 

### Return type

[**[WorkHourOutputModel]**](WorkHourOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workHoursGetInvoiceWorkHours

> [WorkHourOutputModel] workHoursGetInvoiceWorkHours(invoiceGuid, opts)

Get all the work hours on an invoice

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesReadApi();
let invoiceGuid = "invoiceGuid_example"; // String | ID of the invoice.
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56 // Number | Optional: How many rows to fetch, Default 20, maximum 100.
};
apiInstance.workHoursGetInvoiceWorkHours(invoiceGuid, opts, (error, data, response) => {
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
 **invoiceGuid** | **String**| ID of the invoice. | 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 

### Return type

[**[WorkHourOutputModel]**](WorkHourOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workHoursGetUninvoicedWorkHoursForInvoice

> [WorkHourOutputModel] workHoursGetUninvoicedWorkHoursForInvoice(invoiceGuid, opts)

Get uninvoiced work hours available for invoice

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesReadApi();
let invoiceGuid = "invoiceGuid_example"; // String | ID of the invoice.
let opts = {
  'isBillable': true, // Boolean | Optional: Filter the work hours. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null.
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56 // Number | Optional: How many rows to fetch, Default 20, maximum 100.
};
apiInstance.workHoursGetUninvoicedWorkHoursForInvoice(invoiceGuid, opts, (error, data, response) => {
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
 **invoiceGuid** | **String**| ID of the invoice. | 
 **isBillable** | **Boolean**| Optional: Filter the work hours. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null. | [optional] 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 

### Return type

[**[WorkHourOutputModel]**](WorkHourOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

