# MarketplacesChannelCatalogsSettingsApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getChannelCatalogMarketplaceProperties**](MarketplacesChannelCatalogsSettingsApi.md#getChannelCatalogMarketplaceProperties) | **GET** /v2/user/marketplaces/channelcatalogs/{channelCatalogId}/properties | Get the marketplace properties for a channel catalog |
| [**getChannelCatalogMarketplaceSettings**](MarketplacesChannelCatalogsSettingsApi.md#getChannelCatalogMarketplaceSettings) | **GET** /v2/user/marketplaces/channelcatalogs/{channelCatalogId}/settings | Get the marketplace settings for a channel catalog |
| [**setChannelCatalogMarketplaceSettings**](MarketplacesChannelCatalogsSettingsApi.md#setChannelCatalogMarketplaceSettings) | **POST** /v2/user/marketplaces/channelcatalogs/{channelCatalogId}/settings | Save new marketplace settings for a channel catalog |


<a id="getChannelCatalogMarketplaceProperties"></a>
# **getChannelCatalogMarketplaceProperties**
> ChannelCatalogMarketplaceProperties getChannelCatalogMarketplaceProperties(channelCatalogId, redirectionPageUrl, acceptLanguage)

Get the marketplace properties for a channel catalog

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesChannelCatalogsSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesChannelCatalogsSettingsApi apiInstance = new MarketplacesChannelCatalogsSettingsApi(defaultClient);
    String channelCatalogId = "channelCatalogId_example"; // String | 
    URI redirectionPageUrl = new URI(); // URI | 
    List<String> acceptLanguage = Arrays.asList(); // List<String> | Indicates that the client accepts the following languages.
    try {
      ChannelCatalogMarketplaceProperties result = apiInstance.getChannelCatalogMarketplaceProperties(channelCatalogId, redirectionPageUrl, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesChannelCatalogsSettingsApi#getChannelCatalogMarketplaceProperties");
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
| **channelCatalogId** | **String**|  | |
| **redirectionPageUrl** | **URI**|  | |
| **acceptLanguage** | [**List&lt;String&gt;**](String.md)| Indicates that the client accepts the following languages. | [optional] |

### Return type

[**ChannelCatalogMarketplaceProperties**](ChannelCatalogMarketplaceProperties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully fetched channel catalog properties |  -  |
| **404** | Marketplace channel Catalog not found |  -  |
| **503** | The marketplace configuration related to this channel catalog is currently in progress. Please retry later. |  * Retry-After - Indicate the duration to before the next retry in second. <br>  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getChannelCatalogMarketplaceSettings"></a>
# **getChannelCatalogMarketplaceSettings**
> ChannelCatalogMarketplaceSettings getChannelCatalogMarketplaceSettings(channelCatalogId)

Get the marketplace settings for a channel catalog

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesChannelCatalogsSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesChannelCatalogsSettingsApi apiInstance = new MarketplacesChannelCatalogsSettingsApi(defaultClient);
    String channelCatalogId = "channelCatalogId_example"; // String | Channel Catalog Id to query (required)
    try {
      ChannelCatalogMarketplaceSettings result = apiInstance.getChannelCatalogMarketplaceSettings(channelCatalogId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesChannelCatalogsSettingsApi#getChannelCatalogMarketplaceSettings");
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
| **channelCatalogId** | **String**| Channel Catalog Id to query (required) | |

### Return type

[**ChannelCatalogMarketplaceSettings**](ChannelCatalogMarketplaceSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully fetched channel catalog settings |  -  |
| **404** | Marketplace channel catalog not found |  -  |
| **503** | The marketplace configuration related to this channel catalog is currently in progress. Please retry later. |  * Retry-After - Indicate the duration to before the next retry in second. <br>  |
| **0** | Occurs when something goes wrong |  -  |

<a id="setChannelCatalogMarketplaceSettings"></a>
# **setChannelCatalogMarketplaceSettings**
> setChannelCatalogMarketplaceSettings(channelCatalogId, setChannelCatalogMarketplaceSettingsRequest)

Save new marketplace settings for a channel catalog

Allow you to configure your marketplace settings. Partial update accepted. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesChannelCatalogsSettingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesChannelCatalogsSettingsApi apiInstance = new MarketplacesChannelCatalogsSettingsApi(defaultClient);
    String channelCatalogId = "channelCatalogId_example"; // String | Channel Catalog Id to query
    SetChannelCatalogMarketplaceSettingsRequest setChannelCatalogMarketplaceSettingsRequest = new SetChannelCatalogMarketplaceSettingsRequest(); // SetChannelCatalogMarketplaceSettingsRequest | Settings to save
    try {
      apiInstance.setChannelCatalogMarketplaceSettings(channelCatalogId, setChannelCatalogMarketplaceSettingsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesChannelCatalogsSettingsApi#setChannelCatalogMarketplaceSettings");
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
| **channelCatalogId** | **String**| Channel Catalog Id to query | |
| **setChannelCatalogMarketplaceSettingsRequest** | [**SetChannelCatalogMarketplaceSettingsRequest**](SetChannelCatalogMarketplaceSettingsRequest.md)| Settings to save | |

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
| **204** | Successfully saved channel catalog marketplace settings |  -  |
| **400** | One or more channel catalog marketplace property keys or values are invalid for requested marketplace channel catalog. See response for details. |  -  |
| **404** | Marketplace channel catalog not found |  -  |
| **503** | The marketplace configuration related to this channel catalog is currently in progress. Please retry later. |  * Retry-After - Indicate the duration to before the next retry in second. <br>  |
| **0** | Occurs when something goes wrong |  -  |

