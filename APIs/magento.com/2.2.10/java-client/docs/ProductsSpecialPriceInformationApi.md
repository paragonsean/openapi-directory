# ProductsSpecialPriceInformationApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogSpecialPriceStorageV1GetPost**](ProductsSpecialPriceInformationApi.md#catalogSpecialPriceStorageV1GetPost) | **POST** /V1/products/special-price-information | products/special-price-information |


<a id="catalogSpecialPriceStorageV1GetPost"></a>
# **catalogSpecialPriceStorageV1GetPost**
> List&lt;CatalogDataSpecialPriceInterface&gt; catalogSpecialPriceStorageV1GetPost(catalogBasePriceStorageV1GetPostRequest)

products/special-price-information

Return product&#39;s special price. In case of at least one of skus is not found exception will be thrown.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsSpecialPriceInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsSpecialPriceInformationApi apiInstance = new ProductsSpecialPriceInformationApi(defaultClient);
    CatalogBasePriceStorageV1GetPostRequest catalogBasePriceStorageV1GetPostRequest = new CatalogBasePriceStorageV1GetPostRequest(); // CatalogBasePriceStorageV1GetPostRequest | 
    try {
      List<CatalogDataSpecialPriceInterface> result = apiInstance.catalogSpecialPriceStorageV1GetPost(catalogBasePriceStorageV1GetPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsSpecialPriceInformationApi#catalogSpecialPriceStorageV1GetPost");
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

[**List&lt;CatalogDataSpecialPriceInterface&gt;**](CatalogDataSpecialPriceInterface.md)

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

