# DefaultApi

All URIs are relative to *http://api.wmata.com/NextBusService.svc*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**call5476365e031f5909e4fe331d**](DefaultApi.md#call5476365e031f5909e4fe331d) | **GET** /json/jPredictions | JSON - Next Buses |
| [**call5476365e031f5909e4fe331e**](DefaultApi.md#call5476365e031f5909e4fe331e) | **GET** /Predictions | XML - Next Buses |


<a id="call5476365e031f5909e4fe331d"></a>
# **call5476365e031f5909e4fe331d**
> call5476365e031f5909e4fe331d(stopID)

JSON - Next Buses

&lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Description&lt;/h4&gt;    &lt;p&gt;Returns next bus arrival times at a stop.&lt;/p&gt;    &lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Response Elements&lt;/h4&gt;    &lt;table class&#x3D;\&quot;table table-condensed table-hover\&quot;&gt;  &lt;thead&gt;  &lt;tr&gt;  &lt;th class&#x3D;\&quot;col-md-3\&quot;&gt;Element&lt;/th&gt;    &lt;th&gt;Description&lt;/th&gt;  &lt;/tr&gt;  &lt;/thead&gt;    &lt;tbody&gt;  &lt;tr&gt;  &lt;td&gt;Predictions&lt;/td&gt;    &lt;td&gt;  Array containing bus predictions (&lt;a href&#x3D;  \&quot;#NextBusPrediction\&quot;&gt;NextBusPrediction&lt;/a&gt;).  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;StopName&lt;/td&gt;    &lt;td&gt;Full name of the given StopID.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td colspan&#x3D;\&quot;2\&quot;&gt;  &lt;div class&#x3D;\&quot;text-primary\&quot; style&#x3D;\&quot;margin-top: 1em\&quot;&gt;  &lt;a id&#x3D;\&quot;NextBusPrediction\&quot; name&#x3D;  \&quot;NextBusPrediction\&quot;&gt;NextBusPrediction Elements&lt;/a&gt;  &lt;/div&gt;  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;DirectionNum&lt;/td&gt;    &lt;td&gt;Denotes a binary direction (0 or 1) of the bus. There is no  specific mapping to direction, but a different value for the same  route signifies that the buses are traveling in opposite  directions. Use the DirectionText element to show the actual  destination of the bus.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;DirectionText&lt;/td&gt;    &lt;td&gt;Customer-friendly description of direction and destination for  a bus.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Minutes&lt;/td&gt;    &lt;td&gt;Minutes until bus arrival at this stop. Numeric value.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;RouteID&lt;/td&gt;    &lt;td&gt;Base route name as shown on the bus. This can be used in other  bus-related methods. Note that all variants will be shown as their  base route names (i.e.: 10Av1 and 10Av2 will be shown as 10A).&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;TripID&lt;/td&gt;    &lt;td&gt;Trip identifier. This can be correlated with the data in our  bus schedule information as well as bus positions.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;VehicleID&lt;/td&gt;    &lt;td&gt;Bus identifier. This can be correlated with results returned  from bus positions.&lt;/td&gt;  &lt;/tr&gt;  &lt;/tbody&gt;  &lt;/table&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.wmata.com/NextBusService.svc");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String stopID = "1001195"; // String | 7-digit regional stop ID.
    try {
      apiInstance.call5476365e031f5909e4fe331d(stopID);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#call5476365e031f5909e4fe331d");
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
| **stopID** | **String**| 7-digit regional stop ID. | [default to 1001195] [enum: 1001195] |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response type. |  -  |
| **400** | Response from invalid Stop ID. |  -  |

<a id="call5476365e031f5909e4fe331e"></a>
# **call5476365e031f5909e4fe331e**
> call5476365e031f5909e4fe331e(stopID)

XML - Next Buses

&lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Description&lt;/h4&gt;    &lt;p&gt;Returns next bus arrival times at a stop.&lt;/p&gt;    &lt;h4 class&#x3D;\&quot;text-primary\&quot;&gt;Response Elements&lt;/h4&gt;    &lt;table class&#x3D;\&quot;table table-condensed table-hover\&quot;&gt;  &lt;thead&gt;  &lt;tr&gt;  &lt;th class&#x3D;\&quot;col-md-3\&quot;&gt;Element&lt;/th&gt;    &lt;th&gt;Description&lt;/th&gt;  &lt;/tr&gt;  &lt;/thead&gt;    &lt;tbody&gt;  &lt;tr&gt;  &lt;td&gt;Predictions&lt;/td&gt;    &lt;td&gt;  Array containing bus predictions (&lt;a href&#x3D;  \&quot;#NextBusPrediction\&quot;&gt;NextBusPrediction&lt;/a&gt;).  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;StopName&lt;/td&gt;    &lt;td&gt;Full name of the given StopID.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td colspan&#x3D;\&quot;2\&quot;&gt;  &lt;div class&#x3D;\&quot;text-primary\&quot; style&#x3D;\&quot;margin-top: 1em\&quot;&gt;  &lt;a id&#x3D;\&quot;NextBusPrediction\&quot; name&#x3D;  \&quot;NextBusPrediction\&quot;&gt;NextBusPrediction Elements&lt;/a&gt;  &lt;/div&gt;  &lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;DirectionNum&lt;/td&gt;    &lt;td&gt;Denotes a binary direction (0 or 1) of the bus. There is no  specific mapping to direction, but a different value for the same  route signifies that the buses are traveling in opposite  directions. Use the DirectionText element to show the actual  destination of the bus.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;DirectionText&lt;/td&gt;    &lt;td&gt;Customer-friendly description of direction and destination for  a bus.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;Minutes&lt;/td&gt;    &lt;td&gt;Minutes until bus arrival at this stop. Numeric value.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;RouteID&lt;/td&gt;    &lt;td&gt;Base route name as shown on the bus. This can be used in other  bus-related methods. Note that all variants will be shown as their  base route names (i.e.: 10Av1 and 10Av2 will be shown as 10A).&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;TripID&lt;/td&gt;    &lt;td&gt;Trip identifier. This can be correlated with the data in our  bus schedule information as well as bus positions.&lt;/td&gt;  &lt;/tr&gt;    &lt;tr&gt;  &lt;td&gt;VehicleID&lt;/td&gt;    &lt;td&gt;Bus identifier. This can be correlated with results returned  from bus positions.&lt;/td&gt;  &lt;/tr&gt;  &lt;/tbody&gt;  &lt;/table&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.wmata.com/NextBusService.svc");
    
    // Configure API key authorization: apiKeyQuery
    ApiKeyAuth apiKeyQuery = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyQuery");
    apiKeyQuery.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyQuery.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKeyHeader
    ApiKeyAuth apiKeyHeader = (ApiKeyAuth) defaultClient.getAuthentication("apiKeyHeader");
    apiKeyHeader.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKeyHeader.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String stopID = "1001195"; // String | 7-digit regional stop ID.
    try {
      apiInstance.call5476365e031f5909e4fe331e(stopID);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#call5476365e031f5909e4fe331e");
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
| **stopID** | **String**| 7-digit regional stop ID. | [default to 1001195] [enum: 1001195] |

### Return type

null (empty response body)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response code. |  -  |
| **400** | Response from invalid Stop ID. |  -  |

