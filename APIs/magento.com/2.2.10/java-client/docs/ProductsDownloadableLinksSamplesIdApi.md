# ProductsDownloadableLinksSamplesIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**downloadableSampleRepositoryV1DeleteDelete**](ProductsDownloadableLinksSamplesIdApi.md#downloadableSampleRepositoryV1DeleteDelete) | **DELETE** /V1/products/downloadable-links/samples/{id} | products/downloadable-links/samples/{id} |


<a id="downloadableSampleRepositoryV1DeleteDelete"></a>
# **downloadableSampleRepositoryV1DeleteDelete**
> Boolean downloadableSampleRepositoryV1DeleteDelete(id)

products/downloadable-links/samples/{id}

Delete downloadable sample

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsDownloadableLinksSamplesIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsDownloadableLinksSamplesIdApi apiInstance = new ProductsDownloadableLinksSamplesIdApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      Boolean result = apiInstance.downloadableSampleRepositoryV1DeleteDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsDownloadableLinksSamplesIdApi#downloadableSampleRepositoryV1DeleteDelete");
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

