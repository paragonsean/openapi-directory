# Suggestions.MatchReceivedSKUsApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**match**](MatchReceivedSKUsApi.md#match) | **PUT** /suggestions/{sellerId}/{sellerskuid}/versions/{version}/matches/{matchid} | Match Received SKUs individually
[**matchMultiple**](MatchReceivedSKUsApi.md#matchMultiple) | **PUT** /suggestions/matches/action/{actionName} | Match Multiple Received SKUs



## match

> match(accountName, accept, contentType, sellerId, sellerskuid, version, matchid, matchRequest)

Match Received SKUs individually

All SKUs sent from a seller to a marketplace must be reviewed and matched. Actions in the matching process are added in the request body through the [matchType] object. Match type actions include:   1. &#x60;newproduct&#x60;: match the SKU as a new product.   2. &#x60;itemMatch&#x60;: associate the received SKU to an existing SKU.   3. &#x60;productMatch&#x60;: associate the received SKU to an existing product.   4. &#x60;deny&#x60;: deny the received SKU.   5. &#x60;pending&#x60;: the received SKU requires attention.   6. &#x60;incomplete&#x60;: the received SKU is lacking information to be matched.   7. &#x60;insufficientScore&#x60;: the score given by the Matcher to this received SKU doesn&#39;t qualify it to be matched.   Note that  if the autoApprove setting is enabled, the SKUs will be approved, regardless of the Score.

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

let apiInstance = new Suggestions.MatchReceivedSKUsApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account. Used as part of the URL
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let sellerId = "'seller123'"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built.
let sellerskuid = "'1234'"; // String | A string that identifies the SKU in the marketplace. This is the ID that the marketplace will use for future references to this SKU, such as price and inventory notifications.
let version = "'09072021142808277'"; // String | Whenever an SKU Suggestion is updated or changed, a new version of the original one is created. All versions are logged, so you can search for previous our current states of SKU suggestions. This field is the versionId associated to the version you choose to search for. You can get this field's value through the[Get SKU Suggestion by ID](https://developers.vtex.com/vtex-rest-api/reference/getsuggestion). through the `latestVersionId` field.
let matchid = "matchid_example"; // String | Whenever an SKU suggestion is matched, it is associated to a unique ID. Fill in this field with the matchId you wish to filter by. The `matchId`'s value can be obtained through the *[Get SKU Suggestion by ID](https://developers.vtex.com/vtex-rest-api/reference/getsuggestion) endpoint.
let matchRequest = {"matchType":"itemMatch","matcherId":"{{matcherid}}","product":{"brandId":1234567,"categoryId":12,"description":"Book description","matchType":"itemMatch","name":"Book A","specifications":null},"productRef":"{{productRef}}(should be specified when match is a product match)","score":"{{score}} (must be decimal)","sku":{"eans":["12345678901213"],"height":1,"images":[{"imagem1.jpg":{"imagem1.jpg":"https://imageurl.example"}}],"length":1,"measurementUnit":"un","name":"Sku exemplo","refId":null,"specifications":{"Embalagem":"3 k   g"},"unitMultiplier":1,"weight":1,"width":1},"skuRef":"{{skuid}}(should be specifed when match is a sku match)"}; // MatchRequest | 
apiInstance.match(accountName, accept, contentType, sellerId, sellerskuid, version, matchid, matchRequest, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace and informed to the seller before the integration is built. | [default to &#39;seller123&#39;]
 **sellerskuid** | **String**| A string that identifies the SKU in the marketplace. This is the ID that the marketplace will use for future references to this SKU, such as price and inventory notifications. | [default to &#39;1234&#39;]
 **version** | **String**| Whenever an SKU Suggestion is updated or changed, a new version of the original one is created. All versions are logged, so you can search for previous our current states of SKU suggestions. This field is the versionId associated to the version you choose to search for. You can get this field&#39;s value through the[Get SKU Suggestion by ID](https://developers.vtex.com/vtex-rest-api/reference/getsuggestion). through the &#x60;latestVersionId&#x60; field. | [default to &#39;09072021142808277&#39;]
 **matchid** | **String**| Whenever an SKU suggestion is matched, it is associated to a unique ID. Fill in this field with the matchId you wish to filter by. The &#x60;matchId&#x60;&#39;s value can be obtained through the *[Get SKU Suggestion by ID](https://developers.vtex.com/vtex-rest-api/reference/getsuggestion) endpoint. | 
 **matchRequest** | [**MatchRequest**](MatchRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## matchMultiple

> matchMultiple(accountName, contentType, accept, actionName, requestBody)

Match Multiple Received SKUs

This endpoint allows the user to bulk approve, deny, or associate received SKUs. In a single request, you can match up to 25 received SKUs from your sellers.  Through the &#x60;actionName&#x60; attribute you can select the operation you want to apply to the received SKU.   Actions include:   1. &#x60;newproduct&#x60;: match the SKU as a new product.   2. &#x60;skuassociation&#x60;: associate the received SKU to an existing SKU.   3. &#x60;productassociation&#x60;: associate the received SKU to an existing product.   4. &#x60;deny&#x60;: deny the received SKU.

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

let apiInstance = new Suggestions.MatchReceivedSKUsApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account. Used as part of the URL
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let actionName = "'newprodcut'"; // String | This field refers to the operation you choose to apply to received SKUs. Values include: newproduct, skuassociation, productassociation or deny.
let requestBody = [null]; // [Array] | 
apiInstance.matchMultiple(accountName, contentType, accept, actionName, requestBody, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]
 **actionName** | **String**| This field refers to the operation you choose to apply to received SKUs. Values include: newproduct, skuassociation, productassociation or deny. | [default to &#39;newprodcut&#39;]
 **requestBody** | [**[Array]**](Array.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

