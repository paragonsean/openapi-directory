# SharedCatalogSharedCatalogIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sharedCatalogSharedCatalogRepositoryV1DeleteByIdDelete**](SharedCatalogSharedCatalogIdApi.md#sharedCatalogSharedCatalogRepositoryV1DeleteByIdDelete) | **DELETE** /V1/sharedCatalog/{sharedCatalogId} | sharedCatalog/{sharedCatalogId} |
| [**sharedCatalogSharedCatalogRepositoryV1GetGet**](SharedCatalogSharedCatalogIdApi.md#sharedCatalogSharedCatalogRepositoryV1GetGet) | **GET** /V1/sharedCatalog/{sharedCatalogId} | sharedCatalog/{sharedCatalogId} |


<a id="sharedCatalogSharedCatalogRepositoryV1DeleteByIdDelete"></a>
# **sharedCatalogSharedCatalogRepositoryV1DeleteByIdDelete**
> Boolean sharedCatalogSharedCatalogRepositoryV1DeleteByIdDelete(sharedCatalogId)

sharedCatalog/{sharedCatalogId}

Delete a shared catalog by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedCatalogSharedCatalogIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    SharedCatalogSharedCatalogIdApi apiInstance = new SharedCatalogSharedCatalogIdApi(defaultClient);
    Integer sharedCatalogId = 56; // Integer | 
    try {
      Boolean result = apiInstance.sharedCatalogSharedCatalogRepositoryV1DeleteByIdDelete(sharedCatalogId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedCatalogSharedCatalogIdApi#sharedCatalogSharedCatalogRepositoryV1DeleteByIdDelete");
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
| **sharedCatalogId** | **Integer**|  | |

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

<a id="sharedCatalogSharedCatalogRepositoryV1GetGet"></a>
# **sharedCatalogSharedCatalogRepositoryV1GetGet**
> SharedCatalogDataSharedCatalogInterface sharedCatalogSharedCatalogRepositoryV1GetGet(sharedCatalogId)

sharedCatalog/{sharedCatalogId}

Return the following properties for the selected shared catalog: ID, Store Group ID, Name, Type, Description, Customer Group, Tax Class.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedCatalogSharedCatalogIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    SharedCatalogSharedCatalogIdApi apiInstance = new SharedCatalogSharedCatalogIdApi(defaultClient);
    Integer sharedCatalogId = 56; // Integer | 
    try {
      SharedCatalogDataSharedCatalogInterface result = apiInstance.sharedCatalogSharedCatalogRepositoryV1GetGet(sharedCatalogId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedCatalogSharedCatalogIdApi#sharedCatalogSharedCatalogRepositoryV1GetGet");
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
| **sharedCatalogId** | **Integer**|  | |

### Return type

[**SharedCatalogDataSharedCatalogInterface**](SharedCatalogDataSharedCatalogInterface.md)

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
| **0** | Unexpected error |  -  |

