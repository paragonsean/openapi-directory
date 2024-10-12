# CmsPageIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cmsPageRepositoryV1SavePut**](CmsPageIdApi.md#cmsPageRepositoryV1SavePut) | **PUT** /V1/cmsPage/{id} | cmsPage/{id} |


<a id="cmsPageRepositoryV1SavePut"></a>
# **cmsPageRepositoryV1SavePut**
> CmsDataPageInterface cmsPageRepositoryV1SavePut(id, cmsPageRepositoryV1SavePostRequest)

cmsPage/{id}

Save page.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CmsPageIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CmsPageIdApi apiInstance = new CmsPageIdApi(defaultClient);
    String id = "id_example"; // String | 
    CmsPageRepositoryV1SavePostRequest cmsPageRepositoryV1SavePostRequest = new CmsPageRepositoryV1SavePostRequest(); // CmsPageRepositoryV1SavePostRequest | 
    try {
      CmsDataPageInterface result = apiInstance.cmsPageRepositoryV1SavePut(id, cmsPageRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CmsPageIdApi#cmsPageRepositoryV1SavePut");
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

