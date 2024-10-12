# ProductsTierPricesInformationApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogTierPriceStorageV1GetPost**](ProductsTierPricesInformationApi.md#catalogTierPriceStorageV1GetPost) | **POST** /V1/products/tier-prices-information | products/tier-prices-information |


<a id="catalogTierPriceStorageV1GetPost"></a>
# **catalogTierPriceStorageV1GetPost**
> List&lt;CatalogDataTierPriceInterface&gt; catalogTierPriceStorageV1GetPost(catalogBasePriceStorageV1GetPostRequest)

products/tier-prices-information

Return product prices. In case of at least one of skus is not found exception will be thrown.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsTierPricesInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsTierPricesInformationApi apiInstance = new ProductsTierPricesInformationApi(defaultClient);
    CatalogBasePriceStorageV1GetPostRequest catalogBasePriceStorageV1GetPostRequest = new CatalogBasePriceStorageV1GetPostRequest(); // CatalogBasePriceStorageV1GetPostRequest | 
    try {
      List<CatalogDataTierPriceInterface> result = apiInstance.catalogTierPriceStorageV1GetPost(catalogBasePriceStorageV1GetPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsTierPricesInformationApi#catalogTierPriceStorageV1GetPost");
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
| **catalogBasePriceStorageV1GetPostRequest** | [**CatalogBasePriceStorageV1GetPostRequest**](CatalogBasePriceStorageV1GetPostRequest.md)|  | [optional] |

### Return type

[**List&lt;CatalogDataTierPriceInterface&gt;**](CatalogDataTierPriceInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

