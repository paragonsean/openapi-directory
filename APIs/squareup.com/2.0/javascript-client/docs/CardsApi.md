# SquareConnectApi.CardsApi

All URIs are relative to *https://connect.squareup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createCard**](CardsApi.md#createCard) | **POST** /v2/cards | CreateCard
[**disableCard**](CardsApi.md#disableCard) | **POST** /v2/cards/{card_id}/disable | DisableCard
[**listCards**](CardsApi.md#listCards) | **GET** /v2/cards | ListCards
[**retrieveCard**](CardsApi.md#retrieveCard) | **GET** /v2/cards/{card_id} | RetrieveCard



## createCard

> CreateCardResponse createCard(createCardRequest)

CreateCard

Adds a card on file to an existing merchant.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CardsApi();
let createCardRequest = new SquareConnectApi.CreateCardRequest(); // CreateCardRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
apiInstance.createCard(createCardRequest, (error, data, response) => {
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
 **createCardRequest** | [**CreateCardRequest**](CreateCardRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | 

### Return type

[**CreateCardResponse**](CreateCardResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## disableCard

> DisableCardResponse disableCard(cardId)

DisableCard

Disables the card, preventing any further updates or charges. Disabling an already disabled card is allowed but has no effect.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CardsApi();
let cardId = "cardId_example"; // String | Unique ID for the desired Card.
apiInstance.disableCard(cardId, (error, data, response) => {
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
 **cardId** | **String**| Unique ID for the desired Card. | 

### Return type

[**DisableCardResponse**](DisableCardResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCards

> ListCardsResponse listCards(opts)

ListCards

Retrieves a list of cards owned by the account making the request. A max of 25 cards will be returned.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CardsApi();
let opts = {
  'cursor': "cursor_example", // String | A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for your original query.  See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information.
  'customerId': "customerId_example", // String | Limit results to cards associated with the customer supplied. By default, all cards owned by the merchant are returned.
  'includeDisabled': true, // Boolean | Includes disabled cards. By default, all enabled cards owned by the merchant are returned.
  'referenceId': "referenceId_example", // String | Limit results to cards associated with the reference_id supplied.
  'sortOrder': "sortOrder_example" // String | Sorts the returned list by when the card was created with the specified order. This field defaults to ASC.
};
apiInstance.listCards(opts, (error, data, response) => {
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
 **cursor** | **String**| A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for your original query.  See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information. | [optional] 
 **customerId** | **String**| Limit results to cards associated with the customer supplied. By default, all cards owned by the merchant are returned. | [optional] 
 **includeDisabled** | **Boolean**| Includes disabled cards. By default, all enabled cards owned by the merchant are returned. | [optional] 
 **referenceId** | **String**| Limit results to cards associated with the reference_id supplied. | [optional] 
 **sortOrder** | **String**| Sorts the returned list by when the card was created with the specified order. This field defaults to ASC. | [optional] 

### Return type

[**ListCardsResponse**](ListCardsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveCard

> RetrieveCardResponse retrieveCard(cardId)

RetrieveCard

Retrieves details for a specific Card.

### Example

```javascript
import SquareConnectApi from 'square_connect_api';
let defaultClient = SquareConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SquareConnectApi.CardsApi();
let cardId = "cardId_example"; // String | Unique ID for the desired Card.
apiInstance.retrieveCard(cardId, (error, data, response) => {
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
 **cardId** | **String**| Unique ID for the desired Card. | 

### Return type

[**RetrieveCardResponse**](RetrieveCardResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

