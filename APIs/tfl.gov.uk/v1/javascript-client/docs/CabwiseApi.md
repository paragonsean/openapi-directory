# TransportForLondonUnifiedApi.CabwiseApi

All URIs are relative to *https://api.digital.tfl.gov.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cabwiseGet**](CabwiseApi.md#cabwiseGet) | **GET** /Cabwise/search | Gets taxis and minicabs contact information



## cabwiseGet

> Object cabwiseGet(lat, lon, opts)

Gets taxis and minicabs contact information

### Example

```javascript
import TransportForLondonUnifiedApi from 'transport_for_london_unified_api';

let apiInstance = new TransportForLondonUnifiedApi.CabwiseApi();
let lat = 3.4; // Number | Latitude
let lon = 3.4; // Number | Longitude
let opts = {
  'optype': "optype_example", // String | Operator Type e.g Minicab, Executive, Limousine
  'wc': "wc_example", // String | Wheelchair accessible
  'radius': 3.4, // Number | The radius of the bounding circle in metres
  'name': "name_example", // String | Trading name of operating company
  'maxResults': 56, // Number | An optional parameter to limit the number of results return. Default and maximum is 20.
  'legacyFormat': true, // Boolean | Legacy Format
  'forceXml': true, // Boolean | Force Xml
  'twentyFourSevenOnly': true // Boolean | Twenty Four Seven Only
};
apiInstance.cabwiseGet(lat, lon, opts, (error, data, response) => {
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
 **lat** | **Number**| Latitude | 
 **lon** | **Number**| Longitude | 
 **optype** | **String**| Operator Type e.g Minicab, Executive, Limousine | [optional] 
 **wc** | **String**| Wheelchair accessible | [optional] 
 **radius** | **Number**| The radius of the bounding circle in metres | [optional] 
 **name** | **String**| Trading name of operating company | [optional] 
 **maxResults** | **Number**| An optional parameter to limit the number of results return. Default and maximum is 20. | [optional] 
 **legacyFormat** | **Boolean**| Legacy Format | [optional] 
 **forceXml** | **Boolean**| Force Xml | [optional] 
 **twentyFourSevenOnly** | **Boolean**| Twenty Four Seven Only | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml

