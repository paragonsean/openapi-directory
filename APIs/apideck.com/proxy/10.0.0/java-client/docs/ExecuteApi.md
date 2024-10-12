# ExecuteApi

All URIs are relative to *https://unify.apideck.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteProxy**](ExecuteApi.md#deleteProxy) | **DELETE** /proxy | DELETE |
| [**getProxy**](ExecuteApi.md#getProxy) | **GET** /proxy | GET |
| [**optionsProxy**](ExecuteApi.md#optionsProxy) | **OPTIONS** /proxy | OPTIONS |
| [**patchProxy**](ExecuteApi.md#patchProxy) | **PATCH** /proxy | PATCH |
| [**postProxy**](ExecuteApi.md#postProxy) | **POST** /proxy | POST |
| [**putProxy**](ExecuteApi.md#putProxy) | **PUT** /proxy | PUT |


<a id="deleteProxy"></a>
# **deleteProxy**
> Object deleteProxy(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization)

DELETE

Proxies a downstream DELETE request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExecuteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://unify.apideck.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ExecuteApi apiInstance = new ExecuteApi(defaultClient);
    String xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
    String xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
    String xApideckServiceId = "close"; // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    String xApideckDownstreamUrl = "https://api.close.com/api/v1/lead"; // String | Downstream URL
    String xApideckDownstreamAuthorization = "Bearer XXXXXXXXXXXXXXXXX"; // String | Downstream authorization header. This will skip the Vault token injection.
    try {
      Object result = apiInstance.deleteProxy(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExecuteApi#deleteProxy");
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
| **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | |
| **xApideckAppId** | **String**| The ID of your Unify application | |
| **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | |
| **xApideckDownstreamUrl** | **String**| Downstream URL | |
| **xApideckDownstreamAuthorization** | **String**| Downstream authorization header. This will skip the Vault token injection. | [optional] |

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ok |  -  |
| **401** | Unauthorized |  -  |
| **0** | Proxy error |  * x-apideck-downstream-error -  <br>  |

<a id="getProxy"></a>
# **getProxy**
> Object getProxy(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization)

GET

Proxies a downstream GET request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExecuteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://unify.apideck.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ExecuteApi apiInstance = new ExecuteApi(defaultClient);
    String xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
    String xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
    String xApideckServiceId = "close"; // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    String xApideckDownstreamUrl = "https://api.close.com/api/v1/lead"; // String | Downstream URL
    String xApideckDownstreamAuthorization = "Bearer XXXXXXXXXXXXXXXXX"; // String | Downstream authorization header. This will skip the Vault token injection.
    try {
      Object result = apiInstance.getProxy(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExecuteApi#getProxy");
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
| **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | |
| **xApideckAppId** | **String**| The ID of your Unify application | |
| **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | |
| **xApideckDownstreamUrl** | **String**| Downstream URL | |
| **xApideckDownstreamAuthorization** | **String**| Downstream authorization header. This will skip the Vault token injection. | [optional] |

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ok |  -  |
| **401** | Unauthorized |  -  |
| **0** | Proxy error |  * x-apideck-downstream-error -  <br>  |

<a id="optionsProxy"></a>
# **optionsProxy**
> Object optionsProxy(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization)

OPTIONS

Proxies a downstream OPTION request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExecuteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://unify.apideck.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ExecuteApi apiInstance = new ExecuteApi(defaultClient);
    String xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
    String xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
    String xApideckServiceId = "close"; // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    String xApideckDownstreamUrl = "https://api.close.com/api/v1/lead"; // String | Downstream URL
    String xApideckDownstreamAuthorization = "Bearer XXXXXXXXXXXXXXXXX"; // String | Downstream authorization header. This will skip the Vault token injection.
    try {
      Object result = apiInstance.optionsProxy(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExecuteApi#optionsProxy");
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
| **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | |
| **xApideckAppId** | **String**| The ID of your Unify application | |
| **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | |
| **xApideckDownstreamUrl** | **String**| Downstream URL | |
| **xApideckDownstreamAuthorization** | **String**| Downstream authorization header. This will skip the Vault token injection. | [optional] |

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ok |  -  |
| **401** | Unauthorized |  -  |
| **0** | Proxy error |  * x-apideck-downstream-error -  <br>  |

<a id="patchProxy"></a>
# **patchProxy**
> Object patchProxy(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization, postProxyRequest)

PATCH

Proxies a downstream PATCH request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExecuteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://unify.apideck.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ExecuteApi apiInstance = new ExecuteApi(defaultClient);
    String xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
    String xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
    String xApideckServiceId = "close"; // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    String xApideckDownstreamUrl = "https://api.close.com/api/v1/lead"; // String | Downstream URL
    String xApideckDownstreamAuthorization = "Bearer XXXXXXXXXXXXXXXXX"; // String | Downstream authorization header. This will skip the Vault token injection.
    PostProxyRequest postProxyRequest = new PostProxyRequest(); // PostProxyRequest | Depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT.
    try {
      Object result = apiInstance.patchProxy(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization, postProxyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExecuteApi#patchProxy");
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
| **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | |
| **xApideckAppId** | **String**| The ID of your Unify application | |
| **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | |
| **xApideckDownstreamUrl** | **String**| Downstream URL | |
| **xApideckDownstreamAuthorization** | **String**| Downstream authorization header. This will skip the Vault token injection. | [optional] |
| **postProxyRequest** | [**PostProxyRequest**](PostProxyRequest.md)| Depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT. | [optional] |

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ok |  -  |
| **401** | Unauthorized |  -  |
| **0** | Proxy error |  * x-apideck-downstream-error -  <br>  |

<a id="postProxy"></a>
# **postProxy**
> Object postProxy(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization, postProxyRequest)

POST

Proxies a downstream POST request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExecuteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://unify.apideck.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ExecuteApi apiInstance = new ExecuteApi(defaultClient);
    String xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
    String xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
    String xApideckServiceId = "close"; // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    String xApideckDownstreamUrl = "https://api.close.com/api/v1/lead"; // String | Downstream URL
    String xApideckDownstreamAuthorization = "Bearer XXXXXXXXXXXXXXXXX"; // String | Downstream authorization header. This will skip the Vault token injection.
    PostProxyRequest postProxyRequest = new PostProxyRequest(); // PostProxyRequest | Depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT.
    try {
      Object result = apiInstance.postProxy(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization, postProxyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExecuteApi#postProxy");
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
| **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | |
| **xApideckAppId** | **String**| The ID of your Unify application | |
| **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | |
| **xApideckDownstreamUrl** | **String**| Downstream URL | |
| **xApideckDownstreamAuthorization** | **String**| Downstream authorization header. This will skip the Vault token injection. | [optional] |
| **postProxyRequest** | [**PostProxyRequest**](PostProxyRequest.md)| Depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT. | [optional] |

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ok |  -  |
| **401** | Unauthorized |  -  |
| **0** | Proxy error |  * x-apideck-downstream-error -  <br>  |

<a id="putProxy"></a>
# **putProxy**
> Object putProxy(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization, putProxyRequest)

PUT

Proxies a downstream PUT request to a service and injects the necessary credentials into a request stored in Vault. This allows you to have an additional security layer and logging without needing to rely on Unify for normalization. **Note**: Vault will proxy all data to the downstream URL and method/verb in the headers. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExecuteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://unify.apideck.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ExecuteApi apiInstance = new ExecuteApi(defaultClient);
    String xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
    String xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
    String xApideckServiceId = "close"; // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    String xApideckDownstreamUrl = "https://api.close.com/api/v1/lead"; // String | Downstream URL
    String xApideckDownstreamAuthorization = "Bearer XXXXXXXXXXXXXXXXX"; // String | Downstream authorization header. This will skip the Vault token injection.
    PutProxyRequest putProxyRequest = new PutProxyRequest(); // PutProxyRequest | Depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT.
    try {
      Object result = apiInstance.putProxy(xApideckConsumerId, xApideckAppId, xApideckServiceId, xApideckDownstreamUrl, xApideckDownstreamAuthorization, putProxyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExecuteApi#putProxy");
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
| **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | |
| **xApideckAppId** | **String**| The ID of your Unify application | |
| **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | |
| **xApideckDownstreamUrl** | **String**| Downstream URL | |
| **xApideckDownstreamAuthorization** | **String**| Downstream authorization header. This will skip the Vault token injection. | [optional] |
| **putProxyRequest** | [**PutProxyRequest**](PutProxyRequest.md)| Depending on the verb/method of the request this will contain the request body you want to POST/PATCH/PUT. | [optional] |

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Ok |  -  |
| **401** | Unauthorized |  -  |
| **0** | Proxy error |  * x-apideck-downstream-error -  <br>  |

