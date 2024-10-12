# ViewsApi

All URIs are relative to */story*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sessionsIdViewsGet**](ViewsApi.md#sessionsIdViewsGet) | **GET** /sessions/{session_id}/views | Views: List Session Views |
| [**sessionsIdViewsPost**](ViewsApi.md#sessionsIdViewsPost) | **POST** /sessions/{session_id}/views | Views: Create A Session View |
| [**viewsIdDelete**](ViewsApi.md#viewsIdDelete) | **DELETE** /views/{view_id} | Views: Delete by Id |
| [**viewsIdGet**](ViewsApi.md#viewsIdGet) | **GET** /views/{view_id} | Views: Get View |


<a id="sessionsIdViewsGet"></a>
# **sessionsIdViewsGet**
> List&lt;View&gt; sessionsIdViewsGet(sessionId)

Views: List Session Views

Get data for all views in a session

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ViewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    ViewsApi apiInstance = new ViewsApi(defaultClient);
    UUID sessionId = UUID.randomUUID(); // UUID | The primary key for a view session
    try {
      List<View> result = apiInstance.sessionsIdViewsGet(sessionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ViewsApi#sessionsIdViewsGet");
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

[**List&lt;View&gt;**](View.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A List of session views |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |

<a id="sessionsIdViewsPost"></a>
# **sessionsIdViewsPost**
> View sessionsIdViewsPost(sessionId, requiredParametersToCreateAView)

Views: Create A Session View

Create a page view object for a viewing session

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ViewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    ViewsApi apiInstance = new ViewsApi(defaultClient);
    UUID sessionId = UUID.randomUUID(); // UUID | The primary key for a view session
    RequiredParametersToCreateAView requiredParametersToCreateAView = new RequiredParametersToCreateAView(); // RequiredParametersToCreateAView | Collaborator user id and permission type
    try {
      View result = apiInstance.sessionsIdViewsPost(sessionId, requiredParametersToCreateAView);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ViewsApi#sessionsIdViewsPost");
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
| **requiredParametersToCreateAView** | [**RequiredParametersToCreateAView**](RequiredParametersToCreateAView.md)| Collaborator user id and permission type | |

### Return type

[**View**](View.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A new view object |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |

<a id="viewsIdDelete"></a>
# **viewsIdDelete**
> viewsIdDelete(viewId)

Views: Delete by Id

Remove a view and dependant data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ViewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    ViewsApi apiInstance = new ViewsApi(defaultClient);
    UUID viewId = UUID.randomUUID(); // UUID | The primary key for a page view within a session
    try {
      apiInstance.viewsIdDelete(viewId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ViewsApi#viewsIdDelete");
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
| **viewId** | **UUID**| The primary key for a page view within a session | |

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

<a id="viewsIdGet"></a>
# **viewsIdGet**
> View viewsIdGet(viewId)

Views: Get View

Get view meta data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ViewsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    ViewsApi apiInstance = new ViewsApi(defaultClient);
    UUID viewId = UUID.randomUUID(); // UUID | The primary key for a page view within a session
    try {
      View result = apiInstance.viewsIdGet(viewId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ViewsApi#viewsIdGet");
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
| **viewId** | **UUID**| The primary key for a page view within a session | |

### Return type

[**View**](View.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A List of session views |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |

