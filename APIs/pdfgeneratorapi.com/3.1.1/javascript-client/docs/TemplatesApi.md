# PdfGeneratorApi.TemplatesApi

All URIs are relative to *https://us1.pdfgeneratorapi.com/api/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copyTemplate**](TemplatesApi.md#copyTemplate) | **POST** /templates/templateId/copy | Copy template
[**createTemplate**](TemplatesApi.md#createTemplate) | **POST** /templates | Create template
[**deleteTemplate**](TemplatesApi.md#deleteTemplate) | **DELETE** /templates/templateId | Delete template
[**getEditorUrl**](TemplatesApi.md#getEditorUrl) | **POST** /templates/templateId/editor | Open editor
[**getTemplate**](TemplatesApi.md#getTemplate) | **GET** /templates/templateId | Get template
[**getTemplates**](TemplatesApi.md#getTemplates) | **GET** /templates | Get templates
[**updateTemplate**](TemplatesApi.md#updateTemplate) | **PUT** /templates/templateId | Update template



## copyTemplate

> CreateTemplate200Response copyTemplate(templateId, opts)

Copy template

Creates a copy of a template to the workspace specified in authentication parameters.

### Example

```javascript
import PdfGeneratorApi from 'pdf_generator_api';
let defaultClient = PdfGeneratorApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: JSONWebTokenAuth
let JSONWebTokenAuth = defaultClient.authentications['JSONWebTokenAuth'];
JSONWebTokenAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new PdfGeneratorApi.TemplatesApi();
let templateId = 19375; // Number | Template unique identifier
let opts = {
  'name': "My copied template" // String | Name for the copied template. If name is not specified then the original name is used.
};
apiInstance.copyTemplate(templateId, opts, (error, data, response) => {
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
 **templateId** | **Number**| Template unique identifier | 
 **name** | **String**| Name for the copied template. If name is not specified then the original name is used. | [optional] 

### Return type

[**CreateTemplate200Response**](CreateTemplate200Response.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createTemplate

> CreateTemplate200Response createTemplate(templateDefinitionNew)

Create template

Creates a new template. If template configuration is not specified in the request body then an empty template is created. Template is placed to the workspace specified in authentication params. Template configuration must be sent in the request body.

### Example

```javascript
import PdfGeneratorApi from 'pdf_generator_api';
let defaultClient = PdfGeneratorApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: JSONWebTokenAuth
let JSONWebTokenAuth = defaultClient.authentications['JSONWebTokenAuth'];
JSONWebTokenAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new PdfGeneratorApi.TemplatesApi();
let templateDefinitionNew = new PdfGeneratorApi.TemplateDefinitionNew(); // TemplateDefinitionNew | Template configuration as JSON string
apiInstance.createTemplate(templateDefinitionNew, (error, data, response) => {
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
 **templateDefinitionNew** | [**TemplateDefinitionNew**](TemplateDefinitionNew.md)| Template configuration as JSON string | 

### Return type

[**CreateTemplate200Response**](CreateTemplate200Response.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteTemplate

> DeleteTemplate200Response deleteTemplate(templateId)

Delete template

Deletes the template from workspace

### Example

```javascript
import PdfGeneratorApi from 'pdf_generator_api';
let defaultClient = PdfGeneratorApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: JSONWebTokenAuth
let JSONWebTokenAuth = defaultClient.authentications['JSONWebTokenAuth'];
JSONWebTokenAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new PdfGeneratorApi.TemplatesApi();
let templateId = 19375; // Number | Template unique identifier
apiInstance.deleteTemplate(templateId, (error, data, response) => {
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
 **templateId** | **Number**| Template unique identifier | 

### Return type

[**DeleteTemplate200Response**](DeleteTemplate200Response.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEditorUrl

> GetEditorUrl200Response getEditorUrl(templateId, body, opts)

Open editor

Returns an unique URL which you can use to redirect your user to the editor from your application or use the generated URL as iframe source to show the editor within your application. 

### Example

```javascript
import PdfGeneratorApi from 'pdf_generator_api';
let defaultClient = PdfGeneratorApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: JSONWebTokenAuth
let JSONWebTokenAuth = defaultClient.authentications['JSONWebTokenAuth'];
JSONWebTokenAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new PdfGeneratorApi.TemplatesApi();
let templateId = 19375; // Number | Template unique identifier
let body = {key: null}; // Object | Data used to generate the PDF. This can be JSON encoded string or a public URL to your JSON file.
let opts = {
  'language': "en" // String | Specify the editor UI language. Defaults to organization editor language.
};
apiInstance.getEditorUrl(templateId, body, opts, (error, data, response) => {
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
 **templateId** | **Number**| Template unique identifier | 
 **body** | **Object**| Data used to generate the PDF. This can be JSON encoded string or a public URL to your JSON file. | 
 **language** | **String**| Specify the editor UI language. Defaults to organization editor language. | [optional] 

### Return type

[**GetEditorUrl200Response**](GetEditorUrl200Response.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getTemplate

> CreateTemplate200Response getTemplate(templateId)

Get template

Returns template configuration

### Example

```javascript
import PdfGeneratorApi from 'pdf_generator_api';
let defaultClient = PdfGeneratorApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: JSONWebTokenAuth
let JSONWebTokenAuth = defaultClient.authentications['JSONWebTokenAuth'];
JSONWebTokenAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new PdfGeneratorApi.TemplatesApi();
let templateId = 19375; // Number | Template unique identifier
apiInstance.getTemplate(templateId, (error, data, response) => {
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
 **templateId** | **Number**| Template unique identifier | 

### Return type

[**CreateTemplate200Response**](CreateTemplate200Response.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTemplates

> GetTemplates200Response getTemplates()

Get templates

Returns a list of templates available for the authenticated workspace

### Example

```javascript
import PdfGeneratorApi from 'pdf_generator_api';
let defaultClient = PdfGeneratorApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: JSONWebTokenAuth
let JSONWebTokenAuth = defaultClient.authentications['JSONWebTokenAuth'];
JSONWebTokenAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new PdfGeneratorApi.TemplatesApi();
apiInstance.getTemplates((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetTemplates200Response**](GetTemplates200Response.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateTemplate

> CreateTemplate200Response updateTemplate(templateId, templateDefinitionNew)

Update template

Updates template configuration. The template configuration for pages and layout must be complete as the entire configuration is replaced and not merged.

### Example

```javascript
import PdfGeneratorApi from 'pdf_generator_api';
let defaultClient = PdfGeneratorApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: JSONWebTokenAuth
let JSONWebTokenAuth = defaultClient.authentications['JSONWebTokenAuth'];
JSONWebTokenAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new PdfGeneratorApi.TemplatesApi();
let templateId = 19375; // Number | Template unique identifier
let templateDefinitionNew = new PdfGeneratorApi.TemplateDefinitionNew(); // TemplateDefinitionNew | Template configuration as JSON string
apiInstance.updateTemplate(templateId, templateDefinitionNew, (error, data, response) => {
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
 **templateId** | **Number**| Template unique identifier | 
 **templateDefinitionNew** | [**TemplateDefinitionNew**](TemplateDefinitionNew.md)| Template configuration as JSON string | 

### Return type

[**CreateTemplate200Response**](CreateTemplate200Response.md)

### Authorization

[JSONWebTokenAuth](../README.md#JSONWebTokenAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

