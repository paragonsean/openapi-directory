# HandwryttenApi.CardsApi

All URIs are relative to *https://api.handwrytten.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filterableCardDetails**](CardsApi.md#filterableCardDetails) | **POST** /cards/view | Provides full information on a specific card
[**listCards**](CardsApi.md#listCards) | **POST** /cards/list | Lists information on cards
[**simpleListCards**](CardsApi.md#simpleListCards) | **GET** /cards/list | Lists information on cards



## filterableCardDetails

> CardDetails filterableCardDetails(opts)

Provides full information on a specific card

Full card details

### Example

```javascript
import HandwryttenApi from 'handwrytten_api';

let apiInstance = new HandwryttenApi.CardsApi();
let opts = {
  'body': new HandwryttenApi.FilterableCardDetailsRequest() // FilterableCardDetailsRequest | additional parameters
};
apiInstance.filterableCardDetails(opts, (error, data, response) => {
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
 **body** | [**FilterableCardDetailsRequest**](FilterableCardDetailsRequest.md)| additional parameters | [optional] 

### Return type

[**CardDetails**](CardDetails.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listCards

> [Card] listCards(opts)

Lists information on cards

Simple listing of cards.  No filters can be applied.

### Example

```javascript
import HandwryttenApi from 'handwrytten_api';

let apiInstance = new HandwryttenApi.CardsApi();
let opts = {
  'body': new HandwryttenApi.ListCardsRequest() // ListCardsRequest | additional parameters
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
 **body** | [**ListCardsRequest**](ListCardsRequest.md)| additional parameters | [optional] 

### Return type

[**[Card]**](Card.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## simpleListCards

> [Card] simpleListCards()

Lists information on cards

Filterable card list.  If called with UID will also provide user-specific cards.

### Example

```javascript
import HandwryttenApi from 'handwrytten_api';

let apiInstance = new HandwryttenApi.CardsApi();
apiInstance.simpleListCards((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Card]**](Card.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

