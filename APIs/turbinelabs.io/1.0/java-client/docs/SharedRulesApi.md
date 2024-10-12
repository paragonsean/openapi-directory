# SharedRulesApi

All URIs are relative to *https://api.turbinelabs.io/v1.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sharedRulesGet**](SharedRulesApi.md#sharedRulesGet) | **GET** /shared_rules | get shared_rules |
| [**sharedRulesPost**](SharedRulesApi.md#sharedRulesPost) | **POST** /shared_rules | create shared_rules |
| [**sharedRulesSharedRulesKeyGet**](SharedRulesApi.md#sharedRulesSharedRulesKeyGet) | **GET** /shared_rules/{sharedRulesKey} | get shared_rules object |
| [**sharedRulesSharedRulesKeyPut**](SharedRulesApi.md#sharedRulesSharedRulesKeyPut) | **PUT** /shared_rules/{sharedRulesKey} | modify shared_rules object |


<a id="sharedRulesGet"></a>
# **sharedRulesGet**
> MultiSharedRulesResult sharedRulesGet(filters)

get shared_rules

Get a list of shared_rules

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    SharedRulesApi apiInstance = new SharedRulesApi(defaultClient);
    String filters = "filters_example"; // String | A JSON encoded array of SharedRulesFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any SharedRulesFilter will be included. 
    try {
      MultiSharedRulesResult result = apiInstance.sharedRulesGet(filters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedRulesApi#sharedRulesGet");
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
| **filters** | **String**| A JSON encoded array of SharedRulesFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any SharedRulesFilter will be included.  | [optional] |

### Return type

[**MultiSharedRulesResult**](MultiSharedRulesResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | a result containing a list of shared_rules |  -  |
| **0** | Unexpected error |  -  |

<a id="sharedRulesPost"></a>
# **sharedRulesPost**
> SharedRulesResult sharedRulesPost(sharedRules)

create shared_rules

Create a new shared_rules object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    SharedRulesApi apiInstance = new SharedRulesApi(defaultClient);
    SharedRulesCreate sharedRules = new SharedRulesCreate(); // SharedRulesCreate | the shared_rules object to create
    try {
      SharedRulesResult result = apiInstance.sharedRulesPost(sharedRules);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedRulesApi#sharedRulesPost");
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
| **sharedRules** | [**SharedRulesCreate**](SharedRulesCreate.md)| the shared_rules object to create | |

### Return type

[**SharedRulesResult**](SharedRulesResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the newly created shared_rules object |  -  |
| **0** | Unexpected error |  -  |

<a id="sharedRulesSharedRulesKeyGet"></a>
# **sharedRulesSharedRulesKeyGet**
> SharedRulesResult sharedRulesSharedRulesKeyGet(sharedRulesKey)

get shared_rules object

Get details for an existing shared_rules object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    SharedRulesApi apiInstance = new SharedRulesApi(defaultClient);
    String sharedRulesKey = "1c7b1c5e-1a23-4d04-5cb4-eccea4d5994c"; // String | the shared_rules key
    try {
      SharedRulesResult result = apiInstance.sharedRulesSharedRulesKeyGet(sharedRulesKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedRulesApi#sharedRulesSharedRulesKeyGet");
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
| **sharedRulesKey** | **String**| the shared_rules key | |

### Return type

[**SharedRulesResult**](SharedRulesResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | a result containing a single shared_rules object |  -  |
| **0** | Unexpected error |  -  |

<a id="sharedRulesSharedRulesKeyPut"></a>
# **sharedRulesSharedRulesKeyPut**
> SharedRulesResult sharedRulesSharedRulesKeyPut(sharedRulesKey, sharedRules)

modify shared_rules object

Modify an existing shared_rules object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    SharedRulesApi apiInstance = new SharedRulesApi(defaultClient);
    String sharedRulesKey = "1c7b1c5e-1a23-4d04-5cb4-eccea4d5994c"; // String | the shared_rules key
    SharedRules sharedRules = new SharedRules(); // SharedRules | the shared_rules object to modify
    try {
      SharedRulesResult result = apiInstance.sharedRulesSharedRulesKeyPut(sharedRulesKey, sharedRules);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedRulesApi#sharedRulesSharedRulesKeyPut");
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
| **sharedRulesKey** | **String**| the shared_rules key | |
| **sharedRules** | [**SharedRules**](SharedRules.md)| the shared_rules object to modify | |

### Return type

[**SharedRulesResult**](SharedRulesResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A result containing the modified shared_rules object |  -  |
| **0** | Unexpected error |  -  |

