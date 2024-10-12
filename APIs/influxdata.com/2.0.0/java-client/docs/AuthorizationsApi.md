# AuthorizationsApi

All URIs are relative to */api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteAuthorizationsID**](AuthorizationsApi.md#deleteAuthorizationsID) | **DELETE** /authorizations/{authID} | Delete an authorization |
| [**getAuthorizations**](AuthorizationsApi.md#getAuthorizations) | **GET** /authorizations | List all authorizations |
| [**getAuthorizationsID**](AuthorizationsApi.md#getAuthorizationsID) | **GET** /authorizations/{authID} | Retrieve an authorization |
| [**patchAuthorizationsID**](AuthorizationsApi.md#patchAuthorizationsID) | **PATCH** /authorizations/{authID} | Update an authorization to be active or inactive |
| [**postAuthorizations**](AuthorizationsApi.md#postAuthorizations) | **POST** /authorizations | Create an authorization |


<a id="deleteAuthorizationsID"></a>
# **deleteAuthorizationsID**
> deleteAuthorizationsID(authID, zapTraceSpan)

Delete an authorization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    AuthorizationsApi apiInstance = new AuthorizationsApi(defaultClient);
    String authID = "authID_example"; // String | The ID of the authorization to delete.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      apiInstance.deleteAuthorizationsID(authID, zapTraceSpan);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorizationsApi#deleteAuthorizationsID");
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
| **authID** | **String**| The ID of the authorization to delete. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Authorization deleted |  -  |
| **0** | Non 2XX error response from server. |  -  |

<a id="getAuthorizations"></a>
# **getAuthorizations**
> Authorizations getAuthorizations(zapTraceSpan, userID, user, orgID, org)

List all authorizations

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    AuthorizationsApi apiInstance = new AuthorizationsApi(defaultClient);
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    String userID = "userID_example"; // String | Only show authorizations that belong to a user ID.
    String user = "user_example"; // String | Only show authorizations that belong to a user name.
    String orgID = "orgID_example"; // String | Only show authorizations that belong to an organization ID.
    String org = "org_example"; // String | Only show authorizations that belong to a organization name.
    try {
      Authorizations result = apiInstance.getAuthorizations(zapTraceSpan, userID, user, orgID, org);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorizationsApi#getAuthorizations");
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
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |
| **userID** | **String**| Only show authorizations that belong to a user ID. | [optional] |
| **user** | **String**| Only show authorizations that belong to a user name. | [optional] |
| **orgID** | **String**| Only show authorizations that belong to an organization ID. | [optional] |
| **org** | **String**| Only show authorizations that belong to a organization name. | [optional] |

### Return type

[**Authorizations**](Authorizations.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of authorizations |  -  |
| **0** | Non 2XX error response from server. |  -  |

<a id="getAuthorizationsID"></a>
# **getAuthorizationsID**
> Authorization getAuthorizationsID(authID, zapTraceSpan)

Retrieve an authorization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    AuthorizationsApi apiInstance = new AuthorizationsApi(defaultClient);
    String authID = "authID_example"; // String | The ID of the authorization to get.
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Authorization result = apiInstance.getAuthorizationsID(authID, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorizationsApi#getAuthorizationsID");
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
| **authID** | **String**| The ID of the authorization to get. | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Authorization**](Authorization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Authorization details |  -  |
| **0** | Non 2XX error response from server. |  -  |

<a id="patchAuthorizationsID"></a>
# **patchAuthorizationsID**
> Authorization patchAuthorizationsID(authID, authorizationUpdateRequest, zapTraceSpan)

Update an authorization to be active or inactive

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    AuthorizationsApi apiInstance = new AuthorizationsApi(defaultClient);
    String authID = "authID_example"; // String | The ID of the authorization to update.
    AuthorizationUpdateRequest authorizationUpdateRequest = new AuthorizationUpdateRequest(); // AuthorizationUpdateRequest | Authorization to update
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Authorization result = apiInstance.patchAuthorizationsID(authID, authorizationUpdateRequest, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorizationsApi#patchAuthorizationsID");
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
| **authID** | **String**| The ID of the authorization to update. | |
| **authorizationUpdateRequest** | [**AuthorizationUpdateRequest**](AuthorizationUpdateRequest.md)| Authorization to update | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Authorization**](Authorization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The active or inactie authorization |  -  |
| **0** | Non 2XX error response from server. |  -  |

<a id="postAuthorizations"></a>
# **postAuthorizations**
> Authorization postAuthorizations(authorizationPostRequest, zapTraceSpan)

Create an authorization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthorizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v2");

    AuthorizationsApi apiInstance = new AuthorizationsApi(defaultClient);
    AuthorizationPostRequest authorizationPostRequest = new AuthorizationPostRequest(); // AuthorizationPostRequest | Authorization to create
    String zapTraceSpan = "{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}"; // String | OpenTracing span context
    try {
      Authorization result = apiInstance.postAuthorizations(authorizationPostRequest, zapTraceSpan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthorizationsApi#postAuthorizations");
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
| **authorizationPostRequest** | [**AuthorizationPostRequest**](AuthorizationPostRequest.md)| Authorization to create | |
| **zapTraceSpan** | **String**| OpenTracing span context | [optional] |

### Return type

[**Authorization**](Authorization.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Authorization created |  -  |
| **400** | Non 2XX error response from server. |  -  |
| **0** | Non 2XX error response from server. |  -  |

