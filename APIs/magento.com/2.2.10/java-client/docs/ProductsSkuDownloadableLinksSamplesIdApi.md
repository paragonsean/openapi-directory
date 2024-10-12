# ProductsSkuDownloadableLinksSamplesIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**downloadableSampleRepositoryV1SavePut**](ProductsSkuDownloadableLinksSamplesIdApi.md#downloadableSampleRepositoryV1SavePut) | **PUT** /V1/products/{sku}/downloadable-links/samples/{id} | products/{sku}/downloadable-links/samples/{id} |


<a id="downloadableSampleRepositoryV1SavePut"></a>
# **downloadableSampleRepositoryV1SavePut**
> Integer downloadableSampleRepositoryV1SavePut(sku, id, downloadableSampleRepositoryV1SavePostRequest)

products/{sku}/downloadable-links/samples/{id}

Update downloadable sample of the given product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsSkuDownloadableLinksSamplesIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsSkuDownloadableLinksSamplesIdApi apiInstance = new ProductsSkuDownloadableLinksSamplesIdApi(defaultClient);
    String sku = "sku_example"; // String | 
    String id = "id_example"; // String | 
    DownloadableSampleRepositoryV1SavePostRequest downloadableSampleRepositoryV1SavePostRequest = new DownloadableSampleRepositoryV1SavePostRequest(); // DownloadableSampleRepositoryV1SavePostRequest | 
    try {
      Integer result = apiInstance.downloadableSampleRepositoryV1SavePut(sku, id, downloadableSampleRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsSkuDownloadableLinksSamplesIdApi#downloadableSampleRepositoryV1SavePut");
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
| **downloadableSampleRepositoryV1SavePostRequest** | [**DownloadableSampleRepositoryV1SavePostRequest**](DownloadableSampleRepositoryV1SavePostRequest.md)|  | [optional] |

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

