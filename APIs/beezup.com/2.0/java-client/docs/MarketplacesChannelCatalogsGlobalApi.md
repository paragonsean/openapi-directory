# MarketplacesChannelCatalogsGlobalApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMarketplaceChannelCatalogs**](MarketplacesChannelCatalogsGlobalApi.md#getMarketplaceChannelCatalogs) | **GET** /v2/user/marketplaces/channelcatalogs/ | Get your marketplace channel catalog list |


<a id="getMarketplaceChannelCatalogs"></a>
# **getMarketplaceChannelCatalogs**
> MarketplaceChannelCatalogList getMarketplaceChannelCatalogs(storeId)

Get your marketplace channel catalog list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesChannelCatalogsGlobalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesChannelCatalogsGlobalApi apiInstance = new MarketplacesChannelCatalogsGlobalApi(defaultClient);
    String storeId = "04730364-9826-4ff3-92e4-51fccd02bf10"; // String | The StoreId to filter by
    try {
      MarketplaceChannelCatalogList result = apiInstance.getMarketplaceChannelCatalogs(storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesChannelCatalogsGlobalApi#getMarketplaceChannelCatalogs");
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
| **storeId** | **String**| The StoreId to filter by | [optional] |

### Return type

[**MarketplaceChannelCatalogList**](MarketplaceChannelCatalogList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Marketplace channel catalog list |  -  |
| **404** | Store not found |  -  |

