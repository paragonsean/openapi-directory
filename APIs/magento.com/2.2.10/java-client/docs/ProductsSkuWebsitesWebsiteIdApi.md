# ProductsSkuWebsitesWebsiteIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogProductWebsiteLinkRepositoryV1DeleteByIdDelete**](ProductsSkuWebsitesWebsiteIdApi.md#catalogProductWebsiteLinkRepositoryV1DeleteByIdDelete) | **DELETE** /V1/products/{sku}/websites/{websiteId} | products/{sku}/websites/{websiteId} |


<a id="catalogProductWebsiteLinkRepositoryV1DeleteByIdDelete"></a>
# **catalogProductWebsiteLinkRepositoryV1DeleteByIdDelete**
> Boolean catalogProductWebsiteLinkRepositoryV1DeleteByIdDelete(sku, websiteId)

products/{sku}/websites/{websiteId}

Remove the website assignment from the product by product sku

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsSkuWebsitesWebsiteIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsSkuWebsitesWebsiteIdApi apiInstance = new ProductsSkuWebsitesWebsiteIdApi(defaultClient);
    String sku = "sku_example"; // String | 
    Integer websiteId = 56; // Integer | 
    try {
      Boolean result = apiInstance.catalogProductWebsiteLinkRepositoryV1DeleteByIdDelete(sku, websiteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsSkuWebsitesWebsiteIdApi#catalogProductWebsiteLinkRepositoryV1DeleteByIdDelete");
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
| **websiteId** | **Integer**|  | |

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
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

