# ProjectsApi

All URIs are relative to *https://api.swaggerhub.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addSpecToProjectV2**](ProjectsApi.md#addSpecToProjectV2) | **PUT** /projects/{owner}/{projectId}/{specType}/{name} | Add an API or domain to a project |
| [**createProject**](ProjectsApi.md#createProject) | **POST** /projects/{owner} | Create a project in an organization |
| [**deleteProjectV2**](ProjectsApi.md#deleteProjectV2) | **DELETE** /projects/{owner}/{projectId} | Delete a project |
| [**getOrgProjectsV2**](ProjectsApi.md#getOrgProjectsV2) | **GET** /projects/{owner} | Get all projects of an organization |
| [**getProjectMembersV2**](ProjectsApi.md#getProjectMembersV2) | **GET** /projects/{owner}/{projectId}/members | Get project members |
| [**getProjectV2**](ProjectsApi.md#getProjectV2) | **GET** /projects/{owner}/{projectId} | Get project information |
| [**getUserProjects**](ProjectsApi.md#getUserProjects) | **GET** /projects | Get all projects that a user has access to |
| [**saveProjectV2**](ProjectsApi.md#saveProjectV2) | **PUT** /projects/{owner}/{projectId} | Update a project |
| [**updateProjectMembersV2**](ProjectsApi.md#updateProjectMembersV2) | **PUT** /projects/{owner}/{projectId}/members | Update a project&#39;s members list |


<a id="addSpecToProjectV2"></a>
# **addSpecToProjectV2**
> addSpecToProjectV2(owner, projectId, specType, name)

Add an API or domain to a project

Use this operation to add a single API or domain to the specified project.  To add multiple APIs or domains at once, use &#x60;PUT /projects/{owner}/{projectId}&#x60;.

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
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String owner = "owner_example"; // String | Organization name (case-sensitive)
    String projectId = "projectId_example"; // String | Project name (case-sensitive)
    String specType = "apis"; // String | Definition type - `apis` or `domains`.
    String name = "name_example"; // String | The name of an API or domain that you want to add to the project. Case-sensitive.
    try {
      apiInstance.addSpecToProjectV2(owner, projectId, specType, name);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#addSpecToProjectV2");
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
| **owner** | **String**| Organization name (case-sensitive) | |
| **projectId** | **String**| Project name (case-sensitive) | |
| **specType** | **String**| Definition type - &#x60;apis&#x60; or &#x60;domains&#x60;. | [enum: apis, domains] |
| **name** | **String**| The name of an API or domain that you want to add to the project. Case-sensitive. | |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The specified API or domain was successfully added to the project |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | The projects feature is not available for the organization&#39;s plan, or the authenticating user does not have permissions to add definitions to this project  |  -  |
| **404** | The specified organization or project name was not found |  -  |
| **409** | The project already contains this API or domain |  -  |

<a id="createProject"></a>
# **createProject**
> createProject(owner, projectRequest)

Create a project in an organization

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
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String owner = "owner_example"; // String | Organization name (case-sensitive)
    Project projectRequest = new Project(); // Project | The project data. Properties that are not provided are set to empty values. 
    try {
      apiInstance.createProject(owner, projectRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#createProject");
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
| **owner** | **String**| Organization name (case-sensitive) | |
| **projectRequest** | [**Project**](Project.md)| The project data. Properties that are not provided are set to empty values.  | |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The project has been created successfully |  -  |
| **400** | Bad request. For example, some of the specified &#x60;apis&#x60; or &#x60;domains&#x60; do not exist in the organization.  |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | Projects are not available in the organization&#39;s plan |  -  |
| **404** | The specified organization was not found |  -  |
| **409** | A project with this name already exists in the organization |  -  |

<a id="deleteProjectV2"></a>
# **deleteProjectV2**
> deleteProjectV2(owner, projectId)

Delete a project

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
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String owner = "owner_example"; // String | Organization name (case-sensitive)
    String projectId = "projectId_example"; // String | Project name (case-sensitive)
    try {
      apiInstance.deleteProjectV2(owner, projectId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteProjectV2");
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
| **owner** | **String**| Organization name (case-sensitive) | |
| **projectId** | **String**| Project name (case-sensitive) | |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The project has been deleted successfully |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | Projects are not available in the organization&#39;s plan, or you are not a member of the specified project. |  -  |
| **404** | The specified organization or project name was not found |  -  |

<a id="getOrgProjectsV2"></a>
# **getOrgProjectsV2**
> ProjectsJson getOrgProjectsV2(owner, nameOnly, page, limit, order)

Get all projects of an organization

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
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String owner = "owner_example"; // String | Organization name (case-sensitive)
    Boolean nameOnly = false; // Boolean | Return the project information excluding APIs and domains
    Integer page = 0; // Integer | Page to return
    Integer limit = 10; // Integer | Number of results per page (1 .. 100)
    String order = "ASC"; // String | Sort order
    try {
      ProjectsJson result = apiInstance.getOrgProjectsV2(owner, nameOnly, page, limit, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getOrgProjectsV2");
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
| **owner** | **String**| Organization name (case-sensitive) | |
| **nameOnly** | **Boolean**| Return the project information excluding APIs and domains | [optional] [default to false] |
| **page** | **Integer**| Page to return | [optional] [default to 0] |
| **limit** | **Integer**| Number of results per page (1 .. 100) | [optional] [default to 10] |
| **order** | **String**| Sort order | [optional] [default to ASC] [enum: ASC, DESC] |

### Return type

[**ProjectsJson**](ProjectsJson.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Project belonging to the specified organization |  -  |
| **403** | Projects are not available in the organization&#39;s plan |  -  |
| **404** | The specified organization was not found |  -  |

<a id="getProjectMembersV2"></a>
# **getProjectMembersV2**
> ProjectMemberList getProjectMembersV2(owner, projectId)

Get project members

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
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String owner = "owner_example"; // String | Organization name (case-sensitive)
    String projectId = "projectId_example"; // String | Project name (case-sensitive)
    try {
      ProjectMemberList result = apiInstance.getProjectMembersV2(owner, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getProjectMembersV2");
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
| **owner** | **String**| Organization name (case-sensitive) | |
| **projectId** | **String**| Project name (case-sensitive) | |

### Return type

[**ProjectMemberList**](ProjectMemberList.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of project members (users and teams) |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | Projects are not available in the organization&#39;s plan, or you are not a member of the specified project.  |  -  |
| **404** | The specified organization or project name was not found |  -  |

<a id="getProjectV2"></a>
# **getProjectV2**
> Project getProjectV2(owner, projectId)

Get project information

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
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String owner = "owner_example"; // String | Organization name (case-sensitive)
    String projectId = "projectId_example"; // String | Project name (case-sensitive)
    try {
      Project result = apiInstance.getProjectV2(owner, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getProjectV2");
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
| **owner** | **String**| Organization name (case-sensitive) | |
| **projectId** | **String**| Project name (case-sensitive) | |

### Return type

[**Project**](Project.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Project information |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | Projects are not available in the organization&#39;s plan, or you are not a member of the specified project  |  -  |
| **404** | The specified organization or project name was not found |  -  |

<a id="getUserProjects"></a>
# **getUserProjects**
> ProjectsJson getUserProjects(nameOnly, page, limit, sort, order)

Get all projects that a user has access to

Returns all projects that the authenticating user has access to. Organization owners get a list of all projects in owned organizations. Other members get a list of just the projects they are member of.

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
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Boolean nameOnly = false; // Boolean | Return the project information excluding APIs and domains
    Integer page = 0; // Integer | Page to return
    Integer limit = 10; // Integer | Number of results per page (1 .. 100)
    String sort = "NAME"; // String | Sort criteria or result set: * NAME * OWNER 
    String order = "ASC"; // String | Sort order
    try {
      ProjectsJson result = apiInstance.getUserProjects(nameOnly, page, limit, sort, order);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getUserProjects");
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
| **nameOnly** | **Boolean**| Return the project information excluding APIs and domains | [optional] [default to false] |
| **page** | **Integer**| Page to return | [optional] [default to 0] |
| **limit** | **Integer**| Number of results per page (1 .. 100) | [optional] [default to 10] |
| **sort** | **String**| Sort criteria or result set: * NAME * OWNER  | [optional] [default to NAME] [enum: NAME, OWNER] |
| **order** | **String**| Sort order | [optional] [default to ASC] [enum: ASC, DESC] |

### Return type

[**ProjectsJson**](ProjectsJson.md)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All projects accessible to the current user |  -  |
| **401** | Access token is not set or invalid |  -  |

<a id="saveProjectV2"></a>
# **saveProjectV2**
> saveProjectV2(owner, projectId, projectRequest)

Update a project

Use this operation to update an existing project, for example, add or remove APIs, or change the project description.  When updating a project, the &#x60;apis&#x60; and &#x60;domains&#x60; lists _replace_ the existing ones. This means that to add new APIs and domains to a project, you need to send the &#x60;apis&#x60; and &#x60;domains&#x60; lists containing both the existing and new APIs and domains.  To add a single API or domain to a project, you can use &#x60;PUT /projects/{owner}/{projectId}/{specType}/{name}&#x60; instead.

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
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String owner = "owner_example"; // String | Organization name (case-sensitive)
    String projectId = "projectId_example"; // String | Project name (case-sensitive)
    Project projectRequest = new Project(); // Project | The project data. Properties that are not provided are set to empty values. 
    try {
      apiInstance.saveProjectV2(owner, projectId, projectRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#saveProjectV2");
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
| **owner** | **String**| Organization name (case-sensitive) | |
| **projectId** | **String**| Project name (case-sensitive) | |
| **projectRequest** | [**Project**](Project.md)| The project data. Properties that are not provided are set to empty values.  | |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The project has been updated successfully |  -  |
| **400** | Bad request. For example, some of the specified &#x60;apis&#x60; or &#x60;domains&#x60; do not exist in the organization to which the project belongs.  |  -  |
| **401** | Access token is not set or invalid |  -  |
| **403** | Projects are not available in the organization&#39;s plan, or you are not a member of the specified project  |  -  |
| **404** | The specified organization or project name was not found |  -  |

<a id="updateProjectMembersV2"></a>
# **updateProjectMembersV2**
> updateProjectMembersV2(owner, projectId, projectMemberList)

Update a project&#39;s members list

When updating a project, the &#x60;members&#x60; list _replaces_ the existing one. This means that to add new members to a project, you need to send the &#x60;members&#x60; list containing both the existing and new members. 

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
    defaultClient.setBasePath("https://api.swaggerhub.com");
    
    // Configure API key authorization: TokenSecured
    ApiKeyAuth TokenSecured = (ApiKeyAuth) defaultClient.getAuthentication("TokenSecured");
    TokenSecured.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //TokenSecured.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String owner = "owner_example"; // String | Organization name (case-sensitive)
    String projectId = "projectId_example"; // String | Project name (case-sensitive)
    ProjectMemberList projectMemberList = new ProjectMemberList(); // ProjectMemberList | A list of users and teams to add to the project
    try {
      apiInstance.updateProjectMembersV2(owner, projectId, projectMemberList);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#updateProjectMembersV2");
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
| **owner** | **String**| Organization name (case-sensitive) | |
| **projectId** | **String**| Project name (case-sensitive) | |
| **projectMemberList** | [**ProjectMemberList**](ProjectMemberList.md)| A list of users and teams to add to the project | |

### Return type

null (empty response body)

### Authorization

[TokenSecured](../README.md#TokenSecured)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The project members list has been updated successfully |  -  |
| **403** | Projects are not available in the organization&#39;s plan, or you are not a member of the specified project.  |  -  |
| **404** | The specified organization or project name was not found |  -  |

