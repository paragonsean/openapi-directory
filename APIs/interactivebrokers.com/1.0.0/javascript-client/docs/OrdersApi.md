# Ibkr3rdPartyWebApi.OrdersApi

All URIs are relative to *https://www.interactivebrokers.com/tradingapi/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountsAccountOrdersCustomerOrderIdDelete**](OrdersApi.md#accountsAccountOrdersCustomerOrderIdDelete) | **DELETE** /accounts/{account}/orders/{CustomerOrderId} | Cancel Order
[**accountsAccountOrdersCustomerOrderIdGet**](OrdersApi.md#accountsAccountOrdersCustomerOrderIdGet) | **GET** /accounts/{account}/orders/{CustomerOrderId} | Return specific order info
[**accountsAccountOrdersCustomerOrderIdPut**](OrdersApi.md#accountsAccountOrdersCustomerOrderIdPut) | **PUT** /accounts/{account}/orders/{CustomerOrderId} | Modify Order
[**accountsAccountOrdersGet**](OrdersApi.md#accountsAccountOrdersGet) | **GET** /accounts/{account}/orders | Open Orders
[**accountsAccountOrdersPost**](OrdersApi.md#accountsAccountOrdersPost) | **POST** /accounts/{account}/orders | Place Order



## accountsAccountOrdersCustomerOrderIdDelete

> [AccountsAccountOrdersCustomerOrderIdPut200ResponseInner] accountsAccountOrdersCustomerOrderIdDelete(account, customerOrderId)

Cancel Order

Cancels the order with the referenced Customer Order ID for the account passed in the URL.

### Example

```javascript
import Ibkr3rdPartyWebApi from 'ibkr_3rd_party_web_api';
let defaultClient = Ibkr3rdPartyWebApi.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications['cookieAuth'];
cookieAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';

let apiInstance = new Ibkr3rdPartyWebApi.OrdersApi();
let account = "account_example"; // String | Account Number
let customerOrderId = "customerOrderId_example"; // String | Customer Order ID
apiInstance.accountsAccountOrdersCustomerOrderIdDelete(account, customerOrderId, (error, data, response) => {
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
 **account** | **String**| Account Number | 
 **customerOrderId** | **String**| Customer Order ID | 

### Return type

[**[AccountsAccountOrdersCustomerOrderIdPut200ResponseInner]**](AccountsAccountOrdersCustomerOrderIdPut200ResponseInner.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsAccountOrdersCustomerOrderIdGet

> [OrderState] accountsAccountOrdersCustomerOrderIdGet(account, customerOrderId)

Return specific order info

Returns the order with the referenced Customer Order ID for the account passed in the URL.

### Example

```javascript
import Ibkr3rdPartyWebApi from 'ibkr_3rd_party_web_api';
let defaultClient = Ibkr3rdPartyWebApi.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications['cookieAuth'];
cookieAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';

let apiInstance = new Ibkr3rdPartyWebApi.OrdersApi();
let account = "account_example"; // String | Account Number
let customerOrderId = "customerOrderId_example"; // String | Customer Order ID
apiInstance.accountsAccountOrdersCustomerOrderIdGet(account, customerOrderId, (error, data, response) => {
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
 **account** | **String**| Account Number | 
 **customerOrderId** | **String**| Customer Order ID | 

### Return type

[**[OrderState]**](OrderState.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsAccountOrdersCustomerOrderIdPut

> [AccountsAccountOrdersCustomerOrderIdPut200ResponseInner] accountsAccountOrdersCustomerOrderIdPut(account, customerOrderId, accountsAccountOrdersCustomerOrderIdPutRequest)

Modify Order

Allows the caller to modify the order with the referenced Customer Order ID specified in the URL. A separate Customer Order ID must be provided in the request body for the modification.

### Example

```javascript
import Ibkr3rdPartyWebApi from 'ibkr_3rd_party_web_api';
let defaultClient = Ibkr3rdPartyWebApi.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications['cookieAuth'];
cookieAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';

let apiInstance = new Ibkr3rdPartyWebApi.OrdersApi();
let account = "account_example"; // String | Account Number
let customerOrderId = "customerOrderId_example"; // String | Customer Order ID
let accountsAccountOrdersCustomerOrderIdPutRequest = new Ibkr3rdPartyWebApi.AccountsAccountOrdersCustomerOrderIdPutRequest(); // AccountsAccountOrdersCustomerOrderIdPutRequest | Order Parameters
apiInstance.accountsAccountOrdersCustomerOrderIdPut(account, customerOrderId, accountsAccountOrdersCustomerOrderIdPutRequest, (error, data, response) => {
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
 **account** | **String**| Account Number | 
 **customerOrderId** | **String**| Customer Order ID | 
 **accountsAccountOrdersCustomerOrderIdPutRequest** | [**AccountsAccountOrdersCustomerOrderIdPutRequest**](AccountsAccountOrdersCustomerOrderIdPutRequest.md)| Order Parameters | 

### Return type

[**[AccountsAccountOrdersCustomerOrderIdPut200ResponseInner]**](AccountsAccountOrdersCustomerOrderIdPut200ResponseInner.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## accountsAccountOrdersGet

> [OrderState] accountsAccountOrdersGet(account)

Open Orders

Returns a list of orders for the account passed in the URL

### Example

```javascript
import Ibkr3rdPartyWebApi from 'ibkr_3rd_party_web_api';
let defaultClient = Ibkr3rdPartyWebApi.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications['cookieAuth'];
cookieAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';

let apiInstance = new Ibkr3rdPartyWebApi.OrdersApi();
let account = "account_example"; // String | Account Number
apiInstance.accountsAccountOrdersGet(account, (error, data, response) => {
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
 **account** | **String**| Account Number | 

### Return type

[**[OrderState]**](OrderState.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsAccountOrdersPost

> [OrderState] accountsAccountOrdersPost(account, accountsAccountOrdersPostRequest)

Place Order

Places order

### Example

```javascript
import Ibkr3rdPartyWebApi from 'ibkr_3rd_party_web_api';
let defaultClient = Ibkr3rdPartyWebApi.ApiClient.instance;
// Configure API key authorization: cookieAuth
let cookieAuth = defaultClient.authentications['cookieAuth'];
cookieAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//cookieAuth.apiKeyPrefix = 'Token';

let apiInstance = new Ibkr3rdPartyWebApi.OrdersApi();
let account = "account_example"; // String | Account Number
let accountsAccountOrdersPostRequest = new Ibkr3rdPartyWebApi.AccountsAccountOrdersPostRequest(); // AccountsAccountOrdersPostRequest | Order Parameters
apiInstance.accountsAccountOrdersPost(account, accountsAccountOrdersPostRequest, (error, data, response) => {
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
 **account** | **String**| Account Number | 
 **accountsAccountOrdersPostRequest** | [**AccountsAccountOrdersPostRequest**](AccountsAccountOrdersPostRequest.md)| Order Parameters | 

### Return type

[**[OrderState]**](OrderState.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

