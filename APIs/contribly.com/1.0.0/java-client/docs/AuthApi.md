# AuthApi

All URIs are relative to *https://api.contribly.com/1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**credentialsGet**](AuthApi.md#credentialsGet) | **GET** /credentials | List the credentials associated with the authenticated user. |
| [**scopesGet**](AuthApi.md#scopesGet) | **GET** /scopes | Scopes |
| [**verifyPost**](AuthApi.md#verifyPost) | **POST** /verify | Verify token and return details of the owning user |


<a id="credentialsGet"></a>
# **credentialsGet**
> List&lt;Credential&gt; credentialsGet()

List the credentials associated with the authenticated user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    AuthApi apiInstance = new AuthApi(defaultClient);
    try {
      List<Credential> result = apiInstance.credentialsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#credentialsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;Credential&gt;**](Credential.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of credentials associated with this user. |  -  |
| **401** | Not authorised |  -  |

<a id="scopesGet"></a>
# **scopesGet**
> List&lt;String&gt; scopesGet()

Scopes

List available token scopes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    AuthApi apiInstance = new AuthApi(defaultClient);
    try {
      List<String> result = apiInstance.scopesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#scopesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of scopes |  -  |

<a id="verifyPost"></a>
# **verifyPost**
> Authority verifyPost()

Verify token and return details of the owning user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");
    
    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    AuthApi apiInstance = new AuthApi(defaultClient);
    try {
      Authority result = apiInstance.verifyPost();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthApi#verifyPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Authority**](Authority.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Token is valid |  -  |

