# SeveraPublicRestApiDocumentation.InvoicesDeleteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoiceRowsDeleteInvoiceRow**](InvoicesDeleteApi.md#invoiceRowsDeleteInvoiceRow) | **DELETE** /v1/invoicerows/{guid} | Deletes an invoice row
[**invoicesDeleteInvoice**](InvoicesDeleteApi.md#invoicesDeleteInvoice) | **DELETE** /v1/invoices/{guid} | Delete an invoice.
[**invoicesDeleteProjectFromInvoice**](InvoicesDeleteApi.md#invoicesDeleteProjectFromInvoice) | **DELETE** /v1/invoices/{guid}/projects/{projectGuid} | Delete a project from invoice.
[**projectInvoiceSettingsDeleteProjectInvoiceSettings**](InvoicesDeleteApi.md#projectInvoiceSettingsDeleteProjectInvoiceSettings) | **DELETE** /v1/projectinvoicesettings/{guid} | Delete an project invoice settings.



## invoiceRowsDeleteInvoiceRow

> invoiceRowsDeleteInvoiceRow(guid, opts)

Deletes an invoice row

Returns: No Content (204) if succeeded.

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

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesDeleteApi();
let guid = "guid_example"; // String | GUID used to delete the invoice row.
let opts = {
  'setAsNonBillable': false // Boolean | 
};
apiInstance.invoiceRowsDeleteInvoiceRow(guid, opts, (error, data, response) => {
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
 **guid** | **String**| GUID used to delete the invoice row. | 
 **setAsNonBillable** | **Boolean**|  | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoicesDeleteInvoice

> invoicesDeleteInvoice(guid)

Delete an invoice.

Returns: No Content (204) if succeeded. Not found (404) if cost center can&#39;t be found.

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

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesDeleteApi();
let guid = "guid_example"; // String | ID for the invoice to delete.
apiInstance.invoicesDeleteInvoice(guid, (error, data, response) => {
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
 **guid** | **String**| ID for the invoice to delete. | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invoicesDeleteProjectFromInvoice

> invoicesDeleteProjectFromInvoice(guid, projectGuid)

Delete a project from invoice.

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

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesDeleteApi();
let guid = "guid_example"; // String | The invoice GUID.
let projectGuid = "projectGuid_example"; // String | The project GUID.
apiInstance.invoicesDeleteProjectFromInvoice(guid, projectGuid, (error, data, response) => {
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
 **guid** | **String**| The invoice GUID. | 
 **projectGuid** | **String**| The project GUID. | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectInvoiceSettingsDeleteProjectInvoiceSettings

> projectInvoiceSettingsDeleteProjectInvoiceSettings(guid)

Delete an project invoice settings.

Returns: No Content (204) if succeeded. Not found (404) if project invoice settings can&#39;t be found.

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

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesDeleteApi();
let guid = "guid_example"; // String | ID for the project invoice settings to delete.
apiInstance.projectInvoiceSettingsDeleteProjectInvoiceSettings(guid, (error, data, response) => {
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
 **guid** | **String**| ID for the project invoice settings to delete. | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

