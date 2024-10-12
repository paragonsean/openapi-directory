# CmsBlockIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cmsBlockRepositoryV1SavePut**](CmsBlockIdApi.md#cmsBlockRepositoryV1SavePut) | **PUT** /V1/cmsBlock/{id} | cmsBlock/{id} |


<a id="cmsBlockRepositoryV1SavePut"></a>
# **cmsBlockRepositoryV1SavePut**
> CmsDataBlockInterface cmsBlockRepositoryV1SavePut(id, cmsBlockRepositoryV1SavePostRequest)

cmsBlock/{id}

Save block.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CmsBlockIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CmsBlockIdApi apiInstance = new CmsBlockIdApi(defaultClient);
    String id = "id_example"; // String | 
    CmsBlockRepositoryV1SavePostRequest cmsBlockRepositoryV1SavePostRequest = new CmsBlockRepositoryV1SavePostRequest(); // CmsBlockRepositoryV1SavePostRequest | 
    try {
      CmsDataBlockInterface result = apiInstance.cmsBlockRepositoryV1SavePut(id, cmsBlockRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CmsBlockIdApi#cmsBlockRepositoryV1SavePut");
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
| **cmsBlockRepositoryV1SavePostRequest** | [**CmsBlockRepositoryV1SavePostRequest**](CmsBlockRepositoryV1SavePostRequest.md)|  | [optional] |

### Return type

[**CmsDataBlockInterface**](CmsDataBlockInterface.md)

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
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

