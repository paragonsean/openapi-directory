# ProductsCostInformationApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogCostStorageV1GetPost**](ProductsCostInformationApi.md#catalogCostStorageV1GetPost) | **POST** /V1/products/cost-information | products/cost-information |


<a id="catalogCostStorageV1GetPost"></a>
# **catalogCostStorageV1GetPost**
> List&lt;CatalogDataCostInterface&gt; catalogCostStorageV1GetPost(catalogBasePriceStorageV1GetPostRequest)

products/cost-information

Return product prices. In case of at least one of skus is not found exception will be thrown.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsCostInformationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsCostInformationApi apiInstance = new ProductsCostInformationApi(defaultClient);
    CatalogBasePriceStorageV1GetPostRequest catalogBasePriceStorageV1GetPostRequest = new CatalogBasePriceStorageV1GetPostRequest(); // CatalogBasePriceStorageV1GetPostRequest | 
    try {
      List<CatalogDataCostInterface> result = apiInstance.catalogCostStorageV1GetPost(catalogBasePriceStorageV1GetPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsCostInformationApi#catalogCostStorageV1GetPost");
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

[**List&lt;CatalogDataCostInterface&gt;**](CatalogDataCostInterface.md)

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

