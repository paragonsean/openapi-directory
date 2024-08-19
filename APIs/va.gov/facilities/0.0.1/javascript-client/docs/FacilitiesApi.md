# VaFacilities.FacilitiesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAllFacilities**](FacilitiesApi.md#getAllFacilities) | **GET** /facilities/all | Bulk download information for all facilities
[**getFacilitiesByLocation**](FacilitiesApi.md#getFacilitiesByLocation) | **GET** /facilities | Query facilities by location or IDs, with optional filters
[**getFacilityById**](FacilitiesApi.md#getFacilityById) | **GET** /facilities/{id} | Retrieve a specific facility by ID
[**getFacilityIds**](FacilitiesApi.md#getFacilityIds) | **GET** /ids | Bulk download of all facility IDs
[**getNearbyFacilities**](FacilitiesApi.md#getNearbyFacilities) | **GET** /nearby | Retrieve all VA health facilities reachable by driving within the specified time period



## getAllFacilities

> GeoFacilitiesResponse getAllFacilities(accept)

Bulk download information for all facilities

Retrieve all available facilities in a single operation, formatted as either a GeoJSON FeatureCollection or as a CSV. Due to the complexity of the facility resource type, the CSV response contains a subset of available facility data - specifically it omits the available services, patient satisfaction, and patient wait time data.

### Example

```javascript
import VaFacilities from 'va_facilities';

let apiInstance = new VaFacilities.FacilitiesApi();
let accept = "application/geo+json"; // String | 
apiInstance.getAllFacilities(accept, (error, data, response) => {
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
 **accept** | **String**|  | 

### Return type

[**GeoFacilitiesResponse**](GeoFacilitiesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/geo+json, application/json, application/vnd.geo+json, text/csv


## getFacilitiesByLocation

> GeoFacilitiesResponse getFacilitiesByLocation(opts)

Query facilities by location or IDs, with optional filters

Query facilities by bounding box, latitude and longitude, state, visn, or zip code. Bounding box is specified as four &#x60;bbox[]&#x60; parameters, long1, lat1, long2, lat2. (Relative order is unimportant.)  A query by latitude and longitude returns all facilities in the system, sorted by distance from that location. Providing an optional radius in miles to this query will narrow the scope of the returned facilities to those falling within the specified radius from that location.  All location queries support filtering by facility type, available services, and mobile status.  One can also retrieve facilities by ID using a comma-separated list like &#x60;?ids&#x3D;id1,id2&#x60;. When requesting multiple facilities by ID, the API will return as many results as it can find matches for, omitting IDs where there is no match. It will not return an HTTP error code if it is unable to match a requested ID. Clients may supply IDs up to the limit their HTTP client enforces for URI path lengths. (Usually 2048 characters.)  Results are paginated. JSON responses include pagination information in the standard JSON API \&quot;links\&quot; and \&quot;meta\&quot; elements.   ### Parameter combinations You may optionally specify &#x60;page&#x60; and &#x60;per_page&#x60; with any query. You must specify one of the following parameter combinations:   - &#x60;bbox[]&#x60;, with the option of any combination of &#x60;type&#x60;, &#x60;services[]&#x60;, or &#x60;mobile&#x60;  - &#x60;ids&#x60;  - &#x60;lat&#x60; and &#x60;long&#x60;, with the option of any combination of &#x60;radius&#x60;, &#x60;ids&#x60;, &#x60;type&#x60;, &#x60;services[]&#x60;, or &#x60;mobile&#x60;  - &#x60;state&#x60;, with the option of any combination of &#x60;type&#x60;, &#x60;services[]&#x60;, or &#x60;mobile&#x60;  - &#x60;visn&#x60;  - &#x60;zip&#x60;, with the option of any combination of &#x60;type&#x60;, &#x60;services[]&#x60;, or &#x60;mobile&#x60;   Invalid combinations will return &#x60;400 Bad Request&#x60;. 

### Example

```javascript
import VaFacilities from 'va_facilities';

let apiInstance = new VaFacilities.FacilitiesApi();
let opts = {
  'ids': ["null"], // [String] | List of comma-separated facility IDs to retrieve in a single request. Can be combined with lat and long parameters to retrieve facilities sorted by distance from a location.
  'zip': "80301-1000", // String | Zip code to search for facilities. More detailed zip codes can be passed in, but only the first five digits are used to determine facilities to return.
  'state': "CO", // String | State in which to search for facilities. Except in rare cases, this is two characters.
  'lat': 56.7, // Number | Latitude of point to search for facilities, in WGS84 coordinate reference system.
  '_long': -123.4, // Number | Longitude of point to search for facilities, in WGS84 coordinate reference system.
  'radius': 75, // Number | Optional radial distance from specified latitude and longitude to filter facilities search in WGS84 coordinate reference system.
  'bbox': [null], // [Number] | Bounding box (longitude, latitude, longitude, latitude) within which facilities will be returned. (WGS84 coordinate reference system)
  'visn': 3.4, // Number | VISN search of matching facilities.
  'type': "type_example", // String | Optional facility type search filter
  'services': ["null"], // [String] | Optional facility service search filter
  'mobile': true, // Boolean | Optional facility mobile search filter
  'page': 1, // Number | Page of results to return per paginated response.
  'perPage': 10 // Number | Number of results to return per paginated response.
};
apiInstance.getFacilitiesByLocation(opts, (error, data, response) => {
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
 **ids** | [**[String]**](String.md)| List of comma-separated facility IDs to retrieve in a single request. Can be combined with lat and long parameters to retrieve facilities sorted by distance from a location. | [optional] 
 **zip** | **String**| Zip code to search for facilities. More detailed zip codes can be passed in, but only the first five digits are used to determine facilities to return. | [optional] 
 **state** | **String**| State in which to search for facilities. Except in rare cases, this is two characters. | [optional] 
 **lat** | **Number**| Latitude of point to search for facilities, in WGS84 coordinate reference system. | [optional] 
 **_long** | **Number**| Longitude of point to search for facilities, in WGS84 coordinate reference system. | [optional] 
 **radius** | **Number**| Optional radial distance from specified latitude and longitude to filter facilities search in WGS84 coordinate reference system. | [optional] 
 **bbox** | [**[Number]**](Number.md)| Bounding box (longitude, latitude, longitude, latitude) within which facilities will be returned. (WGS84 coordinate reference system) | [optional] 
 **visn** | **Number**| VISN search of matching facilities. | [optional] 
 **type** | **String**| Optional facility type search filter | [optional] 
 **services** | [**[String]**](String.md)| Optional facility service search filter | [optional] 
 **mobile** | **Boolean**| Optional facility mobile search filter | [optional] 
 **page** | **Number**| Page of results to return per paginated response. | [optional] [default to 1]
 **perPage** | **Number**| Number of results to return per paginated response. | [optional] [default to 10]

### Return type

[**GeoFacilitiesResponse**](GeoFacilitiesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/geo+json, application/json, application/vnd.geo+json


## getFacilityById

> GeoFacilityReadResponse getFacilityById(id)

Retrieve a specific facility by ID

### Example

```javascript
import VaFacilities from 'va_facilities';

let apiInstance = new VaFacilities.FacilitiesApi();
let id = "vha_688"; // String | Facility ID, in the form `<prefix>_<station>`, where prefix is one of \"vha\", \"vba\", \"nca\", or \"vc\", for health facility, benefits, cemetery, or vet center, respectively.
apiInstance.getFacilityById(id, (error, data, response) => {
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
 **id** | **String**| Facility ID, in the form &#x60;&lt;prefix&gt;_&lt;station&gt;&#x60;, where prefix is one of \&quot;vha\&quot;, \&quot;vba\&quot;, \&quot;nca\&quot;, or \&quot;vc\&quot;, for health facility, benefits, cemetery, or vet center, respectively. | 

### Return type

[**GeoFacilityReadResponse**](GeoFacilityReadResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/geo+json, application/json, application/vnd.geo+json


## getFacilityIds

> FacilitiesIdsResponse getFacilityIds(opts)

Bulk download of all facility IDs

Retrieves all available facility IDs only

### Example

```javascript
import VaFacilities from 'va_facilities';

let apiInstance = new VaFacilities.FacilitiesApi();
let opts = {
  'type': "type_example" // String | Optional facility type search filter
};
apiInstance.getFacilityIds(opts, (error, data, response) => {
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
 **type** | **String**| Optional facility type search filter | [optional] 

### Return type

[**FacilitiesIdsResponse**](FacilitiesIdsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNearbyFacilities

> NearbyResponse getNearbyFacilities(opts)

Retrieve all VA health facilities reachable by driving within the specified time period

Retrieve all VA health facilities that are located within a specified drive time from a specified location based on coordinates (lat and lng). Optional filter parameters include drive_time and services[]. Address (street_address, city, state, and zip) no longer returns results.  The \&quot;attributes\&quot; element has information about the drive-time band that contains the requested location for each facility in the response. The values of &#x60;min_time&#x60; and &#x60;max_time&#x60; are in minutes. For example, a facility returned with a matched &#x60;min_time&#x60; of 10 and &#x60;max_time&#x60; of 20 is a 10 to 20 minute drive from the requested location.  To retrieve full details for nearby facilities, see the documentation for &#x60;/facilities?ids&#x60;.

### Example

```javascript
import VaFacilities from 'va_facilities';

let apiInstance = new VaFacilities.FacilitiesApi();
let opts = {
  'lat': 56.7, // Number | Latitude of the location from which drive time will be calculated.
  'lng': -123.4, // Number | Longitude of the location from which drive time will be calculated.
  'streetAddress': "1350 I St. NW", // String | Street address of the location from which drive time will be calculated.
  'city': "Washington", // String | City of the location from which drive time will be calculated.
  'state': "DC", // String | Two character state code of the location from which drive time will be calculated.
  'zip': "20005-3305", // String | Zip code of the location from which drive time will be calculated.
  'driveTime': 90, // Number | Filter to only include facilities that are within the specified number of drive time minutes from the requested location.
  'services': ["null"] // [String] | Optional facility service search filter
};
apiInstance.getNearbyFacilities(opts, (error, data, response) => {
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
 **lat** | **Number**| Latitude of the location from which drive time will be calculated. | [optional] 
 **lng** | **Number**| Longitude of the location from which drive time will be calculated. | [optional] 
 **streetAddress** | **String**| Street address of the location from which drive time will be calculated. | [optional] 
 **city** | **String**| City of the location from which drive time will be calculated. | [optional] 
 **state** | **String**| Two character state code of the location from which drive time will be calculated. | [optional] 
 **zip** | **String**| Zip code of the location from which drive time will be calculated. | [optional] 
 **driveTime** | **Number**| Filter to only include facilities that are within the specified number of drive time minutes from the requested location. | [optional] [default to 90]
 **services** | [**[String]**](String.md)| Optional facility service search filter | [optional] 

### Return type

[**NearbyResponse**](NearbyResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

