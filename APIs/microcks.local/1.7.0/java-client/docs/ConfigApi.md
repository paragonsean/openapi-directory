# ConfigApi

All URIs are relative to *http://microcks.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSecret**](ConfigApi.md#createSecret) | **POST** /secrets | Create a new Secret |
| [**deleteSecret**](ConfigApi.md#deleteSecret) | **DELETE** /secrets/{id} | Delete Secret |
| [**getFeaturesConfiguration**](ConfigApi.md#getFeaturesConfiguration) | **GET** /features/config | Get features configuration |
| [**getKeycloakConfig**](ConfigApi.md#getKeycloakConfig) | **GET** /keycloak/config | Get authentification configuration |
| [**getSecret**](ConfigApi.md#getSecret) | **GET** /secrets/{id} | Get Secret |
| [**getSecrets**](ConfigApi.md#getSecrets) | **GET** /secrets | Get Secrets |
| [**getSecretsCounter**](ConfigApi.md#getSecretsCounter) | **GET** /secrets/count | Get the Secrets counter |
| [**updateSecret**](ConfigApi.md#updateSecret) | **PUT** /secrets/{id} | Update Secret |


<a id="createSecret"></a>
# **createSecret**
> Secret createSecret(secret)

Create a new Secret

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    Secret secret = new Secret(); // Secret | 
    try {
      Secret result = apiInstance.createSecret(secret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#createSecret");
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
| **secret** | [**Secret**](Secret.md)|  | [optional] |

### Return type

[**Secret**](Secret.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created Secret |  -  |

<a id="deleteSecret"></a>
# **deleteSecret**
> deleteSecret(id)

Delete Secret

Delete a Secret

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    String id = "id_example"; // String | Unique identifier of Secret to manage
    try {
      apiInstance.deleteSecret(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#deleteSecret");
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
| **id** | **String**| Unique identifier of Secret to manage | |

### Return type

null (empty response body)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Secret has been deleted |  -  |

<a id="getFeaturesConfiguration"></a>
# **getFeaturesConfiguration**
> getFeaturesConfiguration()

Get features configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    try {
      apiInstance.getFeaturesConfiguration();
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#getFeaturesConfiguration");
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

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get features configuration |  -  |

<a id="getKeycloakConfig"></a>
# **getKeycloakConfig**
> KeycloakConfig getKeycloakConfig()

Get authentification configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    try {
      KeycloakConfig result = apiInstance.getKeycloakConfig();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#getKeycloakConfig");
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

[**KeycloakConfig**](KeycloakConfig.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get current configuration |  -  |

<a id="getSecret"></a>
# **getSecret**
> Secret getSecret(id)

Get Secret

Retrieve a Secret

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    String id = "id_example"; // String | Unique identifier of Secret to manage
    try {
      Secret result = apiInstance.getSecret(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#getSecret");
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
| **id** | **String**| Unique identifier of Secret to manage | |

### Return type

[**Secret**](Secret.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Found Secret |  -  |

<a id="getSecrets"></a>
# **getSecrets**
> List&lt;Secret&gt; getSecrets(page, size)

Get Secrets

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    Integer page = 56; // Integer | Page of Secrets to retrieve (starts at and defaults to 0)
    Integer size = 56; // Integer | Size of a page. Maximum number of Secrets to include in a response (defaults to 20)
    try {
      List<Secret> result = apiInstance.getSecrets(page, size);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#getSecrets");
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
| **page** | **Integer**| Page of Secrets to retrieve (starts at and defaults to 0) | [optional] |
| **size** | **Integer**| Size of a page. Maximum number of Secrets to include in a response (defaults to 20) | [optional] |

### Return type

[**List&lt;Secret&gt;**](Secret.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of found Secrets |  -  |

<a id="getSecretsCounter"></a>
# **getSecretsCounter**
> Counter getSecretsCounter()

Get the Secrets counter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    try {
      Counter result = apiInstance.getSecretsCounter();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#getSecretsCounter");
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

[**Counter**](Counter.md)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Number of Secrets in datastore |  -  |

<a id="updateSecret"></a>
# **updateSecret**
> updateSecret(id)

Update Secret

Update a Secret

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConfigApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://microcks.local");
    
    // Configure OAuth2 access token for authorization: jwt-bearer
    OAuth jwt-bearer = (OAuth) defaultClient.getAuthentication("jwt-bearer");
    jwt-bearer.setAccessToken("YOUR ACCESS TOKEN");

    ConfigApi apiInstance = new ConfigApi(defaultClient);
    String id = "id_example"; // String | Unique identifier of Secret to manage
    try {
      apiInstance.updateSecret(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConfigApi#updateSecret");
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
| **id** | **String**| Unique identifier of Secret to manage | |

### Return type

null (empty response body)

### Authorization

[jwt-bearer](../README.md#jwt-bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated Secret |  -  |

