# SeveraPublicRestApiDocumentation.FilesReadApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fileDataGetDataForFile**](FilesReadApi.md#fileDataGetDataForFile) | **GET** /v1/files/{guid}/filedata | Get file data by ID.
[**filesGetFile**](FilesReadApi.md#filesGetFile) | **GET** /v1/files/{guid} | Get file by ID.
[**filesGetInvoiceFile**](FilesReadApi.md#filesGetInvoiceFile) | **GET** /v1/invoicefiles/{guid} | Get invoice file by ID.
[**filesGetInvoiceFiles**](FilesReadApi.md#filesGetInvoiceFiles) | **GET** /v1/invoices/{invoiceGuid}/files | Get all files of a invoice by its id.
[**filesGetProjectFile**](FilesReadApi.md#filesGetProjectFile) | **GET** /v1/projectfiles/{guid} | Get project file by ID.
[**filesGetProjectFiles**](FilesReadApi.md#filesGetProjectFiles) | **GET** /v1/projects/{projectGuid}/files | Get all files of a project by its id.
[**filesGetTravelExpenseFile**](FilesReadApi.md#filesGetTravelExpenseFile) | **GET** /v1/projecttravelexpensefiles/{guid} | Get travel expense file by ID.
[**filesGetTravelExpenseFiles**](FilesReadApi.md#filesGetTravelExpenseFiles) | **GET** /v1/projecttravelexpenses/{projectTravelExpenseGuid}/files | Get all files of a travel expense by its id.
[**filesGetUsersTravelExpensesFiles**](FilesReadApi.md#filesGetUsersTravelExpensesFiles) | **GET** /v1/users/{userGuid}/travelexpensesfiles | Get all files of all travel expenses of the user.
[**keywordsGetFileKeywords**](FilesReadApi.md#keywordsGetFileKeywords) | **GET** /v1/files/{fileGuid}/keywords | Get all the keywords for file.
[**pdfGetInvoicePdf**](FilesReadApi.md#pdfGetInvoicePdf) | **GET** /v1/invoices/{guid}/pdf | Get an invoice PDF.
[**pdfGetTravelReimbursementPdf**](FilesReadApi.md#pdfGetTravelReimbursementPdf) | **GET** /v1/travelreimbursements/{guid}/pdf | Get a travel reimbursement PDF.



## fileDataGetDataForFile

> File fileDataGetDataForFile(guid)

Get file data by ID.

Returns binary data, which contains content with type given in Content-Type header.

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

let apiInstance = new SeveraPublicRestApiDocumentation.FilesReadApi();
let guid = "guid_example"; // String | GUID used to get the file.
apiInstance.fileDataGetDataForFile(guid, (error, data, response) => {
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
 **guid** | **String**| GUID used to get the file. | 

### Return type

**File**

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json


## filesGetFile

> FileModel filesGetFile(guid, opts)

Get file by ID.

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

let apiInstance = new SeveraPublicRestApiDocumentation.FilesReadApi();
let guid = "guid_example"; // String | GUID used to get the file.
let opts = {
  'includeDataInResponse': false // Boolean | Is data included in response as base64 string.
};
apiInstance.filesGetFile(guid, opts, (error, data, response) => {
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
 **guid** | **String**| GUID used to get the file. | 
 **includeDataInResponse** | **Boolean**| Is data included in response as base64 string. | [optional] [default to false]

### Return type

[**FileModel**](FileModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## filesGetInvoiceFile

> InvoiceFileModel filesGetInvoiceFile(guid)

Get invoice file by ID.

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

let apiInstance = new SeveraPublicRestApiDocumentation.FilesReadApi();
let guid = "guid_example"; // String | GUID used to get the invoice file.
apiInstance.filesGetInvoiceFile(guid, (error, data, response) => {
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
 **guid** | **String**| GUID used to get the invoice file. | 

### Return type

[**InvoiceFileModel**](InvoiceFileModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## filesGetInvoiceFiles

> [InvoiceFileModel] filesGetInvoiceFiles(invoiceGuid, opts)

Get all files of a invoice by its id.

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

let apiInstance = new SeveraPublicRestApiDocumentation.FilesReadApi();
let invoiceGuid = "invoiceGuid_example"; // String | GUID of the invoice used to get the files.
let opts = {
  'firstRow': 56, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56 // Number | Optional: How many rows to fetch.
};
apiInstance.filesGetInvoiceFiles(invoiceGuid, opts, (error, data, response) => {
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
 **invoiceGuid** | **String**| GUID of the invoice used to get the files. | 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch. | [optional] 

### Return type

[**[InvoiceFileModel]**](InvoiceFileModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## filesGetProjectFile

> ProjectFileModel filesGetProjectFile(guid)

Get project file by ID.

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

let apiInstance = new SeveraPublicRestApiDocumentation.FilesReadApi();
let guid = "guid_example"; // String | GUID used to get the project file.
apiInstance.filesGetProjectFile(guid, (error, data, response) => {
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
 **guid** | **String**| GUID used to get the project file. | 

### Return type

[**ProjectFileModel**](ProjectFileModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## filesGetProjectFiles

> [ProjectFileModel] filesGetProjectFiles(projectGuid, opts)

Get all files of a project by its id.

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

let apiInstance = new SeveraPublicRestApiDocumentation.FilesReadApi();
let projectGuid = "projectGuid_example"; // String | GUID of the project used to get the files.
let opts = {
  'firstRow': 56, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()] // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=Name&sortings[0].value=Desc&sortings[1].key=Number&sortings[1].value=Asc\".
};
apiInstance.filesGetProjectFiles(projectGuid, opts, (error, data, response) => {
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
 **projectGuid** | **String**| GUID of the project used to get the files. | 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch. | [optional] 
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc&amp;sortings[1].key&#x3D;Number&amp;sortings[1].value&#x3D;Asc\&quot;. | [optional] 

### Return type

[**[ProjectFileModel]**](ProjectFileModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## filesGetTravelExpenseFile

> ProjectTravelExpenseFileModel filesGetTravelExpenseFile(guid)

Get travel expense file by ID.

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

let apiInstance = new SeveraPublicRestApiDocumentation.FilesReadApi();
let guid = "guid_example"; // String | GUID used to get the travel expense file.
apiInstance.filesGetTravelExpenseFile(guid, (error, data, response) => {
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
 **guid** | **String**| GUID used to get the travel expense file. | 

### Return type

[**ProjectTravelExpenseFileModel**](ProjectTravelExpenseFileModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## filesGetTravelExpenseFiles

> [ProjectTravelExpenseFileModel] filesGetTravelExpenseFiles(projectTravelExpenseGuid, opts)

Get all files of a travel expense by its id.

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

let apiInstance = new SeveraPublicRestApiDocumentation.FilesReadApi();
let projectTravelExpenseGuid = "projectTravelExpenseGuid_example"; // String | GUID of the travel expense used to get the files.
let opts = {
  'firstRow': 56, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56 // Number | Optional: How many rows to fetch.
};
apiInstance.filesGetTravelExpenseFiles(projectTravelExpenseGuid, opts, (error, data, response) => {
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
 **projectTravelExpenseGuid** | **String**| GUID of the travel expense used to get the files. | 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch. | [optional] 

### Return type

[**[ProjectTravelExpenseFileModel]**](ProjectTravelExpenseFileModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## filesGetUsersTravelExpensesFiles

> [ProjectTravelExpenseFileModel] filesGetUsersTravelExpensesFiles(userGuid, opts)

Get all files of all travel expenses of the user.

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

let apiInstance = new SeveraPublicRestApiDocumentation.FilesReadApi();
let userGuid = "userGuid_example"; // String | GUID of the user used to get the files attached to travel expenses.
let opts = {
  'firstRow': 56, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch.
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: Start date to from which to check travel expenses.
  'endDate': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: End date to check for availability until travel expenses.
};
apiInstance.filesGetUsersTravelExpensesFiles(userGuid, opts, (error, data, response) => {
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
 **userGuid** | **String**| GUID of the user used to get the files attached to travel expenses. | 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch. | [optional] 
 **startDate** | **Date**| Optional: Start date to from which to check travel expenses. | [optional] 
 **endDate** | **Date**| Optional: End date to check for availability until travel expenses. | [optional] 

### Return type

[**[ProjectTravelExpenseFileModel]**](ProjectTravelExpenseFileModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## keywordsGetFileKeywords

> [FileKeywordModel] keywordsGetFileKeywords(fileGuid, opts)

Get all the keywords for file.

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

let apiInstance = new SeveraPublicRestApiDocumentation.FilesReadApi();
let fileGuid = "fileGuid_example"; // String | ID of the file for which keywords are requested.
let opts = {
  'active': true, // Boolean | If not given, return all Keywords, if given as true return only active Keywords, if given as false returns only inactive Keywords.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()] // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=Keyword&sortings[0].value=Desc\".
};
apiInstance.keywordsGetFileKeywords(fileGuid, opts, (error, data, response) => {
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
 **fileGuid** | **String**| ID of the file for which keywords are requested. | 
 **active** | **Boolean**| If not given, return all Keywords, if given as true return only active Keywords, if given as false returns only inactive Keywords. | [optional] 
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Keyword&amp;sortings[0].value&#x3D;Desc\&quot;. | [optional] 

### Return type

[**[FileKeywordModel]**](FileKeywordModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pdfGetInvoicePdf

> File pdfGetInvoicePdf(guid, opts)

Get an invoice PDF.

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

let apiInstance = new SeveraPublicRestApiDocumentation.FilesReadApi();
let guid = "guid_example"; // String | The invoice GUID.
let opts = {
  'invoiceType': new SeveraPublicRestApiDocumentation.InvoiceType(), // InvoiceType | Optional: type of invoice.
  'pdfGetOptions': new SeveraPublicRestApiDocumentation.InvoicePdfGetOptions() // InvoicePdfGetOptions | Optional: what to include in the PDF. Defaults to InvoicePdfGetOptions.All.
};
apiInstance.pdfGetInvoicePdf(guid, opts, (error, data, response) => {
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
 **guid** | **String**| The invoice GUID. | 
 **invoiceType** | [**InvoiceType**](.md)| Optional: type of invoice. | [optional] 
 **pdfGetOptions** | [**InvoicePdfGetOptions**](.md)| Optional: what to include in the PDF. Defaults to InvoicePdfGetOptions.All. | [optional] 

### Return type

**File**

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/pdf, application/json


## pdfGetTravelReimbursementPdf

> File pdfGetTravelReimbursementPdf(guid)

Get a travel reimbursement PDF.

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

let apiInstance = new SeveraPublicRestApiDocumentation.FilesReadApi();
let guid = "guid_example"; // String | The travel reimbursement GUID.
apiInstance.pdfGetTravelReimbursementPdf(guid, (error, data, response) => {
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
 **guid** | **String**| The travel reimbursement GUID. | 

### Return type

**File**

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/pdf, application/json

