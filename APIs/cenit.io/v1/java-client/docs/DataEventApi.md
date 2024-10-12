# DataEventApi

All URIs are relative to *https://cenit.io/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**setupObserverGet**](DataEventApi.md#setupObserverGet) | **GET** /setup/observer/ | Returns a list of events |
| [**setupObserverIdDelete**](DataEventApi.md#setupObserverIdDelete) | **DELETE** /setup/observer/{id} | Delete an event |
| [**setupObserverIdGet**](DataEventApi.md#setupObserverIdGet) | **GET** /setup/observer/{id} | Retrieve an existing event |
| [**setupObserverPost**](DataEventApi.md#setupObserverPost) | **POST** /setup/observer/ | Create or update an event |


<a id="setupObserverGet"></a>
# **setupObserverGet**
> List&lt;Observer&gt; setupObserverGet()

Returns a list of events

Returns a list of events you&#39;ve previously created. The events are returned in sorted order, with the most recent event appearing first.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataEventApi;

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

    DataEventApi apiInstance = new DataEventApi(defaultClient);
    try {
      List<Observer> result = apiInstance.setupObserverGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataEventApi#setupObserverGet");
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

[**List&lt;Observer&gt;**](Observer.md)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="setupObserverIdDelete"></a>
# **setupObserverIdDelete**
> setupObserverIdDelete(id)

Delete an event

Deletes the specified event observer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataEventApi;

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

    DataEventApi apiInstance = new DataEventApi(defaultClient);
    String id = "id_example"; // String | Observer ID
    try {
      apiInstance.setupObserverIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataEventApi#setupObserverIdDelete");
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
| **id** | **String**| Observer ID | |

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

<a id="setupObserverIdGet"></a>
# **setupObserverIdGet**
> Observer setupObserverIdGet(id)

Retrieve an existing event

Retrieves the details of an existing event. You need only supply the unique event identifier that was returned upon event creation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataEventApi;

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

    DataEventApi apiInstance = new DataEventApi(defaultClient);
    String id = "id_example"; // String | Observer ID
    try {
      Observer result = apiInstance.setupObserverIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataEventApi#setupObserverIdGet");
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
| **id** | **String**| Observer ID | |

### Return type

[**Observer**](Observer.md)

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

<a id="setupObserverPost"></a>
# **setupObserverPost**
> Observer setupObserverPost()

Create or update an event

Creates or updates the specified event observer. Any parameters not provided will be left unchanged.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataEventApi;

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

    DataEventApi apiInstance = new DataEventApi(defaultClient);
    try {
      Observer result = apiInstance.setupObserverPost();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataEventApi#setupObserverPost");
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

[**Observer**](Observer.md)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

