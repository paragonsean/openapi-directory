# ProductsCostDeleteApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogCostStorageV1DeletePost**](ProductsCostDeleteApi.md#catalogCostStorageV1DeletePost) | **POST** /V1/products/cost-delete | products/cost-delete |


<a id="catalogCostStorageV1DeletePost"></a>
# **catalogCostStorageV1DeletePost**
> Boolean catalogCostStorageV1DeletePost(catalogBasePriceStorageV1GetPostRequest)

products/cost-delete

Delete product cost. In case of at least one of skus is not found exception will be thrown. If error occurred during the delete exception will be thrown.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsCostDeleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsCostDeleteApi apiInstance = new ProductsCostDeleteApi(defaultClient);
    CatalogBasePriceStorageV1GetPostRequest catalogBasePriceStorageV1GetPostRequest = new CatalogBasePriceStorageV1GetPostRequest(); // CatalogBasePriceStorageV1GetPostRequest | 
    try {
      Boolean result = apiInstance.catalogCostStorageV1DeletePost(catalogBasePriceStorageV1GetPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsCostDeleteApi#catalogCostStorageV1DeletePost");
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

**Boolean**

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

