# WorkspaceApi

All URIs are relative to *http://airbyte.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createWorkspace**](WorkspaceApi.md#createWorkspace) | **POST** /v1/workspaces/create | Creates a workspace |
| [**deleteWorkspace**](WorkspaceApi.md#deleteWorkspace) | **POST** /v1/workspaces/delete | Deletes a workspace |
| [**getWorkspace**](WorkspaceApi.md#getWorkspace) | **POST** /v1/workspaces/get | Find workspace by ID |
| [**getWorkspaceByConnectionId**](WorkspaceApi.md#getWorkspaceByConnectionId) | **POST** /v1/workspaces/get_by_connection_id | Find workspace by connection id |
| [**getWorkspaceBySlug**](WorkspaceApi.md#getWorkspaceBySlug) | **POST** /v1/workspaces/get_by_slug | Find workspace by slug |
| [**listWorkspaces**](WorkspaceApi.md#listWorkspaces) | **POST** /v1/workspaces/list | List all workspaces registered in the current Airbyte deployment |
| [**updateWorkspace**](WorkspaceApi.md#updateWorkspace) | **POST** /v1/workspaces/update | Update workspace state |
| [**updateWorkspaceFeedback**](WorkspaceApi.md#updateWorkspaceFeedback) | **POST** /v1/workspaces/tag_feedback_status_as_done | Update workspace feedback state |
| [**updateWorkspaceName**](WorkspaceApi.md#updateWorkspaceName) | **POST** /v1/workspaces/update_name | Update workspace name |


<a id="createWorkspace"></a>
# **createWorkspace**
> WorkspaceRead createWorkspace(workspaceCreate)

Creates a workspace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    WorkspaceApi apiInstance = new WorkspaceApi(defaultClient);
    WorkspaceCreate workspaceCreate = new WorkspaceCreate(); // WorkspaceCreate | 
    try {
      WorkspaceRead result = apiInstance.createWorkspace(workspaceCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspaceApi#createWorkspace");
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
| **workspaceCreate** | [**WorkspaceCreate**](WorkspaceCreate.md)|  | |

### Return type

[**WorkspaceRead**](WorkspaceRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **422** | Input failed validation |  -  |

<a id="deleteWorkspace"></a>
# **deleteWorkspace**
> deleteWorkspace(workspaceIdRequestBody)

Deletes a workspace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    WorkspaceApi apiInstance = new WorkspaceApi(defaultClient);
    WorkspaceIdRequestBody workspaceIdRequestBody = new WorkspaceIdRequestBody(); // WorkspaceIdRequestBody | 
    try {
      apiInstance.deleteWorkspace(workspaceIdRequestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspaceApi#deleteWorkspace");
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
| **workspaceIdRequestBody** | [**WorkspaceIdRequestBody**](WorkspaceIdRequestBody.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The resource was deleted successfully. |  -  |
| **404** | Object with given id was not found. |  -  |
| **422** | Input failed validation |  -  |

<a id="getWorkspace"></a>
# **getWorkspace**
> WorkspaceRead getWorkspace(workspaceIdRequestBody)

Find workspace by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    WorkspaceApi apiInstance = new WorkspaceApi(defaultClient);
    WorkspaceIdRequestBody workspaceIdRequestBody = new WorkspaceIdRequestBody(); // WorkspaceIdRequestBody | 
    try {
      WorkspaceRead result = apiInstance.getWorkspace(workspaceIdRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspaceApi#getWorkspace");
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
| **workspaceIdRequestBody** | [**WorkspaceIdRequestBody**](WorkspaceIdRequestBody.md)|  | |

### Return type

[**WorkspaceRead**](WorkspaceRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **404** | Object with given id was not found. |  -  |
| **422** | Input failed validation |  -  |

<a id="getWorkspaceByConnectionId"></a>
# **getWorkspaceByConnectionId**
> WorkspaceRead getWorkspaceByConnectionId(connectionIdRequestBody)

Find workspace by connection id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    WorkspaceApi apiInstance = new WorkspaceApi(defaultClient);
    ConnectionIdRequestBody connectionIdRequestBody = new ConnectionIdRequestBody(); // ConnectionIdRequestBody | 
    try {
      WorkspaceRead result = apiInstance.getWorkspaceByConnectionId(connectionIdRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspaceApi#getWorkspaceByConnectionId");
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
| **connectionIdRequestBody** | [**ConnectionIdRequestBody**](ConnectionIdRequestBody.md)|  | |

### Return type

[**WorkspaceRead**](WorkspaceRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **404** | Object with given id was not found. |  -  |
| **422** | Input failed validation |  -  |

<a id="getWorkspaceBySlug"></a>
# **getWorkspaceBySlug**
> WorkspaceRead getWorkspaceBySlug(slugRequestBody)

Find workspace by slug

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    WorkspaceApi apiInstance = new WorkspaceApi(defaultClient);
    SlugRequestBody slugRequestBody = new SlugRequestBody(); // SlugRequestBody | 
    try {
      WorkspaceRead result = apiInstance.getWorkspaceBySlug(slugRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspaceApi#getWorkspaceBySlug");
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
| **slugRequestBody** | [**SlugRequestBody**](SlugRequestBody.md)|  | |

### Return type

[**WorkspaceRead**](WorkspaceRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **404** | Object with given id was not found. |  -  |
| **422** | Input failed validation |  -  |

<a id="listWorkspaces"></a>
# **listWorkspaces**
> WorkspaceReadList listWorkspaces()

List all workspaces registered in the current Airbyte deployment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    WorkspaceApi apiInstance = new WorkspaceApi(defaultClient);
    try {
      WorkspaceReadList result = apiInstance.listWorkspaces();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspaceApi#listWorkspaces");
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

[**WorkspaceReadList**](WorkspaceReadList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateWorkspace"></a>
# **updateWorkspace**
> WorkspaceRead updateWorkspace(workspaceUpdate)

Update workspace state

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    WorkspaceApi apiInstance = new WorkspaceApi(defaultClient);
    WorkspaceUpdate workspaceUpdate = new WorkspaceUpdate(); // WorkspaceUpdate | 
    try {
      WorkspaceRead result = apiInstance.updateWorkspace(workspaceUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspaceApi#updateWorkspace");
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
| **workspaceUpdate** | [**WorkspaceUpdate**](WorkspaceUpdate.md)|  | |

### Return type

[**WorkspaceRead**](WorkspaceRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **404** | Object with given id was not found. |  -  |
| **422** | Input failed validation |  -  |

<a id="updateWorkspaceFeedback"></a>
# **updateWorkspaceFeedback**
> updateWorkspaceFeedback(workspaceGiveFeedback)

Update workspace feedback state

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    WorkspaceApi apiInstance = new WorkspaceApi(defaultClient);
    WorkspaceGiveFeedback workspaceGiveFeedback = new WorkspaceGiveFeedback(); // WorkspaceGiveFeedback | 
    try {
      apiInstance.updateWorkspaceFeedback(workspaceGiveFeedback);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspaceApi#updateWorkspaceFeedback");
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
| **workspaceGiveFeedback** | [**WorkspaceGiveFeedback**](WorkspaceGiveFeedback.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The feedback state has been properly updated |  -  |
| **404** | Object with given id was not found. |  -  |

<a id="updateWorkspaceName"></a>
# **updateWorkspaceName**
> WorkspaceRead updateWorkspaceName(workspaceUpdateName)

Update workspace name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspaceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://airbyte.local");

    WorkspaceApi apiInstance = new WorkspaceApi(defaultClient);
    WorkspaceUpdateName workspaceUpdateName = new WorkspaceUpdateName(); // WorkspaceUpdateName | 
    try {
      WorkspaceRead result = apiInstance.updateWorkspaceName(workspaceUpdateName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspaceApi#updateWorkspaceName");
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
| **workspaceUpdateName** | [**WorkspaceUpdateName**](WorkspaceUpdateName.md)|  | |

### Return type

[**WorkspaceRead**](WorkspaceRead.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **404** | Object with given id was not found. |  -  |
| **422** | Input failed validation |  -  |

