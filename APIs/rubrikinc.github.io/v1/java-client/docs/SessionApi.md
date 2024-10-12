# SessionApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSession**](SessionApi.md#createSession) | **POST** /session | Create user session |
| [**deleteSession**](SessionApi.md#deleteSession) | **DELETE** /session/{id} | Delete user session |


<a id="createSession"></a>
# **createSession**
> SessionSummary createSession(organizationId, realm)

Create user session

Open a user session.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    SessionApi apiInstance = new SessionApi(defaultClient);
    String organizationId = "organizationId_example"; // String | Bind the new session to the specified organization. When this parameter is not specified, the session will be bound to an organization chosen according to the user's preferences and authorizations.
    String realm = "realm_example"; // String | Bind the new session to the specified directory. When this parameter is unspecified, the session will be bound to local domain.
    try {
      SessionSummary result = apiInstance.createSession(organizationId, realm);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionApi#createSession");
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
| **organizationId** | **String**| Bind the new session to the specified organization. When this parameter is not specified, the session will be bound to an organization chosen according to the user&#39;s preferences and authorizations. | [optional] |
| **realm** | **String**| Bind the new session to the specified directory. When this parameter is unspecified, the session will be bound to local domain. | [optional] |

### Return type

[**SessionSummary**](SessionSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Session creation successful. |  -  |

<a id="deleteSession"></a>
# **deleteSession**
> deleteSession(id)

Delete user session

Close a user session and invalidate the session token.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    SessionApi apiInstance = new SessionApi(defaultClient);
    String id = "me"; // String | Session ID or  *me* for session of bearer token.
    try {
      apiInstance.deleteSession(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionApi#deleteSession");
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
| **id** | **String**| Session ID or  *me* for session of bearer token. | [default to me] |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Invalidation successful. |  -  |

