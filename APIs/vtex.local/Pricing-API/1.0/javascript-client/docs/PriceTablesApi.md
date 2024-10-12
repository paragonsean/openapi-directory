# PricingApi.PriceTablesApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getallpricetablesandrules**](PriceTablesApi.md#getallpricetablesandrules) | **GET** /pricing/pipeline/catalog | Get all price tables and their rules
[**getrulesforapricetable**](PriceTablesApi.md#getrulesforapricetable) | **GET** /pricing/pipeline/catalog/{priceTableId} | Get rules for a price table
[**listpricetables**](PriceTablesApi.md#listpricetables) | **GET** /pricing/tables | List price tables
[**pricingPipelineCatalogPriceTableIdPut**](PriceTablesApi.md#pricingPipelineCatalogPriceTableIdPut) | **PUT** /pricing/pipeline/catalog/{priceTableId} | Update rules for a price table



## getallpricetablesandrules

> [Getallpricetablesandrules200ResponseInner] getallpricetablesandrules(contentType, accept)

Get all price tables and their rules

This method will retrieve all price tables and their rules.    ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;tradePolicyId\&quot;: \&quot;2\&quot;,          \&quot;rules\&quot;: [              {                  \&quot;id\&quot;: 0,                  \&quot;context\&quot;: {                      \&quot;categories\&quot;: {},                      \&quot;brands\&quot;: {},                      \&quot;stockStatuses\&quot;: null,                      \&quot;internalCategories\&quot;: null,                      \&quot;markupRange\&quot;: null,                      \&quot;dateRange\&quot;: null                  },                  \&quot;percentualModifier\&quot;: 20              }          ]      },      {          \&quot;tradePolicyId\&quot;: \&quot;b2c\&quot;,          \&quot;rules\&quot;: [              {                  \&quot;id\&quot;: 0,                  \&quot;context\&quot;: {                      \&quot;categories\&quot;: {},                      \&quot;brands\&quot;: {                          \&quot;2000009\&quot;: \&quot;Whiskas\&quot;                      },                      \&quot;stockStatuses\&quot;: null,                      \&quot;internalCategories\&quot;: null,                      \&quot;markupRange\&quot;: null,                      \&quot;dateRange\&quot;: null                  },                  \&quot;percentualModifier\&quot;: 15              }          ]      }  ]  &#x60;&#x60;&#x60;

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

let apiInstance = new PricingApi.PriceTablesApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
apiInstance.getallpricetablesandrules(contentType, accept, (error, data, response) => {
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

### Return type

[**[Getallpricetablesandrules200ResponseInner]**](Getallpricetablesandrules200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getrulesforapricetable

> Getrulesforapricetable200Response getrulesforapricetable(contentType, accept, priceTableId)

Get rules for a price table

This method will retrieve the rules from a specific Price Table.    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;tradePolicyId\&quot;: \&quot;b2c\&quot;,      \&quot;rules\&quot;: [{          \&quot;id\&quot;: 0,          \&quot;context\&quot;: {              \&quot;categories\&quot;: {},              \&quot;brands\&quot;: {                  \&quot;2000009\&quot;: \&quot;Whiskas\&quot;              },              \&quot;stockStatuses\&quot;: null,              \&quot;internalCategories\&quot;: null,              \&quot;markupRange\&quot;: null,              \&quot;dateRange\&quot;: null          },          \&quot;percentualModifier\&quot;: 15      }]  }  &#x60;&#x60;&#x60;

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

let apiInstance = new PricingApi.PriceTablesApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let priceTableId = "b2c"; // String | Price Table Name.
apiInstance.getrulesforapricetable(contentType, accept, priceTableId, (error, data, response) => {
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
 **priceTableId** | **String**| Price Table Name. | 

### Return type

[**Getrulesforapricetable200Response**](Getrulesforapricetable200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listpricetables

> [String] listpricetables(contentType, accept)

List price tables

This method will list all price tables.    ## Response body example    &#x60;&#x60;&#x60;json  [      \&quot;1\&quot;,      \&quot;2\&quot;,      \&quot;3\&quot;,      \&quot;b2c\&quot;,      \&quot;b2b\&quot;,      \&quot;gold\&quot;  ]  &#x60;&#x60;&#x60;

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

let apiInstance = new PricingApi.PriceTablesApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
apiInstance.listpricetables(contentType, accept, (error, data, response) => {
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

### Return type

**[String]**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pricingPipelineCatalogPriceTableIdPut

> pricingPipelineCatalogPriceTableIdPut(contentType, accept, priceTableId, opts)

Update rules for a price table

This method will update the rules from a specific Price Table. It will delete all the rules from the requested Price Table and create new rules based on the content of the request.    ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;rules\&quot;: [            {                 \&quot;id\&quot;: 1,                 \&quot;context\&quot;: {                      \&quot;categories\&quot;: {                           \&quot;Category ID\&quot;: \&quot;1\&quot;,                           \&quot;Category Name\&quot;: \&quot;Alimentação\&quot;                      },                      \&quot;brands\&quot;: {                           \&quot;Brand ID\&quot;: \&quot;2000002\&quot;,                           \&quot;Brand Name\&quot;: \&quot;Whiskas\&quot;                      },                      \&quot;markupRange\&quot;: {                           \&quot;from\&quot;: 0,                           \&quot;to\&quot;: 200                      },                      \&quot;dateRange\&quot;: {                           \&quot;from\&quot;: \&quot;2022-01-23T19:00:00.000Z\&quot;,                           \&quot;to\&quot;: \&quot;2023-10-26T00:00:00.000Z\&quot;                      }                 },                 \&quot;percentualModifier\&quot;: 0            }      ]  }  &#x60;&#x60;&#x60;

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

let apiInstance = new PricingApi.PriceTablesApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let priceTableId = "priceTableId_example"; // String | Price Table Name.
let opts = {
  'pricingPipelineCatalogPriceTableIdPutRequest': new PricingApi.PricingPipelineCatalogPriceTableIdPutRequest() // PricingPipelineCatalogPriceTableIdPutRequest | 
};
apiInstance.pricingPipelineCatalogPriceTableIdPut(contentType, accept, priceTableId, opts, (error, data, response) => {
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
 **priceTableId** | **String**| Price Table Name. | 
 **pricingPipelineCatalogPriceTableIdPutRequest** | [**PricingPipelineCatalogPriceTableIdPutRequest**](PricingPipelineCatalogPriceTableIdPutRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

