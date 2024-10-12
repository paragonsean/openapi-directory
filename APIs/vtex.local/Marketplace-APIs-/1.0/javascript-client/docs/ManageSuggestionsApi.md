# Suggestions.ManageSuggestionsApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteSuggestion**](ManageSuggestionsApi.md#deleteSuggestion) | **DELETE** /suggestions/{sellerId}/{sellerSkuId} | Delete SKU Suggestion
[**saveSuggestion**](ManageSuggestionsApi.md#saveSuggestion) | **PUT** /suggestions/{sellerId}/{sellerSkuId} | Send SKU Suggestion



## deleteSuggestion

> deleteSuggestion(accountName, accept, contentType, sellerId, sellerSkuId)

Delete SKU Suggestion

This endpoint deletes a chosen SKU suggestion. Only one SKU should be deleted per request. This request cannot be undone. A workaround to revert its action, is to send the suggestion again, through the Send Suggestion API.

### Example

```javascript
import Suggestions from 'suggestions';
let defaultClient = Suggestions.ApiClient.instance;
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

let apiInstance = new Suggestions.ManageSuggestionsApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account. Used as part of the URL.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let sellerId = "'seller123'"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built.
let sellerSkuId = "'1234'"; // String | A string that identifies the SKU in the marketplace. This is the ID that the marketplace will use for future references to this SKU, such as price and inventory notifications.
apiInstance.deleteSuggestion(accountName, accept, contentType, sellerId, sellerSkuId, (error, data, response) => {
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
 **accountName** | **String**| Name of the VTEX account. Used as part of the URL. | [default to &#39;apiexamples&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built. | [default to &#39;seller123&#39;]
 **sellerSkuId** | **String**| A string that identifies the SKU in the marketplace. This is the ID that the marketplace will use for future references to this SKU, such as price and inventory notifications. | [default to &#39;1234&#39;]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## saveSuggestion

> saveSuggestion(accountName, accept, contentType, sellerId, sellerSkuId, saveSuggestionRequest)

Send SKU Suggestion

This request is used by the seller when it wants to suggest that one of their SKUs is sold in the marketplace.  Before using this request, the seller should always use the [Change Notification](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-seller-sku-notification) request in order to check if the SKU already exists in the marketplace. If it doesn&#39;t, then this is the next call in the SKU integration flow.  In the Send Suggestion request, the seller must send information about the SKU, such as the product and SKU name, the seller ID, and the image URL. All parameters are explained below. 

### Example

```javascript
import Suggestions from 'suggestions';
let defaultClient = Suggestions.ApiClient.instance;
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

let apiInstance = new Suggestions.ManageSuggestionsApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account to which the seller wants to suggest a new SKU. It is used as part of the request URL.
let accept = "application/vnd.vtex.suggestion.v0+json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let sellerId = "'seller123'"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built.
let sellerSkuId = "'1234'"; // String | A string that identifies the SKU in the seller. This is the ID that the marketplace will use for future references to this SKU, such as price and inventory notifications.
let saveSuggestionRequest = {"AvailableQuantity":111,"BrandName":"Brand 1","CategoryFullPath":"Category 1","EAN":"EAN123","Height":1,"Images":[{"imageName":"Principal","imageUrl":"https://i.pinimg.com/originals/2d/96/4a/2d964a6bf37d9224d0615dc85fccdd62.jpg"}],"Length":1,"MeasurementUnit":"un","NameComplete":"Complete product name","Pricing":{"Currency":"BRL","CurrencySymbol":"R$","SalePrice":399},"ProductDescription":"sample","ProductId":"321","ProductName":"Product sample","ProductSpecifications":[{"fieldName":"Fabric","fieldValues":["Cotton","Velvet"]}],"RefId":"REFID123","SellerId":"string","SellerStockKeepingUnitId":567,"SkuName":"Sku sample","SkuSpecifications":[{"fieldName":"Color","fieldValues":["Red","Blue"]}],"UnitMultiplier":1,"Updated":null,"Weight":1,"Width":1}; // SaveSuggestionRequest | 
apiInstance.saveSuggestion(accountName, accept, contentType, sellerId, sellerSkuId, saveSuggestionRequest, (error, data, response) => {
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
 **accountName** | **String**| Name of the VTEX account to which the seller wants to suggest a new SKU. It is used as part of the request URL. | [default to &#39;apiexamples&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built. | [default to &#39;seller123&#39;]
 **sellerSkuId** | **String**| A string that identifies the SKU in the seller. This is the ID that the marketplace will use for future references to this SKU, such as price and inventory notifications. | [default to &#39;1234&#39;]
 **saveSuggestionRequest** | [**SaveSuggestionRequest**](SaveSuggestionRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

