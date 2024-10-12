# ProjectStatusesApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**projectStatusesBulkDeleteDelete**](ProjectStatusesApi.md#projectStatusesBulkDeleteDelete) | **DELETE** /project_statuses/bulkDelete | Bulk delete project statuses |
| [**projectStatusesGet**](ProjectStatusesApi.md#projectStatusesGet) | **GET** /project_statuses | Get list of project statuses |
| [**projectStatusesPost**](ProjectStatusesApi.md#projectStatusesPost) | **POST** /project_statuses | Create a new project status |
| [**projectStatusesProjectStatusIdDelete**](ProjectStatusesApi.md#projectStatusesProjectStatusIdDelete) | **DELETE** /project_statuses/{project_status_id} | Delete a project status |
| [**projectStatusesProjectStatusIdGet**](ProjectStatusesApi.md#projectStatusesProjectStatusIdGet) | **GET** /project_statuses/{project_status_id} | Get a single project status |
| [**projectStatusesProjectStatusIdPut**](ProjectStatusesApi.md#projectStatusesProjectStatusIdPut) | **PUT** /project_statuses/{project_status_id} | Edit a project status |
| [**projectsHasProjectsWithCustomStatusesGet**](ProjectStatusesApi.md#projectsHasProjectsWithCustomStatusesGet) | **GET** /projects/has_projects_with_custom_statuses | Check if the company has projects with custom statuses |


<a id="projectStatusesBulkDeleteDelete"></a>
# **projectStatusesBulkDeleteDelete**
> EmptySuccessResponse projectStatusesBulkDeleteDelete(bulkActionRequestBody)

Bulk delete project statuses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");

    ProjectStatusesApi apiInstance = new ProjectStatusesApi(defaultClient);
    BulkActionRequestBody bulkActionRequestBody = new BulkActionRequestBody(); // BulkActionRequestBody | Project statuses ids
    try {
      EmptySuccessResponse result = apiInstance.projectStatusesBulkDeleteDelete(bulkActionRequestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectStatusesApi#projectStatusesBulkDeleteDelete");
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
| **bulkActionRequestBody** | [**BulkActionRequestBody**](BulkActionRequestBody.md)| Project statuses ids | |

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |

<a id="projectStatusesGet"></a>
# **projectStatusesGet**
> ProjectStatusesGet200Response projectStatusesGet()

Get list of project statuses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    ProjectStatusesApi apiInstance = new ProjectStatusesApi(defaultClient);
    try {
      ProjectStatusesGet200Response result = apiInstance.projectStatusesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectStatusesApi#projectStatusesGet");
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

[**ProjectStatusesGet200Response**](ProjectStatusesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="projectStatusesPost"></a>
# **projectStatusesPost**
> CreateSuccessResponse projectStatusesPost(projectStatusesPostRequest)

Create a new project status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    ProjectStatusesApi apiInstance = new ProjectStatusesApi(defaultClient);
    ProjectStatusesPostRequest projectStatusesPostRequest = new ProjectStatusesPostRequest(); // ProjectStatusesPostRequest | 
    try {
      CreateSuccessResponse result = apiInstance.projectStatusesPost(projectStatusesPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectStatusesApi#projectStatusesPost");
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
| **projectStatusesPostRequest** | [**ProjectStatusesPostRequest**](ProjectStatusesPostRequest.md)|  | |

### Return type

[**CreateSuccessResponse**](CreateSuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | OK |  -  |
| **403** | Forbidden |  -  |
| **422** | Validation error |  -  |

<a id="projectStatusesProjectStatusIdDelete"></a>
# **projectStatusesProjectStatusIdDelete**
> EmptySuccessResponse projectStatusesProjectStatusIdDelete(projectStatusId)

Delete a project status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");

    ProjectStatusesApi apiInstance = new ProjectStatusesApi(defaultClient);
    UUID projectStatusId = UUID.randomUUID(); // UUID | 
    try {
      EmptySuccessResponse result = apiInstance.projectStatusesProjectStatusIdDelete(projectStatusId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectStatusesApi#projectStatusesProjectStatusIdDelete");
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
| **projectStatusId** | **UUID**|  | |

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **403** | Forbidden |  -  |
| **404** | Record not found |  -  |

<a id="projectStatusesProjectStatusIdGet"></a>
# **projectStatusesProjectStatusIdGet**
> ProjectStatusesProjectStatusIdGet200Response projectStatusesProjectStatusIdGet(projectStatusId)

Get a single project status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    ProjectStatusesApi apiInstance = new ProjectStatusesApi(defaultClient);
    String projectStatusId = "projectStatusId_example"; // String | 
    try {
      ProjectStatusesProjectStatusIdGet200Response result = apiInstance.projectStatusesProjectStatusIdGet(projectStatusId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectStatusesApi#projectStatusesProjectStatusIdGet");
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
| **projectStatusId** | **String**|  | |

### Return type

[**ProjectStatusesProjectStatusIdGet200Response**](ProjectStatusesProjectStatusIdGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |

<a id="projectStatusesProjectStatusIdPut"></a>
# **projectStatusesProjectStatusIdPut**
> EmptySuccessResponse projectStatusesProjectStatusIdPut(projectStatusId)

Edit a project status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    ProjectStatusesApi apiInstance = new ProjectStatusesApi(defaultClient);
    String projectStatusId = "projectStatusId_example"; // String | 
    try {
      EmptySuccessResponse result = apiInstance.projectStatusesProjectStatusIdPut(projectStatusId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectStatusesApi#projectStatusesProjectStatusIdPut");
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
| **projectStatusId** | **String**|  | |

### Return type

[**EmptySuccessResponse**](EmptySuccessResponse.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **403** | Forbidden |  -  |
| **404** | Record Not Found |  -  |
| **422** | Validation error |  -  |

<a id="projectsHasProjectsWithCustomStatusesGet"></a>
# **projectsHasProjectsWithCustomStatusesGet**
> ProjectsHasProjectsWithCustomStatusesGet200Response projectsHasProjectsWithCustomStatusesGet()

Check if the company has projects with custom statuses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectStatusesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    ProjectStatusesApi apiInstance = new ProjectStatusesApi(defaultClient);
    try {
      ProjectsHasProjectsWithCustomStatusesGet200Response result = apiInstance.projectsHasProjectsWithCustomStatusesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectStatusesApi#projectsHasProjectsWithCustomStatusesGet");
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

[**ProjectsHasProjectsWithCustomStatusesGet200Response**](ProjectsHasProjectsWithCustomStatusesGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

