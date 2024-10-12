# PromotionsTaxesApi.CouponsApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiRnbPvtCouponPost**](CouponsApi.md#apiRnbPvtCouponPost) | **POST** /api/rnb/pvt/coupon/ | Create coupon
[**apiRnbPvtMultipleCouponsPost**](CouponsApi.md#apiRnbPvtMultipleCouponsPost) | **POST** /api/rnb/pvt/multiple-coupons | Create multiple coupons
[**archivebycouponcode**](CouponsApi.md#archivebycouponcode) | **POST** /api/rnb/pvt/archive/coupon/{couponCode} | Archive coupon by coupon code
[**getall**](CouponsApi.md#getall) | **GET** /api/rnb/pvt/coupon | Get all coupons
[**getarchivedbycouponcode**](CouponsApi.md#getarchivedbycouponcode) | **GET** /api/rnb/pvt/archive/coupon/{couponCode} | Get archived coupon by coupon code
[**getbycouponcode**](CouponsApi.md#getbycouponcode) | **GET** /api/rnb/pvt/coupon/{couponCode} | Get coupon by coupon code
[**getusage**](CouponsApi.md#getusage) | **GET** /api/rnb/pvt/coupon/usage/{couponCode} | Get coupon usage
[**massiveGeneration**](CouponsApi.md#massiveGeneration) | **POST** /api/rnb/pvt/coupons | Coupon Massive Generation
[**unarchivebycouponcode**](CouponsApi.md#unarchivebycouponcode) | **POST** /api/rnb/pvt/unarchive/coupon/{couponCode} | Unarchive coupon by coupon code
[**update**](CouponsApi.md#update) | **POST** /api/rnb/pvt/coupon | Update coupon



## apiRnbPvtCouponPost

> Getarchivedbycouponcode200Response apiRnbPvtCouponPost(contentType, accept, opts)

Create coupon

Creates a single new coupon.

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

let apiInstance = new PromotionsTaxesApi.CouponsApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let opts = {
  'apiRnbPvtCouponPostRequest': new PromotionsTaxesApi.ApiRnbPvtCouponPostRequest() // ApiRnbPvtCouponPostRequest | 
};
apiInstance.apiRnbPvtCouponPost(contentType, accept, opts, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **apiRnbPvtCouponPostRequest** | [**ApiRnbPvtCouponPostRequest**](ApiRnbPvtCouponPostRequest.md)|  | [optional] 

### Return type

[**Getarchivedbycouponcode200Response**](Getarchivedbycouponcode200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## apiRnbPvtMultipleCouponsPost

> [String] apiRnbPvtMultipleCouponsPost(contentType, accept, opts)

Create multiple coupons

Creates multiple coupons with different coupon codes. This endpoint has a throttling of 60 requests per minute.

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

let apiInstance = new PromotionsTaxesApi.CouponsApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let opts = {
  'apiRnbPvtMultipleCouponsPostRequestInner': [{"couponConfiguration":{"couponCode":"promobf4","expirationIntervalPerUse":"00:00:00","isArchived":false,"maxItemsPerClient":10,"utmCampaign":"bf","utmSource":"fb"},"quantity":1}] // [ApiRnbPvtMultipleCouponsPostRequestInner] | 
};
apiInstance.apiRnbPvtMultipleCouponsPost(contentType, accept, opts, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **apiRnbPvtMultipleCouponsPostRequestInner** | [**[ApiRnbPvtMultipleCouponsPostRequestInner]**](ApiRnbPvtMultipleCouponsPostRequestInner.md)|  | [optional] 

### Return type

**[String]**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## archivebycouponcode

> String archivebycouponcode(contentType, accept, couponCode)

Archive coupon by coupon code

Archives a specifc coupon by its coupon code.

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

let apiInstance = new PromotionsTaxesApi.CouponsApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let couponCode = "test"; // String | Coupon Code
apiInstance.archivebycouponcode(contentType, accept, couponCode, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **couponCode** | **String**| Coupon Code | 

### Return type

**String**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getall

> [Getall200ResponseInner] getall(contentType, accept)

Get all coupons

  &gt; Check the new [Promotions onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/promotions-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Promotions and is organized by focusing on the developer&#39;s journey.     Retrieves all coupons from an account.

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

let apiInstance = new PromotionsTaxesApi.CouponsApi();
let contentType = "'application/json'"; // String | 
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
apiInstance.getall(contentType, accept, (error, data, response) => {
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
 **contentType** | **String**|  | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]

### Return type

[**[Getall200ResponseInner]**](Getall200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getarchivedbycouponcode

> Getarchivedbycouponcode200Response getarchivedbycouponcode(contentType, accept, couponCode)

Get archived coupon by coupon code

Retrieves a specific archived coupon by its coupon code.

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

let apiInstance = new PromotionsTaxesApi.CouponsApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let couponCode = "promo10"; // String | Coupon Code
apiInstance.getarchivedbycouponcode(contentType, accept, couponCode, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **couponCode** | **String**| Coupon Code | 

### Return type

[**Getarchivedbycouponcode200Response**](Getarchivedbycouponcode200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getbycouponcode

> Getarchivedbycouponcode200Response getbycouponcode(contentType, accept, couponCode)

Get coupon by coupon code

Retrieves a specific coupon by its coupon code.

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

let apiInstance = new PromotionsTaxesApi.CouponsApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let couponCode = "promo10"; // String | Coupon Code
apiInstance.getbycouponcode(contentType, accept, couponCode, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **couponCode** | **String**| Coupon Code | 

### Return type

[**Getarchivedbycouponcode200Response**](Getarchivedbycouponcode200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getusage

> Getusage200Response getusage(contentType, accept, couponCode)

Get coupon usage

Retrieves information about the coupon usage.

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

let apiInstance = new PromotionsTaxesApi.CouponsApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let couponCode = "test"; // String | Coupon Code
apiInstance.getusage(contentType, accept, couponCode, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **couponCode** | **String**| Coupon Code | 

### Return type

[**Getusage200Response**](Getusage200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## massiveGeneration

> [String] massiveGeneration(contentType, accept, quantity, massiveGenerationRequest)

Coupon Massive Generation

Generates a massive amount of coupons

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

let apiInstance = new PromotionsTaxesApi.CouponsApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let quantity = 10; // Number | Quantity of coupons to generate
let massiveGenerationRequest = new PromotionsTaxesApi.MassiveGenerationRequest(); // MassiveGenerationRequest | 
apiInstance.massiveGeneration(contentType, accept, quantity, massiveGenerationRequest, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **quantity** | **Number**| Quantity of coupons to generate | 
 **massiveGenerationRequest** | [**MassiveGenerationRequest**](MassiveGenerationRequest.md)|  | 

### Return type

**[String]**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## unarchivebycouponcode

> String unarchivebycouponcode(contentType, accept, couponCode)

Unarchive coupon by coupon code

Unarchives a specifc coupon by its coupon code.

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

let apiInstance = new PromotionsTaxesApi.CouponsApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let couponCode = "test"; // String | Coupon Code
apiInstance.unarchivebycouponcode(contentType, accept, couponCode, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **couponCode** | **String**| Coupon Code | 

### Return type

**String**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## update

> Getarchivedbycouponcode200Response update(contentType, accept, updateRequest)

Update coupon

Updates information of a specific coupon.

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

let apiInstance = new PromotionsTaxesApi.CouponsApi();
let contentType = "'application/json'"; // String | Type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
let updateRequest = new PromotionsTaxesApi.UpdateRequest(); // UpdateRequest | 
apiInstance.update(contentType, accept, updateRequest, (error, data, response) => {
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
 **contentType** | **String**| Type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **updateRequest** | [**UpdateRequest**](UpdateRequest.md)|  | 

### Return type

[**Getarchivedbycouponcode200Response**](Getarchivedbycouponcode200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

