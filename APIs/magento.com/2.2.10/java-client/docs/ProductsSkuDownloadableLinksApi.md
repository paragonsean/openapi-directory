# ProductsSkuDownloadableLinksApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**downloadableLinkRepositoryV1GetListGet**](ProductsSkuDownloadableLinksApi.md#downloadableLinkRepositoryV1GetListGet) | **GET** /V1/products/{sku}/downloadable-links | products/{sku}/downloadable-links |
| [**downloadableLinkRepositoryV1SavePost**](ProductsSkuDownloadableLinksApi.md#downloadableLinkRepositoryV1SavePost) | **POST** /V1/products/{sku}/downloadable-links | products/{sku}/downloadable-links |


<a id="downloadableLinkRepositoryV1GetListGet"></a>
# **downloadableLinkRepositoryV1GetListGet**
> List&lt;DownloadableDataLinkInterface&gt; downloadableLinkRepositoryV1GetListGet(sku)

products/{sku}/downloadable-links

List of links with associated samples

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsSkuDownloadableLinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsSkuDownloadableLinksApi apiInstance = new ProductsSkuDownloadableLinksApi(defaultClient);
    String sku = "sku_example"; // String | 
    try {
      List<DownloadableDataLinkInterface> result = apiInstance.downloadableLinkRepositoryV1GetListGet(sku);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsSkuDownloadableLinksApi#downloadableLinkRepositoryV1GetListGet");
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

### Return type

[**List&lt;DownloadableDataLinkInterface&gt;**](DownloadableDataLinkInterface.md)

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

<a id="downloadableLinkRepositoryV1SavePost"></a>
# **downloadableLinkRepositoryV1SavePost**
> Integer downloadableLinkRepositoryV1SavePost(sku, downloadableLinkRepositoryV1SavePostRequest)

products/{sku}/downloadable-links

Update downloadable link of the given product (link type and its resources cannot be changed)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsSkuDownloadableLinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsSkuDownloadableLinksApi apiInstance = new ProductsSkuDownloadableLinksApi(defaultClient);
    String sku = "sku_example"; // String | 
    DownloadableLinkRepositoryV1SavePostRequest downloadableLinkRepositoryV1SavePostRequest = new DownloadableLinkRepositoryV1SavePostRequest(); // DownloadableLinkRepositoryV1SavePostRequest | 
    try {
      Integer result = apiInstance.downloadableLinkRepositoryV1SavePost(sku, downloadableLinkRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsSkuDownloadableLinksApi#downloadableLinkRepositoryV1SavePost");
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

