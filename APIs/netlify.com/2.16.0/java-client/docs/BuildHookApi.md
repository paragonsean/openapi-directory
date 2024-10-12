# BuildHookApi

All URIs are relative to *https://api.netlify.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSiteBuildHook**](BuildHookApi.md#createSiteBuildHook) | **POST** /sites/{site_id}/build_hooks |  |
| [**deleteSiteBuildHook**](BuildHookApi.md#deleteSiteBuildHook) | **DELETE** /sites/{site_id}/build_hooks/{id} |  |
| [**getSiteBuildHook**](BuildHookApi.md#getSiteBuildHook) | **GET** /sites/{site_id}/build_hooks/{id} |  |
| [**listSiteBuildHooks**](BuildHookApi.md#listSiteBuildHooks) | **GET** /sites/{site_id}/build_hooks |  |
| [**updateSiteBuildHook**](BuildHookApi.md#updateSiteBuildHook) | **PUT** /sites/{site_id}/build_hooks/{id} |  |


<a id="createSiteBuildHook"></a>
# **createSiteBuildHook**
> BuildHook createSiteBuildHook(siteId, buildHook)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildHookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    BuildHookApi apiInstance = new BuildHookApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    BuildHookSetup buildHook = new BuildHookSetup(); // BuildHookSetup | 
    try {
      BuildHook result = apiInstance.createSiteBuildHook(siteId, buildHook);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildHookApi#createSiteBuildHook");
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
| **buildHook** | [**BuildHookSetup**](BuildHookSetup.md)|  | |

### Return type

[**BuildHook**](BuildHook.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **0** | error |  -  |

<a id="deleteSiteBuildHook"></a>
# **deleteSiteBuildHook**
> deleteSiteBuildHook(siteId, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildHookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    BuildHookApi apiInstance = new BuildHookApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.deleteSiteBuildHook(siteId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildHookApi#deleteSiteBuildHook");
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
| **id** | **String**|  | |

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
| **204** | No content |  -  |
| **0** | error |  -  |

<a id="getSiteBuildHook"></a>
# **getSiteBuildHook**
> BuildHook getSiteBuildHook(siteId, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildHookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    BuildHookApi apiInstance = new BuildHookApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      BuildHook result = apiInstance.getSiteBuildHook(siteId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildHookApi#getSiteBuildHook");
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
| **id** | **String**|  | |

### Return type

[**BuildHook**](BuildHook.md)

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

<a id="listSiteBuildHooks"></a>
# **listSiteBuildHooks**
> List&lt;BuildHook&gt; listSiteBuildHooks(siteId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildHookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    BuildHookApi apiInstance = new BuildHookApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    try {
      List<BuildHook> result = apiInstance.listSiteBuildHooks(siteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildHookApi#listSiteBuildHooks");
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

[**List&lt;BuildHook&gt;**](BuildHook.md)

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

<a id="updateSiteBuildHook"></a>
# **updateSiteBuildHook**
> updateSiteBuildHook(siteId, id, buildHook)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildHookApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    BuildHookApi apiInstance = new BuildHookApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    String id = "id_example"; // String | 
    BuildHookSetup buildHook = new BuildHookSetup(); // BuildHookSetup | 
    try {
      apiInstance.updateSiteBuildHook(siteId, id, buildHook);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildHookApi#updateSiteBuildHook");
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
| **id** | **String**|  | |
| **buildHook** | [**BuildHookSetup**](BuildHookSetup.md)|  | |

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

