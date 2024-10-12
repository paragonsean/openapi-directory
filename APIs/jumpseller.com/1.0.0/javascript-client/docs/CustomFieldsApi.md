# JumpsellerApi.CustomFieldsApi

All URIs are relative to *https://api.jumpseller.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customFieldsIdJsonDelete**](CustomFieldsApi.md#customFieldsIdJsonDelete) | **DELETE** /custom_fields/{id}.json | Delete an existing CustomField.
[**customFieldsIdJsonGet**](CustomFieldsApi.md#customFieldsIdJsonGet) | **GET** /custom_fields/{id}.json | Retrieve a single CustomField.
[**customFieldsIdJsonPut**](CustomFieldsApi.md#customFieldsIdJsonPut) | **PUT** /custom_fields/{id}.json | Update a CustomField.
[**customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonDelete**](CustomFieldsApi.md#customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonDelete) | **DELETE** /custom_fields/{id}/select_options/{custom_field_select_option_id}.json | Delete an existing CustomFieldSelectOption.
[**customFieldsJsonGet**](CustomFieldsApi.md#customFieldsJsonGet) | **GET** /custom_fields.json | Retrieve all Store&#39;s Custom Fields.
[**customFieldsJsonPost**](CustomFieldsApi.md#customFieldsJsonPost) | **POST** /custom_fields.json | Create a new Custom Field.



## customFieldsIdJsonDelete

> String customFieldsIdJsonDelete(login, authtoken, id)

Delete an existing CustomField.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CustomFieldsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the CustomField
apiInstance.customFieldsIdJsonDelete(login, authtoken, id, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **id** | **Number**| Id of the CustomField | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customFieldsIdJsonGet

> CustomField customFieldsIdJsonGet(login, authtoken, id)

Retrieve a single CustomField.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CustomFieldsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the CustomField
apiInstance.customFieldsIdJsonGet(login, authtoken, id, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **id** | **Number**| Id of the CustomField | 

### Return type

[**CustomField**](CustomField.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customFieldsIdJsonPut

> CustomField customFieldsIdJsonPut(login, authtoken, id, customFieldEdit)

Update a CustomField.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CustomFieldsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the CustomField
let customFieldEdit = new JumpsellerApi.CustomFieldEdit(); // CustomFieldEdit | CustomField parameters.
apiInstance.customFieldsIdJsonPut(login, authtoken, id, customFieldEdit, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **id** | **Number**| Id of the CustomField | 
 **customFieldEdit** | [**CustomFieldEdit**](CustomFieldEdit.md)| CustomField parameters. | 

### Return type

[**CustomField**](CustomField.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonDelete

> String customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonDelete(login, authtoken, id, customFieldSelectOptionId)

Delete an existing CustomFieldSelectOption.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CustomFieldsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the CustomField
let customFieldSelectOptionId = 56; // Number | Id of the CustomFieldSelectOption
apiInstance.customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonDelete(login, authtoken, id, customFieldSelectOptionId, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **id** | **Number**| Id of the CustomField | 
 **customFieldSelectOptionId** | **Number**| Id of the CustomFieldSelectOption | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customFieldsJsonGet

> [CustomField] customFieldsJsonGet(login, authtoken)

Retrieve all Store&#39;s Custom Fields.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CustomFieldsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
apiInstance.customFieldsJsonGet(login, authtoken, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 

### Return type

[**[CustomField]**](CustomField.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customFieldsJsonPost

> CustomField customFieldsJsonPost(login, authtoken, customFieldEdit)

Create a new Custom Field.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CustomFieldsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let customFieldEdit = new JumpsellerApi.CustomFieldEdit(); // CustomFieldEdit | Custom Field parameters.
apiInstance.customFieldsJsonPost(login, authtoken, customFieldEdit, (error, data, response) => {
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
 **login** | **String**| API OAuth login. | 
 **authtoken** | **String**| API OAuth token. | 
 **customFieldEdit** | [**CustomFieldEdit**](CustomFieldEdit.md)| Custom Field parameters. | 

### Return type

[**CustomField**](CustomField.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

