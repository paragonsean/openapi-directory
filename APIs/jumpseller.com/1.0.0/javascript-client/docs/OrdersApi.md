# JumpsellerApi.OrdersApi

All URIs are relative to *https://api.jumpseller.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ordersAfterIdJsonGet**](OrdersApi.md#ordersAfterIdJsonGet) | **GET** /orders/after/{id}.json | Retrieve orders filtered by Order Id.
[**ordersCountJsonGet**](OrdersApi.md#ordersCountJsonGet) | **GET** /orders/count.json | Count all Orders.
[**ordersIdHistoryJsonGet**](OrdersApi.md#ordersIdHistoryJsonGet) | **GET** /orders/{id}/history.json | Retrieve all Order History.
[**ordersIdHistoryJsonPost**](OrdersApi.md#ordersIdHistoryJsonPost) | **POST** /orders/{id}/history.json | Create a new Order History Entry.
[**ordersIdJsonGet**](OrdersApi.md#ordersIdJsonGet) | **GET** /orders/{id}.json | Retrieve a single Order.
[**ordersIdJsonPut**](OrdersApi.md#ordersIdJsonPut) | **PUT** /orders/{id}.json | Modify an existing Order.
[**ordersJsonGet**](OrdersApi.md#ordersJsonGet) | **GET** /orders.json | Retrieve all Orders.
[**ordersJsonPost**](OrdersApi.md#ordersJsonPost) | **POST** /orders.json | Create a new Order.
[**ordersStatusStatusJsonGet**](OrdersApi.md#ordersStatusStatusJsonGet) | **GET** /orders/status/{status}.json | Retrieve orders filtered by status.



## ordersAfterIdJsonGet

> Order ordersAfterIdJsonGet(login, authtoken, id)

Retrieve orders filtered by Order Id.

For example the GET /orders/after/5000 will return Order 5001, 5002, 5003, etc.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.OrdersApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Order
apiInstance.ordersAfterIdJsonGet(login, authtoken, id, (error, data, response) => {
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

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ordersCountJsonGet

> Count ordersCountJsonGet(login, authtoken)

Count all Orders.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.OrdersApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
apiInstance.ordersCountJsonGet(login, authtoken, (error, data, response) => {
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


## ordersIdHistoryJsonGet

> [OrderHistory] ordersIdHistoryJsonGet(login, authtoken, id)

Retrieve all Order History.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.OrdersApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Order
apiInstance.ordersIdHistoryJsonGet(login, authtoken, id, (error, data, response) => {
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

[**[OrderHistory]**](OrderHistory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ordersIdHistoryJsonPost

> OrderHistory ordersIdHistoryJsonPost(login, authtoken, id, orderHistoryEdit)

Create a new Order History Entry.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.OrdersApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the OrderHistory
let orderHistoryEdit = new JumpsellerApi.OrderHistoryEdit(); // OrderHistoryEdit | Order History parameters.
apiInstance.ordersIdHistoryJsonPost(login, authtoken, id, orderHistoryEdit, (error, data, response) => {
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
 **id** | **Number**| Id of the OrderHistory | 
 **orderHistoryEdit** | [**OrderHistoryEdit**](OrderHistoryEdit.md)| Order History parameters. | 

### Return type

[**OrderHistory**](OrderHistory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ordersIdJsonGet

> Order ordersIdJsonGet(login, authtoken, id)

Retrieve a single Order.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.OrdersApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Order
apiInstance.ordersIdJsonGet(login, authtoken, id, (error, data, response) => {
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

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ordersIdJsonPut

> Order ordersIdJsonPut(login, authtoken, id, orderEdit)

Modify an existing Order.

Only &#x60;status&#x60;, &#x60;shipment_status&#x60;, &#x60;tracking_number&#x60;, &#x60;tracking_company&#x60;, &#x60;tracking_url&#x60;, &#x60;additional_information&#x60; and &#x60;additional_fields&#x60; are available for update. An email is send if &#x60;shipment_status&#x60; changes.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.OrdersApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let id = 56; // Number | Id of the Order
let orderEdit = new JumpsellerApi.OrderEdit(); // OrderEdit | Order parameters to change
apiInstance.ordersIdJsonPut(login, authtoken, id, orderEdit, (error, data, response) => {
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
 **orderEdit** | [**OrderEdit**](OrderEdit.md)| Order parameters to change | 

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ordersJsonGet

> [Order] ordersJsonGet(login, authtoken, opts)

Retrieve all Orders.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.OrdersApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let opts = {
  'limit': 50, // Number | List restriction
  'page': 1 // Number | List page
};
apiInstance.ordersJsonGet(login, authtoken, opts, (error, data, response) => {
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

[**[Order]**](Order.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## ordersJsonPost

> Order ordersJsonPost(login, authtoken, orderCreate)

Create a new Order.

Orders created externally keep the given order product&#39;s values (bypassing internal promotion or product amounts).

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.OrdersApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let orderCreate = new JumpsellerApi.OrderCreate(); // OrderCreate | Order parameters.
apiInstance.ordersJsonPost(login, authtoken, orderCreate, (error, data, response) => {
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
 **orderCreate** | [**OrderCreate**](OrderCreate.md)| Order parameters. | 

### Return type

[**Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## ordersStatusStatusJsonGet

> [Order] ordersStatusStatusJsonGet(login, authtoken, status)

Retrieve orders filtered by status.

### Example

```javascript
import JumpsellerApi from 'jumpseller_api';

let apiInstance = new JumpsellerApi.OrdersApi();
let login = "login_example"; // String | API OAuth login.
let authtoken = "authtoken_example"; // String | API OAuth token.
let status = "status_example"; // String | Status of the Order used as filter
apiInstance.ordersStatusStatusJsonGet(login, authtoken, status, (error, data, response) => {
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
 **status** | **String**| Status of the Order used as filter | 

### Return type

[**[Order]**](Order.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

