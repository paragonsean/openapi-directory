# AssetApi

All URIs are relative to *https://api.netlify.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSiteAsset**](AssetApi.md#createSiteAsset) | **POST** /sites/{site_id}/assets |  |
| [**deleteSiteAsset**](AssetApi.md#deleteSiteAsset) | **DELETE** /sites/{site_id}/assets/{asset_id} |  |
| [**getSiteAssetInfo**](AssetApi.md#getSiteAssetInfo) | **GET** /sites/{site_id}/assets/{asset_id} |  |
| [**listSiteAssets**](AssetApi.md#listSiteAssets) | **GET** /sites/{site_id}/assets |  |
| [**updateSiteAsset**](AssetApi.md#updateSiteAsset) | **PUT** /sites/{site_id}/assets/{asset_id} |  |


<a id="createSiteAsset"></a>
# **createSiteAsset**
> AssetSignature createSiteAsset(siteId, name, size, contentType, visibility)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    AssetApi apiInstance = new AssetApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    String name = "name_example"; // String | 
    Long size = 56L; // Long | 
    String contentType = "contentType_example"; // String | 
    String visibility = "visibility_example"; // String | 
    try {
      AssetSignature result = apiInstance.createSiteAsset(siteId, name, size, contentType, visibility);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetApi#createSiteAsset");
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
| **name** | **String**|  | |
| **size** | **Long**|  | |
| **contentType** | **String**|  | |
| **visibility** | **String**|  | [optional] |

### Return type

[**AssetSignature**](AssetSignature.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **0** | error |  -  |

<a id="deleteSiteAsset"></a>
# **deleteSiteAsset**
> deleteSiteAsset(siteId, assetId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    AssetApi apiInstance = new AssetApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    String assetId = "assetId_example"; // String | 
    try {
      apiInstance.deleteSiteAsset(siteId, assetId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetApi#deleteSiteAsset");
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
| **assetId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Deleted |  -  |
| **0** | error |  -  |

<a id="getSiteAssetInfo"></a>
# **getSiteAssetInfo**
> Asset getSiteAssetInfo(siteId, assetId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    AssetApi apiInstance = new AssetApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    String assetId = "assetId_example"; // String | 
    try {
      Asset result = apiInstance.getSiteAssetInfo(siteId, assetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetApi#getSiteAssetInfo");
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
| **assetId** | **String**|  | |

### Return type

[**Asset**](Asset.md)

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

<a id="listSiteAssets"></a>
# **listSiteAssets**
> List&lt;Asset&gt; listSiteAssets(siteId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    AssetApi apiInstance = new AssetApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    try {
      List<Asset> result = apiInstance.listSiteAssets(siteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetApi#listSiteAssets");
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

[**List&lt;Asset&gt;**](Asset.md)

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

<a id="updateSiteAsset"></a>
# **updateSiteAsset**
> Asset updateSiteAsset(siteId, assetId, state)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AssetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    AssetApi apiInstance = new AssetApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    String assetId = "assetId_example"; // String | 
    String state = "state_example"; // String | 
    try {
      Asset result = apiInstance.updateSiteAsset(siteId, assetId, state);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AssetApi#updateSiteAsset");
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
| **assetId** | **String**|  | |
| **state** | **String**|  | |

### Return type

[**Asset**](Asset.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated |  -  |
| **0** | error |  -  |

