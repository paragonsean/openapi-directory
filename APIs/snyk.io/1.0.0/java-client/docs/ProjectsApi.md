# ProjectsApi

All URIs are relative to *https://api.snyk.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**activate**](ProjectsApi.md#activate) | **POST** /org/{orgId}/project/{projectId}/activate | Activate |
| [**addATagToAProject**](ProjectsApi.md#addATagToAProject) | **POST** /org/{orgId}/project/{projectId}/tags | Add a tag to a project |
| [**addIgnore**](ProjectsApi.md#addIgnore) | **POST** /org/{orgId}/project/{projectId}/ignore/{issueId} | Add ignore |
| [**applyingAttributes**](ProjectsApi.md#applyingAttributes) | **POST** /org/{orgId}/project/{projectId}/attributes | Applying attributes |
| [**createJiraIssue**](ProjectsApi.md#createJiraIssue) | **POST** /org/{orgId}/project/{projectId}/issue/{issueId}/jira-issue | Create jira issue |
| [**deactivate**](ProjectsApi.md#deactivate) | **POST** /org/{orgId}/project/{projectId}/deactivate | Deactivate |
| [**deleteAProject**](ProjectsApi.md#deleteAProject) | **DELETE** /org/{orgId}/project/{projectId} | Delete a project |
| [**deleteIgnores**](ProjectsApi.md#deleteIgnores) | **DELETE** /org/{orgId}/project/{projectId}/ignore/{issueId} | Delete ignores |
| [**deleteProjectSettings**](ProjectsApi.md#deleteProjectSettings) | **DELETE** /org/{orgId}/project/{projectId}/settings | Delete project settings |
| [**getProjectDependencyGraph**](ProjectsApi.md#getProjectDependencyGraph) | **GET** /org/{orgId}/project/{projectId}/dep-graph | Get Project dependency graph |
| [**listAllAggregatedIssues**](ProjectsApi.md#listAllAggregatedIssues) | **POST** /org/{orgId}/project/{projectId}/aggregated-issues | List all Aggregated issues |
| [**listAllIgnores**](ProjectsApi.md#listAllIgnores) | **GET** /org/{orgId}/project/{projectId}/ignores | List all ignores |
| [**listAllJiraIssues**](ProjectsApi.md#listAllJiraIssues) | **GET** /org/{orgId}/project/{projectId}/jira-issues | List all jira issues |
| [**listAllProjectIssuePaths**](ProjectsApi.md#listAllProjectIssuePaths) | **GET** /org/{orgId}/project/{projectId}/issue/{issueId}/paths | List all project issue paths |
| [**listAllProjectSnapshotAggregatedIssues**](ProjectsApi.md#listAllProjectSnapshotAggregatedIssues) | **POST** /org/{orgId}/project/{projectId}/history/{snapshotId}/aggregated-issues | List all project snapshot aggregated issues |
| [**listAllProjectSnapshotIssuePaths**](ProjectsApi.md#listAllProjectSnapshotIssuePaths) | **GET** /org/{orgId}/project/{projectId}/history/{snapshotId}/issue/{issueId}/paths | List all project snapshot issue paths |
| [**listAllProjectSnapshots**](ProjectsApi.md#listAllProjectSnapshots) | **POST** /org/{orgId}/project/{projectId}/history | List all project snapshots |
| [**listAllProjects**](ProjectsApi.md#listAllProjects) | **POST** /org/{orgId}/projects | List all projects |
| [**listProjectSettings**](ProjectsApi.md#listProjectSettings) | **GET** /org/{orgId}/project/{projectId}/settings | List project settings |
| [**moveProjectToADifferentOrganization**](ProjectsApi.md#moveProjectToADifferentOrganization) | **PUT** /org/{orgId}/project/{projectId}/move | Move project to a different organization |
| [**removeATagFromAProject**](ProjectsApi.md#removeATagFromAProject) | **POST** /org/{orgId}/project/{projectId}/tags/remove | Remove a tag from a project |
| [**replaceIgnores**](ProjectsApi.md#replaceIgnores) | **PUT** /org/{orgId}/project/{projectId}/ignore/{issueId} | Replace ignores |
| [**retrieveASingleProject**](ProjectsApi.md#retrieveASingleProject) | **GET** /org/{orgId}/project/{projectId} | Retrieve a single project |
| [**retrieveIgnore**](ProjectsApi.md#retrieveIgnore) | **GET** /org/{orgId}/project/{projectId}/ignore/{issueId} | Retrieve ignore |
| [**updateAProject**](ProjectsApi.md#updateAProject) | **PUT** /org/{orgId}/project/{projectId} | Update a project |
| [**updateProjectSettings**](ProjectsApi.md#updateProjectSettings) | **PUT** /org/{orgId}/project/{projectId}/settings | Update project settings |


<a id="activate"></a>
# **activate**
> activate(orgId, projectId)

Activate

Activating a project will:  - Add a repository webhook for supported integrations.  - Enable pull request tests for new vulnerabilities.  - Open Fix pull request for newly disclosed vulnerabilities.  - Enable recurring tests, sending email alerts about newly disclosed vulnerabilities.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID the project belongs to. The `API_KEY` must have access to this organization.
    String projectId = "463c1ee5-31bc-428c-b451-b79a3270db08"; // String | The project ID.
    try {
      apiInstance.activate(orgId, projectId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#activate");
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
| **orgId** | **String**| The organization ID the project belongs to. The &#x60;API_KEY&#x60; must have access to this organization. | |
| **projectId** | **String**| The project ID. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="addATagToAProject"></a>
# **addATagToAProject**
> AddATagToAProject200Response addATagToAProject(orgId, projectId, addATagToAProjectRequest)

Add a tag to a project

​

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have access to this organization.
    String projectId = "6d5813be-7e6d-4ab8-80c2-1e3e2a454545"; // String | The project ID to apply the tag to
    AddATagToAProjectRequest addATagToAProjectRequest = new AddATagToAProjectRequest(); // AddATagToAProjectRequest | 
    try {
      AddATagToAProject200Response result = apiInstance.addATagToAProject(orgId, projectId, addATagToAProjectRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#addATagToAProject");
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
| **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. | |
| **projectId** | **String**| The project ID to apply the tag to | |
| **addATagToAProjectRequest** | [**AddATagToAProjectRequest**](AddATagToAProjectRequest.md)|  | [optional] |

### Return type

[**AddATagToAProject200Response**](AddATagToAProject200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="addIgnore"></a>
# **addIgnore**
> Object addIgnore(orgId, projectId, issueId, addIgnoreRequest)

Add ignore



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String orgId = "orgId_example"; // String | Automatically added
    String projectId = "projectId_example"; // String | Automatically added
    String issueId = "issueId_example"; // String | Automatically added
    AddIgnoreRequest addIgnoreRequest = new AddIgnoreRequest(); // AddIgnoreRequest | 
    try {
      Object result = apiInstance.addIgnore(orgId, projectId, issueId, addIgnoreRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#addIgnore");
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
| **orgId** | **String**| Automatically added | |
| **projectId** | **String**| Automatically added | |
| **issueId** | **String**| Automatically added | |
| **addIgnoreRequest** | [**AddIgnoreRequest**](AddIgnoreRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="applyingAttributes"></a>
# **applyingAttributes**
> ApplyingAttributes200Response applyingAttributes(orgId, projectId, applyingAttributesRequest)

Applying attributes

Applies an attribute to the provided project. It is possible to assign multiple values to each attribute, but you can only assign values to one of the predefined attribute categories, using the predefined options for this category. Assigning an attribute requires the caller to be either an Organization Administrator or a Group Administrator. Assigning an attribute will override any existing values that the specific attribute already has set. In order to clear out an attribute value, an empty array can be set.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have access to this organization.
    String projectId = "6d5813be-7e6d-4ab8-80c2-1e3e2a454545"; // String | The project ID to remove a tag from
    ApplyingAttributesRequest applyingAttributesRequest = new ApplyingAttributesRequest(); // ApplyingAttributesRequest | 
    try {
      ApplyingAttributes200Response result = apiInstance.applyingAttributes(orgId, projectId, applyingAttributesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#applyingAttributes");
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
| **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. | |
| **projectId** | **String**| The project ID to remove a tag from | |
| **applyingAttributesRequest** | [**ApplyingAttributesRequest**](ApplyingAttributesRequest.md)|  | [optional] |

### Return type

[**ApplyingAttributes200Response**](ApplyingAttributes200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="createJiraIssue"></a>
# **createJiraIssue**
> CreateJiraIssue200Response createJiraIssue(issueId, orgId, projectId, createJiraIssueRequest)

Create jira issue



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String issueId = "npm:qs:20140806-1"; // String | The issue ID to create Jira issue for.
    String orgId = "orgId_example"; // String | Automatically added
    String projectId = "projectId_example"; // String | Automatically added
    CreateJiraIssueRequest createJiraIssueRequest = new CreateJiraIssueRequest(); // CreateJiraIssueRequest | 
    try {
      CreateJiraIssue200Response result = apiInstance.createJiraIssue(issueId, orgId, projectId, createJiraIssueRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#createJiraIssue");
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
| **issueId** | **String**| The issue ID to create Jira issue for. | |
| **orgId** | **String**| Automatically added | |
| **projectId** | **String**| Automatically added | |
| **createJiraIssueRequest** | [**CreateJiraIssueRequest**](CreateJiraIssueRequest.md)|  | [optional] |

### Return type

[**CreateJiraIssue200Response**](CreateJiraIssue200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="deactivate"></a>
# **deactivate**
> deactivate(orgId, projectId)

Deactivate

Deactivating a project will:  - Disable pull request tests for new vulnerabilities.  - Disable Fix pull request from being opened for newly disclosed vulnerabilities.  - Disable recurring tests - email alerts about newly disclosed vulnerabilities will be turned off.  - If the repository has no other active projects, then remove any webhooks related to the project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID the project belongs to. The `API_KEY` must have access to this organization.
    String projectId = "463c1ee5-31bc-428c-b451-b79a3270db08"; // String | The project ID.
    try {
      apiInstance.deactivate(orgId, projectId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deactivate");
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
| **orgId** | **String**| The organization ID the project belongs to. The &#x60;API_KEY&#x60; must have access to this organization. | |
| **projectId** | **String**| The project ID. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="deleteAProject"></a>
# **deleteAProject**
> deleteAProject(orgId, projectId)

Delete a project



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String orgId = "orgId_example"; // String | Automatically added
    String projectId = "projectId_example"; // String | Automatically added
    try {
      apiInstance.deleteAProject(orgId, projectId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteAProject");
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
| **orgId** | **String**| Automatically added | |
| **projectId** | **String**| Automatically added | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="deleteIgnores"></a>
# **deleteIgnores**
> deleteIgnores(orgId, projectId, issueId)

Delete ignores



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String orgId = "orgId_example"; // String | Automatically added
    String projectId = "projectId_example"; // String | Automatically added
    String issueId = "issueId_example"; // String | Automatically added
    try {
      apiInstance.deleteIgnores(orgId, projectId, issueId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteIgnores");
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
| **orgId** | **String**| Automatically added | |
| **projectId** | **String**| Automatically added | |
| **issueId** | **String**| Automatically added | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="deleteProjectSettings"></a>
# **deleteProjectSettings**
> deleteProjectSettings(orgId, projectId)

Delete project settings

Deleting project settings will set the project to inherit default settings from its integration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String orgId = "orgId_example"; // String | Automatically added
    String projectId = "projectId_example"; // String | Automatically added
    try {
      apiInstance.deleteProjectSettings(orgId, projectId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#deleteProjectSettings");
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
| **orgId** | **String**| Automatically added | |
| **projectId** | **String**| Automatically added | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="getProjectDependencyGraph"></a>
# **getProjectDependencyGraph**
> GetProjectDependencyGraph200Response getProjectDependencyGraph(orgId, projectId)

Get Project dependency graph



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have access to this organization.
    String projectId = "6d5813be-7e6d-4ab8-80c2-1e3e2a454545"; // String | The project ID to return issues for.
    try {
      GetProjectDependencyGraph200Response result = apiInstance.getProjectDependencyGraph(orgId, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#getProjectDependencyGraph");
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
| **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. | |
| **projectId** | **String**| The project ID to return issues for. | |

### Return type

[**GetProjectDependencyGraph200Response**](GetProjectDependencyGraph200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | * A reference implementation of the graph, as well as conversion functions to/from legacy tree format, can be found at: https://github.com/snyk/dep-graph.  * The object might contain additional fields in the future, in a backward-compatible way (&#x60;schemaVersion&#x60; will change accordingly). |  -  |

<a id="listAllAggregatedIssues"></a>
# **listAllAggregatedIssues**
> ListAllAggregatedIssues200Response listAllAggregatedIssues(orgId, projectId, listAllAggregatedIssuesRequest)

List all Aggregated issues



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have access to this organization.
    String projectId = "6d5813be-7e6d-4ab8-80c2-1e3e2a454545"; // String | The project ID to return issues for.
    ListAllAggregatedIssuesRequest listAllAggregatedIssuesRequest = new ListAllAggregatedIssuesRequest(); // ListAllAggregatedIssuesRequest | 
    try {
      ListAllAggregatedIssues200Response result = apiInstance.listAllAggregatedIssues(orgId, projectId, listAllAggregatedIssuesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#listAllAggregatedIssues");
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
| **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. | |
| **projectId** | **String**| The project ID to return issues for. | |
| **listAllAggregatedIssuesRequest** | [**ListAllAggregatedIssuesRequest**](ListAllAggregatedIssuesRequest.md)|  | [optional] |

### Return type

[**ListAllAggregatedIssues200Response**](ListAllAggregatedIssues200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listAllIgnores"></a>
# **listAllIgnores**
> Object listAllIgnores(orgId, projectId)

List all ignores

Temporary ignores include an &#x60;expires&#x60; attribute, while permanent ignores do not.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID to list ignores for. The `API_KEY` must have access to this organization.
    String projectId = "463c1ee5-31bc-428c-b451-b79a3270db08"; // String | The project ID to list ignores for.
    try {
      Object result = apiInstance.listAllIgnores(orgId, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#listAllIgnores");
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
| **orgId** | **String**| The organization ID to list ignores for. The &#x60;API_KEY&#x60; must have access to this organization. | |
| **projectId** | **String**| The project ID to list ignores for. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listAllJiraIssues"></a>
# **listAllJiraIssues**
> Object listAllJiraIssues(orgId, projectId)

List all jira issues



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID to list Jira issues for. The `API_KEY` must have access to this organization.
    String projectId = "463c1ee5-31bc-428c-b451-b79a3270db08"; // String | The project ID to list Jira issues for.
    try {
      Object result = apiInstance.listAllJiraIssues(orgId, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#listAllJiraIssues");
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
| **orgId** | **String**| The organization ID to list Jira issues for. The &#x60;API_KEY&#x60; must have access to this organization. | |
| **projectId** | **String**| The project ID to list Jira issues for. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listAllProjectIssuePaths"></a>
# **listAllProjectIssuePaths**
> ListAllProjectSnapshotIssuePaths200Response listAllProjectIssuePaths(orgId, projectId, issueId, snapshotId, perPage, page)

List all project issue paths



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have access to this organization.
    String projectId = "6d5813be-7e6d-4ab8-80c2-1e3e2a454545"; // String | The project ID for which to return issue paths.
    String issueId = "SNYK-JS-LODASH-590103"; // String | The issue ID for which to return issue paths.
    String snapshotId = "latest"; // String | The project snapshot ID for which to return issue paths. If set to `latest`, the most recent snapshot will be used. Use the \"List all project snapshots\" endpoint to find suitable values for this.
    BigDecimal perPage = new BigDecimal("100"); // BigDecimal | The number of results to return per page (1 - 1000, inclusive).
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page of results to return.
    try {
      ListAllProjectSnapshotIssuePaths200Response result = apiInstance.listAllProjectIssuePaths(orgId, projectId, issueId, snapshotId, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#listAllProjectIssuePaths");
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
| **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. | |
| **projectId** | **String**| The project ID for which to return issue paths. | |
| **issueId** | **String**| The issue ID for which to return issue paths. | |
| **snapshotId** | **String**| The project snapshot ID for which to return issue paths. If set to &#x60;latest&#x60;, the most recent snapshot will be used. Use the \&quot;List all project snapshots\&quot; endpoint to find suitable values for this. | [optional] [default to latest] |
| **perPage** | **BigDecimal**| The number of results to return per page (1 - 1000, inclusive). | [optional] [default to 100] |
| **page** | **BigDecimal**| The page of results to return. | [optional] [default to 1] |

### Return type

[**ListAllProjectSnapshotIssuePaths200Response**](ListAllProjectSnapshotIssuePaths200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Link -  <br>  |

<a id="listAllProjectSnapshotAggregatedIssues"></a>
# **listAllProjectSnapshotAggregatedIssues**
> ListAllAggregatedIssues200Response listAllProjectSnapshotAggregatedIssues(orgId, projectId, snapshotId, listAllAggregatedIssuesRequest)

List all project snapshot aggregated issues



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String orgId = "2d5c4d0c-c6d6-4658-a703-c2721c135b26"; // String | The organization ID. The `API_KEY` must have access to this organization.
    String projectId = "6d5813be-7e6d-4ab8-80c2-1e3e2a454545"; // String | The project ID.
    String snapshotId = "6d5813be-7e6d-4ab8-80c2-1e3e2a454553"; // String | The snapshot ID. If set to latest, the most recent snapshot will be used.
    ListAllAggregatedIssuesRequest listAllAggregatedIssuesRequest = new ListAllAggregatedIssuesRequest(); // ListAllAggregatedIssuesRequest | 
    try {
      ListAllAggregatedIssues200Response result = apiInstance.listAllProjectSnapshotAggregatedIssues(orgId, projectId, snapshotId, listAllAggregatedIssuesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#listAllProjectSnapshotAggregatedIssues");
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
| **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. | |
| **projectId** | **String**| The project ID. | |
| **snapshotId** | **String**| The snapshot ID. If set to latest, the most recent snapshot will be used. | |
| **listAllAggregatedIssuesRequest** | [**ListAllAggregatedIssuesRequest**](ListAllAggregatedIssuesRequest.md)|  | [optional] |

### Return type

[**ListAllAggregatedIssues200Response**](ListAllAggregatedIssues200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listAllProjectSnapshotIssuePaths"></a>
# **listAllProjectSnapshotIssuePaths**
> ListAllProjectSnapshotIssuePaths200Response listAllProjectSnapshotIssuePaths(orgId, projectId, snapshotId, issueId, perPage, page)

List all project snapshot issue paths



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have access to this organization.
    String projectId = "6d5813be-7e6d-4ab8-80c2-1e3e2a454545"; // String | The project ID for which to return issue paths.
    String snapshotId = "6d5813be-7e6d-4ab8-80c2-1e3e2a454553"; // String | The project snapshot ID for which to return issue paths. If set to `latest`, the most recent snapshot will be used. Use the \"List all project snapshots\" endpoint to find suitable values for this.
    String issueId = "SNYK-JS-LODASH-590103"; // String | The issue ID for which to return issue paths.
    BigDecimal perPage = new BigDecimal("100"); // BigDecimal | The number of results to return per page (1 - 1000, inclusive).
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page of results to return.
    try {
      ListAllProjectSnapshotIssuePaths200Response result = apiInstance.listAllProjectSnapshotIssuePaths(orgId, projectId, snapshotId, issueId, perPage, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#listAllProjectSnapshotIssuePaths");
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
| **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. | |
| **projectId** | **String**| The project ID for which to return issue paths. | |
| **snapshotId** | **String**| The project snapshot ID for which to return issue paths. If set to &#x60;latest&#x60;, the most recent snapshot will be used. Use the \&quot;List all project snapshots\&quot; endpoint to find suitable values for this. | |
| **issueId** | **String**| The issue ID for which to return issue paths. | |
| **perPage** | **BigDecimal**| The number of results to return per page (1 - 1000, inclusive). | [optional] [default to 100] |
| **page** | **BigDecimal**| The page of results to return. | [optional] [default to 1] |

### Return type

[**ListAllProjectSnapshotIssuePaths200Response**](ListAllProjectSnapshotIssuePaths200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Link -  <br>  |

<a id="listAllProjectSnapshots"></a>
# **listAllProjectSnapshots**
> ListAllProjectSnapshots200Response listAllProjectSnapshots(orgId, projectId, perPage, page, listAllProjectSnapshotsRequest)

List all project snapshots



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have access to this organization.
    String projectId = "6d5813be-7e6d-4ab8-80c2-1e3e2a454545"; // String | The project ID to return snapshots for.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of results to return (the default is 10, the maximum is 100).
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The offset from which to start returning results from.
    ListAllProjectSnapshotsRequest listAllProjectSnapshotsRequest = new ListAllProjectSnapshotsRequest(); // ListAllProjectSnapshotsRequest | 
    try {
      ListAllProjectSnapshots200Response result = apiInstance.listAllProjectSnapshots(orgId, projectId, perPage, page, listAllProjectSnapshotsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#listAllProjectSnapshots");
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
| **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. | |
| **projectId** | **String**| The project ID to return snapshots for. | |
| **perPage** | **BigDecimal**| The number of results to return (the default is 10, the maximum is 100). | [optional] |
| **page** | **BigDecimal**| The offset from which to start returning results from. | [optional] |
| **listAllProjectSnapshotsRequest** | [**ListAllProjectSnapshotsRequest**](ListAllProjectSnapshotsRequest.md)|  | [optional] |

### Return type

[**ListAllProjectSnapshots200Response**](ListAllProjectSnapshots200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Link -  <br>  |

<a id="listAllProjects"></a>
# **listAllProjects**
> ListAllProjects200Response listAllProjects(orgId, listAllProjectsRequest)

List all projects



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID to list projects for. The `API_KEY` must have access to this organization.
    ListAllProjectsRequest listAllProjectsRequest = new ListAllProjectsRequest(); // ListAllProjectsRequest | 
    try {
      ListAllProjects200Response result = apiInstance.listAllProjects(orgId, listAllProjectsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#listAllProjects");
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
| **orgId** | **String**| The organization ID to list projects for. The &#x60;API_KEY&#x60; must have access to this organization. | |
| **listAllProjectsRequest** | [**ListAllProjectsRequest**](ListAllProjectsRequest.md)|  | [optional] |

### Return type

[**ListAllProjects200Response**](ListAllProjects200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listProjectSettings"></a>
# **listProjectSettings**
> ListProjectSettings200Response listProjectSettings(orgId, projectId)

List project settings



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID to which the project belongs. The API_KEY must have access to this organization.
    String projectId = "463c1ee5-31bc-428c-b451-b79a3270db08"; // String | The project ID
    try {
      ListProjectSettings200Response result = apiInstance.listProjectSettings(orgId, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#listProjectSettings");
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
| **orgId** | **String**| The organization ID to which the project belongs. The API_KEY must have access to this organization. | |
| **projectId** | **String**| The project ID | |

### Return type

[**ListProjectSettings200Response**](ListProjectSettings200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response will contain only attributes that can be updated (see &#x60;ATTRIBUTES&#x60; section in &#x60;Update project settings&#x60;) and that have been previously set. |  -  |

<a id="moveProjectToADifferentOrganization"></a>
# **moveProjectToADifferentOrganization**
> moveProjectToADifferentOrganization(orgId, projectId, moveProjectToADifferentOrganizationRequest)

Move project to a different organization

Note: when moving a project to a new organization, the historical data used for reporting does not move with it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID to which the project belongs. The API_KEY must have group admin permissions. If the project is moved to a new group, a personal level API key is needed.
    String projectId = "463c1ee5-31bc-428c-b451-b79a3270db08"; // String | The project ID.
    MoveProjectToADifferentOrganizationRequest moveProjectToADifferentOrganizationRequest = new MoveProjectToADifferentOrganizationRequest(); // MoveProjectToADifferentOrganizationRequest | 
    try {
      apiInstance.moveProjectToADifferentOrganization(orgId, projectId, moveProjectToADifferentOrganizationRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#moveProjectToADifferentOrganization");
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
| **orgId** | **String**| The organization ID to which the project belongs. The API_KEY must have group admin permissions. If the project is moved to a new group, a personal level API key is needed. | |
| **projectId** | **String**| The project ID. | |
| **moveProjectToADifferentOrganizationRequest** | [**MoveProjectToADifferentOrganizationRequest**](MoveProjectToADifferentOrganizationRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="removeATagFromAProject"></a>
# **removeATagFromAProject**
> AddATagToAProject200Response removeATagFromAProject(orgId, projectId, addATagToAProjectRequest)

Remove a tag from a project



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID. The `API_KEY` must have access to this organization.
    String projectId = "6d5813be-7e6d-4ab8-80c2-1e3e2a454545"; // String | The project ID to remove a tag from
    AddATagToAProjectRequest addATagToAProjectRequest = new AddATagToAProjectRequest(); // AddATagToAProjectRequest | 
    try {
      AddATagToAProject200Response result = apiInstance.removeATagFromAProject(orgId, projectId, addATagToAProjectRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#removeATagFromAProject");
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
| **orgId** | **String**| The organization ID. The &#x60;API_KEY&#x60; must have access to this organization. | |
| **projectId** | **String**| The project ID to remove a tag from | |
| **addATagToAProjectRequest** | [**AddATagToAProjectRequest**](AddATagToAProjectRequest.md)|  | [optional] |

### Return type

[**AddATagToAProject200Response**](AddATagToAProject200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="replaceIgnores"></a>
# **replaceIgnores**
> List&lt;Object&gt; replaceIgnores(orgId, projectId, issueId)

Replace ignores



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String orgId = "orgId_example"; // String | Automatically added
    String projectId = "projectId_example"; // String | Automatically added
    String issueId = "issueId_example"; // String | Automatically added
    try {
      List<Object> result = apiInstance.replaceIgnores(orgId, projectId, issueId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#replaceIgnores");
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
| **orgId** | **String**| Automatically added | |
| **projectId** | **String**| Automatically added | |
| **issueId** | **String**| Automatically added | |

### Return type

**List&lt;Object&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="retrieveASingleProject"></a>
# **retrieveASingleProject**
> RetrieveASingleProject200Response retrieveASingleProject(orgId, projectId)

Retrieve a single project



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID the project belongs to. The `API_KEY` must have access to this organization.
    String projectId = "463c1ee5-31bc-428c-b451-b79a3270db08"; // String | The project ID.
    try {
      RetrieveASingleProject200Response result = apiInstance.retrieveASingleProject(orgId, projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#retrieveASingleProject");
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
| **orgId** | **String**| The organization ID the project belongs to. The &#x60;API_KEY&#x60; must have access to this organization. | |
| **projectId** | **String**| The project ID. | |

### Return type

[**RetrieveASingleProject200Response**](RetrieveASingleProject200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="retrieveIgnore"></a>
# **retrieveIgnore**
> Object retrieveIgnore(orgId, projectId, issueId)

Retrieve ignore



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String orgId = "4a18d42f-0706-4ad0-b127-24078731fbed"; // String | The organization ID to modify ignores for. The `API_KEY` must have access to this organization.
    String projectId = "463c1ee5-31bc-428c-b451-b79a3270db08"; // String | The project ID to modify ignores for.
    String issueId = "npm:qs:20140806-1"; // String | The issue ID to modify ignores for. Can be a vulnerability or a license Issue.
    try {
      Object result = apiInstance.retrieveIgnore(orgId, projectId, issueId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#retrieveIgnore");
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
| **orgId** | **String**| The organization ID to modify ignores for. The &#x60;API_KEY&#x60; must have access to this organization. | |
| **projectId** | **String**| The project ID to modify ignores for. | |
| **issueId** | **String**| The issue ID to modify ignores for. Can be a vulnerability or a license Issue. | |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateAProject"></a>
# **updateAProject**
> RetrieveASingleProject200Response updateAProject(orgId, projectId, updateAProjectRequest)

Update a project



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String orgId = "orgId_example"; // String | Automatically added
    String projectId = "projectId_example"; // String | Automatically added
    UpdateAProjectRequest updateAProjectRequest = new UpdateAProjectRequest(); // UpdateAProjectRequest | 
    try {
      RetrieveASingleProject200Response result = apiInstance.updateAProject(orgId, projectId, updateAProjectRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#updateAProject");
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
| **orgId** | **String**| Automatically added | |
| **projectId** | **String**| Automatically added | |
| **updateAProjectRequest** | [**UpdateAProjectRequest**](UpdateAProjectRequest.md)|  | [optional] |

### Return type

[**RetrieveASingleProject200Response**](RetrieveASingleProject200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateProjectSettings"></a>
# **updateProjectSettings**
> ListProjectSettings200Response updateProjectSettings(orgId, projectId, updateProjectSettingsRequest)

Update project settings



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.snyk.io/v1");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String orgId = "orgId_example"; // String | Automatically added
    String projectId = "projectId_example"; // String | Automatically added
    UpdateProjectSettingsRequest updateProjectSettingsRequest = new UpdateProjectSettingsRequest(); // UpdateProjectSettingsRequest | 
    try {
      ListProjectSettings200Response result = apiInstance.updateProjectSettings(orgId, projectId, updateProjectSettingsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#updateProjectSettings");
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
| **orgId** | **String**| Automatically added | |
| **projectId** | **String**| Automatically added | |
| **updateProjectSettingsRequest** | [**UpdateProjectSettingsRequest**](UpdateProjectSettingsRequest.md)|  | [optional] |

### Return type

[**ListProjectSettings200Response**](ListProjectSettings200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response will contain the attributes and values that have been sent in the request and successfully updated. |  -  |

