# UsersApi

All URIs are relative to *https://api.journy.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteUser**](UsersApi.md#deleteUser) | **DELETE** /users | Delete user |
| [**link**](UsersApi.md#link) | **POST** /link | Link web activity to user |
| [**upsertUser**](UsersApi.md#upsertUser) | **POST** /users/upsert | Create or update user |


<a id="deleteUser"></a>
# **deleteUser**
> DeleteAccount202Response deleteUser(deleteUserRequest)

Delete user

Endpoint to delete a user.

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
    defaultClient.setBasePath("https://api.journy.io");

    UsersApi apiInstance = new UsersApi(defaultClient);
    DeleteUserRequest deleteUserRequest = new DeleteUserRequest(); // DeleteUserRequest | 
    try {
      DeleteAccount202Response result = apiInstance.deleteUser(deleteUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#deleteUser");
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
| **deleteUserRequest** | [**DeleteUserRequest**](DeleteUserRequest.md)|  | |

### Return type

[**DeleteAccount202Response**](DeleteAccount202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Accepted |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **400** | Bad request, some fields or parameters are incorrect |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **401** | No API Key was provided or the key is not authorised to perform the action |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **403** | The API Key provided is currently not enabled |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **429** | Too many API requests were send |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **500** | An unexpected error occurred |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |

<a id="link"></a>
# **link**
> DeleteAccount202Response link(linkRequest)

Link web activity to user

💡 You don&#39;t need to use this endpoint if you use our JavaScript snippet in your application.  This endpoint is used to link web activity to a user in your application. This will help you discover which channels and campaigns work best.  When our JavaScript snippet is embedded on your website, blog or landing pages, a cookie named \&quot;__journey\&quot; will be set.  This will only work if your website and application are under the same top level domain.  Website, blog or landing pages * www.my-domain.tld * blog.my-domain.tld * landing-page.my-domain.tld  Application * app.my-domain.tld  The cookie on my-domain.tld will also be send to your app domain.  You should call this endpoint after the user succesfully logged in (so that you know the user&#39;s ID). Use the value of the cookie as device ID.

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
    defaultClient.setBasePath("https://api.journy.io");

    UsersApi apiInstance = new UsersApi(defaultClient);
    LinkRequest linkRequest = new LinkRequest(); // LinkRequest | 
    try {
      DeleteAccount202Response result = apiInstance.link(linkRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#link");
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
| **linkRequest** | [**LinkRequest**](LinkRequest.md)|  | |

### Return type

[**DeleteAccount202Response**](DeleteAccount202Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Object was created |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **400** | Bad request, some fields or parameters are incorrect |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **401** | No API Key was provided or the key is not authorised to perform the action |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **403** | The API Key provided is currently not enabled |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **429** | Too many API requests were send |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **500** | An unexpected error occurred |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |

<a id="upsertUser"></a>
# **upsertUser**
> UpsertUser201Response upsertUser(upsertUserRequest)

Create or update user

Endpoint to create or update a user.

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
    defaultClient.setBasePath("https://api.journy.io");

    UsersApi apiInstance = new UsersApi(defaultClient);
    UpsertUserRequest upsertUserRequest = new UpsertUserRequest(); // UpsertUserRequest | 
    try {
      UpsertUser201Response result = apiInstance.upsertUser(upsertUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#upsertUser");
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
| **upsertUserRequest** | [**UpsertUserRequest**](UpsertUserRequest.md)|  | |

### Return type

[**UpsertUser201Response**](UpsertUser201Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | User will be created |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **400** | Bad request, some fields or parameters are incorrect |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **401** | No API Key was provided or the key is not authorised to perform the action |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **403** | The API Key provided is currently not enabled |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **429** | Too many API requests were send |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
| **500** | An unexpected error occurred |  * X-RateLimit-Limit - Request limit per minute. <br>  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |

