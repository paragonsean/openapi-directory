# GisgraphyWebservices.GeolocalisationApi

All URIs are relative to *http://free.gisgraphy.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geoloc**](GeolocalisationApi.md#geoloc) | **GET** /geoloc/search | Geocode an address



## geoloc

> GeolocResultsDto geoloc(lat, lng, opts)

Geocode an address

The geolocalisation service allows to search for features around a earth location. you can Specify GPS position, Limit the results to a specific place type (e.g : search all monuments around a point), Limit the results to a specified radius, Paginate the results, Tells if you want the output to be indented (currently, applies only for XML, not JSON for performance reasons. May change in next version)

### Example

```javascript
import GisgraphyWebservices from 'gisgraphy_webservices';
let defaultClient = GisgraphyWebservices.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new GisgraphyWebservices.GeolocalisationApi();
let lat = 3.4; // Number | The latitude (north-south) for the location point to search around. The value is a floating number, between -90 and +90. It uses GPS coordinates
let lng = 3.4; // Number | TThe longitude (east-West) for the location point to search around. The value is a floating number between -180 and +180. It uses GPS coordinates.
let opts = {
  'radius': 10000.0, // Number | distance from the location point in meters we'd like to search around. The value is a number > 0 if it is not specify or incorrect.
  'distance': true, // Boolean | Whether (or not) we want the distance field to be output. This option is useful to improve the performance if we don't care about the distance (e.g : we search for name). Of course, the results won't be sorted by distance. If you use a checkbox in a form to indent the results, the value will be 'on' or 'off', so to simplify the use : the value for the web service can be 'true' or 'on'
  'placetype': "placetype_example", // String | filter search for a given placetype
  'format': "'XML'", // String | The output format.
  'from': 1, // Number | The first pagination index. Numbered from 1. If the number is < 1 or not specified, it will be set to the default value : 1
  'to': 10, // Number | The last pagination index. if < 1 or not specified, it will be set to startindex + 10. Max = 10 (can be changed)
  'callback': "callback_example", // String | The callback method name (optional), use to wrap the content into a (alphanumeric) Javascript method. Works only for script output formats (JSON, PHP, Ruby, Python)
  'indent': false // Boolean | indents the results.Default to false. Possible values are true or false (or on when used with the rest service. If you use a checkbox in a web form, to indent the results, the value will be 'on' or 'off', so for a simple use : the value of indent can be 'true' or 'on'
};
apiInstance.geoloc(lat, lng, opts, (error, data, response) => {
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
 **radius** | **Number**| distance from the location point in meters we&#39;d like to search around. The value is a number &gt; 0 if it is not specify or incorrect. | [optional] [default to 10000.0]
 **distance** | **Boolean**| Whether (or not) we want the distance field to be output. This option is useful to improve the performance if we don&#39;t care about the distance (e.g : we search for name). Of course, the results won&#39;t be sorted by distance. If you use a checkbox in a form to indent the results, the value will be &#39;on&#39; or &#39;off&#39;, so to simplify the use : the value for the web service can be &#39;true&#39; or &#39;on&#39; | [optional] [default to true]
 **placetype** | **String**| filter search for a given placetype | [optional] 
 **format** | **String**| The output format. | [optional] [default to &#39;XML&#39;]
 **from** | **Number**| The first pagination index. Numbered from 1. If the number is &lt; 1 or not specified, it will be set to the default value : 1 | [optional] [default to 1]
 **to** | **Number**| The last pagination index. if &lt; 1 or not specified, it will be set to startindex + 10. Max &#x3D; 10 (can be changed) | [optional] [default to 10]
 **callback** | **String**| The callback method name (optional), use to wrap the content into a (alphanumeric) Javascript method. Works only for script output formats (JSON, PHP, Ruby, Python) | [optional] 
 **indent** | **Boolean**| indents the results.Default to false. Possible values are true or false (or on when used with the rest service. If you use a checkbox in a web form, to indent the results, the value will be &#39;on&#39; or &#39;off&#39;, so for a simple use : the value of indent can be &#39;true&#39; or &#39;on&#39; | [optional] [default to false]

### Return type

[**GeolocResultsDto**](GeolocResultsDto.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, application/php, application/ruby, application/yaml, application/python, text/plain

