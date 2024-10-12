# RegistriesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createRegistry**](RegistriesApi.md#createRegistry) | **POST** /registries | Add a new registry |
| [**deleteRegistry**](RegistriesApi.md#deleteRegistry) | **DELETE** /registries/{registry} | Delete a registry configuration |
| [**getRegistry**](RegistriesApi.md#getRegistry) | **GET** /registries/{registry} | Get a specific registry configuration |
| [**listRegistries**](RegistriesApi.md#listRegistries) | **GET** /registries | List configured registries |
| [**updateRegistry**](RegistriesApi.md#updateRegistry) | **PUT** /registries/{registry} | Update/replace a registry configuration |


<a id="createRegistry"></a>
# **createRegistry**
> List&lt;RegistryConfiguration&gt; createRegistry(registryConfigurationRequest, validate, xAnchoreAccount)

Add a new registry

Adds a new registry to the system

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RegistriesApi apiInstance = new RegistriesApi(defaultClient);
    RegistryConfigurationRequest registryConfigurationRequest = new RegistryConfigurationRequest(); // RegistryConfigurationRequest | 
    Boolean validate = true; // Boolean | flag to determine whether or not to validate registry/credential at registry add time
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      List<RegistryConfiguration> result = apiInstance.createRegistry(registryConfigurationRequest, validate, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistriesApi#createRegistry");
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
| **registryConfigurationRequest** | [**RegistryConfigurationRequest**](RegistryConfigurationRequest.md)|  | |
| **validate** | **Boolean**| flag to determine whether or not to validate registry/credential at registry add time | [optional] |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**List&lt;RegistryConfiguration&gt;**](RegistryConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Saved registry configuration |  -  |
| **500** | Internal Error |  -  |

<a id="deleteRegistry"></a>
# **deleteRegistry**
> deleteRegistry(registry, xAnchoreAccount)

Delete a registry configuration

Delete a registry configuration record from the system. Does not remove any images.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RegistriesApi apiInstance = new RegistriesApi(defaultClient);
    String registry = "registry_example"; // String | 
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      apiInstance.deleteRegistry(registry, xAnchoreAccount);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistriesApi#deleteRegistry");
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
| **registry** | **String**|  | |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Delete success |  -  |
| **500** | Internal Error |  -  |

<a id="getRegistry"></a>
# **getRegistry**
> List&lt;RegistryConfiguration&gt; getRegistry(registry, xAnchoreAccount)

Get a specific registry configuration

Get information on a specific registry

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RegistriesApi apiInstance = new RegistriesApi(defaultClient);
    String registry = "registry_example"; // String | 
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      List<RegistryConfiguration> result = apiInstance.getRegistry(registry, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistriesApi#getRegistry");
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
| **registry** | **String**|  | |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**List&lt;RegistryConfiguration&gt;**](RegistryConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Registry configuration |  -  |

<a id="listRegistries"></a>
# **listRegistries**
> List&lt;RegistryConfiguration&gt; listRegistries(xAnchoreAccount)

List configured registries

List all configured registries the system can/will watch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RegistriesApi apiInstance = new RegistriesApi(defaultClient);
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      List<RegistryConfiguration> result = apiInstance.listRegistries(xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistriesApi#listRegistries");
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
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**List&lt;RegistryConfiguration&gt;**](RegistryConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Registry listing |  -  |

<a id="updateRegistry"></a>
# **updateRegistry**
> List&lt;RegistryConfiguration&gt; updateRegistry(registry, registryConfigurationRequest, validate, xAnchoreAccount)

Update/replace a registry configuration

Replaces an existing registry record with the given record

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RegistriesApi apiInstance = new RegistriesApi(defaultClient);
    String registry = "registry_example"; // String | 
    RegistryConfigurationRequest registryConfigurationRequest = new RegistryConfigurationRequest(); // RegistryConfigurationRequest | 
    Boolean validate = true; // Boolean | flag to determine whether or not to validate registry/credential at registry update time
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      List<RegistryConfiguration> result = apiInstance.updateRegistry(registry, registryConfigurationRequest, validate, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistriesApi#updateRegistry");
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
| **registry** | **String**|  | |
| **registryConfigurationRequest** | [**RegistryConfigurationRequest**](RegistryConfigurationRequest.md)|  | |
| **validate** | **Boolean**| flag to determine whether or not to validate registry/credential at registry update time | [optional] |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**List&lt;RegistryConfiguration&gt;**](RegistryConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated registry configuration |  -  |
| **500** | Internal Error |  -  |

