# Apacta.FormFieldsApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**formFieldsFormFieldIdGet**](FormFieldsApi.md#formFieldsFormFieldIdGet) | **GET** /form_fields/{form_field_id} | Get details about single &#x60;FormField&#x60;
[**formFieldsPost**](FormFieldsApi.md#formFieldsPost) | **POST** /form_fields | Add a new field to a &#x60;Form&#x60;



## formFieldsFormFieldIdGet

> FormFieldsFormFieldIdGet200Response formFieldsFormFieldIdGet(formFieldId)

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

let apiInstance = new Apacta.FormFieldsApi();
let formFieldId = "formFieldId_example"; // String | 
apiInstance.formFieldsFormFieldIdGet(formFieldId, (error, data, response) => {
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
 **formFieldId** | **String**|  | 

### Return type

[**FormFieldsFormFieldIdGet200Response**](FormFieldsFormFieldIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## formFieldsPost

> ClockingRecordsPost201Response formFieldsPost(opts)

Add a new field to a &#x60;Form&#x60;

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

let apiInstance = new Apacta.FormFieldsApi();
let opts = {
  'formFieldsPostRequest': new Apacta.FormFieldsPostRequest() // FormFieldsPostRequest | 
};
apiInstance.formFieldsPost(opts, (error, data, response) => {
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
 **formFieldsPostRequest** | [**FormFieldsPostRequest**](FormFieldsPostRequest.md)|  | [optional] 

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

