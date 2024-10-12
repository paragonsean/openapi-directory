# UserOrganizationApi

All URIs are relative to *https://api.redirection.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteUserOrganizationItem**](UserOrganizationApi.md#deleteUserOrganizationItem) | **DELETE** /user-organizations/{id} | Removes the UserOrganization resource. |
| [**getUserOrganizationItem**](UserOrganizationApi.md#getUserOrganizationItem) | **GET** /user-organizations/{id} | Retrieves a UserOrganization resource. |
| [**postUserOrganizationCollection**](UserOrganizationApi.md#postUserOrganizationCollection) | **POST** /user-organizations | Creates a UserOrganization resource. |
| [**putUserOrganizationItem**](UserOrganizationApi.md#putUserOrganizationItem) | **PUT** /user-organizations/{id} | Replaces the UserOrganization resource. |


<a id="deleteUserOrganizationItem"></a>
# **deleteUserOrganizationItem**
> deleteUserOrganizationItem(id)

Removes the UserOrganization resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserOrganizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    UserOrganizationApi apiInstance = new UserOrganizationApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.deleteUserOrganizationItem(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserOrganizationApi#deleteUserOrganizationItem");
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
| **204** | UserOrganization resource deleted |  -  |
| **404** | Resource not found |  -  |

<a id="getUserOrganizationItem"></a>
# **getUserOrganizationItem**
> UserOrganizationRead getUserOrganizationItem(id)

Retrieves a UserOrganization resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserOrganizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    UserOrganizationApi apiInstance = new UserOrganizationApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      UserOrganizationRead result = apiInstance.getUserOrganizationItem(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserOrganizationApi#getUserOrganizationItem");
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

[**UserOrganizationRead**](UserOrganizationRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | UserOrganization resource response |  -  |
| **404** | Resource not found |  -  |

<a id="postUserOrganizationCollection"></a>
# **postUserOrganizationCollection**
> UserOrganizationRead postUserOrganizationCollection(userOrganization)

Creates a UserOrganization resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserOrganizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    UserOrganizationApi apiInstance = new UserOrganizationApi(defaultClient);
    UserOrganizationCreationWrite userOrganization = new UserOrganizationCreationWrite(); // UserOrganizationCreationWrite | The new UserOrganization resource
    try {
      UserOrganizationRead result = apiInstance.postUserOrganizationCollection(userOrganization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserOrganizationApi#postUserOrganizationCollection");
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
| **userOrganization** | [**UserOrganizationCreationWrite**](UserOrganizationCreationWrite.md)| The new UserOrganization resource | [optional] |

### Return type

[**UserOrganizationRead**](UserOrganizationRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html, text/csv
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | UserOrganization resource created |  -  |
| **400** | Invalid input |  -  |
| **404** | Resource not found |  -  |

<a id="putUserOrganizationItem"></a>
# **putUserOrganizationItem**
> UserOrganizationRead putUserOrganizationItem(id, userOrganization)

Replaces the UserOrganization resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserOrganizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    UserOrganizationApi apiInstance = new UserOrganizationApi(defaultClient);
    String id = "id_example"; // String | 
    UserOrganizationWrite userOrganization = new UserOrganizationWrite(); // UserOrganizationWrite | The updated UserOrganization resource
    try {
      UserOrganizationRead result = apiInstance.putUserOrganizationItem(id, userOrganization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserOrganizationApi#putUserOrganizationItem");
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
| **userOrganization** | [**UserOrganizationWrite**](UserOrganizationWrite.md)| The updated UserOrganization resource | [optional] |

### Return type

[**UserOrganizationRead**](UserOrganizationRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html, text/csv
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | UserOrganization resource updated |  -  |
| **400** | Invalid input |  -  |
| **404** | Resource not found |  -  |

