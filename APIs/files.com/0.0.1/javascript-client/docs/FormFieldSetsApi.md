# FilesComApi.FormFieldSetsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteFormFieldSetsId**](FormFieldSetsApi.md#deleteFormFieldSetsId) | **DELETE** /form_field_sets/{id} | Delete Form Field Set
[**getFormFieldSets**](FormFieldSetsApi.md#getFormFieldSets) | **GET** /form_field_sets | List Form Field Sets
[**getFormFieldSetsId**](FormFieldSetsApi.md#getFormFieldSetsId) | **GET** /form_field_sets/{id} | Show Form Field Set
[**patchFormFieldSetsId**](FormFieldSetsApi.md#patchFormFieldSetsId) | **PATCH** /form_field_sets/{id} | Update Form Field Set
[**postFormFieldSets**](FormFieldSetsApi.md#postFormFieldSets) | **POST** /form_field_sets | Create Form Field Set



## deleteFormFieldSetsId

> deleteFormFieldSetsId(id)

Delete Form Field Set

Delete Form Field Set

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.FormFieldSetsApi();
let id = 56; // Number | Form Field Set ID.
apiInstance.deleteFormFieldSetsId(id, (error, data, response) => {
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
 **id** | **Number**| Form Field Set ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getFormFieldSets

> [FormFieldSetEntity] getFormFieldSets(opts)

List Form Field Sets

List Form Field Sets

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.FormFieldSetsApi();
let opts = {
  'userId': 56, // Number | User ID.  Provide a value of `0` to operate the current session's user.
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56 // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
};
apiInstance.getFormFieldSets(opts, (error, data, response) => {
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
 **userId** | **Number**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] 
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 

### Return type

[**[FormFieldSetEntity]**](FormFieldSetEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFormFieldSetsId

> FormFieldSetEntity getFormFieldSetsId(id)

Show Form Field Set

Show Form Field Set

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.FormFieldSetsApi();
let id = 56; // Number | Form Field Set ID.
apiInstance.getFormFieldSetsId(id, (error, data, response) => {
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
 **id** | **Number**| Form Field Set ID. | 

### Return type

[**FormFieldSetEntity**](FormFieldSetEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchFormFieldSetsId

> FormFieldSetEntity patchFormFieldSetsId(id, patchFormFieldSets)

Update Form Field Set

Update Form Field Set

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.FormFieldSetsApi();
let id = 56; // Number | Form Field Set ID.
let patchFormFieldSets = new FilesComApi.PatchFormFieldSets(); // PatchFormFieldSets | 
apiInstance.patchFormFieldSetsId(id, patchFormFieldSets, (error, data, response) => {
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
 **id** | **Number**| Form Field Set ID. | 
 **patchFormFieldSets** | [**PatchFormFieldSets**](PatchFormFieldSets.md)|  | 

### Return type

[**FormFieldSetEntity**](FormFieldSetEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json


## postFormFieldSets

> FormFieldSetEntity postFormFieldSets(postFormFieldSets)

Create Form Field Set

Create Form Field Set

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.FormFieldSetsApi();
let postFormFieldSets = new FilesComApi.PostFormFieldSets(); // PostFormFieldSets | 
apiInstance.postFormFieldSets(postFormFieldSets, (error, data, response) => {
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
 **postFormFieldSets** | [**PostFormFieldSets**](PostFormFieldSets.md)|  | 

### Return type

[**FormFieldSetEntity**](FormFieldSetEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
- **Accept**: application/json

