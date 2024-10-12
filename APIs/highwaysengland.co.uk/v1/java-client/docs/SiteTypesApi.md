# SiteTypesApi

All URIs are relative to *https://webtris.highwaysengland.co.uk/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**siteTypesGetSitesForPublicFacingAPI**](SiteTypesApi.md#siteTypesGetSitesForPublicFacingAPI) | **GET** /v{version}/sitetypes/{siteType_Id}/sites | Returns the layer metadata for the LayerId specified. |
| [**siteTypesIndex**](SiteTypesApi.md#siteTypesIndex) | **GET** /v{version}/sitetypes | Return list of site types |


<a id="siteTypesGetSitesForPublicFacingAPI"></a>
# **siteTypesGetSitesForPublicFacingAPI**
> SiteTypeLayer siteTypesGetSitesForPublicFacingAPI(siteTypeId, version)

Returns the layer metadata for the LayerId specified.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SiteTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://webtris.highwaysengland.co.uk/api");

    SiteTypesApi apiInstance = new SiteTypesApi(defaultClient);
    Integer siteTypeId = 56; // Integer | 1 = MIDAS, 2 = TAME, 3 = TMU, 4 = TRADS Legacy
    String version = "version_example"; // String | 
    try {
      SiteTypeLayer result = apiInstance.siteTypesGetSitesForPublicFacingAPI(siteTypeId, version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SiteTypesApi#siteTypesGetSitesForPublicFacingAPI");
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
| **siteTypeId** | **Integer**| 1 &#x3D; MIDAS, 2 &#x3D; TAME, 3 &#x3D; TMU, 4 &#x3D; TRADS Legacy | |
| **version** | **String**|  | |

### Return type

[**SiteTypeLayer**](SiteTypeLayer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Bad request |  -  |
| **404** | Layer not found |  -  |
| **500** | Internal Server Error |  -  |

<a id="siteTypesIndex"></a>
# **siteTypesIndex**
> SiteTypeResponse siteTypesIndex(version)

Return list of site types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SiteTypesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://webtris.highwaysengland.co.uk/api");

    SiteTypesApi apiInstance = new SiteTypesApi(defaultClient);
    String version = "version_example"; // String | 
    try {
      SiteTypeResponse result = apiInstance.siteTypesIndex(version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SiteTypesApi#siteTypesIndex");
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
| **version** | **String**|  | |

### Return type

[**SiteTypeResponse**](SiteTypeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Bad request |  -  |
| **500** | Internal Server Error |  -  |

