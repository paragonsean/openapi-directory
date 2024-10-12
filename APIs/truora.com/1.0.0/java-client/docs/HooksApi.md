# HooksApi

All URIs are relative to *https://api.truora.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createHook**](HooksApi.md#createHook) | **POST** /v1/hooks | Creates a hook subscription |
| [**deletHook**](HooksApi.md#deletHook) | **DELETE** /v1/hooks/{hook_id} | Deletes hook |
| [**listHook**](HooksApi.md#listHook) | **GET** /v1/hooks | Lists all hooks |
| [**updateHook**](HooksApi.md#updateHook) | **PUT** /v1/hooks/{hook_id} | Updates hook |


<a id="createHook"></a>
# **createHook**
> Hook createHook(eventType, subscriberType, actions, status, subscriberAddress, subscriberLanguage, subscriberName, subscriberUrl)

Creates a hook subscription

Creates a hook subscription to notify events in Truora plataform. Subscriptions broadcast data as events occur and additional subscription instances are not required in order to refresh the information. Events are received in an array as a JWT and are decoded using the signing key returned by this endpoint. Their structure is as follows:  &#x60;&#x60;&#x60; {     \&quot;events\&quot;: [         {             \&quot;event_action\&quot;: \&quot;created\&quot;,             \&quot;event_type\&quot;: \&quot;check\&quot;,             \&quot;id\&quot;: \&quot;HKEdd28c569cf5eb74e45f0f4c092096e62c1c95ba2\&quot;,             \&quot;object\&quot;: {                 \&quot;check_id\&quot;: \&quot;CHK9c39003424c521aec8566ce59e1ddc86\&quot;,                 \&quot;country\&quot;: \&quot;CO\&quot;,                 \&quot;creation_date\&quot;: \&quot;2020-04-01T23:00:30.581232281Z\&quot;,                 \&quot;homonym_score\&quot;: 0,                 \&quot;id_score\&quot;: 0,                 \&quot;national_id\&quot;: \&quot;1151959906\&quot;,                 \&quot;previous_check\&quot;: \&quot;CHK4ec814fecd147eaae41027081d7d5caf\&quot;,                 \&quot;score\&quot;: -1,                 \&quot;status\&quot;: \&quot;not_started\&quot;,                 \&quot;type\&quot;: \&quot;person\&quot;,                 \&quot;update_date\&quot;: \&quot;2020-04-01T23:00:30.680937413Z\&quot;             },             \&quot;timestamp\&quot;: \&quot;2020-04-01T23:00:30Z\&quot;,             \&quot;version\&quot;: \&quot;1.0\&quot;         }     ],     \&quot;iat\&quot;: 1585782031,     \&quot;iss\&quot;: \&quot;Truora\&quot; } &#x60;&#x60;&#x60;  Keep in mind that the object attribute varies depending on the event_type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.truora.com");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    HooksApi apiInstance = new HooksApi(defaultClient);
    String eventType = "all"; // String | The entity events the client wants to subscribe
    String subscriberType = "web"; // String | A platform with an endpoint ready to process the information
    List<String> actions = Arrays.asList(); // List<String> | Actions you want to be notified. Possible inputs are created, started, and finished or any combination of those three
    String status = "enabled"; // String | indicates whether the hook is active or not. enabled by default
    String subscriberAddress = "subscriberAddress_example"; // String | Email address where the notification is to be sent. Required if subscriber_type was set to email
    String subscriberLanguage = "af"; // String | Language for the notification to be sent
    String subscriberName = "subscriberName_example"; // String | Name of the person to be notified
    String subscriberUrl = "subscriberUrl_example"; // String | URL where the notification is to be sent. Required only if subscriber_type is set to web
    try {
      Hook result = apiInstance.createHook(eventType, subscriberType, actions, status, subscriberAddress, subscriberLanguage, subscriberName, subscriberUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HooksApi#createHook");
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
| **eventType** | **String**| The entity events the client wants to subscribe | [enum: all, check, continuous_check] |
| **subscriberType** | **String**| A platform with an endpoint ready to process the information | [enum: web, email] |
| **actions** | [**List&lt;String&gt;**](String.md)| Actions you want to be notified. Possible inputs are created, started, and finished or any combination of those three | [optional] |
| **status** | **String**| indicates whether the hook is active or not. enabled by default | [optional] [enum: enabled, disabled] |
| **subscriberAddress** | **String**| Email address where the notification is to be sent. Required if subscriber_type was set to email | [optional] |
| **subscriberLanguage** | **String**| Language for the notification to be sent | [optional] [enum: af, ar, ca, cs, da, de, el, en, es, fi, fr, he, hi, hr, hu, id, it, ja, ko, ms, nb, nl, pl, pt, pr-BR, ro, ru, sv, th, tl, tr, vi, zh, zh-CN, zh-HK] |
| **subscriberName** | **String**| Name of the person to be notified | [optional] |
| **subscriberUrl** | **String**| URL where the notification is to be sent. Required only if subscriber_type is set to web | [optional] |

### Return type

[**Hook**](Hook.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |
| **400** | Validation error, at least one of the parameters was invalid. |  -  |

<a id="deletHook"></a>
# **deletHook**
> String deletHook(hookId)

Deletes hook

Deletes hook configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.truora.com");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    HooksApi apiInstance = new HooksApi(defaultClient);
    String hookId = "hookId_example"; // String | Hook ID
    try {
      String result = apiInstance.deletHook(hookId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HooksApi#deletHook");
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
| **hookId** | **String**| Hook ID | |

### Return type

**String**

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="listHook"></a>
# **listHook**
> HookOutput listHook()

Lists all hooks

Lists all the configured hooks in your account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.truora.com");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    HooksApi apiInstance = new HooksApi(defaultClient);
    try {
      HookOutput result = apiInstance.listHook();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HooksApi#listHook");
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

[**HookOutput**](HookOutput.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="updateHook"></a>
# **updateHook**
> Hook updateHook(hookId, eventType, subscriberType, actions, status, subscriberAddress, subscriberLanguage, subscriberName, subscriberUrl)

Updates hook

Updates a hook configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HooksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.truora.com");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    HooksApi apiInstance = new HooksApi(defaultClient);
    String hookId = "hookId_example"; // String | Hook ID
    String eventType = "all"; // String | The entity events the client wants to subscribe
    String subscriberType = "web"; // String | A platform with an endpoint ready to process the information
    List<String> actions = Arrays.asList(); // List<String> | Actions you want to be notified. Possible inputs are created, started, and finished or any combination of those three
    String status = "enabled"; // String | indicates whether the hook is active or not. enabled by default
    String subscriberAddress = "subscriberAddress_example"; // String | Email address where the notification is to be sent. Required if subscriber_type was set to email
    String subscriberLanguage = "af"; // String | Language for the notification to be sent
    String subscriberName = "subscriberName_example"; // String | Name of the person to be notified
    String subscriberUrl = "subscriberUrl_example"; // String | URL where the notification is to be sent. Required only if subscriber_type is set to web
    try {
      Hook result = apiInstance.updateHook(hookId, eventType, subscriberType, actions, status, subscriberAddress, subscriberLanguage, subscriberName, subscriberUrl);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HooksApi#updateHook");
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
| **hookId** | **String**| Hook ID | |
| **eventType** | **String**| The entity events the client wants to subscribe | [enum: all, check, continuous_check] |
| **subscriberType** | **String**| A platform with an endpoint ready to process the information | [enum: web, email] |
| **actions** | [**List&lt;String&gt;**](String.md)| Actions you want to be notified. Possible inputs are created, started, and finished or any combination of those three | [optional] |
| **status** | **String**| indicates whether the hook is active or not. enabled by default | [optional] [enum: enabled, disabled] |
| **subscriberAddress** | **String**| Email address where the notification is to be sent. Required if subscriber_type was set to email | [optional] |
| **subscriberLanguage** | **String**| Language for the notification to be sent | [optional] [enum: af, ar, ca, cs, da, de, el, en, es, fi, fr, he, hi, hr, hu, id, it, ja, ko, ms, nb, nl, pl, pt, pr-BR, ro, ru, sv, th, tl, tr, vi, zh, zh-CN, zh-HK] |
| **subscriberName** | **String**| Name of the person to be notified | [optional] |
| **subscriberUrl** | **String**| URL where the notification is to be sent. Required only if subscriber_type is set to web | [optional] |

### Return type

[**Hook**](Hook.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/x-www-form-urlencoded, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Validation error, at least one of the parameters was invalid. |  -  |

