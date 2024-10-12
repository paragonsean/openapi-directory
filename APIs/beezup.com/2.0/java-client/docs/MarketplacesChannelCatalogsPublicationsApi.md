# MarketplacesChannelCatalogsPublicationsApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPublications**](MarketplacesChannelCatalogsPublicationsApi.md#getPublications) | **GET** /v2/user/marketplaces/channelcatalogs/publications/{marketplaceTechnicalCode}/{accountId}/history | Fetch the publication history for an account, sorted by descending start date |
| [**publishCatalogToMarketplace**](MarketplacesChannelCatalogsPublicationsApi.md#publishCatalogToMarketplace) | **POST** /v2/user/marketplaces/channelcatalogs/publications/{marketplaceTechnicalCode}/{accountId}/publish | [PREVIEW] Launch a publication of the catalog to the marketplace |


<a id="getPublications"></a>
# **getPublications**
> AccountPublications getPublications(marketplaceTechnicalCode, accountId, publicationTypes, channelCatalogId, count)

Fetch the publication history for an account, sorted by descending start date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesChannelCatalogsPublicationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesChannelCatalogsPublicationsApi apiInstance = new MarketplacesChannelCatalogsPublicationsApi(defaultClient);
    String marketplaceTechnicalCode = "marketplaceTechnicalCode_example"; // String | Marketplace Technical Code to query (required)
    Integer accountId = 56; // Integer | Account Id to query (required)
    List<String> publicationTypes = Arrays.asList(); // List<String> | Publication types by which to filter (optional)
    String channelCatalogId = "channelCatalogId_example"; // String | Channel Catalog Id by which to filter (optional)
    Integer count = 56; // Integer | Amount of entries to fetch (optional, default set to 10)
    try {
      AccountPublications result = apiInstance.getPublications(marketplaceTechnicalCode, accountId, publicationTypes, channelCatalogId, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesChannelCatalogsPublicationsApi#getPublications");
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
| **marketplaceTechnicalCode** | **String**| Marketplace Technical Code to query (required) | |
| **accountId** | **Integer**| Account Id to query (required) | |
| **publicationTypes** | [**List&lt;String&gt;**](String.md)| Publication types by which to filter (optional) | [enum: PublishProducts, PublishOffers, Unpublish, PublishRelationshipsEnum, PublishProductImagesEnum, PublishInventoryEnum, PublishPricingEnum] |
| **channelCatalogId** | **String**| Channel Catalog Id by which to filter (optional) | [optional] |
| **count** | **Integer**| Amount of entries to fetch (optional, default set to 10) | [optional] |

### Return type

[**AccountPublications**](AccountPublications.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully fetched channel catalog settings |  -  |
| **400** | Feature only available for Amazon, Ebay, CDiscount and Mirakl marketplaces |  -  |
| **404** | Requested account, marketplace or authorization for current user not found |  -  |
| **503** | The marketplace configuration related to this channel catalog is currently in progress. Please retry later. |  * Retry-After - Indicate the duration to before the next retry in second. <br>  |
| **0** | Occurs when something goes wrong |  -  |

<a id="publishCatalogToMarketplace"></a>
# **publishCatalogToMarketplace**
> publishCatalogToMarketplace(marketplaceTechnicalCode, accountId, publishCatalogToMarketplaceRequest)

[PREVIEW] Launch a publication of the catalog to the marketplace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarketplacesChannelCatalogsPublicationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    MarketplacesChannelCatalogsPublicationsApi apiInstance = new MarketplacesChannelCatalogsPublicationsApi(defaultClient);
    String marketplaceTechnicalCode = "marketplaceTechnicalCode_example"; // String | Marketplace Technical Code to query (required)
    Integer accountId = 56; // Integer | Account Id to query (required)
    PublishCatalogToMarketplaceRequest publishCatalogToMarketplaceRequest = new PublishCatalogToMarketplaceRequest(); // PublishCatalogToMarketplaceRequest | 
    try {
      apiInstance.publishCatalogToMarketplace(marketplaceTechnicalCode, accountId, publishCatalogToMarketplaceRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarketplacesChannelCatalogsPublicationsApi#publishCatalogToMarketplace");
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
| **marketplaceTechnicalCode** | **String**| Marketplace Technical Code to query (required) | |
| **accountId** | **Integer**| Account Id to query (required) | |
| **publishCatalogToMarketplaceRequest** | [**PublishCatalogToMarketplaceRequest**](PublishCatalogToMarketplaceRequest.md)|  | |

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
| **202** | Publication request accepted |  -  |
| **400** | One or more channel catalog marketplace property keys or values are invalid for requested marketplace channel catalog. See response for details. |  -  |
| **404** | Requested account, marketplace or authorization for current user not found |  -  |
| **503** | The marketplace configuration related to this channel catalog is currently in progress. Please retry later. |  * Retry-After - Indicate the duration to before the next retry in second. <br>  |
| **0** | Occurs when something goes wrong |  -  |

