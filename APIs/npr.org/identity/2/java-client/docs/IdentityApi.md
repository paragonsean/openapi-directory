# IdentityApi

All URIs are relative to *https://identity.api.npr.org*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteUser**](IdentityApi.md#deleteUser) | **DELETE** /v2/user | Delete the user&#39;s account |
| [**getUser**](IdentityApi.md#getUser) | **GET** /v2/user | Get the latest state information about the logged-in user |
| [**inheritFromTempUser**](IdentityApi.md#inheritFromTempUser) | **POST** /v2/user/inherit | Copy listening data from a temporary user account to the logged-in user&#39;s account |
| [**postFollowing**](IdentityApi.md#postFollowing) | **POST** /v2/following | Update the following status of the logged-in user for a particular aggregation |
| [**updateStations**](IdentityApi.md#updateStations) | **PUT** /v2/stations | Update the logged-in user&#39;s favorite station(s) |


<a id="deleteUser"></a>
# **deleteUser**
> UserDocument deleteUser(authorization)

Delete the user&#39;s account

Use with caution as some steps are irreverisble. Initiates the user account deletion process, including removal of all user PII and account access.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://identity.api.npr.org");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    IdentityApi apiInstance = new IdentityApi(defaultClient);
    String authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
    try {
      UserDocument result = apiInstance.deleteUser(authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentityApi#deleteUser");
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
| **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | |

### Return type

[**UserDocument**](UserDocument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.collection.doc+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **401** | The client is not authorized to complete this request. Check to ensure a valid access token was passed in the headers. |  -  |
| **500** | A server error |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **503** | The system is undergoing maintenance and we are unable to fulfill this request. Look for a &#x60;Retry-After&#x60; header to see the predicted time the system will be back up. |  * Retry-After - The predicted time the system will be back up <br>  |

<a id="getUser"></a>
# **getUser**
> UserDocument getUser(authorization)

Get the latest state information about the logged-in user

After a successful login, the client should send a &#x60;GET&#x60; call approximately once an hour to refresh the user data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://identity.api.npr.org");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    IdentityApi apiInstance = new IdentityApi(defaultClient);
    String authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
    try {
      UserDocument result = apiInstance.getUser(authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentityApi#getUser");
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
| **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | |

### Return type

[**UserDocument**](UserDocument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.collection.doc+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **401** | The client is not authorized to complete this request. Check to ensure a valid access token was passed in the headers. |  -  |
| **429** | The client has exceeded the number of daily calls as per their rate limit. For now, this only applies to prototype applications and untrusted clients. Trusted clients will never be rate-limited, nor will any production apps. |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **500** | A server error |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **503** | The system is undergoing maintenance and we are unable to fulfill this request. Look for a &#x60;Retry-After&#x60; header to see the predicted time the system will be back up. |  * Retry-After - The predicted time the system will be back up <br>  |

<a id="inheritFromTempUser"></a>
# **inheritFromTempUser**
> UserDocument inheritFromTempUser(authorization, tempUser)

Copy listening data from a temporary user account to the logged-in user&#39;s account

This can and should only be used by clients who have access to the &#x60;temporary_user&#x60; grant type.     Third-party developers do not have access to this grant type by default, and will not need this endpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://identity.api.npr.org");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    IdentityApi apiInstance = new IdentityApi(defaultClient);
    String authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
    Integer tempUser = 56; // Integer | The temporary user's ID before the user registered or logged in
    try {
      UserDocument result = apiInstance.inheritFromTempUser(authorization, tempUser);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentityApi#inheritFromTempUser");
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
| **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | |
| **tempUser** | **Integer**| The temporary user&#39;s ID before the user registered or logged in | |

### Return type

[**UserDocument**](UserDocument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.collection.doc+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The request was successful |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **400** | A bad request; generally, one or more parameters passed in were incorrect or missing |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **429** | The client has exceeded the number of daily calls as per their rate limit. For now, this only applies to prototype applications and untrusted clients. Trusted clients will never be rate-limited, nor will any production apps. |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **500** | A server error |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **503** | The system is undergoing maintenance and we are unable to fulfill this request. Look for a &#x60;Retry-After&#x60; header to see the predicted time the system will be back up. |  * Retry-After - The predicted time the system will be back up <br>  |

<a id="postFollowing"></a>
# **postFollowing**
> UserDocument postFollowing(authorization, body)

Update the following status of the logged-in user for a particular aggregation

After a successful call, this returns a User document with an updated list of affiliations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://identity.api.npr.org");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    IdentityApi apiInstance = new IdentityApi(defaultClient);
    String authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
    Affiliation body = new Affiliation(); // Affiliation | A JSON-serialized object which contains data about a user affiliation such as the aggregation ID, affiliation rating, aggregation URL, days since last listen, and following status.
    try {
      UserDocument result = apiInstance.postFollowing(authorization, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentityApi#postFollowing");
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
| **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | |
| **body** | [**Affiliation**](Affiliation.md)| A JSON-serialized object which contains data about a user affiliation such as the aggregation ID, affiliation rating, aggregation URL, days since last listen, and following status. | |

### Return type

[**UserDocument**](UserDocument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/vnd.collection.doc+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The request was successful |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **400** | A bad request; generally, one or more parameters passed in were incorrect or missing |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **401** | The client is not authorized to complete this request. Check to ensure a valid access token was passed in the headers. |  -  |
| **429** | The client has exceeded the number of daily calls as per their rate limit. For now, this only applies to prototype applications and untrusted clients. Trusted clients will never be rate-limited, nor will any production apps. |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **500** | A server error |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **503** | The system is undergoing maintenance and we are unable to fulfill this request. Look for a &#x60;Retry-After&#x60; header to see the predicted time the system will be back up. |  * Retry-After - The predicted time the system will be back up <br>  |

<a id="updateStations"></a>
# **updateStations**
> UserDocument updateStations(authorization, body)

Update the logged-in user&#39;s favorite station(s)

Right now, only the primary station can be changed. Previously selected stations will not be deleted, but the new station will be moved to first in the array.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdentityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://identity.api.npr.org");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    IdentityApi apiInstance = new IdentityApi(defaultClient);
    String authorization = "authorization_example"; // String | Your access token from the Authorization Service. Should start with `Bearer`, followed by a space, followed by the token.
    List<Integer> body = Arrays.asList(); // List<Integer> | A JSON-serialized array of station IDs
    try {
      UserDocument result = apiInstance.updateStations(authorization, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdentityApi#updateStations");
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
| **authorization** | **String**| Your access token from the Authorization Service. Should start with &#x60;Bearer&#x60;, followed by a space, followed by the token. | |
| **body** | [**List&lt;Integer&gt;**](Integer.md)| A JSON-serialized array of station IDs | [optional] |

### Return type

[**UserDocument**](UserDocument.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.collection.doc+json
 - **Accept**: application/json, application/vnd.collection.doc+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The request was successful |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **400** | A bad request; generally, one or more parameters passed in were incorrect or missing |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **401** | The client is not authorized to complete this request. Check to ensure a valid access token was passed in the headers. |  -  |
| **429** | The client has exceeded the number of daily calls as per their rate limit. For now, this only applies to prototype applications and untrusted clients. Trusted clients will never be rate-limited, nor will any production apps. |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **500** | A server error |  * X-RateLimit-Remaining - The number of remaining requests in the current period <br>  * X-RateLimit-Reset - The number of seconds left in the current period <br>  * X-RateLimit-Limit - The number of allowed requests in the current period <br>  |
| **503** | The system is undergoing maintenance and we are unable to fulfill this request. Look for a &#x60;Retry-After&#x60; header to see the predicted time the system will be back up. |  * Retry-After - The predicted time the system will be back up <br>  |

