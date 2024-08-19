# WorkspacesApi

All URIs are relative to *https://app.orbit.love/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**workspacesGet**](WorkspacesApi.md#workspacesGet) | **GET** /workspaces | Get all workspaces for the current user |
| [**workspacesWorkspaceSlugGet**](WorkspacesApi.md#workspacesWorkspaceSlugGet) | **GET** /workspaces/{workspace_slug} | Get a workspace |


<a id="workspacesGet"></a>
# **workspacesGet**
> workspacesGet()

Get all workspaces for the current user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.orbit.love/api/v1");
    
    // Configure HTTP bearer authorization: bearer
    HttpBearerAuth bearer = (HttpBearerAuth) defaultClient.getAuthentication("bearer");
    bearer.setBearerToken("BEARER TOKEN");

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    try {
      apiInstance.workspacesGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesGet");
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

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |

<a id="workspacesWorkspaceSlugGet"></a>
# **workspacesWorkspaceSlugGet**
> workspacesWorkspaceSlugGet(workspaceSlug, includeOrbitLevelCounts)

Get a workspace

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.WorkspacesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.orbit.love/api/v1");
    
    // Configure HTTP bearer authorization: bearer
    HttpBearerAuth bearer = (HttpBearerAuth) defaultClient.getAuthentication("bearer");
    bearer.setBearerToken("BEARER TOKEN");

    WorkspacesApi apiInstance = new WorkspacesApi(defaultClient);
    String workspaceSlug = "workspaceSlug_example"; // String | 
    Boolean includeOrbitLevelCounts = true; // Boolean | Include the number of members by Orbit Level in the attributes
    try {
      apiInstance.workspacesWorkspaceSlugGet(workspaceSlug, includeOrbitLevelCounts);
    } catch (ApiException e) {
      System.err.println("Exception when calling WorkspacesApi#workspacesWorkspaceSlugGet");
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
| **workspaceSlug** | **String**|  | |
| **includeOrbitLevelCounts** | **Boolean**| Include the number of members by Orbit Level in the attributes | [optional] |

### Return type

null (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success |  -  |

