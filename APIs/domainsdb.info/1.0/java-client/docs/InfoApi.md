# InfoApi

All URIs are relative to */v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getApiInfoItem**](InfoApi.md#getApiInfoItem) | **GET** /info/api |  |
| [**getStatisticsCollection**](InfoApi.md#getStatisticsCollection) | **GET** /info/stat/ | Returns overall stagtistics |
| [**getStatisticsItem**](InfoApi.md#getStatisticsItem) | **GET** /info/stat/{zone} | Returns statistics for specific zone |
| [**infoTldGet**](InfoApi.md#infoTldGet) | **GET** /info/tld/ | Returns overall Tld info |
| [**infoTldZoneGet**](InfoApi.md#infoTldZoneGet) | **GET** /info/tld/{zone} | Returns statistics for specific zone |


<a id="getApiInfoItem"></a>
# **getApiInfoItem**
> APIKeyInfo getApiInfoItem(apiKey)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v1");

    InfoApi apiInstance = new InfoApi(defaultClient);
    String apiKey = "apiKey_example"; // String | API key
    try {
      APIKeyInfo result = apiInstance.getApiInfoItem(apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfoApi#getApiInfoItem");
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
| **apiKey** | **String**| API key | [optional] |

### Return type

[**APIKeyInfo**](APIKeyInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getStatisticsCollection"></a>
# **getStatisticsCollection**
> List&lt;ZoneStats&gt; getStatisticsCollection(page, limit)

Returns overall stagtistics

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v1");

    InfoApi apiInstance = new InfoApi(defaultClient);
    String page = "page_example"; // String | Search page to request
    Integer limit = 50; // Integer | Results per page
    try {
      List<ZoneStats> result = apiInstance.getStatisticsCollection(page, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfoApi#getStatisticsCollection");
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
| **page** | **String**| Search page to request | [optional] |
| **limit** | **Integer**| Results per page | [optional] [default to 50] |

### Return type

[**List&lt;ZoneStats&gt;**](ZoneStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getStatisticsItem"></a>
# **getStatisticsItem**
> ZoneStats getStatisticsItem(zone, page, limit)

Returns statistics for specific zone

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v1");

    InfoApi apiInstance = new InfoApi(defaultClient);
    String zone = "zone_example"; // String | 
    String page = "page_example"; // String | Search page to request
    Integer limit = 50; // Integer | Results per page
    try {
      ZoneStats result = apiInstance.getStatisticsItem(zone, page, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfoApi#getStatisticsItem");
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
| **zone** | **String**|  | |
| **page** | **String**| Search page to request | [optional] |
| **limit** | **Integer**| Results per page | [optional] [default to 50] |

### Return type

[**ZoneStats**](ZoneStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Zone not found. |  -  |

<a id="infoTldGet"></a>
# **infoTldGet**
> List&lt;ZoneInfo&gt; infoTldGet()

Returns overall Tld info

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v1");

    InfoApi apiInstance = new InfoApi(defaultClient);
    try {
      List<ZoneInfo> result = apiInstance.infoTldGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfoApi#infoTldGet");
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

[**List&lt;ZoneInfo&gt;**](ZoneInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="infoTldZoneGet"></a>
# **infoTldZoneGet**
> ZoneInfo infoTldZoneGet(zone, page, limit)

Returns statistics for specific zone

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v1");

    InfoApi apiInstance = new InfoApi(defaultClient);
    String zone = "zone_example"; // String | 
    String page = "page_example"; // String | Search page to request
    Integer limit = 50; // Integer | Results per page
    try {
      ZoneInfo result = apiInstance.infoTldZoneGet(zone, page, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfoApi#infoTldZoneGet");
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
| **zone** | **String**|  | |
| **page** | **String**| Search page to request | [optional] |
| **limit** | **Integer**| Results per page | [optional] [default to 50] |

### Return type

[**ZoneInfo**](ZoneInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Zone not found. |  -  |

