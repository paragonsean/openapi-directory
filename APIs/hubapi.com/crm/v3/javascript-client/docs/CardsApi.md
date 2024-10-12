# CrmCards.CardsApi

All URIs are relative to *https://api.hubapi.com/crm/v3/extensions/cards*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteCrmV3ExtensionsCardsAppIdCardId**](CardsApi.md#deleteCrmV3ExtensionsCardsAppIdCardId) | **DELETE** /{appId}/{cardId} | Delete a card
[**getCrmV3ExtensionsCardsAppId**](CardsApi.md#getCrmV3ExtensionsCardsAppId) | **GET** /{appId} | Get all cards
[**getCrmV3ExtensionsCardsAppIdCardId**](CardsApi.md#getCrmV3ExtensionsCardsAppIdCardId) | **GET** /{appId}/{cardId} | Get a card.
[**patchCrmV3ExtensionsCardsAppIdCardId**](CardsApi.md#patchCrmV3ExtensionsCardsAppIdCardId) | **PATCH** /{appId}/{cardId} | Update a card
[**postCrmV3ExtensionsCardsAppId**](CardsApi.md#postCrmV3ExtensionsCardsAppId) | **POST** /{appId} | Create a new card



## deleteCrmV3ExtensionsCardsAppIdCardId

> deleteCrmV3ExtensionsCardsAppIdCardId(appId, cardId)

Delete a card

Permanently deletes a card definition with the given ID. Once deleted, data fetch requests for this card will no longer be sent to your service. This can&#39;t be undone.

### Example

```javascript
import CrmCards from 'crm_cards';
let defaultClient = CrmCards.ApiClient.instance;
// Configure API key authorization: developer_hapikey
let developer_hapikey = defaultClient.authentications['developer_hapikey'];
developer_hapikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developer_hapikey.apiKeyPrefix = 'Token';

let apiInstance = new CrmCards.CardsApi();
let appId = 56; // Number | The ID of the target app.
let cardId = "cardId_example"; // String | The ID of the card to delete.
apiInstance.deleteCrmV3ExtensionsCardsAppIdCardId(appId, cardId, (error, data, response) => {
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
 **appId** | **Number**| The ID of the target app. | 
 **cardId** | **String**| The ID of the card to delete. | 

### Return type

null (empty response body)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getCrmV3ExtensionsCardsAppId

> CardListResponse getCrmV3ExtensionsCardsAppId(appId)

Get all cards

Returns a list of cards for a given app.

### Example

```javascript
import CrmCards from 'crm_cards';
let defaultClient = CrmCards.ApiClient.instance;
// Configure API key authorization: developer_hapikey
let developer_hapikey = defaultClient.authentications['developer_hapikey'];
developer_hapikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developer_hapikey.apiKeyPrefix = 'Token';

let apiInstance = new CrmCards.CardsApi();
let appId = 56; // Number | The ID of the target app.
apiInstance.getCrmV3ExtensionsCardsAppId(appId, (error, data, response) => {
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
 **appId** | **Number**| The ID of the target app. | 

### Return type

[**CardListResponse**](CardListResponse.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## getCrmV3ExtensionsCardsAppIdCardId

> CardResponse getCrmV3ExtensionsCardsAppIdCardId(appId, cardId)

Get a card.

Returns the definition for a card with the given ID.

### Example

```javascript
import CrmCards from 'crm_cards';
let defaultClient = CrmCards.ApiClient.instance;
// Configure API key authorization: developer_hapikey
let developer_hapikey = defaultClient.authentications['developer_hapikey'];
developer_hapikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developer_hapikey.apiKeyPrefix = 'Token';

let apiInstance = new CrmCards.CardsApi();
let appId = 56; // Number | The ID of the target app.
let cardId = "cardId_example"; // String | The ID of the target card.
apiInstance.getCrmV3ExtensionsCardsAppIdCardId(appId, cardId, (error, data, response) => {
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
 **appId** | **Number**| The ID of the target app. | 
 **cardId** | **String**| The ID of the target card. | 

### Return type

[**CardResponse**](CardResponse.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*


## patchCrmV3ExtensionsCardsAppIdCardId

> CardResponse patchCrmV3ExtensionsCardsAppIdCardId(appId, cardId, cardPatchRequest)

Update a card

Update a card definition with new details.

### Example

```javascript
import CrmCards from 'crm_cards';
let defaultClient = CrmCards.ApiClient.instance;
// Configure API key authorization: developer_hapikey
let developer_hapikey = defaultClient.authentications['developer_hapikey'];
developer_hapikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developer_hapikey.apiKeyPrefix = 'Token';

let apiInstance = new CrmCards.CardsApi();
let appId = 56; // Number | The ID of the target app.
let cardId = "cardId_example"; // String | The ID of the card to update.
let cardPatchRequest = new CrmCards.CardPatchRequest(); // CardPatchRequest | Card definition fields to be updated.
apiInstance.patchCrmV3ExtensionsCardsAppIdCardId(appId, cardId, cardPatchRequest, (error, data, response) => {
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
 **appId** | **Number**| The ID of the target app. | 
 **cardId** | **String**| The ID of the card to update. | 
 **cardPatchRequest** | [**CardPatchRequest**](CardPatchRequest.md)| Card definition fields to be updated. | 

### Return type

[**CardResponse**](CardResponse.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, */*


## postCrmV3ExtensionsCardsAppId

> CardResponse postCrmV3ExtensionsCardsAppId(appId, cardCreateRequest)

Create a new card

Defines a new card that will become active on an account when this app is installed.

### Example

```javascript
import CrmCards from 'crm_cards';
let defaultClient = CrmCards.ApiClient.instance;
// Configure API key authorization: developer_hapikey
let developer_hapikey = defaultClient.authentications['developer_hapikey'];
developer_hapikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//developer_hapikey.apiKeyPrefix = 'Token';

let apiInstance = new CrmCards.CardsApi();
let appId = 56; // Number | The ID of the target app.
let cardCreateRequest = new CrmCards.CardCreateRequest(); // CardCreateRequest | The new card definition.
apiInstance.postCrmV3ExtensionsCardsAppId(appId, cardCreateRequest, (error, data, response) => {
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
 **appId** | **Number**| The ID of the target app. | 
 **cardCreateRequest** | [**CardCreateRequest**](CardCreateRequest.md)| The new card definition. | 

### Return type

[**CardResponse**](CardResponse.md)

### Authorization

[developer_hapikey](../README.md#developer_hapikey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, */*

