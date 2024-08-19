# StopPointApi

All URIs are relative to *https://api.digital.tfl.gov.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**stopPointArrivalDepartures**](StopPointApi.md#stopPointArrivalDepartures) | **GET** /StopPoint/{id}/ArrivalDepartures | Gets the list of arrival and departure predictions for the given stop point id (overground, Elizabeth line and thameslink only) |
| [**stopPointArrivals**](StopPointApi.md#stopPointArrivals) | **GET** /StopPoint/{id}/Arrivals | Gets the list of arrival predictions for the given stop point id |
| [**stopPointCrowding**](StopPointApi.md#stopPointCrowding) | **GET** /StopPoint/{id}/Crowding/{line} | Gets all the Crowding data (static) for the StopPointId, plus crowding data for a given line and optionally a particular direction. |
| [**stopPointDirection**](StopPointApi.md#stopPointDirection) | **GET** /StopPoint/{id}/DirectionTo/{toStopPointId} | Returns the canonical direction, \&quot;inbound\&quot; or \&quot;outbound\&quot;, for a given pair of stop point Ids in the direction from -&amp;gt; to. |
| [**stopPointDisruption**](StopPointApi.md#stopPointDisruption) | **GET** /StopPoint/{ids}/Disruption | Gets all disruptions for the specified StopPointId, plus disruptions for any child Naptan records it may have. |
| [**stopPointDisruptionByMode**](StopPointApi.md#stopPointDisruptionByMode) | **GET** /StopPoint/Mode/{modes}/Disruption | Gets a distinct list of disrupted stop points for the given modes |
| [**stopPointGet**](StopPointApi.md#stopPointGet) | **GET** /StopPoint/{ids} | Gets a list of StopPoints corresponding to the given list of stop ids. |
| [**stopPointGetByGeoPoint**](StopPointApi.md#stopPointGetByGeoPoint) | **GET** /StopPoint | Gets a list of StopPoints within {radius} by the specified criteria |
| [**stopPointGetByMode**](StopPointApi.md#stopPointGetByMode) | **GET** /StopPoint/Mode/{modes} | Gets a list of StopPoints filtered by the modes available at that StopPoint. |
| [**stopPointGetBySms**](StopPointApi.md#stopPointGetBySms) | **GET** /StopPoint/Sms/{id} | Gets a StopPoint for a given sms code. |
| [**stopPointGetByType**](StopPointApi.md#stopPointGetByType) | **GET** /StopPoint/Type/{types} | Gets all stop points of a given type |
| [**stopPointGetByTypeWithPagination**](StopPointApi.md#stopPointGetByTypeWithPagination) | **GET** /StopPoint/Type/{types}/page/{page} | Gets all the stop points of given type(s) with a page number |
| [**stopPointGetCarParksById**](StopPointApi.md#stopPointGetCarParksById) | **GET** /StopPoint/{stopPointId}/CarParks | Get car parks corresponding to the given stop point id. |
| [**stopPointGetServiceTypes**](StopPointApi.md#stopPointGetServiceTypes) | **GET** /StopPoint/ServiceTypes | Gets the service types for a given stoppoint |
| [**stopPointGetTaxiRanksByIds**](StopPointApi.md#stopPointGetTaxiRanksByIds) | **GET** /StopPoint/{stopPointId}/TaxiRanks | Gets a list of taxi ranks corresponding to the given stop point id. |
| [**stopPointIdPlaceTypesGet**](StopPointApi.md#stopPointIdPlaceTypesGet) | **GET** /StopPoint/{id}/placeTypes | Get a list of places corresponding to a given id and place types. |
| [**stopPointMetaCategories**](StopPointApi.md#stopPointMetaCategories) | **GET** /StopPoint/Meta/Categories | Gets the list of available StopPoint additional information categories |
| [**stopPointMetaModes**](StopPointApi.md#stopPointMetaModes) | **GET** /StopPoint/Meta/Modes | Gets the list of available StopPoint modes |
| [**stopPointMetaStopTypes**](StopPointApi.md#stopPointMetaStopTypes) | **GET** /StopPoint/Meta/StopTypes | Gets the list of available StopPoint types |
| [**stopPointReachableFrom**](StopPointApi.md#stopPointReachableFrom) | **GET** /StopPoint/{id}/CanReachOnLine/{lineId} | Gets Stopoints that are reachable from a station/line combination. |
| [**stopPointRoute**](StopPointApi.md#stopPointRoute) | **GET** /StopPoint/{id}/Route | Returns the route sections for all the lines that service the given stop point ids |
| [**stopPointSearch**](StopPointApi.md#stopPointSearch) | **GET** /StopPoint/Search/{query} | Search StopPoints by their common name, or their 5-digit Countdown Bus Stop Code. |
| [**stopPointSearchGet**](StopPointApi.md#stopPointSearchGet) | **GET** /StopPoint/Search | Search StopPoints by their common name, or their 5-digit Countdown Bus Stop Code. |


<a id="stopPointArrivalDepartures"></a>
# **stopPointArrivalDepartures**
> List&lt;TflApiPresentationEntitiesArrivalDeparture&gt; stopPointArrivalDepartures(id, lineIds)

Gets the list of arrival and departure predictions for the given stop point id (overground, Elizabeth line and thameslink only)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StopPointApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    StopPointApi apiInstance = new StopPointApi(defaultClient);
    String id = "id_example"; // String | A StopPoint id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name)
    List<String> lineIds = Arrays.asList(); // List<String> | A comma-separated list of line ids e.g. elizabeth, london-overground, thameslink
    try {
      List<TflApiPresentationEntitiesArrivalDeparture> result = apiInstance.stopPointArrivalDepartures(id, lineIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StopPointApi#stopPointArrivalDepartures");
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
| **id** | **String**| A StopPoint id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name) | |
| **lineIds** | [**List&lt;String&gt;**](String.md)| A comma-separated list of line ids e.g. elizabeth, london-overground, thameslink | |

### Return type

[**List&lt;TflApiPresentationEntitiesArrivalDeparture&gt;**](TflApiPresentationEntitiesArrivalDeparture.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="stopPointArrivals"></a>
# **stopPointArrivals**
> List&lt;TflApiPresentationEntitiesPrediction&gt; stopPointArrivals(id)

Gets the list of arrival predictions for the given stop point id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StopPointApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    StopPointApi apiInstance = new StopPointApi(defaultClient);
    String id = "id_example"; // String | A StopPoint id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name)
    try {
      List<TflApiPresentationEntitiesPrediction> result = apiInstance.stopPointArrivals(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StopPointApi#stopPointArrivals");
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
| **id** | **String**| A StopPoint id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name) | |

### Return type

[**List&lt;TflApiPresentationEntitiesPrediction&gt;**](TflApiPresentationEntitiesPrediction.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="stopPointCrowding"></a>
# **stopPointCrowding**
> List&lt;TflApiPresentationEntitiesStopPoint&gt; stopPointCrowding(id, line, direction)

Gets all the Crowding data (static) for the StopPointId, plus crowding data for a given line and optionally a particular direction.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StopPointApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    StopPointApi apiInstance = new StopPointApi(defaultClient);
    String id = "id_example"; // String | The Naptan id of the stop
    String line = "line_example"; // String | A particular line e.g. victoria, circle, northern etc.
    String direction = "inbound"; // String | The direction of travel. Can be inbound or outbound.
    try {
      List<TflApiPresentationEntitiesStopPoint> result = apiInstance.stopPointCrowding(id, line, direction);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StopPointApi#stopPointCrowding");
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
| **id** | **String**| The Naptan id of the stop | |
| **line** | **String**| A particular line e.g. victoria, circle, northern etc. | |
| **direction** | **String**| The direction of travel. Can be inbound or outbound. | [enum: inbound, outbound, all] |

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

<a id="stopPointDirection"></a>
# **stopPointDirection**
> String stopPointDirection(id, toStopPointId, lineId)

Returns the canonical direction, \&quot;inbound\&quot; or \&quot;outbound\&quot;, for a given pair of stop point Ids in the direction from -&amp;gt; to.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StopPointApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    StopPointApi apiInstance = new StopPointApi(defaultClient);
    String id = "id_example"; // String | Originating stop id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name)
    String toStopPointId = "toStopPointId_example"; // String | Destination stop id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name)
    String lineId = "lineId_example"; // String | Optional line id filter e.g. victoria
    try {
      String result = apiInstance.stopPointDirection(id, toStopPointId, lineId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StopPointApi#stopPointDirection");
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
| **id** | **String**| Originating stop id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name) | |
| **toStopPointId** | **String**| Destination stop id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name) | |
| **lineId** | **String**| Optional line id filter e.g. victoria | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="stopPointDisruption"></a>
# **stopPointDisruption**
> List&lt;TflApiPresentationEntitiesDisruptedPoint&gt; stopPointDisruption(ids, getFamily, includeRouteBlockedStops, flattenResponse)

Gets all disruptions for the specified StopPointId, plus disruptions for any child Naptan records it may have.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StopPointApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    StopPointApi apiInstance = new StopPointApi(defaultClient);
    List<String> ids = Arrays.asList(); // List<String> | A comma-seperated list of stop point ids. Max. approx. 20 ids.              You can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name.
    Boolean getFamily = true; // Boolean | Specify true to return disruptions for entire family, or false to return disruptions for just this stop point. Defaults to false.
    Boolean includeRouteBlockedStops = true; // Boolean | 
    Boolean flattenResponse = true; // Boolean | Specify true to associate all disruptions with parent stop point. (Only applicable when getFamily is true).
    try {
      List<TflApiPresentationEntitiesDisruptedPoint> result = apiInstance.stopPointDisruption(ids, getFamily, includeRouteBlockedStops, flattenResponse);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StopPointApi#stopPointDisruption");
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
| **ids** | [**List&lt;String&gt;**](String.md)| A comma-seperated list of stop point ids. Max. approx. 20 ids.              You can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name. | |
| **getFamily** | **Boolean**| Specify true to return disruptions for entire family, or false to return disruptions for just this stop point. Defaults to false. | [optional] |
| **includeRouteBlockedStops** | **Boolean**|  | [optional] |
| **flattenResponse** | **Boolean**| Specify true to associate all disruptions with parent stop point. (Only applicable when getFamily is true). | [optional] |

### Return type

[**List&lt;TflApiPresentationEntitiesDisruptedPoint&gt;**](TflApiPresentationEntitiesDisruptedPoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="stopPointDisruptionByMode"></a>
# **stopPointDisruptionByMode**
> List&lt;TflApiPresentationEntitiesDisruptedPoint&gt; stopPointDisruptionByMode(modes, includeRouteBlockedStops)

Gets a distinct list of disrupted stop points for the given modes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StopPointApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    StopPointApi apiInstance = new StopPointApi(defaultClient);
    List<String> modes = Arrays.asList(); // List<String> | A comma-seperated list of modes e.g. tube,dlr
    Boolean includeRouteBlockedStops = true; // Boolean | 
    try {
      List<TflApiPresentationEntitiesDisruptedPoint> result = apiInstance.stopPointDisruptionByMode(modes, includeRouteBlockedStops);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StopPointApi#stopPointDisruptionByMode");
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
| **modes** | [**List&lt;String&gt;**](String.md)| A comma-seperated list of modes e.g. tube,dlr | |
| **includeRouteBlockedStops** | **Boolean**|  | [optional] |

### Return type

[**List&lt;TflApiPresentationEntitiesDisruptedPoint&gt;**](TflApiPresentationEntitiesDisruptedPoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="stopPointGet"></a>
# **stopPointGet**
> List&lt;TflApiPresentationEntitiesStopPoint&gt; stopPointGet(ids, includeCrowdingData)

Gets a list of StopPoints corresponding to the given list of stop ids.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StopPointApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    StopPointApi apiInstance = new StopPointApi(defaultClient);
    List<String> ids = Arrays.asList(); // List<String> | A comma-separated list of stop point ids (station naptan code e.g. 940GZZLUASL). Max. approx. 20 ids.              You can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name.
    Boolean includeCrowdingData = true; // Boolean | Include the crowding data (static). To Filter further use: /StopPoint/{ids}/Crowding/{line}
    try {
      List<TflApiPresentationEntitiesStopPoint> result = apiInstance.stopPointGet(ids, includeCrowdingData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StopPointApi#stopPointGet");
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
| **ids** | [**List&lt;String&gt;**](String.md)| A comma-separated list of stop point ids (station naptan code e.g. 940GZZLUASL). Max. approx. 20 ids.              You can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name. | |
| **includeCrowdingData** | **Boolean**| Include the crowding data (static). To Filter further use: /StopPoint/{ids}/Crowding/{line} | [optional] |

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

<a id="stopPointGetByGeoPoint"></a>
# **stopPointGetByGeoPoint**
> TflApiPresentationEntitiesStopPointsResponse stopPointGetByGeoPoint(stopTypes, locationLat, locationLon, radius, useStopPointHierarchy, modes, categories, returnLines)

Gets a list of StopPoints within {radius} by the specified criteria

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StopPointApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    StopPointApi apiInstance = new StopPointApi(defaultClient);
    List<String> stopTypes = Arrays.asList(); // List<String> | a list of stopTypes that should be returned (a list of valid stop types can be obtained from the StopPoint/meta/stoptypes endpoint)
    Double locationLat = 3.4D; // Double | 
    Double locationLon = 3.4D; // Double | 
    Integer radius = 56; // Integer | the radius of the bounding circle in metres (default : 200)
    Boolean useStopPointHierarchy = true; // Boolean | Re-arrange the output into a parent/child hierarchy
    List<String> modes = Arrays.asList(); // List<String> | the list of modes to search (comma separated mode names e.g. tube,dlr)
    List<String> categories = Arrays.asList(); // List<String> | an optional list of comma separated property categories to return in the StopPoint's property bag. If null or empty, all categories of property are returned. Pass the keyword \"none\" to return no properties (a valid list of categories can be obtained from the /StopPoint/Meta/categories endpoint)
    Boolean returnLines = true; // Boolean | true to return the lines that each stop point serves as a nested resource
    try {
      TflApiPresentationEntitiesStopPointsResponse result = apiInstance.stopPointGetByGeoPoint(stopTypes, locationLat, locationLon, radius, useStopPointHierarchy, modes, categories, returnLines);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StopPointApi#stopPointGetByGeoPoint");
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
| **stopTypes** | [**List&lt;String&gt;**](String.md)| a list of stopTypes that should be returned (a list of valid stop types can be obtained from the StopPoint/meta/stoptypes endpoint) | |
| **locationLat** | **Double**|  | |
| **locationLon** | **Double**|  | |
| **radius** | **Integer**| the radius of the bounding circle in metres (default : 200) | [optional] |
| **useStopPointHierarchy** | **Boolean**| Re-arrange the output into a parent/child hierarchy | [optional] |
| **modes** | [**List&lt;String&gt;**](String.md)| the list of modes to search (comma separated mode names e.g. tube,dlr) | [optional] |
| **categories** | [**List&lt;String&gt;**](String.md)| an optional list of comma separated property categories to return in the StopPoint&#39;s property bag. If null or empty, all categories of property are returned. Pass the keyword \&quot;none\&quot; to return no properties (a valid list of categories can be obtained from the /StopPoint/Meta/categories endpoint) | [optional] |
| **returnLines** | **Boolean**| true to return the lines that each stop point serves as a nested resource | [optional] |

### Return type

[**TflApiPresentationEntitiesStopPointsResponse**](TflApiPresentationEntitiesStopPointsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="stopPointGetByMode"></a>
# **stopPointGetByMode**
> TflApiPresentationEntitiesStopPointsResponse stopPointGetByMode(modes, page)

Gets a list of StopPoints filtered by the modes available at that StopPoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StopPointApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    StopPointApi apiInstance = new StopPointApi(defaultClient);
    List<String> modes = Arrays.asList(); // List<String> | A comma-seperated list of modes e.g. tube,dlr
    Integer page = 56; // Integer | The data set page to return. Page 1 equates to the first 1000 stop points, page 2 equates to 1001-2000 etc. Must be entered for bus mode as data set is too large.
    try {
      TflApiPresentationEntitiesStopPointsResponse result = apiInstance.stopPointGetByMode(modes, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StopPointApi#stopPointGetByMode");
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
| **modes** | [**List&lt;String&gt;**](String.md)| A comma-seperated list of modes e.g. tube,dlr | |
| **page** | **Integer**| The data set page to return. Page 1 equates to the first 1000 stop points, page 2 equates to 1001-2000 etc. Must be entered for bus mode as data set is too large. | [optional] |

### Return type

[**TflApiPresentationEntitiesStopPointsResponse**](TflApiPresentationEntitiesStopPointsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="stopPointGetBySms"></a>
# **stopPointGetBySms**
> Object stopPointGetBySms(id, output)

Gets a StopPoint for a given sms code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StopPointApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    StopPointApi apiInstance = new StopPointApi(defaultClient);
    String id = "id_example"; // String | A 5-digit Countdown Bus Stop Code e.g. 73241, 50435, 56334.
    String output = "output_example"; // String | If set to \"web\", a 302 redirect to relevant website bus stop page is returned. Valid values are : web. All other values are ignored.
    try {
      Object result = apiInstance.stopPointGetBySms(id, output);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StopPointApi#stopPointGetBySms");
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
| **id** | **String**| A 5-digit Countdown Bus Stop Code e.g. 73241, 50435, 56334. | |
| **output** | **String**| If set to \&quot;web\&quot;, a 302 redirect to relevant website bus stop page is returned. Valid values are : web. All other values are ignored. | [optional] |

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

<a id="stopPointGetByType"></a>
# **stopPointGetByType**
> List&lt;TflApiPresentationEntitiesStopPoint&gt; stopPointGetByType(types)

Gets all stop points of a given type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StopPointApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    StopPointApi apiInstance = new StopPointApi(defaultClient);
    List<String> types = Arrays.asList(); // List<String> | A comma-separated list of the types to return. Max. approx. 12 types.               A list of valid stop types can be obtained from the StopPoint/meta/stoptypes endpoint.
    try {
      List<TflApiPresentationEntitiesStopPoint> result = apiInstance.stopPointGetByType(types);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StopPointApi#stopPointGetByType");
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
| **types** | [**List&lt;String&gt;**](String.md)| A comma-separated list of the types to return. Max. approx. 12 types.               A list of valid stop types can be obtained from the StopPoint/meta/stoptypes endpoint. | |

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

<a id="stopPointGetByTypeWithPagination"></a>
# **stopPointGetByTypeWithPagination**
> List&lt;TflApiPresentationEntitiesStopPoint&gt; stopPointGetByTypeWithPagination(types, page)

Gets all the stop points of given type(s) with a page number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StopPointApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    StopPointApi apiInstance = new StopPointApi(defaultClient);
    List<String> types = Arrays.asList(); // List<String> | 
    Integer page = 56; // Integer | 
    try {
      List<TflApiPresentationEntitiesStopPoint> result = apiInstance.stopPointGetByTypeWithPagination(types, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StopPointApi#stopPointGetByTypeWithPagination");
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
| **types** | [**List&lt;String&gt;**](String.md)|  | |
| **page** | **Integer**|  | |

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

<a id="stopPointGetCarParksById"></a>
# **stopPointGetCarParksById**
> List&lt;TflApiPresentationEntitiesPlace&gt; stopPointGetCarParksById(stopPointId)

Get car parks corresponding to the given stop point id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StopPointApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    StopPointApi apiInstance = new StopPointApi(defaultClient);
    String stopPointId = "stopPointId_example"; // String | stopPointId is required to get the car parks.
    try {
      List<TflApiPresentationEntitiesPlace> result = apiInstance.stopPointGetCarParksById(stopPointId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StopPointApi#stopPointGetCarParksById");
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
| **stopPointId** | **String**| stopPointId is required to get the car parks. | |

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

<a id="stopPointGetServiceTypes"></a>
# **stopPointGetServiceTypes**
> List&lt;TflApiPresentationEntitiesLineServiceType&gt; stopPointGetServiceTypes(id, lineIds, modes)

Gets the service types for a given stoppoint

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StopPointApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    StopPointApi apiInstance = new StopPointApi(defaultClient);
    String id = "id_example"; // String | The Naptan id of the stop
    List<String> lineIds = Arrays.asList(); // List<String> | The lines which contain the given Naptan id (all lines relevant to the given stoppoint if empty)
    List<String> modes = Arrays.asList(); // List<String> | The modes which the lines are relevant to (all if empty)
    try {
      List<TflApiPresentationEntitiesLineServiceType> result = apiInstance.stopPointGetServiceTypes(id, lineIds, modes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StopPointApi#stopPointGetServiceTypes");
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
| **id** | **String**| The Naptan id of the stop | |
| **lineIds** | [**List&lt;String&gt;**](String.md)| The lines which contain the given Naptan id (all lines relevant to the given stoppoint if empty) | [optional] |
| **modes** | [**List&lt;String&gt;**](String.md)| The modes which the lines are relevant to (all if empty) | [optional] |

### Return type

[**List&lt;TflApiPresentationEntitiesLineServiceType&gt;**](TflApiPresentationEntitiesLineServiceType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="stopPointGetTaxiRanksByIds"></a>
# **stopPointGetTaxiRanksByIds**
> List&lt;TflApiPresentationEntitiesPlace&gt; stopPointGetTaxiRanksByIds(stopPointId)

Gets a list of taxi ranks corresponding to the given stop point id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StopPointApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    StopPointApi apiInstance = new StopPointApi(defaultClient);
    String stopPointId = "stopPointId_example"; // String | stopPointId is required to get the taxi ranks.
    try {
      List<TflApiPresentationEntitiesPlace> result = apiInstance.stopPointGetTaxiRanksByIds(stopPointId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StopPointApi#stopPointGetTaxiRanksByIds");
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
| **stopPointId** | **String**| stopPointId is required to get the taxi ranks. | |

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

<a id="stopPointIdPlaceTypesGet"></a>
# **stopPointIdPlaceTypesGet**
> List&lt;TflApiPresentationEntitiesPlace&gt; stopPointIdPlaceTypesGet(id, placeTypes)

Get a list of places corresponding to a given id and place types.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StopPointApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    StopPointApi apiInstance = new StopPointApi(defaultClient);
    String id = "id_example"; // String | A naptan id for a stop point (station naptan code e.g. 940GZZLUASL).
    List<String> placeTypes = Arrays.asList(); // List<String> | A comcomma-separated value representing the place types.
    try {
      List<TflApiPresentationEntitiesPlace> result = apiInstance.stopPointIdPlaceTypesGet(id, placeTypes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StopPointApi#stopPointIdPlaceTypesGet");
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
| **id** | **String**| A naptan id for a stop point (station naptan code e.g. 940GZZLUASL). | |
| **placeTypes** | [**List&lt;String&gt;**](String.md)| A comcomma-separated value representing the place types. | |

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

<a id="stopPointMetaCategories"></a>
# **stopPointMetaCategories**
> List&lt;TflApiPresentationEntitiesStopPointCategory&gt; stopPointMetaCategories()

Gets the list of available StopPoint additional information categories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StopPointApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    StopPointApi apiInstance = new StopPointApi(defaultClient);
    try {
      List<TflApiPresentationEntitiesStopPointCategory> result = apiInstance.stopPointMetaCategories();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StopPointApi#stopPointMetaCategories");
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

[**List&lt;TflApiPresentationEntitiesStopPointCategory&gt;**](TflApiPresentationEntitiesStopPointCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="stopPointMetaModes"></a>
# **stopPointMetaModes**
> List&lt;TflApiPresentationEntitiesMode&gt; stopPointMetaModes()

Gets the list of available StopPoint modes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StopPointApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    StopPointApi apiInstance = new StopPointApi(defaultClient);
    try {
      List<TflApiPresentationEntitiesMode> result = apiInstance.stopPointMetaModes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StopPointApi#stopPointMetaModes");
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

[**List&lt;TflApiPresentationEntitiesMode&gt;**](TflApiPresentationEntitiesMode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="stopPointMetaStopTypes"></a>
# **stopPointMetaStopTypes**
> List&lt;String&gt; stopPointMetaStopTypes()

Gets the list of available StopPoint types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StopPointApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    StopPointApi apiInstance = new StopPointApi(defaultClient);
    try {
      List<String> result = apiInstance.stopPointMetaStopTypes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StopPointApi#stopPointMetaStopTypes");
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

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="stopPointReachableFrom"></a>
# **stopPointReachableFrom**
> List&lt;TflApiPresentationEntitiesStopPoint&gt; stopPointReachableFrom(id, lineId, serviceTypes)

Gets Stopoints that are reachable from a station/line combination.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StopPointApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    StopPointApi apiInstance = new StopPointApi(defaultClient);
    String id = "id_example"; // String | The id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name) of the stop point to filter by
    String lineId = "lineId_example"; // String | Line id of the line to filter by (e.g. victoria)
    List<String> serviceTypes = Arrays.asList(); // List<String> | A comma-separated list of service types to filter on. If not specified. Supported values: Regular, Night. Defaulted to 'Regular' if not specified
    try {
      List<TflApiPresentationEntitiesStopPoint> result = apiInstance.stopPointReachableFrom(id, lineId, serviceTypes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StopPointApi#stopPointReachableFrom");
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
| **id** | **String**| The id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name) of the stop point to filter by | |
| **lineId** | **String**| Line id of the line to filter by (e.g. victoria) | |
| **serviceTypes** | [**List&lt;String&gt;**](String.md)| A comma-separated list of service types to filter on. If not specified. Supported values: Regular, Night. Defaulted to &#39;Regular&#39; if not specified | [optional] [enum: Regular, Night] |

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

<a id="stopPointRoute"></a>
# **stopPointRoute**
> List&lt;TflApiPresentationEntitiesStopPointRouteSection&gt; stopPointRoute(id, serviceTypes)

Returns the route sections for all the lines that service the given stop point ids

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StopPointApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    StopPointApi apiInstance = new StopPointApi(defaultClient);
    String id = "id_example"; // String | A stop point id (station naptan codes e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name)
    List<String> serviceTypes = Arrays.asList(); // List<String> | A comma-separated list of service types to filter on. If not specified. Supported values: Regular, Night. Defaulted to 'Regular' if not specified
    try {
      List<TflApiPresentationEntitiesStopPointRouteSection> result = apiInstance.stopPointRoute(id, serviceTypes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StopPointApi#stopPointRoute");
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
| **id** | **String**| A stop point id (station naptan codes e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name) | |
| **serviceTypes** | [**List&lt;String&gt;**](String.md)| A comma-separated list of service types to filter on. If not specified. Supported values: Regular, Night. Defaulted to &#39;Regular&#39; if not specified | [optional] [enum: Regular, Night] |

### Return type

[**List&lt;TflApiPresentationEntitiesStopPointRouteSection&gt;**](TflApiPresentationEntitiesStopPointRouteSection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="stopPointSearch"></a>
# **stopPointSearch**
> TflApiPresentationEntitiesSearchResponse stopPointSearch(query, modes, faresOnly, maxResults, lines, includeHubs, tflOperatedNationalRailStationsOnly)

Search StopPoints by their common name, or their 5-digit Countdown Bus Stop Code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StopPointApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    StopPointApi apiInstance = new StopPointApi(defaultClient);
    String query = "query_example"; // String | The query string, case-insensitive. Leading and trailing wildcards are applied automatically.
    List<String> modes = Arrays.asList(); // List<String> | An optional, parameter separated list of the modes to filter by
    Boolean faresOnly = true; // Boolean | True to only return stations in that have Fares data available for single fares to another station.
    Integer maxResults = 56; // Integer | An optional result limit, defaulting to and with a maximum of 50. Since children of the stop point heirarchy are returned for matches,              it is possible that the flattened result set will contain more than 50 items.
    List<String> lines = Arrays.asList(); // List<String> | An optional, parameter separated list of the lines to filter by
    Boolean includeHubs = true; // Boolean | If true, returns results including HUBs.
    Boolean tflOperatedNationalRailStationsOnly = true; // Boolean | If the national-rail mode is included, this flag will filter the national rail stations so that only those operated by TfL are returned
    try {
      TflApiPresentationEntitiesSearchResponse result = apiInstance.stopPointSearch(query, modes, faresOnly, maxResults, lines, includeHubs, tflOperatedNationalRailStationsOnly);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StopPointApi#stopPointSearch");
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
| **query** | **String**| The query string, case-insensitive. Leading and trailing wildcards are applied automatically. | |
| **modes** | [**List&lt;String&gt;**](String.md)| An optional, parameter separated list of the modes to filter by | [optional] |
| **faresOnly** | **Boolean**| True to only return stations in that have Fares data available for single fares to another station. | [optional] |
| **maxResults** | **Integer**| An optional result limit, defaulting to and with a maximum of 50. Since children of the stop point heirarchy are returned for matches,              it is possible that the flattened result set will contain more than 50 items. | [optional] |
| **lines** | [**List&lt;String&gt;**](String.md)| An optional, parameter separated list of the lines to filter by | [optional] |
| **includeHubs** | **Boolean**| If true, returns results including HUBs. | [optional] |
| **tflOperatedNationalRailStationsOnly** | **Boolean**| If the national-rail mode is included, this flag will filter the national rail stations so that only those operated by TfL are returned | [optional] |

### Return type

[**TflApiPresentationEntitiesSearchResponse**](TflApiPresentationEntitiesSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="stopPointSearchGet"></a>
# **stopPointSearchGet**
> TflApiPresentationEntitiesSearchResponse stopPointSearchGet(query, modes, faresOnly, maxResults, lines, includeHubs, tflOperatedNationalRailStationsOnly)

Search StopPoints by their common name, or their 5-digit Countdown Bus Stop Code.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StopPointApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.digital.tfl.gov.uk");

    StopPointApi apiInstance = new StopPointApi(defaultClient);
    String query = "query_example"; // String | The query string, case-insensitive. Leading and trailing wildcards are applied automatically.
    List<String> modes = Arrays.asList(); // List<String> | An optional, parameter separated list of the modes to filter by
    Boolean faresOnly = true; // Boolean | True to only return stations in that have Fares data available for single fares to another station.
    Integer maxResults = 56; // Integer | An optional result limit, defaulting to and with a maximum of 50. Since children of the stop point heirarchy are returned for matches,              it is possible that the flattened result set will contain more than 50 items.
    List<String> lines = Arrays.asList(); // List<String> | An optional, parameter separated list of the lines to filter by
    Boolean includeHubs = true; // Boolean | If true, returns results including HUBs.
    Boolean tflOperatedNationalRailStationsOnly = true; // Boolean | If the national-rail mode is included, this flag will filter the national rail stations so that only those operated by TfL are returned
    try {
      TflApiPresentationEntitiesSearchResponse result = apiInstance.stopPointSearchGet(query, modes, faresOnly, maxResults, lines, includeHubs, tflOperatedNationalRailStationsOnly);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StopPointApi#stopPointSearchGet");
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
| **query** | **String**| The query string, case-insensitive. Leading and trailing wildcards are applied automatically. | |
| **modes** | [**List&lt;String&gt;**](String.md)| An optional, parameter separated list of the modes to filter by | [optional] |
| **faresOnly** | **Boolean**| True to only return stations in that have Fares data available for single fares to another station. | [optional] |
| **maxResults** | **Integer**| An optional result limit, defaulting to and with a maximum of 50. Since children of the stop point heirarchy are returned for matches,              it is possible that the flattened result set will contain more than 50 items. | [optional] |
| **lines** | [**List&lt;String&gt;**](String.md)| An optional, parameter separated list of the lines to filter by | [optional] |
| **includeHubs** | **Boolean**| If true, returns results including HUBs. | [optional] |
| **tflOperatedNationalRailStationsOnly** | **Boolean**| If the national-rail mode is included, this flag will filter the national rail stations so that only those operated by TfL are returned | [optional] |

### Return type

[**TflApiPresentationEntitiesSearchResponse**](TflApiPresentationEntitiesSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

