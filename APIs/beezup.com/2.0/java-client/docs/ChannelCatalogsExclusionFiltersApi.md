# ChannelCatalogsExclusionFiltersApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**configureChannelCatalogExclusionFilters**](ChannelCatalogsExclusionFiltersApi.md#configureChannelCatalogExclusionFilters) | **PUT** /v2/user/channelCatalogs/{channelCatalogId}/exclusionFilters | Configure channel catalog exclusion filters |
| [**getChannelCatalogExclusionFilters**](ChannelCatalogsExclusionFiltersApi.md#getChannelCatalogExclusionFilters) | **GET** /v2/user/channelCatalogs/{channelCatalogId}/exclusionFilters | Get channel catalog exclusion filters |


<a id="configureChannelCatalogExclusionFilters"></a>
# **configureChannelCatalogExclusionFilters**
> configureChannelCatalogExclusionFilters(channelCatalogId, exclusionFilter)

Configure channel catalog exclusion filters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelCatalogsExclusionFiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelCatalogsExclusionFiltersApi apiInstance = new ChannelCatalogsExclusionFiltersApi(defaultClient);
    String channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
    List<ExclusionFilter> exclusionFilter = Arrays.asList(); // List<ExclusionFilter> | 
    try {
      apiInstance.configureChannelCatalogExclusionFilters(channelCatalogId, exclusionFilter);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelCatalogsExclusionFiltersApi#configureChannelCatalogExclusionFilters");
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
| **exclusionFilter** | [**List&lt;ExclusionFilter&gt;**](ExclusionFilter.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Channel catalog exclusion filter list configured |  -  |
| **400** | BadRequest. See Error Response for more details |  -  |
| **404** | ChannelCatalogId not found or not authorized |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getChannelCatalogExclusionFilters"></a>
# **getChannelCatalogExclusionFilters**
> ExclusionFiltersResponse getChannelCatalogExclusionFilters(channelCatalogId)

Get channel catalog exclusion filters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelCatalogsExclusionFiltersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelCatalogsExclusionFiltersApi apiInstance = new ChannelCatalogsExclusionFiltersApi(defaultClient);
    String channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
    try {
      ExclusionFiltersResponse result = apiInstance.getChannelCatalogExclusionFilters(channelCatalogId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelCatalogsExclusionFiltersApi#getChannelCatalogExclusionFilters");
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

[**ExclusionFiltersResponse**](ExclusionFiltersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Channel catalog exclusion filter list |  -  |
| **404** | ChannelCatalogId not found or not authorized |  -  |
| **0** | Occurs when something goes wrong |  -  |

