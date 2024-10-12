# NamespaceApi

All URIs are relative to *https://cenit.io/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**setupNamespaceGet**](NamespaceApi.md#setupNamespaceGet) | **GET** /setup/namespace/ | Returns a list of namespaces |
| [**setupNamespaceIdDelete**](NamespaceApi.md#setupNamespaceIdDelete) | **DELETE** /setup/namespace/{id} | Delete a namespace |
| [**setupNamespaceIdGet**](NamespaceApi.md#setupNamespaceIdGet) | **GET** /setup/namespace/{id} | Retrieve an existing namespace |
| [**setupNamespacePost**](NamespaceApi.md#setupNamespacePost) | **POST** /setup/namespace/ | Create or update a namespace |


<a id="setupNamespaceGet"></a>
# **setupNamespaceGet**
> List&lt;Namespace&gt; setupNamespaceGet()

Returns a list of namespaces

Returns a list of namespaces you&#39;ve previously created. The namespaces are returned in sorted order, with the most recent namespace appearing first.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamespaceApi;

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

    NamespaceApi apiInstance = new NamespaceApi(defaultClient);
    try {
      List<Namespace> result = apiInstance.setupNamespaceGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamespaceApi#setupNamespaceGet");
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

[**List&lt;Namespace&gt;**](Namespace.md)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="setupNamespaceIdDelete"></a>
# **setupNamespaceIdDelete**
> setupNamespaceIdDelete(id)

Delete a namespace

Deletes the specified namespace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamespaceApi;

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

    NamespaceApi apiInstance = new NamespaceApi(defaultClient);
    String id = "id_example"; // String | Namespace ID.
    try {
      apiInstance.setupNamespaceIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamespaceApi#setupNamespaceIdDelete");
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
| **id** | **String**| Namespace ID. | |

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

<a id="setupNamespaceIdGet"></a>
# **setupNamespaceIdGet**
> Namespace setupNamespaceIdGet(id)

Retrieve an existing namespace

Retrieves the details of an existing namespace. You need only supply the unique webhook namespace that was returned upon namespace creation.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamespaceApi;

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

    NamespaceApi apiInstance = new NamespaceApi(defaultClient);
    String id = "id_example"; // String | Namespace ID.
    try {
      Namespace result = apiInstance.setupNamespaceIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamespaceApi#setupNamespaceIdGet");
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
| **id** | **String**| Namespace ID. | |

### Return type

[**Namespace**](Namespace.md)

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

<a id="setupNamespacePost"></a>
# **setupNamespacePost**
> Namespace setupNamespacePost()

Create or update a namespace

Creates or updates the specified namespace. Any parameters not provided will be left unchanged.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NamespaceApi;

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

    NamespaceApi apiInstance = new NamespaceApi(defaultClient);
    try {
      Namespace result = apiInstance.setupNamespacePost();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NamespaceApi#setupNamespacePost");
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

[**Namespace**](Namespace.md)

### Authorization

[X-User-Access-Key](../README.md#X-User-Access-Key), [X-User-Access-Token](../README.md#X-User-Access-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

