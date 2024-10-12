# ProductsSkuDownloadableLinksSamplesApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**downloadableSampleRepositoryV1GetListGet**](ProductsSkuDownloadableLinksSamplesApi.md#downloadableSampleRepositoryV1GetListGet) | **GET** /V1/products/{sku}/downloadable-links/samples | products/{sku}/downloadable-links/samples |
| [**downloadableSampleRepositoryV1SavePost**](ProductsSkuDownloadableLinksSamplesApi.md#downloadableSampleRepositoryV1SavePost) | **POST** /V1/products/{sku}/downloadable-links/samples | products/{sku}/downloadable-links/samples |


<a id="downloadableSampleRepositoryV1GetListGet"></a>
# **downloadableSampleRepositoryV1GetListGet**
> List&lt;DownloadableDataSampleInterface&gt; downloadableSampleRepositoryV1GetListGet(sku)

products/{sku}/downloadable-links/samples

List of samples for downloadable product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsSkuDownloadableLinksSamplesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsSkuDownloadableLinksSamplesApi apiInstance = new ProductsSkuDownloadableLinksSamplesApi(defaultClient);
    String sku = "sku_example"; // String | 
    try {
      List<DownloadableDataSampleInterface> result = apiInstance.downloadableSampleRepositoryV1GetListGet(sku);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsSkuDownloadableLinksSamplesApi#downloadableSampleRepositoryV1GetListGet");
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

[**List&lt;DownloadableDataSampleInterface&gt;**](DownloadableDataSampleInterface.md)

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

<a id="downloadableSampleRepositoryV1SavePost"></a>
# **downloadableSampleRepositoryV1SavePost**
> Integer downloadableSampleRepositoryV1SavePost(sku, downloadableSampleRepositoryV1SavePostRequest)

products/{sku}/downloadable-links/samples

Update downloadable sample of the given product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsSkuDownloadableLinksSamplesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsSkuDownloadableLinksSamplesApi apiInstance = new ProductsSkuDownloadableLinksSamplesApi(defaultClient);
    String sku = "sku_example"; // String | 
    DownloadableSampleRepositoryV1SavePostRequest downloadableSampleRepositoryV1SavePostRequest = new DownloadableSampleRepositoryV1SavePostRequest(); // DownloadableSampleRepositoryV1SavePostRequest | 
    try {
      Integer result = apiInstance.downloadableSampleRepositoryV1SavePost(sku, downloadableSampleRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsSkuDownloadableLinksSamplesApi#downloadableSampleRepositoryV1SavePost");
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

