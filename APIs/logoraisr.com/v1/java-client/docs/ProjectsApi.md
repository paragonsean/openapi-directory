# ProjectsApi

All URIs are relative to *https://api.logoraisr.com/rest-v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**projectsCreate**](ProjectsApi.md#projectsCreate) | **POST** /projects/ | Create a new project. |
| [**projectsList**](ProjectsApi.md#projectsList) | **GET** /projects/ | Get user project list. |
| [**projectsRead**](ProjectsApi.md#projectsRead) | **GET** /projects/{project_number}/ | Get project details. |


<a id="projectsCreate"></a>
# **projectsCreate**
> ProjectResponse projectsCreate(projectRequest)

Create a new project.

This POST-Method creates a new project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.logoraisr.com/rest-v1");
    
    // Configure API key authorization: Token
    ApiKeyAuth Token = (ApiKeyAuth) defaultClient.getAuthentication("Token");
    Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    ProjectRequest projectRequest = new ProjectRequest(); // ProjectRequest | 
    try {
      ProjectResponse result = apiInstance.projectsCreate(projectRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsCreate");
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
| **projectRequest** | [**ProjectRequest**](ProjectRequest.md)|  | |

### Return type

[**ProjectResponse**](ProjectResponse.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |
| **400** | BAD REQUEST |  -  |
| **403** | FORBIDDEN |  -  |
| **404** | NOT FOUND |  -  |

<a id="projectsList"></a>
# **projectsList**
> Project projectsList()

Get user project list.

This GET-Method lists the user&#39;s projects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.logoraisr.com/rest-v1");
    
    // Configure API key authorization: Token
    ApiKeyAuth Token = (ApiKeyAuth) defaultClient.getAuthentication("Token");
    Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    try {
      Project result = apiInstance.projectsList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsList");
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

[**Project**](Project.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **403** | FORBIDDEN |  -  |
| **404** | NOT FOUND |  -  |

<a id="projectsRead"></a>
# **projectsRead**
> Project projectsRead(projectNumber)

Get project details.

This GET-Method returns a specific project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.logoraisr.com/rest-v1");
    
    // Configure API key authorization: Token
    ApiKeyAuth Token = (ApiKeyAuth) defaultClient.getAuthentication("Token");
    Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Token.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String projectNumber = "projectNumber_example"; // String | Number of the project.
    try {
      Project result = apiInstance.projectsRead(projectNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsRead");
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
| **projectNumber** | **String**| Number of the project. | |

### Return type

[**Project**](Project.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **403** | FORBIDDEN |  -  |
| **404** | NOT FOUND |  -  |

