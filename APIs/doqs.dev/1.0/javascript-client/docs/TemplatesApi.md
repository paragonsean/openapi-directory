# DoqsDevPdfFillingApi.TemplatesApi

All URIs are relative to *https://api.doqs.dev/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](TemplatesApi.md#create) | **POST** /templates | Create
[**deleteTemplatesIdDelete**](TemplatesApi.md#deleteTemplatesIdDelete) | **DELETE** /templates/{id} | Delete 
[**fill**](TemplatesApi.md#fill) | **POST** /templates/{id}/fill | Fill
[**get**](TemplatesApi.md#get) | **GET** /templates/{id} | Get Template
[**getFileTemplatesIdFileGet**](TemplatesApi.md#getFileTemplatesIdFileGet) | **GET** /templates/{id}/file | Get File
[**list**](TemplatesApi.md#list) | **GET** /templates | List 
[**update**](TemplatesApi.md#update) | **PUT** /templates/{id} | Update



## create

> ResponseOkTemplate create(file)

Create

### Example

```javascript
import DoqsDevPdfFillingApi from 'doqs_dev___pdf_filling_api';
let defaultClient = DoqsDevPdfFillingApi.ApiClient.instance;
// Configure API key authorization: apiKeyAuth
let apiKeyAuth = defaultClient.authentications['apiKeyAuth'];
apiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new DoqsDevPdfFillingApi.TemplatesApi();
let file = "/path/to/file"; // File | 
apiInstance.create(file, (error, data, response) => {
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
 **file** | **File**|  | 

### Return type

[**ResponseOkTemplate**](ResponseOkTemplate.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## deleteTemplatesIdDelete

> ResponseOkNoneType deleteTemplatesIdDelete(id)

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

let apiInstance = new DoqsDevPdfFillingApi.TemplatesApi();
let id = "id_example"; // String | 
apiInstance.deleteTemplatesIdDelete(id, (error, data, response) => {
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


## fill

> Object fill(id, fillTemplateRequest)

Fill

### Example

```javascript
import DoqsDevPdfFillingApi from 'doqs_dev___pdf_filling_api';
let defaultClient = DoqsDevPdfFillingApi.ApiClient.instance;
// Configure API key authorization: apiKeyAuth
let apiKeyAuth = defaultClient.authentications['apiKeyAuth'];
apiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new DoqsDevPdfFillingApi.TemplatesApi();
let id = "id_example"; // String | 
let fillTemplateRequest = new DoqsDevPdfFillingApi.FillTemplateRequest(); // FillTemplateRequest | 
apiInstance.fill(id, fillTemplateRequest, (error, data, response) => {
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
 **fillTemplateRequest** | [**FillTemplateRequest**](FillTemplateRequest.md)|  | 

### Return type

**Object**

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## get

> ResponseOkTemplate get(id)

Get Template

### Example

```javascript
import DoqsDevPdfFillingApi from 'doqs_dev___pdf_filling_api';
let defaultClient = DoqsDevPdfFillingApi.ApiClient.instance;
// Configure API key authorization: apiKeyAuth
let apiKeyAuth = defaultClient.authentications['apiKeyAuth'];
apiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new DoqsDevPdfFillingApi.TemplatesApi();
let id = "id_example"; // String | 
apiInstance.get(id, (error, data, response) => {
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

[**ResponseOkTemplate**](ResponseOkTemplate.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFileTemplatesIdFileGet

> ResponseOkHttpUrl getFileTemplatesIdFileGet(id)

Get File

### Example

```javascript
import DoqsDevPdfFillingApi from 'doqs_dev___pdf_filling_api';
let defaultClient = DoqsDevPdfFillingApi.ApiClient.instance;
// Configure API key authorization: apiKeyAuth
let apiKeyAuth = defaultClient.authentications['apiKeyAuth'];
apiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new DoqsDevPdfFillingApi.TemplatesApi();
let id = "id_example"; // String | 
apiInstance.getFileTemplatesIdFileGet(id, (error, data, response) => {
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

[**ResponseOkHttpUrl**](ResponseOkHttpUrl.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## list

> ResponseOkListAppsApiRoutesTemplatesTemplate list(opts)

List 

### Example

```javascript
import DoqsDevPdfFillingApi from 'doqs_dev___pdf_filling_api';
let defaultClient = DoqsDevPdfFillingApi.ApiClient.instance;
// Configure API key authorization: apiKeyAuth
let apiKeyAuth = defaultClient.authentications['apiKeyAuth'];
apiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new DoqsDevPdfFillingApi.TemplatesApi();
let opts = {
  'limit': 100, // Number | 
  'offset': 0 // Number | 
};
apiInstance.list(opts, (error, data, response) => {
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

[**ResponseOkListAppsApiRoutesTemplatesTemplate**](ResponseOkListAppsApiRoutesTemplatesTemplate.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## update

> ResponseOkTemplate update(id, updateTemplateRequest)

Update

### Example

```javascript
import DoqsDevPdfFillingApi from 'doqs_dev___pdf_filling_api';
let defaultClient = DoqsDevPdfFillingApi.ApiClient.instance;
// Configure API key authorization: apiKeyAuth
let apiKeyAuth = defaultClient.authentications['apiKeyAuth'];
apiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new DoqsDevPdfFillingApi.TemplatesApi();
let id = "id_example"; // String | 
let updateTemplateRequest = new DoqsDevPdfFillingApi.UpdateTemplateRequest(); // UpdateTemplateRequest | 
apiInstance.update(id, updateTemplateRequest, (error, data, response) => {
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
 **updateTemplateRequest** | [**UpdateTemplateRequest**](UpdateTemplateRequest.md)|  | 

### Return type

[**ResponseOkTemplate**](ResponseOkTemplate.md)

### Authorization

[apiKeyAuth](../README.md#apiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

