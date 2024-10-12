# Apacta.FormFieldTypesApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**formFieldTypesFormFieldTypeIdGet**](FormFieldTypesApi.md#formFieldTypesFormFieldTypeIdGet) | **GET** /form_field_types/{form_field_type_id} | Get details about single &#x60;FormField&#x60;
[**formFieldTypesGet**](FormFieldTypesApi.md#formFieldTypesGet) | **GET** /form_field_types | Get list of form field types



## formFieldTypesFormFieldTypeIdGet

> FormFieldTypesFormFieldTypeIdGet200Response formFieldTypesFormFieldTypeIdGet(formFieldTypeId)

Get details about single &#x60;FormField&#x60;

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

let apiInstance = new Apacta.FormFieldTypesApi();
let formFieldTypeId = "formFieldTypeId_example"; // String | 
apiInstance.formFieldTypesFormFieldTypeIdGet(formFieldTypeId, (error, data, response) => {
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
 **formFieldTypeId** | **String**|  | 

### Return type

[**FormFieldTypesFormFieldTypeIdGet200Response**](FormFieldTypesFormFieldTypeIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## formFieldTypesGet

> FormFieldTypesGet200Response formFieldTypesGet(opts)

Get list of form field types

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

let apiInstance = new Apacta.FormFieldTypesApi();
let opts = {
  'name': "name_example", // String | Used to filter on the `name` of the form_fields
  'identifier': "identifier_example" // String | Used to filter on the `identifier` of the form_fields
};
apiInstance.formFieldTypesGet(opts, (error, data, response) => {
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
 **name** | **String**| Used to filter on the &#x60;name&#x60; of the form_fields | [optional] 
 **identifier** | **String**| Used to filter on the &#x60;identifier&#x60; of the form_fields | [optional] 

### Return type

[**FormFieldTypesGet200Response**](FormFieldTypesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

