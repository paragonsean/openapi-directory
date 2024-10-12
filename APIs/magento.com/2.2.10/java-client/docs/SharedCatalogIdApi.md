# SharedCatalogIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sharedCatalogSharedCatalogRepositoryV1SavePut**](SharedCatalogIdApi.md#sharedCatalogSharedCatalogRepositoryV1SavePut) | **PUT** /V1/sharedCatalog/{id} | sharedCatalog/{id} |


<a id="sharedCatalogSharedCatalogRepositoryV1SavePut"></a>
# **sharedCatalogSharedCatalogRepositoryV1SavePut**
> Integer sharedCatalogSharedCatalogRepositoryV1SavePut(id, sharedCatalogSharedCatalogRepositoryV1SavePostRequest)

sharedCatalog/{id}

Create or update Shared Catalog service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedCatalogIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    SharedCatalogIdApi apiInstance = new SharedCatalogIdApi(defaultClient);
    String id = "id_example"; // String | 
    SharedCatalogSharedCatalogRepositoryV1SavePostRequest sharedCatalogSharedCatalogRepositoryV1SavePostRequest = new SharedCatalogSharedCatalogRepositoryV1SavePostRequest(); // SharedCatalogSharedCatalogRepositoryV1SavePostRequest | 
    try {
      Integer result = apiInstance.sharedCatalogSharedCatalogRepositoryV1SavePut(id, sharedCatalogSharedCatalogRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedCatalogIdApi#sharedCatalogSharedCatalogRepositoryV1SavePut");
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
| **id** | **String**|  | |
| **sharedCatalogSharedCatalogRepositoryV1SavePostRequest** | [**SharedCatalogSharedCatalogRepositoryV1SavePostRequest**](SharedCatalogSharedCatalogRepositoryV1SavePostRequest.md)|  | [optional] |

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
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

