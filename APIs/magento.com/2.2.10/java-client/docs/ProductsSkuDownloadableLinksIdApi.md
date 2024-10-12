# ProductsSkuDownloadableLinksIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**downloadableLinkRepositoryV1SavePut**](ProductsSkuDownloadableLinksIdApi.md#downloadableLinkRepositoryV1SavePut) | **PUT** /V1/products/{sku}/downloadable-links/{id} | products/{sku}/downloadable-links/{id} |


<a id="downloadableLinkRepositoryV1SavePut"></a>
# **downloadableLinkRepositoryV1SavePut**
> Integer downloadableLinkRepositoryV1SavePut(sku, id, downloadableLinkRepositoryV1SavePostRequest)

products/{sku}/downloadable-links/{id}

Update downloadable link of the given product (link type and its resources cannot be changed)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsSkuDownloadableLinksIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsSkuDownloadableLinksIdApi apiInstance = new ProductsSkuDownloadableLinksIdApi(defaultClient);
    String sku = "sku_example"; // String | 
    String id = "id_example"; // String | 
    DownloadableLinkRepositoryV1SavePostRequest downloadableLinkRepositoryV1SavePostRequest = new DownloadableLinkRepositoryV1SavePostRequest(); // DownloadableLinkRepositoryV1SavePostRequest | 
    try {
      Integer result = apiInstance.downloadableLinkRepositoryV1SavePut(sku, id, downloadableLinkRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsSkuDownloadableLinksIdApi#downloadableLinkRepositoryV1SavePut");
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
| **sku** | **String**|  | |
| **id** | **String**|  | |
| **downloadableLinkRepositoryV1SavePostRequest** | [**DownloadableLinkRepositoryV1SavePostRequest**](DownloadableLinkRepositoryV1SavePostRequest.md)|  | [optional] |

### Return type

**Integer**

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

