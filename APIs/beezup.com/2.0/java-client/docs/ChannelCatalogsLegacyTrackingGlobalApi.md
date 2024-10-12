# ChannelCatalogsLegacyTrackingGlobalApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getLegacyTrackingChannelCatalog**](ChannelCatalogsLegacyTrackingGlobalApi.md#getLegacyTrackingChannelCatalog) | **GET** /v2/user/legacyTracking/channelCatalogs/{channelCatalogId} | Get the channel catalog configured to use legacy tracking format information |
| [**getLegacyTrackingChannelCatalogs**](ChannelCatalogsLegacyTrackingGlobalApi.md#getLegacyTrackingChannelCatalogs) | **GET** /v2/user/legacyTracking/channelCatalogs/ | List all your current channel catalogs configured to use legacy tracking format |
| [**migrateLegacyTrackingChannelCatalog**](ChannelCatalogsLegacyTrackingGlobalApi.md#migrateLegacyTrackingChannelCatalog) | **POST** /v2/user/legacyTracking/channelCatalogs/{channelCatalogId}/migrate | Migrate a channel catalog to current tracking format |


<a id="getLegacyTrackingChannelCatalog"></a>
# **getLegacyTrackingChannelCatalog**
> LegacyTrackingChannelCatalog getLegacyTrackingChannelCatalog(channelCatalogId)

Get the channel catalog configured to use legacy tracking format information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelCatalogsLegacyTrackingGlobalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelCatalogsLegacyTrackingGlobalApi apiInstance = new ChannelCatalogsLegacyTrackingGlobalApi(defaultClient);
    String channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
    try {
      LegacyTrackingChannelCatalog result = apiInstance.getLegacyTrackingChannelCatalog(channelCatalogId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelCatalogsLegacyTrackingGlobalApi#getLegacyTrackingChannelCatalog");
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

[**LegacyTrackingChannelCatalog**](LegacyTrackingChannelCatalog.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Channel catalog configured to use legacy tracking format |  -  |
| **404** | Channel catalog not found or not authorized |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getLegacyTrackingChannelCatalogs"></a>
# **getLegacyTrackingChannelCatalogs**
> LegacyTrackingChannelCatalogList getLegacyTrackingChannelCatalogs(storeId)

List all your current channel catalogs configured to use legacy tracking format

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelCatalogsLegacyTrackingGlobalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelCatalogsLegacyTrackingGlobalApi apiInstance = new ChannelCatalogsLegacyTrackingGlobalApi(defaultClient);
    String storeId = "04730364-9826-4ff3-92e4-51fccd02bf10"; // String | The store identifier
    try {
      LegacyTrackingChannelCatalogList result = apiInstance.getLegacyTrackingChannelCatalogs(storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelCatalogsLegacyTrackingGlobalApi#getLegacyTrackingChannelCatalogs");
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
| **storeId** | **String**| The store identifier | [optional] |

### Return type

[**LegacyTrackingChannelCatalogList**](LegacyTrackingChannelCatalogList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="migrateLegacyTrackingChannelCatalog"></a>
# **migrateLegacyTrackingChannelCatalog**
> migrateLegacyTrackingChannelCatalog(channelCatalogId)

Migrate a channel catalog to current tracking format

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelCatalogsLegacyTrackingGlobalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelCatalogsLegacyTrackingGlobalApi apiInstance = new ChannelCatalogsLegacyTrackingGlobalApi(defaultClient);
    String channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
    try {
      apiInstance.migrateLegacyTrackingChannelCatalog(channelCatalogId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelCatalogsLegacyTrackingGlobalApi#migrateLegacyTrackingChannelCatalog");
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
| **204** | Channel catalog migrated |  -  |
| **404** | Channel catalog not found or not authorized |  -  |
| **0** | Occurs when something goes wrong |  -  |

