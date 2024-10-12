# ProductsBasePricesInformationApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogBasePriceStorageV1GetPost**](ProductsBasePricesInformationApi.md#catalogBasePriceStorageV1GetPost) | **POST** /V1/products/base-prices-information | products/base-prices-information |


<a id="catalogBasePriceStorageV1GetPost"></a>
# **catalogBasePriceStorageV1GetPost**
> List&lt;CatalogDataBasePriceInterface&gt; catalogBasePriceStorageV1GetPost(catalogBasePriceStorageV1GetPostRequest)

products/base-prices-information

Return product prices. In case of at least one of skus is not found exception will be thrown.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsBasePricesInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsBasePricesInformationApi apiInstance = new ProductsBasePricesInformationApi(defaultClient);
    CatalogBasePriceStorageV1GetPostRequest catalogBasePriceStorageV1GetPostRequest = new CatalogBasePriceStorageV1GetPostRequest(); // CatalogBasePriceStorageV1GetPostRequest | 
    try {
      List<CatalogDataBasePriceInterface> result = apiInstance.catalogBasePriceStorageV1GetPost(catalogBasePriceStorageV1GetPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsBasePricesInformationApi#catalogBasePriceStorageV1GetPost");
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

[**List&lt;CatalogDataBasePriceInterface&gt;**](CatalogDataBasePriceInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

