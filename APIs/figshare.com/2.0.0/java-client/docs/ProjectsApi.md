# ProjectsApi

All URIs are relative to *https://api.figshare.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**privateProjectArticleDelete**](ProjectsApi.md#privateProjectArticleDelete) | **DELETE** /account/projects/{project_id}/articles/{article_id} | Delete project article |
| [**privateProjectArticleDetails**](ProjectsApi.md#privateProjectArticleDetails) | **GET** /account/projects/{project_id}/articles/{article_id} | Project article details |
| [**privateProjectArticleFile**](ProjectsApi.md#privateProjectArticleFile) | **GET** /account/projects/{project_id}/articles/{article_id}/files/{file_id} | Project article file details |
| [**privateProjectArticleFiles**](ProjectsApi.md#privateProjectArticleFiles) | **GET** /account/projects/{project_id}/articles/{article_id}/files | Project article list files |
| [**privateProjectArticlesCreate**](ProjectsApi.md#privateProjectArticlesCreate) | **POST** /account/projects/{project_id}/articles | Create project article |
| [**privateProjectArticlesList**](ProjectsApi.md#privateProjectArticlesList) | **GET** /account/projects/{project_id}/articles | List project articles |
| [**privateProjectCollaboratorDelete**](ProjectsApi.md#privateProjectCollaboratorDelete) | **DELETE** /account/projects/{project_id}/collaborators/{user_id} | Remove project collaborator |
| [**privateProjectCollaboratorsInvite**](ProjectsApi.md#privateProjectCollaboratorsInvite) | **POST** /account/projects/{project_id}/collaborators | Invite project collaborators |
| [**privateProjectCollaboratorsList**](ProjectsApi.md#privateProjectCollaboratorsList) | **GET** /account/projects/{project_id}/collaborators | List project collaborators |
| [**privateProjectCreate**](ProjectsApi.md#privateProjectCreate) | **POST** /account/projects | Create project |
| [**privateProjectDelete**](ProjectsApi.md#privateProjectDelete) | **DELETE** /account/projects/{project_id} | Delete project |
| [**privateProjectDetails**](ProjectsApi.md#privateProjectDetails) | **GET** /account/projects/{project_id} | View project details |
| [**privateProjectLeave**](ProjectsApi.md#privateProjectLeave) | **POST** /account/projects/{project_id}/leave | Private Project Leave |
| [**privateProjectNote**](ProjectsApi.md#privateProjectNote) | **GET** /account/projects/{project_id}/notes/{note_id} | Project note details |
| [**privateProjectNoteDelete**](ProjectsApi.md#privateProjectNoteDelete) | **DELETE** /account/projects/{project_id}/notes/{note_id} | Delete project note |
| [**privateProjectNoteUpdate**](ProjectsApi.md#privateProjectNoteUpdate) | **PUT** /account/projects/{project_id}/notes/{note_id} | Update project note |
| [**privateProjectNotesCreate**](ProjectsApi.md#privateProjectNotesCreate) | **POST** /account/projects/{project_id}/notes | Create project note |
| [**privateProjectNotesList**](ProjectsApi.md#privateProjectNotesList) | **GET** /account/projects/{project_id}/notes | List project notes |
| [**privateProjectPublish**](ProjectsApi.md#privateProjectPublish) | **POST** /account/projects/{project_id}/publish | Private Project Publish |
| [**privateProjectUpdate**](ProjectsApi.md#privateProjectUpdate) | **PUT** /account/projects/{project_id} | Update project |
| [**privateProjectsList**](ProjectsApi.md#privateProjectsList) | **GET** /account/projects | Private Projects |
| [**privateProjectsSearch**](ProjectsApi.md#privateProjectsSearch) | **POST** /account/projects/search | Private Projects search |
| [**projectArticles**](ProjectsApi.md#projectArticles) | **GET** /projects/{project_id}/articles | Public Project Articles |
| [**projectDetails**](ProjectsApi.md#projectDetails) | **GET** /projects/{project_id} | Public Project |
| [**projectsList**](ProjectsApi.md#projectsList) | **GET** /projects | Public Projects |
| [**projectsSearch**](ProjectsApi.md#projectsSearch) | **POST** /projects/search | Public Projects Search |


<a id="privateProjectArticleDelete"></a>
# **privateProjectArticleDelete**
> privateProjectArticleDelete(projectId, articleId)

Delete project article

Delete project article

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
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Long projectId = 56L; // Long | Project unique identifier
    Long articleId = 56L; // Long | Project Article unique identifier
    try {
      apiInstance.privateProjectArticleDelete(projectId, articleId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#privateProjectArticleDelete");
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
| **projectId** | **Long**| Project unique identifier | |
| **articleId** | **Long**| Project Article unique identifier | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateProjectArticleDetails"></a>
# **privateProjectArticleDetails**
> ProjectArticle privateProjectArticleDetails(projectId, articleId)

Project article details

Project article details

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
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Long projectId = 56L; // Long | Project unique identifier
    Long articleId = 56L; // Long | Project Article unique identifier
    try {
      ProjectArticle result = apiInstance.privateProjectArticleDetails(projectId, articleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#privateProjectArticleDetails");
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
| **projectId** | **Long**| Project unique identifier | |
| **articleId** | **Long**| Project Article unique identifier | |

### Return type

[**ProjectArticle**](ProjectArticle.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Article representation |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateProjectArticleFile"></a>
# **privateProjectArticleFile**
> PrivateFile privateProjectArticleFile(projectId, articleId, fileId)

Project article file details

Project article file details

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
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Long projectId = 56L; // Long | Project unique identifier
    Long articleId = 56L; // Long | Project Article unique identifier
    Long fileId = 56L; // Long | File unique identifier
    try {
      PrivateFile result = apiInstance.privateProjectArticleFile(projectId, articleId, fileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#privateProjectArticleFile");
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
| **projectId** | **Long**| Project unique identifier | |
| **articleId** | **Long**| Project Article unique identifier | |
| **fileId** | **Long**| File unique identifier | |

### Return type

[**PrivateFile**](PrivateFile.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. File representation |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateProjectArticleFiles"></a>
# **privateProjectArticleFiles**
> List&lt;PrivateFile&gt; privateProjectArticleFiles(projectId, articleId)

Project article list files

List article files

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
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Long projectId = 56L; // Long | Project unique identifier
    Long articleId = 56L; // Long | Project Article unique identifier
    try {
      List<PrivateFile> result = apiInstance.privateProjectArticleFiles(projectId, articleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#privateProjectArticleFiles");
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
| **projectId** | **Long**| Project unique identifier | |
| **articleId** | **Long**| Project Article unique identifier | |

### Return type

[**List&lt;PrivateFile&gt;**](PrivateFile.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. List of files |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateProjectArticlesCreate"></a>
# **privateProjectArticlesCreate**
> LocationWarnings privateProjectArticlesCreate(projectId, articleProjectCreate, page, pageSize, limit, offset)

Create project article

Create a new Article and associate it with this project

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
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Long projectId = 56L; // Long | Project unique identifier
    ArticleProjectCreate articleProjectCreate = new ArticleProjectCreate(); // ArticleProjectCreate | Article description
    Long page = 56L; // Long | Page number. Used for pagination with page_size
    Long pageSize = 10L; // Long | The number of results included on a page. Used for pagination with page
    Long limit = 56L; // Long | Number of results included on a page. Used for pagination with query
    Long offset = 56L; // Long | Where to start the listing(the offset of the first result). Used for pagination with limit
    try {
      LocationWarnings result = apiInstance.privateProjectArticlesCreate(projectId, articleProjectCreate, page, pageSize, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#privateProjectArticlesCreate");
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
| **projectId** | **Long**| Project unique identifier | |
| **articleProjectCreate** | [**ArticleProjectCreate**](ArticleProjectCreate.md)| Article description | |
| **page** | **Long**| Page number. Used for pagination with page_size | [optional] |
| **pageSize** | **Long**| The number of results included on a page. Used for pagination with page | [optional] [default to 10] |
| **limit** | **Long**| Number of results included on a page. Used for pagination with query | [optional] |
| **offset** | **Long**| Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] |

### Return type

[**LocationWarnings**](LocationWarnings.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  * Location - Location note <br>  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateProjectArticlesList"></a>
# **privateProjectArticlesList**
> List&lt;Article&gt; privateProjectArticlesList(projectId, page, pageSize, limit, offset)

List project articles

List project articles

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
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Long projectId = 56L; // Long | Project unique identifier
    Long page = 56L; // Long | Page number. Used for pagination with page_size
    Long pageSize = 10L; // Long | The number of results included on a page. Used for pagination with page
    Long limit = 56L; // Long | Number of results included on a page. Used for pagination with query
    Long offset = 56L; // Long | Where to start the listing(the offset of the first result). Used for pagination with limit
    try {
      List<Article> result = apiInstance.privateProjectArticlesList(projectId, page, pageSize, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#privateProjectArticlesList");
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
| **projectId** | **Long**| Project unique identifier | |
| **page** | **Long**| Page number. Used for pagination with page_size | [optional] |
| **pageSize** | **Long**| The number of results included on a page. Used for pagination with page | [optional] [default to 10] |
| **limit** | **Long**| Number of results included on a page. Used for pagination with query | [optional] |
| **offset** | **Long**| Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] |

### Return type

[**List&lt;Article&gt;**](Article.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. List of articles |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateProjectCollaboratorDelete"></a>
# **privateProjectCollaboratorDelete**
> privateProjectCollaboratorDelete(projectId, userId)

Remove project collaborator

Remove project collaborator

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
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Long projectId = 56L; // Long | Project unique identifier
    Long userId = 56L; // Long | User unique identifier
    try {
      apiInstance.privateProjectCollaboratorDelete(projectId, userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#privateProjectCollaboratorDelete");
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
| **projectId** | **Long**| Project unique identifier | |
| **userId** | **Long**| User unique identifier | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | OK |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateProjectCollaboratorsInvite"></a>
# **privateProjectCollaboratorsInvite**
> ResponseMessage privateProjectCollaboratorsInvite(projectId, projectCollaboratorInvite)

Invite project collaborators

Invite users to collaborate on project or view the project

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
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Long projectId = 56L; // Long | Project unique identifier
    ProjectCollaboratorInvite projectCollaboratorInvite = new ProjectCollaboratorInvite(); // ProjectCollaboratorInvite | viewer or collaborator role. User user_id or email of user
    try {
      ResponseMessage result = apiInstance.privateProjectCollaboratorsInvite(projectId, projectCollaboratorInvite);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#privateProjectCollaboratorsInvite");
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
| **projectId** | **Long**| Project unique identifier | |
| **projectCollaboratorInvite** | [**ProjectCollaboratorInvite**](ProjectCollaboratorInvite.md)| viewer or collaborator role. User user_id or email of user | |

### Return type

[**ResponseMessage**](ResponseMessage.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateProjectCollaboratorsList"></a>
# **privateProjectCollaboratorsList**
> List&lt;ProjectCollaborator&gt; privateProjectCollaboratorsList(projectId)

List project collaborators

List Project collaborators and invited users

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
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Long projectId = 56L; // Long | Project unique identifier
    try {
      List<ProjectCollaborator> result = apiInstance.privateProjectCollaboratorsList(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#privateProjectCollaboratorsList");
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
| **projectId** | **Long**| Project unique identifier | |

### Return type

[**List&lt;ProjectCollaborator&gt;**](ProjectCollaborator.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. List of Collaborators |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateProjectCreate"></a>
# **privateProjectCreate**
> CreateProjectResponse privateProjectCreate(projectCreate)

Create project

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
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    ProjectCreate projectCreate = new ProjectCreate(); // ProjectCreate | Project  description
    try {
      CreateProjectResponse result = apiInstance.privateProjectCreate(projectCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#privateProjectCreate");
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
| **projectCreate** | [**ProjectCreate**](ProjectCreate.md)| Project  description | |

### Return type

[**CreateProjectResponse**](CreateProjectResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateProjectDelete"></a>
# **privateProjectDelete**
> privateProjectDelete(projectId)

Delete project

A project can be deleted only if: - it is not public - it does not have public articles.  When an individual project is deleted, all the articles are moved to my data of each owner.  When a group project is deleted, all the articles and files are deleted as well. Only project owner, group admin and above can delete a project. 

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
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Long projectId = 56L; // Long | Project unique identifier
    try {
      apiInstance.privateProjectDelete(projectId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#privateProjectDelete");
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
| **projectId** | **Long**| Project unique identifier | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateProjectDetails"></a>
# **privateProjectDetails**
> ProjectCompletePrivate privateProjectDetails(projectId)

View project details

View a private project

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
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Long projectId = 56L; // Long | Project unique identifier
    try {
      ProjectCompletePrivate result = apiInstance.privateProjectDetails(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#privateProjectDetails");
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
| **projectId** | **Long**| Project unique identifier | |

### Return type

[**ProjectCompletePrivate**](ProjectCompletePrivate.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Project representation |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateProjectLeave"></a>
# **privateProjectLeave**
> privateProjectLeave(projectId)

Private Project Leave

Please note: project&#39;s owner cannot leave the project.

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
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Long projectId = 56L; // Long | Project unique identifier
    try {
      apiInstance.privateProjectLeave(projectId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#privateProjectLeave");
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
| **projectId** | **Long**| Project unique identifier | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateProjectNote"></a>
# **privateProjectNote**
> ProjectNotePrivate privateProjectNote(projectId, noteId)

Project note details

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
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Long projectId = 56L; // Long | Project unique identifier
    Long noteId = 56L; // Long | Note unique identifier
    try {
      ProjectNotePrivate result = apiInstance.privateProjectNote(projectId, noteId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#privateProjectNote");
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
| **projectId** | **Long**| Project unique identifier | |
| **noteId** | **Long**| Note unique identifier | |

### Return type

[**ProjectNotePrivate**](ProjectNotePrivate.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Note representation |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateProjectNoteDelete"></a>
# **privateProjectNoteDelete**
> privateProjectNoteDelete(projectId, noteId)

Delete project note

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
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Long projectId = 56L; // Long | Project unique identifier
    Long noteId = 56L; // Long | Note unique identifier
    try {
      apiInstance.privateProjectNoteDelete(projectId, noteId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#privateProjectNoteDelete");
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
| **projectId** | **Long**| Project unique identifier | |
| **noteId** | **Long**| Note unique identifier | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateProjectNoteUpdate"></a>
# **privateProjectNoteUpdate**
> privateProjectNoteUpdate(projectId, noteId, projectNoteCreate)

Update project note

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
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Long projectId = 56L; // Long | Project unique identifier
    Long noteId = 56L; // Long | Note unique identifier
    ProjectNoteCreate projectNoteCreate = new ProjectNoteCreate(); // ProjectNoteCreate | Note message
    try {
      apiInstance.privateProjectNoteUpdate(projectId, noteId, projectNoteCreate);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#privateProjectNoteUpdate");
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
| **projectId** | **Long**| Project unique identifier | |
| **noteId** | **Long**| Note unique identifier | |
| **projectNoteCreate** | [**ProjectNoteCreate**](ProjectNoteCreate.md)| Note message | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **205** | Reset Content |  * Location - Location note <br>  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateProjectNotesCreate"></a>
# **privateProjectNotesCreate**
> Location privateProjectNotesCreate(projectId, projectNoteCreate)

Create project note

Create a new project note

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
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Long projectId = 56L; // Long | Project unique identifier
    ProjectNoteCreate projectNoteCreate = new ProjectNoteCreate(); // ProjectNoteCreate | Note message
    try {
      Location result = apiInstance.privateProjectNotesCreate(projectId, projectNoteCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#privateProjectNotesCreate");
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
| **projectId** | **Long**| Project unique identifier | |
| **projectNoteCreate** | [**ProjectNoteCreate**](ProjectNoteCreate.md)| Note message | |

### Return type

[**Location**](Location.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  * Location - Location note <br>  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateProjectNotesList"></a>
# **privateProjectNotesList**
> List&lt;ProjectNote&gt; privateProjectNotesList(projectId, page, pageSize, limit, offset)

List project notes

List project notes

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
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Long projectId = 56L; // Long | Project unique identifier
    Long page = 56L; // Long | Page number. Used for pagination with page_size
    Long pageSize = 10L; // Long | The number of results included on a page. Used for pagination with page
    Long limit = 56L; // Long | Number of results included on a page. Used for pagination with query
    Long offset = 56L; // Long | Where to start the listing(the offset of the first result). Used for pagination with limit
    try {
      List<ProjectNote> result = apiInstance.privateProjectNotesList(projectId, page, pageSize, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#privateProjectNotesList");
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
| **projectId** | **Long**| Project unique identifier | |
| **page** | **Long**| Page number. Used for pagination with page_size | [optional] |
| **pageSize** | **Long**| The number of results included on a page. Used for pagination with page | [optional] [default to 10] |
| **limit** | **Long**| Number of results included on a page. Used for pagination with query | [optional] |
| **offset** | **Long**| Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] |

### Return type

[**List&lt;ProjectNote&gt;**](ProjectNote.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. List of project notes |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateProjectPublish"></a>
# **privateProjectPublish**
> ResponseMessage privateProjectPublish(projectId)

Private Project Publish

Publish a project. Possible after all items inside it are public

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
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Long projectId = 56L; // Long | Project unique identifier
    try {
      ResponseMessage result = apiInstance.privateProjectPublish(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#privateProjectPublish");
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
| **projectId** | **Long**| Project unique identifier | |

### Return type

[**ResponseMessage**](ResponseMessage.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateProjectUpdate"></a>
# **privateProjectUpdate**
> privateProjectUpdate(projectId, projectUpdate)

Update project

Updating an project by passing body parameters; request can also be made with the PATCH method.

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
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Long projectId = 56L; // Long | Project unique identifier
    ProjectUpdate projectUpdate = new ProjectUpdate(); // ProjectUpdate | Project description
    try {
      apiInstance.privateProjectUpdate(projectId, projectUpdate);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#privateProjectUpdate");
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
| **projectId** | **Long**| Project unique identifier | |
| **projectUpdate** | [**ProjectUpdate**](ProjectUpdate.md)| Project description | |

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **205** | Reset Content |  * Location - Location of project <br>  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateProjectsList"></a>
# **privateProjectsList**
> List&lt;ProjectPrivate&gt; privateProjectsList(page, pageSize, limit, offset, order, orderDirection, storage, roles)

Private Projects

List private projects

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
    defaultClient.setBasePath("https://api.figshare.com/v2");
    
    // Configure OAuth2 access token for authorization: OAuth2
    OAuth OAuth2 = (OAuth) defaultClient.getAuthentication("OAuth2");
    OAuth2.setAccessToken("YOUR ACCESS TOKEN");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Long page = 56L; // Long | Page number. Used for pagination with page_size
    Long pageSize = 10L; // Long | The number of results included on a page. Used for pagination with page
    Long limit = 56L; // Long | Number of results included on a page. Used for pagination with query
    Long offset = 56L; // Long | Where to start the listing(the offset of the first result). Used for pagination with limit
    String order = "published_date"; // String | The field by which to order.
    String orderDirection = "asc"; // String | 
    String storage = "group"; // String | only return collections from this institution
    String roles = "roles_example"; // String | Any combination of owner, collaborator, viewer separated by comma. Examples: \"owner\" or \"owner,collaborator\".
    try {
      List<ProjectPrivate> result = apiInstance.privateProjectsList(page, pageSize, limit, offset, order, orderDirection, storage, roles);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#privateProjectsList");
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
| **page** | **Long**| Page number. Used for pagination with page_size | [optional] |
| **pageSize** | **Long**| The number of results included on a page. Used for pagination with page | [optional] [default to 10] |
| **limit** | **Long**| Number of results included on a page. Used for pagination with query | [optional] |
| **offset** | **Long**| Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] |
| **order** | **String**| The field by which to order. | [optional] [default to published_date] [enum: published_date, modified_date, views] |
| **orderDirection** | **String**|  | [optional] [default to desc] [enum: asc, desc] |
| **storage** | **String**| only return collections from this institution | [optional] [enum: group, individual] |
| **roles** | **String**| Any combination of owner, collaborator, viewer separated by comma. Examples: \&quot;owner\&quot; or \&quot;owner,collaborator\&quot;. | [optional] |

### Return type

[**List&lt;ProjectPrivate&gt;**](ProjectPrivate.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. An array of projects |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **500** | Internal Server Error |  -  |

<a id="privateProjectsSearch"></a>
# **privateProjectsSearch**
> List&lt;ProjectPrivate&gt; privateProjectsSearch(projectsSearch)

Private Projects search

Search inside the private projects

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
    defaultClient.setBasePath("https://api.figshare.com/v2");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    ProjectsSearch projectsSearch = new ProjectsSearch(); // ProjectsSearch | Search Parameters
    try {
      List<ProjectPrivate> result = apiInstance.privateProjectsSearch(projectsSearch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#privateProjectsSearch");
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
| **projectsSearch** | [**ProjectsSearch**](ProjectsSearch.md)| Search Parameters | [optional] |

### Return type

[**List&lt;ProjectPrivate&gt;**](ProjectPrivate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. An array of projects |  -  |
| **400** | Bad Request |  -  |
| **422** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |

<a id="projectArticles"></a>
# **projectArticles**
> List&lt;Article&gt; projectArticles(projectId)

Public Project Articles

List articles in project

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
    defaultClient.setBasePath("https://api.figshare.com/v2");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Long projectId = 56L; // Long | Project Unique identifier
    try {
      List<Article> result = apiInstance.projectArticles(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectArticles");
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
| **projectId** | **Long**| Project Unique identifier | |

### Return type

[**List&lt;Article&gt;**](Article.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Project articles list |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="projectDetails"></a>
# **projectDetails**
> ProjectComplete projectDetails(projectId)

Public Project

View a project

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
    defaultClient.setBasePath("https://api.figshare.com/v2");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    Long projectId = 56L; // Long | Project Unique identifier
    try {
      ProjectComplete result = apiInstance.projectDetails(projectId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectDetails");
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
| **projectId** | **Long**| Project Unique identifier | |

### Return type

[**ProjectComplete**](ProjectComplete.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. Project representation |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

<a id="projectsList"></a>
# **projectsList**
> List&lt;Project&gt; projectsList(xCursor, page, pageSize, limit, offset, order, orderDirection, institution, publishedSince, group)

Public Projects

Returns a list of public projects

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
    defaultClient.setBasePath("https://api.figshare.com/v2");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    UUID xCursor = UUID.randomUUID(); // UUID | Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected.
    Long page = 56L; // Long | Page number. Used for pagination with page_size
    Long pageSize = 10L; // Long | The number of results included on a page. Used for pagination with page
    Long limit = 56L; // Long | Number of results included on a page. Used for pagination with query
    Long offset = 56L; // Long | Where to start the listing(the offset of the first result). Used for pagination with limit
    String order = "published_date"; // String | The field by which to order. Default varies by endpoint/resource.
    String orderDirection = "asc"; // String | 
    Long institution = 56L; // Long | only return collections from this institution
    String publishedSince = "publishedSince_example"; // String | Filter by article publishing date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD
    Long group = 56L; // Long | only return collections from this group
    try {
      List<Project> result = apiInstance.projectsList(xCursor, page, pageSize, limit, offset, order, orderDirection, institution, publishedSince, group);
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
| **xCursor** | **UUID**| Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected. | [optional] |
| **page** | **Long**| Page number. Used for pagination with page_size | [optional] |
| **pageSize** | **Long**| The number of results included on a page. Used for pagination with page | [optional] [default to 10] |
| **limit** | **Long**| Number of results included on a page. Used for pagination with query | [optional] |
| **offset** | **Long**| Where to start the listing(the offset of the first result). Used for pagination with limit | [optional] |
| **order** | **String**| The field by which to order. Default varies by endpoint/resource. | [optional] [default to published_date] [enum: published_date, modified_date, views] |
| **orderDirection** | **String**|  | [optional] [default to desc] [enum: asc, desc] |
| **institution** | **Long**| only return collections from this institution | [optional] |
| **publishedSince** | **String**| Filter by article publishing date. Will only return articles published after the date. date(ISO 8601) YYYY-MM-DD | [optional] |
| **group** | **Long**| only return collections from this group | [optional] |

### Return type

[**List&lt;Project&gt;**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. An array of projects |  * X-Cursor - Unique hash used for bypassing the item retrieval limit of 9,000 entities. <br>  |
| **400** | Bad Request |  -  |
| **422** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |

<a id="projectsSearch"></a>
# **projectsSearch**
> List&lt;Project&gt; projectsSearch(xCursor, projectsSearch)

Public Projects Search

Returns a list of public articles

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
    defaultClient.setBasePath("https://api.figshare.com/v2");

    ProjectsApi apiInstance = new ProjectsApi(defaultClient);
    UUID xCursor = UUID.randomUUID(); // UUID | Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected.
    ProjectsSearch projectsSearch = new ProjectsSearch(); // ProjectsSearch | Search Parameters
    try {
      List<Project> result = apiInstance.projectsSearch(xCursor, projectsSearch);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectsApi#projectsSearch");
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
| **xCursor** | **UUID**| Unique hash used for bypassing the item retrieval limit of 9,000 entities. When using this parameter, please note that the offset parameter will not be available, but the limit parameter will still work as expected. | [optional] |
| **projectsSearch** | [**ProjectsSearch**](ProjectsSearch.md)| Search Parameters | [optional] |

### Return type

[**List&lt;Project&gt;**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK. An array of projects |  * X-Cursor - Unique hash used for bypassing the item retrieval limit of 9,000 entities. <br>  |
| **400** | Bad Request |  -  |
| **422** | Bad Request |  -  |
| **500** | Internal Server Error |  -  |

