# MetadataApi

All URIs are relative to *https://api.netlify.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSiteMetadata**](MetadataApi.md#getSiteMetadata) | **GET** /sites/{site_id}/metadata |  |
| [**updateSiteMetadata**](MetadataApi.md#updateSiteMetadata) | **PUT** /sites/{site_id}/metadata |  |


<a id="getSiteMetadata"></a>
# **getSiteMetadata**
> Object getSiteMetadata(siteId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    MetadataApi apiInstance = new MetadataApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    try {
      Object result = apiInstance.getSiteMetadata(siteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataApi#getSiteMetadata");
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
| **siteId** | **String**|  | |

### Return type

**Object**

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | error |  -  |

<a id="updateSiteMetadata"></a>
# **updateSiteMetadata**
> updateSiteMetadata(siteId, metadata)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetadataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    MetadataApi apiInstance = new MetadataApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    Object metadata = null; // Object | 
    try {
      apiInstance.updateSiteMetadata(siteId, metadata);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetadataApi#updateSiteMetadata");
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
| **siteId** | **String**|  | |
| **metadata** | **Object**|  | |

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No content |  -  |
| **0** | error |  -  |

