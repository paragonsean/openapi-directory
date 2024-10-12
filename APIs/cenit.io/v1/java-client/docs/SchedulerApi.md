# SchedulerApi

All URIs are relative to *https://cenit.io/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**setupSchedulerGet**](SchedulerApi.md#setupSchedulerGet) | **GET** /setup/scheduler/ | Returns a list of schedulers |
| [**setupSchedulerIdDelete**](SchedulerApi.md#setupSchedulerIdDelete) | **DELETE** /setup/scheduler/{id} | Delete an schedule |
| [**setupSchedulerIdGet**](SchedulerApi.md#setupSchedulerIdGet) | **GET** /setup/scheduler/{id} | Retrieve an existing schedule |
| [**setupSchedulerPost**](SchedulerApi.md#setupSchedulerPost) | **POST** /setup/scheduler/ | Create or update an scheduler |


<a id="setupSchedulerGet"></a>
# **setupSchedulerGet**
> List&lt;Scheduler&gt; setupSchedulerGet()

Returns a list of schedulers

Returns a list of schedulers you&#39;ve previously created. The schedulers are returned in sorted order, with the most recent scheduler appearing first.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchedulerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cenit.io/api/v1");
    
    // Configure API key authorization: X-User-Access-Key
    ApiKeyAuth X-User-Access-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-User-Access-Key");
    X-User-Access-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-User-Access-Key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-User-Access-Token
    ApiKeyAuth X-User-Access-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-User-Access-Token");
    X-User-Access-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-User-Access-Token.setApiKeyPrefix("Token");

    SchedulerApi apiInstance = new SchedulerApi(defaultClient);
    try {
      List<Scheduler> result = apiInstance.setupSchedulerGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchedulerApi#setupSchedulerGet");
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

[**List&lt;Scheduler&gt;**](Scheduler.md)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="setupSchedulerIdDelete"></a>
# **setupSchedulerIdDelete**
> setupSchedulerIdDelete(id)

Delete an schedule

Deletes the specified scheduler.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchedulerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cenit.io/api/v1");
    
    // Configure API key authorization: X-User-Access-Key
    ApiKeyAuth X-User-Access-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-User-Access-Key");
    X-User-Access-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-User-Access-Key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-User-Access-Token
    ApiKeyAuth X-User-Access-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-User-Access-Token");
    X-User-Access-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-User-Access-Token.setApiKeyPrefix("Token");

    SchedulerApi apiInstance = new SchedulerApi(defaultClient);
    String id = "id_example"; // String | Scheduler ID
    try {
      apiInstance.setupSchedulerIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchedulerApi#setupSchedulerIdDelete");
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
| **id** | **String**| Scheduler ID | |

### Return type

null (empty response body)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Item not found |  -  |

<a id="setupSchedulerIdGet"></a>
# **setupSchedulerIdGet**
> Scheduler setupSchedulerIdGet(id)

Retrieve an existing schedule

Retrieves the details of an existing scheduler. You need only supply the unique scheduler identifier that was returned upon scheduler creation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchedulerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cenit.io/api/v1");
    
    // Configure API key authorization: X-User-Access-Key
    ApiKeyAuth X-User-Access-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-User-Access-Key");
    X-User-Access-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-User-Access-Key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-User-Access-Token
    ApiKeyAuth X-User-Access-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-User-Access-Token");
    X-User-Access-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-User-Access-Token.setApiKeyPrefix("Token");

    SchedulerApi apiInstance = new SchedulerApi(defaultClient);
    String id = "id_example"; // String | Scheduler ID
    try {
      Scheduler result = apiInstance.setupSchedulerIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchedulerApi#setupSchedulerIdGet");
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
| **id** | **String**| Scheduler ID | |

### Return type

[**Scheduler**](Scheduler.md)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Item not found. |  -  |

<a id="setupSchedulerPost"></a>
# **setupSchedulerPost**
> Scheduler setupSchedulerPost()

Create or update an scheduler

Creates or updates the specified scheduler. Any parameters not provided will be left unchanged.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchedulerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cenit.io/api/v1");
    
    // Configure API key authorization: X-User-Access-Key
    ApiKeyAuth X-User-Access-Key = (ApiKeyAuth) defaultClient.getAuthentication("X-User-Access-Key");
    X-User-Access-Key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-User-Access-Key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-User-Access-Token
    ApiKeyAuth X-User-Access-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-User-Access-Token");
    X-User-Access-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-User-Access-Token.setApiKeyPrefix("Token");

    SchedulerApi apiInstance = new SchedulerApi(defaultClient);
    try {
      Scheduler result = apiInstance.setupSchedulerPost();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchedulerApi#setupSchedulerPost");
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

[**Scheduler**](Scheduler.md)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

