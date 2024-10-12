# CmsPagePageIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cmsPageRepositoryV1DeleteByIdDelete**](CmsPagePageIdApi.md#cmsPageRepositoryV1DeleteByIdDelete) | **DELETE** /V1/cmsPage/{pageId} | cmsPage/{pageId} |
| [**cmsPageRepositoryV1GetByIdGet**](CmsPagePageIdApi.md#cmsPageRepositoryV1GetByIdGet) | **GET** /V1/cmsPage/{pageId} | cmsPage/{pageId} |


<a id="cmsPageRepositoryV1DeleteByIdDelete"></a>
# **cmsPageRepositoryV1DeleteByIdDelete**
> Boolean cmsPageRepositoryV1DeleteByIdDelete(pageId)

cmsPage/{pageId}

Delete page by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CmsPagePageIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CmsPagePageIdApi apiInstance = new CmsPagePageIdApi(defaultClient);
    Integer pageId = 56; // Integer | 
    try {
      Boolean result = apiInstance.cmsPageRepositoryV1DeleteByIdDelete(pageId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CmsPagePageIdApi#cmsPageRepositoryV1DeleteByIdDelete");
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
| **pageId** | **Integer**|  | |

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
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

<a id="cmsPageRepositoryV1GetByIdGet"></a>
# **cmsPageRepositoryV1GetByIdGet**
> CmsDataPageInterface cmsPageRepositoryV1GetByIdGet(pageId)

cmsPage/{pageId}

Retrieve page.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CmsPagePageIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CmsPagePageIdApi apiInstance = new CmsPagePageIdApi(defaultClient);
    Integer pageId = 56; // Integer | 
    try {
      CmsDataPageInterface result = apiInstance.cmsPageRepositoryV1GetByIdGet(pageId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CmsPagePageIdApi#cmsPageRepositoryV1GetByIdGet");
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
| **pageId** | **Integer**|  | |

### Return type

[**CmsDataPageInterface**](CmsDataPageInterface.md)

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
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

