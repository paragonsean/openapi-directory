# Contribly.FormApi

All URIs are relative to *https://api.contribly.com/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**formResponsesGet**](FormApi.md#formResponsesGet) | **GET** /form-responses | List form responses
[**formResponsesIdGet**](FormApi.md#formResponsesIdGet) | **GET** /form-responses/{id} | Get a single form response by id
[**formResponsesPost**](FormApi.md#formResponsesPost) | **POST** /form-responses | Submit a response to a form
[**formsGet**](FormApi.md#formsGet) | **GET** /forms | List forms
[**formsIdDelete**](FormApi.md#formsIdDelete) | **DELETE** /forms/{id} | Delete this form and all of it&#39;s responses.
[**formsIdGet**](FormApi.md#formsIdGet) | **GET** /forms/{id} | Get a single form by id
[**formsPost**](FormApi.md#formsPost) | **POST** /forms | Create a form



## formResponsesGet

> [FormResponse] formResponsesGet(opts)

List form responses

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.FormApi();
let opts = {
  'user': "user_example", // String | Restrict results to responses submitted by this user.
  'form': "form_example", // String | Restrict results to responses submitted to this form.
  'contribution': "contribution_example" // String | Restrict results to responses relating to this contribution.
};
apiInstance.formResponsesGet(opts, (error, data, response) => {
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
 **user** | **String**| Restrict results to responses submitted by this user. | [optional] 
 **form** | **String**| Restrict results to responses submitted to this form. | [optional] 
 **contribution** | **String**| Restrict results to responses relating to this contribution. | [optional] 

### Return type

[**[FormResponse]**](FormResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## formResponsesIdGet

> FormResponse formResponsesIdGet(id)

Get a single form response by id

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.FormApi();
let id = "id_example"; // String | Id of the assignment to return
apiInstance.formResponsesIdGet(id, (error, data, response) => {
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
 **id** | **String**| Id of the assignment to return | 

### Return type

[**FormResponse**](FormResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## formResponsesPost

> FormResponse formResponsesPost(formResponseSubmission)

Submit a response to a form

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.FormApi();
let formResponseSubmission = new Contribly.FormResponseSubmission(); // FormResponseSubmission | Form response
apiInstance.formResponsesPost(formResponseSubmission, (error, data, response) => {
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
 **formResponseSubmission** | [**FormResponseSubmission**](FormResponseSubmission.md)| Form response | 

### Return type

[**FormResponse**](FormResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## formsGet

> [Form] formsGet(ownedBy)

List forms

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.FormApi();
let ownedBy = "ownedBy_example"; // String | Restrict results to forms owned by this user.
apiInstance.formsGet(ownedBy, (error, data, response) => {
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
 **ownedBy** | **String**| Restrict results to forms owned by this user. | 

### Return type

[**[Form]**](Form.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## formsIdDelete

> formsIdDelete(id)

Delete this form and all of it&#39;s responses.

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.FormApi();
let id = "id_example"; // String | Id of the form to delete
apiInstance.formsIdDelete(id, (error, data, response) => {
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
 **id** | **String**| Id of the form to delete | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## formsIdGet

> Form formsIdGet(id)

Get a single form by id

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.FormApi();
let id = "id_example"; // String | Id of the form to return
apiInstance.formsIdGet(id, (error, data, response) => {
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
 **id** | **String**| Id of the form to return | 

### Return type

[**Form**](Form.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## formsPost

> Form formsPost(formSubmission)

Create a form

### Example

```javascript
import Contribly from 'contribly';

let apiInstance = new Contribly.FormApi();
let formSubmission = new Contribly.FormSubmission(); // FormSubmission | Form object to be created
apiInstance.formsPost(formSubmission, (error, data, response) => {
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
 **formSubmission** | [**FormSubmission**](FormSubmission.md)| Form object to be created | 

### Return type

[**Form**](Form.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

