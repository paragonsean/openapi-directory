# UsersApi

All URIs are relative to *https://api.victorops.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiPublicV1UserGet**](UsersApi.md#apiPublicV1UserGet) | **GET** /api-public/v1/user | List users |
| [**apiPublicV1UserPost**](UsersApi.md#apiPublicV1UserPost) | **POST** /api-public/v1/user | Add a user |
| [**apiPublicV1UserUserDelete**](UsersApi.md#apiPublicV1UserUserDelete) | **DELETE** /api-public/v1/user/{user} | Remove a user |
| [**apiPublicV1UserUserGet**](UsersApi.md#apiPublicV1UserUserGet) | **GET** /api-public/v1/user/{user} | Retrieve information for a user |
| [**apiPublicV1UserUserPut**](UsersApi.md#apiPublicV1UserUserPut) | **PUT** /api-public/v1/user/{user} | Update a user |
| [**apiPublicV1UserUserTeamsGet**](UsersApi.md#apiPublicV1UserUserTeamsGet) | **GET** /api-public/v1/user/{user}/teams | Retrieve the user&#39;s team membership |


<a id="apiPublicV1UserGet"></a>
# **apiPublicV1UserGet**
> ListUserResponse apiPublicV1UserGet(xVOApiId, xVOApiKey)

List users

Get a list of users for your organization  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    try {
      ListUserResponse result = apiInstance.apiPublicV1UserGet(xVOApiId, xVOApiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#apiPublicV1UserGet");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |

### Return type

[**ListUserResponse**](ListUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of users for your organization |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | User not found |  -  |
| **422** | You have reached your user limit.  |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1UserPost"></a>
# **apiPublicV1UserPost**
> V1User apiPublicV1UserPost(xVOApiId, xVOApiKey, body)

Add a user

Add a user to your organization  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    AddUserPayload body = new AddUserPayload(); // AddUserPayload | 
    try {
      V1User result = apiInstance.apiPublicV1UserPost(xVOApiId, xVOApiKey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#apiPublicV1UserPost");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **body** | [**AddUserPayload**](AddUserPayload.md)|  | |

### Return type

[**V1User**](V1User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Some details about the user that was added |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | User not found |  -  |
| **422** | Username or email is unavailable, or you have reached your user limit.  |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1UserUserDelete"></a>
# **apiPublicV1UserUserDelete**
> apiPublicV1UserUserDelete(xVOApiId, xVOApiKey, user, body)

Remove a user

Remove a user from your organization. If no replacement is specified, an empty JSON payload (\&quot;{}\&quot;) is still required.  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String user = "user_example"; // String | The VictorOps user to be deleted
    DeleteUserPayload body = new DeleteUserPayload(); // DeleteUserPayload | 
    try {
      apiInstance.apiPublicV1UserUserDelete(xVOApiId, xVOApiKey, user, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#apiPublicV1UserUserDelete");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **user** | **String**| The VictorOps user to be deleted | |
| **body** | [**DeleteUserPayload**](DeleteUserPayload.md)|  | |

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
| **200** | User was deleted |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | User not found |  -  |
| **422** | There was a problem with the delete such as a replacement is required or the replacement user was not found.  |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1UserUserGet"></a>
# **apiPublicV1UserUserGet**
> V1User apiPublicV1UserUserGet(xVOApiId, xVOApiKey, user)

Retrieve information for a user

Get the information for the specified user  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String user = "user_example"; // String | The VictorOps user to fetch
    try {
      V1User result = apiInstance.apiPublicV1UserUserGet(xVOApiId, xVOApiKey, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#apiPublicV1UserUserGet");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **user** | **String**| The VictorOps user to fetch | |

### Return type

[**V1User**](V1User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Some details about the user that was added |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | User not found |  -  |
| **422** | Username or email is unavailable, or you have reached your user limit.  |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1UserUserPut"></a>
# **apiPublicV1UserUserPut**
> V1User apiPublicV1UserUserPut(xVOApiId, xVOApiKey, user, body)

Update a user

Update the designated user  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String user = "user_example"; // String | The VictorOps user to be updated
    AddUserPayload body = new AddUserPayload(); // AddUserPayload | 
    try {
      V1User result = apiInstance.apiPublicV1UserUserPut(xVOApiId, xVOApiKey, user, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#apiPublicV1UserUserPut");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **user** | **String**| The VictorOps user to be updated | |
| **body** | [**AddUserPayload**](AddUserPayload.md)|  | |

### Return type

[**V1User**](V1User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Some details about the user that was added |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | User not found |  -  |
| **422** | Username or email is unavailable, or you have reached your user limit.  |  -  |
| **500** | Internal Server Error |  -  |

<a id="apiPublicV1UserUserTeamsGet"></a>
# **apiPublicV1UserUserTeamsGet**
> UserTeamsResponse apiPublicV1UserUserTeamsGet(xVOApiId, xVOApiKey, user)

Retrieve the user&#39;s team membership

This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String user = "user_example"; // String | The VictorOps user
    try {
      UserTeamsResponse result = apiInstance.apiPublicV1UserUserTeamsGet(xVOApiId, xVOApiKey, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#apiPublicV1UserUserTeamsGet");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **user** | **String**| The VictorOps user | |

### Return type

[**UserTeamsResponse**](UserTeamsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Team details |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | User not found |  -  |
| **500** | Internal Server Error |  -  |

