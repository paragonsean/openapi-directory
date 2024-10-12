# PricingApi.PricingConfigurationApi

All URIs are relative to *https://vtex.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getPricingConfig**](PricingConfigurationApi.md#getPricingConfig) | **GET** /pricing/config | Get Pricing Configuration
[**getPricingv2Status**](PricingConfigurationApi.md#getPricingv2Status) | **GET** /pricing/migration | Get Pricing v2 Status



## getPricingConfig

> PricingConfiguration getPricingConfig(contentType, accept)

Get Pricing Configuration

Retrieves Pricing Configuration.  ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;hasMigrated\&quot;: true,      \&quot;migrationStatus\&quot;: \&quot;Completed\&quot;,      \&quot;defaultMarkup\&quot;: 100,      \&quot;priceVariation\&quot;: {          \&quot;upperLimit\&quot;: null,          \&quot;lowerLimit\&quot;: null      },      \&quot;minimumMarkups\&quot;: {          \&quot;1\&quot;: 100,          \&quot;2\&quot;: 90      },      \&quot;tradePolicyConfigs\&quot;: [],      \&quot;sellersToOverride\&quot;: [],      \&quot;hasPriceInheritance\&quot;: false,      \&quot;priceInheritance\&quot;: \&quot;never\&quot;,      \&quot;hasOptionalBasePrice\&quot;: false,      \&quot;blockAccount\&quot;: false,      \&quot;blockedRoutes\&quot;: null,      \&quot;priceTableSelectionStrategy\&quot;: \&quot;first\&quot;,      \&quot;priceTableLimit\&quot;: null  }  &#x60;&#x60;&#x60;

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

let apiInstance = new PricingApi.PricingConfigurationApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
apiInstance.getPricingConfig(contentType, accept, (error, data, response) => {
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

[**PricingConfiguration**](PricingConfiguration.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8


## getPricingv2Status

> GetPricingv2Status200Response getPricingv2Status(contentType, accept)

Get Pricing v2 Status

Retrieves Pricing v2 Status.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;isActive\&quot;: true,      \&quot;hasMigrated\&quot;: true  }  &#x60;&#x60;&#x60;

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

let apiInstance = new PricingApi.PricingConfigurationApi();
let contentType = "'application/json'"; // String | Describes the type of the content being sent.
let accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
apiInstance.getPricingv2Status(contentType, accept, (error, data, response) => {
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

[**GetPricingv2Status200Response**](GetPricingv2Status200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json; charset=utf-8

