# HandwryttenApi.GiftCardsApi

All URIs are relative to *https://api.handwrytten.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getGiftCardDetails**](GiftCardsApi.md#getGiftCardDetails) | **GET** /giftCards/view | Lists information on gift cards
[**giftCardDetails**](GiftCardsApi.md#giftCardDetails) | **POST** /giftCards/view | Lists information on gift cards



## getGiftCardDetails

> [GiftCard] getGiftCardDetails()

Lists information on gift cards

Returns images and details (and associated denominations) of all gift cards

### Example

```javascript
import HandwryttenApi from 'handwrytten_api';

let apiInstance = new HandwryttenApi.GiftCardsApi();
apiInstance.getGiftCardDetails((error, data, response) => {
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

[**[GiftCard]**](GiftCard.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## giftCardDetails

> [GiftCard] giftCardDetails()

Lists information on gift cards

Returns images and details (and associated denominations) of all gift cards

### Example

```javascript
import HandwryttenApi from 'handwrytten_api';

let apiInstance = new HandwryttenApi.GiftCardsApi();
apiInstance.giftCardDetails((error, data, response) => {
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

[**[GiftCard]**](GiftCard.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

