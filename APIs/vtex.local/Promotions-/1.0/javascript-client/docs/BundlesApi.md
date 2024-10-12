# PromotionsTaxesApi.BundlesApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculatediscountsandtaxesBundles**](BundlesApi.md#calculatediscountsandtaxesBundles) | **POST** /pub/bundles | Calculate discounts and taxes (Bundles)



## calculatediscountsandtaxesBundles

> calculatediscountsandtaxesBundles(contentType, accept, calculatediscountsandtaxesBundlesRequest)

Calculate discounts and taxes (Bundles)

Calculate discounts and taxes

### Example

```javascript
import PromotionsTaxesApi from 'promotions__taxes_api';
let defaultClient = PromotionsTaxesApi.ApiClient.instance;
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

let apiInstance = new PromotionsTaxesApi.BundlesApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let calculatediscountsandtaxesBundlesRequest = {"isShoppingCart":true,"items":[{"id":"160","index":0,"isGift":false,"logisticsInfos":[],"measurementUnit":"un","params":[{"name":"Seller@CatalogSystem","value":"1"},{"name":"product@CatalogSystem","value":"94"}],"priceSheet":[],"priceTags":[],"productSpecifications":[],"quantity":3,"sellerId":"1","unitMultiplier":1}],"origin":"Marketplace","params":[{"name":"product@CatalogSystem","value":"2662"},{"name":"couponCode@Marketing","value":"coupon"}],"profileId":"aa","salesChannel":"1"}; // CalculatediscountsandtaxesBundlesRequest | 
apiInstance.calculatediscountsandtaxesBundles(contentType, accept, calculatediscountsandtaxesBundlesRequest, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **calculatediscountsandtaxesBundlesRequest** | [**CalculatediscountsandtaxesBundlesRequest**](CalculatediscountsandtaxesBundlesRequest.md)|  | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

