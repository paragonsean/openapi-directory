# OpenCageGeocoder.DefaultApi

All URIs are relative to *https://api.opencagedata.com/geocode*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vversionFormatGet**](DefaultApi.md#vversionFormatGet) | **GET** /v{version}/{format} | 



## vversionFormatGet

> Response vversionFormatGet(version, format, q, key, opts)



geocode a query

### Example

```javascript
import OpenCageGeocoder from 'open_cage_geocoder';

let apiInstance = new OpenCageGeocoder.DefaultApi();
let version = 56; // Number | API version.
let format = "format_example"; // String | format of the response. One of 'json', 'xml' or 'map'.
let q = "q_example"; // String | string or lat,lng to be geocoded.
let key = "key_example"; // String | an application key.
let opts = {
  'abbrv': true, // Boolean | when true we attempt to abbreviate the formatted field of results.
  'addressOnly': true, // Boolean | when true we include only address details in the formatted field of results.
  'addRequest': true, // Boolean | if true the request is included in the response.
  'bounds': "bounds_example", // String | four coordinate points forming the south-west and north-east corners of a bounding box (min long, min lat, max long, max lat).
  'countrycode': "countrycode_example", // String | two letter code ISO 3166-1 Alpha 2 code to limit results to that country.
  'jsonp': "jsonp_example", // String | wraps the returned JSON with a function name.
  'language': "language_example", // String | an IETF format language code (ex: 'es' or 'pt-BR').
  'limit': 56, // Number | maximum number of results to return. Default is 10. Maximum is 100.
  'minConfidence': 56, // Number | integer from 1-10. Only results with at least this confidence are returned.
  'noAnnotations': true, // Boolean | when true annotations are not added to results.
  'noDedupe': true, // Boolean | when true results are not deduplicated.
  'noRecord': true, // Boolean | when true query content is not logged.
  'pretty': true, // Boolean | when true results are pretty printed. Useful for debugging.
  'proximity': "proximity_example", // String | lat,lng to bias results.
  'roadinfo': true // Boolean | match nearest road, include roadinfo annotation
};
apiInstance.vversionFormatGet(version, format, q, key, opts, (error, data, response) => {
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
 **version** | **Number**| API version. | 
 **format** | **String**| format of the response. One of &#39;json&#39;, &#39;xml&#39; or &#39;map&#39;. | 
 **q** | **String**| string or lat,lng to be geocoded. | 
 **key** | **String**| an application key. | 
 **abbrv** | **Boolean**| when true we attempt to abbreviate the formatted field of results. | [optional] 
 **addressOnly** | **Boolean**| when true we include only address details in the formatted field of results. | [optional] 
 **addRequest** | **Boolean**| if true the request is included in the response. | [optional] 
 **bounds** | **String**| four coordinate points forming the south-west and north-east corners of a bounding box (min long, min lat, max long, max lat). | [optional] 
 **countrycode** | **String**| two letter code ISO 3166-1 Alpha 2 code to limit results to that country. | [optional] 
 **jsonp** | **String**| wraps the returned JSON with a function name. | [optional] 
 **language** | **String**| an IETF format language code (ex: &#39;es&#39; or &#39;pt-BR&#39;). | [optional] 
 **limit** | **Number**| maximum number of results to return. Default is 10. Maximum is 100. | [optional] 
 **minConfidence** | **Number**| integer from 1-10. Only results with at least this confidence are returned. | [optional] 
 **noAnnotations** | **Boolean**| when true annotations are not added to results. | [optional] 
 **noDedupe** | **Boolean**| when true results are not deduplicated. | [optional] 
 **noRecord** | **Boolean**| when true query content is not logged. | [optional] 
 **pretty** | **Boolean**| when true results are pretty printed. Useful for debugging. | [optional] 
 **proximity** | **String**| lat,lng to bias results. | [optional] 
 **roadinfo** | **Boolean**| match nearest road, include roadinfo annotation | [optional] 

### Return type

[**Response**](Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/html

