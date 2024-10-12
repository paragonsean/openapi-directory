# GiftCardApi.TransactionApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelGiftCardTransaction**](TransactionApi.md#cancelGiftCardTransaction) | **POST** /giftcards/{giftCardID}/transactions/{transactionID}/cancellations | Cancel GiftCard Transaction
[**createGiftCardTransaction**](TransactionApi.md#createGiftCardTransaction) | **POST** /giftcards/{giftCardID}/transactions | Create GiftCard Transaction
[**getGiftCardTransactionbyID**](TransactionApi.md#getGiftCardTransactionbyID) | **GET** /giftcards/{giftCardID}/transactions/{transactionID} | Get GiftCard Transaction by ID
[**getGiftCardTransactions**](TransactionApi.md#getGiftCardTransactions) | **GET** /giftcards/{giftCardID}/transactions | Get GiftCard Transactions
[**getTransactionAuthorizations**](TransactionApi.md#getTransactionAuthorizations) | **GET** /giftcards/{giftCardID}/transactions/{transactionID}/authorization | Get Transaction Authorizations
[**getTransactionCancellations**](TransactionApi.md#getTransactionCancellations) | **GET** /giftcards/{giftCardID}/transactions/{transactionID}/cancellations | Get Transaction Cancellations
[**getTransactionSettlements**](TransactionApi.md#getTransactionSettlements) | **GET** /giftcards/{giftCardID}/transactions/{transactionID}/settlements | Get Transaction Settlements
[**settleGiftCardTransaction**](TransactionApi.md#settleGiftCardTransaction) | **POST** /giftcards/{giftCardID}/transactions/{transactionID}/settlements | Settle GiftCard Transaction



## cancelGiftCardTransaction

> Response6 cancelGiftCardTransaction(accept, contentType, giftCardID, transactionID, cancelGiftCardTransactionRequest)

Cancel GiftCard Transaction

Creates a cancellation in the transaction. Cancel a item reservation or create a refund.

### Example

```javascript
import GiftCardApi from 'gift_card_api';
let defaultClient = GiftCardApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new GiftCardApi.TransactionApi();
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let giftCardID = "'6'"; // String | 
let transactionID = "'b476900c'"; // String | 
let cancelGiftCardTransactionRequest = {"requestId":"6360f","value":13}; // CancelGiftCardTransactionRequest | 
apiInstance.cancelGiftCardTransaction(accept, contentType, giftCardID, transactionID, cancelGiftCardTransactionRequest, (error, data, response) => {
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
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **giftCardID** | **String**|  | [default to &#39;6&#39;]
 **transactionID** | **String**|  | [default to &#39;b476900c&#39;]
 **cancelGiftCardTransactionRequest** | [**CancelGiftCardTransactionRequest**](CancelGiftCardTransactionRequest.md)|  | 

### Return type

[**Response6**](Response6.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createGiftCardTransaction

> Response3 createGiftCardTransaction(accept, contentType, giftCardID, opts)

Create GiftCard Transaction

Register a new giftcard transaction and authorize the item reservation.

### Example

```javascript
import GiftCardApi from 'gift_card_api';
let defaultClient = GiftCardApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new GiftCardApi.TransactionApi();
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let giftCardID = "'7'"; // String | 
let opts = {
  'createGiftCardTransactionRequest': {"description":"GiftCardHub","operation":"Debit","orderInfo":{"cart":{"discounts":-7.5,"grandTotal":0,"items":[{"discount":-7.5,"id":"2001023","name":"Vaporizador Des. ColC4nia Branco","price":14.99,"priceTags":[{"name":"discount@price-discount_store_183#4911bf6f-22a2-4af1-a365-cce895c3df2c","value":0}],"productId":"2000492","quantity":1,"refId":"35994","shippingDiscount":0,"value":14.99}],"itemsTotal":14.99,"shipping":7.27,"taxes":0},"clientProfile":{"birthDate":"0001-01-01T00:00:00","document":"02906792063","email":"miguel.scott96@yahoo.com.br","firstName":"miguel","isCorporate":false,"lastName":"scott","phone":"+551111111111","profileId":"92de2449-0e02-4ca9-a4aa-a09cc9d8f7ff"},"orderId":"v5006128str","sequence":5006128,"shipping":{"city":"Rio de Janeiro","complement":null,"country":"BRA","neighborhood":"Botafogo","number":"111","postalCode":"22250040","receiverName":"miguel scott","reference":null,"state":"RJ","street":"Praia de Botafogo"}},"redemptionCode":"","redemptionToken":"b2dac6f2-f365-48cd-82a9-0b376a55557a","requestId":"B56CBE231DEE4E1A859183C1030CE926","value":3} // CreateGiftCardTransactionRequest | 
};
apiInstance.createGiftCardTransaction(accept, contentType, giftCardID, opts, (error, data, response) => {
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
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **giftCardID** | **String**|  | [default to &#39;7&#39;]
 **createGiftCardTransactionRequest** | [**CreateGiftCardTransactionRequest**](CreateGiftCardTransactionRequest.md)|  | [optional] 

### Return type

[**Response3**](Response3.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getGiftCardTransactionbyID

> Response5 getGiftCardTransactionbyID(accept, contentType, giftCardID, transactionID)

Get GiftCard Transaction by ID



### Example

```javascript
import GiftCardApi from 'gift_card_api';
let defaultClient = GiftCardApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new GiftCardApi.TransactionApi();
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let giftCardID = "'6'"; // String | 
let transactionID = "'b47690'"; // String | 
apiInstance.getGiftCardTransactionbyID(accept, contentType, giftCardID, transactionID, (error, data, response) => {
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
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **giftCardID** | **String**|  | [default to &#39;6&#39;]
 **transactionID** | **String**|  | [default to &#39;b47690&#39;]

### Return type

[**Response5**](Response5.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGiftCardTransactions

> [Response3] getGiftCardTransactions(accept, contentType, giftCardID)

Get GiftCard Transactions

Returns all transaction of a giftcard.

### Example

```javascript
import GiftCardApi from 'gift_card_api';
let defaultClient = GiftCardApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new GiftCardApi.TransactionApi();
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let giftCardID = "'2'"; // String | 
apiInstance.getGiftCardTransactions(accept, contentType, giftCardID, (error, data, response) => {
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
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **giftCardID** | **String**|  | [default to &#39;2&#39;]

### Return type

[**[Response3]**](Response3.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTransactionAuthorizations

> Response6 getTransactionAuthorizations(accept, contentType, giftCardID, transactionID)

Get Transaction Authorizations

Returns the giftcard transaction authorizations.

### Example

```javascript
import GiftCardApi from 'gift_card_api';
let defaultClient = GiftCardApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new GiftCardApi.TransactionApi();
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let giftCardID = "'6'"; // String | 
let transactionID = "'b47690'"; // String | 
apiInstance.getTransactionAuthorizations(accept, contentType, giftCardID, transactionID, (error, data, response) => {
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
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **giftCardID** | **String**|  | [default to &#39;6&#39;]
 **transactionID** | **String**|  | [default to &#39;b47690&#39;]

### Return type

[**Response6**](Response6.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTransactionCancellations

> [Response7] getTransactionCancellations(accept, contentType, giftCardID, transactionID)

Get Transaction Cancellations

Returns the giftcard transaction cancellations.

### Example

```javascript
import GiftCardApi from 'gift_card_api';
let defaultClient = GiftCardApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new GiftCardApi.TransactionApi();
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let giftCardID = "'6'"; // String | 
let transactionID = "'b47690'"; // String | 
apiInstance.getTransactionCancellations(accept, contentType, giftCardID, transactionID, (error, data, response) => {
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
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **giftCardID** | **String**|  | [default to &#39;6&#39;]
 **transactionID** | **String**|  | [default to &#39;b47690&#39;]

### Return type

[**[Response7]**](Response7.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTransactionSettlements

> [Response6] getTransactionSettlements(accept, contentType, giftCardID, transactionID)

Get Transaction Settlements

Returns the giftcard transaction settlements.

### Example

```javascript
import GiftCardApi from 'gift_card_api';
let defaultClient = GiftCardApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new GiftCardApi.TransactionApi();
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let giftCardID = "'7'"; // String | 
let transactionID = "'b47690'"; // String | 
apiInstance.getTransactionSettlements(accept, contentType, giftCardID, transactionID, (error, data, response) => {
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
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **giftCardID** | **String**|  | [default to &#39;7&#39;]
 **transactionID** | **String**|  | [default to &#39;b47690&#39;]

### Return type

[**[Response6]**](Response6.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## settleGiftCardTransaction

> Response6 settleGiftCardTransaction(accept, contentType, giftCardID, transactionID, settleGiftCardTransactionRequest)

Settle GiftCard Transaction

Creates a giftcard transaction settlement.

### Example

```javascript
import GiftCardApi from 'gift_card_api';
let defaultClient = GiftCardApi.ApiClient.instance;
// Configure API key authorization: appToken
let appToken = defaultClient.authentications['appToken'];
appToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appToken.apiKeyPrefix = 'Token';
// Configure API key authorization: appKey
let appKey = defaultClient.authentications['appKey'];
appKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//appKey.apiKeyPrefix = 'Token';

let apiInstance = new GiftCardApi.TransactionApi();
let accept = "'application/json'"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
let contentType = "'application/json'"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
let giftCardID = "'6'"; // String | 
let transactionID = "'b47690'"; // String | 
let settleGiftCardTransactionRequest = {"requestId":"6360f98eb0cf6fd5afa77e39bba8c20fe5807d8c","value":17.4}; // SettleGiftCardTransactionRequest | 
apiInstance.settleGiftCardTransaction(accept, contentType, giftCardID, transactionID, settleGiftCardTransactionRequest, (error, data, response) => {
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
 **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to &#39;application/json&#39;]
 **giftCardID** | **String**|  | [default to &#39;6&#39;]
 **transactionID** | **String**|  | [default to &#39;b47690&#39;]
 **settleGiftCardTransactionRequest** | [**SettleGiftCardTransactionRequest**](SettleGiftCardTransactionRequest.md)|  | 

### Return type

[**Response6**](Response6.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

