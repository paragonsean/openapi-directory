# JumpsellerApi.CheckoutCustomFieldsApi

All URIs are relative to *https://api.jumpseller.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkoutCustomFieldsIdJsonDelete**](CheckoutCustomFieldsApi.md#checkoutCustomFieldsIdJsonDelete) | **DELETE** /checkout_custom_fields/{id}.json | Delete an existing CheckoutCustomField.
[**checkoutCustomFieldsIdJsonGet**](CheckoutCustomFieldsApi.md#checkoutCustomFieldsIdJsonGet) | **GET** /checkout_custom_fields/{id}.json | Retrieve a single CheckoutCustomField.
[**checkoutCustomFieldsIdJsonPut**](CheckoutCustomFieldsApi.md#checkoutCustomFieldsIdJsonPut) | **PUT** /checkout_custom_fields/{id}.json | Update a CheckoutCustomField.
[**checkoutCustomFieldsJsonGet**](CheckoutCustomFieldsApi.md#checkoutCustomFieldsJsonGet) | **GET** /checkout_custom_fields.json | Retrieve all Checkout Custom Fields.
[**checkoutCustomFieldsJsonPost**](CheckoutCustomFieldsApi.md#checkoutCustomFieldsJsonPost) | **POST** /checkout_custom_fields.json | Create a new CheckoutCustomField.



## checkoutCustomFieldsIdJsonDelete

> String checkoutCustomFieldsIdJsonDelete(login, authtoken, id)

Delete an existing CheckoutCustomField.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CheckoutCustomFieldsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the CheckoutCustomField
apiInstance.checkoutCustomFieldsIdJsonDelete(login, authtoken, id, (error, data, response) => {
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
 **id** | **Number**| Id of the CheckoutCustomField | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## checkoutCustomFieldsIdJsonGet

> CheckoutCustomField checkoutCustomFieldsIdJsonGet(login, authtoken, id)

Retrieve a single CheckoutCustomField.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CheckoutCustomFieldsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the CheckoutCustomField
apiInstance.checkoutCustomFieldsIdJsonGet(login, authtoken, id, (error, data, response) => {
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
 **id** | **Number**| Id of the CheckoutCustomField | 

### Return type

[**CheckoutCustomField**](CheckoutCustomField.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## checkoutCustomFieldsIdJsonPut

> CheckoutCustomField checkoutCustomFieldsIdJsonPut(login, authtoken, id, checkoutCustomFieldEdit)

Update a CheckoutCustomField.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CheckoutCustomFieldsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the CheckoutCustomField
let checkoutCustomFieldEdit = new JumpsellerApi.CheckoutCustomFieldEdit(); // CheckoutCustomFieldEdit | CheckoutCustomField parameters.
apiInstance.checkoutCustomFieldsIdJsonPut(login, authtoken, id, checkoutCustomFieldEdit, (error, data, response) => {
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
 **id** | **Number**| Id of the CheckoutCustomField | 
 **checkoutCustomFieldEdit** | [**CheckoutCustomFieldEdit**](CheckoutCustomFieldEdit.md)| CheckoutCustomField parameters. | 

### Return type

[**CheckoutCustomField**](CheckoutCustomField.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## checkoutCustomFieldsJsonGet

> [CheckoutCustomField] checkoutCustomFieldsJsonGet(login, authtoken, opts)

Retrieve all Checkout Custom Fields.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CheckoutCustomFieldsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let opts = {
  'limit': 50, // Number | List restriction
  'page': 1 // Number | List page
};
apiInstance.checkoutCustomFieldsJsonGet(login, authtoken, opts, (error, data, response) => {
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
 **limit** | **Number**| List restriction | [optional] [default to 50]
 **page** | **Number**| List page | [optional] [default to 1]

### Return type

[**[CheckoutCustomField]**](CheckoutCustomField.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## checkoutCustomFieldsJsonPost

> CheckoutCustomField checkoutCustomFieldsJsonPost(login, authtoken, checkoutCustomFieldEdit)

Create a new CheckoutCustomField.

Type values can be: input, selection, checkbox, date or text. Area values can be: contact, billing_shipping or other.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.CheckoutCustomFieldsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let checkoutCustomFieldEdit = new JumpsellerApi.CheckoutCustomFieldEdit(); // CheckoutCustomFieldEdit | CheckoutCustomField parameters.
apiInstance.checkoutCustomFieldsJsonPost(login, authtoken, checkoutCustomFieldEdit, (error, data, response) => {
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
 **checkoutCustomFieldEdit** | [**CheckoutCustomFieldEdit**](CheckoutCustomFieldEdit.md)| CheckoutCustomField parameters. | 

### Return type

[**CheckoutCustomField**](CheckoutCustomField.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

