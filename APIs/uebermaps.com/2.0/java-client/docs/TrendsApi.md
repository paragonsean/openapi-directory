# TrendsApi

All URIs are relative to *http://uebermaps.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**trendsLatestGet**](TrendsApi.md#trendsLatestGet) | **GET** /trends/latest | List latest maps |
| [**trendsRecommendedGet**](TrendsApi.md#trendsRecommendedGet) | **GET** /trends/recommended | List recommended maps |


<a id="trendsLatestGet"></a>
# **trendsLatestGet**
> List&lt;Map&gt; trendsLatestGet()

List latest maps

List latest maps.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrendsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    TrendsApi apiInstance = new TrendsApi(defaultClient);
    try {
      List<Map> result = apiInstance.trendsLatestGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrendsApi#trendsLatestGet");
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

[**List&lt;Map&gt;**](Map.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains list of maps. |  -  |

<a id="trendsRecommendedGet"></a>
# **trendsRecommendedGet**
> List&lt;Map&gt; trendsRecommendedGet()

List recommended maps

List recommended maps.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TrendsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    TrendsApi apiInstance = new TrendsApi(defaultClient);
    try {
      List<Map> result = apiInstance.trendsRecommendedGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TrendsApi#trendsRecommendedGet");
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

[**List&lt;Map&gt;**](Map.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains list of maps. |  -  |

