# PricingHub.PricingHubPricesApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiPricingHubPricesPost**](PricingHubPricesApi.md#apiPricingHubPricesPost) | **POST** /api/pricing-hub/prices | Get Prices
[**configExternalPriceSource**](PricingHubPricesApi.md#configExternalPriceSource) | **PUT** /config | Configure External Price Source



## apiPricingHubPricesPost

> Response2 apiPricingHubPricesPost(accountName, accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, getPricesRequestObject)

Get Prices

This route retrieves and applies prices for the items that are passed in the request. Pricing Hub will select the pricing method that will be used for each item and will fetch their respective price from the selected pricing method.     &gt;ℹ️ &gt; This feature is in closed beta, available only for selected customers. If you have any questions, contact our [Support](https://support.vtex.com/hc/en-us/requests). 

### Example

```javascript
import PricingHub from 'pricing_hub';
let defaultClient = PricingHub.ApiClient.instance;
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

let apiInstance = new PricingHub.PricingHubPricesApi();
let accountName = "'apiexamples'"; // String | Name of the VTEX account. Used as part of the URL
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let contentType = "'application/json'"; // String | Describes the type of the content being sent
let xVTEXAPIAppKey = "'{{X-VTEX-API-AppKey}}'"; // String | The AppKey configured by the merchant
let xVTEXAPIAppToken = "'{{X-VTEX-API-AppToken}}'"; // String | The AppToken configured by the merchant
let getPricesRequestObject = {"UtmCampaign":"summer","UtmInternalCampaign":"sale","UtmMedium":"social","UtmSource":"facebook","email":"customer@email.com","items":[{"brandId":"2000000","categoriesIds":["1"],"index":0,"priceTableIds":[],"quantity":1,"sellerId":"1","skuId":"13"}],"salesChannel":"1"}; // GetPricesRequestObject | 
apiInstance.apiPricingHubPricesPost(accountName, accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, getPricesRequestObject, (error, data, response) => {
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
 **accountName** | **String**| Name of the VTEX account. Used as part of the URL | [default to &#39;apiexamples&#39;]
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]
 **contentType** | **String**| Describes the type of the content being sent | [default to &#39;application/json&#39;]
 **xVTEXAPIAppKey** | **String**| The AppKey configured by the merchant | [default to &#39;{{X-VTEX-API-AppKey}}&#39;]
 **xVTEXAPIAppToken** | **String**| The AppToken configured by the merchant | [default to &#39;{{X-VTEX-API-AppToken}}&#39;]
 **getPricesRequestObject** | [**GetPricesRequestObject**](GetPricesRequestObject.md)|  | 

### Return type

[**Response2**](Response2.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## configExternalPriceSource

> configExternalPriceSource(accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, configExternalPriceSourceRequest, opts)

Configure External Price Source

This route facilitates setting up an external price source in Pricing Hub. It also allows you to activate or deactivate that source in a given account.     &gt;ℹ️ This feature is in closed beta, available only for selected customers. If you have any questions, contact our [Support](https://support.vtex.com/hc/en-us/requests). 

### Example

```javascript
import PricingHub from 'pricing_hub';
let defaultClient = PricingHub.ApiClient.instance;
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

let apiInstance = new PricingHub.PricingHubPricesApi();
let accept = "'application/json'"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
let contentType = "'application/json'"; // String | Describes the type of the content being sent
let xVTEXAPIAppKey = "'{{X-VTEX-API-AppKey}}'"; // String | The AppKey configured by the merchant
let xVTEXAPIAppToken = "'{{X-VTEX-API-AppToken}}'"; // String | The AppToken configured by the merchant
let configExternalPriceSourceRequest = {"active":true,"appName":"apiexamples_app_name"}; // ConfigExternalPriceSourceRequest | 
let opts = {
  'an': "apiexamples" // String | Name of the VTEX account
};
apiInstance.configExternalPriceSource(accept, contentType, xVTEXAPIAppKey, xVTEXAPIAppToken, configExternalPriceSourceRequest, opts, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to &#39;application/json&#39;]
 **contentType** | **String**| Describes the type of the content being sent | [default to &#39;application/json&#39;]
 **xVTEXAPIAppKey** | **String**| The AppKey configured by the merchant | [default to &#39;{{X-VTEX-API-AppKey}}&#39;]
 **xVTEXAPIAppToken** | **String**| The AppToken configured by the merchant | [default to &#39;{{X-VTEX-API-AppToken}}&#39;]
 **configExternalPriceSourceRequest** | [**ConfigExternalPriceSourceRequest**](ConfigExternalPriceSourceRequest.md)|  | 
 **an** | **String**| Name of the VTEX account | [optional] 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

