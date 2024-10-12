# LookupApi

All URIs are relative to *https://gateway.seven.io/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lookup**](LookupApi.md#lookup) | **POST** /lookup |  |
| [**lookupCnam**](LookupApi.md#lookupCnam) | **POST** /lookup/cnam |  |
| [**lookupFormat**](LookupApi.md#lookupFormat) | **POST** /lookup/format |  |
| [**lookupHlr**](LookupApi.md#lookupHlr) | **POST** /lookup/hlr |  |
| [**lookupMnp**](LookupApi.md#lookupMnp) | **POST** /lookup/mnp |  |


<a id="lookup"></a>
# **lookup**
> lookup(type, number, json)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gateway.seven.io/api");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    LookupApi apiInstance = new LookupApi(defaultClient);
    String type = "type_example"; // String | Allowed values are \"cnam\", \"format\", \"hlr\" and \"mnp\".
    List<String> number = Arrays.asList(); // List<String> | The phone number to look up.
    String json = "json_example"; // String | Determines whether the response shall be returned in JSON format. Does not work with type \"format\".
    try {
      apiInstance.lookup(type, number, json);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#lookup");
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
| **type** | **String**| Allowed values are \&quot;cnam\&quot;, \&quot;format\&quot;, \&quot;hlr\&quot; and \&quot;mnp\&quot;. | |
| **number** | [**List&lt;String&gt;**](String.md)| The phone number to look up. | |
| **json** | **String**| Determines whether the response shall be returned in JSON format. Does not work with type \&quot;format\&quot;. | [optional] |

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="lookupCnam"></a>
# **lookupCnam**
> lookupCnam(number)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gateway.seven.io/api");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    LookupApi apiInstance = new LookupApi(defaultClient);
    List<String> number = Arrays.asList(); // List<String> | The phone number to look up.
    try {
      apiInstance.lookupCnam(number);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#lookupCnam");
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
| **number** | [**List&lt;String&gt;**](String.md)| The phone number to look up. | |

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="lookupFormat"></a>
# **lookupFormat**
> lookupFormat(number)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gateway.seven.io/api");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    LookupApi apiInstance = new LookupApi(defaultClient);
    List<String> number = Arrays.asList(); // List<String> | The phone number to look up.
    try {
      apiInstance.lookupFormat(number);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#lookupFormat");
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
| **number** | [**List&lt;String&gt;**](String.md)| The phone number to look up. | |

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="lookupHlr"></a>
# **lookupHlr**
> lookupHlr(number)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gateway.seven.io/api");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    LookupApi apiInstance = new LookupApi(defaultClient);
    List<String> number = Arrays.asList(); // List<String> | The phone number to look up.
    try {
      apiInstance.lookupHlr(number);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#lookupHlr");
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
| **number** | [**List&lt;String&gt;**](String.md)| The phone number to look up. | |

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="lookupMnp"></a>
# **lookupMnp**
> lookupMnp(number, json)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookupApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gateway.seven.io/api");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    LookupApi apiInstance = new LookupApi(defaultClient);
    List<String> number = Arrays.asList(); // List<String> | The phone number to look up.
    String json = "json_example"; // String | Determines whether the response shall be returned in JSON format.
    try {
      apiInstance.lookupMnp(number, json);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookupApi#lookupMnp");
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
| **number** | [**List&lt;String&gt;**](String.md)| The phone number to look up. | |
| **json** | **String**| Determines whether the response shall be returned in JSON format. | [optional] |

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

