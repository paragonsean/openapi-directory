# BikeWiseApiV2.LocationsApi

All URIs are relative to *https://bikewise.org/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gETVersionLocationsFormat**](LocationsApi.md#gETVersionLocationsFormat) | **GET** /v2/locations | Unpaginated geojson response
[**gETVersionLocationsMarkersFormat**](LocationsApi.md#gETVersionLocationsMarkersFormat) | **GET** /v2/locations/markers | Unpaginated geojson response with simplestyled markers



## gETVersionLocationsFormat

> gETVersionLocationsFormat(opts)

Unpaginated geojson response

&lt;p&gt;&lt;strong&gt;This endpoint behaves exactly like&lt;/strong&gt; &lt;code&gt;incidents&lt;/code&gt;, but returns a valid geojson &lt;code&gt;FeatureCollection&lt;/code&gt; that looks like this:&lt;/p&gt;  &lt;pre&gt;&lt;code&gt;{   type: \&quot;FeatureCollection\&quot;,   features: [     {       type: \&quot;Feature\&quot;,       properties: {       id: 4474199,       type: \&quot;Theft\&quot;,       occurred_at: 1428536937     },       geometry: {       type: \&quot;Point\&quot;,       coordinates: [ -122.6244177, 45.5164386 ]     }   } } &lt;/code&gt;&lt;/pre&gt;  &lt;p&gt;It doesn’t paginate. If you pass the &lt;code&gt;all&lt;/code&gt; parameter it returns all matches (which can be big, &amp;gt; 4mb), otherwise it returns the 100 most recent.&lt;/p&gt;  &lt;p&gt;&lt;strong&gt;Go forth and make maps!&lt;/strong&gt;&lt;/p&gt; 

### Example

```javascript
import BikeWiseApiV2 from 'bike_wise_api_v2';

let apiInstance = new BikeWiseApiV2.LocationsApi();
let opts = {
  'occurredBefore': 56, // Number | <p>End of period</p> 
  'occurredAfter': 56, // Number | <p>Start of period</p> 
  'incidentType': "incidentType_example", // String | <p>Only incidents of specific type</p> 
  'proximity': "proximity_example", // String | <p>Center of location for proximity search</p> 
  'proximitySquare': 100, // Number | <p>Size of the proximity search</p> 
  'query': "query_example", // String | <p>Full text search of incidents</p> 
  'limit': 56, // Number | <p>Max number of results to return. Defaults to 100</p> 
  'all': true // Boolean | <p>Give ‘em all to me. Will ignore limit</p> 
};
apiInstance.gETVersionLocationsFormat(opts, (error, data, response) => {
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
 **occurredBefore** | **Number**| &lt;p&gt;End of period&lt;/p&gt;  | [optional] 
 **occurredAfter** | **Number**| &lt;p&gt;Start of period&lt;/p&gt;  | [optional] 
 **incidentType** | **String**| &lt;p&gt;Only incidents of specific type&lt;/p&gt;  | [optional] 
 **proximity** | **String**| &lt;p&gt;Center of location for proximity search&lt;/p&gt;  | [optional] 
 **proximitySquare** | **Number**| &lt;p&gt;Size of the proximity search&lt;/p&gt;  | [optional] [default to 100]
 **query** | **String**| &lt;p&gt;Full text search of incidents&lt;/p&gt;  | [optional] 
 **limit** | **Number**| &lt;p&gt;Max number of results to return. Defaults to 100&lt;/p&gt;  | [optional] 
 **all** | **Boolean**| &lt;p&gt;Give ‘em all to me. Will ignore limit&lt;/p&gt;  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## gETVersionLocationsMarkersFormat

> gETVersionLocationsMarkersFormat(opts)

Unpaginated geojson response with simplestyled markers

&lt;p&gt;This behaves exactly like the root &lt;code&gt;locations&lt;/code&gt; endpoint, but returns &lt;a href&#x3D;\&quot;https://github.com/mapbox/simplestyle-spec\&quot;&gt;simplestyled markers&lt;/a&gt; (&lt;a href&#x3D;\&quot;https://www.mapbox.com/guides/markers/#simple-style\&quot;&gt;mapbox styled markers&lt;/a&gt;)&lt;/p&gt;  &lt;p&gt;&lt;strong&gt;Go forth and make maps!&lt;/strong&gt;&lt;/p&gt; 

### Example

```javascript
import BikeWiseApiV2 from 'bike_wise_api_v2';

let apiInstance = new BikeWiseApiV2.LocationsApi();
let opts = {
  'occurredBefore': 56, // Number | <p>End of period</p> 
  'occurredAfter': 56, // Number | <p>Start of period</p> 
  'incidentType': "incidentType_example", // String | <p>Only incidents of specific type</p> 
  'proximity': "proximity_example", // String | <p>Center of location for proximity search</p> 
  'proximitySquare': 100, // Number | <p>Size of the proximity search</p> 
  'query': "query_example", // String | <p>Full text search of incidents</p> 
  'limit': 56, // Number | <p>Max number of results to return. Defaults to 100</p> 
  'all': true // Boolean | <p>Give ‘em all to me. Will ignore limit</p> 
};
apiInstance.gETVersionLocationsMarkersFormat(opts, (error, data, response) => {
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
 **occurredBefore** | **Number**| &lt;p&gt;End of period&lt;/p&gt;  | [optional] 
 **occurredAfter** | **Number**| &lt;p&gt;Start of period&lt;/p&gt;  | [optional] 
 **incidentType** | **String**| &lt;p&gt;Only incidents of specific type&lt;/p&gt;  | [optional] 
 **proximity** | **String**| &lt;p&gt;Center of location for proximity search&lt;/p&gt;  | [optional] 
 **proximitySquare** | **Number**| &lt;p&gt;Size of the proximity search&lt;/p&gt;  | [optional] [default to 100]
 **query** | **String**| &lt;p&gt;Full text search of incidents&lt;/p&gt;  | [optional] 
 **limit** | **Number**| &lt;p&gt;Max number of results to return. Defaults to 100&lt;/p&gt;  | [optional] 
 **all** | **Boolean**| &lt;p&gt;Give ‘em all to me. Will ignore limit&lt;/p&gt;  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

