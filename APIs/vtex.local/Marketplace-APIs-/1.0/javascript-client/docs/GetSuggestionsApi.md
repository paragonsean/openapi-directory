# Suggestions.GetSuggestionsApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSuggestion**](GetSuggestionsApi.md#getSuggestion) | **GET** /suggestions/{sellerId}/{sellerSkuId} | Get SKU Suggestion by ID
[**getsuggestions**](GetSuggestionsApi.md#getsuggestions) | **GET** /suggestions | Get all SKU suggestions



## getSuggestion

> getSuggestion(accountName, accept, contentType, sellerId, sellerSkuId)

Get SKU Suggestion by ID

This endpoint retrieves the data of a specific SKU sent by the seller, to the marketplace. Marketplaces or external matchers can call this endpoint when they want to check the information about a single SKU.   Note that all the information sent by the seller will be in the [content] object. All remaining information in this endpoint&#39;s response is given by the Matcher.   Matcher rates received SKUs by correlating the data sent by sellers, to existing fields in the marketplace. The calculation of these scores determines whether the product has been:   &#x60;Approved&#x60;: score equal to or greater than 80 points.   &#x60;Pending&#x60;: from 31 to 79 points.  &#x60;Denied&#x60;: from 0 to 30 points.   Note that  if the autoApprove setting is enabled, the SKUs will be approved, regardless of the Score.

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

let apiInstance = new Suggestions.GetSuggestionsApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account. Used as part of the URL
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let sellerId = "'seller123'"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built.
let sellerSkuId = "'1234'"; // String | A string that identifies the SKU in the marketplace. This is the ID that the marketplace will use for future references to this SKU, such as price and inventory notifications.
apiInstance.getSuggestion(accountName, accept, contentType, sellerId, sellerSkuId, (error, data, response) => {
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
 **accountName** | **String**| Name of the VTEX account. Used as part of the URL | [default to &#39;apiexamples&#39;]
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


## getsuggestions

> getsuggestions(accountName, accept, contentType, opts)

Get all SKU suggestions

This endpoint retrieves a list of all SKUs sent by the seller for the Marketplace&#39;s approval. Marketplace operators should use this endpoint whenever they want to check the full list of received SKUs and their  information.   Note that all the information sent by the seller will be in the [content] object. All remaining information in this endpoint&#39;s response is given by the Matcher.   Matcher rates received SKUs by correlating the data sent by sellers, to existing fields in the marketplace. The calculation of these scores determines whether the product has been:   &#x60;Approved&#x60;: score equal to or greater than 80 points.   &#x60;Pending&#x60;: from 31 to 79 points.  &#x60;Denied&#x60;: from 0 to 30 points.   Note that  if the autoApprove setting is enabled, the SKUs will be approved, regardless of the Score.

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

let apiInstance = new Suggestions.GetSuggestionsApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account. Used as part of the URL
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Type of the content being sent.
let opts = {
  'q': "", // String | This field allows you to customize your search. You can fill in this query param if you want to narrow down your search using the available filters on Received SKU modules.
  'type': "new", // String | This field allows users to filter SKU suggestions, by searching only the new suggestions that were just sent, and suggestions that have already been sent, but were updated. Possible values for this field include `new` and `update`.
  'seller': "", // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller so it can call this endpoint.
  'status': "accepted", // String | Narrow down you search, filtering by status. Values allowed on this field include: `accepted`, `pending` and `denied.`
  'hasmapping': "true", // String | This field allows you to filter SKUs that have mapping or not. Insert `true` to filter SKUs that have mapping, or `false` to retrieve SKUs that aren't mapped.
  'matcherid': "'vtex-matcher'", // String | Identifies the matching entity. It can be either VTEX's matcher, or an external matcher developed by partners, for example. The `matcherId`'s value can be obtained through the [Get SKU Suggestion by ID](https://developers.vtex.com/vtex-rest-api/reference/getsuggestion) endpoint.
  'from': 1, // Number | Define your pagination range, by adding the pagination starting value. Values should be bigger than 0, with a maximum of 50 records per page.
  'to': 50 // Number | Define your pagination range, by adding the pagination ending value. Values should be bigger than 0, with a maximum of 50 records per page.
};
apiInstance.getsuggestions(accountName, accept, contentType, opts, (error, data, response) => {
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
 **accountName** | **String**| Name of the VTEX account. Used as part of the URL | [default to &#39;apiexamples&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **q** | **String**| This field allows you to customize your search. You can fill in this query param if you want to narrow down your search using the available filters on Received SKU modules. | [optional] 
 **type** | **String**| This field allows users to filter SKU suggestions, by searching only the new suggestions that were just sent, and suggestions that have already been sent, but were updated. Possible values for this field include &#x60;new&#x60; and &#x60;update&#x60;. | [optional] 
 **seller** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller so it can call this endpoint. | [optional] 
 **status** | **String**| Narrow down you search, filtering by status. Values allowed on this field include: &#x60;accepted&#x60;, &#x60;pending&#x60; and &#x60;denied.&#x60; | [optional] 
 **hasmapping** | **String**| This field allows you to filter SKUs that have mapping or not. Insert &#x60;true&#x60; to filter SKUs that have mapping, or &#x60;false&#x60; to retrieve SKUs that aren&#39;t mapped. | [optional] 
 **matcherid** | **String**| Identifies the matching entity. It can be either VTEX&#39;s matcher, or an external matcher developed by partners, for example. The &#x60;matcherId&#x60;&#39;s value can be obtained through the [Get SKU Suggestion by ID](https://developers.vtex.com/vtex-rest-api/reference/getsuggestion) endpoint. | [optional] [default to &#39;vtex-matcher&#39;]
 **from** | **Number**| Define your pagination range, by adding the pagination starting value. Values should be bigger than 0, with a maximum of 50 records per page. | [optional] [default to 1]
 **to** | **Number**| Define your pagination range, by adding the pagination ending value. Values should be bigger than 0, with a maximum of 50 records per page. | [optional] [default to 50]

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

