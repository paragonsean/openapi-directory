# LegacySearchApi.CrossSellingApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**productSearchAccessories**](CrossSellingApi.md#productSearchAccessories) | **GET** /api/catalog_system/pub/products/crossselling/accessories/{productId} | Get Product Search of Accessories
[**productSearchShowTogether**](CrossSellingApi.md#productSearchShowTogether) | **GET** /api/catalog_system/pub/products/crossselling/showtogether/{productId} | Get Product Search of Show Together
[**productSearchSimilars**](CrossSellingApi.md#productSearchSimilars) | **GET** /api/catalog_system/pub/products/crossselling/similars/{productId} | Get Product Search of Similars
[**productSearchSuggestions**](CrossSellingApi.md#productSearchSuggestions) | **GET** /api/catalog_system/pub/products/crossselling/suggestions/{productId} | Get Product Search of Suggestions
[**productSearchWhoBoughtAlsoBought**](CrossSellingApi.md#productSearchWhoBoughtAlsoBought) | **GET** /api/catalog_system/pub/products/crossselling/whoboughtalsobought/{productId} | Get Product Search of Who Bought Also Bought
[**productSearchWhoSawAlsoBought**](CrossSellingApi.md#productSearchWhoSawAlsoBought) | **GET** /api/catalog_system/pub/products/crossselling/whosawalsobought/{productId} | Get Product Search of Who Saw Also Bought
[**productSearchWhoSawAlsoSaw**](CrossSellingApi.md#productSearchWhoSawAlsoSaw) | **GET** /api/catalog_system/pub/products/crossselling/whosawalsosaw/{productId} | Get Product Search of Who Saw Also Saw



## productSearchAccessories

> productSearchAccessories(accept, contentType, productId)

Get Product Search of Accessories

Retrieves general information about the product&#39;s accessories.

### Example

```javascript
import LegacySearchApi from 'legacy_search_api';
let defaultClient = LegacySearchApi.ApiClient.instance;
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

let apiInstance = new LegacySearchApi.CrossSellingApi();
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "application/json"; // String | Describes the type of the content being sent.
let productId = 1; // Number | Product's unique identifier
apiInstance.productSearchAccessories(accept, contentType, productId, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 
 **contentType** | **String**| Describes the type of the content being sent. | 
 **productId** | **Number**| Product&#39;s unique identifier | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## productSearchShowTogether

> productSearchShowTogether(accept, contentType, productId)

Get Product Search of Show Together

Retrieves general information about the products that are show together with the product in question.

### Example

```javascript
import LegacySearchApi from 'legacy_search_api';
let defaultClient = LegacySearchApi.ApiClient.instance;
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

let apiInstance = new LegacySearchApi.CrossSellingApi();
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "application/json"; // String | Describes the type of the content being sent.
let productId = 1; // Number | Product's unique identifier
apiInstance.productSearchShowTogether(accept, contentType, productId, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 
 **contentType** | **String**| Describes the type of the content being sent. | 
 **productId** | **Number**| Product&#39;s unique identifier | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## productSearchSimilars

> productSearchSimilars(accept, contentType, productId)

Get Product Search of Similars

Retrieves general information about related product searches.

### Example

```javascript
import LegacySearchApi from 'legacy_search_api';
let defaultClient = LegacySearchApi.ApiClient.instance;
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

let apiInstance = new LegacySearchApi.CrossSellingApi();
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "application/json"; // String | Describes the type of the content being sent.
let productId = 1; // Number | Product's unique identifier
apiInstance.productSearchSimilars(accept, contentType, productId, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 
 **contentType** | **String**| Describes the type of the content being sent. | 
 **productId** | **Number**| Product&#39;s unique identifier | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## productSearchSuggestions

> productSearchSuggestions(accept, contentType, productId)

Get Product Search of Suggestions

Retrieves general information about other product suggestions related to the product.

### Example

```javascript
import LegacySearchApi from 'legacy_search_api';
let defaultClient = LegacySearchApi.ApiClient.instance;
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

let apiInstance = new LegacySearchApi.CrossSellingApi();
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "application/json"; // String | Describes the type of the content being sent.
let productId = 1; // Number | Product's unique identifier
apiInstance.productSearchSuggestions(accept, contentType, productId, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 
 **contentType** | **String**| Describes the type of the content being sent. | 
 **productId** | **Number**| Product&#39;s unique identifier | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## productSearchWhoBoughtAlsoBought

> [ProductSearchWhoBoughtAlsoBought200ResponseInner] productSearchWhoBoughtAlsoBought(accept, contentType, productId)

Get Product Search of Who Bought Also Bought

Retrieves general information about other related products that the user also bought.

### Example

```javascript
import LegacySearchApi from 'legacy_search_api';
let defaultClient = LegacySearchApi.ApiClient.instance;
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

let apiInstance = new LegacySearchApi.CrossSellingApi();
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "application/json"; // String | Describes the type of the content being sent.
let productId = "1"; // String | Product unique identifier.
apiInstance.productSearchWhoBoughtAlsoBought(accept, contentType, productId, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 
 **contentType** | **String**| Describes the type of the content being sent. | 
 **productId** | **String**| Product unique identifier. | 

### Return type

[**[ProductSearchWhoBoughtAlsoBought200ResponseInner]**](ProductSearchWhoBoughtAlsoBought200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productSearchWhoSawAlsoBought

> [ProductSearchWhoBoughtAlsoBought200ResponseInner] productSearchWhoSawAlsoBought(accept, contentType, productId)

Get Product Search of Who Saw Also Bought

Retrieves general information about other related products that the users saw and also bought.

### Example

```javascript
import LegacySearchApi from 'legacy_search_api';
let defaultClient = LegacySearchApi.ApiClient.instance;
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

let apiInstance = new LegacySearchApi.CrossSellingApi();
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "application/json"; // String | Describes the type of the content being sent.
let productId = "1"; // String | Product unique identifier.
apiInstance.productSearchWhoSawAlsoBought(accept, contentType, productId, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 
 **contentType** | **String**| Describes the type of the content being sent. | 
 **productId** | **String**| Product unique identifier. | 

### Return type

[**[ProductSearchWhoBoughtAlsoBought200ResponseInner]**](ProductSearchWhoBoughtAlsoBought200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productSearchWhoSawAlsoSaw

> [ProductSearchWhoBoughtAlsoBought200ResponseInner] productSearchWhoSawAlsoSaw(accept, contentType, productId)

Get Product Search of Who Saw Also Saw

Retrieves general information about other related products that the users also saw.

### Example

```javascript
import LegacySearchApi from 'legacy_search_api';
let defaultClient = LegacySearchApi.ApiClient.instance;
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

let apiInstance = new LegacySearchApi.CrossSellingApi();
let accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let contentType = "application/json"; // String | Describes the type of the content being sent.
let productId = 1; // Number | Product unique identifier.
apiInstance.productSearchWhoSawAlsoSaw(accept, contentType, productId, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | 
 **contentType** | **String**| Describes the type of the content being sent. | 
 **productId** | **Number**| Product unique identifier. | 

### Return type

[**[ProductSearchWhoBoughtAlsoBought200ResponseInner]**](ProductSearchWhoBoughtAlsoBought200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

