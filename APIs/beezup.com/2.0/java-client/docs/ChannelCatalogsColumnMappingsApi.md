# ChannelCatalogsColumnMappingsApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**configureChannelCatalogColumnMappings**](ChannelCatalogsColumnMappingsApi.md#configureChannelCatalogColumnMappings) | **PUT** /v2/user/channelCatalogs/{channelCatalogId}/columnMappings | Configure channel catalog column mappings |


<a id="configureChannelCatalogColumnMappings"></a>
# **configureChannelCatalogColumnMappings**
> configureChannelCatalogColumnMappings(channelCatalogId, channelCatalogColumnMapping)

Configure channel catalog column mappings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelCatalogsColumnMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelCatalogsColumnMappingsApi apiInstance = new ChannelCatalogsColumnMappingsApi(defaultClient);
    String channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
    List<ChannelCatalogColumnMapping> channelCatalogColumnMapping = Arrays.asList(); // List<ChannelCatalogColumnMapping> | 
    try {
      apiInstance.configureChannelCatalogColumnMappings(channelCatalogId, channelCatalogColumnMapping);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelCatalogsColumnMappingsApi#configureChannelCatalogColumnMappings");
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
| **channelCatalogColumnMapping** | [**List&lt;ChannelCatalogColumnMapping&gt;**](ChannelCatalogColumnMapping.md)|  | |

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
| **204** | Channel catalog column mappings configured |  -  |
| **404** | ChannelCatalogId not found or not authorized |  -  |
| **0** | Occurs when something goes wrong |  -  |

