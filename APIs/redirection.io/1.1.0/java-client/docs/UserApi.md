# UserApi

All URIs are relative to *https://api.redirection.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**confirmNewEmailUserItem**](UserApi.md#confirmNewEmailUserItem) | **GET** /users/{id}/confirm-new-email/{newEmailToken} | Retrieves a User resource. |
| [**deleteUserItem**](UserApi.md#deleteUserItem) | **DELETE** /users/{id} | Removes the User resource. |
| [**editEmailUserItem**](UserApi.md#editEmailUserItem) | **PUT** /users/{id}/edit-email | Replaces the User resource. |
| [**editInfoUserItem**](UserApi.md#editInfoUserItem) | **PUT** /users/{id}/edit-info | Replaces the User resource. |
| [**editPasswordUserItem**](UserApi.md#editPasswordUserItem) | **PUT** /users/{id}/edit-password | Replaces the User resource. |
| [**forgotPasswordUserItem**](UserApi.md#forgotPasswordUserItem) | **PUT** /users/forgot-password/{resetToken} | Replaces the User resource. |
| [**getUserCollection**](UserApi.md#getUserCollection) | **GET** /users | Retrieves the collection of User resources. |
| [**getUserItem**](UserApi.md#getUserItem) | **GET** /users/{id} | Retrieves a User resource. |
| [**postUserCollection**](UserApi.md#postUserCollection) | **POST** /users | Creates a User resource. |


<a id="confirmNewEmailUserItem"></a>
# **confirmNewEmailUserItem**
> UserRead confirmNewEmailUserItem(id, newEmailToken)

Retrieves a User resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    UserApi apiInstance = new UserApi(defaultClient);
    String id = "id_example"; // String | 
    String newEmailToken = "newEmailToken_example"; // String | 
    try {
      UserRead result = apiInstance.confirmNewEmailUserItem(id, newEmailToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#confirmNewEmailUserItem");
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
| **newEmailToken** | **String**|  | |

### Return type

[**UserRead**](UserRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User resource response |  -  |
| **404** | Resource not found |  -  |

<a id="deleteUserItem"></a>
# **deleteUserItem**
> deleteUserItem(id)

Removes the User resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    UserApi apiInstance = new UserApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.deleteUserItem(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#deleteUserItem");
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
| **204** | User resource deleted |  -  |
| **404** | Resource not found |  -  |

<a id="editEmailUserItem"></a>
# **editEmailUserItem**
> UserRead editEmailUserItem(id, user)

Replaces the User resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    UserApi apiInstance = new UserApi(defaultClient);
    String id = "id_example"; // String | 
    UserEditInfo user = new UserEditInfo(); // UserEditInfo | The updated User resource
    try {
      UserRead result = apiInstance.editEmailUserItem(id, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#editEmailUserItem");
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
| **user** | [**UserEditInfo**](UserEditInfo.md)| The updated User resource | [optional] |

### Return type

[**UserRead**](UserRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html, text/csv
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User resource updated |  -  |
| **400** | Invalid input |  -  |
| **404** | Resource not found |  -  |

<a id="editInfoUserItem"></a>
# **editInfoUserItem**
> UserRead editInfoUserItem(id, user)

Replaces the User resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    UserApi apiInstance = new UserApi(defaultClient);
    String id = "id_example"; // String | 
    UserEditInfo user = new UserEditInfo(); // UserEditInfo | The updated User resource
    try {
      UserRead result = apiInstance.editInfoUserItem(id, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#editInfoUserItem");
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
| **user** | [**UserEditInfo**](UserEditInfo.md)| The updated User resource | [optional] |

### Return type

[**UserRead**](UserRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html, text/csv
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User resource updated |  -  |
| **400** | Invalid input |  -  |
| **404** | Resource not found |  -  |

<a id="editPasswordUserItem"></a>
# **editPasswordUserItem**
> UserRead editPasswordUserItem(id, user)

Replaces the User resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    UserApi apiInstance = new UserApi(defaultClient);
    String id = "id_example"; // String | 
    UserEditInfo user = new UserEditInfo(); // UserEditInfo | The updated User resource
    try {
      UserRead result = apiInstance.editPasswordUserItem(id, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#editPasswordUserItem");
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
| **user** | [**UserEditInfo**](UserEditInfo.md)| The updated User resource | [optional] |

### Return type

[**UserRead**](UserRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html, text/csv
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User resource updated |  -  |
| **400** | Invalid input |  -  |
| **404** | Resource not found |  -  |

<a id="forgotPasswordUserItem"></a>
# **forgotPasswordUserItem**
> UserRead forgotPasswordUserItem(resetToken, user)

Replaces the User resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    UserApi apiInstance = new UserApi(defaultClient);
    String resetToken = "resetToken_example"; // String | 
    UserPassword user = new UserPassword(); // UserPassword | The updated User resource
    try {
      UserRead result = apiInstance.forgotPasswordUserItem(resetToken, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#forgotPasswordUserItem");
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
| **resetToken** | **String**|  | |
| **user** | [**UserPassword**](UserPassword.md)| The updated User resource | [optional] |

### Return type

[**UserRead**](UserRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html, text/csv
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User resource updated |  -  |
| **400** | Invalid input |  -  |
| **404** | Resource not found |  -  |

<a id="getUserCollection"></a>
# **getUserCollection**
> List&lt;UserList&gt; getUserCollection(organizationId, search)

Retrieves the collection of User resources.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    UserApi apiInstance = new UserApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String search = "search_example"; // String | 
    try {
      List<UserList> result = apiInstance.getUserCollection(organizationId, search);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#getUserCollection");
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
| **organizationId** | **String**|  | |
| **search** | **String**|  | [optional] |

### Return type

[**List&lt;UserList&gt;**](UserList.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User collection response |  -  |

<a id="getUserItem"></a>
# **getUserItem**
> UserRead getUserItem(id)

Retrieves a User resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    UserApi apiInstance = new UserApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      UserRead result = apiInstance.getUserItem(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#getUserItem");
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

[**UserRead**](UserRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User resource response |  -  |
| **404** | Resource not found |  -  |

<a id="postUserCollection"></a>
# **postUserCollection**
> UserRead postUserCollection(user)

Creates a User resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    UserApi apiInstance = new UserApi(defaultClient);
    UserCreationWrite user = new UserCreationWrite(); // UserCreationWrite | The new User resource
    try {
      UserRead result = apiInstance.postUserCollection(user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#postUserCollection");
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
| **user** | [**UserCreationWrite**](UserCreationWrite.md)| The new User resource | [optional] |

### Return type

[**UserRead**](UserRead.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html, text/csv
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | User resource created |  -  |
| **400** | Invalid input |  -  |
| **404** | Resource not found |  -  |

