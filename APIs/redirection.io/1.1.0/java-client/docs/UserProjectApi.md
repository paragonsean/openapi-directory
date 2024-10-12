# UserProjectApi

All URIs are relative to *https://api.redirection.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteUserProjectItem**](UserProjectApi.md#deleteUserProjectItem) | **DELETE** /user-projects/{id} | Removes the UserProject resource. |
| [**getUserProjectItem**](UserProjectApi.md#getUserProjectItem) | **GET** /user-projects/{id} | Retrieves a UserProject resource. |
| [**postUserProjectCollection**](UserProjectApi.md#postUserProjectCollection) | **POST** /user-projects | Creates a UserProject resource. |
| [**putUserProjectItem**](UserProjectApi.md#putUserProjectItem) | **PUT** /user-projects/{id} | Replaces the UserProject resource. |


<a id="deleteUserProjectItem"></a>
# **deleteUserProjectItem**
> deleteUserProjectItem(id)

Removes the UserProject resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    UserProjectApi apiInstance = new UserProjectApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.deleteUserProjectItem(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserProjectApi#deleteUserProjectItem");
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
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | UserProject resource deleted |  -  |
| **404** | Resource not found |  -  |

<a id="getUserProjectItem"></a>
# **getUserProjectItem**
> UserProjectRead getUserProjectItem(id)

Retrieves a UserProject resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    UserProjectApi apiInstance = new UserProjectApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      UserProjectRead result = apiInstance.getUserProjectItem(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserProjectApi#getUserProjectItem");
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
| **id** | **String**|  | |

### Return type

[**UserProjectRead**](UserProjectRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | UserProject resource response |  -  |
| **404** | Resource not found |  -  |

<a id="postUserProjectCollection"></a>
# **postUserProjectCollection**
> UserProjectRead postUserProjectCollection(userProject)

Creates a UserProject resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    UserProjectApi apiInstance = new UserProjectApi(defaultClient);
    UserProjectCreationWrite userProject = new UserProjectCreationWrite(); // UserProjectCreationWrite | The new UserProject resource
    try {
      UserProjectRead result = apiInstance.postUserProjectCollection(userProject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserProjectApi#postUserProjectCollection");
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
| **userProject** | [**UserProjectCreationWrite**](UserProjectCreationWrite.md)| The new UserProject resource | [optional] |

### Return type

[**UserProjectRead**](UserProjectRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html, text/csv
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | UserProject resource created |  -  |
| **400** | Invalid input |  -  |
| **404** | Resource not found |  -  |

<a id="putUserProjectItem"></a>
# **putUserProjectItem**
> UserProjectRead putUserProjectItem(id, userProject)

Replaces the UserProject resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserProjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    UserProjectApi apiInstance = new UserProjectApi(defaultClient);
    String id = "id_example"; // String | 
    UserProjectWrite userProject = new UserProjectWrite(); // UserProjectWrite | The updated UserProject resource
    try {
      UserProjectRead result = apiInstance.putUserProjectItem(id, userProject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserProjectApi#putUserProjectItem");
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
| **id** | **String**|  | |
| **userProject** | [**UserProjectWrite**](UserProjectWrite.md)| The updated UserProject resource | [optional] |

### Return type

[**UserProjectRead**](UserProjectRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html, text/csv
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | UserProject resource updated |  -  |
| **400** | Invalid input |  -  |
| **404** | Resource not found |  -  |

