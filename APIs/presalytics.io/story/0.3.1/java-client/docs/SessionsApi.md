# SessionsApi

All URIs are relative to */story*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sessionIdDelete**](SessionsApi.md#sessionIdDelete) | **DELETE** /sessions/{session_id} | Sessions: Delete by Id |
| [**sessionIdGet**](SessionsApi.md#sessionIdGet) | **GET** /sessions/{session_id} | Sessions: Get |
| [**storyIdSessionPost**](SessionsApi.md#storyIdSessionPost) | **POST** /{id}/sessions | Sessions: Create a Session |
| [**storyIdSessionsGet**](SessionsApi.md#storyIdSessionsGet) | **GET** /{id}/sessions | Sessions: List Story Sessions |


<a id="sessionIdDelete"></a>
# **sessionIdDelete**
> sessionIdDelete(sessionId)

Sessions: Delete by Id

Remove a session and dependant data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    SessionsApi apiInstance = new SessionsApi(defaultClient);
    UUID sessionId = UUID.randomUUID(); // UUID | The primary key for a view session
    try {
      apiInstance.sessionIdDelete(sessionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionsApi#sessionIdDelete");
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
| **sessionId** | **UUID**| The primary key for a view session | |

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
| **204** | Success |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not found |  -  |

<a id="sessionIdGet"></a>
# **sessionIdGet**
> Session sessionIdGet(sessionId, includeRelationships)

Sessions: Get

Get session metadata

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    SessionsApi apiInstance = new SessionsApi(defaultClient);
    UUID sessionId = UUID.randomUUID(); // UUID | The primary key for a view session
    Boolean includeRelationships = true; // Boolean | Indicate whether the returned object should include child relationships
    try {
      Session result = apiInstance.sessionIdGet(sessionId, includeRelationships);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionsApi#sessionIdGet");
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
| **sessionId** | **UUID**| The primary key for a view session | |
| **includeRelationships** | **Boolean**| Indicate whether the returned object should include child relationships | [optional] |

### Return type

[**Session**](Session.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A session object |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |

<a id="storyIdSessionPost"></a>
# **storyIdSessionPost**
> Session storyIdSessionPost(id, createSessionRequest)

Sessions: Create a Session

Create a new session

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    SessionsApi apiInstance = new SessionsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | the id from the story object
    CreateSessionRequest createSessionRequest = new CreateSessionRequest(); // CreateSessionRequest | Collaborator user id and permission type
    try {
      Session result = apiInstance.storyIdSessionPost(id, createSessionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionsApi#storyIdSessionPost");
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
| **id** | **UUID**| the id from the story object | |
| **createSessionRequest** | [**CreateSessionRequest**](CreateSessionRequest.md)| Collaborator user id and permission type | |

### Return type

[**Session**](Session.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A new session object |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |

<a id="storyIdSessionsGet"></a>
# **storyIdSessionsGet**
> List&lt;Session&gt; storyIdSessionsGet(id, includeRelationships)

Sessions: List Story Sessions

Get a list of sessions asscoaited with this story

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    SessionsApi apiInstance = new SessionsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | the id from the story object
    Boolean includeRelationships = true; // Boolean | Indicate whether the returned object should include child relationships
    try {
      List<Session> result = apiInstance.storyIdSessionsGet(id, includeRelationships);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionsApi#storyIdSessionsGet");
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
| **id** | **UUID**| the id from the story object | |
| **includeRelationships** | **Boolean**| Indicate whether the returned object should include child relationships | [optional] |

### Return type

[**List&lt;Session&gt;**](Session.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of session objects |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |

