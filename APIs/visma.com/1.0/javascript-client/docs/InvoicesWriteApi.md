# SeveraPublicRestApiDocumentation.InvoicesWriteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoiceRowsPatchInvoiceRow**](InvoicesWriteApi.md#invoiceRowsPatchInvoiceRow) | **PATCH** /v1/invoicerows/{guid} | Update (Patch) a invoice row or a part of it
[**invoiceSettingsPatchInvoiceSettings**](InvoicesWriteApi.md#invoiceSettingsPatchInvoiceSettings) | **PATCH** /v1/invoicesettings/{guid} | Update (Patch) invoice setting
[**invoicesPatchInvoice**](InvoicesWriteApi.md#invoicesPatchInvoice) | **PATCH** /v1/invoices/{guid} | Update (Patch) an invoice or a part of it
[**invoicesPostInvoiceCreation**](InvoicesWriteApi.md#invoicesPostInvoiceCreation) | **POST** /v1/invoices | Add an invoice to project(s)
[**projectInvoiceSettingsPatchProjectInvoiceSettings**](InvoicesWriteApi.md#projectInvoiceSettingsPatchProjectInvoiceSettings) | **PATCH** /v1/projectinvoicesettings/{guid} | Update (Patch) project invoice settings.
[**projectInvoiceSettingsPostProjectInvoiceSettings**](InvoicesWriteApi.md#projectInvoiceSettingsPostProjectInvoiceSettings) | **POST** /v1/projectinvoicesettings | Create a new project invoice settings.



## invoiceRowsPatchInvoiceRow

> [InvoiceRowOutputModel] invoiceRowsPatchInvoiceRow(guid, opts)

Update (Patch) a invoice row or a part of it

If CostCenterNumber, SalesAccountNumber or RecurringSalesAccountNumber are changed and the invoice row is related to one or many ProjectFees or ProjectTravelExpenses, the values for those will also be updated.

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

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesWriteApi();
let guid = "guid_example"; // String | ID of the invoice row
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON Patch document of InvoiceRowModel
};
apiInstance.invoiceRowsPatchInvoiceRow(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the invoice row | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON Patch document of InvoiceRowModel | [optional] 

### Return type

[**[InvoiceRowOutputModel]**](InvoiceRowOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## invoiceSettingsPatchInvoiceSettings

> InvoiceSettingsOutputModel invoiceSettingsPatchInvoiceSettings(guid, opts)

Update (Patch) invoice setting

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

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesWriteApi();
let guid = "guid_example"; // String | ID of the invoice settings
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON patch document of InvoiceSettingsModel
};
apiInstance.invoiceSettingsPatchInvoiceSettings(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the invoice settings | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON patch document of InvoiceSettingsModel | [optional] 

### Return type

[**InvoiceSettingsOutputModel**](InvoiceSettingsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## invoicesPatchInvoice

> [InvoiceOutputModel] invoicesPatchInvoice(guid, opts)

Update (Patch) an invoice or a part of it

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

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesWriteApi();
let guid = "guid_example"; // String | GUID of the invoice
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON patch document of InvoiceInputModel
};
apiInstance.invoicesPatchInvoice(guid, opts, (error, data, response) => {
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
 **guid** | **String**| GUID of the invoice | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON patch document of InvoiceInputModel | [optional] 

### Return type

[**[InvoiceOutputModel]**](InvoiceOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## invoicesPostInvoiceCreation

> [InvoiceOutputModel] invoicesPostInvoiceCreation(opts)

Add an invoice to project(s)

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

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesWriteApi();
let opts = {
  'createInvoiceModel': new SeveraPublicRestApiDocumentation.CreateInvoiceModel() // CreateInvoiceModel | CreateInvoiceModel
};
apiInstance.invoicesPostInvoiceCreation(opts, (error, data, response) => {
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
 **createInvoiceModel** | [**CreateInvoiceModel**](CreateInvoiceModel.md)| CreateInvoiceModel | [optional] 

### Return type

[**[InvoiceOutputModel]**](InvoiceOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectInvoiceSettingsPatchProjectInvoiceSettings

> [ProjectInvoiceSettingsOutputModel] projectInvoiceSettingsPatchProjectInvoiceSettings(guid, opts)

Update (Patch) project invoice settings.

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

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesWriteApi();
let guid = "guid_example"; // String | ID of the project invoice settings.
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON patch document of ProjectInvoiceSettingsInputModel.
};
apiInstance.projectInvoiceSettingsPatchProjectInvoiceSettings(guid, opts, (error, data, response) => {
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
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON patch document of ProjectInvoiceSettingsInputModel. | [optional] 

### Return type

[**[ProjectInvoiceSettingsOutputModel]**](ProjectInvoiceSettingsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectInvoiceSettingsPostProjectInvoiceSettings

> ProjectInvoiceSettingsOutputModel projectInvoiceSettingsPostProjectInvoiceSettings(opts)

Create a new project invoice settings.

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

let apiInstance = new SeveraPublicRestApiDocumentation.InvoicesWriteApi();
let opts = {
  'projectInvoiceSettingsInputModel': new SeveraPublicRestApiDocumentation.ProjectInvoiceSettingsInputModel() // ProjectInvoiceSettingsInputModel | Project invoice settings.
};
apiInstance.projectInvoiceSettingsPostProjectInvoiceSettings(opts, (error, data, response) => {
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
 **projectInvoiceSettingsInputModel** | [**ProjectInvoiceSettingsInputModel**](ProjectInvoiceSettingsInputModel.md)| Project invoice settings. | [optional] 

### Return type

[**ProjectInvoiceSettingsOutputModel**](ProjectInvoiceSettingsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

