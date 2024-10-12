# HandwryttenApi.TemplatesApi

All URIs are relative to *https://api.handwrytten.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTemplate**](TemplatesApi.md#createTemplate) | **POST** /templates/create | Creates a New Template in the User’s Account
[**deleteTemplate**](TemplatesApi.md#deleteTemplate) | **POST** /templates/delete | Deletes a users template
[**getTemplateCategories**](TemplatesApi.md#getTemplateCategories) | **GET** /templateCategories/list | List template categories
[**getTemplateCategoriesAuthorized**](TemplatesApi.md#getTemplateCategoriesAuthorized) | **POST** /templateCategories/list | List template categories
[**getTemplateDetail**](TemplatesApi.md#getTemplateDetail) | **POST** /templates/view | Get all info on a template
[**getTemplates**](TemplatesApi.md#getTemplates) | **GET** /templates/list | List template categories
[**getTemplatessAuthorized**](TemplatesApi.md#getTemplatessAuthorized) | **POST** /templates/list | List template categories
[**updateTemplate**](TemplatesApi.md#updateTemplate) | **POST** /templates/update | Updates an Existing Template in the User’s Account



## createTemplate

> [Template] createTemplate(body)

Creates a New Template in the User’s Account

Creates a new Template in the User’s Account

### Example

```javascript
import HandwryttenApi from 'handwrytten_api';

let apiInstance = new HandwryttenApi.TemplatesApi();
let body = new HandwryttenApi.CreateTemplateRequest(); // CreateTemplateRequest | additional parameters
apiInstance.createTemplate(body, (error, data, response) => {
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
 **body** | [**CreateTemplateRequest**](CreateTemplateRequest.md)| additional parameters | 

### Return type

[**[Template]**](Template.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteTemplate

> ChangePassword200Response deleteTemplate(body)

Deletes a users template

Deletes a template in the User’s Account

### Example

```javascript
import HandwryttenApi from 'handwrytten_api';

let apiInstance = new HandwryttenApi.TemplatesApi();
let body = new HandwryttenApi.DeleteTemplateRequest(); // DeleteTemplateRequest | additional parameters
apiInstance.deleteTemplate(body, (error, data, response) => {
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
 **body** | [**DeleteTemplateRequest**](DeleteTemplateRequest.md)| additional parameters | 

### Return type

[**ChangePassword200Response**](ChangePassword200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getTemplateCategories

> [TemplateCategory] getTemplateCategories()

List template categories

Lists the common template categories of all users. As you are not logged in, this is what you are limited to.

### Example

```javascript
import HandwryttenApi from 'handwrytten_api';

let apiInstance = new HandwryttenApi.TemplatesApi();
apiInstance.getTemplateCategories((error, data, response) => {
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

[**[TemplateCategory]**](TemplateCategory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTemplateCategoriesAuthorized

> [TemplateCategory] getTemplateCategoriesAuthorized(opts)

List template categories

Lists the template categories of all users. By passing the optional UID, any custom template categories are also available.

### Example

```javascript
import HandwryttenApi from 'handwrytten_api';

let apiInstance = new HandwryttenApi.TemplatesApi();
let opts = {
  'body': new HandwryttenApi.GetTemplateCategoriesAuthorizedRequest() // GetTemplateCategoriesAuthorizedRequest | additional parameters
};
apiInstance.getTemplateCategoriesAuthorized(opts, (error, data, response) => {
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
 **body** | [**GetTemplateCategoriesAuthorizedRequest**](GetTemplateCategoriesAuthorizedRequest.md)| additional parameters | [optional] 

### Return type

[**[TemplateCategory]**](TemplateCategory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getTemplateDetail

> Template getTemplateDetail(body)

Get all info on a template

Provides all details on a template

### Example

```javascript
import HandwryttenApi from 'handwrytten_api';

let apiInstance = new HandwryttenApi.TemplatesApi();
let body = new HandwryttenApi.GetTemplateDetailRequest(); // GetTemplateDetailRequest | additional parameters
apiInstance.getTemplateDetail(body, (error, data, response) => {
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
 **body** | [**GetTemplateDetailRequest**](GetTemplateDetailRequest.md)| additional parameters | 

### Return type

[**Template**](Template.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getTemplates

> [Template] getTemplates()

List template categories

Lists the common template categories of all users. As you are not logged in, this is what you are limited to.

### Example

```javascript
import HandwryttenApi from 'handwrytten_api';

let apiInstance = new HandwryttenApi.TemplatesApi();
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

[**[Template]**](Template.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTemplatessAuthorized

> [Template] getTemplatessAuthorized(opts)

List template categories

Lists the template categories of all users. By passing the optional UID, any custom template categories are also available.

### Example

```javascript
import HandwryttenApi from 'handwrytten_api';

let apiInstance = new HandwryttenApi.TemplatesApi();
let opts = {
  'body': new HandwryttenApi.GetTemplatessAuthorizedRequest() // GetTemplatessAuthorizedRequest | additional parameters
};
apiInstance.getTemplatessAuthorized(opts, (error, data, response) => {
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
 **body** | [**GetTemplatessAuthorizedRequest**](GetTemplatessAuthorizedRequest.md)| additional parameters | [optional] 

### Return type

[**[Template]**](Template.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateTemplate

> [Template] updateTemplate(body)

Updates an Existing Template in the User’s Account

Updates an Existing Template in the User’s Account

### Example

```javascript
import HandwryttenApi from 'handwrytten_api';

let apiInstance = new HandwryttenApi.TemplatesApi();
let body = new HandwryttenApi.UpdateTemplateRequest(); // UpdateTemplateRequest | additional parameters
apiInstance.updateTemplate(body, (error, data, response) => {
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
 **body** | [**UpdateTemplateRequest**](UpdateTemplateRequest.md)| additional parameters | 

### Return type

[**[Template]**](Template.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

