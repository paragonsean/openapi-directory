# RoutesApi

All URIs are relative to *https://esi.evetech.net/latest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getRouteOriginDestination**](RoutesApi.md#getRouteOriginDestination) | **GET** /route/{origin}/{destination}/ | Get route |


<a id="getRouteOriginDestination"></a>
# **getRouteOriginDestination**
> List&lt;Integer&gt; getRouteOriginDestination(destination, origin, avoid, connections, datasource, flag, ifNoneMatch)

Get route

Get the systems between origin and destination  --- Alternate route: &#x60;/dev/route/{origin}/{destination}/&#x60;  Alternate route: &#x60;/legacy/route/{origin}/{destination}/&#x60;  Alternate route: &#x60;/v1/route/{origin}/{destination}/&#x60;  --- This route is cached for up to 86400 seconds

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoutesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://esi.evetech.net/latest");

    RoutesApi apiInstance = new RoutesApi(defaultClient);
    Integer destination = 56; // Integer | destination solar system ID
    Integer origin = 56; // Integer | origin solar system ID
    Set<Integer> avoid = Arrays.asList(); // Set<Integer> | avoid solar system ID(s)
    Set<Set<Integer>> connections = Arrays.asList(new LinkedHashSet<>()); // Set<Set<Integer>> | connected solar system pairs
    String datasource = "tranquility"; // String | The server name you would like data from
    String flag = "shortest"; // String | route security preference
    String ifNoneMatch = "ifNoneMatch_example"; // String | ETag from a previous request. A 304 will be returned if this matches the current ETag
    try {
      List<Integer> result = apiInstance.getRouteOriginDestination(destination, origin, avoid, connections, datasource, flag, ifNoneMatch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoutesApi#getRouteOriginDestination");
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
| **destination** | **Integer**| destination solar system ID | |
| **origin** | **Integer**| origin solar system ID | |
| **avoid** | [**Set&lt;Integer&gt;**](Integer.md)| avoid solar system ID(s) | [optional] |
| **connections** | [**Set&lt;Set&lt;Integer&gt;&gt;**](Set&lt;Integer&gt;.md)| connected solar system pairs | [optional] |
| **datasource** | **String**| The server name you would like data from | [optional] [default to tranquility] [enum: tranquility, singularity] |
| **flag** | **String**| route security preference | [optional] [default to shortest] [enum: shortest, secure, insecure] |
| **ifNoneMatch** | **String**| ETag from a previous request. A 304 will be returned if this matches the current ETag | [optional] |

### Return type

**List&lt;Integer&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Solar systems in route from origin to destination |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **304** | Not modified |  * Cache-Control - The caching mechanism used <br>  * ETag - RFC7232 compliant entity tag <br>  * Expires - RFC7231 formatted datetime string <br>  * Last-Modified - RFC7231 formatted datetime string <br>  |
| **400** | Bad request |  -  |
| **404** | No route found |  -  |
| **420** | Error limited |  -  |
| **500** | Internal server error |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

