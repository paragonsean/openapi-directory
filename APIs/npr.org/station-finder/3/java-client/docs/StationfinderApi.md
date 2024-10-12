# StationfinderApi

All URIs are relative to *https://station.api.npr.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getStationById**](StationfinderApi.md#getStationById) | **GET** /v3/stations/{stationId} | Retrieve metadata for the station with the given numeric ID |
| [**searchStations**](StationfinderApi.md#searchStations) | **GET** /v3/stations | List stations close to you or filter by search criteria |


<a id="getStationById"></a>
# **getStationById**
> StationDocument getStationById(authorization, stationId)

Retrieve metadata for the station with the given numeric ID

This endpoint retrieves information about a given station, based on its numeric ID, which is consistent across all of NPR&#39;s APIs.  A typical use case for this data is for clients who want to create a dropdown menu, modal/pop-up or dedicated page displaying more information about the station the client is localized to, including, for example, links to the station&#39;s homepage and donation (pledge) page.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StationfinderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://station.api.npr.org");

    StationfinderApi apiInstance = new StationfinderApi(defaultClient);
    String authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
    Long stationId = 56L; // Long | The numeric ID of a station
    try {
      StationDocument result = apiInstance.getStationById(authorization, stationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StationfinderApi#getStationById");
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
| **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | |
| **stationId** | **Long**| The numeric ID of a station | |

### Return type

[**StationDocument**](StationDocument.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.collection.doc+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A document describing the station with the given ID |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **400** | A bad request; generally, one or more parameters passed in were incorrect or missing |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **401** | The client is not authorized to complete this request. Check to ensure a valid access token was passed in the headers. |  -  |
| **404** | The resource with the requested ID could not be found, and the server was unable to complete the request. |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **429** | The client has exceeded the number of daily calls as per their rate limit. For now, this only applies to prototype applications and untrusted clients. Trusted clients will never be rate-limited, nor will any production apps. |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **500** | A server error |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **503** | The system is undergoing maintenance and we are unable to fulfill this request. Look for a &#x60;Retry-After&#x60; header to see the predicted time the system will be back up. |  * Retry-After - The predicted time the system will be back up <br>  |

<a id="searchStations"></a>
# **searchStations**
> StationListDocument searchStations(authorization, q, city, state, lat, lon)

List stations close to you or filter by search criteria

This endpoint has two main use cases:  - If no query parameters passed in, it returns a list of stations that are geographically closest to the calling client (based on GeoIP information) - If one or more query parameters are passed in, it performs a search of NPR stations that match those search criteria (not taking into account the client&#39;s physical location)  Clients wanting to implement a &#39;Change Station&#39; UI should use this endpoint to power their search. In most cases, you&#39;ll want to build a search interface that uses one of the 3 provided schemas: &#x60;lat&#x60; and &#x60;lon&#x60; (using e.g. the HTML5 Geolocation API), &#x60;city&#x60; and &#x60;state&#x60;, _or_ the generic &#x60;q&#x60; query which can accept a station name, call letters, network name, or zip code. Technically speaking, &#x60;q&#x60; can also take in either a city name or a state name, but using the &#x60;city&#x60; and &#x60;state&#x60; parameters together will yield more accurate geographic search results than &#x60;q&#x3D;{cityName}&#x60;.  The &#x60;lat&#x60; and &#x60;lon&#x60; query parameters should always be passed in together (otherwise the API will return a 400 error), and if included in the query, they will take precedence over any other search criteria; that is, &#x60;lat&#x60; and &#x60;lon&#x60; will do a purely geographic search and not take into account &#x60;q&#x60;, &#x60;city&#x60; or &#x60;state&#x60;.  Similarly, &#x60;city&#x60; and/or &#x60;state&#x60; will take precedence over (and ignore) &#x60;q&#x60;.  If clients want to be able to offer multiple types of searches (e.g. &#39;Search for a station name, city or zipcode&#39;) using a *single* search input form, &#x60;q&#x60; should be used. But again, be aware that using &#x60;city&#x60; and &#x60;state&#x60; together will yield more accurate search results than &#x60;q&#x3D;{cityName}&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StationfinderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://station.api.npr.org");

    StationfinderApi apiInstance = new StationfinderApi(defaultClient);
    String authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
    String q = "q_example"; // String | Search terms to search on; can be a station name, network name, call letters, or zipcode
    String city = "city_example"; // String | A city to look for stations from; intended to be paired with `state`
    String state = "state_example"; // String | A state to look for stations from (using the 2-letter abbreviation); intended to be paired with `city`
    Float lat = 3.4F; // Float | A latitude value from a geographic coordinate system; only works if paired with `lon`
    Float lon = 3.4F; // Float | A longitude value from a geographic coordinate system; only works if paired with `lat`
    try {
      StationListDocument result = apiInstance.searchStations(authorization, q, city, state, lat, lon);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StationfinderApi#searchStations");
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
| **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | |
| **q** | **String**| Search terms to search on; can be a station name, network name, call letters, or zipcode | [optional] |
| **city** | **String**| A city to look for stations from; intended to be paired with &#x60;state&#x60; | [optional] |
| **state** | **String**| A state to look for stations from (using the 2-letter abbreviation); intended to be paired with &#x60;city&#x60; | [optional] |
| **lat** | **Float**| A latitude value from a geographic coordinate system; only works if paired with &#x60;lon&#x60; | [optional] |
| **lon** | **Float**| A longitude value from a geographic coordinate system; only works if paired with &#x60;lat&#x60; | [optional] |

### Return type

[**StationListDocument**](StationListDocument.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.collection.doc+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of one or more stations matching the search query |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **400** | A bad request; generally, one or more parameters passed in were incorrect or missing |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **401** | The client is not authorized to complete this request. Check to ensure a valid access token was passed in the headers. |  -  |
| **429** | The client has exceeded the number of daily calls as per their rate limit. For now, this only applies to prototype applications and untrusted clients. Trusted clients will never be rate-limited, nor will any production apps. |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **500** | A server error |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **503** | The system is undergoing maintenance and we are unable to fulfill this request. Look for a &#x60;Retry-After&#x60; header to see the predicted time the system will be back up. |  * Retry-After - The predicted time the system will be back up <br>  |

