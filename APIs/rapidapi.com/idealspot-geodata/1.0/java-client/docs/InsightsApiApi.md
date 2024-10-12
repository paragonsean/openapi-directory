# InsightsApiApi

All URIs are relative to *https://idealspot-geodata.p.rapidapi.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchAvailableInsights**](InsightsApiApi.md#fetchAvailableInsights) | **GET** /data/insights | Fetch Available Insights |
| [**fetchInsightQueryParameters**](InsightsApiApi.md#fetchInsightQueryParameters) | **GET** /data/insights/{insight_id:} | Fetch Insight Query Parameters |
| [**queryInsightatLocation**](InsightsApiApi.md#queryInsightatLocation) | **GET** /data/insights/{insight_id:}/query | Query Insight at Location |


<a id="fetchAvailableInsights"></a>
# **fetchAvailableInsights**
> ListAllLocalInsights fetchAvailableInsights(xRapidAPIKey, xRapidAPIHost)

Fetch Available Insights

List all insights that the user has access to. This includes population, household income, crime statistics, walking traffic, vehicle traffic counts, employment, and much more,

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://idealspot-geodata.p.rapidapi.com/api/v1");

    InsightsApiApi apiInstance = new InsightsApiApi(defaultClient);
    String xRapidAPIKey = "xRapidAPIKey_example"; // String | (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata
    String xRapidAPIHost = "xRapidAPIHost_example"; // String | 
    try {
      ListAllLocalInsights result = apiInstance.fetchAvailableInsights(xRapidAPIKey, xRapidAPIHost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightsApiApi#fetchAvailableInsights");
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
| **xRapidAPIKey** | **String**| (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata | |
| **xRapidAPIHost** | **String**|  | |

### Return type

[**ListAllLocalInsights**](ListAllLocalInsights.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Length -  <br>  * Date -  <br>  * Server -  <br>  * Vary -  <br>  * Via -  <br>  * X-RapidAPI-Region -  <br>  * X-RapidAPI-Version -  <br>  * access-control-allow-credentials -  <br>  * access-control-allow-origin -  <br>  * access-control-expose-headers -  <br>  * cache-control -  <br>  |

<a id="fetchInsightQueryParameters"></a>
# **fetchInsightQueryParameters**
> DescribeOccupationInsight fetchInsightQueryParameters(insightIdColon, xRapidAPIKey, xRapidAPIHost)

Fetch Insight Query Parameters

Fetch request/response structure metadata for a given Insight. This provides you the periods of data available as well as any other parameters you may want to query the Insight by. Example Insights include population and market data such as: age, daytime population, avg. home value, crime indexes, foot traffic, employment, income, occupation, etc.  For the full-list see the developer documentation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://idealspot-geodata.p.rapidapi.com/api/v1");

    InsightsApiApi apiInstance = new InsightsApiApi(defaultClient);
    String insightIdColon = "insightIdColon_example"; // String | Insight ID. See developer documentation for full list.
    String xRapidAPIKey = "xRapidAPIKey_example"; // String | (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata
    String xRapidAPIHost = "xRapidAPIHost_example"; // String | 
    try {
      DescribeOccupationInsight result = apiInstance.fetchInsightQueryParameters(insightIdColon, xRapidAPIKey, xRapidAPIHost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightsApiApi#fetchInsightQueryParameters");
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
| **insightIdColon** | **String**| Insight ID. See developer documentation for full list. | |
| **xRapidAPIKey** | **String**| (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata | |
| **xRapidAPIHost** | **String**|  | |

### Return type

[**DescribeOccupationInsight**](DescribeOccupationInsight.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Length -  <br>  * Date -  <br>  * Server -  <br>  * Vary -  <br>  * Via -  <br>  * X-RapidAPI-Region -  <br>  * X-RapidAPI-Version -  <br>  * access-control-allow-credentials -  <br>  * access-control-allow-origin -  <br>  * access-control-expose-headers -  <br>  * cache-control -  <br>  |

<a id="queryInsightatLocation"></a>
# **queryInsightatLocation**
> Homevalueswithin1miRadiusofLocation queryInsightatLocation(version, location, insightIdColon, xRapidAPIKey, xRapidAPIHost)

Query Insight at Location

Execute a query for a given insight and location(s). Some Insights may require you to provide required options. ie., when querying &#x60;occupation&#x60; for White-Collar Workers, you can filter by opt&#x3D;&#x60;{\&quot;data\&quot;:{\&quot;category\&quot;:[2469]}}&#x60;  For examples of &#x60;locations&#x60;, please see [Location API Documentation](https://idealspot.gitlab.io/developer-docs/#location)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InsightsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://idealspot-geodata.p.rapidapi.com/api/v1");

    InsightsApiApi apiInstance = new InsightsApiApi(defaultClient);
    String version = "version_example"; // String | (Required) Insight version. Insight versions are incremented when a response format changes in any way, including the addition of new groups. Old versions are retained, unmodified, for backwards compatibility.
    String location = "location_example"; // String | (Required) Represents a buffer, region, or custom polygon specification. Accepts the `Location` model (as a `Buffer`, `Region`, or `Custom Polygon`) formatted as a JSON string. Multiple `location` query parameters are allowed. NOTE: When requesting multiple locations, you must include brackets(i.e. `?location[]=...&location[]=...`). If not included, only the last location will be used. For more detail, see https://idealspot.gitlab.io/developer-docs/#location
    String insightIdColon = "insightIdColon_example"; // String | Insight ID. See https://developer.idealspot.com/data for full list.
    String xRapidAPIKey = "xRapidAPIKey_example"; // String | (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata
    String xRapidAPIHost = "xRapidAPIHost_example"; // String | 
    try {
      Homevalueswithin1miRadiusofLocation result = apiInstance.queryInsightatLocation(version, location, insightIdColon, xRapidAPIKey, xRapidAPIHost);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InsightsApiApi#queryInsightatLocation");
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
| **version** | **String**| (Required) Insight version. Insight versions are incremented when a response format changes in any way, including the addition of new groups. Old versions are retained, unmodified, for backwards compatibility. | |
| **location** | **String**| (Required) Represents a buffer, region, or custom polygon specification. Accepts the &#x60;Location&#x60; model (as a &#x60;Buffer&#x60;, &#x60;Region&#x60;, or &#x60;Custom Polygon&#x60;) formatted as a JSON string. Multiple &#x60;location&#x60; query parameters are allowed. NOTE: When requesting multiple locations, you must include brackets(i.e. &#x60;?location[]&#x3D;...&amp;location[]&#x3D;...&#x60;). If not included, only the last location will be used. For more detail, see https://idealspot.gitlab.io/developer-docs/#location | |
| **insightIdColon** | **String**| Insight ID. See https://developer.idealspot.com/data for full list. | |
| **xRapidAPIKey** | **String**| (Required) Rapid API Key. See https://rapidapi.com/idealspot-inc-idealspot-inc-default/api/idealspot-geodata | |
| **xRapidAPIHost** | **String**|  | |

### Return type

[**Homevalueswithin1miRadiusofLocation**](Homevalueswithin1miRadiusofLocation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Length -  <br>  * Date -  <br>  * Server -  <br>  * Vary -  <br>  * Via -  <br>  * X-RapidAPI-Region -  <br>  * X-RapidAPI-Version -  <br>  * access-control-allow-credentials -  <br>  * access-control-allow-origin -  <br>  * access-control-expose-headers -  <br>  * cache-control -  <br>  |

