# CarboneApi.TemplateApi

All URIs are relative to *https://api.carbone.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**templatePost**](TemplateApi.md#templatePost) | **POST** /template | Upload a template.
[**templateTemplateIdDelete**](TemplateApi.md#templateTemplateIdDelete) | **DELETE** /template/{templateId} | Delete a template from a template ID
[**templateTemplateIdGet**](TemplateApi.md#templateTemplateIdGet) | **GET** /template/{templateId} | Download a template from a template ID



## templatePost

> TemplatePost200Response templatePost(carboneVersion, templatePostRequest)

Upload a template.

Documentation: https://carbone.io/api-reference.html#add-templates

### Example

```javascript
import CarboneApi from 'carbone_api';
let defaultClient = CarboneApi.ApiClient.instance;
// Configure Bearer (eyJhbGci...) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new CarboneApi.TemplateApi();
let carboneVersion = 4; // Number | Carbone version
let templatePostRequest = new CarboneApi.TemplatePostRequest(); // TemplatePostRequest | Template File to upload, supported formats: DOCX, XLSX, PPTX, ODT, ODS, ODP, ODG, XHTML, IDML, HTML or an XML file
apiInstance.templatePost(carboneVersion, templatePostRequest, (error, data, response) => {
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
 **carboneVersion** | **Number**| Carbone version | [default to 4]
 **templatePostRequest** | [**TemplatePostRequest**](TemplatePostRequest.md)| Template File to upload, supported formats: DOCX, XLSX, PPTX, ODT, ODS, ODP, ODG, XHTML, IDML, HTML or an XML file | 

### Return type

[**TemplatePost200Response**](TemplatePost200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json, multipart/form-data
- **Accept**: application/json


## templateTemplateIdDelete

> TemplateTemplateIdDelete200Response templateTemplateIdDelete(templateId, carboneVersion)

Delete a template from a template ID

Documentation: https://carbone.io/api-reference.html#delete-templates

### Example

```javascript
import CarboneApi from 'carbone_api';
let defaultClient = CarboneApi.ApiClient.instance;
// Configure Bearer (eyJhbGci...) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new CarboneApi.TemplateApi();
let templateId = "templateId_example"; // String | Unique identifier of the template
let carboneVersion = 4; // Number | Carbone version
apiInstance.templateTemplateIdDelete(templateId, carboneVersion, (error, data, response) => {
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
 **templateId** | **String**| Unique identifier of the template | 
 **carboneVersion** | **Number**| Carbone version | [default to 4]

### Return type

[**TemplateTemplateIdDelete200Response**](TemplateTemplateIdDelete200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## templateTemplateIdGet

> templateTemplateIdGet(templateId, carboneVersion)

Download a template from a template ID

Documentation: https://carbone.io/api-reference.html#get-templates

### Example

```javascript
import CarboneApi from 'carbone_api';
let defaultClient = CarboneApi.ApiClient.instance;
// Configure Bearer (eyJhbGci...) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new CarboneApi.TemplateApi();
let templateId = "templateId_example"; // String | Unique identifier of the template
let carboneVersion = 4; // Number | Carbone version
apiInstance.templateTemplateIdGet(templateId, carboneVersion, (error, data, response) => {
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
 **templateId** | **String**| Unique identifier of the template | 
 **carboneVersion** | **Number**| Carbone version | [default to 4]

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

