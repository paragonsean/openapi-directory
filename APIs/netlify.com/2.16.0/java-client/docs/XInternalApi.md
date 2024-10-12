# XInternalApi

All URIs are relative to *https://api.netlify.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createPluginRun**](XInternalApi.md#createPluginRun) | **POST** /deploys/{deploy_id}/plugin_runs |  |
| [**getLatestPluginRuns**](XInternalApi.md#getLatestPluginRuns) | **GET** /sites/{site_id}/plugin_runs/latest |  |
| [**updatePlugin**](XInternalApi.md#updatePlugin) | **PUT** /sites/{site_id}/plugins/{package} |  |


<a id="createPluginRun"></a>
# **createPluginRun**
> PluginRun createPluginRun(deployId, pluginRun)



This is an internal-only endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.XInternalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    XInternalApi apiInstance = new XInternalApi(defaultClient);
    String deployId = "deployId_example"; // String | 
    PluginRunData pluginRun = new PluginRunData(); // PluginRunData | 
    try {
      PluginRun result = apiInstance.createPluginRun(deployId, pluginRun);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling XInternalApi#createPluginRun");
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
| **deployId** | **String**|  | |
| **pluginRun** | [**PluginRunData**](PluginRunData.md)|  | [optional] |

### Return type

[**PluginRun**](PluginRun.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | CREATED |  -  |
| **0** | error |  -  |

<a id="getLatestPluginRuns"></a>
# **getLatestPluginRuns**
> List&lt;PluginRun&gt; getLatestPluginRuns(siteId, packages, state)



This is an internal-only endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.XInternalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    XInternalApi apiInstance = new XInternalApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    List<String> packages = Arrays.asList(); // List<String> | 
    String state = "state_example"; // String | 
    try {
      List<PluginRun> result = apiInstance.getLatestPluginRuns(siteId, packages, state);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling XInternalApi#getLatestPluginRuns");
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
| **packages** | [**List&lt;String&gt;**](String.md)|  | |
| **state** | **String**|  | [optional] |

### Return type

[**List&lt;PluginRun&gt;**](PluginRun.md)

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

<a id="updatePlugin"></a>
# **updatePlugin**
> Plugin updatePlugin(siteId, _package, pluginParams)



This is an internal-only endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.XInternalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    XInternalApi apiInstance = new XInternalApi(defaultClient);
    String siteId = "siteId_example"; // String | 
    String _package = "_package_example"; // String | 
    PluginParams pluginParams = new PluginParams(); // PluginParams | 
    try {
      Plugin result = apiInstance.updatePlugin(siteId, _package, pluginParams);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling XInternalApi#updatePlugin");
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
| **_package** | **String**|  | |
| **pluginParams** | [**PluginParams**](PluginParams.md)|  | [optional] |

### Return type

[**Plugin**](Plugin.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | error |  -  |

