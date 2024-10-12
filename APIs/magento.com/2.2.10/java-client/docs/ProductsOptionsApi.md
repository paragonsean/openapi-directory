# ProductsOptionsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogProductCustomOptionRepositoryV1SavePost**](ProductsOptionsApi.md#catalogProductCustomOptionRepositoryV1SavePost) | **POST** /V1/products/options | products/options |


<a id="catalogProductCustomOptionRepositoryV1SavePost"></a>
# **catalogProductCustomOptionRepositoryV1SavePost**
> CatalogDataProductCustomOptionInterface catalogProductCustomOptionRepositoryV1SavePost(catalogProductCustomOptionRepositoryV1SavePostRequest)

products/options

Save Custom Option

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsOptionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsOptionsApi apiInstance = new ProductsOptionsApi(defaultClient);
    CatalogProductCustomOptionRepositoryV1SavePostRequest catalogProductCustomOptionRepositoryV1SavePostRequest = new CatalogProductCustomOptionRepositoryV1SavePostRequest(); // CatalogProductCustomOptionRepositoryV1SavePostRequest | 
    try {
      CatalogDataProductCustomOptionInterface result = apiInstance.catalogProductCustomOptionRepositoryV1SavePost(catalogProductCustomOptionRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsOptionsApi#catalogProductCustomOptionRepositoryV1SavePost");
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
| **catalogProductCustomOptionRepositoryV1SavePostRequest** | [**CatalogProductCustomOptionRepositoryV1SavePostRequest**](CatalogProductCustomOptionRepositoryV1SavePostRequest.md)|  | [optional] |

### Return type

[**CatalogDataProductCustomOptionInterface**](CatalogDataProductCustomOptionInterface.md)

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

