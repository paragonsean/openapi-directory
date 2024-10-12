# VaForms.FormsApi

All URIs are relative to *https://sandbox-api.va.gov/services/va_forms/v0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**findFormByFormName**](FormsApi.md#findFormByFormName) | **GET** /forms/{form_name} | Find form by form name
[**findForms**](FormsApi.md#findForms) | **GET** /forms | Returns all VA Forms and their last revision date



## findFormByFormName

> FindFormByFormName200Response findFormByFormName(formName)

Find form by form name

Returns a single form and the full revision history

### Example

```javascript
import VaForms from 'va_forms';
let defaultClient = VaForms.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new VaForms.FormsApi();
let formName = "10-10EZ"; // String | The VA form_name of the form being requested. The exact form name must be passed, including proper placement of prefixes and/or hyphens.
apiInstance.findFormByFormName(formName, (error, data, response) => {
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
 **formName** | **String**| The VA form_name of the form being requested. The exact form name must be passed, including proper placement of prefixes and/or hyphens. | 

### Return type

[**FindFormByFormName200Response**](FindFormByFormName200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## findForms

> FindForms200Response findForms(opts)

Returns all VA Forms and their last revision date

Returns an index of all available VA forms. Optionally, pass a query parameter to filter forms by form number or title.

### Example

```javascript
import VaForms from 'va_forms';
let defaultClient = VaForms.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new VaForms.FormsApi();
let opts = {
  'query': "query_example" // String | Returns form data based on entered form name.
};
apiInstance.findForms(opts, (error, data, response) => {
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
 **query** | **String**| Returns form data based on entered form name. | [optional] 

### Return type

[**FindForms200Response**](FindForms200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

