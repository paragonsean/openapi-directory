# StaticApi

All URIs are relative to *https://api.motaword.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getEndpoints**](StaticApi.md#getEndpoints) | **GET** / | Available endpoints |
| [**getFormats**](StaticApi.md#getFormats) | **GET** /formats | List of supported file formats |
| [**getLanguages**](StaticApi.md#getLanguages) | **GET** /languages | List of supported languages |
| [**getSwaggerYaml**](StaticApi.md#getSwaggerYaml) | **GET** /swagger | OpenAPI YAML representation of our API |


<a id="getEndpoints"></a>
# **getEndpoints**
> Object getEndpoints()

Available endpoints

The root endpoint will provide you with an OpenAPI definition of MotaWord API. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StaticApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");

    StaticApi apiInstance = new StaticApi(defaultClient);
    try {
      Object result = apiInstance.getEndpoints();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StaticApi#getEndpoints");
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

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/yaml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | YAML representation of our OpenAPI definition. |  -  |
| **0** | Authentication error |  -  |

<a id="getFormats"></a>
# **getFormats**
> List&lt;Formats&gt; getFormats()

List of supported file formats

Get a list of supported formats for documents, style guides and extensions. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StaticApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");

    StaticApi apiInstance = new StaticApi(defaultClient);
    try {
      List<Formats> result = apiInstance.getFormats();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StaticApi#getFormats");
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

[**List&lt;Formats&gt;**](Formats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of supported formats |  -  |

<a id="getLanguages"></a>
# **getLanguages**
> List&lt;Language&gt; getLanguages()

List of supported languages

Get a list of supported languages

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StaticApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");

    StaticApi apiInstance = new StaticApi(defaultClient);
    try {
      List<Language> result = apiInstance.getLanguages();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StaticApi#getLanguages");
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

[**List&lt;Language&gt;**](Language.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of supported languages |  -  |

<a id="getSwaggerYaml"></a>
# **getSwaggerYaml**
> String getSwaggerYaml()

OpenAPI YAML representation of our API

Get Swagger YAML

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StaticApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.motaword.com");
    
    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: mwoAuth
    OAuth mwoAuth = (OAuth) defaultClient.getAuthentication("mwoAuth");
    mwoAuth.setAccessToken("YOUR ACCESS TOKEN");

    StaticApi apiInstance = new StaticApi(defaultClient);
    try {
      String result = apiInstance.getSwaggerYaml();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StaticApi#getSwaggerYaml");
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

**String**

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Swagger YAML |  -  |

