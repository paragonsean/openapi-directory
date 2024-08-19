# BcGeographicalNamesWebServiceRestApi.SearchApi

All URIs are relative to *https://apps.gov.bc.ca/pub/bcgnws*

Method | HTTP request | Description
------------- | ------------- | -------------
[**namesChangesGet**](SearchApi.md#namesChangesGet) | **GET** /names/changes | Search for names with metadata changes in a given period
[**namesDecisionsRecentGet**](SearchApi.md#namesDecisionsRecentGet) | **GET** /names/decisions/recent | Search for names affected by recent naming decision
[**namesDecisionsYearGet**](SearchApi.md#namesDecisionsYearGet) | **GET** /names/decisions/year | Search for names affected by naming decisions in a given year
[**namesInsideGet**](SearchApi.md#namesInsideGet) | **GET** /names/inside | Search in a geographic area
[**namesNearGet**](SearchApi.md#namesNearGet) | **GET** /names/near | Search near to a geographic point
[**namesNotOfficialSearchGet**](SearchApi.md#namesNotOfficialSearchGet) | **GET** /names/notOfficial/search | Search by name, limit to unofficial names only
[**namesOfficialSearchGet**](SearchApi.md#namesOfficialSearchGet) | **GET** /names/official/search | Search by name, limit to official names only
[**namesSearchGet**](SearchApi.md#namesSearchGet) | **GET** /names/search | Search by name



## namesChangesGet

> namesChangesGet(outputFormat, fromDate, toDate, opts)

Search for names with metadata changes in a given period

Search for information about geographical names which have changed most recently within a specified time window.  Changes may include status cupdates and metadata corrections.

### Example

```javascript
import BcGeographicalNamesWebServiceRestApi from 'bc_geographical_names_web_service_rest_api';

let apiInstance = new BcGeographicalNamesWebServiceRestApi.SearchApi();
let outputFormat = "json"; // String | The format of the output.
let fromDate = 2017-01-01; // Number | Defines the earliest date (YYYY-MM-DD format) of the change time window for the search
let toDate = 2017-06-30; // Number | Defines the latest date (YYYY-MM-DD format) of the change time window for the search
let opts = {
  'featureClass': "'*'", // String | A filter to limit the search to names associated with features of a certain 'class'  The value of this parameter should be a 'featureClassCode' value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included.
  'featureCategory': "'*'", // String | A filter to limit the search to names associated with features of a certain 'category'  The value of this parameter should be a 'featureCategoryCode' value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included.
  'featureType': "'*'", // String | A filter to limit the search to names associated with features of a certain 'type'  The value of this parameter should be a 'featureTypeCode' value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included
  'sortBy': "'name'", // String | The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint.
  'outputSRS': 4326, // Number | The EPSG code of the spatial reference system (SRS) to use for output geometries.
  'embed': 56, // Number | A flag to indicate whether to embed the corresponding 'feature' into each matching name
  'outputStyle': "'summary'", // String | A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail)
  'itemsPerPage': 20, // Number | The number of search results to return (1-200)
  'startIndex': 1 // Number | The index of the first record to be returned (>= 1)
};
apiInstance.namesChangesGet(outputFormat, fromDate, toDate, opts, (error, data, response) => {
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
 **outputFormat** | **String**| The format of the output. | [default to &#39;json&#39;]
 **fromDate** | **Number**| Defines the earliest date (YYYY-MM-DD format) of the change time window for the search | 
 **toDate** | **Number**| Defines the latest date (YYYY-MM-DD format) of the change time window for the search | 
 **featureClass** | **String**| A filter to limit the search to names associated with features of a certain &#39;class&#39;  The value of this parameter should be a &#39;featureClassCode&#39; value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included. | [optional] [default to &#39;*&#39;]
 **featureCategory** | **String**| A filter to limit the search to names associated with features of a certain &#39;category&#39;  The value of this parameter should be a &#39;featureCategoryCode&#39; value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included. | [optional] [default to &#39;*&#39;]
 **featureType** | **String**| A filter to limit the search to names associated with features of a certain &#39;type&#39;  The value of this parameter should be a &#39;featureTypeCode&#39; value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included | [optional] [default to &#39;*&#39;]
 **sortBy** | **String**| The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint. | [optional] [default to &#39;name&#39;]
 **outputSRS** | **Number**| The EPSG code of the spatial reference system (SRS) to use for output geometries. | [optional] [default to 4326]
 **embed** | **Number**| A flag to indicate whether to embed the corresponding &#39;feature&#39; into each matching name | [optional] 
 **outputStyle** | **String**| A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail) | [optional] [default to &#39;summary&#39;]
 **itemsPerPage** | **Number**| The number of search results to return (1-200) | [optional] [default to 20]
 **startIndex** | **Number**| The index of the first record to be returned (&gt;&#x3D; 1) | [optional] [default to 1]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## namesDecisionsRecentGet

> namesDecisionsRecentGet(outputFormat, days, opts)

Search for names affected by recent naming decision

Search for information about geographical names affected by naming &#39;decisions&#39; made by the BC Geographical Names Office (naming authority) within the last X days.

### Example

```javascript
import BcGeographicalNamesWebServiceRestApi from 'bc_geographical_names_web_service_rest_api';

let apiInstance = new BcGeographicalNamesWebServiceRestApi.SearchApi();
let outputFormat = "json"; // String | The format of the output.
let days = 30; // Number | The number of days used to define the time window of naming decisions to search.  The number is interpreted as searching for 'names affected by decisions within the last X days'.
let opts = {
  'featureClass': "'*'", // String | A filter to limit the search to names associated with features of a certain 'class'  The value of this parameter should be a 'featureClassCode' value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included.
  'featureCategory': "'*'", // String | A filter to limit the search to names associated with features of a certain 'category'  The value of this parameter should be a 'featureCategoryCode' value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included.
  'featureType': "'*'", // String | A filter to limit the search to names associated with features of a certain 'type'  The value of this parameter should be a 'featureTypeCode' value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included
  'sortBy': "'name'", // String | The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint.
  'outputSRS': 4326, // Number | The EPSG code of the spatial reference system (SRS) to use for output geometries.
  'embed': 56, // Number | A flag to indicate whether to embed the corresponding 'feature' into each matching name
  'outputStyle': "'summary'", // String | A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail)
  'itemsPerPage': 20, // Number | The number of search results to return (1-200)
  'startIndex': 1 // Number | The index of the first record to be returned (>= 1)
};
apiInstance.namesDecisionsRecentGet(outputFormat, days, opts, (error, data, response) => {
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
 **outputFormat** | **String**| The format of the output. | [default to &#39;json&#39;]
 **days** | **Number**| The number of days used to define the time window of naming decisions to search.  The number is interpreted as searching for &#39;names affected by decisions within the last X days&#39;. | [default to 30]
 **featureClass** | **String**| A filter to limit the search to names associated with features of a certain &#39;class&#39;  The value of this parameter should be a &#39;featureClassCode&#39; value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included. | [optional] [default to &#39;*&#39;]
 **featureCategory** | **String**| A filter to limit the search to names associated with features of a certain &#39;category&#39;  The value of this parameter should be a &#39;featureCategoryCode&#39; value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included. | [optional] [default to &#39;*&#39;]
 **featureType** | **String**| A filter to limit the search to names associated with features of a certain &#39;type&#39;  The value of this parameter should be a &#39;featureTypeCode&#39; value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included | [optional] [default to &#39;*&#39;]
 **sortBy** | **String**| The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint. | [optional] [default to &#39;name&#39;]
 **outputSRS** | **Number**| The EPSG code of the spatial reference system (SRS) to use for output geometries. | [optional] [default to 4326]
 **embed** | **Number**| A flag to indicate whether to embed the corresponding &#39;feature&#39; into each matching name | [optional] 
 **outputStyle** | **String**| A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail) | [optional] [default to &#39;summary&#39;]
 **itemsPerPage** | **Number**| The number of search results to return (1-200) | [optional] [default to 20]
 **startIndex** | **Number**| The index of the first record to be returned (&gt;&#x3D; 1) | [optional] [default to 1]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## namesDecisionsYearGet

> namesDecisionsYearGet(outputFormat, year, opts)

Search for names affected by naming decisions in a given year

Search for information about geographical names affected by naming &#39;decisions&#39; made by the BC Geographical Names Office (naming authority) in a given year.

### Example

```javascript
import BcGeographicalNamesWebServiceRestApi from 'bc_geographical_names_web_service_rest_api';

let apiInstance = new BcGeographicalNamesWebServiceRestApi.SearchApi();
let outputFormat = "json"; // String | The format of the output.
let year = 2007; // Number | The year in which to search for names affected by naming decisions'.
let opts = {
  'featureClass': "'*'", // String | A filter to limit the search to names associated with features of a certain 'class'  The value of this parameter should be a 'featureClassCode' value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included.
  'featureCategory': "'*'", // String | A filter to limit the search to names associated with features of a certain 'category'  The value of this parameter should be a 'featureCategoryCode' value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included.
  'featureType': "'*'", // String | A filter to limit the search to names associated with features of a certain 'type'  The value of this parameter should be a 'featureTypeCode' value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included
  'sortBy': "'name'", // String | The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint.
  'outputSRS': 4326, // Number | The EPSG code of the spatial reference system (SRS) to use for output geometries.
  'embed': 56, // Number | A flag to indicate whether to embed the corresponding 'feature' into each matching name
  'outputStyle': "'summary'", // String | A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail)
  'itemsPerPage': 20, // Number | The number of search results to return (1-200)
  'startIndex': 1 // Number | The index of the first record to be returned (>= 1)
};
apiInstance.namesDecisionsYearGet(outputFormat, year, opts, (error, data, response) => {
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
 **outputFormat** | **String**| The format of the output. | [default to &#39;json&#39;]
 **year** | **Number**| The year in which to search for names affected by naming decisions&#39;. | 
 **featureClass** | **String**| A filter to limit the search to names associated with features of a certain &#39;class&#39;  The value of this parameter should be a &#39;featureClassCode&#39; value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included. | [optional] [default to &#39;*&#39;]
 **featureCategory** | **String**| A filter to limit the search to names associated with features of a certain &#39;category&#39;  The value of this parameter should be a &#39;featureCategoryCode&#39; value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included. | [optional] [default to &#39;*&#39;]
 **featureType** | **String**| A filter to limit the search to names associated with features of a certain &#39;type&#39;  The value of this parameter should be a &#39;featureTypeCode&#39; value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included | [optional] [default to &#39;*&#39;]
 **sortBy** | **String**| The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint. | [optional] [default to &#39;name&#39;]
 **outputSRS** | **Number**| The EPSG code of the spatial reference system (SRS) to use for output geometries. | [optional] [default to 4326]
 **embed** | **Number**| A flag to indicate whether to embed the corresponding &#39;feature&#39; into each matching name | [optional] 
 **outputStyle** | **String**| A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail) | [optional] [default to &#39;summary&#39;]
 **itemsPerPage** | **Number**| The number of search results to return (1-200) | [optional] [default to 20]
 **startIndex** | **Number**| The index of the first record to be returned (&gt;&#x3D; 1) | [optional] [default to 1]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## namesInsideGet

> namesInsideGet(outputFormat, bbox, opts)

Search in a geographic area

Search for information about geographical names that correspond to features within a geographic bounding box.  Various options and filter parameters are available to refine the search.

### Example

```javascript
import BcGeographicalNamesWebServiceRestApi from 'bc_geographical_names_web_service_rest_api';

let apiInstance = new BcGeographicalNamesWebServiceRestApi.SearchApi();
let outputFormat = "json"; // String | The format of the output.
let bbox = "-119,49,-118,50"; // String | A geographic bounding box defining the search area.  Must be specified as a string of the form 'minLongitude,minLatitude,maxLongitude,maxLatitude' (WGS84). e.g. -119,49,-118,50
let opts = {
  'featureClass': "'*'", // String | A filter to limit the search to names associated with features of a certain 'class'  The value of this parameter should be a 'featureClassCode' value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included.
  'featureCategory': "'*'", // String | A filter to limit the search to names associated with features of a certain 'category'  The value of this parameter should be a 'featureCategoryCode' value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included.
  'featureType': "'*'", // String | A filter to limit the search to names associated with features of a certain 'type'  The value of this parameter should be a 'featureTypeCode' value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included
  'sortBy': "'name'", // String | The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint.
  'outputSRS': 4326, // Number | The EPSG code of the spatial reference system (SRS) to use for output geometries.
  'embed': 56, // Number | A flag to indicate whether to embed the corresponding 'feature' into each matching name
  'outputStyle': "'summary'", // String | A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail)
  'itemsPerPage': 20, // Number | The number of search results to return (1-200)
  'startIndex': 1 // Number | The index of the first record to be returned (>= 1)
};
apiInstance.namesInsideGet(outputFormat, bbox, opts, (error, data, response) => {
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
 **outputFormat** | **String**| The format of the output. | [default to &#39;json&#39;]
 **bbox** | **String**| A geographic bounding box defining the search area.  Must be specified as a string of the form &#39;minLongitude,minLatitude,maxLongitude,maxLatitude&#39; (WGS84). e.g. -119,49,-118,50 | 
 **featureClass** | **String**| A filter to limit the search to names associated with features of a certain &#39;class&#39;  The value of this parameter should be a &#39;featureClassCode&#39; value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included. | [optional] [default to &#39;*&#39;]
 **featureCategory** | **String**| A filter to limit the search to names associated with features of a certain &#39;category&#39;  The value of this parameter should be a &#39;featureCategoryCode&#39; value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included. | [optional] [default to &#39;*&#39;]
 **featureType** | **String**| A filter to limit the search to names associated with features of a certain &#39;type&#39;  The value of this parameter should be a &#39;featureTypeCode&#39; value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included | [optional] [default to &#39;*&#39;]
 **sortBy** | **String**| The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint. | [optional] [default to &#39;name&#39;]
 **outputSRS** | **Number**| The EPSG code of the spatial reference system (SRS) to use for output geometries. | [optional] [default to 4326]
 **embed** | **Number**| A flag to indicate whether to embed the corresponding &#39;feature&#39; into each matching name | [optional] 
 **outputStyle** | **String**| A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail) | [optional] [default to &#39;summary&#39;]
 **itemsPerPage** | **Number**| The number of search results to return (1-200) | [optional] [default to 20]
 **startIndex** | **Number**| The index of the first record to be returned (&gt;&#x3D; 1) | [optional] [default to 1]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## namesNearGet

> namesNearGet(outputFormat, featurePoint, distance, opts)

Search near to a geographic point

Search for information about geographical names that correspond to features within a geographic area defined by a centre point and a radius.  Various options and filter parameters are available to refine the search.

### Example

```javascript
import BcGeographicalNamesWebServiceRestApi from 'bc_geographical_names_web_service_rest_api';

let apiInstance = new BcGeographicalNamesWebServiceRestApi.SearchApi();
let outputFormat = "-119,49,-118,50"; // String | The format of the output.
let featurePoint = "-120,51"; // String | A geographic coordinate specifying the centre point of the search area.  Must be specified as a string of the form 'longitude,latitude' (WGS84).  e.g. -120,51
let distance = "distance_example"; // String | A radius (in kilometres) around the centre point.
let opts = {
  'featureClass': "'*'", // String | A filter to limit the search to names associated with features of a certain 'class'  The value of this parameter should be a 'featureClassCode' value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included.
  'featureCategory': "'*'", // String | A filter to limit the search to names associated with features of a certain 'category'  The value of this parameter should be a 'featureCategoryCode' value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included.
  'featureType': "'*'", // String | A filter to limit the search to names associated with features of a certain 'type'  The value of this parameter should be a 'featureTypeCode' value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included
  'sortBy': "'name'", // String | The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint.
  'outputSRS': 4326, // Number | The EPSG code of the spatial reference system (SRS) to use for output geometries.
  'embed': 56, // Number | A flag to indicate whether to embed the corresponding 'feature' into each matching name
  'outputStyle': "'summary'", // String | A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail)
  'itemsPerPage': 20, // Number | The number of search results to return (1-200)
  'startIndex': 1 // Number | The index of the first record to be returned (>= 1)
};
apiInstance.namesNearGet(outputFormat, featurePoint, distance, opts, (error, data, response) => {
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
 **outputFormat** | **String**| The format of the output. | [default to &#39;json&#39;]
 **featurePoint** | **String**| A geographic coordinate specifying the centre point of the search area.  Must be specified as a string of the form &#39;longitude,latitude&#39; (WGS84).  e.g. -120,51 | 
 **distance** | **String**| A radius (in kilometres) around the centre point. | 
 **featureClass** | **String**| A filter to limit the search to names associated with features of a certain &#39;class&#39;  The value of this parameter should be a &#39;featureClassCode&#39; value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included. | [optional] [default to &#39;*&#39;]
 **featureCategory** | **String**| A filter to limit the search to names associated with features of a certain &#39;category&#39;  The value of this parameter should be a &#39;featureCategoryCode&#39; value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included. | [optional] [default to &#39;*&#39;]
 **featureType** | **String**| A filter to limit the search to names associated with features of a certain &#39;type&#39;  The value of this parameter should be a &#39;featureTypeCode&#39; value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included | [optional] [default to &#39;*&#39;]
 **sortBy** | **String**| The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint. | [optional] [default to &#39;name&#39;]
 **outputSRS** | **Number**| The EPSG code of the spatial reference system (SRS) to use for output geometries. | [optional] [default to 4326]
 **embed** | **Number**| A flag to indicate whether to embed the corresponding &#39;feature&#39; into each matching name | [optional] 
 **outputStyle** | **String**| A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail) | [optional] [default to &#39;summary&#39;]
 **itemsPerPage** | **Number**| The number of search results to return (1-200) | [optional] [default to 20]
 **startIndex** | **Number**| The index of the first record to be returned (&gt;&#x3D; 1) | [optional] [default to 1]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## namesNotOfficialSearchGet

> namesNotOfficialSearchGet(outputFormat, name, opts)

Search by name, limit to unofficial names only

Search for information about unofficial geographical names by the text of the name itself.  Various options and filter parameters are available to refine the search.

### Example

```javascript
import BcGeographicalNamesWebServiceRestApi from 'bc_geographical_names_web_service_rest_api';

let apiInstance = new BcGeographicalNamesWebServiceRestApi.SearchApi();
let outputFormat = "json"; // String | The format of the output.
let name = "Victoria"; // String | A filter to search based on the the text of the name itself.  Use the asterisk (*) as a wildcard character.  For example 'vancouv*'
let opts = {
  'exactSpelling': 0, // Number | If the 'name' parameter is specified, 'exactSpelling' specifies whether to include only names that exactly match the search text (exactSpelling=1), or whether to also include names with similar spellings (exactSpelling=0)
  'featureClass': "'*'", // String | A filter to limit the search to names associated with features of a certain 'class'  The value of this parameter should be a 'featureClassCode' value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included.
  'featureCategory': "'*'", // String | A filter to limit the search to names associated with features of a certain 'category'  The value of this parameter should be a 'featureCategoryCode' value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included.
  'featureType': "'*'", // String | A filter to limit the search to names associated with features of a certain 'type'  The value of this parameter should be a 'featureTypeCode' value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included
  'sortBy': "'relevance'", // String | The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint.
  'outputSRS': 4326, // Number | The EPSG code of the spatial reference system (SRS) to use for output geometries.
  'embed': 56, // Number | A flag to indicate whether to embed the corresponding 'feature' into each matching name
  'outputStyle': "'summary'", // String | A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail)
  'itemsPerPage': 20, // Number | The number of search results to return (1-200)
  'startIndex': 1 // Number | The index of the first record to be returned (>= 1)
};
apiInstance.namesNotOfficialSearchGet(outputFormat, name, opts, (error, data, response) => {
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
 **outputFormat** | **String**| The format of the output. | [default to &#39;json&#39;]
 **name** | **String**| A filter to search based on the the text of the name itself.  Use the asterisk (*) as a wildcard character.  For example &#39;vancouv*&#39; | 
 **exactSpelling** | **Number**| If the &#39;name&#39; parameter is specified, &#39;exactSpelling&#39; specifies whether to include only names that exactly match the search text (exactSpelling&#x3D;1), or whether to also include names with similar spellings (exactSpelling&#x3D;0) | [optional] [default to 0]
 **featureClass** | **String**| A filter to limit the search to names associated with features of a certain &#39;class&#39;  The value of this parameter should be a &#39;featureClassCode&#39; value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included. | [optional] [default to &#39;*&#39;]
 **featureCategory** | **String**| A filter to limit the search to names associated with features of a certain &#39;category&#39;  The value of this parameter should be a &#39;featureCategoryCode&#39; value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included. | [optional] [default to &#39;*&#39;]
 **featureType** | **String**| A filter to limit the search to names associated with features of a certain &#39;type&#39;  The value of this parameter should be a &#39;featureTypeCode&#39; value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included | [optional] [default to &#39;*&#39;]
 **sortBy** | **String**| The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint. | [optional] [default to &#39;relevance&#39;]
 **outputSRS** | **Number**| The EPSG code of the spatial reference system (SRS) to use for output geometries. | [optional] [default to 4326]
 **embed** | **Number**| A flag to indicate whether to embed the corresponding &#39;feature&#39; into each matching name | [optional] 
 **outputStyle** | **String**| A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail) | [optional] [default to &#39;summary&#39;]
 **itemsPerPage** | **Number**| The number of search results to return (1-200) | [optional] [default to 20]
 **startIndex** | **Number**| The index of the first record to be returned (&gt;&#x3D; 1) | [optional] [default to 1]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## namesOfficialSearchGet

> namesOfficialSearchGet(outputFormat, name, opts)

Search by name, limit to official names only

Search for information about official geographical names by the text of the name itself.  Various options and filter parameters are available to refine the search.

### Example

```javascript
import BcGeographicalNamesWebServiceRestApi from 'bc_geographical_names_web_service_rest_api';

let apiInstance = new BcGeographicalNamesWebServiceRestApi.SearchApi();
let outputFormat = "json"; // String | The format of the output.
let name = "Victoria"; // String | A filter to search based on the the text of the name itself.  Use the asterisk (*) as a wildcard character.  For example 'vancouv*'
let opts = {
  'exactSpelling': 0, // Number | If the 'name' parameter is specified, 'exactSpelling' specifies whether to include only names that exactly match the search text (exactSpelling=1), or whether to also include names with similar spellings (exactSpelling=0)
  'featureClass': "'*'", // String | A filter to limit the search to names associated with features of a certain 'class'  The value of this parameter should be a 'featureClassCode' value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included.
  'featureCategory': "'*'", // String | A filter to limit the search to names associated with features of a certain 'category'  The value of this parameter should be a 'featureCategoryCode' value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included.
  'featureType': "'*'", // String | A filter to limit the search to names associated with features of a certain 'type'  The value of this parameter should be a 'featureTypeCode' value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included
  'sortBy': "'relevance'", // String | The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint.
  'outputSRS': 4326, // Number | The EPSG code of the spatial reference system (SRS) to use for output geometries.
  'embed': 56, // Number | A flag to indicate whether to embed the corresponding 'feature' into each matching name
  'outputStyle': "'summary'", // String | A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail)
  'itemsPerPage': 20, // Number | The number of search results to return (1-200)
  'startIndex': 1 // Number | The index of the first record to be returned (>= 1)
};
apiInstance.namesOfficialSearchGet(outputFormat, name, opts, (error, data, response) => {
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
 **outputFormat** | **String**| The format of the output. | [default to &#39;json&#39;]
 **name** | **String**| A filter to search based on the the text of the name itself.  Use the asterisk (*) as a wildcard character.  For example &#39;vancouv*&#39; | 
 **exactSpelling** | **Number**| If the &#39;name&#39; parameter is specified, &#39;exactSpelling&#39; specifies whether to include only names that exactly match the search text (exactSpelling&#x3D;1), or whether to also include names with similar spellings (exactSpelling&#x3D;0) | [optional] [default to 0]
 **featureClass** | **String**| A filter to limit the search to names associated with features of a certain &#39;class&#39;  The value of this parameter should be a &#39;featureClassCode&#39; value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included. | [optional] [default to &#39;*&#39;]
 **featureCategory** | **String**| A filter to limit the search to names associated with features of a certain &#39;category&#39;  The value of this parameter should be a &#39;featureCategoryCode&#39; value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included. | [optional] [default to &#39;*&#39;]
 **featureType** | **String**| A filter to limit the search to names associated with features of a certain &#39;type&#39;  The value of this parameter should be a &#39;featureTypeCode&#39; value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included | [optional] [default to &#39;*&#39;]
 **sortBy** | **String**| The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint. | [optional] [default to &#39;relevance&#39;]
 **outputSRS** | **Number**| The EPSG code of the spatial reference system (SRS) to use for output geometries. | [optional] [default to 4326]
 **embed** | **Number**| A flag to indicate whether to embed the corresponding &#39;feature&#39; into each matching name | [optional] 
 **outputStyle** | **String**| A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail) | [optional] [default to &#39;summary&#39;]
 **itemsPerPage** | **Number**| The number of search results to return (1-200) | [optional] [default to 20]
 **startIndex** | **Number**| The index of the first record to be returned (&gt;&#x3D; 1) | [optional] [default to 1]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## namesSearchGet

> namesSearchGet(outputFormat, name, opts)

Search by name

Search for information about geographical names by the text of the name itself.  The response will include both official and unofficial names.  Various options and filter parameters are available to refine the search.

### Example

```javascript
import BcGeographicalNamesWebServiceRestApi from 'bc_geographical_names_web_service_rest_api';

let apiInstance = new BcGeographicalNamesWebServiceRestApi.SearchApi();
let outputFormat = "json"; // String | The format of the output.
let name = "Victoria"; // String | A filter to search based on the the text of the name itself.  Use the asterisk (*) as a wildcard character.  For example 'vancouv*'
let opts = {
  'exactSpelling': 0, // Number | If the 'name' parameter is specified, 'exactSpelling' specifies whether to include only names that exactly match the search text (exactSpelling=1), or whether to also include names with similar spellings (exactSpelling=0)
  'featureClass': "'*'", // String | A filter to limit the search to names associated with features of a certain 'class'  The value of this parameter should be a 'featureClassCode' value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included.
  'featureCategory': "'*'", // String | A filter to limit the search to names associated with features of a certain 'category'  The value of this parameter should be a 'featureCategoryCode' value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included.
  'featureType': "'*'", // String | A filter to limit the search to names associated with features of a certain 'type'  The value of this parameter should be a 'featureTypeCode' value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included
  'sortBy': "'relevance'", // String | The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint.
  'outputSRS': 4326, // Number | The EPSG code of the spatial reference system (SRS) to use for output geometries.
  'embed': 56, // Number | A flag to indicate whether to embed the corresponding 'feature' into each matching name
  'outputStyle': "'summary'", // String | A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail)
  'itemsPerPage': 20, // Number | The number of search results to return (1-200)
  'startIndex': 1 // Number | The index of the first record to be returned (>= 1)
};
apiInstance.namesSearchGet(outputFormat, name, opts, (error, data, response) => {
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
 **outputFormat** | **String**| The format of the output. | [default to &#39;json&#39;]
 **name** | **String**| A filter to search based on the the text of the name itself.  Use the asterisk (*) as a wildcard character.  For example &#39;vancouv*&#39; | 
 **exactSpelling** | **Number**| If the &#39;name&#39; parameter is specified, &#39;exactSpelling&#39; specifies whether to include only names that exactly match the search text (exactSpelling&#x3D;1), or whether to also include names with similar spellings (exactSpelling&#x3D;0) | [optional] [default to 0]
 **featureClass** | **String**| A filter to limit the search to names associated with features of a certain &#39;class&#39;  The value of this parameter should be a &#39;featureClassCode&#39; value returned by the /featureClasses resource, or an asterisk (*) to request that all feature classes be included. | [optional] [default to &#39;*&#39;]
 **featureCategory** | **String**| A filter to limit the search to names associated with features of a certain &#39;category&#39;  The value of this parameter should be a &#39;featureCategoryCode&#39; value returned by the /featureCategories resource, or an asterisk (*) to request that all feature categories be included. | [optional] [default to &#39;*&#39;]
 **featureType** | **String**| A filter to limit the search to names associated with features of a certain &#39;type&#39;  The value of this parameter should be a &#39;featureTypeCode&#39; value returned by the /featureTypes resource, or an asterisk (*) to request that all feature types be included | [optional] [default to &#39;*&#39;]
 **sortBy** | **String**| The distance to move the accessPoint away from the curb and towards the inside of the parcel (in metres). Ignored if locationDescriptor not set to accessPoint. | [optional] [default to &#39;relevance&#39;]
 **outputSRS** | **Number**| The EPSG code of the spatial reference system (SRS) to use for output geometries. | [optional] [default to 4326]
 **embed** | **Number**| A flag to indicate whether to embed the corresponding &#39;feature&#39; into each matching name | [optional] 
 **outputStyle** | **String**| A flag indicating whether to include with each matching name a succinct list of attributes (summary), or a comprehensive list of attributes (detail) | [optional] [default to &#39;summary&#39;]
 **itemsPerPage** | **Number**| The number of search results to return (1-200) | [optional] [default to 20]
 **startIndex** | **Number**| The index of the first record to be returned (&gt;&#x3D; 1) | [optional] [default to 1]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

