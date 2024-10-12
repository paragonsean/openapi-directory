# ProjectsEssentialsApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createProject**](ProjectsEssentialsApi.md#createProject) | **POST** /users/{user_id}/projects | Create a project |
| [**createProjectAlt1**](ProjectsEssentialsApi.md#createProjectAlt1) | **POST** /me/projects | Create a project |
| [**deleteProject**](ProjectsEssentialsApi.md#deleteProject) | **DELETE** /users/{user_id}/projects/{project_id} | Delete a project |
| [**deleteProjectAlt1**](ProjectsEssentialsApi.md#deleteProjectAlt1) | **DELETE** /me/projects/{project_id} | Delete a project |
| [**editProject**](ProjectsEssentialsApi.md#editProject) | **PATCH** /users/{user_id}/projects/{project_id} | Edit a project |
| [**editProjectAlt1**](ProjectsEssentialsApi.md#editProjectAlt1) | **PATCH** /me/projects/{project_id} | Edit a project |
| [**getProject**](ProjectsEssentialsApi.md#getProject) | **GET** /users/{user_id}/projects/{project_id} | Get a specific project |
| [**getProjectAlt1**](ProjectsEssentialsApi.md#getProjectAlt1) | **GET** /me/projects/{project_id} | Get a specific project |
| [**getProjects**](ProjectsEssentialsApi.md#getProjects) | **GET** /users/{user_id}/projects | Get all the projects that belong to a user |
| [**getProjectsAlt1**](ProjectsEssentialsApi.md#getProjectsAlt1) | **GET** /me/projects | Get all the projects that belong to a user |


<a id="createProject"></a>
# **createProject**
> Project createProject(userId, createProjectAlt1Request)

Create a project

This method creates a new project for the specified user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsEssentialsApi apiInstance = new ProjectsEssentialsApi(defaultClient);
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    CreateProjectAlt1Request createProjectAlt1Request = new CreateProjectAlt1Request(); // CreateProjectAlt1Request | 
    try {
      Project result = apiInstance.createProject(userId, createProjectAlt1Request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsEssentialsApi#createProject");
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
| **userId** | **BigDecimal**| The ID of the user. | |
| **createProjectAlt1Request** | [**CreateProjectAlt1Request**](CreateProjectAlt1Request.md)|  | |

### Return type

[**Project**](Project.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The project was created. |  -  |
| **400** | * Error code 2205: The input is empty. * Error code 2204: The input is invalid. |  -  |
| **401** | Error code 8000: The user credentials are invalid. |  -  |
| **403** | Error code 3200: The authenticated user can&#39;t create projects. |  -  |

<a id="createProjectAlt1"></a>
# **createProjectAlt1**
> Project createProjectAlt1(createProjectAlt1Request)

Create a project

This method creates a new project for the specified user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsEssentialsApi apiInstance = new ProjectsEssentialsApi(defaultClient);
    CreateProjectAlt1Request createProjectAlt1Request = new CreateProjectAlt1Request(); // CreateProjectAlt1Request | 
    try {
      Project result = apiInstance.createProjectAlt1(createProjectAlt1Request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsEssentialsApi#createProjectAlt1");
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
| **createProjectAlt1Request** | [**CreateProjectAlt1Request**](CreateProjectAlt1Request.md)|  | |

### Return type

[**Project**](Project.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The project was created. |  -  |
| **400** | * Error code 2205: The input is empty. * Error code 2204: The input is invalid. |  -  |
| **401** | Error code 8000: The user credentials are invalid. |  -  |
| **403** | Error code 3200: The authenticated user can&#39;t create projects. |  -  |

<a id="deleteProject"></a>
# **deleteProject**
> deleteProject(projectId, userId, shouldDeleteClips)

Delete a project

This method deletes a project and optionally also the videos that it contains.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsEssentialsApi apiInstance = new ProjectsEssentialsApi(defaultClient);
    BigDecimal projectId = new BigDecimal("12345"); // BigDecimal | The ID of the project.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    Boolean shouldDeleteClips = true; // Boolean | Whether to delete all the videos in the project along with the project itself.
    try {
      apiInstance.deleteProject(projectId, userId, shouldDeleteClips);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsEssentialsApi#deleteProject");
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
| **projectId** | **BigDecimal**| The ID of the project. | |
| **userId** | **BigDecimal**| The ID of the user. | |
| **shouldDeleteClips** | **Boolean**| Whether to delete all the videos in the project along with the project itself. | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The project was deleted. |  -  |
| **401** | Error code 8000: The user credentials are invalid. |  -  |
| **403** | Error code 3200: The authenticated user can&#39;t delete the project. |  -  |
| **404** | Error code 5000: No such project exists. |  -  |

<a id="deleteProjectAlt1"></a>
# **deleteProjectAlt1**
> deleteProjectAlt1(projectId, shouldDeleteClips)

Delete a project

This method deletes a project and optionally also the videos that it contains.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsEssentialsApi apiInstance = new ProjectsEssentialsApi(defaultClient);
    BigDecimal projectId = new BigDecimal("12345"); // BigDecimal | The ID of the project.
    Boolean shouldDeleteClips = true; // Boolean | Whether to delete all the videos in the project along with the project itself.
    try {
      apiInstance.deleteProjectAlt1(projectId, shouldDeleteClips);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsEssentialsApi#deleteProjectAlt1");
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
| **projectId** | **BigDecimal**| The ID of the project. | |
| **shouldDeleteClips** | **Boolean**| Whether to delete all the videos in the project along with the project itself. | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The project was deleted. |  -  |
| **401** | Error code 8000: The user credentials are invalid. |  -  |
| **403** | Error code 3200: The authenticated user can&#39;t delete the project. |  -  |
| **404** | Error code 5000: No such project exists. |  -  |

<a id="editProject"></a>
# **editProject**
> Project editProject(projectId, userId, createProjectAlt1Request)

Edit a project

This method edits an existing project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsEssentialsApi apiInstance = new ProjectsEssentialsApi(defaultClient);
    BigDecimal projectId = new BigDecimal("12345"); // BigDecimal | The ID of the project.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    CreateProjectAlt1Request createProjectAlt1Request = new CreateProjectAlt1Request(); // CreateProjectAlt1Request | 
    try {
      Project result = apiInstance.editProject(projectId, userId, createProjectAlt1Request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsEssentialsApi#editProject");
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
| **projectId** | **BigDecimal**| The ID of the project. | |
| **userId** | **BigDecimal**| The ID of the user. | |
| **createProjectAlt1Request** | [**CreateProjectAlt1Request**](CreateProjectAlt1Request.md)|  | |

### Return type

[**Project**](Project.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The project was edited. |  -  |
| **400** | * Error code 2204: The input is invalid. * Error code 2205: The input is empty. |  -  |
| **401** | Error code 8000: The user credentials are invalid. |  -  |
| **403** | Error code 3200: The authenticated user can&#39;t edit the project. |  -  |
| **404** | Error code 5000: No such project exists. |  -  |

<a id="editProjectAlt1"></a>
# **editProjectAlt1**
> Project editProjectAlt1(projectId, createProjectAlt1Request)

Edit a project

This method edits an existing project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsEssentialsApi apiInstance = new ProjectsEssentialsApi(defaultClient);
    BigDecimal projectId = new BigDecimal("12345"); // BigDecimal | The ID of the project.
    CreateProjectAlt1Request createProjectAlt1Request = new CreateProjectAlt1Request(); // CreateProjectAlt1Request | 
    try {
      Project result = apiInstance.editProjectAlt1(projectId, createProjectAlt1Request);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsEssentialsApi#editProjectAlt1");
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
| **projectId** | **BigDecimal**| The ID of the project. | |
| **createProjectAlt1Request** | [**CreateProjectAlt1Request**](CreateProjectAlt1Request.md)|  | |

### Return type

[**Project**](Project.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The project was edited. |  -  |
| **400** | * Error code 2204: The input is invalid. * Error code 2205: The input is empty. |  -  |
| **401** | Error code 8000: The user credentials are invalid. |  -  |
| **403** | Error code 3200: The authenticated user can&#39;t edit the project. |  -  |
| **404** | Error code 5000: No such project exists. |  -  |

<a id="getProject"></a>
# **getProject**
> Project getProject(projectId, userId)

Get a specific project

This method gets a single project that belongs to the specified user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsEssentialsApi apiInstance = new ProjectsEssentialsApi(defaultClient);
    BigDecimal projectId = new BigDecimal("12345"); // BigDecimal | The ID of the project.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    try {
      Project result = apiInstance.getProject(projectId, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsEssentialsApi#getProject");
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
| **projectId** | **BigDecimal**| The ID of the project. | |
| **userId** | **BigDecimal**| The ID of the user. | |

### Return type

[**Project**](Project.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The project was returned. |  -  |
| **401** | Error code 8000: The user credentials are invalid. |  -  |
| **404** | Error code 5000: No such project exists. |  -  |

<a id="getProjectAlt1"></a>
# **getProjectAlt1**
> Project getProjectAlt1(projectId)

Get a specific project

This method gets a single project that belongs to the specified user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsEssentialsApi apiInstance = new ProjectsEssentialsApi(defaultClient);
    BigDecimal projectId = new BigDecimal("12345"); // BigDecimal | The ID of the project.
    try {
      Project result = apiInstance.getProjectAlt1(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsEssentialsApi#getProjectAlt1");
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
| **projectId** | **BigDecimal**| The ID of the project. | |

### Return type

[**Project**](Project.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The project was returned. |  -  |
| **401** | Error code 8000: The user credentials are invalid. |  -  |
| **404** | Error code 5000: No such project exists. |  -  |

<a id="getProjects"></a>
# **getProjects**
> List&lt;Project&gt; getProjects(userId, direction, page, perPage, sort)

Get all the projects that belong to a user

This method gets all the projects that belong to the specified user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsEssentialsApi apiInstance = new ProjectsEssentialsApi(defaultClient);
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    String direction = "asc"; // String | The sort direction of the results.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String sort = "date"; // String | The way to sort the results.
    try {
      List<Project> result = apiInstance.getProjects(userId, direction, page, perPage, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsEssentialsApi#getProjects");
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
| **userId** | **BigDecimal**| The ID of the user. | |
| **direction** | **String**| The sort direction of the results. | [optional] [enum: asc, desc] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **sort** | **String**| The way to sort the results. | [optional] [enum: date, default, modified_time, name] |

### Return type

[**List&lt;Project&gt;**](Project.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The projects were returned. |  -  |
| **401** | Error code 8000: The user credentials are invalid. |  -  |

<a id="getProjectsAlt1"></a>
# **getProjectsAlt1**
> List&lt;Project&gt; getProjectsAlt1(direction, page, perPage, sort)

Get all the projects that belong to a user

This method gets all the projects that belong to the specified user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsEssentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsEssentialsApi apiInstance = new ProjectsEssentialsApi(defaultClient);
    String direction = "asc"; // String | The sort direction of the results.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String sort = "date"; // String | The way to sort the results.
    try {
      List<Project> result = apiInstance.getProjectsAlt1(direction, page, perPage, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsEssentialsApi#getProjectsAlt1");
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
| **direction** | **String**| The sort direction of the results. | [optional] [enum: asc, desc] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **sort** | **String**| The way to sort the results. | [optional] [enum: date, default, modified_time, name] |

### Return type

[**List&lt;Project&gt;**](Project.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The projects were returned. |  -  |
| **401** | Error code 8000: The user credentials are invalid. |  -  |

