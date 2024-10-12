# UserCustomFieldValueApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**usersUserIdUserCustomFieldValueGet**](UserCustomFieldValueApi.md#usersUserIdUserCustomFieldValueGet) | **GET** /users/{user_id}/user_custom_field_value | Get a list of user custom field values |
| [**usersUserIdUserCustomFieldValueUserCustomFieldValueIdGet**](UserCustomFieldValueApi.md#usersUserIdUserCustomFieldValueUserCustomFieldValueIdGet) | **GET** /users/{user_id}/user_custom_field_value/{user_custom_field_value_id} | Get a single record of user custom field value |
| [**usersUserIdUserCustomFieldValueUserCustomFieldValueIdPut**](UserCustomFieldValueApi.md#usersUserIdUserCustomFieldValueUserCustomFieldValueIdPut) | **PUT** /users/{user_id}/user_custom_field_value/{user_custom_field_value_id} | Update a single record of user custom field value |


<a id="usersUserIdUserCustomFieldValueGet"></a>
# **usersUserIdUserCustomFieldValueGet**
> UsersUserIdUserCustomFieldValueGet200Response usersUserIdUserCustomFieldValueGet(userId)

Get a list of user custom field values

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserCustomFieldValueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    UserCustomFieldValueApi apiInstance = new UserCustomFieldValueApi(defaultClient);
    String userId = "userId_example"; // String | Automatically added
    try {
      UsersUserIdUserCustomFieldValueGet200Response result = apiInstance.usersUserIdUserCustomFieldValueGet(userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserCustomFieldValueApi#usersUserIdUserCustomFieldValueGet");
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
| **userId** | **String**| Automatically added | |

### Return type

[**UsersUserIdUserCustomFieldValueGet200Response**](UsersUserIdUserCustomFieldValueGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="usersUserIdUserCustomFieldValueUserCustomFieldValueIdGet"></a>
# **usersUserIdUserCustomFieldValueUserCustomFieldValueIdGet**
> UsersUserIdUserCustomFieldValueUserCustomFieldValueIdGet200Response usersUserIdUserCustomFieldValueUserCustomFieldValueIdGet(userId, userCustomFieldValueId)

Get a single record of user custom field value

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserCustomFieldValueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    UserCustomFieldValueApi apiInstance = new UserCustomFieldValueApi(defaultClient);
    String userId = "userId_example"; // String | Automatically added
    String userCustomFieldValueId = "userCustomFieldValueId_example"; // String | Automatically added
    try {
      UsersUserIdUserCustomFieldValueUserCustomFieldValueIdGet200Response result = apiInstance.usersUserIdUserCustomFieldValueUserCustomFieldValueIdGet(userId, userCustomFieldValueId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserCustomFieldValueApi#usersUserIdUserCustomFieldValueUserCustomFieldValueIdGet");
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
| **userId** | **String**| Automatically added | |
| **userCustomFieldValueId** | **String**| Automatically added | |

### Return type

[**UsersUserIdUserCustomFieldValueUserCustomFieldValueIdGet200Response**](UsersUserIdUserCustomFieldValueUserCustomFieldValueIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="usersUserIdUserCustomFieldValueUserCustomFieldValueIdPut"></a>
# **usersUserIdUserCustomFieldValueUserCustomFieldValueIdPut**
> UsersUserIdUserCustomFieldValueUserCustomFieldValueIdPut200Response usersUserIdUserCustomFieldValueUserCustomFieldValueIdPut(userId, userCustomFieldValueId)

Update a single record of user custom field value

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserCustomFieldValueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    UserCustomFieldValueApi apiInstance = new UserCustomFieldValueApi(defaultClient);
    String userId = "userId_example"; // String | Automatically added
    String userCustomFieldValueId = "userCustomFieldValueId_example"; // String | Automatically added
    try {
      UsersUserIdUserCustomFieldValueUserCustomFieldValueIdPut200Response result = apiInstance.usersUserIdUserCustomFieldValueUserCustomFieldValueIdPut(userId, userCustomFieldValueId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserCustomFieldValueApi#usersUserIdUserCustomFieldValueUserCustomFieldValueIdPut");
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
| **userId** | **String**| Automatically added | |
| **userCustomFieldValueId** | **String**| Automatically added | |

### Return type

[**UsersUserIdUserCustomFieldValueUserCustomFieldValueIdPut200Response**](UsersUserIdUserCustomFieldValueUserCustomFieldValueIdPut200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

