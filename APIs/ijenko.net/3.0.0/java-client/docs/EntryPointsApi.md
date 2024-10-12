# EntryPointsApi

All URIs are relative to *https://ioe2api.ijenko.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**authAccountLogin_0**](EntryPointsApi.md#authAccountLogin_0) | **POST** /auth/login | Get a token using login+password |
| [**meGet**](EntryPointsApi.md#meGet) | **GET** /me | Information about the User |
| [**mePatch**](EntryPointsApi.md#mePatch) | **PATCH** /me | Update User information |
| [**mePlaces**](EntryPointsApi.md#mePlaces) | **GET** /places | List accessible Places |


<a id="authAccountLogin_0"></a>
# **authAccountLogin_0**
> AuthTokens authAccountLogin_0(loginInfo)

Get a token using login+password

Get an access+refresh tokens pair from login and password information.  The *access token* obtained with this request can then be used in an &#x60;Access-Token&#x60; HTTP header or in a &#x60;token&#x60; URL query parameter in requests that require authentication.  The *refresh token* can be used with &#x60;/auth/refresh&#x60; when the *access token* expires to retrieve a new *access token*. The lifetime of the refresh token is the maximum lifetime of this authentication request.  The default lifetime of the *refresh token* is defined by the &#x60;appId&#x60; used. The &#x60;ttl&#x60; input parameter allows to request a *refresh token* with a shorter lifetime.  To implement *logout*, use &#x60;/auth/revoke&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntryPointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");

    EntryPointsApi apiInstance = new EntryPointsApi(defaultClient);
    AuthLogin loginInfo = new AuthLogin(); // AuthLogin | Login information.
    try {
      AuthTokens result = apiInstance.authAccountLogin_0(loginInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntryPointsApi#authAccountLogin_0");
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
| **loginInfo** | [**AuthLogin**](AuthLogin.md)| Login information. | |

### Return type

[**AuthTokens**](AuthTokens.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Login successful. The access token is given to use the API. The refresh token must be stored in a safe place. |  -  |
| **401** | Authentication failure. |  -  |
| **0** | Other error. |  -  |

<a id="meGet"></a>
# **meGet**
> UserMe meGet()

Information about the User

Get information on the authenticated *User* who does the request.  The *login* property is returned only if the *User* is the administrator of the *Account*. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntryPointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    EntryPointsApi apiInstance = new EntryPointsApi(defaultClient);
    try {
      UserMe result = apiInstance.meGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntryPointsApi#meGet");
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

[**UserMe**](UserMe.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="mePatch"></a>
# **mePatch**
> mePatch(userPatch)

Update User information

Update *User* information (locale). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntryPointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    EntryPointsApi apiInstance = new EntryPointsApi(defaultClient);
    UserMePatch userPatch = new UserMePatch(); // UserMePatch | Updated user info.
    try {
      apiInstance.mePatch(userPatch);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntryPointsApi#mePatch");
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
| **userPatch** | [**UserMePatch**](UserMePatch.md)| Updated user info. | |

### Return type

null (empty response body)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Modification successful. |  -  |
| **304** | Successful, but nothing changed. |  -  |
| **0** | Other error. |  -  |

<a id="mePlaces"></a>
# **mePlaces**
> Set&lt;PlaceItem&gt; mePlaces(embedMetadata)

List accessible Places

List the *Places* to which the *Token* has access.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntryPointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ioe2api.ijenko.net");
    
    // Configure API key authorization: Token in query
    ApiKeyAuth Token in query = (ApiKeyAuth) defaultClient.getAuthentication("Token in query");
    Token in query.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in query.setApiKeyPrefix("Token");

    // Configure API key authorization: Token in Access-Token header
    ApiKeyAuth Token in Access-Token header = (ApiKeyAuth) defaultClient.getAuthentication("Token in Access-Token header");
    Token in Access-Token header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token in Access-Token header.setApiKeyPrefix("Token");

    EntryPointsApi apiInstance = new EntryPointsApi(defaultClient);
    List<String> embedMetadata = Arrays.asList(); // List<String> | Request to include the given keys of metadata in the response. If a key doesn't exist on the resource it is ignored. **Note:** This only applies to the top level resources. 
    try {
      Set<PlaceItem> result = apiInstance.mePlaces(embedMetadata);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntryPointsApi#mePlaces");
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
| **embedMetadata** | [**List&lt;String&gt;**](String.md)| Request to include the given keys of metadata in the response. If a key doesn&#39;t exist on the resource it is ignored. **Note:** This only applies to the top level resources.  | [optional] |

### Return type

[**Set&lt;PlaceItem&gt;**](PlaceItem.md)

### Authorization

[Token in query](../README.md#Token in query), [Token in Access-Token header](../README.md#Token in Access-Token header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

