# NumberInsightApi.DefaultApi

All URIs are relative to *https://api.nexmo.com/ni*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNumberInsightAdvanced**](DefaultApi.md#getNumberInsightAdvanced) | **GET** /advanced/{format} | Advanced Number Insight (sync)
[**getNumberInsightAsync**](DefaultApi.md#getNumberInsightAsync) | **GET** /advanced/async/{format} | Advanced Number Insight (async)
[**getNumberInsightBasic**](DefaultApi.md#getNumberInsightBasic) | **GET** /basic/{format} | Basic Number Insight
[**getNumberInsightStandard**](DefaultApi.md#getNumberInsightStandard) | **GET** /standard/{format} | Standard Number Insight



## getNumberInsightAdvanced

> GetNumberInsightAdvanced200Response getNumberInsightAdvanced(format, number, opts)

Advanced Number Insight (sync)

Provides [advanced number insight](/number-insight/overview#basic-standard-and-advanced-apis) information about a number synchronously, in the same way that the basic and standard endpoints do.  Vonage recommends accessing the Advanced API **asynchronously** using the &#x60;/advanced/async&#x60; endpoint, to avoid timeouts.  Note that this endpoint also supports &#x60;POST&#x60; requests. 

### Example

```javascript
import NumberInsightApi from 'number_insight_api';
let defaultClient = NumberInsightApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';
// Configure API key authorization: apiSecret
let apiSecret = defaultClient.authentications['apiSecret'];
apiSecret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiSecret.apiKeyPrefix = 'Token';

let apiInstance = new NumberInsightApi.DefaultApi();
let format = "json"; // String | The format of the response
let number = "447700900000"; // String | A single phone number that you need insight about in national or international format.
let opts = {
  'realTimeData': true, // Boolean | A boolean to choose whether to get real time data back in the response.
  'country': "GB", // String | If a number does not have a country code or is uncertain, set the two-character country code. This code must be in ISO 3166-1 alpha-2 format and in upper case. For example, GB or US. If you set country and number is already in [E.164](https://en.wikipedia.org/wiki/E.164) format, country must match the country code in number.
  'cnam': true, // Boolean | Indicates if the name of the person who owns the phone number should be looked up and returned in the response. Set to true to receive phone number owner name in the response. This features is available for US numbers only and incurs an additional charge.
  'ip': "123.0.0.255" // String | This parameter is deprecated as we are no longer able to retrieve reliable IP data globally from carriers. 
};
apiInstance.getNumberInsightAdvanced(format, number, opts, (error, data, response) => {
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
 **format** | **String**| The format of the response | 
 **number** | **String**| A single phone number that you need insight about in national or international format. | 
 **realTimeData** | **Boolean**| A boolean to choose whether to get real time data back in the response. | [optional] 
 **country** | **String**| If a number does not have a country code or is uncertain, set the two-character country code. This code must be in ISO 3166-1 alpha-2 format and in upper case. For example, GB or US. If you set country and number is already in [E.164](https://en.wikipedia.org/wiki/E.164) format, country must match the country code in number. | [optional] 
 **cnam** | **Boolean**| Indicates if the name of the person who owns the phone number should be looked up and returned in the response. Set to true to receive phone number owner name in the response. This features is available for US numbers only and incurs an additional charge. | [optional] [default to false]
 **ip** | **String**| This parameter is deprecated as we are no longer able to retrieve reliable IP data globally from carriers.  | [optional] 

### Return type

[**GetNumberInsightAdvanced200Response**](GetNumberInsightAdvanced200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [apiSecret](../README.md#apiSecret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/xml


## getNumberInsightAsync

> GetNumberInsightAsync200Response getNumberInsightAsync(format, callback, number, opts)

Advanced Number Insight (async)

Provides [advanced number insight](/number-insight/overview#basic-standard-and-advanced-apis) number information **asynchronously** using the URL specified in the &#x60;callback&#x60; parameter.  recommends asynchronous use of the Number Insight Advanced API, to avoid timeouts.  Note that this endpoint also supports &#x60;POST&#x60; requests. 

### Example

```javascript
import NumberInsightApi from 'number_insight_api';
let defaultClient = NumberInsightApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';
// Configure API key authorization: apiSecret
let apiSecret = defaultClient.authentications['apiSecret'];
apiSecret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiSecret.apiKeyPrefix = 'Token';

let apiInstance = new NumberInsightApi.DefaultApi();
let format = "json"; // String | The format of the response
let callback = "https://example.com/callback"; // String | The callback URL
let number = "447700900000"; // String | A single phone number that you need insight about in national or international format.
let opts = {
  'country': "GB", // String | If a number does not have a country code or is uncertain, set the two-character country code. This code must be in ISO 3166-1 alpha-2 format and in upper case. For example, GB or US. If you set country and number is already in [E.164](https://en.wikipedia.org/wiki/E.164) format, country must match the country code in number.
  'cnam': true, // Boolean | Indicates if the name of the person who owns the phone number should be looked up and returned in the response. Set to true to receive phone number owner name in the response. This features is available for US numbers only and incurs an additional charge.
  'ip': "123.0.0.255" // String | This parameter is deprecated as we are no longer able to retrieve reliable IP data globally from carriers. 
};
apiInstance.getNumberInsightAsync(format, callback, number, opts, (error, data, response) => {
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
 **format** | **String**| The format of the response | 
 **callback** | **String**| The callback URL | 
 **number** | **String**| A single phone number that you need insight about in national or international format. | 
 **country** | **String**| If a number does not have a country code or is uncertain, set the two-character country code. This code must be in ISO 3166-1 alpha-2 format and in upper case. For example, GB or US. If you set country and number is already in [E.164](https://en.wikipedia.org/wiki/E.164) format, country must match the country code in number. | [optional] 
 **cnam** | **Boolean**| Indicates if the name of the person who owns the phone number should be looked up and returned in the response. Set to true to receive phone number owner name in the response. This features is available for US numbers only and incurs an additional charge. | [optional] [default to false]
 **ip** | **String**| This parameter is deprecated as we are no longer able to retrieve reliable IP data globally from carriers.  | [optional] 

### Return type

[**GetNumberInsightAsync200Response**](GetNumberInsightAsync200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [apiSecret](../README.md#apiSecret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/xml


## getNumberInsightBasic

> NiResponseJsonBasic getNumberInsightBasic(format, number, opts)

Basic Number Insight

Provides [basic number insight](/number-insight/overview#basic-standard-and-advanced-apis) information about a number.  Note that this endpoint also supports &#x60;POST&#x60; requests. 

### Example

```javascript
import NumberInsightApi from 'number_insight_api';
let defaultClient = NumberInsightApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';
// Configure API key authorization: apiSecret
let apiSecret = defaultClient.authentications['apiSecret'];
apiSecret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiSecret.apiKeyPrefix = 'Token';

let apiInstance = new NumberInsightApi.DefaultApi();
let format = "json"; // String | The format of the response
let number = "447700900000"; // String | A single phone number that you need insight about in national or international format.
let opts = {
  'country': "GB" // String | If a number does not have a country code or is uncertain, set the two-character country code. This code must be in ISO 3166-1 alpha-2 format and in upper case. For example, GB or US. If you set country and number is already in [E.164](https://en.wikipedia.org/wiki/E.164) format, country must match the country code in number.
};
apiInstance.getNumberInsightBasic(format, number, opts, (error, data, response) => {
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
 **format** | **String**| The format of the response | 
 **number** | **String**| A single phone number that you need insight about in national or international format. | 
 **country** | **String**| If a number does not have a country code or is uncertain, set the two-character country code. This code must be in ISO 3166-1 alpha-2 format and in upper case. For example, GB or US. If you set country and number is already in [E.164](https://en.wikipedia.org/wiki/E.164) format, country must match the country code in number. | [optional] 

### Return type

[**NiResponseJsonBasic**](NiResponseJsonBasic.md)

### Authorization

[apiKey](../README.md#apiKey), [apiSecret](../README.md#apiSecret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/xml


## getNumberInsightStandard

> GetNumberInsightStandard200Response getNumberInsightStandard(format, number, opts)

Standard Number Insight

Provides [standard number insight](/number-insight/overview#basic-standard-and-advanced-apis) information about a number.  Note that this endpoint also supports &#x60;POST&#x60; requests. 

### Example

```javascript
import NumberInsightApi from 'number_insight_api';
let defaultClient = NumberInsightApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';
// Configure API key authorization: apiSecret
let apiSecret = defaultClient.authentications['apiSecret'];
apiSecret.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiSecret.apiKeyPrefix = 'Token';

let apiInstance = new NumberInsightApi.DefaultApi();
let format = "json"; // String | The format of the response
let number = "447700900000"; // String | A single phone number that you need insight about in national or international format.
let opts = {
  'country': "GB", // String | If a number does not have a country code or is uncertain, set the two-character country code. This code must be in ISO 3166-1 alpha-2 format and in upper case. For example, GB or US. If you set country and number is already in [E.164](https://en.wikipedia.org/wiki/E.164) format, country must match the country code in number.
  'cnam': true // Boolean | Indicates if the name of the person who owns the phone number should be looked up and returned in the response. Set to true to receive phone number owner name in the response. This features is available for US numbers only and incurs an additional charge.
};
apiInstance.getNumberInsightStandard(format, number, opts, (error, data, response) => {
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
 **format** | **String**| The format of the response | 
 **number** | **String**| A single phone number that you need insight about in national or international format. | 
 **country** | **String**| If a number does not have a country code or is uncertain, set the two-character country code. This code must be in ISO 3166-1 alpha-2 format and in upper case. For example, GB or US. If you set country and number is already in [E.164](https://en.wikipedia.org/wiki/E.164) format, country must match the country code in number. | [optional] 
 **cnam** | **Boolean**| Indicates if the name of the person who owns the phone number should be looked up and returned in the response. Set to true to receive phone number owner name in the response. This features is available for US numbers only and incurs an additional charge. | [optional] [default to false]

### Return type

[**GetNumberInsightStandard200Response**](GetNumberInsightStandard200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [apiSecret](../README.md#apiSecret)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/xml

