# JumpsellerApi.PaymentMethodsApi

All URIs are relative to *https://api.jumpseller.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**paymentMethodsIdJsonGet**](PaymentMethodsApi.md#paymentMethodsIdJsonGet) | **GET** /payment_methods/{id}.json | Retrieve a single Payment Method.
[**paymentMethodsJsonGet**](PaymentMethodsApi.md#paymentMethodsJsonGet) | **GET** /payment_methods.json | Retrieve all Store&#39;s Payment Methods.



## paymentMethodsIdJsonGet

> PaymentMethod paymentMethodsIdJsonGet(login, authtoken, id)

Retrieve a single Payment Method.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.PaymentMethodsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Payment Method
apiInstance.paymentMethodsIdJsonGet(login, authtoken, id, (error, data, response) => {
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
 **id** | **Number**| Id of the Payment Method | 

### Return type

[**PaymentMethod**](PaymentMethod.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## paymentMethodsJsonGet

> [PaymentMethod] paymentMethodsJsonGet(login, authtoken)

Retrieve all Store&#39;s Payment Methods.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.PaymentMethodsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
apiInstance.paymentMethodsJsonGet(login, authtoken, (error, data, response) => {
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

[**[PaymentMethod]**](PaymentMethod.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

