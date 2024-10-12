# CmsPageApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cmsPageRepositoryV1SavePost**](CmsPageApi.md#cmsPageRepositoryV1SavePost) | **POST** /V1/cmsPage | cmsPage |


<a id="cmsPageRepositoryV1SavePost"></a>
# **cmsPageRepositoryV1SavePost**
> CmsDataPageInterface cmsPageRepositoryV1SavePost(cmsPageRepositoryV1SavePostRequest)

cmsPage

Save page.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CmsPageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CmsPageApi apiInstance = new CmsPageApi(defaultClient);
    CmsPageRepositoryV1SavePostRequest cmsPageRepositoryV1SavePostRequest = new CmsPageRepositoryV1SavePostRequest(); // CmsPageRepositoryV1SavePostRequest | 
    try {
      CmsDataPageInterface result = apiInstance.cmsPageRepositoryV1SavePost(cmsPageRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CmsPageApi#cmsPageRepositoryV1SavePost");
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
| **cmsPageRepositoryV1SavePostRequest** | [**CmsPageRepositoryV1SavePostRequest**](CmsPageRepositoryV1SavePostRequest.md)|  | [optional] |

### Return type

[**CmsDataPageInterface**](CmsDataPageInterface.md)

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

