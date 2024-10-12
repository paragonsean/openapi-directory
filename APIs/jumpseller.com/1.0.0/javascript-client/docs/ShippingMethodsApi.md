# JumpsellerApi.ShippingMethodsApi

All URIs are relative to *https://api.jumpseller.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shippingMethodsIdJsonDelete**](ShippingMethodsApi.md#shippingMethodsIdJsonDelete) | **DELETE** /shipping_methods/{id}.json | Delete an existing Shipping Method.
[**shippingMethodsIdJsonGet**](ShippingMethodsApi.md#shippingMethodsIdJsonGet) | **GET** /shipping_methods/{id}.json | Retrieve a single Shipping Method.
[**shippingMethodsIdJsonPut**](ShippingMethodsApi.md#shippingMethodsIdJsonPut) | **PUT** /shipping_methods/{id}.json | Update a Shipping Method.
[**shippingMethodsJsonGet**](ShippingMethodsApi.md#shippingMethodsJsonGet) | **GET** /shipping_methods.json | Retrieve all Store&#39;s Shipping Methods.
[**shippingMethodsJsonPost**](ShippingMethodsApi.md#shippingMethodsJsonPost) | **POST** /shipping_methods.json | Creates a Shipping Method.



## shippingMethodsIdJsonDelete

> String shippingMethodsIdJsonDelete(login, authtoken, id)

Delete an existing Shipping Method.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ShippingMethodsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Shipping Method
apiInstance.shippingMethodsIdJsonDelete(login, authtoken, id, (error, data, response) => {
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
 **id** | **Number**| Id of the Shipping Method | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## shippingMethodsIdJsonGet

> ShippingMethod shippingMethodsIdJsonGet(login, authtoken, id)

Retrieve a single Shipping Method.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ShippingMethodsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Shipping Method
apiInstance.shippingMethodsIdJsonGet(login, authtoken, id, (error, data, response) => {
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
 **id** | **Number**| Id of the Shipping Method | 

### Return type

[**ShippingMethod**](ShippingMethod.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## shippingMethodsIdJsonPut

> ShippingMethod shippingMethodsIdJsonPut(login, authtoken, id, shippingMethodEdit)

Update a Shipping Method.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ShippingMethodsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Shipping Method
let shippingMethodEdit = new JumpsellerApi.ShippingMethodEdit(); // ShippingMethodEdit | Shipping Method parameters.
apiInstance.shippingMethodsIdJsonPut(login, authtoken, id, shippingMethodEdit, (error, data, response) => {
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
 **id** | **Number**| Id of the Shipping Method | 
 **shippingMethodEdit** | [**ShippingMethodEdit**](ShippingMethodEdit.md)| Shipping Method parameters. | 

### Return type

[**ShippingMethod**](ShippingMethod.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## shippingMethodsJsonGet

> [ShippingMethod] shippingMethodsJsonGet(login, authtoken)

Retrieve all Store&#39;s Shipping Methods.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ShippingMethodsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
apiInstance.shippingMethodsJsonGet(login, authtoken, (error, data, response) => {
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

[**[ShippingMethod]**](ShippingMethod.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## shippingMethodsJsonPost

> ShippingMethod shippingMethodsJsonPost(login, authtoken, shippingMethodEdit)

Creates a Shipping Method.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.ShippingMethodsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let shippingMethodEdit = new JumpsellerApi.ShippingMethodEdit(); // ShippingMethodEdit | Shipping Method parameters.
apiInstance.shippingMethodsJsonPost(login, authtoken, shippingMethodEdit, (error, data, response) => {
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
 **shippingMethodEdit** | [**ShippingMethodEdit**](ShippingMethodEdit.md)| Shipping Method parameters. | 

### Return type

[**ShippingMethod**](ShippingMethod.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

