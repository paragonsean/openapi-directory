# GisgraphyWebservices.AddressparserStandardizerApi

All URIs are relative to *http://free.gisgraphy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addressparsing**](AddressparserStandardizerApi.md#addressparsing) | **GET** /addressparser/parse | split a raw address into several parts



## addressparsing

> AddressResultsDto addressparsing(address, opts)

split a raw address into several parts

The address parser and address standardizer, are part of the Gisgraphy project (free open source worldwide geocoder). Address parsing is the process of dividing a single address string into its individual component parts. Please visit [http://www.address-parser.net](http://www.address-parser.net) for more details 

### Example

```javascript
import GisgraphyWebservices from 'gisgraphy_webservices';
let defaultClient = GisgraphyWebservices.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new GisgraphyWebservices.AddressparserStandardizerApi();
let address = "address_example"; // String | A postal address.
let opts = {
  'country': "country_example", // String | The ISO 3166 Alpha 2 code of the country.
  'format': "'XML'", // String | The output format.
  'callback': "callback_example", // String | The callback method name (optional), use to wrap the content into a (alphanumeric) Javascript method. Works only for script output formats (JSON, PHP, Ruby, Python)
  'indent': false, // Boolean | indents the results.Default to false. Possible values are true or false (or on when used with the rest service. If you use a checkbox in a web form, to indent the results, the value will be 'on' or 'off', so for a simple use : the value of indent can be 'true' or 'on'
  'standardize': false, // Boolean | Whether the address should be standardized after parsing, the value will be 'on' or 'off', so for a simple use : the value of indent can be 'true' or 'on'
  'geocode': false // Boolean | UNUSED YET. Whether the address should be geocoded after parsing, the value will be 'on' or 'off', so for a simple use : the value of indent can be 'true' or 'on'
};
apiInstance.addressparsing(address, opts, (error, data, response) => {
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
 **address** | **String**| A postal address. | 
 **country** | **String**| The ISO 3166 Alpha 2 code of the country. | [optional] 
 **format** | **String**| The output format. | [optional] [default to &#39;XML&#39;]
 **callback** | **String**| The callback method name (optional), use to wrap the content into a (alphanumeric) Javascript method. Works only for script output formats (JSON, PHP, Ruby, Python) | [optional] 
 **indent** | **Boolean**| indents the results.Default to false. Possible values are true or false (or on when used with the rest service. If you use a checkbox in a web form, to indent the results, the value will be &#39;on&#39; or &#39;off&#39;, so for a simple use : the value of indent can be &#39;true&#39; or &#39;on&#39; | [optional] [default to false]
 **standardize** | **Boolean**| Whether the address should be standardized after parsing, the value will be &#39;on&#39; or &#39;off&#39;, so for a simple use : the value of indent can be &#39;true&#39; or &#39;on&#39; | [optional] [default to false]
 **geocode** | **Boolean**| UNUSED YET. Whether the address should be geocoded after parsing, the value will be &#39;on&#39; or &#39;off&#39;, so for a simple use : the value of indent can be &#39;true&#39; or &#39;on&#39; | [optional] [default to false]

### Return type

[**AddressResultsDto**](AddressResultsDto.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, application/php, application/ruby, application/yaml, application/python

