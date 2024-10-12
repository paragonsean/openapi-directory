# FireFinancialServicesBusinessApi.CardsApi

All URIs are relative to *https://api.fire.com/business*

Method | HTTP request | Description
------------- | ------------- | -------------
[**blockCard**](CardsApi.md#blockCard) | **POST** /v1/cards/{cardId}/block | Block a card
[**createNewCard**](CardsApi.md#createNewCard) | **POST** /v1/cards | Create a new debit card.
[**getListofCardTransactions**](CardsApi.md#getListofCardTransactions) | **GET** /v1/cards/{cardId}/transactions | List Card Transactions.
[**getListofCards**](CardsApi.md#getListofCards) | **GET** /v1/cards | View List of Cards.
[**unblockCard**](CardsApi.md#unblockCard) | **POST** /v1/cards/{cardId}/unblock | Unblock a card



## blockCard

> blockCard(cardId)

Block a card

Updates status of an existing card to block which prevents any transactions being carried out with that card.

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.CardsApi();
let cardId = 789; // Number | 
apiInstance.blockCard(cardId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cardId** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## createNewCard

> NewCardResponse createNewCard(newCard)

Create a new debit card.

You can create multiple debit cards which can be linked to your fire.com accounts.

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.CardsApi();
let newCard = new FireFinancialServicesBusinessApi.NewCard(); // NewCard | Details of the new card
apiInstance.createNewCard(newCard, (error, data, response) => {
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
 **newCard** | [**NewCard**](NewCard.md)| Details of the new card | 

### Return type

[**NewCardResponse**](NewCardResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getListofCardTransactions

> [CardTransactionsv1] getListofCardTransactions(cardId, opts)

List Card Transactions.

Returns a list of cards transactions related to your fire.com card.

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.CardsApi();
let cardId = 789; // Number | 
let opts = {
  'limit': 789, // Number | 
  'offset': 789 // Number | 
};
apiInstance.getListofCardTransactions(cardId, opts, (error, data, response) => {
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
 **cardId** | **Number**|  | 
 **limit** | **Number**|  | [optional] 
 **offset** | **Number**|  | [optional] 

### Return type

[**[CardTransactionsv1]**](CardTransactionsv1.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getListofCards

> Cards getListofCards()

View List of Cards.

Returns a list of cards related to your fire.com account.

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.CardsApi();
apiInstance.getListofCards((error, data, response) => {
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

[**Cards**](Cards.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## unblockCard

> unblockCard(cardId)

Unblock a card

Updates status of an existing card to unblock which means that transactions can be carried out with that card.

### Example

```javascript
import FireFinancialServicesBusinessApi from 'fire_financial_services_business_api';
let defaultClient = FireFinancialServicesBusinessApi.ApiClient.instance;
// Configure Bearer (API Access Token) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new FireFinancialServicesBusinessApi.CardsApi();
let cardId = 789; // Number | 
apiInstance.unblockCard(cardId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cardId** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

