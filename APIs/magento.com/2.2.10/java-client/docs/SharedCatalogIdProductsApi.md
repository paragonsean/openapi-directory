# SharedCatalogIdProductsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sharedCatalogProductManagementV1GetProductsGet**](SharedCatalogIdProductsApi.md#sharedCatalogProductManagementV1GetProductsGet) | **GET** /V1/sharedCatalog/{id}/products | sharedCatalog/{id}/products |


<a id="sharedCatalogProductManagementV1GetProductsGet"></a>
# **sharedCatalogProductManagementV1GetProductsGet**
> List&lt;String&gt; sharedCatalogProductManagementV1GetProductsGet(id)

sharedCatalog/{id}/products

Return the list of product SKUs in the selected shared catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedCatalogIdProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    SharedCatalogIdProductsApi apiInstance = new SharedCatalogIdProductsApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      List<String> result = apiInstance.sharedCatalogProductManagementV1GetProductsGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedCatalogIdProductsApi#sharedCatalogProductManagementV1GetProductsGet");
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

**List&lt;String&gt;**

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

