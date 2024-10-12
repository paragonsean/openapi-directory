# EnvironmentVariablesApi

All URIs are relative to *https://api.netlify.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createEnvVars**](EnvironmentVariablesApi.md#createEnvVars) | **POST** /accounts/{account_id}/env |  |
| [**deleteEnvVar**](EnvironmentVariablesApi.md#deleteEnvVar) | **DELETE** /accounts/{account_id}/env/{key} |  |
| [**deleteEnvVarValue**](EnvironmentVariablesApi.md#deleteEnvVarValue) | **DELETE** /accounts/{account_id}/env/{key}/value/{id} |  |
| [**getEnvVar**](EnvironmentVariablesApi.md#getEnvVar) | **GET** /accounts/{account_id}/env/{key} |  |
| [**getEnvVars**](EnvironmentVariablesApi.md#getEnvVars) | **GET** /accounts/{account_id}/env |  |
| [**setEnvVarValue**](EnvironmentVariablesApi.md#setEnvVarValue) | **PATCH** /accounts/{account_id}/env/{key} |  |
| [**updateEnvVar**](EnvironmentVariablesApi.md#updateEnvVar) | **PUT** /accounts/{account_id}/env/{key} |  |


<a id="createEnvVars"></a>
# **createEnvVars**
> List&lt;EnvVar&gt; createEnvVars(accountId, siteId, envVars)



Creates new environment variables. Granular scopes are available on Pro plans and above.  To use this endpoint, your site must no longer be using the &lt;a href&#x3D;\&quot;https://docs.netlify.com/environment-variables/classic-experience/\&quot;&gt;classic environment variables experience&lt;/a&gt;.  Migrate now with the Netlify UI.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentVariablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    EnvironmentVariablesApi apiInstance = new EnvironmentVariablesApi(defaultClient);
    String accountId = "accountId_example"; // String | Scope response to account_id
    String siteId = "siteId_example"; // String | If provided, create an environment variable on the site level, not the account level
    List<CreateEnvVarsRequestInner> envVars = Arrays.asList(); // List<CreateEnvVarsRequestInner> | 
    try {
      List<EnvVar> result = apiInstance.createEnvVars(accountId, siteId, envVars);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentVariablesApi#createEnvVars");
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
| **accountId** | **String**| Scope response to account_id | |
| **siteId** | **String**| If provided, create an environment variable on the site level, not the account level | [optional] |
| **envVars** | [**List&lt;CreateEnvVarsRequestInner&gt;**](CreateEnvVarsRequestInner.md)|  | [optional] |

### Return type

[**List&lt;EnvVar&gt;**](EnvVar.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |
| **0** | error |  -  |

<a id="deleteEnvVar"></a>
# **deleteEnvVar**
> deleteEnvVar(accountId, key, siteId)



Deletes an environment variable. To use this endpoint, your site must no longer be using the &lt;a href&#x3D;\&quot;https://docs.netlify.com/environment-variables/classic-experience/\&quot;&gt;classic environment variables experience&lt;/a&gt;.  Migrate now with the Netlify UI.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentVariablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    EnvironmentVariablesApi apiInstance = new EnvironmentVariablesApi(defaultClient);
    String accountId = "accountId_example"; // String | Scope response to account_id
    String key = "key_example"; // String | The environment variable key (case-sensitive)
    String siteId = "siteId_example"; // String | If provided, delete the environment variable from this site
    try {
      apiInstance.deleteEnvVar(accountId, key, siteId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentVariablesApi#deleteEnvVar");
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
| **accountId** | **String**| Scope response to account_id | |
| **key** | **String**| The environment variable key (case-sensitive) | |
| **siteId** | **String**| If provided, delete the environment variable from this site | [optional] |

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
| **204** | No Content (success) |  -  |
| **0** | error |  -  |

<a id="deleteEnvVarValue"></a>
# **deleteEnvVarValue**
> deleteEnvVarValue(accountId, id, key, siteId)



Deletes a specific environment variable value. To use this endpoint, your site must no longer be using the &lt;a href&#x3D;\&quot;https://docs.netlify.com/environment-variables/classic-experience/\&quot;&gt;classic environment variables experience&lt;/a&gt;.  Migrate now with the Netlify UI.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentVariablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    EnvironmentVariablesApi apiInstance = new EnvironmentVariablesApi(defaultClient);
    String accountId = "accountId_example"; // String | Scope response to account_id
    String id = "id_example"; // String | The environment variable value's ID
    String key = "key_example"; // String | The environment variable key name (case-sensitive)
    String siteId = "siteId_example"; // String | If provided, delete the value from an environment variable on this site
    try {
      apiInstance.deleteEnvVarValue(accountId, id, key, siteId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentVariablesApi#deleteEnvVarValue");
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
| **accountId** | **String**| Scope response to account_id | |
| **id** | **String**| The environment variable value&#39;s ID | |
| **key** | **String**| The environment variable key name (case-sensitive) | |
| **siteId** | **String**| If provided, delete the value from an environment variable on this site | [optional] |

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
| **204** | No Content (success) |  -  |
| **0** | error |  -  |

<a id="getEnvVar"></a>
# **getEnvVar**
> EnvVar getEnvVar(accountId, key, siteId)



Returns an individual environment variable. To use this endpoint, your site must no longer be using the &lt;a href&#x3D;\&quot;https://docs.netlify.com/environment-variables/classic-experience/\&quot;&gt;classic environment variables experience&lt;/a&gt;.  Migrate now with the Netlify UI.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentVariablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    EnvironmentVariablesApi apiInstance = new EnvironmentVariablesApi(defaultClient);
    String accountId = "accountId_example"; // String | Scope response to account_id
    String key = "key_example"; // String | The environment variable key (case-sensitive)
    String siteId = "siteId_example"; // String | If provided, return the environment variable for a specific site (no merging is performed)
    try {
      EnvVar result = apiInstance.getEnvVar(accountId, key, siteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentVariablesApi#getEnvVar");
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
| **accountId** | **String**| Scope response to account_id | |
| **key** | **String**| The environment variable key (case-sensitive) | |
| **siteId** | **String**| If provided, return the environment variable for a specific site (no merging is performed) | [optional] |

### Return type

[**EnvVar**](EnvVar.md)

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

<a id="getEnvVars"></a>
# **getEnvVars**
> List&lt;EnvVar&gt; getEnvVars(accountId, contextName, scope, siteId)



Returns all environment variables for an account or site. An account corresponds to a team in the Netlify UI. To use this endpoint, your site must no longer be using the &lt;a href&#x3D;\&quot;https://docs.netlify.com/environment-variables/classic-experience/\&quot;&gt;classic environment variables experience&lt;/a&gt;.  Migrate now with the Netlify UI.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentVariablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    EnvironmentVariablesApi apiInstance = new EnvironmentVariablesApi(defaultClient);
    String accountId = "accountId_example"; // String | Scope response to account_id
    String contextName = "all"; // String | Filter by deploy context
    String scope = "builds"; // String | Filter by scope
    String siteId = "siteId_example"; // String | If specified, only return environment variables set on this site
    try {
      List<EnvVar> result = apiInstance.getEnvVars(accountId, contextName, scope, siteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentVariablesApi#getEnvVars");
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
| **accountId** | **String**| Scope response to account_id | |
| **contextName** | **String**| Filter by deploy context | [optional] [enum: all, dev, branch-deploy, deploy-preview, production] |
| **scope** | **String**| Filter by scope | [optional] [enum: builds, functions, runtime, post-processing] |
| **siteId** | **String**| If specified, only return environment variables set on this site | [optional] |

### Return type

[**List&lt;EnvVar&gt;**](EnvVar.md)

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

<a id="setEnvVarValue"></a>
# **setEnvVarValue**
> EnvVar setEnvVarValue(accountId, key, siteId, envVar)



Updates or creates a new value for an existing environment variable. To use this endpoint, your site must no longer be using the &lt;a href&#x3D;\&quot;https://docs.netlify.com/environment-variables/classic-experience/\&quot;&gt;classic environment variables experience&lt;/a&gt;.  Migrate now with the Netlify UI.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentVariablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    EnvironmentVariablesApi apiInstance = new EnvironmentVariablesApi(defaultClient);
    String accountId = "accountId_example"; // String | Scope response to account_id
    String key = "key_example"; // String | The existing environment variable key name (case-sensitive)
    String siteId = "siteId_example"; // String | If provided, update an environment variable set on this site
    SetEnvVarValueRequest envVar = new SetEnvVarValueRequest(); // SetEnvVarValueRequest | 
    try {
      EnvVar result = apiInstance.setEnvVarValue(accountId, key, siteId, envVar);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentVariablesApi#setEnvVarValue");
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
| **accountId** | **String**| Scope response to account_id | |
| **key** | **String**| The existing environment variable key name (case-sensitive) | |
| **siteId** | **String**| If provided, update an environment variable set on this site | [optional] |
| **envVar** | [**SetEnvVarValueRequest**](SetEnvVarValueRequest.md)|  | [optional] |

### Return type

[**EnvVar**](EnvVar.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created (success) |  -  |
| **0** | error |  -  |

<a id="updateEnvVar"></a>
# **updateEnvVar**
> EnvVar updateEnvVar(accountId, key, siteId, envVar)



Updates an existing environment variable and all of its values. Existing values will be replaced by values provided. To use this endpoint, your site must no longer be using the &lt;a href&#x3D;\&quot;https://docs.netlify.com/environment-variables/classic-experience/\&quot;&gt;classic environment variables experience&lt;/a&gt;.  Migrate now with the Netlify UI.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EnvironmentVariablesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    EnvironmentVariablesApi apiInstance = new EnvironmentVariablesApi(defaultClient);
    String accountId = "accountId_example"; // String | Scope response to account_id
    String key = "key_example"; // String | The existing environment variable key name (case-sensitive)
    String siteId = "siteId_example"; // String | If provided, update an environment variable set on this site
    CreateEnvVarsRequestInner envVar = new CreateEnvVarsRequestInner(); // CreateEnvVarsRequestInner | 
    try {
      EnvVar result = apiInstance.updateEnvVar(accountId, key, siteId, envVar);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EnvironmentVariablesApi#updateEnvVar");
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
| **accountId** | **String**| Scope response to account_id | |
| **key** | **String**| The existing environment variable key name (case-sensitive) | |
| **siteId** | **String**| If provided, update an environment variable set on this site | [optional] |
| **envVar** | [**CreateEnvVarsRequestInner**](CreateEnvVarsRequestInner.md)|  | [optional] |

### Return type

[**EnvVar**](EnvVar.md)

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

