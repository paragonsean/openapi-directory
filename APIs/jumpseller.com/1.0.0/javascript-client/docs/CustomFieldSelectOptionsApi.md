# JumpsellerApi.CustomFieldSelectOptionsApi

All URIs are relative to *https://api.jumpseller.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonGet**](CustomFieldSelectOptionsApi.md#customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonGet) | **GET** /custom_fields/{id}/select_options/{custom_field_select_option_id}.json | Retrieve a single SelectOption from a CustomField.
[**customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonPut**](CustomFieldSelectOptionsApi.md#customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonPut) | **PUT** /custom_fields/{id}/select_options/{custom_field_select_option_id}.json | Update a SelectOption from a CustomField.
[**customFieldsIdSelectOptionsJsonGet**](CustomFieldSelectOptionsApi.md#customFieldsIdSelectOptionsJsonGet) | **GET** /custom_fields/{id}/select_options.json | Retrieve all Store&#39;s Custom Fields.
[**customFieldsIdSelectOptionsJsonPost**](CustomFieldSelectOptionsApi.md#customFieldsIdSelectOptionsJsonPost) | **POST** /custom_fields/{id}/select_options.json | Create a new Custom Field Select Option.



## customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonGet

> CustomFieldSelectOption customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonGet(login, authtoken, id, customFieldSelectOptionId)

Retrieve a single SelectOption from a CustomField.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CustomFieldSelectOptionsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the CustomField
let customFieldSelectOptionId = 56; // Number | Id of the CustomFieldSelectOption
apiInstance.customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonGet(login, authtoken, id, customFieldSelectOptionId, (error, data, response) => {
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

[**CustomFieldSelectOption**](CustomFieldSelectOption.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonPut

> CustomFieldSelectOption customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonPut(login, authtoken, id, customFieldSelectOptionId, customFieldSelectOptionEdit)

Update a SelectOption from a CustomField.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CustomFieldSelectOptionsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the CustomField
let customFieldSelectOptionId = 56; // Number | Id of the CustomFieldSelectOption
let customFieldSelectOptionEdit = new JumpsellerApi.CustomFieldSelectOptionEdit(); // CustomFieldSelectOptionEdit | CustomFieldSelectOption parameters.
apiInstance.customFieldsIdSelectOptionsCustomFieldSelectOptionIdJsonPut(login, authtoken, id, customFieldSelectOptionId, customFieldSelectOptionEdit, (error, data, response) => {
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
 **customFieldSelectOptionEdit** | [**CustomFieldSelectOptionEdit**](CustomFieldSelectOptionEdit.md)| CustomFieldSelectOption parameters. | 

### Return type

[**CustomFieldSelectOption**](CustomFieldSelectOption.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## customFieldsIdSelectOptionsJsonGet

> [CustomFieldSelectOption] customFieldsIdSelectOptionsJsonGet(login, authtoken, id)

Retrieve all Store&#39;s Custom Fields.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CustomFieldSelectOptionsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the CustomField
apiInstance.customFieldsIdSelectOptionsJsonGet(login, authtoken, id, (error, data, response) => {
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

[**[CustomFieldSelectOption]**](CustomFieldSelectOption.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## customFieldsIdSelectOptionsJsonPost

> CustomFieldSelectOption customFieldsIdSelectOptionsJsonPost(login, authtoken, id, customFieldSelectOptionEdit)

Create a new Custom Field Select Option.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CustomFieldSelectOptionsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = "id_example"; // String | Automatically added
let customFieldSelectOptionEdit = new JumpsellerApi.CustomFieldSelectOptionEdit(); // CustomFieldSelectOptionEdit | Custom Field Select Option parameters.
apiInstance.customFieldsIdSelectOptionsJsonPost(login, authtoken, id, customFieldSelectOptionEdit, (error, data, response) => {
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
 **id** | **String**| Automatically added | 
 **customFieldSelectOptionEdit** | [**CustomFieldSelectOptionEdit**](CustomFieldSelectOptionEdit.md)| Custom Field Select Option parameters. | 

### Return type

[**CustomFieldSelectOption**](CustomFieldSelectOption.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

