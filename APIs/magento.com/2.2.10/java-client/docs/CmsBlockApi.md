# CmsBlockApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cmsBlockRepositoryV1SavePost**](CmsBlockApi.md#cmsBlockRepositoryV1SavePost) | **POST** /V1/cmsBlock | cmsBlock |


<a id="cmsBlockRepositoryV1SavePost"></a>
# **cmsBlockRepositoryV1SavePost**
> CmsDataBlockInterface cmsBlockRepositoryV1SavePost(cmsBlockRepositoryV1SavePostRequest)

cmsBlock

Save block.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CmsBlockApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CmsBlockApi apiInstance = new CmsBlockApi(defaultClient);
    CmsBlockRepositoryV1SavePostRequest cmsBlockRepositoryV1SavePostRequest = new CmsBlockRepositoryV1SavePostRequest(); // CmsBlockRepositoryV1SavePostRequest | 
    try {
      CmsDataBlockInterface result = apiInstance.cmsBlockRepositoryV1SavePost(cmsBlockRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CmsBlockApi#cmsBlockRepositoryV1SavePost");
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

