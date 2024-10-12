# SquareConnectApi.TerminalApi

All URIs are relative to *https://connect.squareup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelTerminalCheckout**](TerminalApi.md#cancelTerminalCheckout) | **POST** /v2/terminals/checkouts/{checkout_id}/cancel | CancelTerminalCheckout
[**cancelTerminalRefund**](TerminalApi.md#cancelTerminalRefund) | **POST** /v2/terminals/refunds/{terminal_refund_id}/cancel | CancelTerminalRefund
[**createTerminalCheckout**](TerminalApi.md#createTerminalCheckout) | **POST** /v2/terminals/checkouts | CreateTerminalCheckout
[**createTerminalRefund**](TerminalApi.md#createTerminalRefund) | **POST** /v2/terminals/refunds | CreateTerminalRefund
[**getTerminalCheckout**](TerminalApi.md#getTerminalCheckout) | **GET** /v2/terminals/checkouts/{checkout_id} | GetTerminalCheckout
[**getTerminalRefund**](TerminalApi.md#getTerminalRefund) | **GET** /v2/terminals/refunds/{terminal_refund_id} | GetTerminalRefund
[**searchTerminalCheckouts**](TerminalApi.md#searchTerminalCheckouts) | **POST** /v2/terminals/checkouts/search | SearchTerminalCheckouts
[**searchTerminalRefunds**](TerminalApi.md#searchTerminalRefunds) | **POST** /v2/terminals/refunds/search | SearchTerminalRefunds



## cancelTerminalCheckout

> CancelTerminalCheckoutResponse cancelTerminalCheckout(checkoutId)

CancelTerminalCheckout

Cancels a Terminal checkout request if the status of the request permits it.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.TerminalApi();
let checkoutId = "checkoutId_example"; // String | The unique ID for the desired `TerminalCheckout`.
apiInstance.cancelTerminalCheckout(checkoutId, (error, data, response) => {
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
 **checkoutId** | **String**| The unique ID for the desired &#x60;TerminalCheckout&#x60;. | 

### Return type

[**CancelTerminalCheckoutResponse**](CancelTerminalCheckoutResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## cancelTerminalRefund

> CancelTerminalRefundResponse cancelTerminalRefund(terminalRefundId)

CancelTerminalRefund

Cancels an Interac Terminal refund request by refund request ID if the status of the request permits it.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.TerminalApi();
let terminalRefundId = "terminalRefundId_example"; // String | The unique ID for the desired `TerminalRefund`.
apiInstance.cancelTerminalRefund(terminalRefundId, (error, data, response) => {
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
 **terminalRefundId** | **String**| The unique ID for the desired &#x60;TerminalRefund&#x60;. | 

### Return type

[**CancelTerminalRefundResponse**](CancelTerminalRefundResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createTerminalCheckout

> CreateTerminalCheckoutResponse createTerminalCheckout(createTerminalCheckoutRequest)

CreateTerminalCheckout

Creates a Terminal checkout request and sends it to the specified device to take a payment for the requested amount.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.TerminalApi();
let createTerminalCheckoutRequest = new SquareConnectApi.CreateTerminalCheckoutRequest(); // CreateTerminalCheckoutRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.createTerminalCheckout(createTerminalCheckoutRequest, (error, data, response) => {
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
 **createTerminalCheckoutRequest** | [**CreateTerminalCheckoutRequest**](CreateTerminalCheckoutRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**CreateTerminalCheckoutResponse**](CreateTerminalCheckoutResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createTerminalRefund

> CreateTerminalRefundResponse createTerminalRefund(createTerminalRefundRequest)

CreateTerminalRefund

Creates a request to refund an Interac payment completed on a Square Terminal.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.TerminalApi();
let createTerminalRefundRequest = new SquareConnectApi.CreateTerminalRefundRequest(); // CreateTerminalRefundRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.createTerminalRefund(createTerminalRefundRequest, (error, data, response) => {
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
 **createTerminalRefundRequest** | [**CreateTerminalRefundRequest**](CreateTerminalRefundRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**CreateTerminalRefundResponse**](CreateTerminalRefundResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getTerminalCheckout

> GetTerminalCheckoutResponse getTerminalCheckout(checkoutId)

GetTerminalCheckout

Retrieves a Terminal checkout request by &#x60;checkout_id&#x60;.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.TerminalApi();
let checkoutId = "checkoutId_example"; // String | The unique ID for the desired `TerminalCheckout`.
apiInstance.getTerminalCheckout(checkoutId, (error, data, response) => {
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
 **checkoutId** | **String**| The unique ID for the desired &#x60;TerminalCheckout&#x60;. | 

### Return type

[**GetTerminalCheckoutResponse**](GetTerminalCheckoutResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTerminalRefund

> GetTerminalRefundResponse getTerminalRefund(terminalRefundId)

GetTerminalRefund

Retrieves an Interac Terminal refund object by ID.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.TerminalApi();
let terminalRefundId = "terminalRefundId_example"; // String | The unique ID for the desired `TerminalRefund`.
apiInstance.getTerminalRefund(terminalRefundId, (error, data, response) => {
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
 **terminalRefundId** | **String**| The unique ID for the desired &#x60;TerminalRefund&#x60;. | 

### Return type

[**GetTerminalRefundResponse**](GetTerminalRefundResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchTerminalCheckouts

> SearchTerminalCheckoutsResponse searchTerminalCheckouts(searchTerminalCheckoutsRequest)

SearchTerminalCheckouts

Retrieves a filtered list of Terminal checkout requests created by the account making the request.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.TerminalApi();
let searchTerminalCheckoutsRequest = new SquareConnectApi.SearchTerminalCheckoutsRequest(); // SearchTerminalCheckoutsRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.searchTerminalCheckouts(searchTerminalCheckoutsRequest, (error, data, response) => {
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
 **searchTerminalCheckoutsRequest** | [**SearchTerminalCheckoutsRequest**](SearchTerminalCheckoutsRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**SearchTerminalCheckoutsResponse**](SearchTerminalCheckoutsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchTerminalRefunds

> SearchTerminalRefundsResponse searchTerminalRefunds(searchTerminalRefundsRequest)

SearchTerminalRefunds

Retrieves a filtered list of Interac Terminal refund requests created by the seller making the request.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.TerminalApi();
let searchTerminalRefundsRequest = new SquareConnectApi.SearchTerminalRefundsRequest(); // SearchTerminalRefundsRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.searchTerminalRefunds(searchTerminalRefundsRequest, (error, data, response) => {
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
 **searchTerminalRefundsRequest** | [**SearchTerminalRefundsRequest**](SearchTerminalRefundsRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**SearchTerminalRefundsResponse**](SearchTerminalRefundsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

