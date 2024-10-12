# DoqsDevPdfFillingApi.DefaultApi

All URIs are relative to *https://api.doqs.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTemplateDesignerTemplatesPost**](DefaultApi.md#createTemplateDesignerTemplatesPost) | **POST** /designer/templates | Create Template
[**deleteDesignerTemplatesIdDelete**](DefaultApi.md#deleteDesignerTemplatesIdDelete) | **DELETE** /designer/templates/{id} | Delete
[**generatePdfDesignerTemplatesIdGeneratePost**](DefaultApi.md#generatePdfDesignerTemplatesIdGeneratePost) | **POST** /designer/templates/{id}/generate | Generate Pdf
[**listTemplatesDesignerTemplatesGet**](DefaultApi.md#listTemplatesDesignerTemplatesGet) | **GET** /designer/templates | List Templates
[**listTemplatesDesignerTemplatesIdGet**](DefaultApi.md#listTemplatesDesignerTemplatesIdGet) | **GET** /designer/templates/{id} | List Templates
[**previewDesignerTemplatesPreviewPost**](DefaultApi.md#previewDesignerTemplatesPreviewPost) | **POST** /designer/templates/preview | Preview
[**updateTemplateDesignerTemplatesIdPut**](DefaultApi.md#updateTemplateDesignerTemplatesIdPut) | **PUT** /designer/templates/{id} | Update Template



## createTemplateDesignerTemplatesPost

> ResponseOkDesignerTemplate createTemplateDesignerTemplatesPost(createOrUpdateTemplateRequest)

Create Template

### Example

```javascript
import DoqsDevPdfFillingApi from 'doqs_dev___pdf_filling_api';
let defaultClient = DoqsDevPdfFillingApi.ApiClient.instance;
// Configure API key authorization: apiKeyAuth
let apiKeyAuth = defaultClient.authentications['apiKeyAuth'];
apiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new DoqsDevPdfFillingApi.DefaultApi();
let createOrUpdateTemplateRequest = new DoqsDevPdfFillingApi.CreateOrUpdateTemplateRequest(); // CreateOrUpdateTemplateRequest | 
apiInstance.createTemplateDesignerTemplatesPost(createOrUpdateTemplateRequest, (error, data, response) => {
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
 **createOrUpdateTemplateRequest** | [**CreateOrUpdateTemplateRequest**](CreateOrUpdateTemplateRequest.md)|  | 

### Return type

[**ResponseOkDesignerTemplate**](ResponseOkDesignerTemplate.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteDesignerTemplatesIdDelete

> ResponseOkNoneType deleteDesignerTemplatesIdDelete(id)

Delete

### Example

```javascript
import DoqsDevPdfFillingApi from 'doqs_dev___pdf_filling_api';
let defaultClient = DoqsDevPdfFillingApi.ApiClient.instance;
// Configure API key authorization: apiKeyAuth
let apiKeyAuth = defaultClient.authentications['apiKeyAuth'];
apiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new DoqsDevPdfFillingApi.DefaultApi();
let id = "id_example"; // String | 
apiInstance.deleteDesignerTemplatesIdDelete(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**ResponseOkNoneType**](ResponseOkNoneType.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## generatePdfDesignerTemplatesIdGeneratePost

> Object generatePdfDesignerTemplatesIdGeneratePost(id, generatePDFPayload)

Generate Pdf

### Example

```javascript
import DoqsDevPdfFillingApi from 'doqs_dev___pdf_filling_api';
let defaultClient = DoqsDevPdfFillingApi.ApiClient.instance;
// Configure API key authorization: apiKeyAuth
let apiKeyAuth = defaultClient.authentications['apiKeyAuth'];
apiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new DoqsDevPdfFillingApi.DefaultApi();
let id = "id_example"; // String | 
let generatePDFPayload = new DoqsDevPdfFillingApi.GeneratePDFPayload(); // GeneratePDFPayload | 
apiInstance.generatePdfDesignerTemplatesIdGeneratePost(id, generatePDFPayload, (error, data, response) => {
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
 **id** | **String**|  | 
 **generatePDFPayload** | [**GeneratePDFPayload**](GeneratePDFPayload.md)|  | 

### Return type

**Object**

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTemplatesDesignerTemplatesGet

> ResponseOkListFillrEntitiesDesignerTemplateDesignerTemplate listTemplatesDesignerTemplatesGet(opts)

List Templates

### Example

```javascript
import DoqsDevPdfFillingApi from 'doqs_dev___pdf_filling_api';
let defaultClient = DoqsDevPdfFillingApi.ApiClient.instance;
// Configure API key authorization: apiKeyAuth
let apiKeyAuth = defaultClient.authentications['apiKeyAuth'];
apiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new DoqsDevPdfFillingApi.DefaultApi();
let opts = {
  'limit': 100, // Number | 
  'offset': 0 // Number | 
};
apiInstance.listTemplatesDesignerTemplatesGet(opts, (error, data, response) => {
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
 **limit** | **Number**|  | [optional] [default to 100]
 **offset** | **Number**|  | [optional] [default to 0]

### Return type

[**ResponseOkListFillrEntitiesDesignerTemplateDesignerTemplate**](ResponseOkListFillrEntitiesDesignerTemplateDesignerTemplate.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTemplatesDesignerTemplatesIdGet

> ResponseOkDesignerTemplate listTemplatesDesignerTemplatesIdGet(id)

List Templates

### Example

```javascript
import DoqsDevPdfFillingApi from 'doqs_dev___pdf_filling_api';
let defaultClient = DoqsDevPdfFillingApi.ApiClient.instance;
// Configure API key authorization: apiKeyAuth
let apiKeyAuth = defaultClient.authentications['apiKeyAuth'];
apiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new DoqsDevPdfFillingApi.DefaultApi();
let id = "id_example"; // String | 
apiInstance.listTemplatesDesignerTemplatesIdGet(id, (error, data, response) => {
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
 **id** | **String**|  | 

### Return type

[**ResponseOkDesignerTemplate**](ResponseOkDesignerTemplate.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## previewDesignerTemplatesPreviewPost

> ResponseOkPreviewResponse previewDesignerTemplatesPreviewPost(previewModel)

Preview

### Example

```javascript
import DoqsDevPdfFillingApi from 'doqs_dev___pdf_filling_api';
let defaultClient = DoqsDevPdfFillingApi.ApiClient.instance;
// Configure API key authorization: apiKeyAuth
let apiKeyAuth = defaultClient.authentications['apiKeyAuth'];
apiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new DoqsDevPdfFillingApi.DefaultApi();
let previewModel = new DoqsDevPdfFillingApi.PreviewModel(); // PreviewModel | 
apiInstance.previewDesignerTemplatesPreviewPost(previewModel, (error, data, response) => {
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
 **previewModel** | [**PreviewModel**](PreviewModel.md)|  | 

### Return type

[**ResponseOkPreviewResponse**](ResponseOkPreviewResponse.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateTemplateDesignerTemplatesIdPut

> ResponseOkDesignerTemplate updateTemplateDesignerTemplatesIdPut(id, createOrUpdateTemplateRequest)

Update Template

### Example

```javascript
import DoqsDevPdfFillingApi from 'doqs_dev___pdf_filling_api';
let defaultClient = DoqsDevPdfFillingApi.ApiClient.instance;
// Configure API key authorization: apiKeyAuth
let apiKeyAuth = defaultClient.authentications['apiKeyAuth'];
apiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new DoqsDevPdfFillingApi.DefaultApi();
let id = "id_example"; // String | 
let createOrUpdateTemplateRequest = new DoqsDevPdfFillingApi.CreateOrUpdateTemplateRequest(); // CreateOrUpdateTemplateRequest | 
apiInstance.updateTemplateDesignerTemplatesIdPut(id, createOrUpdateTemplateRequest, (error, data, response) => {
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
 **id** | **String**|  | 
 **createOrUpdateTemplateRequest** | [**CreateOrUpdateTemplateRequest**](CreateOrUpdateTemplateRequest.md)|  | 

### Return type

[**ResponseOkDesignerTemplate**](ResponseOkDesignerTemplate.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

