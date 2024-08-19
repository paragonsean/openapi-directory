# ProjectsApi

All URIs are relative to *https://api.illumidesk.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**projectCopy**](ProjectsApi.md#projectCopy) | **POST** /v1/{namespace}/projects/project-copy/ | Copy a project to your own account. |
| [**projectCopyCheck**](ProjectsApi.md#projectCopyCheck) | **HEAD** /v1/{namespace}/projects/project-copy-check/ | Check if you are able to copy a project to your account. |
| [**projectsCollaboratorsCreate**](ProjectsApi.md#projectsCollaboratorsCreate) | **POST** /v1/{namespace}/projects/{project}/collaborators/ | Create project collaborators |
| [**projectsCollaboratorsDelete**](ProjectsApi.md#projectsCollaboratorsDelete) | **DELETE** /v1/{namespace}/projects/{project}/collaborators/{collaborator}/ | Delete a project collaborator |
| [**projectsCollaboratorsList**](ProjectsApi.md#projectsCollaboratorsList) | **GET** /v1/{namespace}/projects/{project}/collaborators/ | Get project collaborators |
| [**projectsCollaboratorsRead**](ProjectsApi.md#projectsCollaboratorsRead) | **GET** /v1/{namespace}/projects/{project}/collaborators/{collaborator}/ | Get a project collaborator |
| [**projectsCollaboratorsUpdate**](ProjectsApi.md#projectsCollaboratorsUpdate) | **PATCH** /v1/{namespace}/projects/{project}/collaborators/{collaborator}/ | Update project collaborator |
| [**projectsCreate**](ProjectsApi.md#projectsCreate) | **POST** /v1/{namespace}/projects/ | Create a new project |
| [**projectsDelete**](ProjectsApi.md#projectsDelete) | **DELETE** /v1/{namespace}/projects/{project}/ | Delete a project |
| [**projectsDeploymentDelete**](ProjectsApi.md#projectsDeploymentDelete) | **DELETE** /v1/{namespace}/projects/{project}/deployments/{deployment}/ | Delete a deployment |
| [**projectsDeploymentsCreate**](ProjectsApi.md#projectsDeploymentsCreate) | **POST** /v1/{namespace}/projects/{project}/deployments/ | Create a new deployment |
| [**projectsDeploymentsDeploy**](ProjectsApi.md#projectsDeploymentsDeploy) | **POST** /v1/{namespace}/projects/{project}/deployments/{deployment}/deploy/ | Deploy an existing model |
| [**projectsDeploymentsList**](ProjectsApi.md#projectsDeploymentsList) | **GET** /v1/{namespace}/projects/{project}/deployments/ | Retrieve deployments |
| [**projectsDeploymentsRead**](ProjectsApi.md#projectsDeploymentsRead) | **GET** /v1/{namespace}/projects/{project}/deployments/{deployment}/ | Retrieve a deployment |
| [**projectsDeploymentsReplace**](ProjectsApi.md#projectsDeploymentsReplace) | **PUT** /v1/{namespace}/projects/{project}/deployments/{deployment}/ | Replace a deployment |
| [**projectsDeploymentsUpdate**](ProjectsApi.md#projectsDeploymentsUpdate) | **PATCH** /v1/{namespace}/projects/{project}/deployments/{deployment}/ | Update a deployment |
| [**projectsList**](ProjectsApi.md#projectsList) | **GET** /v1/{namespace}/projects/ | Get available projects |
| [**projectsProjectFilesCreate**](ProjectsApi.md#projectsProjectFilesCreate) | **POST** /v1/{namespace}/projects/{project}/project_files/ | Create project files |
| [**projectsProjectFilesDelete**](ProjectsApi.md#projectsProjectFilesDelete) | **DELETE** /v1/{namespace}/projects/{project}/project_files/{id}/ | Delete a project file |
| [**projectsProjectFilesList**](ProjectsApi.md#projectsProjectFilesList) | **GET** /v1/{namespace}/projects/{project}/project_files/ | Get project files |
| [**projectsProjectFilesRead**](ProjectsApi.md#projectsProjectFilesRead) | **GET** /v1/{namespace}/projects/{project}/project_files/{id}/ | Get a project file |
| [**projectsProjectFilesReplace**](ProjectsApi.md#projectsProjectFilesReplace) | **PUT** /v1/{namespace}/projects/{project}/project_files/{id}/ | Replace a project file |
| [**projectsProjectFilesUpdate**](ProjectsApi.md#projectsProjectFilesUpdate) | **PATCH** /v1/{namespace}/projects/{project}/project_files/{id}/ | Update a project file |
| [**projectsRead**](ProjectsApi.md#projectsRead) | **GET** /v1/{namespace}/projects/{project}/ | Get a project |
| [**projectsReplace**](ProjectsApi.md#projectsReplace) | **PUT** /v1/{namespace}/projects/{project}/ | Replace a project |
| [**projectsServersApiKey**](ProjectsApi.md#projectsServersApiKey) | **GET** /v1/{namespace}/projects/{project}/servers/{server}/api-key/ | Get server API key |
| [**projectsServersAuth**](ProjectsApi.md#projectsServersAuth) | **POST** /v1/{namespace}/projects/{project}/servers/{server}/auth/ | Server api key validation |
| [**projectsServersCreate**](ProjectsApi.md#projectsServersCreate) | **POST** /v1/{namespace}/projects/{project}/servers/ | Create a new server |
| [**projectsServersDelete**](ProjectsApi.md#projectsServersDelete) | **DELETE** /v1/{namespace}/projects/{project}/servers/{server}/ | Delete a server |
| [**projectsServersList**](ProjectsApi.md#projectsServersList) | **GET** /v1/{namespace}/projects/{project}/servers/ | Retrieve servers |
| [**projectsServersRead**](ProjectsApi.md#projectsServersRead) | **GET** /v1/{namespace}/projects/{project}/servers/{server}/ | Retrieve a server |
| [**projectsServersReplace**](ProjectsApi.md#projectsServersReplace) | **PUT** /v1/{namespace}/projects/{project}/servers/{server}/ | Replace a server |
| [**projectsServersRunStatsCreate**](ProjectsApi.md#projectsServersRunStatsCreate) | **POST** /v1/{namespace}/projects/{project}/servers/{server}/run-stats/ | Create a new server&#39;s run statistics |
| [**projectsServersRunStatsDelete**](ProjectsApi.md#projectsServersRunStatsDelete) | **DELETE** /v1/{namespace}/projects/{project}/servers/{server}/run-stats/{id}/ | Delete a server&#39;s statistics |
| [**projectsServersRunStatsRead**](ProjectsApi.md#projectsServersRunStatsRead) | **GET** /v1/{namespace}/projects/{project}/servers/{server}/run-stats/{id}/ | Retrieve statistics for a server |
| [**projectsServersRunStatsReplace**](ProjectsApi.md#projectsServersRunStatsReplace) | **PUT** /v1/{namespace}/projects/{project}/servers/{server}/run-stats/{id}/ | Replace a server&#39;s statistics |
| [**projectsServersRunStatsUpdate**](ProjectsApi.md#projectsServersRunStatsUpdate) | **PATCH** /v1/{namespace}/projects/{project}/servers/{server}/run-stats/{id}/ | Update a server&#39;s statistics |
| [**projectsServersSshTunnelsCreate**](ProjectsApi.md#projectsServersSshTunnelsCreate) | **POST** /v1/{namespace}/projects/{project}/servers/{server}/ssh-tunnels/ | Create SSH Tunnel associated to a server |
| [**projectsServersSshTunnelsDelete**](ProjectsApi.md#projectsServersSshTunnelsDelete) | **DELETE** /v1/{namespace}/projects/{project}/servers/{server}/ssh-tunnels/{tunnel}/ | Delete an SSH Tunnel associated to a server |
| [**projectsServersSshTunnelsList**](ProjectsApi.md#projectsServersSshTunnelsList) | **GET** /v1/{namespace}/projects/{project}/servers/{server}/ssh-tunnels/ | Get SSH Tunnels associated to a server |
| [**projectsServersSshTunnelsRead**](ProjectsApi.md#projectsServersSshTunnelsRead) | **GET** /v1/{namespace}/projects/{project}/servers/{server}/ssh-tunnels/{tunnel}/ | Get an SSH Tunnel associated to a server |
| [**projectsServersSshTunnelsReplace**](ProjectsApi.md#projectsServersSshTunnelsReplace) | **PUT** /v1/{namespace}/projects/{project}/servers/{server}/ssh-tunnels/{tunnel}/ | Replace SSH Tunnel associated to a server |
| [**projectsServersSshTunnelsUpdate**](ProjectsApi.md#projectsServersSshTunnelsUpdate) | **PATCH** /v1/{namespace}/projects/{project}/servers/{server}/ssh-tunnels/{tunnel}/ | Update an SSH Tunnel associated to a server |
| [**projectsServersStart**](ProjectsApi.md#projectsServersStart) | **POST** /v1/{namespace}/projects/{project}/servers/{server}/start/ | Start a server |
| [**projectsServersStatsDelete**](ProjectsApi.md#projectsServersStatsDelete) | **DELETE** /v1/{namespace}/projects/{project}/servers/{server}/stats/{id}/ | Delete a server&#39;s statistics |
| [**projectsServersStatsRead**](ProjectsApi.md#projectsServersStatsRead) | **GET** /v1/{namespace}/projects/{project}/servers/{server}/stats/{id}/ | Retrieve a server&#39;s statistics |
| [**projectsServersStatsReplace**](ProjectsApi.md#projectsServersStatsReplace) | **PUT** /v1/{namespace}/projects/{project}/servers/{server}/stats/{id}/ | Replace a server&#39;s statistics |
| [**projectsServersStatsUpdate**](ProjectsApi.md#projectsServersStatsUpdate) | **PATCH** /v1/{namespace}/projects/{project}/servers/{server}/stats/{id}/ | Update a server&#39;s statistics |
| [**projectsServersStatuses**](ProjectsApi.md#projectsServersStatuses) | **GET** /v1/{namespace}/projects/{project}/servers/statuses/ | Retrieve server statuses |
| [**projectsServersStop**](ProjectsApi.md#projectsServersStop) | **POST** /v1/{namespace}/projects/{project}/servers/{server}/stop/ | Stop a server |
| [**projectsServersUpdate**](ProjectsApi.md#projectsServersUpdate) | **PATCH** /v1/{namespace}/projects/{project}/servers/{server}/ | Update a server |
| [**projectsUpdate**](ProjectsApi.md#projectsUpdate) | **PATCH** /v1/{namespace}/projects/{project}/ | Update a project |
| [**serviceTriggerCreate**](ProjectsApi.md#serviceTriggerCreate) | **POST** /v1/{namespace}/projects/{project}/servers/{server}/triggers/ | Create a new server trigger |
| [**serviceTriggerDelete**](ProjectsApi.md#serviceTriggerDelete) | **DELETE** /v1/{namespace}/projects/{project}/servers/{server}/triggers/{trigger}/ | Delete a server trigger |
| [**serviceTriggerList**](ProjectsApi.md#serviceTriggerList) | **GET** /v1/{namespace}/projects/{project}/servers/{server}/triggers/ | Retrieve server triggers |
| [**serviceTriggerRead**](ProjectsApi.md#serviceTriggerRead) | **GET** /v1/{namespace}/projects/{project}/servers/{server}/triggers/{trigger}/ | Get a server trigger |
| [**serviceTriggerReplace**](ProjectsApi.md#serviceTriggerReplace) | **PUT** /v1/{namespace}/projects/{project}/servers/{server}/triggers/{trigger}/ | Replace a server trigger |
| [**serviceTriggerUpdate**](ProjectsApi.md#serviceTriggerUpdate) | **PATCH** /v1/{namespace}/projects/{project}/servers/{server}/triggers/{trigger}/ | Update a server trigger |


<a id="projectCopy"></a>
# **projectCopy**
> Project projectCopy(namespace, projectCopyData)

Copy a project to your own account.

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    ProjectCopyRequest projectCopyData = new ProjectCopyRequest(); // ProjectCopyRequest | 
    try {
      Project result = apiInstance.projectCopy(namespace, projectCopyData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectCopy");
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
| **namespace** | **String**| User or team name. | |
| **projectCopyData** | [**ProjectCopyRequest**](ProjectCopyRequest.md)|  | |

### Return type

[**Project**](Project.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Project copied |  -  |
| **400** | Invalid data supplied |  -  |
| **404** | Project not found. |  -  |

<a id="projectCopyCheck"></a>
# **projectCopyCheck**
> projectCopyCheck(namespace, projectCopyData)

Check if you are able to copy a project to your account.

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    ProjectCopyCheckRequest projectCopyData = new ProjectCopyCheckRequest(); // ProjectCopyCheckRequest | 
    try {
      apiInstance.projectCopyCheck(namespace, projectCopyData);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectCopyCheck");
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
| **namespace** | **String**| User or team name. | |
| **projectCopyData** | [**ProjectCopyCheckRequest**](ProjectCopyCheckRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The authenticated has permission to copy this project |  -  |
| **404** | Project not found. |  -  |

<a id="projectsCollaboratorsCreate"></a>
# **projectsCollaboratorsCreate**
> Collaborator projectsCollaboratorsCreate(project, namespace, collaboratorData)

Create project collaborators

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    CollaboratorData collaboratorData = new CollaboratorData(); // CollaboratorData | 
    try {
      Collaborator result = apiInstance.projectsCollaboratorsCreate(project, namespace, collaboratorData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsCollaboratorsCreate");
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
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **collaboratorData** | [**CollaboratorData**](CollaboratorData.md)|  | [optional] |

### Return type

[**Collaborator**](Collaborator.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Collaborator created. |  -  |
| **400** | Invalid data supplied. |  -  |

<a id="projectsCollaboratorsDelete"></a>
# **projectsCollaboratorsDelete**
> projectsCollaboratorsDelete(project, namespace, collaborator)

Delete a project collaborator

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String project = "project_example"; // String | Project unique identifier.
    String namespace = "namespace_example"; // String | User or team name.
    String collaborator = "collaborator_example"; // String | Collaborator unique identifier.
    try {
      apiInstance.projectsCollaboratorsDelete(project, namespace, collaborator);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsCollaboratorsDelete");
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
| **project** | **String**| Project unique identifier. | |
| **namespace** | **String**| User or team name. | |
| **collaborator** | **String**| Collaborator unique identifier. | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Collaborator deleted. |  -  |
| **404** | Collaborator not found. |  -  |

<a id="projectsCollaboratorsList"></a>
# **projectsCollaboratorsList**
> List&lt;Collaborator&gt; projectsCollaboratorsList(project, namespace, limit, offset, ordering)

Get project collaborators

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    String limit = "limit_example"; // String | Limit when retrieving items.
    String offset = "offset_example"; // String | Offset when retrieving items.
    String ordering = "ordering_example"; // String | Ordering when retrieving items.
    try {
      List<Collaborator> result = apiInstance.projectsCollaboratorsList(project, namespace, limit, offset, ordering);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsCollaboratorsList");
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
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **limit** | **String**| Limit when retrieving items. | [optional] |
| **offset** | **String**| Offset when retrieving items. | [optional] |
| **ordering** | **String**| Ordering when retrieving items. | [optional] |

### Return type

[**List&lt;Collaborator&gt;**](Collaborator.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Collaborator list. |  -  |

<a id="projectsCollaboratorsRead"></a>
# **projectsCollaboratorsRead**
> Collaborator projectsCollaboratorsRead(project, namespace, collaborator)

Get a project collaborator

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String project = "project_example"; // String | Project unique identifier.
    String namespace = "namespace_example"; // String | User or team name.
    String collaborator = "collaborator_example"; // String | Collaborator unique identifier expressed as UUID or name.
    try {
      Collaborator result = apiInstance.projectsCollaboratorsRead(project, namespace, collaborator);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsCollaboratorsRead");
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
| **project** | **String**| Project unique identifier. | |
| **namespace** | **String**| User or team name. | |
| **collaborator** | **String**| Collaborator unique identifier expressed as UUID or name. | |

### Return type

[**Collaborator**](Collaborator.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Collaborator retrieved. |  -  |
| **404** | Collaborator not found. |  -  |

<a id="projectsCollaboratorsUpdate"></a>
# **projectsCollaboratorsUpdate**
> Collaborator projectsCollaboratorsUpdate(project, namespace, collaborator, collaboratorData)

Update project collaborator

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String project = "project_example"; // String | 
    String namespace = "namespace_example"; // String | User or team name.
    String collaborator = "collaborator_example"; // String | 
    CollaboratorData collaboratorData = new CollaboratorData(); // CollaboratorData | 
    try {
      Collaborator result = apiInstance.projectsCollaboratorsUpdate(project, namespace, collaborator, collaboratorData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsCollaboratorsUpdate");
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
| **project** | **String**|  | |
| **namespace** | **String**| User or team name. | |
| **collaborator** | **String**|  | |
| **collaboratorData** | [**CollaboratorData**](CollaboratorData.md)|  | [optional] |

### Return type

[**Collaborator**](Collaborator.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Collaborator updated |  -  |
| **400** | Invalid data supplied |  -  |
| **404** | Collaborator not found |  -  |

<a id="projectsCreate"></a>
# **projectsCreate**
> Project projectsCreate(namespace, projectData)

Create a new project

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    ProjectData projectData = new ProjectData(); // ProjectData | 
    try {
      Project result = apiInstance.projectsCreate(namespace, projectData);
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
| **namespace** | **String**| User or team name. | |
| **projectData** | [**ProjectData**](ProjectData.md)|  | [optional] |

### Return type

[**Project**](Project.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Project created |  -  |
| **400** | Invalid data supplied |  -  |

<a id="projectsDelete"></a>
# **projectsDelete**
> projectsDelete(namespace, project)

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    try {
      apiInstance.projectsDelete(namespace, project);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsDelete");
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
| **namespace** | **String**| User or team name. | |
| **project** | **String**| Project unique identifier expressed as UUID or name. | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Project deleted. |  -  |
| **404** | Project not found. |  -  |

<a id="projectsDeploymentDelete"></a>
# **projectsDeploymentDelete**
> projectsDeploymentDelete(project, namespace, deployment)

Delete a deployment

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String project = "project_example"; // String | Project unique identifier.
    String namespace = "namespace_example"; // String | User or team name.
    String deployment = "deployment_example"; // String | User unique identifier.
    try {
      apiInstance.projectsDeploymentDelete(project, namespace, deployment);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsDeploymentDelete");
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
| **project** | **String**| Project unique identifier. | |
| **namespace** | **String**| User or team name. | |
| **deployment** | **String**| User unique identifier. | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Deployment deleted |  -  |
| **404** | Deployment not found |  -  |

<a id="projectsDeploymentsCreate"></a>
# **projectsDeploymentsCreate**
> Deployment projectsDeploymentsCreate(project, namespace, deploymentData)

Create a new deployment

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String project = "project_example"; // String | Project unique identifer expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    DeploymentData deploymentData = new DeploymentData(); // DeploymentData | 
    try {
      Deployment result = apiInstance.projectsDeploymentsCreate(project, namespace, deploymentData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsDeploymentsCreate");
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
| **project** | **String**| Project unique identifer expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **deploymentData** | [**DeploymentData**](DeploymentData.md)|  | [optional] |

### Return type

[**Deployment**](Deployment.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Deployment created. |  -  |
| **400** | Invalid data supplied. |  -  |

<a id="projectsDeploymentsDeploy"></a>
# **projectsDeploymentsDeploy**
> projectsDeploymentsDeploy(project, namespace, deployment)

Deploy an existing model

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    String deployment = "deployment_example"; // String | Deployment unique identifier expressed as UUID or name.
    try {
      apiInstance.projectsDeploymentsDeploy(project, namespace, deployment);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsDeploymentsDeploy");
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
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **deployment** | **String**| Deployment unique identifier expressed as UUID or name. | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Deployment successful. |  -  |
| **400** | Invalid data supplied. |  -  |

<a id="projectsDeploymentsList"></a>
# **projectsDeploymentsList**
> List&lt;Deployment&gt; projectsDeploymentsList(project, namespace, limit, offset, name, ordering)

Retrieve deployments

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    String limit = "limit_example"; // String | Limit results when getting deployment list.
    String offset = "offset_example"; // String | Offset results when getting deployment list.
    String name = "name_example"; // String | Server name.
    String ordering = "ordering_example"; // String | Ordering option when getting deployment list.
    try {
      List<Deployment> result = apiInstance.projectsDeploymentsList(project, namespace, limit, offset, name, ordering);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsDeploymentsList");
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
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **limit** | **String**| Limit results when getting deployment list. | [optional] |
| **offset** | **String**| Offset results when getting deployment list. | [optional] |
| **name** | **String**| Server name. | [optional] |
| **ordering** | **String**| Ordering option when getting deployment list. | [optional] |

### Return type

[**List&lt;Deployment&gt;**](Deployment.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deployment list. |  -  |

<a id="projectsDeploymentsRead"></a>
# **projectsDeploymentsRead**
> Deployment projectsDeploymentsRead(project, namespace, deployment)

Retrieve a deployment

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    String deployment = "deployment_example"; // String | Deployment unique identifier expressed as UUID or name.
    try {
      Deployment result = apiInstance.projectsDeploymentsRead(project, namespace, deployment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsDeploymentsRead");
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
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **deployment** | **String**| Deployment unique identifier expressed as UUID or name. | |

### Return type

[**Deployment**](Deployment.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deployment retrieved. |  -  |
| **404** | Deployment not found. |  -  |

<a id="projectsDeploymentsReplace"></a>
# **projectsDeploymentsReplace**
> Deployment projectsDeploymentsReplace(project, namespace, deployment, deploymentData)

Replace a deployment

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    String deployment = "deployment_example"; // String | Deployment unique identifier expressed as UUID or name.
    DeploymentData deploymentData = new DeploymentData(); // DeploymentData | 
    try {
      Deployment result = apiInstance.projectsDeploymentsReplace(project, namespace, deployment, deploymentData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsDeploymentsReplace");
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
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **deployment** | **String**| Deployment unique identifier expressed as UUID or name. | |
| **deploymentData** | [**DeploymentData**](DeploymentData.md)|  | [optional] |

### Return type

[**Deployment**](Deployment.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deployment updated. |  -  |
| **400** | Invalid data supplied. |  -  |

<a id="projectsDeploymentsUpdate"></a>
# **projectsDeploymentsUpdate**
> Deployment projectsDeploymentsUpdate(project, namespace, deployment, deploymentData)

Update a deployment

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    String deployment = "deployment_example"; // String | Deployment unique identifier expressed as UUID or name.
    DeploymentData deploymentData = new DeploymentData(); // DeploymentData | 
    try {
      Deployment result = apiInstance.projectsDeploymentsUpdate(project, namespace, deployment, deploymentData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsDeploymentsUpdate");
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
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **deployment** | **String**| Deployment unique identifier expressed as UUID or name. | |
| **deploymentData** | [**DeploymentData**](DeploymentData.md)|  | [optional] |

### Return type

[**Deployment**](Deployment.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Deployment updated |  -  |
| **400** | Invalid data supplied |  -  |
| **404** | Deployment not found |  -  |

<a id="projectsList"></a>
# **projectsList**
> List&lt;Project&gt; projectsList(namespace, limit, offset, _private, name, ordering)

Get available projects

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    String limit = "limit_example"; // String | Limit when getting data.
    String offset = "offset_example"; // String | Offset when getting data.
    String _private = "_private_example"; // String | Private project or public project.
    String name = "name_example"; // String | Project name.
    String ordering = "ordering_example"; // String | Ordering when getting projects.
    try {
      List<Project> result = apiInstance.projectsList(namespace, limit, offset, _private, name, ordering);
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

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **namespace** | **String**| User or team name. | |
| **limit** | **String**| Limit when getting data. | [optional] |
| **offset** | **String**| Offset when getting data. | [optional] |
| **_private** | **String**| Private project or public project. | [optional] |
| **name** | **String**| Project name. | [optional] |
| **ordering** | **String**| Ordering when getting projects. | [optional] |

### Return type

[**List&lt;Project&gt;**](Project.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Project list. |  -  |

<a id="projectsProjectFilesCreate"></a>
# **projectsProjectFilesCreate**
> ProjectFile projectsProjectFilesCreate(project, namespace, _file, base64Data, name, path)

Create project files

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String project = "project_example"; // String | Project unique identifier.
    String namespace = "namespace_example"; // String | User or team name.
    File _file = new File("/path/to/file"); // File | File to send, to create new file. This parameter is only used with form data and may include multiple files.
    String base64Data = "base64Data_example"; // String | Fila data, represented as base64.
    String name = "name_example"; // String | File name. May include path when creating file with base64 field.
    String path = "path_example"; // String | File path. Defaults to (/).
    try {
      ProjectFile result = apiInstance.projectsProjectFilesCreate(project, namespace, _file, base64Data, name, path);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsProjectFilesCreate");
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
| **project** | **String**| Project unique identifier. | |
| **namespace** | **String**| User or team name. | |
| **_file** | **File**| File to send, to create new file. This parameter is only used with form data and may include multiple files. | [optional] |
| **base64Data** | **String**| Fila data, represented as base64. | [optional] |
| **name** | **String**| File name. May include path when creating file with base64 field. | [optional] |
| **path** | **String**| File path. Defaults to (/). | [optional] |

### Return type

[**ProjectFile**](ProjectFile.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | ProjectFile created |  -  |
| **400** | Invalid data supplied |  -  |

<a id="projectsProjectFilesDelete"></a>
# **projectsProjectFilesDelete**
> projectsProjectFilesDelete(project, namespace, id)

Delete a project file

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String project = "project_example"; // String | Project unique identifer.
    String namespace = "namespace_example"; // String | User or team name.
    String id = "id_example"; // String | File unique identifier.
    try {
      apiInstance.projectsProjectFilesDelete(project, namespace, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsProjectFilesDelete");
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
| **project** | **String**| Project unique identifer. | |
| **namespace** | **String**| User or team name. | |
| **id** | **String**| File unique identifier. | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | ProjectFile deleted |  -  |
| **404** | ProjectFile not found |  -  |

<a id="projectsProjectFilesList"></a>
# **projectsProjectFilesList**
> List&lt;ProjectFile&gt; projectsProjectFilesList(project, namespace, limit, offset, ordering, filename, content)

Get project files

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String project = "project_example"; // String | Unique identifier for project file expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    String limit = "limit_example"; // String | Limit when getting project file list.
    String offset = "offset_example"; // String | Offset when getting project file list.
    String ordering = "ordering_example"; // String | Ordering of list values when getting project file list.
    String filename = "filename_example"; // String | Exact file name, relative to the project root. If no such file is found, an empty list will be returned.
    String content = "content_example"; // String | Determines whether or not content is returned as base64. Defaults to false.
    try {
      List<ProjectFile> result = apiInstance.projectsProjectFilesList(project, namespace, limit, offset, ordering, filename, content);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsProjectFilesList");
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
| **project** | **String**| Unique identifier for project file expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **limit** | **String**| Limit when getting project file list. | [optional] |
| **offset** | **String**| Offset when getting project file list. | [optional] |
| **ordering** | **String**| Ordering of list values when getting project file list. | [optional] |
| **filename** | **String**| Exact file name, relative to the project root. If no such file is found, an empty list will be returned. | [optional] |
| **content** | **String**| Determines whether or not content is returned as base64. Defaults to false. | [optional] |

### Return type

[**List&lt;ProjectFile&gt;**](ProjectFile.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ProjectFile list |  -  |

<a id="projectsProjectFilesRead"></a>
# **projectsProjectFilesRead**
> ProjectFile projectsProjectFilesRead(project, namespace, id, content)

Get a project file

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String project = "project_example"; // String | Project unique identifer.
    String namespace = "namespace_example"; // String | User or team name.
    String id = "id_example"; // String | File unique identifier.
    String content = "content_example"; // String | Determines whether or not content is returned as base64. Defaults to false.
    try {
      ProjectFile result = apiInstance.projectsProjectFilesRead(project, namespace, id, content);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsProjectFilesRead");
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
| **project** | **String**| Project unique identifer. | |
| **namespace** | **String**| User or team name. | |
| **id** | **String**| File unique identifier. | |
| **content** | **String**| Determines whether or not content is returned as base64. Defaults to false. | [optional] |

### Return type

[**ProjectFile**](ProjectFile.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ProjectFile retrieved |  -  |
| **404** | ProjectFile not found |  -  |

<a id="projectsProjectFilesReplace"></a>
# **projectsProjectFilesReplace**
> ProjectFile projectsProjectFilesReplace(project, namespace, id, _file, base64Data, name, path)

Replace a project file

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String project = "project_example"; // String | Project unique identifer.
    String namespace = "namespace_example"; // String | User or team name.
    String id = "id_example"; // String | File unique identifier.
    File _file = new File("/path/to/file"); // File | File to send, to create new file. This parameter is only used with form data and may include multiple files.
    String base64Data = "base64Data_example"; // String | Fila data, represented as base64.
    String name = "name_example"; // String | File name. May include path when creating file with base64 field.
    String path = "path_example"; // String | File path. Defaults to (/).
    try {
      ProjectFile result = apiInstance.projectsProjectFilesReplace(project, namespace, id, _file, base64Data, name, path);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsProjectFilesReplace");
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
| **project** | **String**| Project unique identifer. | |
| **namespace** | **String**| User or team name. | |
| **id** | **String**| File unique identifier. | |
| **_file** | **File**| File to send, to create new file. This parameter is only used with form data and may include multiple files. | [optional] |
| **base64Data** | **String**| Fila data, represented as base64. | [optional] |
| **name** | **String**| File name. May include path when creating file with base64 field. | [optional] |
| **path** | **String**| File path. Defaults to (/). | [optional] |

### Return type

[**ProjectFile**](ProjectFile.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ProjectFile updated |  -  |
| **400** | Invalid data supplied. |  -  |

<a id="projectsProjectFilesUpdate"></a>
# **projectsProjectFilesUpdate**
> ProjectFile projectsProjectFilesUpdate(project, namespace, id, _file, base64Data, name, path)

Update a project file

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String project = "project_example"; // String | Project unique identifer.
    String namespace = "namespace_example"; // String | User or team name.
    String id = "id_example"; // String | File unique identifier.
    File _file = new File("/path/to/file"); // File | File to send, to create new file. This parameter is only used with form data and may include multiple files.
    String base64Data = "base64Data_example"; // String | Fila data, represented as base64.
    String name = "name_example"; // String | File name. May include path when creating file with base64 field.
    String path = "path_example"; // String | File path. Defaults to (/).
    try {
      ProjectFile result = apiInstance.projectsProjectFilesUpdate(project, namespace, id, _file, base64Data, name, path);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsProjectFilesUpdate");
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
| **project** | **String**| Project unique identifer. | |
| **namespace** | **String**| User or team name. | |
| **id** | **String**| File unique identifier. | |
| **_file** | **File**| File to send, to create new file. This parameter is only used with form data and may include multiple files. | [optional] |
| **base64Data** | **String**| Fila data, represented as base64. | [optional] |
| **name** | **String**| File name. May include path when creating file with base64 field. | [optional] |
| **path** | **String**| File path. Defaults to (/). | [optional] |

### Return type

[**ProjectFile**](ProjectFile.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ProjectFile updated. |  -  |
| **400** | Invalid data supplied. |  -  |
| **404** | ProjectFile not found. |  -  |

<a id="projectsRead"></a>
# **projectsRead**
> Project projectsRead(namespace, project)

Get a project

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    try {
      Project result = apiInstance.projectsRead(namespace, project);
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
| **namespace** | **String**| User or team name. | |
| **project** | **String**| Project unique identifier expressed as UUID or name. | |

### Return type

[**Project**](Project.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Project retrieved. |  -  |
| **404** | Project not found. |  -  |

<a id="projectsReplace"></a>
# **projectsReplace**
> Project projectsReplace(namespace, project, projectData)

Replace a project

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team namespace.
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    ProjectData projectData = new ProjectData(); // ProjectData | 
    try {
      Project result = apiInstance.projectsReplace(namespace, project, projectData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsReplace");
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
| **namespace** | **String**| User or team namespace. | |
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **projectData** | [**ProjectData**](ProjectData.md)|  | [optional] |

### Return type

[**Project**](Project.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Project updated. |  -  |
| **400** | Invalid data supplied. |  -  |

<a id="projectsServersApiKey"></a>
# **projectsServersApiKey**
> JWT projectsServersApiKey(project, namespace, server)

Get server API key

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    String server = "server_example"; // String | Server unique identifier expressed as UUID or name.
    try {
      JWT result = apiInstance.projectsServersApiKey(project, namespace, server);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsServersApiKey");
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
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **server** | **String**| Server unique identifier expressed as UUID or name. | |

### Return type

[**JWT**](JWT.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Server API key |  -  |

<a id="projectsServersAuth"></a>
# **projectsServersAuth**
> projectsServersAuth(project, namespace, server)

Server api key validation

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    String server = "server_example"; // String | Server unique identifier expressed as UUID or name.
    try {
      apiInstance.projectsServersAuth(project, namespace, server);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsServersAuth");
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
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **server** | **String**| Server unique identifier expressed as UUID or name. | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Api key verified |  -  |
| **401** | Invalid api key. |  -  |

<a id="projectsServersCreate"></a>
# **projectsServersCreate**
> Server projectsServersCreate(project, namespace, serverData)

Create a new server

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String project = "project_example"; // String | Project unique identifer expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    ServerData serverData = new ServerData(); // ServerData | 
    try {
      Server result = apiInstance.projectsServersCreate(project, namespace, serverData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsServersCreate");
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
| **project** | **String**| Project unique identifer expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **serverData** | [**ServerData**](ServerData.md)|  | [optional] |

### Return type

[**Server**](Server.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Server created. |  -  |
| **400** | Invalid data supplied. |  -  |

<a id="projectsServersDelete"></a>
# **projectsServersDelete**
> projectsServersDelete(project, namespace, server)

Delete a server

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String project = "project_example"; // String | Project unique identifier.
    String namespace = "namespace_example"; // String | User or team name.
    String server = "server_example"; // String | User unique identifier.
    try {
      apiInstance.projectsServersDelete(project, namespace, server);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsServersDelete");
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
| **project** | **String**| Project unique identifier. | |
| **namespace** | **String**| User or team name. | |
| **server** | **String**| User unique identifier. | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Server deleted |  -  |
| **404** | Server not found |  -  |

<a id="projectsServersList"></a>
# **projectsServersList**
> List&lt;Server&gt; projectsServersList(project, namespace, limit, offset, name, ordering)

Retrieve servers

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    String limit = "limit_example"; // String | Limit results when getting server list.
    String offset = "offset_example"; // String | Offset results when getting server list.
    String name = "name_example"; // String | Server name.
    String ordering = "ordering_example"; // String | Ordering option when getting server list.
    try {
      List<Server> result = apiInstance.projectsServersList(project, namespace, limit, offset, name, ordering);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsServersList");
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
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **limit** | **String**| Limit results when getting server list. | [optional] |
| **offset** | **String**| Offset results when getting server list. | [optional] |
| **name** | **String**| Server name. | [optional] |
| **ordering** | **String**| Ordering option when getting server list. | [optional] |

### Return type

[**List&lt;Server&gt;**](Server.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Server list. |  -  |

<a id="projectsServersRead"></a>
# **projectsServersRead**
> Server projectsServersRead(project, namespace, server)

Retrieve a server

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    String server = "server_example"; // String | Server unique identifier expressed as UUID or name.
    try {
      Server result = apiInstance.projectsServersRead(project, namespace, server);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsServersRead");
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
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **server** | **String**| Server unique identifier expressed as UUID or name. | |

### Return type

[**Server**](Server.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Server retrieved. |  -  |
| **404** | Server not found. |  -  |

<a id="projectsServersReplace"></a>
# **projectsServersReplace**
> Server projectsServersReplace(project, namespace, server, serverData)

Replace a server

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    String server = "server_example"; // String | Server unique identifier expressed as UUID or name.
    ServerData serverData = new ServerData(); // ServerData | 
    try {
      Server result = apiInstance.projectsServersReplace(project, namespace, server, serverData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsServersReplace");
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
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **server** | **String**| Server unique identifier expressed as UUID or name. | |
| **serverData** | [**ServerData**](ServerData.md)|  | [optional] |

### Return type

[**Server**](Server.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Server updated. |  -  |
| **400** | Invalid data supplied. |  -  |

<a id="projectsServersRunStatsCreate"></a>
# **projectsServersRunStatsCreate**
> ServerRunStatistics projectsServersRunStatsCreate(server, project, namespace, serverrunstatsData)

Create a new server&#39;s run statistics

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String server = "server_example"; // String | Server unique identifier expressed as UUID or name.
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    ServerRunStatisticsData serverrunstatsData = new ServerRunStatisticsData(); // ServerRunStatisticsData | 
    try {
      ServerRunStatistics result = apiInstance.projectsServersRunStatsCreate(server, project, namespace, serverrunstatsData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsServersRunStatsCreate");
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
| **server** | **String**| Server unique identifier expressed as UUID or name. | |
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **serverrunstatsData** | [**ServerRunStatisticsData**](ServerRunStatisticsData.md)|  | [optional] |

### Return type

[**ServerRunStatistics**](ServerRunStatistics.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | ServerRunStatistics created. |  -  |
| **400** | Invalid data supplied. |  -  |

<a id="projectsServersRunStatsDelete"></a>
# **projectsServersRunStatsDelete**
> projectsServersRunStatsDelete(server, project, namespace, id)

Delete a server&#39;s statistics

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String server = "server_example"; // String | Server unique identifier expressed as UUID or name.
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    String id = "id_example"; // String | Server run statistics unique identifier expressed as UUID.
    try {
      apiInstance.projectsServersRunStatsDelete(server, project, namespace, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsServersRunStatsDelete");
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
| **server** | **String**| Server unique identifier expressed as UUID or name. | |
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **id** | **String**| Server run statistics unique identifier expressed as UUID. | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | ServerRunStatistics deleted. |  -  |
| **404** | ServerRunStatistics not found. |  -  |

<a id="projectsServersRunStatsRead"></a>
# **projectsServersRunStatsRead**
> ServerRunStatistics projectsServersRunStatsRead(server, project, namespace, id)

Retrieve statistics for a server

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String server = "server_example"; // String | Server unique identifier expressed as UUID or name.
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    String id = "id_example"; // String | Run statistics unique identifier expressed as UUID.
    try {
      ServerRunStatistics result = apiInstance.projectsServersRunStatsRead(server, project, namespace, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsServersRunStatsRead");
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
| **server** | **String**| Server unique identifier expressed as UUID or name. | |
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **id** | **String**| Run statistics unique identifier expressed as UUID. | |

### Return type

[**ServerRunStatistics**](ServerRunStatistics.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ServerRunStatistics retrieved. |  -  |
| **404** | ServerRunStatistics not found. |  -  |

<a id="projectsServersRunStatsReplace"></a>
# **projectsServersRunStatsReplace**
> ServerRunStatistics projectsServersRunStatsReplace(server, project, namespace, id, serverrunstatsData)

Replace a server&#39;s statistics

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String server = "server_example"; // String | Server unique identifier expressed as UUID or name.
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    String id = "id_example"; // String | Server run statistics expressed as UUID.
    ServerRunStatisticsData serverrunstatsData = new ServerRunStatisticsData(); // ServerRunStatisticsData | 
    try {
      ServerRunStatistics result = apiInstance.projectsServersRunStatsReplace(server, project, namespace, id, serverrunstatsData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsServersRunStatsReplace");
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
| **server** | **String**| Server unique identifier expressed as UUID or name. | |
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **id** | **String**| Server run statistics expressed as UUID. | |
| **serverrunstatsData** | [**ServerRunStatisticsData**](ServerRunStatisticsData.md)|  | [optional] |

### Return type

[**ServerRunStatistics**](ServerRunStatistics.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ServerRunStatistics updated. |  -  |
| **400** | Invalid data supplied. |  -  |

<a id="projectsServersRunStatsUpdate"></a>
# **projectsServersRunStatsUpdate**
> ServerRunStatistics projectsServersRunStatsUpdate(server, project, namespace, id, serverrunstatsData)

Update a server&#39;s statistics

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String server = "server_example"; // String | Server unique identifier expressed as UUID or name.
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    String id = "id_example"; // String | Server run statistics unique identifier expressed as UUID.
    ServerRunStatisticsData serverrunstatsData = new ServerRunStatisticsData(); // ServerRunStatisticsData | 
    try {
      ServerRunStatistics result = apiInstance.projectsServersRunStatsUpdate(server, project, namespace, id, serverrunstatsData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsServersRunStatsUpdate");
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
| **server** | **String**| Server unique identifier expressed as UUID or name. | |
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **id** | **String**| Server run statistics unique identifier expressed as UUID. | |
| **serverrunstatsData** | [**ServerRunStatisticsData**](ServerRunStatisticsData.md)|  | [optional] |

### Return type

[**ServerRunStatistics**](ServerRunStatistics.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ServerRunStatistics updated. |  -  |
| **400** | Invalid data supplied. |  -  |
| **404** | ServerRunStatistics not found. |  -  |

<a id="projectsServersSshTunnelsCreate"></a>
# **projectsServersSshTunnelsCreate**
> SshTunnel projectsServersSshTunnelsCreate(server, project, namespace, sshtunnelData)

Create SSH Tunnel associated to a server

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String server = "server_example"; // String | Server unique identifier expressed as UUID or name.
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    SshTunnelData sshtunnelData = new SshTunnelData(); // SshTunnelData | 
    try {
      SshTunnel result = apiInstance.projectsServersSshTunnelsCreate(server, project, namespace, sshtunnelData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsServersSshTunnelsCreate");
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
| **server** | **String**| Server unique identifier expressed as UUID or name. | |
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **sshtunnelData** | [**SshTunnelData**](SshTunnelData.md)|  | [optional] |

### Return type

[**SshTunnel**](SshTunnel.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | SSH Tunnel created. |  -  |
| **400** | Invalid data supplied. |  -  |

<a id="projectsServersSshTunnelsDelete"></a>
# **projectsServersSshTunnelsDelete**
> projectsServersSshTunnelsDelete(server, project, namespace, tunnel)

Delete an SSH Tunnel associated to a server

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String server = "server_example"; // String | Server unique identifier expressed as UUID or name.
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    String tunnel = "tunnel_example"; // String | SSH tunnel unique identifier expressed as UUID or name.
    try {
      apiInstance.projectsServersSshTunnelsDelete(server, project, namespace, tunnel);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsServersSshTunnelsDelete");
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
| **server** | **String**| Server unique identifier expressed as UUID or name. | |
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **tunnel** | **String**| SSH tunnel unique identifier expressed as UUID or name. | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | SSH tunnel deleted. |  -  |
| **404** | SSH tunnel not found. |  -  |

<a id="projectsServersSshTunnelsList"></a>
# **projectsServersSshTunnelsList**
> List&lt;SshTunnel&gt; projectsServersSshTunnelsList(server, project, namespace, limit, offset, ordering)

Get SSH Tunnels associated to a server

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String server = "server_example"; // String | Server unique identifier expressed as UUID or name.
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    String limit = "limit_example"; // String | Limit retrieved items.
    String offset = "offset_example"; // String | Offset retrieved items.
    String ordering = "ordering_example"; // String | Order retrieved items.
    try {
      List<SshTunnel> result = apiInstance.projectsServersSshTunnelsList(server, project, namespace, limit, offset, ordering);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsServersSshTunnelsList");
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
| **server** | **String**| Server unique identifier expressed as UUID or name. | |
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **limit** | **String**| Limit retrieved items. | [optional] |
| **offset** | **String**| Offset retrieved items. | [optional] |
| **ordering** | **String**| Order retrieved items. | [optional] |

### Return type

[**List&lt;SshTunnel&gt;**](SshTunnel.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | SshTunnel list |  -  |

<a id="projectsServersSshTunnelsRead"></a>
# **projectsServersSshTunnelsRead**
> SshTunnel projectsServersSshTunnelsRead(server, project, namespace, tunnel)

Get an SSH Tunnel associated to a server

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String server = "server_example"; // String | Server unique identifier expressed as UUID or name.
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    String tunnel = "tunnel_example"; // String | SSH tunnel unique identifier expressed as UUID or name.
    try {
      SshTunnel result = apiInstance.projectsServersSshTunnelsRead(server, project, namespace, tunnel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsServersSshTunnelsRead");
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
| **server** | **String**| Server unique identifier expressed as UUID or name. | |
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **tunnel** | **String**| SSH tunnel unique identifier expressed as UUID or name. | |

### Return type

[**SshTunnel**](SshTunnel.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | SSH Tunnel retrieved. |  -  |
| **404** | SSH Tunnel not found. |  -  |

<a id="projectsServersSshTunnelsReplace"></a>
# **projectsServersSshTunnelsReplace**
> SshTunnel projectsServersSshTunnelsReplace(server, project, namespace, tunnel, sshtunnelData)

Replace SSH Tunnel associated to a server

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String server = "server_example"; // String | Server unique identifier expressed as UUID or name.
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    String tunnel = "tunnel_example"; // String | SSH tunnel unique identifier expressed as UUID or name.
    SshTunnelData sshtunnelData = new SshTunnelData(); // SshTunnelData | 
    try {
      SshTunnel result = apiInstance.projectsServersSshTunnelsReplace(server, project, namespace, tunnel, sshtunnelData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsServersSshTunnelsReplace");
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
| **server** | **String**| Server unique identifier expressed as UUID or name. | |
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **tunnel** | **String**| SSH tunnel unique identifier expressed as UUID or name. | |
| **sshtunnelData** | [**SshTunnelData**](SshTunnelData.md)|  | [optional] |

### Return type

[**SshTunnel**](SshTunnel.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | SshTunnel updated |  -  |
| **400** | Invalid data supplied |  -  |

<a id="projectsServersSshTunnelsUpdate"></a>
# **projectsServersSshTunnelsUpdate**
> SshTunnel projectsServersSshTunnelsUpdate(server, project, namespace, tunnel, sshtunnelData)

Update an SSH Tunnel associated to a server

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String server = "server_example"; // String | 
    String project = "project_example"; // String | 
    String namespace = "namespace_example"; // String | User or team name.
    String tunnel = "tunnel_example"; // String | 
    SshTunnelData sshtunnelData = new SshTunnelData(); // SshTunnelData | 
    try {
      SshTunnel result = apiInstance.projectsServersSshTunnelsUpdate(server, project, namespace, tunnel, sshtunnelData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsServersSshTunnelsUpdate");
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
| **server** | **String**|  | |
| **project** | **String**|  | |
| **namespace** | **String**| User or team name. | |
| **tunnel** | **String**|  | |
| **sshtunnelData** | [**SshTunnelData**](SshTunnelData.md)|  | [optional] |

### Return type

[**SshTunnel**](SshTunnel.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  SSH Tunnel updated. |  -  |
| **400** | Invalid data supplied. |  -  |
| **404** | SSH tunnel not found. |  -  |

<a id="projectsServersStart"></a>
# **projectsServersStart**
> projectsServersStart(project, namespace, server)

Start a server

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    String server = "server_example"; // String | Server unique identifier expressed as UUID or name.
    try {
      apiInstance.projectsServersStart(project, namespace, server);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsServersStart");
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
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **server** | **String**| Server unique identifier expressed as UUID or name. | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Server started. |  -  |
| **400** | Invalid data supplied. |  -  |

<a id="projectsServersStatsDelete"></a>
# **projectsServersStatsDelete**
> projectsServersStatsDelete(server, project, namespace, id)

Delete a server&#39;s statistics

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String server = "server_example"; // String | Server unique identifier expressed as UUID or name.
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    String id = "id_example"; // String | Stats unique identifier expressed as UUID.
    try {
      apiInstance.projectsServersStatsDelete(server, project, namespace, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsServersStatsDelete");
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
| **server** | **String**| Server unique identifier expressed as UUID or name. | |
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **id** | **String**| Stats unique identifier expressed as UUID. | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | ServerStatistics deleted. |  -  |
| **404** | ServerStatistics not found. |  -  |

<a id="projectsServersStatsRead"></a>
# **projectsServersStatsRead**
> ServerStatistics projectsServersStatsRead(server, project, namespace, id)

Retrieve a server&#39;s statistics

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String server = "server_example"; // String | Server unique identifier expressed as UUID or name.
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    String id = "id_example"; // String | Server statistics unique identifier expressed as UUID.
    try {
      ServerStatistics result = apiInstance.projectsServersStatsRead(server, project, namespace, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsServersStatsRead");
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
| **server** | **String**| Server unique identifier expressed as UUID or name. | |
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **id** | **String**| Server statistics unique identifier expressed as UUID. | |

### Return type

[**ServerStatistics**](ServerStatistics.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ServerStatistics retrieved |  -  |
| **404** | ServerStatistics not found |  -  |

<a id="projectsServersStatsReplace"></a>
# **projectsServersStatsReplace**
> ServerStatistics projectsServersStatsReplace(server, project, namespace, id, serverstatsData)

Replace a server&#39;s statistics

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String server = "server_example"; // String | Server unique identifier expressed as UUID or name.
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    String id = "id_example"; // String | Server statistics unique identifier expressed as UUID.
    ServerStatisticsData serverstatsData = new ServerStatisticsData(); // ServerStatisticsData | 
    try {
      ServerStatistics result = apiInstance.projectsServersStatsReplace(server, project, namespace, id, serverstatsData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsServersStatsReplace");
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
| **server** | **String**| Server unique identifier expressed as UUID or name. | |
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **id** | **String**| Server statistics unique identifier expressed as UUID. | |
| **serverstatsData** | [**ServerStatisticsData**](ServerStatisticsData.md)|  | [optional] |

### Return type

[**ServerStatistics**](ServerStatistics.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ServerStatistics updated |  -  |
| **400** | Invalid data supplied. |  -  |

<a id="projectsServersStatsUpdate"></a>
# **projectsServersStatsUpdate**
> ServerStatistics projectsServersStatsUpdate(server, project, namespace, id, serverstatsData)

Update a server&#39;s statistics

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String server = "server_example"; // String | Server unique identifier expressed as UUID or name.
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    String id = "id_example"; // String | Server statistics unique identifier expressed as UUID.
    ServerStatisticsData serverstatsData = new ServerStatisticsData(); // ServerStatisticsData | 
    try {
      ServerStatistics result = apiInstance.projectsServersStatsUpdate(server, project, namespace, id, serverstatsData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsServersStatsUpdate");
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
| **server** | **String**| Server unique identifier expressed as UUID or name. | |
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **id** | **String**| Server statistics unique identifier expressed as UUID. | |
| **serverstatsData** | [**ServerStatisticsData**](ServerStatisticsData.md)|  | [optional] |

### Return type

[**ServerStatistics**](ServerStatistics.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ServerStatistics updated. |  -  |
| **400** | Invalid data supplied. |  -  |
| **404** | ServerStatistics not found. |  -  |

<a id="projectsServersStatuses"></a>
# **projectsServersStatuses**
> List&lt;ServerStatus&gt; projectsServersStatuses(project, namespace)

Retrieve server statuses

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    try {
      List<ServerStatus> result = apiInstance.projectsServersStatuses(project, namespace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsServersStatuses");
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
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |

### Return type

[**List&lt;ServerStatus&gt;**](ServerStatus.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Server statuses list. |  -  |

<a id="projectsServersStop"></a>
# **projectsServersStop**
> projectsServersStop(project, namespace, server)

Stop a server

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    String server = "server_example"; // String | Server unique identifier expressed as UUID or name.
    try {
      apiInstance.projectsServersStop(project, namespace, server);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsServersStop");
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
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **server** | **String**| Server unique identifier expressed as UUID or name. | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Server stopped. |  -  |
| **400** | Invalid data supplied. |  -  |

<a id="projectsServersUpdate"></a>
# **projectsServersUpdate**
> Server projectsServersUpdate(project, namespace, server, serverData)

Update a server

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    String server = "server_example"; // String | Server unique identifier expressed as UUID or name.
    ServerData serverData = new ServerData(); // ServerData | 
    try {
      Server result = apiInstance.projectsServersUpdate(project, namespace, server, serverData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsServersUpdate");
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
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **server** | **String**| Server unique identifier expressed as UUID or name. | |
| **serverData** | [**ServerData**](ServerData.md)|  | [optional] |

### Return type

[**Server**](Server.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Server updated |  -  |
| **400** | Invalid data supplied |  -  |
| **404** | Server not found |  -  |

<a id="projectsUpdate"></a>
# **projectsUpdate**
> Project projectsUpdate(namespace, project, projectData)

Update a project

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String namespace = "namespace_example"; // String | User or team name.
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    ProjectData projectData = new ProjectData(); // ProjectData | 
    try {
      Project result = apiInstance.projectsUpdate(namespace, project, projectData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsUpdate");
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
| **namespace** | **String**| User or team name. | |
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **projectData** | [**ProjectData**](ProjectData.md)|  | [optional] |

### Return type

[**Project**](Project.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Project updated |  -  |
| **400** | Invalid data supplied |  -  |
| **404** | Project not found |  -  |

<a id="serviceTriggerCreate"></a>
# **serviceTriggerCreate**
> ServerAction serviceTriggerCreate(server, project, namespace, serverAction)

Create a new server trigger

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String server = "server_example"; // String | Server unique identifier expressed as UUID or name.
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    ServerActionData serverAction = new ServerActionData(); // ServerActionData | Server action.
    try {
      ServerAction result = apiInstance.serviceTriggerCreate(server, project, namespace, serverAction);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#serviceTriggerCreate");
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
| **server** | **String**| Server unique identifier expressed as UUID or name. | |
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **serverAction** | [**ServerActionData**](ServerActionData.md)| Server action. | [optional] |

### Return type

[**ServerAction**](ServerAction.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Server action created. |  -  |
| **400** | Invalid data supplied |  -  |

<a id="serviceTriggerDelete"></a>
# **serviceTriggerDelete**
> serviceTriggerDelete(server, project, namespace, trigger)

Delete a server trigger

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String server = "server_example"; // String | Server unique identifier expressed as UUID or name.
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    String trigger = "trigger_example"; // String | Trigger identifier expressed as UUID or name.
    try {
      apiInstance.serviceTriggerDelete(server, project, namespace, trigger);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#serviceTriggerDelete");
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
| **server** | **String**| Server unique identifier expressed as UUID or name. | |
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **trigger** | **String**| Trigger identifier expressed as UUID or name. | |

### Return type

null (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | ServerAction deleted |  -  |
| **404** | ServerAction not found |  -  |

<a id="serviceTriggerList"></a>
# **serviceTriggerList**
> List&lt;ServerAction&gt; serviceTriggerList(server, project, namespace, name, limit, offset, ordering)

Retrieve server triggers

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String server = "server_example"; // String | Server unique identifier expressed as UUID or name.
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    String name = "name_example"; // String | Trigger name.
    String limit = "limit_example"; // String | Limit when getting triggers.
    String offset = "offset_example"; // String | Offset when getting triggers.
    String ordering = "ordering_example"; // String | Ordering when getting triggers.
    try {
      List<ServerAction> result = apiInstance.serviceTriggerList(server, project, namespace, name, limit, offset, ordering);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#serviceTriggerList");
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
| **server** | **String**| Server unique identifier expressed as UUID or name. | |
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **name** | **String**| Trigger name. | [optional] |
| **limit** | **String**| Limit when getting triggers. | [optional] |
| **offset** | **String**| Offset when getting triggers. | [optional] |
| **ordering** | **String**| Ordering when getting triggers. | [optional] |

### Return type

[**List&lt;ServerAction&gt;**](ServerAction.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ServerAction list |  -  |

<a id="serviceTriggerRead"></a>
# **serviceTriggerRead**
> ServerAction serviceTriggerRead(server, project, namespace, trigger)

Get a server trigger

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String server = "server_example"; // String | Server unique identifier expressed as UUID or name.
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    String trigger = "trigger_example"; // String | Trigger unique identifier.
    try {
      ServerAction result = apiInstance.serviceTriggerRead(server, project, namespace, trigger);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#serviceTriggerRead");
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
| **server** | **String**| Server unique identifier expressed as UUID or name. | |
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **trigger** | **String**| Trigger unique identifier. | |

### Return type

[**ServerAction**](ServerAction.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Server action retrieved. |  -  |
| **404** | ServerAction not found. |  -  |

<a id="serviceTriggerReplace"></a>
# **serviceTriggerReplace**
> ServerAction serviceTriggerReplace(server, project, namespace, trigger, serverAction)

Replace a server trigger

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String server = "server_example"; // String | Server unique identifier expressed as UUID or name.
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    String trigger = "trigger_example"; // String | Trigger unique identifier.
    ServerActionData serverAction = new ServerActionData(); // ServerActionData | 
    try {
      ServerAction result = apiInstance.serviceTriggerReplace(server, project, namespace, trigger, serverAction);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#serviceTriggerReplace");
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
| **server** | **String**| Server unique identifier expressed as UUID or name. | |
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **trigger** | **String**| Trigger unique identifier. | |
| **serverAction** | [**ServerActionData**](ServerActionData.md)|  | [optional] |

### Return type

[**ServerAction**](ServerAction.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | ServerAction updated. |  -  |
| **400** | Invalid data supplied. |  -  |
| **404** | Server action not found. |  -  |

<a id="serviceTriggerUpdate"></a>
# **serviceTriggerUpdate**
> ServerAction serviceTriggerUpdate(server, project, namespace, trigger, serverAction)

Update a server trigger

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
    defaultClient.setBasePath("https://api.illumidesk.com");
    
    // Configure API key authorization: jwt
    ApiKeyAuth jwt = (ApiKeyAuth) defaultClient.getAuthentication("jwt");
    jwt.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //jwt.setApiKeyPrefix("Token");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    String server = "server_example"; // String | Server unique identifier expressed as UUID or name.
    String project = "project_example"; // String | Project unique identifier expressed as UUID or name.
    String namespace = "namespace_example"; // String | User or team name.
    String trigger = "trigger_example"; // String | Trigger identifier expressed as UUID or name.
    ServerActionData serverAction = new ServerActionData(); // ServerActionData | 
    try {
      ServerAction result = apiInstance.serviceTriggerUpdate(server, project, namespace, trigger, serverAction);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#serviceTriggerUpdate");
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
| **server** | **String**| Server unique identifier expressed as UUID or name. | |
| **project** | **String**| Project unique identifier expressed as UUID or name. | |
| **namespace** | **String**| User or team name. | |
| **trigger** | **String**| Trigger identifier expressed as UUID or name. | |
| **serverAction** | [**ServerActionData**](ServerActionData.md)|  | [optional] |

### Return type

[**ServerAction**](ServerAction.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Server action updated. |  -  |
| **400** | Invalid data supplied |  -  |
| **404** | Server action not found. |  -  |

