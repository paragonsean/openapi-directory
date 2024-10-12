# PluginsApi

All URIs are relative to *https://peertube2.cpy.re*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addPlugin**](PluginsApi.md#addPlugin) | **POST** /api/v1/plugins/install | Install a plugin |
| [**apiV1PluginsNpmNamePublicSettingsGet**](PluginsApi.md#apiV1PluginsNpmNamePublicSettingsGet) | **GET** /api/v1/plugins/{npmName}/public-settings | Get a plugin&#39;s public settings |
| [**apiV1PluginsNpmNameRegisteredSettingsGet**](PluginsApi.md#apiV1PluginsNpmNameRegisteredSettingsGet) | **GET** /api/v1/plugins/{npmName}/registered-settings | Get a plugin&#39;s registered settings |
| [**apiV1PluginsNpmNameSettingsPut**](PluginsApi.md#apiV1PluginsNpmNameSettingsPut) | **PUT** /api/v1/plugins/{npmName}/settings | Set a plugin&#39;s settings |
| [**getAvailablePlugins**](PluginsApi.md#getAvailablePlugins) | **GET** /api/v1/plugins/available | List available plugins |
| [**getPlugin**](PluginsApi.md#getPlugin) | **GET** /api/v1/plugins/{npmName} | Get a plugin |
| [**getPlugins**](PluginsApi.md#getPlugins) | **GET** /api/v1/plugins | List plugins |
| [**uninstallPlugin**](PluginsApi.md#uninstallPlugin) | **POST** /api/v1/plugins/uninstall | Uninstall a plugin |
| [**updatePlugin**](PluginsApi.md#updatePlugin) | **POST** /api/v1/plugins/update | Update a plugin |


<a id="addPlugin"></a>
# **addPlugin**
> addPlugin(addPluginRequest)

Install a plugin

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PluginsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PluginsApi apiInstance = new PluginsApi(defaultClient);
    AddPluginRequest addPluginRequest = new AddPluginRequest(); // AddPluginRequest | 
    try {
      apiInstance.addPlugin(addPluginRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling PluginsApi#addPlugin");
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
| **addPluginRequest** | [**AddPluginRequest**](AddPluginRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |
| **400** | should have either &#x60;npmName&#x60; or &#x60;path&#x60; set |  -  |

<a id="apiV1PluginsNpmNamePublicSettingsGet"></a>
# **apiV1PluginsNpmNamePublicSettingsGet**
> Map&lt;String, Object&gt; apiV1PluginsNpmNamePublicSettingsGet(npmName)

Get a plugin&#39;s public settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PluginsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");

    PluginsApi apiInstance = new PluginsApi(defaultClient);
    String npmName = "peertube-plugin-auth-ldap"; // String | name of the plugin/theme on npmjs.com or in its package.json
    try {
      Map<String, Object> result = apiInstance.apiV1PluginsNpmNamePublicSettingsGet(npmName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PluginsApi#apiV1PluginsNpmNamePublicSettingsGet");
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
| **npmName** | **String**| name of the plugin/theme on npmjs.com or in its package.json | |

### Return type

**Map&lt;String, Object&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **404** | plugin not found |  -  |

<a id="apiV1PluginsNpmNameRegisteredSettingsGet"></a>
# **apiV1PluginsNpmNameRegisteredSettingsGet**
> Map&lt;String, Object&gt; apiV1PluginsNpmNameRegisteredSettingsGet(npmName)

Get a plugin&#39;s registered settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PluginsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PluginsApi apiInstance = new PluginsApi(defaultClient);
    String npmName = "peertube-plugin-auth-ldap"; // String | name of the plugin/theme on npmjs.com or in its package.json
    try {
      Map<String, Object> result = apiInstance.apiV1PluginsNpmNameRegisteredSettingsGet(npmName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PluginsApi#apiV1PluginsNpmNameRegisteredSettingsGet");
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
| **npmName** | **String**| name of the plugin/theme on npmjs.com or in its package.json | |

### Return type

**Map&lt;String, Object&gt;**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **404** | plugin not found |  -  |

<a id="apiV1PluginsNpmNameSettingsPut"></a>
# **apiV1PluginsNpmNameSettingsPut**
> apiV1PluginsNpmNameSettingsPut(npmName, apiV1PluginsNpmNameSettingsPutRequest)

Set a plugin&#39;s settings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PluginsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PluginsApi apiInstance = new PluginsApi(defaultClient);
    String npmName = "peertube-plugin-auth-ldap"; // String | name of the plugin/theme on npmjs.com or in its package.json
    ApiV1PluginsNpmNameSettingsPutRequest apiV1PluginsNpmNameSettingsPutRequest = new ApiV1PluginsNpmNameSettingsPutRequest(); // ApiV1PluginsNpmNameSettingsPutRequest | 
    try {
      apiInstance.apiV1PluginsNpmNameSettingsPut(npmName, apiV1PluginsNpmNameSettingsPutRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling PluginsApi#apiV1PluginsNpmNameSettingsPut");
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
| **npmName** | **String**| name of the plugin/theme on npmjs.com or in its package.json | |
| **apiV1PluginsNpmNameSettingsPutRequest** | [**ApiV1PluginsNpmNameSettingsPutRequest**](ApiV1PluginsNpmNameSettingsPutRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |
| **404** | plugin not found |  -  |

<a id="getAvailablePlugins"></a>
# **getAvailablePlugins**
> PluginResponse getAvailablePlugins(search, pluginType, currentPeerTubeEngine, start, count, sort)

List available plugins

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PluginsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PluginsApi apiInstance = new PluginsApi(defaultClient);
    String search = "search_example"; // String | 
    Integer pluginType = 56; // Integer | 
    String currentPeerTubeEngine = "currentPeerTubeEngine_example"; // String | 
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String sort = "-createdAt"; // String | Sort column
    try {
      PluginResponse result = apiInstance.getAvailablePlugins(search, pluginType, currentPeerTubeEngine, start, count, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PluginsApi#getAvailablePlugins");
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
| **search** | **String**|  | [optional] |
| **pluginType** | **Integer**|  | [optional] |
| **currentPeerTubeEngine** | **String**|  | [optional] |
| **start** | **Integer**| Offset used to paginate results | [optional] |
| **count** | **Integer**| Number of items to return | [optional] [default to 15] |
| **sort** | **String**| Sort column | [optional] |

### Return type

[**PluginResponse**](PluginResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **503** | plugin index unavailable |  -  |

<a id="getPlugin"></a>
# **getPlugin**
> Plugin getPlugin(npmName)

Get a plugin

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PluginsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PluginsApi apiInstance = new PluginsApi(defaultClient);
    String npmName = "peertube-plugin-auth-ldap"; // String | name of the plugin/theme on npmjs.com or in its package.json
    try {
      Plugin result = apiInstance.getPlugin(npmName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PluginsApi#getPlugin");
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
| **npmName** | **String**| name of the plugin/theme on npmjs.com or in its package.json | |

### Return type

[**Plugin**](Plugin.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **404** | plugin not found |  -  |

<a id="getPlugins"></a>
# **getPlugins**
> PluginResponse getPlugins(pluginType, uninstalled, start, count, sort)

List plugins

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PluginsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PluginsApi apiInstance = new PluginsApi(defaultClient);
    Integer pluginType = 56; // Integer | 
    Boolean uninstalled = true; // Boolean | 
    Integer start = 56; // Integer | Offset used to paginate results
    Integer count = 15; // Integer | Number of items to return
    String sort = "-createdAt"; // String | Sort column
    try {
      PluginResponse result = apiInstance.getPlugins(pluginType, uninstalled, start, count, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PluginsApi#getPlugins");
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
| **pluginType** | **Integer**|  | [optional] |
| **uninstalled** | **Boolean**|  | [optional] |
| **start** | **Integer**| Offset used to paginate results | [optional] |
| **count** | **Integer**| Number of items to return | [optional] [default to 15] |
| **sort** | **String**| Sort column | [optional] |

### Return type

[**PluginResponse**](PluginResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="uninstallPlugin"></a>
# **uninstallPlugin**
> uninstallPlugin(uninstallPluginRequest)

Uninstall a plugin

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PluginsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PluginsApi apiInstance = new PluginsApi(defaultClient);
    UninstallPluginRequest uninstallPluginRequest = new UninstallPluginRequest(); // UninstallPluginRequest | 
    try {
      apiInstance.uninstallPlugin(uninstallPluginRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling PluginsApi#uninstallPlugin");
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
| **uninstallPluginRequest** | [**UninstallPluginRequest**](UninstallPluginRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |
| **404** | existing plugin not found |  -  |

<a id="updatePlugin"></a>
# **updatePlugin**
> updatePlugin(addPluginRequest)

Update a plugin

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PluginsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://peertube2.cpy.re");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    PluginsApi apiInstance = new PluginsApi(defaultClient);
    AddPluginRequest addPluginRequest = new AddPluginRequest(); // AddPluginRequest | 
    try {
      apiInstance.updatePlugin(addPluginRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling PluginsApi#updatePlugin");
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
| **addPluginRequest** | [**AddPluginRequest**](AddPluginRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | successful operation |  -  |
| **400** | should have either &#x60;npmName&#x60; or &#x60;path&#x60; set |  -  |
| **404** | existing plugin not found |  -  |

