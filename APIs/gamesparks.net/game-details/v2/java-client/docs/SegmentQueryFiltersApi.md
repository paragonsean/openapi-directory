# SegmentQueryFiltersApi

All URIs are relative to *http://config2.gamesparks.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSegmentQueryFiltersConfigUsingGET**](SegmentQueryFiltersApi.md#getSegmentQueryFiltersConfigUsingGET) | **GET** /restv2/game/{apiKey}/admin/segmentQueryFilters/config | getSegmentQueryFiltersConfig |
| [**getSegmentQueryFiltersUsingGET**](SegmentQueryFiltersApi.md#getSegmentQueryFiltersUsingGET) | **GET** /restv2/game/{apiKey}/admin/segmentQueryFilters | getSegmentQueryFilters |
| [**getSegmentQueryStandardFiltersUsingGET**](SegmentQueryFiltersApi.md#getSegmentQueryStandardFiltersUsingGET) | **GET** /restv2/game/{apiKey}/admin/segmentQueryFilters/standardFilters | getSegmentQueryStandardFilters |
| [**updateSegmentQueryFiltersConfigUsingPUT**](SegmentQueryFiltersApi.md#updateSegmentQueryFiltersConfigUsingPUT) | **PUT** /restv2/game/{apiKey}/admin/segmentQueryFilters/config | updateSegmentQueryFiltersConfig |


<a id="getSegmentQueryFiltersConfigUsingGET"></a>
# **getSegmentQueryFiltersConfigUsingGET**
> SegmentQueryFilterConfigModel getSegmentQueryFiltersConfigUsingGET(apiKey)

getSegmentQueryFiltersConfig

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SegmentQueryFiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    SegmentQueryFiltersApi apiInstance = new SegmentQueryFiltersApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    try {
      SegmentQueryFilterConfigModel result = apiInstance.getSegmentQueryFiltersConfigUsingGET(apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SegmentQueryFiltersApi#getSegmentQueryFiltersConfigUsingGET");
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
| **apiKey** | **String**| apiKey | |

### Return type

[**SegmentQueryFilterConfigModel**](SegmentQueryFilterConfigModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="getSegmentQueryFiltersUsingGET"></a>
# **getSegmentQueryFiltersUsingGET**
> SegmentQueryFilterListModel getSegmentQueryFiltersUsingGET(apiKey)

getSegmentQueryFilters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SegmentQueryFiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    SegmentQueryFiltersApi apiInstance = new SegmentQueryFiltersApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    try {
      SegmentQueryFilterListModel result = apiInstance.getSegmentQueryFiltersUsingGET(apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SegmentQueryFiltersApi#getSegmentQueryFiltersUsingGET");
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
| **apiKey** | **String**| apiKey | |

### Return type

[**SegmentQueryFilterListModel**](SegmentQueryFilterListModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="getSegmentQueryStandardFiltersUsingGET"></a>
# **getSegmentQueryStandardFiltersUsingGET**
> SegmentQueryFilterListModel getSegmentQueryStandardFiltersUsingGET(apiKey)

getSegmentQueryStandardFilters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SegmentQueryFiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    SegmentQueryFiltersApi apiInstance = new SegmentQueryFiltersApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    try {
      SegmentQueryFilterListModel result = apiInstance.getSegmentQueryStandardFiltersUsingGET(apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SegmentQueryFiltersApi#getSegmentQueryStandardFiltersUsingGET");
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
| **apiKey** | **String**| apiKey | |

### Return type

[**SegmentQueryFilterListModel**](SegmentQueryFilterListModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

<a id="updateSegmentQueryFiltersConfigUsingPUT"></a>
# **updateSegmentQueryFiltersConfigUsingPUT**
> SegmentQueryFilterConfigModel updateSegmentQueryFiltersConfigUsingPUT(apiKey, segmentQueryFilterConfigModel)

updateSegmentQueryFiltersConfig

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SegmentQueryFiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://config2.gamesparks.net");

    SegmentQueryFiltersApi apiInstance = new SegmentQueryFiltersApi(defaultClient);
    String apiKey = "apiKey_example"; // String | apiKey
    SegmentQueryFilterConfigModel segmentQueryFilterConfigModel = new SegmentQueryFilterConfigModel(); // SegmentQueryFilterConfigModel | segmentQueryConfig
    try {
      SegmentQueryFilterConfigModel result = apiInstance.updateSegmentQueryFiltersConfigUsingPUT(apiKey, segmentQueryFilterConfigModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SegmentQueryFiltersApi#updateSegmentQueryFiltersConfigUsingPUT");
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
| **apiKey** | **String**| apiKey | |
| **segmentQueryFilterConfigModel** | [**SegmentQueryFilterConfigModel**](SegmentQueryFilterConfigModel.md)| segmentQueryConfig | |

### Return type

[**SegmentQueryFilterConfigModel**](SegmentQueryFilterConfigModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | json error |  -  |
| **403** | not allowed |  -  |
| **404** | not found |  -  |

