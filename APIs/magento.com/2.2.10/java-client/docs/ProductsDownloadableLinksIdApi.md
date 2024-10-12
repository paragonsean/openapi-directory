# ProductsDownloadableLinksIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**downloadableLinkRepositoryV1DeleteDelete**](ProductsDownloadableLinksIdApi.md#downloadableLinkRepositoryV1DeleteDelete) | **DELETE** /V1/products/downloadable-links/{id} | products/downloadable-links/{id} |


<a id="downloadableLinkRepositoryV1DeleteDelete"></a>
# **downloadableLinkRepositoryV1DeleteDelete**
> Boolean downloadableLinkRepositoryV1DeleteDelete(id)

products/downloadable-links/{id}

Delete downloadable link

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsDownloadableLinksIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsDownloadableLinksIdApi apiInstance = new ProductsDownloadableLinksIdApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      Boolean result = apiInstance.downloadableLinkRepositoryV1DeleteDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsDownloadableLinksIdApi#downloadableLinkRepositoryV1DeleteDelete");
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
| **id** | **Integer**|  | |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

