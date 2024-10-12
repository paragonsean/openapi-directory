# PricingApi.PricesAndFixedPricesApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createUpdatePriceOrFixedPrice**](PricesAndFixedPricesApi.md#createUpdatePriceOrFixedPrice) | **PUT** /pricing/prices/{itemId} | Create or Update Base Price or Fixed Prices
[**createorupdatefixedpricesonpricetableortradepolicy**](PricesAndFixedPricesApi.md#createorupdatefixedpricesonpricetableortradepolicy) | **POST** /pricing/prices/{itemId}/fixed/{priceTableId} | Create or Update Fixed Prices on a price table or trade policy
[**deletePrice**](PricesAndFixedPricesApi.md#deletePrice) | **DELETE** /pricing/prices/{itemId} | Delete Price
[**deletefixedpricesonapricetableortradepolicy**](PricesAndFixedPricesApi.md#deletefixedpricesonapricetableortradepolicy) | **DELETE** /pricing/prices/{itemId}/fixed/{priceTableId} | Delete Fixed Prices on a price table or trade policy
[**getComputedPricebypricetable**](PricesAndFixedPricesApi.md#getComputedPricebypricetable) | **GET** /pricing/prices/{itemId}/computed/{priceTableId} | Get Computed Price by price table or trade policy
[**getFixedPrices**](PricesAndFixedPricesApi.md#getFixedPrices) | **GET** /pricing/prices/{itemId}/fixed | Get Fixed Prices
[**getFixedPricesonapricetable**](PricesAndFixedPricesApi.md#getFixedPricesonapricetable) | **GET** /pricing/prices/{itemId}/fixed/{priceTableId} | Get Fixed Prices on a price table or trade policy
[**getPrice**](PricesAndFixedPricesApi.md#getPrice) | **GET** /pricing/prices/{itemId} | Get Price



## createUpdatePriceOrFixedPrice

> createUpdatePriceOrFixedPrice(accept, contentType, itemId, opts)

Create or Update Base Price or Fixed Prices

Creates or updates an SKU Base Price or Fixed Prices. The **base price** is the basic selling price of a product, it comprises the cost price and the markup wanted in the sale of the product. The **fixed price** is an optional price of the SKU for a specific trade policy with a specific minimum quantity to be activated.     &lt;p&gt; You may optionally set a list price. Additionally, you may set either a cost price or a markup value. By defining either one of them, the other will be calculated to conform to the formula &lt;code&gt;costPrice * (1 + markup) &#x3D; basePrice&lt;/code&gt;.&lt;/p&gt; &lt;h2&gt;Request body example&lt;/h2&gt;    &#x60;&#x60;&#x60;json  {      \&quot;markup\&quot;: 30,      \&quot;basePrice\&quot;: 100,      \&quot;listPrice\&quot;: 35,      \&quot;fixedPrices\&quot;: [          {              \&quot;tradePolicyId\&quot;: \&quot;1\&quot;,              \&quot;value\&quot;: 31,              \&quot;listPrice\&quot;: 32,              \&quot;minQuantity\&quot;: 1,              \&quot;dateRange\&quot;: {                  \&quot;from\&quot;: \&quot;2022-05-21T22:00:00Z\&quot;,                  \&quot;to\&quot;: \&quot;2023-05-28T22:00:00Z\&quot;              }          },          {              \&quot;tradePolicyId\&quot;: \&quot;1\&quot;,              \&quot;value\&quot;: 31.5,              \&quot;listPrice\&quot;: 33,              \&quot;minQuantity\&quot;: 2          }      ]  }  &#x60;&#x60;&#x60;

### Example

```javascript
import PricingApi from 'pricing_api';
let defaultClient = PricingApi.ApiClient.instance;
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

let apiInstance = new PricingApi.PricesAndFixedPricesApi();
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let itemId = 1; // Number | SKU unique identifier number.
let opts = {
  'createUpdatePriceOrFixedPriceRequest': new PricingApi.CreateUpdatePriceOrFixedPriceRequest() // CreateUpdatePriceOrFixedPriceRequest | 
};
apiInstance.createUpdatePriceOrFixedPrice(accept, contentType, itemId, opts, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | 
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **itemId** | **Number**| SKU unique identifier number. | 
 **createUpdatePriceOrFixedPriceRequest** | [**CreateUpdatePriceOrFixedPriceRequest**](CreateUpdatePriceOrFixedPriceRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## createorupdatefixedpricesonpricetableortradepolicy

> createorupdatefixedpricesonpricetableortradepolicy(contentType, accept, itemId, priceTableId, opts)

Create or Update Fixed Prices on a price table or trade policy

Creates or updates the fixed prices of an SKU for a specific price table or trade policy. You can add one or multiple fixed prices per SKU.     ## Request body example    &#x60;&#x60;&#x60;json  [    {      \&quot;value\&quot;: 50.5,      \&quot;listPrice\&quot;: 50.5,      \&quot;minQuantity\&quot;: 2,      \&quot;dateRange\&quot;: {        \&quot;from\&quot;: \&quot;2021-12-30T22:00:00-03:00\&quot;,        \&quot;to\&quot;: \&quot;2021-12-30T22:00:00-04:00\&quot;      }    }  ]  &#x60;&#x60;&#x60;

### Example

```javascript
import PricingApi from 'pricing_api';
let defaultClient = PricingApi.ApiClient.instance;
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

let apiInstance = new PricingApi.PricesAndFixedPricesApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let itemId = 1; // Number | SKU ID.
let priceTableId = "priceTableA"; // String | SKU **price table** name or **trade policy** ID.
let opts = {
  'createorupdatefixedpricesonpricetableortradepolicyRequestInner': [new PricingApi.CreateorupdatefixedpricesonpricetableortradepolicyRequestInner()] // [CreateorupdatefixedpricesonpricetableortradepolicyRequestInner] | 
};
apiInstance.createorupdatefixedpricesonpricetableortradepolicy(contentType, accept, itemId, priceTableId, opts, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **itemId** | **Number**| SKU ID. | 
 **priceTableId** | **String**| SKU **price table** name or **trade policy** ID. | 
 **createorupdatefixedpricesonpricetableortradepolicyRequestInner** | [**[CreateorupdatefixedpricesonpricetableortradepolicyRequestInner]**](CreateorupdatefixedpricesonpricetableortradepolicyRequestInner.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## deletePrice

> deletePrice(contentType, accept, itemId)

Delete Price

Deletes the Base Price and all available Fixed Prices for an SKU in all trade policies.

### Example

```javascript
import PricingApi from 'pricing_api';
let defaultClient = PricingApi.ApiClient.instance;
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

let apiInstance = new PricingApi.PricesAndFixedPricesApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let itemId = 1; // Number | SKU ID.
apiInstance.deletePrice(contentType, accept, itemId, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **itemId** | **Number**| SKU ID. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deletefixedpricesonapricetableortradepolicy

> deletefixedpricesonapricetableortradepolicy(contentType, accept, itemId, priceTableId)

Delete Fixed Prices on a price table or trade policy

Deletes all Fixed Prices of an SKU in a specific Price Table or Trade Policy.

### Example

```javascript
import PricingApi from 'pricing_api';
let defaultClient = PricingApi.ApiClient.instance;
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

let apiInstance = new PricingApi.PricesAndFixedPricesApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let itemId = 1; // Number | SKU ID.
let priceTableId = "gold"; // String | Price Table or Trade Policy Name.
apiInstance.deletefixedpricesonapricetableortradepolicy(contentType, accept, itemId, priceTableId, (error, data, response) => {
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
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | 
 **itemId** | **Number**| SKU ID. | 
 **priceTableId** | **String**| Price Table or Trade Policy Name. | 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getComputedPricebypricetable

> Getcomputedprice getComputedPricebypricetable(categoryIds, brandId, quantity, contentType, accept, itemId, priceTableId)

Get Computed Price by price table or trade policy

Gets the Computed Price, which is the price after all the steps in the Pricing pipeline, for an SKU in a specific price table or trade policy.     ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;tradePolicyId\&quot;: \&quot;1\&quot;,      \&quot;listPrice\&quot;: 30,      \&quot;costPrice\&quot;: 76.92,      \&quot;sellingPrice\&quot;: 18.9,      \&quot;priceValidUntil\&quot;: \&quot;2018-12-20T18:12:14Z\&quot;  }  &#x60;&#x60;&#x60;

### Example

```javascript
import PricingApi from 'pricing_api';
let defaultClient = PricingApi.ApiClient.instance;
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

let apiInstance = new PricingApi.PricesAndFixedPricesApi();
let categoryIds = 1; // Number | Category ID.
let brandId = 3; // Number | Brand ID.
let quantity = 2; // Number | SKU quantity.
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let itemId = 1; // Number | SKU ID.
let priceTableId = "gold"; // String | SKU Price Table Name.
apiInstance.getComputedPricebypricetable(categoryIds, brandId, quantity, contentType, accept, itemId, priceTableId, (error, data, response) => {
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
 **categoryIds** | **Number**| Category ID. | 
 **brandId** | **Number**| Brand ID. | 
 **quantity** | **Number**| SKU quantity. | 
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | 
 **itemId** | **Number**| SKU ID. | 
 **priceTableId** | **String**| SKU Price Table Name. | 

### Return type

[**Getcomputedprice**](Getcomputedprice.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## getFixedPrices

> [FixedPrice] getFixedPrices(accept, contentType, itemId)

Get Fixed Prices

The **fixed price** is an optional price of the SKU for a specific trade policy with a specific minimum quantity to be activated. This method retrieves an array of Fixed Prices for an SKU in a Trade Policy with Minimum Quantities.     The default value for a Minimum Quantity is &#x60;1&#x60;. This means a Fixed Price will be valid for a SKU in a Trade Policy for orders containing the specified number of Minimum Quantity or above, unless a higher Minimum Quantity is specified.     Fixed prices may, optionally, be scheduled. If so, these objects will contain the &#x60;dateRange&#x60; object with &#x60;from&#x60; and &#x60;to&#x60; properties, indicating the start and end time of the scheduled fixed price in the RFC3339 timestamp format (&#x60;YYYY-MM-DDT23:59:60Z&#x60;).     Note that the &#39;Z&#39;, at the end, represents the UTC time (GMT+00:00). If it was in GMT-03:00, for example, it would be (&#x60;YYYY-MM-DDT23:59:60-03:00&#x60;).     ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;tradePolicyId\&quot;: \&quot;6\&quot;,          \&quot;value\&quot;: 20.9,          \&quot;listPrice\&quot;: 22.9,          \&quot;minQuantity\&quot;: 1,          \&quot;dateRange\&quot;: {              \&quot;from\&quot;: \&quot;2021-12-30T22:00:00-03:00\&quot;,              \&quot;to\&quot;: \&quot;2021-12-30T22:00:00-03:00\&quot;          }      },      {          \&quot;tradePolicyId\&quot;: \&quot;1\&quot;,          \&quot;value\&quot;: 18.9,          \&quot;listPrice\&quot;: null,          \&quot;minQuantity\&quot;: 1,          \&quot;dateRange\&quot;: {              \&quot;from\&quot;: \&quot;2021-12-30T22:00:00-03:00\&quot;,              \&quot;to\&quot;: \&quot;2021-12-30T22:00:00-03:00\&quot;          }      }  ]  &#x60;&#x60;&#x60;

### Example

```javascript
import PricingApi from 'pricing_api';
let defaultClient = PricingApi.ApiClient.instance;
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

let apiInstance = new PricingApi.PricesAndFixedPricesApi();
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let itemId = 1; // Number | SKU ID.
apiInstance.getFixedPrices(accept, contentType, itemId, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | 
 **contentType** | **String**| Describes the type of the content being sent. | [default to &#39;application/json&#39;]
 **itemId** | **Number**| SKU ID. | 

### Return type

[**[FixedPrice]**](FixedPrice.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## getFixedPricesonapricetable

> [FixedPrice] getFixedPricesonapricetable(contentType, accept, itemId, priceTableId)

Get Fixed Prices on a price table or trade policy

Retrieves all Fixed Prices on a price table or trade policy.     ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;tradePolicyId\&quot;: \&quot;6\&quot;,          \&quot;value\&quot;: 20.9,          \&quot;listPrice\&quot;: 22.9,          \&quot;minQuantity\&quot;: 1,          \&quot;dateRange\&quot;: {              \&quot;from\&quot;: \&quot;2021-12-30T22:00:00-03:00\&quot;,              \&quot;to\&quot;: \&quot;2021-12-30T22:00:00-04:00\&quot;          }      },      {          \&quot;tradePolicyId\&quot;: \&quot;1\&quot;,          \&quot;value\&quot;: 18.9,          \&quot;listPrice\&quot;: null,          \&quot;minQuantity\&quot;: 1      }  ]  &#x60;&#x60;&#x60;

### Example

```javascript
import PricingApi from 'pricing_api';
let defaultClient = PricingApi.ApiClient.instance;
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

let apiInstance = new PricingApi.PricesAndFixedPricesApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "application/json"; // String | 
let itemId = 1; // Number | SKU ID.
let priceTableId = "gold"; // String | Price Table Name
apiInstance.getFixedPricesonapricetable(contentType, accept, itemId, priceTableId, (error, data, response) => {
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
 **accept** | **String**|  | 
 **itemId** | **Number**| SKU ID. | 
 **priceTableId** | **String**| Price Table Name | 

### Return type

[**[FixedPrice]**](FixedPrice.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## getPrice

> Getprice getPrice(contentType, accept, itemId)

Get Price

Retrieves price data given a specific SKU ID. Within the &#x60;fixedPrices&#x60; object, there might be a list of prices for specific Trade Policies and Minimium Quantities of the SKU. Fixed Prices may also be scheduled.     ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;itemId\&quot;: \&quot;1\&quot;,      \&quot;listPrice\&quot;: 50,      \&quot;costPrice\&quot;: 90,      \&quot;markup\&quot;: 30,      \&quot;basePrice\&quot;: 117,      \&quot;fixedPrices\&quot;: [          {              \&quot;tradePolicyId\&quot;: \&quot;1\&quot;,              \&quot;value\&quot;: 50.5,              \&quot;listPrice\&quot;: 50.5,              \&quot;minQuantity\&quot;: 2,              \&quot;dateRange\&quot;: {                  \&quot;from\&quot;: \&quot;2021-12-31T01:00:00Z\&quot;,                  \&quot;to\&quot;: \&quot;2022-12-31T01:00:00Z\&quot;              }          },          {              \&quot;tradePolicyId\&quot;: \&quot;2\&quot;,              \&quot;value\&quot;: 30,              \&quot;listPrice\&quot;: 50,              \&quot;minQuantity\&quot;: 2          }      ]  }  &#x60;&#x60;&#x60;

### Example

```javascript
import PricingApi from 'pricing_api';
let defaultClient = PricingApi.ApiClient.instance;
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

let apiInstance = new PricingApi.PricesAndFixedPricesApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let itemId = 1; // Number | SKU ID.
apiInstance.getPrice(contentType, accept, itemId, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | 
 **itemId** | **Number**| SKU ID. | 

### Return type

[**Getprice**](Getprice.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

