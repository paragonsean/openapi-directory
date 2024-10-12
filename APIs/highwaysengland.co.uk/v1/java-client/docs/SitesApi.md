# SitesApi

All URIs are relative to *https://webtris.highwaysengland.co.uk/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sitesIndex**](SitesApi.md#sitesIndex) | **GET** /v{version}/sites | Get a list of sites |
| [**vversionSitesSiteIdsGet**](SitesApi.md#vversionSitesSiteIdsGet) | **GET** /v{version}/sites/{site_Ids} | Get selected sites |


<a id="sitesIndex"></a>
# **sitesIndex**
> SiteResponse sitesIndex(version)

Get a list of sites

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://webtris.highwaysengland.co.uk/api");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String version = "version_example"; // String | 
    try {
      SiteResponse result = apiInstance.sitesIndex(version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#sitesIndex");
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

[**SiteResponse**](SiteResponse.md)

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

<a id="vversionSitesSiteIdsGet"></a>
# **vversionSitesSiteIdsGet**
> SiteResponse vversionSitesSiteIdsGet(siteIds, version)

Get selected sites

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SitesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://webtris.highwaysengland.co.uk/api");

    SitesApi apiInstance = new SitesApi(defaultClient);
    String siteIds = "siteIds_example"; // String | site id
    String version = "version_example"; // String | 
    try {
      SiteResponse result = apiInstance.vversionSitesSiteIdsGet(siteIds, version);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SitesApi#vversionSitesSiteIdsGet");
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
| **siteIds** | **String**| site id | |
| **version** | **String**|  | |

### Return type

[**SiteResponse**](SiteResponse.md)

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

