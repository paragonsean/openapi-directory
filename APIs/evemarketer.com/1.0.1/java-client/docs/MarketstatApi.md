# MarketstatApi

All URIs are relative to *https://api.evemarketer.com/ec*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**marketstatGet**](MarketstatApi.md#marketstatGet) | **GET** /marketstat | XML Marketstat |
| [**marketstatJsonGet**](MarketstatApi.md#marketstatJsonGet) | **GET** /marketstat/json | JSON Marketstat |
| [**marketstatJsonPost**](MarketstatApi.md#marketstatJsonPost) | **POST** /marketstat/json | JSON Marketstat |
| [**marketstatPost**](MarketstatApi.md#marketstatPost) | **POST** /marketstat | XML Marketstat |


<a id="marketstatGet"></a>
# **marketstatGet**
> ExecAPI marketstatGet(typeid, regionlimit, usesystem)

XML Marketstat

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketstatApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.evemarketer.com/ec");

    MarketstatApi apiInstance = new MarketstatApi(defaultClient);
    List<Integer> typeid = Arrays.asList(); // List<Integer> | TypeID. Multiple TypeIDs can be specified in the following format (up to 200 TypeIDs per request): typeid=34&typeid=35 or typeid=34,35 
    Integer regionlimit = 56; // Integer | Limit the statistics to a single region.
    Integer usesystem = 56; // Integer | Limit the statistics to a single solar system.
    try {
      ExecAPI result = apiInstance.marketstatGet(typeid, regionlimit, usesystem);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketstatApi#marketstatGet");
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
| **typeid** | [**List&lt;Integer&gt;**](Integer.md)| TypeID. Multiple TypeIDs can be specified in the following format (up to 200 TypeIDs per request): typeid&#x3D;34&amp;typeid&#x3D;35 or typeid&#x3D;34,35  | |
| **regionlimit** | **Integer**| Limit the statistics to a single region. | [optional] |
| **usesystem** | **Integer**| Limit the statistics to a single solar system. | [optional] |

### Return type

[**ExecAPI**](ExecAPI.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Request |  * X-Ratelimit-Reset - The time at which the current rate limit window resets in UTC epoch seconds. <br>  * X-Ratelimit-Limit - The number of allowed requests in the current period <br>  * X-Ratelimit-Remaining - The number of remaining requests in the current period <br>  |
| **400** | Invalid Parameters |  -  |
| **429** | Rate limit exceeded |  -  |

<a id="marketstatJsonGet"></a>
# **marketstatJsonGet**
> List&lt;Type&gt; marketstatJsonGet(typeid, regionlimit, usesystem)

JSON Marketstat

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketstatApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.evemarketer.com/ec");

    MarketstatApi apiInstance = new MarketstatApi(defaultClient);
    List<Integer> typeid = Arrays.asList(); // List<Integer> | TypeID. Multiple TypeIDs can be specified in the following format (up to 200 TypeIDs per request): typeid=34&typeid=35 or typeid=34,35 
    Integer regionlimit = 56; // Integer | Limit the statistics to a single region.
    Integer usesystem = 56; // Integer | Limit the statistics to a single region.
    try {
      List<Type> result = apiInstance.marketstatJsonGet(typeid, regionlimit, usesystem);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketstatApi#marketstatJsonGet");
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
| **typeid** | [**List&lt;Integer&gt;**](Integer.md)| TypeID. Multiple TypeIDs can be specified in the following format (up to 200 TypeIDs per request): typeid&#x3D;34&amp;typeid&#x3D;35 or typeid&#x3D;34,35  | |
| **regionlimit** | **Integer**| Limit the statistics to a single region. | [optional] |
| **usesystem** | **Integer**| Limit the statistics to a single region. | [optional] |

### Return type

[**List&lt;Type&gt;**](Type.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Request |  * X-Ratelimit-Reset - The time at which the current rate limit window resets in UTC epoch seconds. <br>  * X-Ratelimit-Limit - The number of allowed requests in the current period <br>  * X-Ratelimit-Remaining - The number of remaining requests in the current period <br>  |
| **400** | Invalid Parameters |  -  |
| **429** | Rate limit exceeded |  -  |

<a id="marketstatJsonPost"></a>
# **marketstatJsonPost**
> List&lt;Type&gt; marketstatJsonPost(typeid, regionlimit, usesystem)

JSON Marketstat

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketstatApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.evemarketer.com/ec");

    MarketstatApi apiInstance = new MarketstatApi(defaultClient);
    List<Integer> typeid = Arrays.asList(); // List<Integer> | TypeID. Multiple TypeIDs can be specified in the following format (up to 200 TypeIDs per request): typeid=34&typeid=35 or typeid=34,35 
    Integer regionlimit = 56; // Integer | Limit the statistics to a single region.
    Integer usesystem = 56; // Integer | Limit the statistics to a single region.
    try {
      List<Type> result = apiInstance.marketstatJsonPost(typeid, regionlimit, usesystem);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketstatApi#marketstatJsonPost");
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
| **typeid** | [**List&lt;Integer&gt;**](Integer.md)| TypeID. Multiple TypeIDs can be specified in the following format (up to 200 TypeIDs per request): typeid&#x3D;34&amp;typeid&#x3D;35 or typeid&#x3D;34,35  | |
| **regionlimit** | **Integer**| Limit the statistics to a single region. | [optional] |
| **usesystem** | **Integer**| Limit the statistics to a single region. | [optional] |

### Return type

[**List&lt;Type&gt;**](Type.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Request |  * X-Ratelimit-Reset - The time at which the current rate limit window resets in UTC epoch seconds. <br>  * X-Ratelimit-Limit - The number of allowed requests in the current period <br>  * X-Ratelimit-Remaining - The number of remaining requests in the current period <br>  |
| **400** | Invalid Parameters |  -  |
| **429** | Rate limit exceeded |  -  |

<a id="marketstatPost"></a>
# **marketstatPost**
> ExecAPI marketstatPost(typeid, regionlimit, usesystem)

XML Marketstat

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketstatApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.evemarketer.com/ec");

    MarketstatApi apiInstance = new MarketstatApi(defaultClient);
    List<Integer> typeid = Arrays.asList(); // List<Integer> | TypeID. Multiple TypeIDs can be specified in the following format (up to 200 TypeIDs per request): typeid=34&typeid=35 or typeid=34,35 
    Integer regionlimit = 56; // Integer | Limit the statistics to a single region.
    Integer usesystem = 56; // Integer | Limit the statistics to a single solar system.
    try {
      ExecAPI result = apiInstance.marketstatPost(typeid, regionlimit, usesystem);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketstatApi#marketstatPost");
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
| **typeid** | [**List&lt;Integer&gt;**](Integer.md)| TypeID. Multiple TypeIDs can be specified in the following format (up to 200 TypeIDs per request): typeid&#x3D;34&amp;typeid&#x3D;35 or typeid&#x3D;34,35  | |
| **regionlimit** | **Integer**| Limit the statistics to a single region. | [optional] |
| **usesystem** | **Integer**| Limit the statistics to a single solar system. | [optional] |

### Return type

[**ExecAPI**](ExecAPI.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Request |  * X-Ratelimit-Reset - The time at which the current rate limit window resets in UTC epoch seconds. <br>  * X-Ratelimit-Limit - The number of allowed requests in the current period <br>  * X-Ratelimit-Remaining - The number of remaining requests in the current period <br>  |
| **400** | Invalid Parameters |  -  |
| **429** | Rate limit exceeded |  -  |

