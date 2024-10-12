# Apacta.FormTemplatesApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**formTemplatesFormTemplateIdGet**](FormTemplatesApi.md#formTemplatesFormTemplateIdGet) | **GET** /form_templates/{form_template_id} | View one form template
[**formTemplatesGet**](FormTemplatesApi.md#formTemplatesGet) | **GET** /form_templates | Get array of form_templates for your company



## formTemplatesFormTemplateIdGet

> FormTemplatesFormTemplateIdGet200Response formTemplatesFormTemplateIdGet(formTemplateId)

View one form template

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.FormTemplatesApi();
let formTemplateId = "formTemplateId_example"; // String | 
apiInstance.formTemplatesFormTemplateIdGet(formTemplateId, (error, data, response) => {
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
 **formTemplateId** | **String**|  | 

### Return type

[**FormTemplatesFormTemplateIdGet200Response**](FormTemplatesFormTemplateIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## formTemplatesGet

> FormTemplatesGet200Response formTemplatesGet(opts)

Get array of form_templates for your company

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.FormTemplatesApi();
let opts = {
  'name': "name_example", // String | Used to filter on the `name` of the form_templates
  'identifier': "identifier_example", // String | Used to filter on the `identifier` of the form_templates
  'pdfTemplateIdentifier': "pdfTemplateIdentifier_example", // String | Used to filter on the `pdf_template_identifier` of the form_templates
  'description': "description_example" // String | Used to filter on the `description` of the form_templates
};
apiInstance.formTemplatesGet(opts, (error, data, response) => {
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
 **name** | **String**| Used to filter on the &#x60;name&#x60; of the form_templates | [optional] 
 **identifier** | **String**| Used to filter on the &#x60;identifier&#x60; of the form_templates | [optional] 
 **pdfTemplateIdentifier** | **String**| Used to filter on the &#x60;pdf_template_identifier&#x60; of the form_templates | [optional] 
 **description** | **String**| Used to filter on the &#x60;description&#x60; of the form_templates | [optional] 

### Return type

[**FormTemplatesGet200Response**](FormTemplatesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

