# MapMatchingApiApi

All URIs are relative to *https://graphhopper.com/api/1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postGPX**](MapMatchingApiApi.md#postGPX) | **POST** /match | Map-match a GPX file |


<a id="postGPX"></a>
# **postGPX**
> RouteResponse postGPX(gpsAccuracy, vehicle)

Map-match a GPX file

### Example You get an example response for a GPX via:  &#x60;&#x60;&#x60; curl -XPOST -H \&quot;Content-Type: application/gpx+xml\&quot; \&quot;https://graphhopper.com/api/1/match?vehicle&#x3D;car&amp;key&#x3D;[YOUR_KEY]\&quot; --data @/path/to/some.gpx &#x60;&#x60;&#x60;  A minimal working GPX file looks like &#x60;&#x60;&#x60;gpx &lt;gpx&gt;  &lt;trk&gt;   &lt;trkseg&gt;    &lt;trkpt lat&#x3D;\&quot;51.343657\&quot; lon&#x3D;\&quot;12.360708\&quot;&gt;&lt;/trkpt&gt;    &lt;trkpt lat&#x3D;\&quot;51.343796\&quot; lon&#x3D;\&quot;12.361337\&quot;&gt;&lt;/trkpt&gt;    &lt;trkpt lat&#x3D;\&quot;51.342784\&quot; lon&#x3D;\&quot;12.361882\&quot;&gt;&lt;/trkpt&gt;   &lt;/trkseg&gt;  &lt;/trk&gt; &lt;/gpx&gt; &#x60;&#x60;&#x60;  ### Introduction ![Map Matching screenshot](./img/map-matching-example.gif)  The Map Matching API is part of the GraphHopper Directions API and with this API you can snap measured GPS points typically as GPX files to a digital road network to e.g. clean data or attach certain data like elevation or turn instructions to it. Read more at Wikipedia.  In the example screenshot above and demo you see the Map Matching API in action where the black line is the GPS track and the green one is matched result.  Most of the times, you can simply POST a GPX file, but some of the request parameters of the [Routing API](#tag/Routing-API) apply here, too.  ### API Clients and Examples See the [clients](#section/API-Clients) section in the main documentation, and [live examples](https://graphhopper.com/api/1/examples/#map-matching).  ### Limits and Counts The cost for one request depends on the number of GPS location and is documented [here](https://graphhopper.com/api/1/docs/FAQ/).  One request should not exceed the Map Matching API location limit depending on the package, see the pricing in our dashboard. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MapMatchingApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://graphhopper.com/api/1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    MapMatchingApiApi apiInstance = new MapMatchingApiApi(defaultClient);
    Integer gpsAccuracy = 56; // Integer | Specify the precision of a point, in meter
    String vehicle = "vehicle_example"; // String | Specify the vehicle profile like car
    try {
      RouteResponse result = apiInstance.postGPX(gpsAccuracy, vehicle);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MapMatchingApiApi#postGPX");
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
| **gpsAccuracy** | **Integer**| Specify the precision of a point, in meter | [optional] |
| **vehicle** | **String**| Specify the vehicle profile like car | [optional] |

### Return type

[**RouteResponse**](RouteResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Routing Result |  * X-RateLimit-Credits - The credit costs for this request. Note it could be a decimal and even negative number, e.g. when an async request failed. <br>  * X-RateLimit-Limit - Your current daily credit limit. <br>  * X-RateLimit-Remaining - Your remaining credits until the reset. <br>  * X-RateLimit-Reset - The number of seconds that you have to wait before a reset of the credit count is done. <br>  |
| **0** | Unexpected Error |  -  |

