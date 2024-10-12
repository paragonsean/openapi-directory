# CatalogApi.SalesChannelApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesChannelList**](SalesChannelApi.md#salesChannelList) | **GET** /api/catalog_system/pvt/saleschannel/list | Get Sales Channel List
[**salesChannelbyId**](SalesChannelApi.md#salesChannelbyId) | **GET** /api/catalog_system/pub/saleschannel/{salesChannelId} | Get Sales Channel by ID



## salesChannelList

> [SalesChannelbyId200Response] salesChannelList(contentType, accept)

Get Sales Channel List

Retrieves a list with details about the store&#39;s sales channels.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 1,          \&quot;Name\&quot;: \&quot;Loja Principal\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;ProductClusterId\&quot;: null,          \&quot;CountryCode\&quot;: \&quot;BRA\&quot;,          \&quot;CultureInfo\&quot;: \&quot;pt-BR\&quot;,          \&quot;TimeZone\&quot;: \&quot;E. South America Standard Time\&quot;,          \&quot;CurrencyCode\&quot;: \&quot;BRL\&quot;,          \&quot;CurrencySymbol\&quot;: \&quot;R$\&quot;,          \&quot;CurrencyLocale\&quot;: 1046,          \&quot;CurrencyFormatInfo\&quot;: {              \&quot;CurrencyDecimalDigits\&quot;: 1,              \&quot;CurrencyDecimalSeparator\&quot;: \&quot;,\&quot;,              \&quot;CurrencyGroupSeparator\&quot;: \&quot;.\&quot;,              \&quot;CurrencyGroupSize\&quot;: 3,              \&quot;StartsWithCurrencySymbol\&quot;: true          },          \&quot;Origin\&quot;: null,          \&quot;Position\&quot;: 2,          \&quot;ConditionRule\&quot;: null,          \&quot;CurrencyDecimalDigits\&quot;: 1      }  ]  &#x60;&#x60;&#x60;

### Example

```javascript
import CatalogApi from 'catalog_api';
let defaultClient = CatalogApi.ApiClient.instance;
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

let apiInstance = new CatalogApi.SalesChannelApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
apiInstance.salesChannelList(contentType, accept, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]

### Return type

[**[SalesChannelbyId200Response]**](SalesChannelbyId200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## salesChannelbyId

> SalesChannelbyId200Response salesChannelbyId(contentType, accept, salesChannelId)

Get Sales Channel by ID

Retrieves a specific sales channel by its ID.     ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;Name\&quot;: \&quot;Loja Principal\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;ProductClusterId\&quot;: null,      \&quot;CountryCode\&quot;: \&quot;BRA\&quot;,      \&quot;CultureInfo\&quot;: \&quot;pt-BR\&quot;,      \&quot;TimeZone\&quot;: \&quot;E. South America Standard Time\&quot;,      \&quot;CurrencyCode\&quot;: \&quot;BRL\&quot;,      \&quot;CurrencySymbol\&quot;: \&quot;R$\&quot;,      \&quot;CurrencyLocale\&quot;: 1046,      \&quot;CurrencyFormatInfo\&quot;: {          \&quot;CurrencyDecimalDigits\&quot;: 1,          \&quot;CurrencyDecimalSeparator\&quot;: \&quot;,\&quot;,          \&quot;CurrencyGroupSeparator\&quot;: \&quot;.\&quot;,          \&quot;CurrencyGroupSize\&quot;: 3,          \&quot;StartsWithCurrencySymbol\&quot;: true      },      \&quot;Origin\&quot;: null,      \&quot;Position\&quot;: 2,      \&quot;ConditionRule\&quot;: null,      \&quot;CurrencyDecimalDigits\&quot;: 1  }  &#x60;&#x60;&#x60;

### Example

```javascript
import CatalogApi from 'catalog_api';
let defaultClient = CatalogApi.ApiClient.instance;
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

let apiInstance = new CatalogApi.SalesChannelApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "'application/json'"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
let salesChannelId = "1"; // String | 
apiInstance.salesChannelbyId(contentType, accept, salesChannelId, (error, data, response) => {
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
 **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to &#39;application/json&#39;]
 **salesChannelId** | **String**|  | 

### Return type

[**SalesChannelbyId200Response**](SalesChannelbyId200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

