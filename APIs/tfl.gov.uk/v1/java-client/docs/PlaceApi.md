# PlaceApi

All URIs are relative to *https://api.digital.tfl.gov.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**placeGet**](PlaceApi.md#placeGet) | **GET** /Place/{id} | Gets the place with the given id. |
| [**placeGetAt**](PlaceApi.md#placeGetAt) | **GET** /Place/{type}/At/{Lat}/{Lon} | Gets any places of the given type whose geography intersects the given latitude and longitude. In practice this means the Place              must be polygonal e.g. a BoroughBoundary. |
| [**placeGetByGeo**](PlaceApi.md#placeGetByGeo) | **GET** /Place | Gets the places that lie within a geographic region. The geographic region of interest can either be specified              by using a lat/lon geo-point and a radius in metres to return places within the locus defined by the lat/lon of              its centre or alternatively, by the use of a bounding box defined by the lat/lon of its north-west and south-east corners.              Optionally filters on type and can strip properties for a smaller payload. |
| [**placeGetByType**](PlaceApi.md#placeGetByType) | **GET** /Place/Type/{types} | Gets all places of a given type |
| [**placeGetOverlay**](PlaceApi.md#placeGetOverlay) | **GET** /Place/{type}/overlay/{z}/{Lat}/{Lon}/{width}/{height} | Gets the place overlay for a given set of co-ordinates and a given width/height. |
| [**placeGetStreetsByPostCode**](PlaceApi.md#placeGetStreetsByPostCode) | **GET** /Place/Address/Streets/{Postcode} | Gets the set of streets associated with a post code. |
| [**placeMetaCategories**](PlaceApi.md#placeMetaCategories) | **GET** /Place/Meta/Categories | Gets a list of all of the available place property categories and keys. |
| [**placeMetaPlaceTypes**](PlaceApi.md#placeMetaPlaceTypes) | **GET** /Place/Meta/PlaceTypes | Gets a list of the available types of Place. |
| [**placeSearch**](PlaceApi.md#placeSearch) | **GET** /Place/Search | Gets all places that matches the given query |


<a id="placeGet"></a>
# **placeGet**
> List&lt;TflApiPresentationEntitiesPlace&gt; placeGet(id, includeChildren)

Gets the place with the given id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    PlaceApi apiInstance = new PlaceApi(defaultClient);
    String id = "id_example"; // String | The id of the place, you can use the /Place/Types/{types} endpoint to get a list of places for a given type including their ids
    Boolean includeChildren = true; // Boolean | Defaults to false. If true child places e.g. individual charging stations at a charge point while be included, otherwise just the URLs of any child places will be returned
    try {
      List<TflApiPresentationEntitiesPlace> result = apiInstance.placeGet(id, includeChildren);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlaceApi#placeGet");
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
| **id** | **String**| The id of the place, you can use the /Place/Types/{types} endpoint to get a list of places for a given type including their ids | |
| **includeChildren** | **Boolean**| Defaults to false. If true child places e.g. individual charging stations at a charge point while be included, otherwise just the URLs of any child places will be returned | [optional] |

### Return type

[**List&lt;TflApiPresentationEntitiesPlace&gt;**](TflApiPresentationEntitiesPlace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="placeGetAt"></a>
# **placeGetAt**
> Object placeGetAt(type, lat, lon, locationLat, locationLon, lat2, lon2)

Gets any places of the given type whose geography intersects the given latitude and longitude. In practice this means the Place              must be polygonal e.g. a BoroughBoundary.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    PlaceApi apiInstance = new PlaceApi(defaultClient);
    List<String> type = Arrays.asList(); // List<String> | The place type (a valid list of place types can be obtained from the /Place/Meta/placeTypes endpoint)
    String lat = "lat_example"; // String | 
    String lon = "lon_example"; // String | 
    Double locationLat = 3.4D; // Double | 
    Double locationLon = 3.4D; // Double | 
    String lat2 = "lat_example"; // String | Automatically added
    String lon2 = "lon_example"; // String | Automatically added
    try {
      Object result = apiInstance.placeGetAt(type, lat, lon, locationLat, locationLon, lat2, lon2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlaceApi#placeGetAt");
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
| **type** | [**List&lt;String&gt;**](String.md)| The place type (a valid list of place types can be obtained from the /Place/Meta/placeTypes endpoint) | |
| **lat** | **String**|  | |
| **lon** | **String**|  | |
| **locationLat** | **Double**|  | |
| **locationLon** | **Double**|  | |
| **lat2** | **String**| Automatically added | |
| **lon2** | **String**| Automatically added | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="placeGetByGeo"></a>
# **placeGetByGeo**
> List&lt;TflApiPresentationEntitiesStopPoint&gt; placeGetByGeo(radius, categories, includeChildren, type, activeOnly, numberOfPlacesToReturn, placeGeoSwLat, placeGeoSwLon, placeGeoNeLat, placeGeoNeLon, placeGeoLat, placeGeoLon)

Gets the places that lie within a geographic region. The geographic region of interest can either be specified              by using a lat/lon geo-point and a radius in metres to return places within the locus defined by the lat/lon of              its centre or alternatively, by the use of a bounding box defined by the lat/lon of its north-west and south-east corners.              Optionally filters on type and can strip properties for a smaller payload.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    PlaceApi apiInstance = new PlaceApi(defaultClient);
    Double radius = 3.4D; // Double | The radius of the bounding circle in metres when only lat/lon are specified.
    List<String> categories = Arrays.asList(); // List<String> | An optional list of comma separated property categories to return in the Place's property bag. If null or empty, all categories of property are returned. Pass the keyword \"none\" to return no properties (a valid list of categories can be obtained from the /Place/Meta/categories endpoint)
    Boolean includeChildren = true; // Boolean | Defaults to false. If true child places e.g. individual charging stations at a charge point while be included, otherwise just the URLs of any child places will be returned
    List<String> type = Arrays.asList(); // List<String> | Place types to filter on, or null to return all types
    Boolean activeOnly = true; // Boolean | An optional parameter to limit the results to active records only (Currently only the 'VariableMessageSign' place type is supported)
    Integer numberOfPlacesToReturn = 56; // Integer | If specified, limits the number of returned places equal to the given value
    Double placeGeoSwLat = 3.4D; // Double | 
    Double placeGeoSwLon = 3.4D; // Double | 
    Double placeGeoNeLat = 3.4D; // Double | 
    Double placeGeoNeLon = 3.4D; // Double | 
    Double placeGeoLat = 3.4D; // Double | 
    Double placeGeoLon = 3.4D; // Double | 
    try {
      List<TflApiPresentationEntitiesStopPoint> result = apiInstance.placeGetByGeo(radius, categories, includeChildren, type, activeOnly, numberOfPlacesToReturn, placeGeoSwLat, placeGeoSwLon, placeGeoNeLat, placeGeoNeLon, placeGeoLat, placeGeoLon);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlaceApi#placeGetByGeo");
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
| **radius** | **Double**| The radius of the bounding circle in metres when only lat/lon are specified. | [optional] |
| **categories** | [**List&lt;String&gt;**](String.md)| An optional list of comma separated property categories to return in the Place&#39;s property bag. If null or empty, all categories of property are returned. Pass the keyword \&quot;none\&quot; to return no properties (a valid list of categories can be obtained from the /Place/Meta/categories endpoint) | [optional] |
| **includeChildren** | **Boolean**| Defaults to false. If true child places e.g. individual charging stations at a charge point while be included, otherwise just the URLs of any child places will be returned | [optional] |
| **type** | [**List&lt;String&gt;**](String.md)| Place types to filter on, or null to return all types | [optional] |
| **activeOnly** | **Boolean**| An optional parameter to limit the results to active records only (Currently only the &#39;VariableMessageSign&#39; place type is supported) | [optional] |
| **numberOfPlacesToReturn** | **Integer**| If specified, limits the number of returned places equal to the given value | [optional] |
| **placeGeoSwLat** | **Double**|  | [optional] |
| **placeGeoSwLon** | **Double**|  | [optional] |
| **placeGeoNeLat** | **Double**|  | [optional] |
| **placeGeoNeLon** | **Double**|  | [optional] |
| **placeGeoLat** | **Double**|  | [optional] |
| **placeGeoLon** | **Double**|  | [optional] |

### Return type

[**List&lt;TflApiPresentationEntitiesStopPoint&gt;**](TflApiPresentationEntitiesStopPoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="placeGetByType"></a>
# **placeGetByType**
> List&lt;TflApiPresentationEntitiesPlace&gt; placeGetByType(types, activeOnly)

Gets all places of a given type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    PlaceApi apiInstance = new PlaceApi(defaultClient);
    List<String> types = Arrays.asList(); // List<String> | A comma-separated list of the types to return. Max. approx 12 types.              A valid list of place types can be obtained from the /Place/Meta/placeTypes endpoint.
    Boolean activeOnly = true; // Boolean | An optional parameter to limit the results to active records only (Currently only the 'VariableMessageSign' place type is supported)
    try {
      List<TflApiPresentationEntitiesPlace> result = apiInstance.placeGetByType(types, activeOnly);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlaceApi#placeGetByType");
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
| **types** | [**List&lt;String&gt;**](String.md)| A comma-separated list of the types to return. Max. approx 12 types.              A valid list of place types can be obtained from the /Place/Meta/placeTypes endpoint. | |
| **activeOnly** | **Boolean**| An optional parameter to limit the results to active records only (Currently only the &#39;VariableMessageSign&#39; place type is supported) | [optional] |

### Return type

[**List&lt;TflApiPresentationEntitiesPlace&gt;**](TflApiPresentationEntitiesPlace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="placeGetOverlay"></a>
# **placeGetOverlay**
> Object placeGetOverlay(z, type, width, height, lat, lon, locationLat, locationLon, lat2, lon2)

Gets the place overlay for a given set of co-ordinates and a given width/height.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    PlaceApi apiInstance = new PlaceApi(defaultClient);
    Integer z = 56; // Integer | The zoom level
    List<String> type = Arrays.asList(); // List<String> | The place type (a valid list of place types can be obtained from the /Place/Meta/placeTypes endpoint)
    Integer width = 56; // Integer | The width of the requested overlay.
    Integer height = 56; // Integer | The height of the requested overlay.
    String lat = "lat_example"; // String | 
    String lon = "lon_example"; // String | 
    Double locationLat = 3.4D; // Double | 
    Double locationLon = 3.4D; // Double | 
    String lat2 = "lat_example"; // String | Automatically added
    String lon2 = "lon_example"; // String | Automatically added
    try {
      Object result = apiInstance.placeGetOverlay(z, type, width, height, lat, lon, locationLat, locationLon, lat2, lon2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlaceApi#placeGetOverlay");
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
| **z** | **Integer**| The zoom level | |
| **type** | [**List&lt;String&gt;**](String.md)| The place type (a valid list of place types can be obtained from the /Place/Meta/placeTypes endpoint) | |
| **width** | **Integer**| The width of the requested overlay. | |
| **height** | **Integer**| The height of the requested overlay. | |
| **lat** | **String**|  | |
| **lon** | **String**|  | |
| **locationLat** | **Double**|  | |
| **locationLon** | **Double**|  | |
| **lat2** | **String**| Automatically added | |
| **lon2** | **String**| Automatically added | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="placeGetStreetsByPostCode"></a>
# **placeGetStreetsByPostCode**
> Object placeGetStreetsByPostCode(postcode, postcode2, postcodeInputPostcode)

Gets the set of streets associated with a post code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    PlaceApi apiInstance = new PlaceApi(defaultClient);
    String postcode = "postcode_example"; // String | 
    String postcode2 = "postcode_example"; // String | Automatically added
    String postcodeInputPostcode = "postcodeInputPostcode_example"; // String | 
    try {
      Object result = apiInstance.placeGetStreetsByPostCode(postcode, postcode2, postcodeInputPostcode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlaceApi#placeGetStreetsByPostCode");
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
| **postcode** | **String**|  | |
| **postcode2** | **String**| Automatically added | |
| **postcodeInputPostcode** | **String**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="placeMetaCategories"></a>
# **placeMetaCategories**
> List&lt;TflApiPresentationEntitiesPlaceCategory&gt; placeMetaCategories()

Gets a list of all of the available place property categories and keys.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    PlaceApi apiInstance = new PlaceApi(defaultClient);
    try {
      List<TflApiPresentationEntitiesPlaceCategory> result = apiInstance.placeMetaCategories();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlaceApi#placeMetaCategories");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;TflApiPresentationEntitiesPlaceCategory&gt;**](TflApiPresentationEntitiesPlaceCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="placeMetaPlaceTypes"></a>
# **placeMetaPlaceTypes**
> List&lt;TflApiPresentationEntitiesPlaceCategory&gt; placeMetaPlaceTypes()

Gets a list of the available types of Place.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    PlaceApi apiInstance = new PlaceApi(defaultClient);
    try {
      List<TflApiPresentationEntitiesPlaceCategory> result = apiInstance.placeMetaPlaceTypes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlaceApi#placeMetaPlaceTypes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;TflApiPresentationEntitiesPlaceCategory&gt;**](TflApiPresentationEntitiesPlaceCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="placeSearch"></a>
# **placeSearch**
> List&lt;TflApiPresentationEntitiesPlace&gt; placeSearch(name, types)

Gets all places that matches the given query

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PlaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    PlaceApi apiInstance = new PlaceApi(defaultClient);
    String name = "name_example"; // String | The name of the place, you can use the /Place/Types/{types} endpoint to get a list of places for a given type including their names.
    List<String> types = Arrays.asList(); // List<String> | A comma-separated list of the types to return. Max. approx 12 types.
    try {
      List<TflApiPresentationEntitiesPlace> result = apiInstance.placeSearch(name, types);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PlaceApi#placeSearch");
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
| **name** | **String**| The name of the place, you can use the /Place/Types/{types} endpoint to get a list of places for a given type including their names. | |
| **types** | [**List&lt;String&gt;**](String.md)| A comma-separated list of the types to return. Max. approx 12 types. | [optional] |

### Return type

[**List&lt;TflApiPresentationEntitiesPlace&gt;**](TflApiPresentationEntitiesPlace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

