# FacilitiesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAllFacilities**](FacilitiesApi.md#getAllFacilities) | **GET** /facilities/all | Bulk download information for all facilities |
| [**getFacilitiesByLocation**](FacilitiesApi.md#getFacilitiesByLocation) | **GET** /facilities | Query facilities by location or IDs, with optional filters |
| [**getFacilityById**](FacilitiesApi.md#getFacilityById) | **GET** /facilities/{id} | Retrieve a specific facility by ID |
| [**getFacilityIds**](FacilitiesApi.md#getFacilityIds) | **GET** /ids | Bulk download of all facility IDs |
| [**getNearbyFacilities**](FacilitiesApi.md#getNearbyFacilities) | **GET** /nearby | Retrieve all VA health facilities reachable by driving within the specified time period |


<a id="getAllFacilities"></a>
# **getAllFacilities**
> GeoFacilitiesResponse getAllFacilities(accept)

Bulk download information for all facilities

Retrieve all available facilities in a single operation, formatted as either a GeoJSON FeatureCollection or as a CSV. Due to the complexity of the facility resource type, the CSV response contains a subset of available facility data - specifically it omits the available services, patient satisfaction, and patient wait time data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    FacilitiesApi apiInstance = new FacilitiesApi(defaultClient);
    String accept = "application/geo+json"; // String | 
    try {
      GeoFacilitiesResponse result = apiInstance.getAllFacilities(accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilitiesApi#getAllFacilities");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **accept** | **String**|  | [enum: application/geo+json, application/vnd.geo+json, text/csv] |

### Return type

[**GeoFacilitiesResponse**](GeoFacilitiesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/json, application/vnd.geo+json, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Missing API token |  -  |
| **403** | Invalid API token |  -  |
| **406** | Requested format unacceptable |  -  |
| **429** | API rate limit exceeded |  -  |

<a id="getFacilitiesByLocation"></a>
# **getFacilitiesByLocation**
> GeoFacilitiesResponse getFacilitiesByLocation(ids, zip, state, lat, _long, radius, bbox, visn, type, services, mobile, page, perPage)

Query facilities by location or IDs, with optional filters

Query facilities by bounding box, latitude and longitude, state, visn, or zip code. Bounding box is specified as four &#x60;bbox[]&#x60; parameters, long1, lat1, long2, lat2. (Relative order is unimportant.)  A query by latitude and longitude returns all facilities in the system, sorted by distance from that location. Providing an optional radius in miles to this query will narrow the scope of the returned facilities to those falling within the specified radius from that location.  All location queries support filtering by facility type, available services, and mobile status.  One can also retrieve facilities by ID using a comma-separated list like &#x60;?ids&#x3D;id1,id2&#x60;. When requesting multiple facilities by ID, the API will return as many results as it can find matches for, omitting IDs where there is no match. It will not return an HTTP error code if it is unable to match a requested ID. Clients may supply IDs up to the limit their HTTP client enforces for URI path lengths. (Usually 2048 characters.)  Results are paginated. JSON responses include pagination information in the standard JSON API \&quot;links\&quot; and \&quot;meta\&quot; elements.   ### Parameter combinations You may optionally specify &#x60;page&#x60; and &#x60;per_page&#x60; with any query. You must specify one of the following parameter combinations:   - &#x60;bbox[]&#x60;, with the option of any combination of &#x60;type&#x60;, &#x60;services[]&#x60;, or &#x60;mobile&#x60;  - &#x60;ids&#x60;  - &#x60;lat&#x60; and &#x60;long&#x60;, with the option of any combination of &#x60;radius&#x60;, &#x60;ids&#x60;, &#x60;type&#x60;, &#x60;services[]&#x60;, or &#x60;mobile&#x60;  - &#x60;state&#x60;, with the option of any combination of &#x60;type&#x60;, &#x60;services[]&#x60;, or &#x60;mobile&#x60;  - &#x60;visn&#x60;  - &#x60;zip&#x60;, with the option of any combination of &#x60;type&#x60;, &#x60;services[]&#x60;, or &#x60;mobile&#x60;   Invalid combinations will return &#x60;400 Bad Request&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    FacilitiesApi apiInstance = new FacilitiesApi(defaultClient);
    List<String> ids = Arrays.asList(); // List<String> | List of comma-separated facility IDs to retrieve in a single request. Can be combined with lat and long parameters to retrieve facilities sorted by distance from a location.
    String zip = "80301-1000"; // String | Zip code to search for facilities. More detailed zip codes can be passed in, but only the first five digits are used to determine facilities to return.
    String state = "CO"; // String | State in which to search for facilities. Except in rare cases, this is two characters.
    Float lat = 56.7F; // Float | Latitude of point to search for facilities, in WGS84 coordinate reference system.
    Float _long = -123.4F; // Float | Longitude of point to search for facilities, in WGS84 coordinate reference system.
    Float radius = 75F; // Float | Optional radial distance from specified latitude and longitude to filter facilities search in WGS84 coordinate reference system.
    List<Float> bbox = Arrays.asList(); // List<Float> | Bounding box (longitude, latitude, longitude, latitude) within which facilities will be returned. (WGS84 coordinate reference system)
    BigDecimal visn = new BigDecimal(78); // BigDecimal | VISN search of matching facilities.
    String type = "health"; // String | Optional facility type search filter
    List<String> services = Arrays.asList(); // List<String> | Optional facility service search filter
    Boolean mobile = true; // Boolean | Optional facility mobile search filter
    Long page = 1L; // Long | Page of results to return per paginated response.
    Long perPage = 10L; // Long | Number of results to return per paginated response.
    try {
      GeoFacilitiesResponse result = apiInstance.getFacilitiesByLocation(ids, zip, state, lat, _long, radius, bbox, visn, type, services, mobile, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilitiesApi#getFacilitiesByLocation");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **ids** | [**List&lt;String&gt;**](String.md)| List of comma-separated facility IDs to retrieve in a single request. Can be combined with lat and long parameters to retrieve facilities sorted by distance from a location. | [optional] |
| **zip** | **String**| Zip code to search for facilities. More detailed zip codes can be passed in, but only the first five digits are used to determine facilities to return. | [optional] |
| **state** | **String**| State in which to search for facilities. Except in rare cases, this is two characters. | [optional] |
| **lat** | **Float**| Latitude of point to search for facilities, in WGS84 coordinate reference system. | [optional] |
| **_long** | **Float**| Longitude of point to search for facilities, in WGS84 coordinate reference system. | [optional] |
| **radius** | **Float**| Optional radial distance from specified latitude and longitude to filter facilities search in WGS84 coordinate reference system. | [optional] |
| **bbox** | [**List&lt;Float&gt;**](Float.md)| Bounding box (longitude, latitude, longitude, latitude) within which facilities will be returned. (WGS84 coordinate reference system) | [optional] |
| **visn** | **BigDecimal**| VISN search of matching facilities. | [optional] |
| **type** | **String**| Optional facility type search filter | [optional] [enum: health, cemetery, benefits, vet_center] |
| **services** | [**List&lt;String&gt;**](String.md)| Optional facility service search filter | [optional] |
| **mobile** | **Boolean**| Optional facility mobile search filter | [optional] |
| **page** | **Long**| Page of results to return per paginated response. | [optional] [default to 1] |
| **perPage** | **Long**| Number of results to return per paginated response. | [optional] [default to 10] |

### Return type

[**GeoFacilitiesResponse**](GeoFacilitiesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/json, application/vnd.geo+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Missing API token |  -  |
| **403** | Invalid API token |  -  |
| **406** | Requested format unacceptable |  -  |
| **429** | API rate limit exceeded |  -  |

<a id="getFacilityById"></a>
# **getFacilityById**
> GeoFacilityReadResponse getFacilityById(id)

Retrieve a specific facility by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    FacilitiesApi apiInstance = new FacilitiesApi(defaultClient);
    String id = "vha_688"; // String | Facility ID, in the form `<prefix>_<station>`, where prefix is one of \"vha\", \"vba\", \"nca\", or \"vc\", for health facility, benefits, cemetery, or vet center, respectively.
    try {
      GeoFacilityReadResponse result = apiInstance.getFacilityById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilitiesApi#getFacilityById");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| Facility ID, in the form &#x60;&lt;prefix&gt;_&lt;station&gt;&#x60;, where prefix is one of \&quot;vha\&quot;, \&quot;vba\&quot;, \&quot;nca\&quot;, or \&quot;vc\&quot;, for health facility, benefits, cemetery, or vet center, respectively. | |

### Return type

[**GeoFacilityReadResponse**](GeoFacilityReadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json, application/json, application/vnd.geo+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad request - invalid or missing query parameters |  -  |
| **401** | Missing API token |  -  |
| **403** | Invalid API token |  -  |
| **404** | Facility not found |  -  |
| **406** | Requested format unacceptable |  -  |
| **429** | API rate limit exceeded |  -  |

<a id="getFacilityIds"></a>
# **getFacilityIds**
> FacilitiesIdsResponse getFacilityIds(type)

Bulk download of all facility IDs

Retrieves all available facility IDs only

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    FacilitiesApi apiInstance = new FacilitiesApi(defaultClient);
    String type = "health"; // String | Optional facility type search filter
    try {
      FacilitiesIdsResponse result = apiInstance.getFacilityIds(type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilitiesApi#getFacilityIds");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **type** | **String**| Optional facility type search filter | [optional] [enum: health, cemetery, benefits, vet_center] |

### Return type

[**FacilitiesIdsResponse**](FacilitiesIdsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Missing API token |  -  |
| **403** | Invalid API token |  -  |
| **406** | Requested format unacceptable |  -  |
| **429** | API rate limit exceeded |  -  |

<a id="getNearbyFacilities"></a>
# **getNearbyFacilities**
> NearbyResponse getNearbyFacilities(lat, lng, streetAddress, city, state, zip, driveTime, services)

Retrieve all VA health facilities reachable by driving within the specified time period

Retrieve all VA health facilities that are located within a specified drive time from a specified location based on coordinates (lat and lng). Optional filter parameters include drive_time and services[]. Address (street_address, city, state, and zip) no longer returns results.  The \&quot;attributes\&quot; element has information about the drive-time band that contains the requested location for each facility in the response. The values of &#x60;min_time&#x60; and &#x60;max_time&#x60; are in minutes. For example, a facility returned with a matched &#x60;min_time&#x60; of 10 and &#x60;max_time&#x60; of 20 is a 10 to 20 minute drive from the requested location.  To retrieve full details for nearby facilities, see the documentation for &#x60;/facilities?ids&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FacilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    FacilitiesApi apiInstance = new FacilitiesApi(defaultClient);
    Float lat = 56.7F; // Float | Latitude of the location from which drive time will be calculated.
    Float lng = -123.4F; // Float | Longitude of the location from which drive time will be calculated.
    String streetAddress = "1350 I St. NW"; // String | Street address of the location from which drive time will be calculated.
    String city = "Washington"; // String | City of the location from which drive time will be calculated.
    String state = "DC"; // String | Two character state code of the location from which drive time will be calculated.
    String zip = "20005-3305"; // String | Zip code of the location from which drive time will be calculated.
    Integer driveTime = 10; // Integer | Filter to only include facilities that are within the specified number of drive time minutes from the requested location.
    List<String> services = Arrays.asList(); // List<String> | Optional facility service search filter
    try {
      NearbyResponse result = apiInstance.getNearbyFacilities(lat, lng, streetAddress, city, state, zip, driveTime, services);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FacilitiesApi#getNearbyFacilities");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **lat** | **Float**| Latitude of the location from which drive time will be calculated. | [optional] |
| **lng** | **Float**| Longitude of the location from which drive time will be calculated. | [optional] |
| **streetAddress** | **String**| Street address of the location from which drive time will be calculated. | [optional] |
| **city** | **String**| City of the location from which drive time will be calculated. | [optional] |
| **state** | **String**| Two character state code of the location from which drive time will be calculated. | [optional] |
| **zip** | **String**| Zip code of the location from which drive time will be calculated. | [optional] |
| **driveTime** | **Integer**| Filter to only include facilities that are within the specified number of drive time minutes from the requested location. | [optional] [default to 90] [enum: 10, 20, 30, 40, 50, 60, 70, 80, 90] |
| **services** | [**List&lt;String&gt;**](String.md)| Optional facility service search filter | [optional] |

### Return type

[**NearbyResponse**](NearbyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Missing Required Or Ambiguous Parameters |  -  |
| **401** | Missing API token |  -  |
| **403** | Invalid API token |  -  |
| **406** | Requested format unacceptable |  -  |
| **429** | API rate limit exceeded |  -  |

