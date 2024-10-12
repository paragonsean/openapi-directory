# UserApiApi

All URIs are relative to *http://meshery.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**idDeleteLoadPreferences**](UserApiApi.md#idDeleteLoadPreferences) | **DELETE** /api/user/prefs/perf | Handle DELETE request for load test preferences |
| [**idGetLoadPreferences**](UserApiApi.md#idGetLoadPreferences) | **GET** /api/user/prefs/perf | Handle GET request for load test preferences |
| [**idGetTokenProvider**](UserApiApi.md#idGetTokenProvider) | **GET** /api/user/token | Handle GET request for tokens |
| [**idGetUserLogin**](UserApiApi.md#idGetUserLogin) | **GET** /api/user/login | Handlers GET request for User login |
| [**idGetUserLogout**](UserApiApi.md#idGetUserLogout) | **GET** /api/user/logout | Handlers GET request for User logout |
| [**idGetUserTestPrefs**](UserApiApi.md#idGetUserTestPrefs) | **GET** /api/user/prefs | Handle GET for User Load Test Preferences |
| [**idPostLoadPreferences**](UserApiApi.md#idPostLoadPreferences) | **POST** /api/user/prefs/perf | Handle POST request for load test preferences |
| [**idPostTokenProvider**](UserApiApi.md#idPostTokenProvider) | **POST** /api/user/token | Handle POST request for tokens |
| [**idPostUserTestPrefs**](UserApiApi.md#idPostUserTestPrefs) | **POST** /api/user/prefs | Handle GET for User Load Test Preferences |


<a id="idDeleteLoadPreferences"></a>
# **idDeleteLoadPreferences**
> idDeleteLoadPreferences(uuid)

Handle DELETE request for load test preferences

Used for deleting load test preferences

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    UserApiApi apiInstance = new UserApiApi(defaultClient);
    UUID uuid = UUID.randomUUID(); // UUID | 
    try {
      apiInstance.idDeleteLoadPreferences(uuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApiApi#idDeleteLoadPreferences");
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
| **uuid** | **UUID**|  | [optional] |

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="idGetLoadPreferences"></a>
# **idGetLoadPreferences**
> PerformanceTestConfig idGetLoadPreferences(uuid)

Handle GET request for load test preferences

Used for fetching load test preferences

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    UserApiApi apiInstance = new UserApiApi(defaultClient);
    UUID uuid = UUID.randomUUID(); // UUID | 
    try {
      PerformanceTestConfig result = apiInstance.idGetLoadPreferences(uuid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApiApi#idGetLoadPreferences");
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
| **uuid** | **UUID**|  | [optional] |

### Return type

[**PerformanceTestConfig**](PerformanceTestConfig.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns load test preferences |  -  |

<a id="idGetTokenProvider"></a>
# **idGetTokenProvider**
> idGetTokenProvider()

Handle GET request for tokens

Returns token from the actual provider in a file resposese: 200:

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    UserApiApi apiInstance = new UserApiApi(defaultClient);
    try {
      apiInstance.idGetTokenProvider();
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApiApi#idGetTokenProvider");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Default response |  -  |

<a id="idGetUserLogin"></a>
# **idGetUserLogin**
> idGetUserLogin()

Handlers GET request for User login

Redirects user for auth or issues session

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    UserApiApi apiInstance = new UserApiApi(defaultClient);
    try {
      apiInstance.idGetUserLogin();
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApiApi#idGetUserLogin");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="idGetUserLogout"></a>
# **idGetUserLogout**
> idGetUserLogout()

Handlers GET request for User logout

Redirects user for auth or issues session

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    UserApiApi apiInstance = new UserApiApi(defaultClient);
    try {
      apiInstance.idGetUserLogout();
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApiApi#idGetUserLogout");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="idGetUserTestPrefs"></a>
# **idGetUserTestPrefs**
> Preference idGetUserTestPrefs()

Handle GET for User Load Test Preferences

Returns User Load Test Preferences

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    UserApiApi apiInstance = new UserApiApi(defaultClient);
    try {
      Preference result = apiInstance.idGetUserTestPrefs();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApiApi#idGetUserTestPrefs");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Preference**](Preference.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns User Load Test Preferencee |  -  |

<a id="idPostLoadPreferences"></a>
# **idPostLoadPreferences**
> idPostLoadPreferences(performanceTestConfig)

Handle POST request for load test preferences

Used for persisting load test preferences

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    UserApiApi apiInstance = new UserApiApi(defaultClient);
    PerformanceTestConfig performanceTestConfig = new PerformanceTestConfig(); // PerformanceTestConfig | 
    try {
      apiInstance.idPostLoadPreferences(performanceTestConfig);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApiApi#idPostLoadPreferences");
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
| **performanceTestConfig** | [**PerformanceTestConfig**](PerformanceTestConfig.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="idPostTokenProvider"></a>
# **idPostTokenProvider**
> idPostTokenProvider()

Handle POST request for tokens

Receives token from the actual provider resposese: 200:

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    UserApiApi apiInstance = new UserApiApi(defaultClient);
    try {
      apiInstance.idPostTokenProvider();
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApiApi#idPostTokenProvider");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Default response |  -  |

<a id="idPostUserTestPrefs"></a>
# **idPostUserTestPrefs**
> Preference idPostUserTestPrefs()

Handle GET for User Load Test Preferences

Updates User Load Test Preferences

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://meshery.local");
    
    // Configure API key authorization: token
    ApiKeyAuth token = (ApiKeyAuth) defaultClient.getAuthentication("token");
    token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //token.setApiKeyPrefix("Token");

    UserApiApi apiInstance = new UserApiApi(defaultClient);
    try {
      Preference result = apiInstance.idPostUserTestPrefs();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApiApi#idPostUserTestPrefs");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Preference**](Preference.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns User Load Test Preferencee |  -  |

