# ChannelCatalogsExportationsApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**clearChannelCatalogExportationCache**](ChannelCatalogsExportationsApi.md#clearChannelCatalogExportationCache) | **POST** /v2/user/channelCatalogs/{channelCatalogId}/exportations/cache/clear | Clear the exportation cache |
| [**getChannelCatalogExportationCacheInfo**](ChannelCatalogsExportationsApi.md#getChannelCatalogExportationCacheInfo) | **GET** /v2/user/channelCatalogs/{channelCatalogId}/exportations/cache | Get the exportation cache information |
| [**getChannelCatalogExportationHistory**](ChannelCatalogsExportationsApi.md#getChannelCatalogExportationHistory) | **GET** /v2/user/channelCatalogs/{channelCatalogId}/exportations/history | Get the exportation history |


<a id="clearChannelCatalogExportationCache"></a>
# **clearChannelCatalogExportationCache**
> clearChannelCatalogExportationCache(channelCatalogId)

Clear the exportation cache

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelCatalogsExportationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelCatalogsExportationsApi apiInstance = new ChannelCatalogsExportationsApi(defaultClient);
    String channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
    try {
      apiInstance.clearChannelCatalogExportationCache(channelCatalogId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelCatalogsExportationsApi#clearChannelCatalogExportationCache");
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
| **channelCatalogId** | **String**| The channel catalog identifier | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Channel catalog exportation cache cleared |  -  |
| **404** | ChannelCatalogId not found or not authorized |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getChannelCatalogExportationCacheInfo"></a>
# **getChannelCatalogExportationCacheInfo**
> ChannelCatalogExportCacheInfoResponse getChannelCatalogExportationCacheInfo(channelCatalogId)

Get the exportation cache information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelCatalogsExportationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelCatalogsExportationsApi apiInstance = new ChannelCatalogsExportationsApi(defaultClient);
    String channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
    try {
      ChannelCatalogExportCacheInfoResponse result = apiInstance.getChannelCatalogExportationCacheInfo(channelCatalogId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelCatalogsExportationsApi#getChannelCatalogExportationCacheInfo");
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
| **channelCatalogId** | **String**| The channel catalog identifier | |

### Return type

[**ChannelCatalogExportCacheInfoResponse**](ChannelCatalogExportCacheInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Channel catalog exportation cache information |  -  |
| **404** | ChannelCatalogId not found or not authorized |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getChannelCatalogExportationHistory"></a>
# **getChannelCatalogExportationHistory**
> ChannelCatalogExportationHistory getChannelCatalogExportationHistory(channelCatalogId, pageNumber, pageSize)

Get the exportation history

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelCatalogsExportationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelCatalogsExportationsApi apiInstance = new ChannelCatalogsExportationsApi(defaultClient);
    String channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
    Integer pageNumber = 1; // Integer | The page number you want to get
    Integer pageSize = 25; // Integer | The entry count you want to get
    try {
      ChannelCatalogExportationHistory result = apiInstance.getChannelCatalogExportationHistory(channelCatalogId, pageNumber, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelCatalogsExportationsApi#getChannelCatalogExportationHistory");
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
| **channelCatalogId** | **String**| The channel catalog identifier | |
| **pageNumber** | **Integer**| The page number you want to get | |
| **pageSize** | **Integer**| The entry count you want to get | |

### Return type

[**ChannelCatalogExportationHistory**](ChannelCatalogExportationHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Channel catalog exportation history |  -  |
| **404** | ChannelCatalogId not found or not authorized |  -  |
| **0** | Occurs when something goes wrong |  -  |

