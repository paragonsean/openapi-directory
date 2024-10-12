# GeocoderRestApi.IntersectionsApi

All URIs are relative to *https://geocoder.api.gov.bc.ca*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addressesOutputFormatGet_0**](IntersectionsApi.md#addressesOutputFormatGet_0) | **GET** /addresses.{outputFormat} | Geocode an address
[**intersectionsIntersectionIDOutputFormatGet**](IntersectionsApi.md#intersectionsIntersectionIDOutputFormatGet) | **GET** /intersections/{intersectionID}.{outputFormat} | Get an intersection by its unique ID
[**intersectionsNearOutputFormatGet**](IntersectionsApi.md#intersectionsNearOutputFormatGet) | **GET** /intersections/near.{outputFormat} | Find intersections near to a geographic point
[**intersectionsNearestOutputFormatGet**](IntersectionsApi.md#intersectionsNearestOutputFormatGet) | **GET** /intersections/nearest.{outputFormat} | Find nearest intersection to a geographic point
[**intersectionsWithinOutputFormatGet**](IntersectionsApi.md#intersectionsWithinOutputFormatGet) | **GET** /intersections/within.{outputFormat} | Find intersections in a geographic area



## addressesOutputFormatGet_0

> addressesOutputFormatGet_0(outputFormat, opts)

Geocode an address

Represents the set of geocoded and standardized sites and intersections whose address best matches a given query address.

### Example

```javascript
import GeocoderRestApi from 'geocoder_rest_api';
let defaultClient = GeocoderRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new GeocoderRestApi.IntersectionsApi();
let outputFormat = "json"; // String | Results format. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputFormat target=\"_blank\">outputFormat</a>.   Note: GeoJSON and KML formats only support EPSG:4326 (outputSRS=4326)
let opts = {
  'addressString': "525 Superior Street, Victoria, BC", // String | Civic or intersection address as a single string. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#addressString target=\"_blank\">addressString</a>
  'locationDescriptor': "'any'", // String | Describes the nature of the address location. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#locationDescriptor target=\"_blank\">locationDescriptor</a>
  'maxResults': 1, // Number | The maximum number of search results to return.
  'interpolation': "'adaptive'", // String | accessPoint interpolation method. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#interpolation target=\"_blank\">interpolation</a>
  'echo': true, // Boolean | If true, include unmatched address details such as site name in results.
  'brief': false, // Boolean | If true, include only basic match and address details in results. Not supported for shp, csv, and gml formats.
  'autoComplete': false, // Boolean | If true, addressString is expected to contain a partial address that requires completion. Not supported for shp, csv, gml formats.
  'setBack': 0, // Number | The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint.
  'outputSRS': 4326, // Number | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
  'minScore': 1, // Number | The minimum score required for a match to be returned. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#minScore target=\"_blank\">minScore</a>
  'matchPrecision': "matchPrecision_example", // String | Example: street,locality.  A comma separated list of individual match precision levels to include in results. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#matchPrecision target=\"_blank\">matchPrecision</a>
  'matchPrecisionNot': "matchPrecisionNot_example", // String | Example: street,locality.  A comma separated list of individual match precision levels to exclude from results. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#matchPrecisionNot target=\"_blank\">matchPrecisionNot</a>
  'siteName': "siteName_example", // String | A string containing the name of the building, facility, or institution (e.g., Duck Building, Casa Del Mar, Crystal Garden, Bluebird House).See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#siteName target=\"_blank\">siteName</a>
  'unitDesignator': "unitDesignator_example", // String | The type of unit within a house or building. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#unitDesignator target=\"_blank\">unitDesignator</a>
  'unitNumber': "unitNumber_example", // String | The number of the unit, suite, or apartment within a house or building.
  'unitNumberSuffix': "unitNumberSuffix_example", // String | A letter that follows the unit number as in Unit 1A or Suite 302B.
  'civicNumber': "civicNumber_example", // String | The official number assigned to a site by an address authority. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#civicNumber target=\"_blank\">civicNumber</a>
  'civicNumberSuffix': "civicNumberSuffix_example", // String | A letter or fraction that follows the civic number (e.g., the A in 1039A Bledsoe St). See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#civicNumberSuffix target=\"_blank\">civicNumberSuffix</a>
  'streetName': "streetName_example", // String | The official name of the street as assigned by an address authority (e.g., the Douglas in 1175 Douglas Street). See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#streetName target=\"_blank\">streetName</a>
  'streetType': "streetType_example", // String | The type of street as assigned by a municipality (e.g., the ST in 1175 DOUGLAS St). See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#streetType target=\"_blank\">streetType</a>
  'streetDirection': "streetDirection_example", // String | The abbreviated compass direction as defined by Canada Post and B.C. civic addressing authorities. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#streetDirection target=\"_blank\">streetDirection</a>
  'streetQualifier': "streetQualifier_example", // String | Example: the Bridge in Johnson St Bridge. The qualifier of a street name. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#streetQualifier target=\"_blank\">streetQualifier</a>
  'localityName': "localityName_example", // String | The name of the locality assigned to a given site by an address authority. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#localityName target=\"_blank\">localityName</a>
  'provinceCode': "'BC'", // String | The ISO 3166-2 Sub-Country Code. The code for British Columbia is BC.
  'localities': "localities_example", // String | A comma separated list of locality names that matched addresses must belong to. For example, setting localities to Nanaimo only returns addresses in Nanaimo
  'notLocalities': "notLocalities_example", // String | A comma-separated list of localities to exclude from the search.
  'bbox': "bbox_example", // String | Example: -126.07929,49.7628,-126.0163,49.7907.  A bounding box (xmin,ymin,xmax,ymax) that limits the search area. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#bbox target=\"_blank\">bbox</a>
  'centre': "centre_example", // String | Example: -124.0165926,49.2296251 .  The coordinates of a centre point (x,y) used to define a bounding circle that will limit the search area. This parameter must be specified together with 'maxDistance'. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#centre target='_blank'>centre</a>
  'maxDistance': 3.4, // Number | The maximum distance (in metres) to search from the given point.  If not specified, the search distance is unlimited.
  'extrapolate': true, // Boolean | If true, uses supplied parcelPoint to derive an appropriate accessPoint.           See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#extrapolate target=\"_blank\">extrapolate</a>
  'parcelPoint': "parcelPoint_example" // String | The coordinates of a point (x,y) known to be inside the parcel containing a given address. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#parcelPoint target=\"_blank\">parcelPoint</a>
};
apiInstance.addressesOutputFormatGet_0(outputFormat, opts, (error, data, response) => {
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
 **outputFormat** | **String**| Results format. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputFormat target&#x3D;\&quot;_blank\&quot;&gt;outputFormat&lt;/a&gt;.   Note: GeoJSON and KML formats only support EPSG:4326 (outputSRS&#x3D;4326) | [default to &#39;json&#39;]
 **addressString** | **String**| Civic or intersection address as a single string. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#addressString target&#x3D;\&quot;_blank\&quot;&gt;addressString&lt;/a&gt; | [optional] 
 **locationDescriptor** | **String**| Describes the nature of the address location. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#locationDescriptor target&#x3D;\&quot;_blank\&quot;&gt;locationDescriptor&lt;/a&gt; | [optional] [default to &#39;any&#39;]
 **maxResults** | **Number**| The maximum number of search results to return. | [optional] [default to 1]
 **interpolation** | **String**| accessPoint interpolation method. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#interpolation target&#x3D;\&quot;_blank\&quot;&gt;interpolation&lt;/a&gt; | [optional] [default to &#39;adaptive&#39;]
 **echo** | **Boolean**| If true, include unmatched address details such as site name in results. | [optional] [default to true]
 **brief** | **Boolean**| If true, include only basic match and address details in results. Not supported for shp, csv, and gml formats. | [optional] [default to false]
 **autoComplete** | **Boolean**| If true, addressString is expected to contain a partial address that requires completion. Not supported for shp, csv, gml formats. | [optional] [default to false]
 **setBack** | **Number**| The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint. | [optional] [default to 0]
 **outputSRS** | **Number**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326]
 **minScore** | **Number**| The minimum score required for a match to be returned. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#minScore target&#x3D;\&quot;_blank\&quot;&gt;minScore&lt;/a&gt; | [optional] [default to 1]
 **matchPrecision** | **String**| Example: street,locality.  A comma separated list of individual match precision levels to include in results. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#matchPrecision target&#x3D;\&quot;_blank\&quot;&gt;matchPrecision&lt;/a&gt; | [optional] 
 **matchPrecisionNot** | **String**| Example: street,locality.  A comma separated list of individual match precision levels to exclude from results. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#matchPrecisionNot target&#x3D;\&quot;_blank\&quot;&gt;matchPrecisionNot&lt;/a&gt; | [optional] 
 **siteName** | **String**| A string containing the name of the building, facility, or institution (e.g., Duck Building, Casa Del Mar, Crystal Garden, Bluebird House).See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#siteName target&#x3D;\&quot;_blank\&quot;&gt;siteName&lt;/a&gt; | [optional] 
 **unitDesignator** | **String**| The type of unit within a house or building. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#unitDesignator target&#x3D;\&quot;_blank\&quot;&gt;unitDesignator&lt;/a&gt; | [optional] 
 **unitNumber** | **String**| The number of the unit, suite, or apartment within a house or building. | [optional] 
 **unitNumberSuffix** | **String**| A letter that follows the unit number as in Unit 1A or Suite 302B. | [optional] 
 **civicNumber** | **String**| The official number assigned to a site by an address authority. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#civicNumber target&#x3D;\&quot;_blank\&quot;&gt;civicNumber&lt;/a&gt; | [optional] 
 **civicNumberSuffix** | **String**| A letter or fraction that follows the civic number (e.g., the A in 1039A Bledsoe St). See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#civicNumberSuffix target&#x3D;\&quot;_blank\&quot;&gt;civicNumberSuffix&lt;/a&gt; | [optional] 
 **streetName** | **String**| The official name of the street as assigned by an address authority (e.g., the Douglas in 1175 Douglas Street). See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#streetName target&#x3D;\&quot;_blank\&quot;&gt;streetName&lt;/a&gt; | [optional] 
 **streetType** | **String**| The type of street as assigned by a municipality (e.g., the ST in 1175 DOUGLAS St). See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#streetType target&#x3D;\&quot;_blank\&quot;&gt;streetType&lt;/a&gt; | [optional] 
 **streetDirection** | **String**| The abbreviated compass direction as defined by Canada Post and B.C. civic addressing authorities. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#streetDirection target&#x3D;\&quot;_blank\&quot;&gt;streetDirection&lt;/a&gt; | [optional] 
 **streetQualifier** | **String**| Example: the Bridge in Johnson St Bridge. The qualifier of a street name. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#streetQualifier target&#x3D;\&quot;_blank\&quot;&gt;streetQualifier&lt;/a&gt; | [optional] 
 **localityName** | **String**| The name of the locality assigned to a given site by an address authority. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#localityName target&#x3D;\&quot;_blank\&quot;&gt;localityName&lt;/a&gt; | [optional] 
 **provinceCode** | **String**| The ISO 3166-2 Sub-Country Code. The code for British Columbia is BC. | [optional] [default to &#39;BC&#39;]
 **localities** | **String**| A comma separated list of locality names that matched addresses must belong to. For example, setting localities to Nanaimo only returns addresses in Nanaimo | [optional] 
 **notLocalities** | **String**| A comma-separated list of localities to exclude from the search. | [optional] 
 **bbox** | **String**| Example: -126.07929,49.7628,-126.0163,49.7907.  A bounding box (xmin,ymin,xmax,ymax) that limits the search area. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#bbox target&#x3D;\&quot;_blank\&quot;&gt;bbox&lt;/a&gt; | [optional] 
 **centre** | **String**| Example: -124.0165926,49.2296251 .  The coordinates of a centre point (x,y) used to define a bounding circle that will limit the search area. This parameter must be specified together with &#39;maxDistance&#39;. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#centre target&#x3D;&#39;_blank&#39;&gt;centre&lt;/a&gt; | [optional] 
 **maxDistance** | **Number**| The maximum distance (in metres) to search from the given point.  If not specified, the search distance is unlimited. | [optional] 
 **extrapolate** | **Boolean**| If true, uses supplied parcelPoint to derive an appropriate accessPoint.           See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#extrapolate target&#x3D;\&quot;_blank\&quot;&gt;extrapolate&lt;/a&gt; | [optional] 
 **parcelPoint** | **String**| The coordinates of a point (x,y) known to be inside the parcel containing a given address. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#parcelPoint target&#x3D;\&quot;_blank\&quot;&gt;parcelPoint&lt;/a&gt; | [optional] 

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## intersectionsIntersectionIDOutputFormatGet

> intersectionsIntersectionIDOutputFormatGet(intersectionID, outputFormat, opts)

Get an intersection by its unique ID

Represents a individual intersection

### Example

```javascript
import GeocoderRestApi from 'geocoder_rest_api';
let defaultClient = GeocoderRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new GeocoderRestApi.IntersectionsApi();
let intersectionID = "intersectionID_example"; // String | A unique intersection identifier
let outputFormat = "json"; // String | Results format. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputFormat target=\"_blank\">outputFormat</a>.   Note: GeoJSON and KML formats only support EPSG:4326 (outputSRS=4326)
let opts = {
  'outputSRS': 4326 // Number | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
};
apiInstance.intersectionsIntersectionIDOutputFormatGet(intersectionID, outputFormat, opts, (error, data, response) => {
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
 **intersectionID** | **String**| A unique intersection identifier | 
 **outputFormat** | **String**| Results format. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputFormat target&#x3D;\&quot;_blank\&quot;&gt;outputFormat&lt;/a&gt;.   Note: GeoJSON and KML formats only support EPSG:4326 (outputSRS&#x3D;4326) | [default to &#39;json&#39;]
 **outputSRS** | **Number**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326]

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## intersectionsNearOutputFormatGet

> intersectionsNearOutputFormatGet(outputFormat, point, outputSRS, opts)

Find intersections near to a geographic point

Represents intersections near a given point

### Example

```javascript
import GeocoderRestApi from 'geocoder_rest_api';
let defaultClient = GeocoderRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new GeocoderRestApi.IntersectionsApi();
let outputFormat = "json"; // String | Results format. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputFormat target=\"_blank\">outputFormat</a>.   Note: GeoJSON and KML formats only support EPSG:4326 (outputSRS=4326)
let point = "-122.377,50.121"; // String | The point (x,y) from which the nearest site will be identified. The coordinates must be specified in the same SRS as given by the 'outputSRS' parameter.
let outputSRS = 4326; // Number | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
let opts = {
  'maxDistance': 56, // Number | The maximum distance (in metres) to search from the given point.  If not specified, the search distance is unlimited.
  'maxResults': 1, // Number | The maximum number of search results to return.
  'minDegree': 2, // Number | The minimum degree an intersection can have to be included in results. A dead-end has a degree of 1.
  'maxDegree': 100 // Number | The maximum degree an interesection can have to be included in results. A four-way stop has a degree of 4.
};
apiInstance.intersectionsNearOutputFormatGet(outputFormat, point, outputSRS, opts, (error, data, response) => {
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
 **outputFormat** | **String**| Results format. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputFormat target&#x3D;\&quot;_blank\&quot;&gt;outputFormat&lt;/a&gt;.   Note: GeoJSON and KML formats only support EPSG:4326 (outputSRS&#x3D;4326) | [default to &#39;json&#39;]
 **point** | **String**| The point (x,y) from which the nearest site will be identified. The coordinates must be specified in the same SRS as given by the &#39;outputSRS&#39; parameter. | 
 **outputSRS** | **Number**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [default to 4326]
 **maxDistance** | **Number**| The maximum distance (in metres) to search from the given point.  If not specified, the search distance is unlimited. | [optional] 
 **maxResults** | **Number**| The maximum number of search results to return. | [optional] [default to 1]
 **minDegree** | **Number**| The minimum degree an intersection can have to be included in results. A dead-end has a degree of 1. | [optional] [default to 2]
 **maxDegree** | **Number**| The maximum degree an interesection can have to be included in results. A four-way stop has a degree of 4. | [optional] [default to 100]

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## intersectionsNearestOutputFormatGet

> intersectionsNearestOutputFormatGet(outputFormat, point, opts)

Find nearest intersection to a geographic point

Represents the closest intersection to a given point

### Example

```javascript
import GeocoderRestApi from 'geocoder_rest_api';
let defaultClient = GeocoderRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new GeocoderRestApi.IntersectionsApi();
let outputFormat = "json"; // String | Results format. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputFormat target=\"_blank\">outputFormat</a>.   Note: GeoJSON and KML formats only support EPSG:4326 (outputSRS=4326)
let point = "-122.377,50.121"; // String | Example: -122.377,50.121  The point (x,y) from which the nearest site will be identified. The coordinates must be specified in the same SRS as given by the 'outputSRS' parameter.
let opts = {
  'maxDistance': 56, // Number | The maximum distance (in metres) to search from the given point.  If not specified, the search distance is unlimited.
  'outputSRS': 4326, // Number | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
  'minDegree': 2, // Number | The minimum degree an intersection can have to be included in results. A dead-end has a degree of 1.
  'maxDegree': 100 // Number | The maximum degree an interesection can have to be included in results. A four-way stop has a degree of 4.
};
apiInstance.intersectionsNearestOutputFormatGet(outputFormat, point, opts, (error, data, response) => {
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
 **outputFormat** | **String**| Results format. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputFormat target&#x3D;\&quot;_blank\&quot;&gt;outputFormat&lt;/a&gt;.   Note: GeoJSON and KML formats only support EPSG:4326 (outputSRS&#x3D;4326) | [default to &#39;json&#39;]
 **point** | **String**| Example: -122.377,50.121  The point (x,y) from which the nearest site will be identified. The coordinates must be specified in the same SRS as given by the &#39;outputSRS&#39; parameter. | 
 **maxDistance** | **Number**| The maximum distance (in metres) to search from the given point.  If not specified, the search distance is unlimited. | [optional] 
 **outputSRS** | **Number**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326]
 **minDegree** | **Number**| The minimum degree an intersection can have to be included in results. A dead-end has a degree of 1. | [optional] [default to 2]
 **maxDegree** | **Number**| The maximum degree an interesection can have to be included in results. A four-way stop has a degree of 4. | [optional] [default to 100]

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## intersectionsWithinOutputFormatGet

> intersectionsWithinOutputFormatGet(outputFormat, bbox, opts)

Find intersections in a geographic area

Represents all intersections within a given area

### Example

```javascript
import GeocoderRestApi from 'geocoder_rest_api';
let defaultClient = GeocoderRestApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new GeocoderRestApi.IntersectionsApi();
let outputFormat = "json"; // String | Results format. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputFormat target=\"_blank\">outputFormat</a>.   Note: GeoJSON and KML formats only support EPSG:4326 (outputSRS=4326)
let bbox = "-119.51,49.48,-119.53,49.50"; // String | A bounding box (xmin,ymin,xmax,ymax) used to limit the search area. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#bbox target=\"_blank\">bbox</a>
let opts = {
  'outputSRS': 4326, // Number | The EPSG code of the spatial reference system (SRS) to use for output geometries. See <a href=https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputSRS target=\"_blank\">outputSRS</a>
  'maxResults': 200, // Number | The maximum number of search results
  'minDegree': 2, // Number | The minimum degree an intersection can have to be included in results. A dead-end has a degree of 1.
  'maxDegree': 100 // Number | The maximum degree an interesection can have to be included in results. A four-way stop has a degree of 4.
};
apiInstance.intersectionsWithinOutputFormatGet(outputFormat, bbox, opts, (error, data, response) => {
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
 **outputFormat** | **String**| Results format. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputFormat target&#x3D;\&quot;_blank\&quot;&gt;outputFormat&lt;/a&gt;.   Note: GeoJSON and KML formats only support EPSG:4326 (outputSRS&#x3D;4326) | [default to &#39;json&#39;]
 **bbox** | **String**| A bounding box (xmin,ymin,xmax,ymax) used to limit the search area. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#bbox target&#x3D;\&quot;_blank\&quot;&gt;bbox&lt;/a&gt; | 
 **outputSRS** | **Number**| The EPSG code of the spatial reference system (SRS) to use for output geometries. See &lt;a href&#x3D;https://github.com/bcgov/ols-geocoder/blob/gh-pages/glossary.md#outputSRS target&#x3D;\&quot;_blank\&quot;&gt;outputSRS&lt;/a&gt; | [optional] [default to 4326]
 **maxResults** | **Number**| The maximum number of search results | [optional] [default to 200]
 **minDegree** | **Number**| The minimum degree an intersection can have to be included in results. A dead-end has a degree of 1. | [optional] [default to 2]
 **maxDegree** | **Number**| The maximum degree an interesection can have to be included in results. A four-way stop has a degree of 4. | [optional] [default to 100]

### Return type

null (empty response body)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

