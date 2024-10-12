# SquareConnectApi.GiftCardsApi

All URIs are relative to *https://connect.squareup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createGiftCard**](GiftCardsApi.md#createGiftCard) | **POST** /v2/gift-cards | CreateGiftCard
[**linkCustomerToGiftCard**](GiftCardsApi.md#linkCustomerToGiftCard) | **POST** /v2/gift-cards/{gift_card_id}/link-customer | LinkCustomerToGiftCard
[**listGiftCards**](GiftCardsApi.md#listGiftCards) | **GET** /v2/gift-cards | ListGiftCards
[**retrieveGiftCard**](GiftCardsApi.md#retrieveGiftCard) | **GET** /v2/gift-cards/{id} | RetrieveGiftCard
[**retrieveGiftCardFromGAN**](GiftCardsApi.md#retrieveGiftCardFromGAN) | **POST** /v2/gift-cards/from-gan | RetrieveGiftCardFromGAN
[**retrieveGiftCardFromNonce**](GiftCardsApi.md#retrieveGiftCardFromNonce) | **POST** /v2/gift-cards/from-nonce | RetrieveGiftCardFromNonce
[**unlinkCustomerFromGiftCard**](GiftCardsApi.md#unlinkCustomerFromGiftCard) | **POST** /v2/gift-cards/{gift_card_id}/unlink-customer | UnlinkCustomerFromGiftCard



## createGiftCard

> CreateGiftCardResponse createGiftCard(createGiftCardRequest)

CreateGiftCard

Creates a digital gift card or registers a physical (plastic) gift card. You must activate the gift card before  it can be used for payment. For more information, see  [Selling gift cards](https://developer.squareup.com/docs/gift-cards/using-gift-cards-api#selling-square-gift-cards).

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.GiftCardsApi();
let createGiftCardRequest = new SquareConnectApi.CreateGiftCardRequest(); // CreateGiftCardRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.createGiftCard(createGiftCardRequest, (error, data, response) => {
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
 **createGiftCardRequest** | [**CreateGiftCardRequest**](CreateGiftCardRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**CreateGiftCardResponse**](CreateGiftCardResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## linkCustomerToGiftCard

> LinkCustomerToGiftCardResponse linkCustomerToGiftCard(giftCardId, linkCustomerToGiftCardRequest)

LinkCustomerToGiftCard

Links a customer to a gift card

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.GiftCardsApi();
let giftCardId = "giftCardId_example"; // String | The ID of the gift card to link.
let linkCustomerToGiftCardRequest = new SquareConnectApi.LinkCustomerToGiftCardRequest(); // LinkCustomerToGiftCardRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.linkCustomerToGiftCard(giftCardId, linkCustomerToGiftCardRequest, (error, data, response) => {
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
 **giftCardId** | **String**| The ID of the gift card to link. | 
 **linkCustomerToGiftCardRequest** | [**LinkCustomerToGiftCardRequest**](LinkCustomerToGiftCardRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**LinkCustomerToGiftCardResponse**](LinkCustomerToGiftCardResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listGiftCards

> ListGiftCardsResponse listGiftCards(opts)

ListGiftCards

Lists all gift cards. You can specify optional filters to retrieve  a subset of the gift cards.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.GiftCardsApi();
let opts = {
  'type': "type_example", // String | If a type is provided, gift cards of this type are returned  (see [GiftCardType](https://developer.squareup.com/reference/square_2021-08-18/enums/GiftCardType)). If no type is provided, it returns gift cards of all types.
  'state': "state_example", // String | If the state is provided, it returns the gift cards in the specified state  (see [GiftCardStatus](https://developer.squareup.com/reference/square_2021-08-18/enums/GiftCardStatus)). Otherwise, it returns the gift cards of all states.
  'limit': 56, // Number | If a value is provided, it returns only that number of results per page. The maximum number of results allowed per page is 50. The default value is 30.
  'cursor': "cursor_example", // String | A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for the original query. If a cursor is not provided, it returns the first page of the results.  For more information, see [Pagination](https://developer.squareup.com/docs/docs/working-with-apis/pagination).
  'customerId': "customerId_example" // String | If a value is provided, returns only the gift cards linked to the specified customer
};
apiInstance.listGiftCards(opts, (error, data, response) => {
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
 **type** | **String**| If a type is provided, gift cards of this type are returned  (see [GiftCardType](https://developer.squareup.com/reference/square_2021-08-18/enums/GiftCardType)). If no type is provided, it returns gift cards of all types. | [optional] 
 **state** | **String**| If the state is provided, it returns the gift cards in the specified state  (see [GiftCardStatus](https://developer.squareup.com/reference/square_2021-08-18/enums/GiftCardStatus)). Otherwise, it returns the gift cards of all states. | [optional] 
 **limit** | **Number**| If a value is provided, it returns only that number of results per page. The maximum number of results allowed per page is 50. The default value is 30. | [optional] 
 **cursor** | **String**| A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for the original query. If a cursor is not provided, it returns the first page of the results.  For more information, see [Pagination](https://developer.squareup.com/docs/docs/working-with-apis/pagination). | [optional] 
 **customerId** | **String**| If a value is provided, returns only the gift cards linked to the specified customer | [optional] 

### Return type

[**ListGiftCardsResponse**](ListGiftCardsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveGiftCard

> RetrieveGiftCardResponse retrieveGiftCard(id)

RetrieveGiftCard

Retrieves a gift card using its ID.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.GiftCardsApi();
let id = "id_example"; // String | The ID of the gift card to retrieve.
apiInstance.retrieveGiftCard(id, (error, data, response) => {
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
 **id** | **String**| The ID of the gift card to retrieve. | 

### Return type

[**RetrieveGiftCardResponse**](RetrieveGiftCardResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveGiftCardFromGAN

> RetrieveGiftCardFromGANResponse retrieveGiftCardFromGAN(retrieveGiftCardFromGANRequest)

RetrieveGiftCardFromGAN

Retrieves a gift card using the gift card account number (GAN).

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.GiftCardsApi();
let retrieveGiftCardFromGANRequest = new SquareConnectApi.RetrieveGiftCardFromGANRequest(); // RetrieveGiftCardFromGANRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.retrieveGiftCardFromGAN(retrieveGiftCardFromGANRequest, (error, data, response) => {
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
 **retrieveGiftCardFromGANRequest** | [**RetrieveGiftCardFromGANRequest**](RetrieveGiftCardFromGANRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**RetrieveGiftCardFromGANResponse**](RetrieveGiftCardFromGANResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## retrieveGiftCardFromNonce

> RetrieveGiftCardFromNonceResponse retrieveGiftCardFromNonce(retrieveGiftCardFromNonceRequest)

RetrieveGiftCardFromNonce

Retrieves a gift card using a nonce (a secure token) that represents the gift card.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.GiftCardsApi();
let retrieveGiftCardFromNonceRequest = new SquareConnectApi.RetrieveGiftCardFromNonceRequest(); // RetrieveGiftCardFromNonceRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.retrieveGiftCardFromNonce(retrieveGiftCardFromNonceRequest, (error, data, response) => {
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
 **retrieveGiftCardFromNonceRequest** | [**RetrieveGiftCardFromNonceRequest**](RetrieveGiftCardFromNonceRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**RetrieveGiftCardFromNonceResponse**](RetrieveGiftCardFromNonceResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## unlinkCustomerFromGiftCard

> UnlinkCustomerFromGiftCardResponse unlinkCustomerFromGiftCard(giftCardId, unlinkCustomerFromGiftCardRequest)

UnlinkCustomerFromGiftCard

Unlinks a customer from a gift card

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.GiftCardsApi();
let giftCardId = "giftCardId_example"; // String | 
let unlinkCustomerFromGiftCardRequest = new SquareConnectApi.UnlinkCustomerFromGiftCardRequest(); // UnlinkCustomerFromGiftCardRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.unlinkCustomerFromGiftCard(giftCardId, unlinkCustomerFromGiftCardRequest, (error, data, response) => {
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
 **giftCardId** | **String**|  | 
 **unlinkCustomerFromGiftCardRequest** | [**UnlinkCustomerFromGiftCardRequest**](UnlinkCustomerFromGiftCardRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**UnlinkCustomerFromGiftCardResponse**](UnlinkCustomerFromGiftCardResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

