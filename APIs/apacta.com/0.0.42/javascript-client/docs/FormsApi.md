# Apacta.FormsApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**formsFormIdDelete**](FormsApi.md#formsFormIdDelete) | **DELETE** /forms/{form_id} | Delete a form
[**formsFormIdGet**](FormsApi.md#formsFormIdGet) | **GET** /forms/{form_id} | View form
[**formsFormIdPut**](FormsApi.md#formsFormIdPut) | **PUT** /forms/{form_id} | Edit a form
[**formsGet**](FormsApi.md#formsGet) | **GET** /forms | Retrieve array of forms
[**formsPost**](FormsApi.md#formsPost) | **POST** /forms | Add new form
[**formsUndeleteFormIdGet**](FormsApi.md#formsUndeleteFormIdGet) | **GET** /forms/undelete/{form_id} | Undelete form and related entities to it
[**formsViewTimeFormPdfFormIdGet**](FormsApi.md#formsViewTimeFormPdfFormIdGet) | **GET** /forms/view_time_form_pdf/{form_id} | Generate time form pdf



## formsFormIdDelete

> formsFormIdDelete(formId)

Delete a form

You can only delete the forms that you&#39;ve submitted yourself

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

let apiInstance = new Apacta.FormsApi();
let formId = "formId_example"; // String | 
apiInstance.formsFormIdDelete(formId, (error, data, response) => {
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
 **formId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## formsFormIdGet

> FormsFormIdGet200Response formsFormIdGet(formId)

View form

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

let apiInstance = new Apacta.FormsApi();
let formId = "formId_example"; // String | 
apiInstance.formsFormIdGet(formId, (error, data, response) => {
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
 **formId** | **String**|  | 

### Return type

[**FormsFormIdGet200Response**](FormsFormIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## formsFormIdPut

> formsFormIdPut(formId)

Edit a form

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

let apiInstance = new Apacta.FormsApi();
let formId = "formId_example"; // String | 
apiInstance.formsFormIdPut(formId, (error, data, response) => {
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
 **formId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## formsGet

> FormsGet200Response formsGet(opts)

Retrieve array of forms

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

let apiInstance = new Apacta.FormsApi();
let opts = {
  'extended': "extended_example", // String | Used to have extended details from the forms from the `Form`'s `FormFields`
  'dateFrom': "dateFrom_example", // String | Used in conjunction with `date_to` to only show forms within these dates - format like `2016-28-05`
  'dateTo': "dateTo_example", // String | Used in conjunction with `date_from` to only show forms within these dates - format like `2016-28-30`
  'show': "show_example", // String | Used to show forms with trashed
  'projectId': "projectId_example", // String | Used to filter on the `project_id` of the forms
  'createdById': "createdById_example", // String | Used to filter on the `created_by_id` of the forms
  'formTemplateId': ["null"], // [String] | Used to filter on the `form_template_id` of the forms. Accept single value and array.
  'formTemplateType': "formTemplateType_example", // String | Filter by `form_templates.identifier` containing string passed in `form_template_type`. Accept strings like [`qa`, `dagseddel`]
  'employeeName': "employeeName_example" // String | Used to filter forms by user's first or last name
};
apiInstance.formsGet(opts, (error, data, response) => {
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
 **extended** | **String**| Used to have extended details from the forms from the &#x60;Form&#x60;&#39;s &#x60;FormFields&#x60; | [optional] 
 **dateFrom** | **String**| Used in conjunction with &#x60;date_to&#x60; to only show forms within these dates - format like &#x60;2016-28-05&#x60; | [optional] 
 **dateTo** | **String**| Used in conjunction with &#x60;date_from&#x60; to only show forms within these dates - format like &#x60;2016-28-30&#x60; | [optional] 
 **show** | **String**| Used to show forms with trashed | [optional] 
 **projectId** | **String**| Used to filter on the &#x60;project_id&#x60; of the forms | [optional] 
 **createdById** | **String**| Used to filter on the &#x60;created_by_id&#x60; of the forms | [optional] 
 **formTemplateId** | [**[String]**](String.md)| Used to filter on the &#x60;form_template_id&#x60; of the forms. Accept single value and array. | [optional] 
 **formTemplateType** | **String**| Filter by &#x60;form_templates.identifier&#x60; containing string passed in &#x60;form_template_type&#x60;. Accept strings like [&#x60;qa&#x60;, &#x60;dagseddel&#x60;] | [optional] 
 **employeeName** | **String**| Used to filter forms by user&#39;s first or last name | [optional] 

### Return type

[**FormsGet200Response**](FormsGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## formsPost

> ClockingRecordsPost201Response formsPost(opts)

Add new form

Used to add a form into the system

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

let apiInstance = new Apacta.FormsApi();
let opts = {
  'formsPostRequest': new Apacta.FormsPostRequest() // FormsPostRequest | 
};
apiInstance.formsPost(opts, (error, data, response) => {
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
 **formsPostRequest** | [**FormsPostRequest**](FormsPostRequest.md)|  | [optional] 

### Return type

[**ClockingRecordsPost201Response**](ClockingRecordsPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## formsUndeleteFormIdGet

> EmptySuccessResponse formsUndeleteFormIdGet(formId)

Undelete form and related entities to it

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

let apiInstance = new Apacta.FormsApi();
let formId = "formId_example"; // String | 
apiInstance.formsUndeleteFormIdGet(formId, (error, data, response) => {
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
 **formId** | **String**|  | 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## formsViewTimeFormPdfFormIdGet

> EmptySuccessResponse formsViewTimeFormPdfFormIdGet(formId)

Generate time form pdf

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

let apiInstance = new Apacta.FormsApi();
let formId = "formId_example"; // String | 
apiInstance.formsViewTimeFormPdfFormIdGet(formId, (error, data, response) => {
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
 **formId** | **String**|  | 

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

