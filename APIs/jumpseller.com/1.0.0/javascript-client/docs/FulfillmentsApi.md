# JumpsellerApi.FulfillmentsApi

All URIs are relative to *https://api.jumpseller.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fulfillmentsCountJsonGet**](FulfillmentsApi.md#fulfillmentsCountJsonGet) | **GET** /fulfillments/count.json | Count all Fulfillments.
[**fulfillmentsIdJsonGet**](FulfillmentsApi.md#fulfillmentsIdJsonGet) | **GET** /fulfillments/{id}.json | Retrieve a single Fulfillment.
[**fulfillmentsJsonGet**](FulfillmentsApi.md#fulfillmentsJsonGet) | **GET** /fulfillments.json | Retrieve all Fulfillments.
[**orderIdFulfillmentsJsonGet**](FulfillmentsApi.md#orderIdFulfillmentsJsonGet) | **GET** /order/{id}/fulfillments.json | Retrieve the Fulfillments associated with the Order.



## fulfillmentsCountJsonGet

> Count fulfillmentsCountJsonGet(login, authtoken)

Count all Fulfillments.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.FulfillmentsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
apiInstance.fulfillmentsCountJsonGet(login, authtoken, (error, data, response) => {
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

[**Count**](Count.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fulfillmentsIdJsonGet

> Fulfillment fulfillmentsIdJsonGet(login, authtoken, id)

Retrieve a single Fulfillment.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.FulfillmentsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Fulfillment
apiInstance.fulfillmentsIdJsonGet(login, authtoken, id, (error, data, response) => {
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
 **id** | **Number**| Id of the Fulfillment | 

### Return type

[**Fulfillment**](Fulfillment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fulfillmentsJsonGet

> [Fulfillment] fulfillmentsJsonGet(login, authtoken, opts)

Retrieve all Fulfillments.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.FulfillmentsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let opts = {
  'limit': 50, // Number | List restriction
  'page': 1 // Number | List page
};
apiInstance.fulfillmentsJsonGet(login, authtoken, opts, (error, data, response) => {
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

[**[Fulfillment]**](Fulfillment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## orderIdFulfillmentsJsonGet

> [Fulfillment] orderIdFulfillmentsJsonGet(login, authtoken, id)

Retrieve the Fulfillments associated with the Order.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.FulfillmentsApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Order
apiInstance.orderIdFulfillmentsJsonGet(login, authtoken, id, (error, data, response) => {
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
 **id** | **Number**| Id of the Order | 

### Return type

[**[Fulfillment]**](Fulfillment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

