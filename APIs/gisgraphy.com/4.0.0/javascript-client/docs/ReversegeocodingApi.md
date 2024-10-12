# GisgraphyWebservices.ReversegeocodingApi

All URIs are relative to *http://free.gisgraphy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reversegeocode**](ReversegeocodingApi.md#reversegeocode) | **GET** /reversegeocoding/reversegeocode | Reverse geocode an address



## reversegeocode

> AddressResultsDto reversegeocode(lat, lng, opts)

Reverse geocode an address

The Reverse geocoding service allows to search for an address for a given GPS position.

### Example

```javascript
import GisgraphyWebservices from 'gisgraphy_webservices';
let defaultClient = GisgraphyWebservices.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new GisgraphyWebservices.ReversegeocodingApi();
let lat = 3.4; // Number | The latitude (north-south) for the location point to search around. The value is a floating number, between -90 and +90. It uses GPS coordinates
let lng = 3.4; // Number | TThe longitude (east-West) for the location point to search around. The value is a floating number between -180 and +180. It uses GPS coordinates.
let opts = {
  'format': "'XML'", // String | The output format.
  'from': 1, // Number | The first pagination index. Numbered from 1. If the number is < 1 or not specified, it will be set to the default value : 1
  'to': 10, // Number | The last pagination index. if < 1 or not specified, it will be set to startindex + 10. Max = 10 (can be changed)
  'callback': "callback_example", // String | The callback method name (optional), use to wrap the content into a (alphanumeric) Javascript method. Works only for script output formats (JSON, PHP, Ruby, Python)
  'indent': false // Boolean | indents the results. Possible values are true or false (or on when used with the rest service. If you use a checkbox in a web form, to indent the results, the value will be 'on' or 'off', so for a simple use : the value of indent can be 'true' or 'on'
};
apiInstance.reversegeocode(lat, lng, opts, (error, data, response) => {
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
 **lat** | **Number**| The latitude (north-south) for the location point to search around. The value is a floating number, between -90 and +90. It uses GPS coordinates | 
 **lng** | **Number**| TThe longitude (east-West) for the location point to search around. The value is a floating number between -180 and +180. It uses GPS coordinates. | 
 **format** | **String**| The output format. | [optional] [default to &#39;XML&#39;]
 **from** | **Number**| The first pagination index. Numbered from 1. If the number is &lt; 1 or not specified, it will be set to the default value : 1 | [optional] [default to 1]
 **to** | **Number**| The last pagination index. if &lt; 1 or not specified, it will be set to startindex + 10. Max &#x3D; 10 (can be changed) | [optional] [default to 10]
 **callback** | **String**| The callback method name (optional), use to wrap the content into a (alphanumeric) Javascript method. Works only for script output formats (JSON, PHP, Ruby, Python) | [optional] 
 **indent** | **Boolean**| indents the results. Possible values are true or false (or on when used with the rest service. If you use a checkbox in a web form, to indent the results, the value will be &#39;on&#39; or &#39;off&#39;, so for a simple use : the value of indent can be &#39;true&#39; or &#39;on&#39; | [optional] [default to false]

### Return type

[**AddressResultsDto**](AddressResultsDto.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, application/php, application/ruby, application/yaml, application/python, text/plain

