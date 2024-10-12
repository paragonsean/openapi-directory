# ProductsOptionsOptionIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogProductCustomOptionRepositoryV1SavePut**](ProductsOptionsOptionIdApi.md#catalogProductCustomOptionRepositoryV1SavePut) | **PUT** /V1/products/options/{optionId} | products/options/{optionId} |


<a id="catalogProductCustomOptionRepositoryV1SavePut"></a>
# **catalogProductCustomOptionRepositoryV1SavePut**
> CatalogDataProductCustomOptionInterface catalogProductCustomOptionRepositoryV1SavePut(optionId, catalogProductCustomOptionRepositoryV1SavePostRequest)

products/options/{optionId}

Save Custom Option

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsOptionsOptionIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsOptionsOptionIdApi apiInstance = new ProductsOptionsOptionIdApi(defaultClient);
    String optionId = "optionId_example"; // String | 
    CatalogProductCustomOptionRepositoryV1SavePostRequest catalogProductCustomOptionRepositoryV1SavePostRequest = new CatalogProductCustomOptionRepositoryV1SavePostRequest(); // CatalogProductCustomOptionRepositoryV1SavePostRequest | 
    try {
      CatalogDataProductCustomOptionInterface result = apiInstance.catalogProductCustomOptionRepositoryV1SavePut(optionId, catalogProductCustomOptionRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsOptionsOptionIdApi#catalogProductCustomOptionRepositoryV1SavePut");
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
| **optionId** | **String**|  | |
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

