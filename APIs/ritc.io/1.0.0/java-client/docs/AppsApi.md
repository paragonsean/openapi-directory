# AppsApi

All URIs are relative to *https://api.ritc.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addApp**](AppsApi.md#addApp) | **POST** /apps |  |
| [**addAppChannelUser**](AppsApi.md#addAppChannelUser) | **POST** /apps/channels/{channel_id}/users/{user_id} |  |
| [**addChannelExternalCredentials**](AppsApi.md#addChannelExternalCredentials) | **POST** /apps/ext/api/credentials |  |
| [**getApp**](AppsApi.md#getApp) | **GET** /apps/{app_id} |  |
| [**getAppChannelUser**](AppsApi.md#getAppChannelUser) | **GET** /apps/channels/{channel_id}/users/{user_id} |  |
| [**getChannelExternalCredentials**](AppsApi.md#getChannelExternalCredentials) | **GET** /apps/ext/api/credentials/{channel_id} |  |
| [**listAppChannelUsers**](AppsApi.md#listAppChannelUsers) | **GET** /apps/channels/{channel_id}/users |  |
| [**listAppChannels**](AppsApi.md#listAppChannels) | **GET** /apps/channels/users |  |
| [**listApps**](AppsApi.md#listApps) | **GET** /apps |  |
| [**listChannelExternalCredentials**](AppsApi.md#listChannelExternalCredentials) | **GET** /apps/ext/api/credentials |  |
| [**removeApp**](AppsApi.md#removeApp) | **DELETE** /apps/{app_id} |  |
| [**removeChannelExternalCredentials**](AppsApi.md#removeChannelExternalCredentials) | **DELETE** /apps/ext/api/credentials/{channel_id} |  |
| [**runApp**](AppsApi.md#runApp) | **POST** /apps/rules/run |  |
| [**runRuleGroup**](AppsApi.md#runRuleGroup) | **POST** /apps/rulegroup/run/{rule_id_list} |  |
| [**updateApp**](AppsApi.md#updateApp) | **PATCH** /apps/{app_id} |  |
| [**updateChannelExternalCredentials**](AppsApi.md#updateChannelExternalCredentials) | **PATCH** /apps/ext/api/credentials/{channel_id} |  |


<a id="addApp"></a>
# **addApp**
> AppResponse addApp(appObject)



Create a new app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritc.io");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AppsApi apiInstance = new AppsApi(defaultClient);
    App appObject = new App(); // App | App information
    try {
      AppResponse result = apiInstance.addApp(appObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#addApp");
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
| **appObject** | [**App**](App.md)| App information | |

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An app was created |  -  |
| **400** | Invalid Input |  -  |
| **0** | Unexpected error |  -  |

<a id="addAppChannelUser"></a>
# **addAppChannelUser**
> AppChannelResponse addAppChannelUser(channelId, userId)



Create user channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritc.io");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String channelId = "channelId_example"; // String | Id of Channel
    String userId = "userId_example"; // String | Id of User
    try {
      AppChannelResponse result = apiInstance.addAppChannelUser(channelId, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#addAppChannelUser");
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
| **channelId** | **String**| Id of Channel | |
| **userId** | **String**| Id of User | |

### Return type

[**AppChannelResponse**](AppChannelResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User was assigned to a channel in in app |  -  |
| **400** | Invalid Input |  -  |
| **0** | Unexpected error |  -  |

<a id="addChannelExternalCredentials"></a>
# **addChannelExternalCredentials**
> AppExternalCredentialsResponse addChannelExternalCredentials(appExternalCredentialsObject)



Create new external credentials

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritc.io");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AppsApi apiInstance = new AppsApi(defaultClient);
    AppExternalCredentials appExternalCredentialsObject = new AppExternalCredentials(); // AppExternalCredentials | App_External_Credentials information
    try {
      AppExternalCredentialsResponse result = apiInstance.addChannelExternalCredentials(appExternalCredentialsObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#addChannelExternalCredentials");
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
| **appExternalCredentialsObject** | [**AppExternalCredentials**](AppExternalCredentials.md)| App_External_Credentials information | |

### Return type

[**AppExternalCredentialsResponse**](AppExternalCredentialsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | External credentials created |  -  |
| **400** | Invalid Input |  -  |
| **0** | Unexpected error |  -  |

<a id="getApp"></a>
# **getApp**
> List&lt;AppResponse&gt; getApp(appId)



Get app information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritc.io");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String appId = "appId_example"; // String | Id of App
    try {
      List<AppResponse> result = apiInstance.getApp(appId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#getApp");
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
| **appId** | **String**| Id of App | |

### Return type

[**List&lt;AppResponse&gt;**](AppResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Detailed information about an app |  -  |
| **400** | Invalid input |  -  |
| **0** | Unexpected error |  -  |

<a id="getAppChannelUser"></a>
# **getAppChannelUser**
> List&lt;AppChannelResponse&gt; getAppChannelUser(channelId, userId)



Get user of a specified channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritc.io");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String channelId = "channelId_example"; // String | Id of Channel
    String userId = "userId_example"; // String | Id of User
    try {
      List<AppChannelResponse> result = apiInstance.getAppChannelUser(channelId, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#getAppChannelUser");
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
| **channelId** | **String**| Id of Channel | |
| **userId** | **String**| Id of User | |

### Return type

[**List&lt;AppChannelResponse&gt;**](AppChannelResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Detailed information about a specified user of a specified channel |  -  |
| **400** | Invalid input |  -  |
| **0** | Unexpected error |  -  |

<a id="getChannelExternalCredentials"></a>
# **getChannelExternalCredentials**
> List&lt;AppExternalCredentialsResponse&gt; getChannelExternalCredentials(channelId)



Get credentials for a channel in an app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritc.io");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String channelId = "channelId_example"; // String | Id of Channel
    try {
      List<AppExternalCredentialsResponse> result = apiInstance.getChannelExternalCredentials(channelId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#getChannelExternalCredentials");
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
| **channelId** | **String**| Id of Channel | |

### Return type

[**List&lt;AppExternalCredentialsResponse&gt;**](AppExternalCredentialsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Credentials for a channel in an app |  -  |
| **400** | Invalid input |  -  |
| **0** | Unexpected error |  -  |

<a id="listAppChannelUsers"></a>
# **listAppChannelUsers**
> List&lt;AppChannelResponse&gt; listAppChannelUsers(channelId)



Get users of a specified channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritc.io");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String channelId = "channelId_example"; // String | Id of Channel
    try {
      List<AppChannelResponse> result = apiInstance.listAppChannelUsers(channelId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#listAppChannelUsers");
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
| **channelId** | **String**| Id of Channel | |

### Return type

[**List&lt;AppChannelResponse&gt;**](AppChannelResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Detailed information about users of a specified channel |  -  |
| **400** | Invalid input |  -  |
| **0** | Unexpected error |  -  |

<a id="listAppChannels"></a>
# **listAppChannels**
> List&lt;AppChannelResponse&gt; listAppChannels()



Get app channels

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritc.io");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AppsApi apiInstance = new AppsApi(defaultClient);
    try {
      List<AppChannelResponse> result = apiInstance.listAppChannels();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#listAppChannels");
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

[**List&lt;AppChannelResponse&gt;**](AppChannelResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of all channels in an app |  -  |
| **400** | Invalid input |  -  |
| **0** | Unexpected error |  -  |

<a id="listApps"></a>
# **listApps**
> List&lt;AppResponse&gt; listApps()



Get apps information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritc.io");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AppsApi apiInstance = new AppsApi(defaultClient);
    try {
      List<AppResponse> result = apiInstance.listApps();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#listApps");
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

[**List&lt;AppResponse&gt;**](AppResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of apps in an org |  -  |
| **400** | Invalid input |  -  |
| **0** | Unexpected error |  -  |

<a id="listChannelExternalCredentials"></a>
# **listChannelExternalCredentials**
> List&lt;AppExternalCredentialsResponse&gt; listChannelExternalCredentials()



Get external credentials

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritc.io");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AppsApi apiInstance = new AppsApi(defaultClient);
    try {
      List<AppExternalCredentialsResponse> result = apiInstance.listChannelExternalCredentials();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#listChannelExternalCredentials");
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

[**List&lt;AppExternalCredentialsResponse&gt;**](AppExternalCredentialsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Detailed information about external credentials |  -  |
| **400** | Invalid input |  -  |
| **0** | Unexpected error |  -  |

<a id="removeApp"></a>
# **removeApp**
> removeApp(appId)



Delete an app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritc.io");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String appId = "appId_example"; // String | Id of App
    try {
      apiInstance.removeApp(appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#removeApp");
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
| **appId** | **String**| Id of App | |

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The app was successfully removed |  -  |
| **400** | Invalid input |  -  |
| **0** | Unexpected error |  -  |

<a id="removeChannelExternalCredentials"></a>
# **removeChannelExternalCredentials**
> removeChannelExternalCredentials(channelId)



Delete credentials for a channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritc.io");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String channelId = "channelId_example"; // String | Id of Channel
    try {
      apiInstance.removeChannelExternalCredentials(channelId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#removeChannelExternalCredentials");
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
| **channelId** | **String**| Id of Channel | |

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The credentials for a channel were successfully removed |  -  |
| **400** | Invalid input |  -  |
| **0** | Unexpected error |  -  |

<a id="runApp"></a>
# **runApp**
> List&lt;RuleResults&gt; runApp(breakWhenRuleFires, initialData)



Run active app rules

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritc.io");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AppsApi apiInstance = new AppsApi(defaultClient);
    Boolean breakWhenRuleFires = true; // Boolean | Do not continue with remaining rules after a rule fires
    Object initialData = null; // Object | Initial data
    try {
      List<RuleResults> result = apiInstance.runApp(breakWhenRuleFires, initialData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#runApp");
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
| **breakWhenRuleFires** | **Boolean**| Do not continue with remaining rules after a rule fires | [optional] |
| **initialData** | **Object**| Initial data | [optional] |

### Return type

[**List&lt;RuleResults&gt;**](RuleResults.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Execution of active rules in the app (for user #1) |  -  |
| **400** | Invalid input |  -  |
| **0** | Unexpected error |  -  |

<a id="runRuleGroup"></a>
# **runRuleGroup**
> List&lt;RuleResults&gt; runRuleGroup(ruleIdList, breakWhenRuleFires, initialData)



Run specified rule group in the app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritc.io");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String ruleIdList = "ruleIdList_example"; // String | Ids of rules in the group, separated by commas, no spaces
    Boolean breakWhenRuleFires = true; // Boolean | Do not continue with remaining rules after a rule fires
    Object initialData = null; // Object | Initial data
    try {
      List<RuleResults> result = apiInstance.runRuleGroup(ruleIdList, breakWhenRuleFires, initialData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#runRuleGroup");
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
| **ruleIdList** | **String**| Ids of rules in the group, separated by commas, no spaces | |
| **breakWhenRuleFires** | **Boolean**| Do not continue with remaining rules after a rule fires | [optional] |
| **initialData** | **Object**| Initial data | [optional] |

### Return type

[**List&lt;RuleResults&gt;**](RuleResults.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Execution of specified rules in the app (for user #1) |  -  |
| **400** | Invalid input |  -  |
| **0** | Unexpected error |  -  |

<a id="updateApp"></a>
# **updateApp**
> AppResponse updateApp(appId, appObject)



Update an app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritc.io");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String appId = "appId_example"; // String | Id of app
    App appObject = new App(); // App | App information
    try {
      AppResponse result = apiInstance.updateApp(appId, appObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#updateApp");
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
| **appId** | **String**| Id of app | |
| **appObject** | [**App**](App.md)| App information | |

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Information about the app was updated successfully |  -  |
| **400** | Invalid input |  -  |
| **0** | Unexpected error |  -  |

<a id="updateChannelExternalCredentials"></a>
# **updateChannelExternalCredentials**
> AppExternalCredentialsResponse updateChannelExternalCredentials(channelId, appExternalCredentialsObject)



Update credentials for a channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ritc.io");
    
    // Configure API key authorization: Authorization
    ApiKeyAuth Authorization = (ApiKeyAuth) defaultClient.getAuthentication("Authorization");
    Authorization.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Authorization.setApiKeyPrefix("Token");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String channelId = "channelId_example"; // String | Id of Channel
    AppExternalCredentials appExternalCredentialsObject = new AppExternalCredentials(); // AppExternalCredentials | App_External_Credentials information
    try {
      AppExternalCredentialsResponse result = apiInstance.updateChannelExternalCredentials(channelId, appExternalCredentialsObject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#updateChannelExternalCredentials");
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
| **channelId** | **String**| Id of Channel | |
| **appExternalCredentialsObject** | [**AppExternalCredentials**](AppExternalCredentials.md)| App_External_Credentials information | |

### Return type

[**AppExternalCredentialsResponse**](AppExternalCredentialsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Information about the channel credentials was updated successfully |  -  |
| **400** | Invalid input |  -  |
| **0** | Unexpected error |  -  |

