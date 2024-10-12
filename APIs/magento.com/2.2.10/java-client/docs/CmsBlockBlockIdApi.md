# CmsBlockBlockIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cmsBlockRepositoryV1DeleteByIdDelete**](CmsBlockBlockIdApi.md#cmsBlockRepositoryV1DeleteByIdDelete) | **DELETE** /V1/cmsBlock/{blockId} | cmsBlock/{blockId} |
| [**cmsBlockRepositoryV1GetByIdGet**](CmsBlockBlockIdApi.md#cmsBlockRepositoryV1GetByIdGet) | **GET** /V1/cmsBlock/{blockId} | cmsBlock/{blockId} |


<a id="cmsBlockRepositoryV1DeleteByIdDelete"></a>
# **cmsBlockRepositoryV1DeleteByIdDelete**
> Boolean cmsBlockRepositoryV1DeleteByIdDelete(blockId)

cmsBlock/{blockId}

Delete block by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CmsBlockBlockIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CmsBlockBlockIdApi apiInstance = new CmsBlockBlockIdApi(defaultClient);
    Integer blockId = 56; // Integer | 
    try {
      Boolean result = apiInstance.cmsBlockRepositoryV1DeleteByIdDelete(blockId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CmsBlockBlockIdApi#cmsBlockRepositoryV1DeleteByIdDelete");
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
| **blockId** | **Integer**|  | |

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

<a id="cmsBlockRepositoryV1GetByIdGet"></a>
# **cmsBlockRepositoryV1GetByIdGet**
> CmsDataBlockInterface cmsBlockRepositoryV1GetByIdGet(blockId)

cmsBlock/{blockId}

Retrieve block.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CmsBlockBlockIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CmsBlockBlockIdApi apiInstance = new CmsBlockBlockIdApi(defaultClient);
    Integer blockId = 56; // Integer | 
    try {
      CmsDataBlockInterface result = apiInstance.cmsBlockRepositoryV1GetByIdGet(blockId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CmsBlockBlockIdApi#cmsBlockRepositoryV1GetByIdGet");
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
| **blockId** | **Integer**|  | |

### Return type

[**CmsDataBlockInterface**](CmsDataBlockInterface.md)

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

