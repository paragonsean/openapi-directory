# ConfigurationApi

All URIs are relative to *https://api.semantria.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addConfigurations**](ConfigurationApi.md#addConfigurations) | **POST** /configurations.{content_type} | Create user configurations |
| [**deleteConfigurations**](ConfigurationApi.md#deleteConfigurations) | **DELETE** /configurations.{content_type} | Remove user configurations |
| [**getConfigurations**](ConfigurationApi.md#getConfigurations) | **GET** /configurations.{content_type} | Retrieve user configurations |
| [**updateConfigurations**](ConfigurationApi.md#updateConfigurations) | **PUT** /configurations.{content_type} | Update user configurations |


<a id="addConfigurations"></a>
# **addConfigurations**
> List&lt;ConfigurationResponseVersion&gt; addConfigurations(contentType, configurations)

Create user configurations

This method creates configurations on Semantria side.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    ConfigurationApi apiInstance = new ConfigurationApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    Object configurations = null; // Object | List of parametrized JSON or XML objects.
    try {
      List<ConfigurationResponseVersion> result = apiInstance.addConfigurations(contentType, configurations);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationApi#addConfigurations");
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
| **contentType** | **String**|  | |
| **configurations** | **Object**| List of parametrized JSON or XML objects. | |

### Return type

[**List&lt;ConfigurationResponseVersion&gt;**](ConfigurationResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **202** | Client request accepted and queued. |  -  |
| **400** | Incoming request body is incorrect. Server responds with details. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **406** | Number of allowed configurations for user subscription is reached. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

<a id="deleteConfigurations"></a>
# **deleteConfigurations**
> deleteConfigurations(contentType, configurationIDs)

Remove user configurations

This method removes certain configuration by unique ID on Semantria side.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    ConfigurationApi apiInstance = new ConfigurationApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    List<String> configurationIDs = Arrays.asList(); // List<String> | List of configuration identifiers.
    try {
      apiInstance.deleteConfigurations(contentType, configurationIDs);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationApi#deleteConfigurations");
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
| **contentType** | **String**|  | |
| **configurationIDs** | [**List&lt;String&gt;**](String.md)| List of configuration identifiers. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **202** | Client request accepted and queued. |  -  |
| **400** | Incoming request body is incorrect. Server responds with details. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **403** | Forbidden. Server responds if client tries to remove primary configuration. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

<a id="getConfigurations"></a>
# **getConfigurations**
> List&lt;ConfigurationResponseVersion&gt; getConfigurations(contentType)

Retrieve user configurations

This method retrieves all user configurations available on Semantria side.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    ConfigurationApi apiInstance = new ConfigurationApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    try {
      List<ConfigurationResponseVersion> result = apiInstance.getConfigurations(contentType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationApi#getConfigurations");
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
| **contentType** | **String**|  | |

### Return type

[**List&lt;ConfigurationResponseVersion&gt;**](ConfigurationResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Client request accepted. Server responds with status object. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

<a id="updateConfigurations"></a>
# **updateConfigurations**
> List&lt;ConfigurationResponseVersion&gt; updateConfigurations(contentType, configurations)

Update user configurations

This method updates specific configurations by unique IDs on Semantria side.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigurationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    ConfigurationApi apiInstance = new ConfigurationApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    Object configurations = null; // Object | List of parametrized JSON or XML objects.
    try {
      List<ConfigurationResponseVersion> result = apiInstance.updateConfigurations(contentType, configurations);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigurationApi#updateConfigurations");
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
| **contentType** | **String**|  | |
| **configurations** | **Object**| List of parametrized JSON or XML objects. | |

### Return type

[**List&lt;ConfigurationResponseVersion&gt;**](ConfigurationResponseVersion.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **202** | Client request accepted and queued. |  -  |
| **400** | Incoming request body is incorrect. Server responds with details. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **406** | Number of allowed configurations for user subscription is reached. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

