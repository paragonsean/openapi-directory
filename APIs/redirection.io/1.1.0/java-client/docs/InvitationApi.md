# InvitationApi

All URIs are relative to *https://api.redirection.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**acceptInvitationItem**](InvitationApi.md#acceptInvitationItem) | **POST** /invitations/accept/{token} | Creates a Invitation resource. |
| [**deleteInvitationItem**](InvitationApi.md#deleteInvitationItem) | **DELETE** /invitations/{id} | Removes the Invitation resource. |
| [**getInvitationCollection**](InvitationApi.md#getInvitationCollection) | **GET** /invitations | Retrieves the collection of Invitation resources. |
| [**getInvitationItem**](InvitationApi.md#getInvitationItem) | **GET** /invitations/{id} | Retrieves a Invitation resource. |
| [**postInvitationCollection**](InvitationApi.md#postInvitationCollection) | **POST** /invitations | Creates a Invitation resource. |


<a id="acceptInvitationItem"></a>
# **acceptInvitationItem**
> InvitationRead acceptInvitationItem(token, invitation)

Creates a Invitation resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvitationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    InvitationApi apiInstance = new InvitationApi(defaultClient);
    String token = "token_example"; // String | The invitation acceptation token
    Invitation invitation = new Invitation(); // Invitation | The new Invitation resource
    try {
      InvitationRead result = apiInstance.acceptInvitationItem(token, invitation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvitationApi#acceptInvitationItem");
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
| **token** | **String**| The invitation acceptation token | |
| **invitation** | [**Invitation**](Invitation.md)| The new Invitation resource | |

### Return type

[**InvitationRead**](InvitationRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html, text/csv
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Invitation resource created |  -  |
| **400** | Invalid input |  -  |
| **404** | Resource not found |  -  |

<a id="deleteInvitationItem"></a>
# **deleteInvitationItem**
> deleteInvitationItem(id)

Removes the Invitation resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvitationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    InvitationApi apiInstance = new InvitationApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.deleteInvitationItem(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvitationApi#deleteInvitationItem");
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
| **204** | Invitation resource deleted |  -  |
| **404** | Resource not found |  -  |

<a id="getInvitationCollection"></a>
# **getInvitationCollection**
> List&lt;InvitationRead&gt; getInvitationCollection(targetId, targetType)

Retrieves the collection of Invitation resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvitationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    InvitationApi apiInstance = new InvitationApi(defaultClient);
    String targetId = "targetId_example"; // String | 
    String targetType = "targetType_example"; // String | 
    try {
      List<InvitationRead> result = apiInstance.getInvitationCollection(targetId, targetType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvitationApi#getInvitationCollection");
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
| **targetId** | **String**|  | |
| **targetType** | **String**|  | |

### Return type

[**List&lt;InvitationRead&gt;**](InvitationRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Invitation collection response |  -  |

<a id="getInvitationItem"></a>
# **getInvitationItem**
> InvitationRead getInvitationItem(id)

Retrieves a Invitation resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvitationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    InvitationApi apiInstance = new InvitationApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      InvitationRead result = apiInstance.getInvitationItem(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvitationApi#getInvitationItem");
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

[**InvitationRead**](InvitationRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Invitation resource response |  -  |
| **404** | Resource not found |  -  |

<a id="postInvitationCollection"></a>
# **postInvitationCollection**
> InvitationRead postInvitationCollection(invitation)

Creates a Invitation resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvitationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    InvitationApi apiInstance = new InvitationApi(defaultClient);
    InvitationWrite invitation = new InvitationWrite(); // InvitationWrite | The new Invitation resource
    try {
      InvitationRead result = apiInstance.postInvitationCollection(invitation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvitationApi#postInvitationCollection");
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
| **invitation** | [**InvitationWrite**](InvitationWrite.md)| The new Invitation resource | [optional] |

### Return type

[**InvitationRead**](InvitationRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html, text/csv
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Invitation resource created |  -  |
| **400** | Invalid input |  -  |
| **404** | Resource not found |  -  |

