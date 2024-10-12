# IssueTrackerApi

All URIs are relative to *https://api.bitbucket.org/2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**repositoriesWorkspaceRepoSlugComponentsComponentIdGet**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugComponentsComponentIdGet) | **GET** /repositories/{workspace}/{repo_slug}/components/{component_id} | Get a component for issues |
| [**repositoriesWorkspaceRepoSlugComponentsGet**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugComponentsGet) | **GET** /repositories/{workspace}/{repo_slug}/components | List components |
| [**repositoriesWorkspaceRepoSlugIssuesExportPost**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugIssuesExportPost) | **POST** /repositories/{workspace}/{repo_slug}/issues/export | Export issues |
| [**repositoriesWorkspaceRepoSlugIssuesExportRepoNameIssuesTaskIdZipGet**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugIssuesExportRepoNameIssuesTaskIdZipGet) | **GET** /repositories/{workspace}/{repo_slug}/issues/export/{repo_name}-issues-{task_id}.zip | Check issue export status |
| [**repositoriesWorkspaceRepoSlugIssuesGet**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugIssuesGet) | **GET** /repositories/{workspace}/{repo_slug}/issues | List issues |
| [**repositoriesWorkspaceRepoSlugIssuesImportGet**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugIssuesImportGet) | **GET** /repositories/{workspace}/{repo_slug}/issues/import | Check issue import status |
| [**repositoriesWorkspaceRepoSlugIssuesImportPost**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugIssuesImportPost) | **POST** /repositories/{workspace}/{repo_slug}/issues/import | Import issues |
| [**repositoriesWorkspaceRepoSlugIssuesIssueIdAttachmentsGet**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugIssuesIssueIdAttachmentsGet) | **GET** /repositories/{workspace}/{repo_slug}/issues/{issue_id}/attachments | List attachments for an issue |
| [**repositoriesWorkspaceRepoSlugIssuesIssueIdAttachmentsPathDelete**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugIssuesIssueIdAttachmentsPathDelete) | **DELETE** /repositories/{workspace}/{repo_slug}/issues/{issue_id}/attachments/{path} | Delete an attachment for an issue |
| [**repositoriesWorkspaceRepoSlugIssuesIssueIdAttachmentsPathGet**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugIssuesIssueIdAttachmentsPathGet) | **GET** /repositories/{workspace}/{repo_slug}/issues/{issue_id}/attachments/{path} | Get attachment for an issue |
| [**repositoriesWorkspaceRepoSlugIssuesIssueIdAttachmentsPost**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugIssuesIssueIdAttachmentsPost) | **POST** /repositories/{workspace}/{repo_slug}/issues/{issue_id}/attachments | Upload an attachment to an issue |
| [**repositoriesWorkspaceRepoSlugIssuesIssueIdChangesChangeIdGet**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugIssuesIssueIdChangesChangeIdGet) | **GET** /repositories/{workspace}/{repo_slug}/issues/{issue_id}/changes/{change_id} | Get issue change object |
| [**repositoriesWorkspaceRepoSlugIssuesIssueIdChangesGet**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugIssuesIssueIdChangesGet) | **GET** /repositories/{workspace}/{repo_slug}/issues/{issue_id}/changes | List changes on an issue |
| [**repositoriesWorkspaceRepoSlugIssuesIssueIdChangesPost**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugIssuesIssueIdChangesPost) | **POST** /repositories/{workspace}/{repo_slug}/issues/{issue_id}/changes | Modify the state of an issue |
| [**repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsCommentIdDelete**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsCommentIdDelete) | **DELETE** /repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments/{comment_id} | Delete a comment on an issue |
| [**repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsCommentIdGet**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsCommentIdGet) | **GET** /repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments/{comment_id} | Get a comment on an issue |
| [**repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsCommentIdPut**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsCommentIdPut) | **PUT** /repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments/{comment_id} | Update a comment on an issue |
| [**repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsGet**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsGet) | **GET** /repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments | List comments on an issue |
| [**repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsPost**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsPost) | **POST** /repositories/{workspace}/{repo_slug}/issues/{issue_id}/comments | Create a comment on an issue |
| [**repositoriesWorkspaceRepoSlugIssuesIssueIdDelete**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugIssuesIssueIdDelete) | **DELETE** /repositories/{workspace}/{repo_slug}/issues/{issue_id} | Delete an issue |
| [**repositoriesWorkspaceRepoSlugIssuesIssueIdGet**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugIssuesIssueIdGet) | **GET** /repositories/{workspace}/{repo_slug}/issues/{issue_id} | Get an issue |
| [**repositoriesWorkspaceRepoSlugIssuesIssueIdPut**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugIssuesIssueIdPut) | **PUT** /repositories/{workspace}/{repo_slug}/issues/{issue_id} | Update an issue |
| [**repositoriesWorkspaceRepoSlugIssuesIssueIdVoteDelete**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugIssuesIssueIdVoteDelete) | **DELETE** /repositories/{workspace}/{repo_slug}/issues/{issue_id}/vote | Remove vote for an issue |
| [**repositoriesWorkspaceRepoSlugIssuesIssueIdVoteGet**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugIssuesIssueIdVoteGet) | **GET** /repositories/{workspace}/{repo_slug}/issues/{issue_id}/vote | Check if current user voted for an issue |
| [**repositoriesWorkspaceRepoSlugIssuesIssueIdVotePut**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugIssuesIssueIdVotePut) | **PUT** /repositories/{workspace}/{repo_slug}/issues/{issue_id}/vote | Vote for an issue |
| [**repositoriesWorkspaceRepoSlugIssuesIssueIdWatchDelete**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugIssuesIssueIdWatchDelete) | **DELETE** /repositories/{workspace}/{repo_slug}/issues/{issue_id}/watch | Stop watching an issue |
| [**repositoriesWorkspaceRepoSlugIssuesIssueIdWatchGet**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugIssuesIssueIdWatchGet) | **GET** /repositories/{workspace}/{repo_slug}/issues/{issue_id}/watch | Check if current user is watching a issue |
| [**repositoriesWorkspaceRepoSlugIssuesIssueIdWatchPut**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugIssuesIssueIdWatchPut) | **PUT** /repositories/{workspace}/{repo_slug}/issues/{issue_id}/watch | Watch an issue |
| [**repositoriesWorkspaceRepoSlugIssuesPost**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugIssuesPost) | **POST** /repositories/{workspace}/{repo_slug}/issues | Create an issue |
| [**repositoriesWorkspaceRepoSlugMilestonesGet**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugMilestonesGet) | **GET** /repositories/{workspace}/{repo_slug}/milestones | List milestones |
| [**repositoriesWorkspaceRepoSlugMilestonesMilestoneIdGet**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugMilestonesMilestoneIdGet) | **GET** /repositories/{workspace}/{repo_slug}/milestones/{milestone_id} | Get a milestone |
| [**repositoriesWorkspaceRepoSlugVersionsGet**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugVersionsGet) | **GET** /repositories/{workspace}/{repo_slug}/versions | List defined versions for issues |
| [**repositoriesWorkspaceRepoSlugVersionsVersionIdGet**](IssueTrackerApi.md#repositoriesWorkspaceRepoSlugVersionsVersionIdGet) | **GET** /repositories/{workspace}/{repo_slug}/versions/{version_id} | Get a defined version for issues |


<a id="repositoriesWorkspaceRepoSlugComponentsComponentIdGet"></a>
# **repositoriesWorkspaceRepoSlugComponentsComponentIdGet**
> Component repositoriesWorkspaceRepoSlugComponentsComponentIdGet(componentId, repoSlug, workspace)

Get a component for issues

Returns the specified issue tracker component object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    Integer componentId = 56; // Integer | The component's id
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      Component result = apiInstance.repositoriesWorkspaceRepoSlugComponentsComponentIdGet(componentId, repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugComponentsComponentIdGet");
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
| **componentId** | **Integer**| The component&#39;s id | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**Component**](Component.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The specified component object. |  -  |
| **404** | The specified repository or component does not exist or does not have the issue tracker enabled. |  -  |

<a id="repositoriesWorkspaceRepoSlugComponentsGet"></a>
# **repositoriesWorkspaceRepoSlugComponentsGet**
> PaginatedComponents repositoriesWorkspaceRepoSlugComponentsGet(repoSlug, workspace)

List components

Returns the components that have been defined in the issue tracker.  This resource is only available on repositories that have the issue tracker enabled.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      PaginatedComponents result = apiInstance.repositoriesWorkspaceRepoSlugComponentsGet(repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugComponentsGet");
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
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**PaginatedComponents**](PaginatedComponents.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The components that have been defined in the issue tracker. |  -  |
| **404** | The specified repository does not exist or does not have the issue tracker enabled. |  -  |

<a id="repositoriesWorkspaceRepoSlugIssuesExportPost"></a>
# **repositoriesWorkspaceRepoSlugIssuesExportPost**
> repositoriesWorkspaceRepoSlugIssuesExportPost(repoSlug, workspace, exportOptions)

Export issues

A POST request to this endpoint initiates a new background celery task that archives the repo&#39;s issues.  For example, you can run:  curl -u &lt;username&gt; -X POST http://api.bitbucket.org/2.0/repositories/&lt;owner_username&gt;/&lt;repo_slug&gt;/ issues/export  When the job has been accepted, it will return a 202 (Accepted) along with a unique url to this job in the &#39;Location&#39; response header. This url is the endpoint for where the user can obtain their zip files.\&quot;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    ExportOptions exportOptions = new ExportOptions(); // ExportOptions | The options to apply to the export. Available options include `project_key` and `project_name` which, if specified, are used as the project key and name in the exported Jira json format. Option `send_email` specifies whether an email should be sent upon export result. Option `include_attachments` specifies whether attachments are included in the export.
    try {
      apiInstance.repositoriesWorkspaceRepoSlugIssuesExportPost(repoSlug, workspace, exportOptions);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugIssuesExportPost");
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
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |
| **exportOptions** | [**ExportOptions**](ExportOptions.md)| The options to apply to the export. Available options include &#x60;project_key&#x60; and &#x60;project_name&#x60; which, if specified, are used as the project key and name in the exported Jira json format. Option &#x60;send_email&#x60; specifies whether an email should be sent upon export result. Option &#x60;include_attachments&#x60; specifies whether attachments are included in the export. | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | The export job has been accepted |  -  |
| **401** | The request wasn&#39;t authenticated properly |  -  |
| **403** | When the authenticated user does not have admin permission on the repo |  -  |
| **404** | The repo does not exist or does not have an issue tracker |  -  |

<a id="repositoriesWorkspaceRepoSlugIssuesExportRepoNameIssuesTaskIdZipGet"></a>
# **repositoriesWorkspaceRepoSlugIssuesExportRepoNameIssuesTaskIdZipGet**
> IssueJobStatus repositoriesWorkspaceRepoSlugIssuesExportRepoNameIssuesTaskIdZipGet(repoName, repoSlug, taskId, workspace)

Check issue export status

This endpoint is used to poll for the progress of an issue export job and return the zip file after the job is complete. As long as the job is running, this will return a 200 response with in the response body a description of the current status.  After the job has been scheduled, but before it starts executing, this endpoint&#39;s response is:  {  \&quot;type\&quot;: \&quot;issue_job_status\&quot;,  \&quot;status\&quot;: \&quot;ACCEPTED\&quot;,  \&quot;phase\&quot;: \&quot;Initializing\&quot;,  \&quot;total\&quot;: 0,  \&quot;count\&quot;: 0,  \&quot;pct\&quot;: 0 }   Then once it starts running, it becomes:  {  \&quot;type\&quot;: \&quot;issue_job_status\&quot;,  \&quot;status\&quot;: \&quot;STARTED\&quot;,  \&quot;phase\&quot;: \&quot;Attachments\&quot;,  \&quot;total\&quot;: 15,  \&quot;count\&quot;: 11,  \&quot;pct\&quot;: 73 }  Once the job has successfully completed, it returns a stream of the zip file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    String repoName = "repoName_example"; // String | The name of the repo
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String taskId = "taskId_example"; // String | The ID of the export task
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      IssueJobStatus result = apiInstance.repositoriesWorkspaceRepoSlugIssuesExportRepoNameIssuesTaskIdZipGet(repoName, repoSlug, taskId, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugIssuesExportRepoNameIssuesTaskIdZipGet");
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
| **repoName** | **String**| The name of the repo | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **taskId** | **String**| The ID of the export task | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**IssueJobStatus**](IssueJobStatus.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Export job accepted |  -  |
| **401** | The request wasn&#39;t authenticated properly |  -  |
| **403** | When the authenticated user does not have admin permission on the repo |  -  |
| **404** | No export job has begun |  -  |

<a id="repositoriesWorkspaceRepoSlugIssuesGet"></a>
# **repositoriesWorkspaceRepoSlugIssuesGet**
> PaginatedIssues repositoriesWorkspaceRepoSlugIssuesGet(repoSlug, workspace)

List issues

Returns the issues in the issue tracker.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      PaginatedIssues result = apiInstance.repositoriesWorkspaceRepoSlugIssuesGet(repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugIssuesGet");
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
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**PaginatedIssues**](PaginatedIssues.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of the issues matching any filter criteria that were provided. |  -  |
| **404** | The specified repository does not exist or does not have the issue tracker enabled. |  -  |

<a id="repositoriesWorkspaceRepoSlugIssuesImportGet"></a>
# **repositoriesWorkspaceRepoSlugIssuesImportGet**
> IssueJobStatus repositoriesWorkspaceRepoSlugIssuesImportGet(repoSlug, workspace)

Check issue import status

When using GET, this endpoint reports the status of the current import task. Request example:  &#x60;&#x60;&#x60; $ curl -u &lt;username&gt; -X GET https://api.bitbucket.org/2.0/repositories/&lt;owner_username&gt;/&lt;repo_slug&gt;/issues/import &#x60;&#x60;&#x60;  After the job has been scheduled, but before it starts executing, this endpoint&#39;s response is:  &#x60;&#x60;&#x60; &lt; HTTP/1.1 202 Accepted {     \&quot;type\&quot;: \&quot;issue_job_status\&quot;,     \&quot;status\&quot;: \&quot;PENDING\&quot;,     \&quot;phase\&quot;: \&quot;Attachments\&quot;,     \&quot;total\&quot;: 15,     \&quot;count\&quot;: 0,     \&quot;percent\&quot;: 0 } &#x60;&#x60;&#x60;  Once it starts running, it is a 202 response with status STARTED and progress filled.  After it is finished, it becomes a 200 response with status SUCCESS or FAILURE.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      IssueJobStatus result = apiInstance.repositoriesWorkspaceRepoSlugIssuesImportGet(repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugIssuesImportGet");
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
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**IssueJobStatus**](IssueJobStatus.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Import job complete with either FAILURE or SUCCESS status |  -  |
| **202** | Import job started |  -  |
| **401** | The request wasn&#39;t authenticated properly |  -  |
| **403** | When the authenticated user does not have admin permission on the repo |  -  |
| **404** | No export job has begun |  -  |

<a id="repositoriesWorkspaceRepoSlugIssuesImportPost"></a>
# **repositoriesWorkspaceRepoSlugIssuesImportPost**
> IssueJobStatus repositoriesWorkspaceRepoSlugIssuesImportPost(repoSlug, workspace)

Import issues

A POST request to this endpoint will import the zip file given by the archive parameter into the repository. All existing issues will be deleted and replaced by the contents of the imported zip file.  Imports are done through a multipart/form-data POST. There is one valid and required form field, with the name \&quot;archive,\&quot; which needs to be a file field:  &#x60;&#x60;&#x60; $ curl -u &lt;username&gt; -X POST -F archive&#x3D;@/path/to/file.zip https://api.bitbucket.org/2.0/repositories/&lt;owner_username&gt;/&lt;repo_slug&gt;/issues/import &#x60;&#x60;&#x60;  When the import job is accepted, here is example output:  &#x60;&#x60;&#x60; &lt; HTTP/1.1 202 Accepted  {     \&quot;type\&quot;: \&quot;issue_job_status\&quot;,     \&quot;status\&quot;: \&quot;ACCEPTED\&quot;,     \&quot;phase\&quot;: \&quot;Attachments\&quot;,     \&quot;total\&quot;: 15,     \&quot;count\&quot;: 0,     \&quot;percent\&quot;: 0 } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      IssueJobStatus result = apiInstance.repositoriesWorkspaceRepoSlugIssuesImportPost(repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugIssuesImportPost");
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
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**IssueJobStatus**](IssueJobStatus.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Import job accepted |  -  |
| **401** | The request wasn&#39;t authenticated properly |  -  |
| **403** | When the authenticated user does not have admin permission on the repo |  -  |
| **404** | No export job has begun |  -  |
| **409** | Import already running |  -  |

<a id="repositoriesWorkspaceRepoSlugIssuesIssueIdAttachmentsGet"></a>
# **repositoriesWorkspaceRepoSlugIssuesIssueIdAttachmentsGet**
> PaginatedIssueAttachments repositoriesWorkspaceRepoSlugIssuesIssueIdAttachmentsGet(issueId, repoSlug, workspace)

List attachments for an issue

Returns all attachments for this issue.  This returns the files&#39; meta data. This does not return the files&#39; actual contents.  The files are always ordered by their upload date.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    String issueId = "issueId_example"; // String | The issue id
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      PaginatedIssueAttachments result = apiInstance.repositoriesWorkspaceRepoSlugIssuesIssueIdAttachmentsGet(issueId, repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugIssuesIssueIdAttachmentsGet");
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
| **issueId** | **String**| The issue id | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**PaginatedIssueAttachments**](PaginatedIssueAttachments.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of all attachments for this issue. |  -  |
| **401** | If the issue tracker is private and the request was not authenticated. |  -  |
| **404** | The specified repository or issue does not exist or does not have the issue tracker enabled. |  -  |

<a id="repositoriesWorkspaceRepoSlugIssuesIssueIdAttachmentsPathDelete"></a>
# **repositoriesWorkspaceRepoSlugIssuesIssueIdAttachmentsPathDelete**
> repositoriesWorkspaceRepoSlugIssuesIssueIdAttachmentsPathDelete(issueId, path, repoSlug, workspace)

Delete an attachment for an issue

Deletes an attachment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    String issueId = "issueId_example"; // String | The issue id
    String path = "path_example"; // String | Path to the file.
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      apiInstance.repositoriesWorkspaceRepoSlugIssuesIssueIdAttachmentsPathDelete(issueId, path, repoSlug, workspace);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugIssuesIssueIdAttachmentsPathDelete");
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
| **issueId** | **String**| The issue id | |
| **path** | **String**| Path to the file. | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Indicates that the deletion was successful |  -  |
| **401** | If the issue tracker is private and the request was not authenticated. |  -  |
| **404** | The specified repository or issue does not exist or does not have the issue tracker enabled. |  -  |

<a id="repositoriesWorkspaceRepoSlugIssuesIssueIdAttachmentsPathGet"></a>
# **repositoriesWorkspaceRepoSlugIssuesIssueIdAttachmentsPathGet**
> repositoriesWorkspaceRepoSlugIssuesIssueIdAttachmentsPathGet(issueId, path, repoSlug, workspace)

Get attachment for an issue

Returns the contents of the specified file attachment.  Note that this endpoint does not return a JSON response, but instead returns a redirect pointing to the actual file that in turn will return the raw contents.  The redirect URL contains a one-time token that has a limited lifetime. As a result, the link should not be persisted, stored, or shared.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    String issueId = "issueId_example"; // String | The issue id
    String path = "path_example"; // String | Path to the file.
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      apiInstance.repositoriesWorkspaceRepoSlugIssuesIssueIdAttachmentsPathGet(issueId, path, repoSlug, workspace);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugIssuesIssueIdAttachmentsPathGet");
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
| **issueId** | **String**| The issue id | |
| **path** | **String**| Path to the file. | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **302** | A redirect to the file&#39;s contents |  * Location - The location of the project. This header is only provided when the project key is updated. <br>  |
| **401** | If the issue tracker is private and the request was not authenticated. |  -  |
| **404** | The specified repository or issue does not exist or does not have the issue tracker enabled. |  -  |

<a id="repositoriesWorkspaceRepoSlugIssuesIssueIdAttachmentsPost"></a>
# **repositoriesWorkspaceRepoSlugIssuesIssueIdAttachmentsPost**
> repositoriesWorkspaceRepoSlugIssuesIssueIdAttachmentsPost(issueId, repoSlug, workspace)

Upload an attachment to an issue

Upload new issue attachments.  To upload files, perform a &#x60;multipart/form-data&#x60; POST containing one or more file fields.  When a file is uploaded with the same name as an existing attachment, then the existing file will be replaced.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    String issueId = "issueId_example"; // String | The issue id
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      apiInstance.repositoriesWorkspaceRepoSlugIssuesIssueIdAttachmentsPost(issueId, repoSlug, workspace);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugIssuesIssueIdAttachmentsPost");
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
| **issueId** | **String**| The issue id | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | An empty response document. |  * Location - The location of the project. This header is only provided when the project key is updated. <br>  |
| **400** | If no files were uploaded, or if the wrong &#x60;Content-Type&#x60; was used. |  -  |
| **401** | If the issue tracker is private and the request was not authenticated. |  -  |
| **404** | The specified repository or issue does not exist or does not have the issue tracker enabled. |  -  |

<a id="repositoriesWorkspaceRepoSlugIssuesIssueIdChangesChangeIdGet"></a>
# **repositoriesWorkspaceRepoSlugIssuesIssueIdChangesChangeIdGet**
> IssueChange repositoriesWorkspaceRepoSlugIssuesIssueIdChangesChangeIdGet(changeId, issueId, repoSlug, workspace)

Get issue change object

Returns the specified issue change object.  This resource is only available on repositories that have the issue tracker enabled.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    String changeId = "changeId_example"; // String | The issue change id
    String issueId = "issueId_example"; // String | The issue id
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      IssueChange result = apiInstance.repositoriesWorkspaceRepoSlugIssuesIssueIdChangesChangeIdGet(changeId, issueId, repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugIssuesIssueIdChangesChangeIdGet");
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
| **changeId** | **String**| The issue change id | |
| **issueId** | **String**| The issue id | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**IssueChange**](IssueChange.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The specified issue change object. |  -  |
| **404** | The specified repository or issue change does not exist or does not have the issue tracker enabled. |  -  |

<a id="repositoriesWorkspaceRepoSlugIssuesIssueIdChangesGet"></a>
# **repositoriesWorkspaceRepoSlugIssuesIssueIdChangesGet**
> PaginatedLogEntries repositoriesWorkspaceRepoSlugIssuesIssueIdChangesGet(issueId, repoSlug, workspace, q, sort)

List changes on an issue

Returns the list of all changes that have been made to the specified issue. Changes are returned in chronological order with the oldest change first.  Each time an issue is edited in the UI or through the API, an immutable change record is created under the &#x60;/issues/123/changes&#x60; endpoint. It also has a comment associated with the change.  Note that this operation is changing significantly, due to privacy changes. See the [announcement](https://developer.atlassian.com/cloud/bitbucket/bitbucket-api-changes-gdpr/#changes-to-the-issue-changes-api) for details.  &#x60;&#x60;&#x60; $ curl -s https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/issues/1/changes - | jq .  {   \&quot;pagelen\&quot;: 20,   \&quot;values\&quot;: [     {       \&quot;changes\&quot;: {         \&quot;priority\&quot;: {           \&quot;new\&quot;: \&quot;trivial\&quot;,           \&quot;old\&quot;: \&quot;major\&quot;         },         \&quot;assignee\&quot;: {           \&quot;new\&quot;: \&quot;\&quot;,           \&quot;old\&quot;: \&quot;evzijst\&quot;         },         \&quot;assignee_account_id\&quot;: {           \&quot;new\&quot;: \&quot;\&quot;,           \&quot;old\&quot;: \&quot;557058:c0b72ad0-1cb5-4018-9cdc-0cde8492c443\&quot;         },         \&quot;kind\&quot;: {           \&quot;new\&quot;: \&quot;enhancement\&quot;,           \&quot;old\&quot;: \&quot;bug\&quot;         }       },       \&quot;links\&quot;: {         \&quot;self\&quot;: {           \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/issues/1/changes/2\&quot;         },         \&quot;html\&quot;: {           \&quot;href\&quot;: \&quot;https://bitbucket.org/evzijst/dogslow/issues/1#comment-2\&quot;         }       },       \&quot;issue\&quot;: {         \&quot;links\&quot;: {           \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/evzijst/dogslow/issues/1\&quot;           }         },         \&quot;type\&quot;: \&quot;issue\&quot;,         \&quot;id\&quot;: 1,         \&quot;repository\&quot;: {           \&quot;links\&quot;: {             \&quot;self\&quot;: {               \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/repositories/evzijst/dogslow\&quot;             },             \&quot;html\&quot;: {               \&quot;href\&quot;: \&quot;https://bitbucket.org/evzijst/dogslow\&quot;             },             \&quot;avatar\&quot;: {               \&quot;href\&quot;: \&quot;https://bitbucket.org/evzijst/dogslow/avatar/32/\&quot;             }           },           \&quot;type\&quot;: \&quot;repository\&quot;,           \&quot;name\&quot;: \&quot;dogslow\&quot;,           \&quot;full_name\&quot;: \&quot;evzijst/dogslow\&quot;,           \&quot;uuid\&quot;: \&quot;{988b17c6-1a47-4e70-84ee-854d5f012bf6}\&quot;         },         \&quot;title\&quot;: \&quot;Updated title\&quot;       },       \&quot;created_on\&quot;: \&quot;2018-03-03T00:35:28.353630+00:00\&quot;,       \&quot;user\&quot;: {         \&quot;username\&quot;: \&quot;evzijst\&quot;,         \&quot;nickname\&quot;: \&quot;evzijst\&quot;,         \&quot;display_name\&quot;: \&quot;evzijst\&quot;,         \&quot;type\&quot;: \&quot;user\&quot;,         \&quot;uuid\&quot;: \&quot;{aaa7972b-38af-4fb1-802d-6e3854c95778}\&quot;,         \&quot;links\&quot;: {           \&quot;self\&quot;: {             \&quot;href\&quot;: \&quot;https://api.bitbucket.org/2.0/users/evzijst\&quot;           },           \&quot;html\&quot;: {             \&quot;href\&quot;: \&quot;https://bitbucket.org/evzijst/\&quot;           },           \&quot;avatar\&quot;: {             \&quot;href\&quot;: \&quot;https://bitbucket.org/account/evzijst/avatar/32/\&quot;           }         }       },       \&quot;message\&quot;: {         \&quot;raw\&quot;: \&quot;Removed assignee, changed kind and priority.\&quot;,         \&quot;markup\&quot;: \&quot;markdown\&quot;,         \&quot;html\&quot;: \&quot;&lt;p&gt;Removed assignee, changed kind and priority.&lt;/p&gt;\&quot;,         \&quot;type\&quot;: \&quot;rendered\&quot;       },       \&quot;type\&quot;: \&quot;issue_change\&quot;,       \&quot;id\&quot;: 2     }   ],   \&quot;page\&quot;: 1 } &#x60;&#x60;&#x60;  Changes support [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) that can be used to search for specific changes. For instance, to see when an issue transitioned to \&quot;resolved\&quot;:  &#x60;&#x60;&#x60; $ curl -s https://api.bitbucket.org/2.0/repositories/site/master/issues/1/changes \\    -G --data-urlencode&#x3D;&#39;q&#x3D;changes.state.new &#x3D; \&quot;resolved\&quot;&#39; &#x60;&#x60;&#x60;  This resource is only available on repositories that have the issue tracker enabled.  N.B.  The &#x60;changes.assignee&#x60; and &#x60;changes.assignee_account_id&#x60; fields are not a &#x60;user&#x60; object. Instead, they contain the raw &#x60;username&#x60; and &#x60;account_id&#x60; of the user. This is to protect the integrity of the audit log even after a user account gets deleted.  The &#x60;changes.assignee&#x60; field is deprecated will disappear in the future. Use &#x60;changes.assignee_account_id&#x60; instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    String issueId = "issueId_example"; // String | The issue id
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    String q = "q_example"; // String |  Query string to narrow down the response. See [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for details.
    String sort = "sort_example"; // String |  Name of a response property to sort results. See [filtering and sorting](/cloud/bitbucket/rest/intro/#sorting-query-results) for details. 
    try {
      PaginatedLogEntries result = apiInstance.repositoriesWorkspaceRepoSlugIssuesIssueIdChangesGet(issueId, repoSlug, workspace, q, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugIssuesIssueIdChangesGet");
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
| **issueId** | **String**| The issue id | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |
| **q** | **String**|  Query string to narrow down the response. See [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for details. | [optional] |
| **sort** | **String**|  Name of a response property to sort results. See [filtering and sorting](/cloud/bitbucket/rest/intro/#sorting-query-results) for details.  | [optional] |

### Return type

[**PaginatedLogEntries**](PaginatedLogEntries.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns all the issue changes that were made on the specified issue. |  -  |
| **404** | The specified repository or issue does not exist or does not have the issue tracker enabled. |  -  |

<a id="repositoriesWorkspaceRepoSlugIssuesIssueIdChangesPost"></a>
# **repositoriesWorkspaceRepoSlugIssuesIssueIdChangesPost**
> IssueChange repositoriesWorkspaceRepoSlugIssuesIssueIdChangesPost(issueId, repoSlug, workspace, issueChange)

Modify the state of an issue

Makes a change to the specified issue.  For example, to change an issue&#39;s state and assignee, create a new change object that modifies these fields:  &#x60;&#x60;&#x60; curl https://api.bitbucket.org/2.0/site/master/issues/1234/changes \\   -s -u evzijst -X POST -H \&quot;Content-Type: application/json\&quot; \\   -d &#39;{     \&quot;changes\&quot;: {       \&quot;assignee_account_id\&quot;: {         \&quot;new\&quot;: \&quot;557058:c0b72ad0-1cb5-4018-9cdc-0cde8492c443\&quot;       },       \&quot;state\&quot;: {         \&quot;new\&quot;: &#39;resolved\&quot;       }     }     \&quot;message\&quot;: {       \&quot;raw\&quot;: \&quot;This is now resolved.\&quot;     }   }&#39; &#x60;&#x60;&#x60;  The above example also includes a custom comment to go alongside the change. This comment will also be visible on the issue page in the UI.  The fields of the &#x60;changes&#x60; object are strings, not objects. This allows for immutable change log records, even after user accounts, milestones, or other objects recorded in a change entry, get renamed or deleted.  The &#x60;assignee_account_id&#x60; field stores the account id. When POSTing a new change and changing the assignee, the client should therefore use the user&#39;s account_id in the &#x60;changes.assignee_account_id.new&#x60; field.  This call requires authentication. Private repositories or private issue trackers require the caller to authenticate with an account that has appropriate authorization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    String issueId = "issueId_example"; // String | The issue id
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    IssueChange issueChange = new IssueChange(); // IssueChange | The new issue state change. The only required elements are `changes.[].new`. All other elements can be omitted from the body.
    try {
      IssueChange result = apiInstance.repositoriesWorkspaceRepoSlugIssuesIssueIdChangesPost(issueId, repoSlug, workspace, issueChange);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugIssuesIssueIdChangesPost");
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
| **issueId** | **String**| The issue id | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |
| **issueChange** | [**IssueChange**](IssueChange.md)| The new issue state change. The only required elements are &#x60;changes.[].new&#x60;. All other elements can be omitted from the body. | |

### Return type

[**IssueChange**](IssueChange.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The newly created issue change. |  * Location - The location of the project. This header is only provided when the project key is updated. <br>  |
| **401** | When the request wasn&#39;t authenticated. |  -  |
| **403** | When the authenticated user isn&#39;t authorized to modify the issue. |  -  |
| **404** | The specified repository or issue does not exist or does not have the issue tracker enabled. |  -  |

<a id="repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsCommentIdDelete"></a>
# **repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsCommentIdDelete**
> repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsCommentIdDelete(commentId, issueId, repoSlug, workspace)

Delete a comment on an issue

Deletes the specified comment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    Integer commentId = 56; // Integer | The id of the comment.
    String issueId = "issueId_example"; // String | The issue id
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      apiInstance.repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsCommentIdDelete(commentId, issueId, repoSlug, workspace);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsCommentIdDelete");
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
| **commentId** | **Integer**| The id of the comment. | |
| **issueId** | **String**| The issue id | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Indicates successful deletion. |  -  |

<a id="repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsCommentIdGet"></a>
# **repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsCommentIdGet**
> IssueComment repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsCommentIdGet(commentId, issueId, repoSlug, workspace)

Get a comment on an issue

Returns the specified issue comment object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    Integer commentId = 56; // Integer | The id of the comment.
    String issueId = "issueId_example"; // String | The issue id
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      IssueComment result = apiInstance.repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsCommentIdGet(commentId, issueId, repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsCommentIdGet");
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
| **commentId** | **Integer**| The id of the comment. | |
| **issueId** | **String**| The issue id | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**IssueComment**](IssueComment.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The issue comment. |  -  |

<a id="repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsCommentIdPut"></a>
# **repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsCommentIdPut**
> IssueComment repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsCommentIdPut(commentId, issueId, repoSlug, workspace, issueComment)

Update a comment on an issue

Updates the content of the specified issue comment. Note that only the &#x60;content.raw&#x60; field can be modified.  &#x60;&#x60;&#x60; $ curl https://api.bitbucket.org/2.0/repositories/atlassian/prlinks/issues/42/comments/5728901 \\   -X PUT -u evzijst \\   -H &#39;Content-Type: application/json&#39; \\   -d &#39;{\&quot;content\&quot;: {\&quot;raw\&quot;: \&quot;Lorem ipsum.\&quot;}&#39; &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    Integer commentId = 56; // Integer | The id of the comment.
    String issueId = "issueId_example"; // String | The issue id
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    IssueComment issueComment = new IssueComment(); // IssueComment | The updated comment.
    try {
      IssueComment result = apiInstance.repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsCommentIdPut(commentId, issueId, repoSlug, workspace, issueComment);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsCommentIdPut");
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
| **commentId** | **Integer**| The id of the comment. | |
| **issueId** | **String**| The issue id | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |
| **issueComment** | [**IssueComment**](IssueComment.md)| The updated comment. | |

### Return type

[**IssueComment**](IssueComment.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated issue comment. |  -  |
| **400** | If the input was invalid, or if the update to the comment is detected as spam  |  -  |

<a id="repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsGet"></a>
# **repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsGet**
> PaginatedIssueComments repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsGet(issueId, repoSlug, workspace, q)

List comments on an issue

Returns a paginated list of all comments that were made on the specified issue.  The default sorting is oldest to newest and can be overridden with the &#x60;sort&#x60; query parameter.  This endpoint also supports filtering and sorting of the results. See [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering) for more details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    String issueId = "issueId_example"; // String | The issue id
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    String q = "q_example"; // String |  Query string to narrow down the response as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering).
    try {
      PaginatedIssueComments result = apiInstance.repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsGet(issueId, repoSlug, workspace, q);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsGet");
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
| **issueId** | **String**| The issue id | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |
| **q** | **String**|  Query string to narrow down the response as per [filtering and sorting](/cloud/bitbucket/rest/intro/#filtering). | [optional] |

### Return type

[**PaginatedIssueComments**](PaginatedIssueComments.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A paginated list of issue comments. |  -  |

<a id="repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsPost"></a>
# **repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsPost**
> repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsPost(issueId, repoSlug, workspace, issueComment)

Create a comment on an issue

Creates a new issue comment.  &#x60;&#x60;&#x60; $ curl https://api.bitbucket.org/2.0/repositories/atlassian/prlinks/issues/42/comments/ \\   -X POST -u evzijst \\   -H &#39;Content-Type: application/json&#39; \\   -d &#39;{\&quot;content\&quot;: {\&quot;raw\&quot;: \&quot;Lorem ipsum.\&quot;}}&#39; &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    String issueId = "issueId_example"; // String | The issue id
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    IssueComment issueComment = new IssueComment(); // IssueComment | The new issue comment object.
    try {
      apiInstance.repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsPost(issueId, repoSlug, workspace, issueComment);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugIssuesIssueIdCommentsPost");
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
| **issueId** | **String**| The issue id | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |
| **issueComment** | [**IssueComment**](IssueComment.md)| The new issue comment object. | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The newly created comment. |  * Location - The location of the project. This header is only provided when the project key is updated. <br>  |
| **400** | If the input was invalid, or if the comment being created is detected as spam  |  -  |

<a id="repositoriesWorkspaceRepoSlugIssuesIssueIdDelete"></a>
# **repositoriesWorkspaceRepoSlugIssuesIssueIdDelete**
> Issue repositoriesWorkspaceRepoSlugIssuesIssueIdDelete(issueId, repoSlug, workspace)

Delete an issue

Deletes the specified issue. This requires write access to the repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    String issueId = "issueId_example"; // String | The issue id
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      Issue result = apiInstance.repositoriesWorkspaceRepoSlugIssuesIssueIdDelete(issueId, repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugIssuesIssueIdDelete");
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
| **issueId** | **String**| The issue id | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**Issue**](Issue.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The issue object. |  -  |
| **403** | When the authenticated user isn&#39;t authorized to delete the issue. |  -  |
| **404** | The specified repository or issue does not exist or does not have the issue tracker enabled. |  -  |

<a id="repositoriesWorkspaceRepoSlugIssuesIssueIdGet"></a>
# **repositoriesWorkspaceRepoSlugIssuesIssueIdGet**
> Issue repositoriesWorkspaceRepoSlugIssuesIssueIdGet(issueId, repoSlug, workspace)

Get an issue

Returns the specified issue.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    String issueId = "issueId_example"; // String | The issue id
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      Issue result = apiInstance.repositoriesWorkspaceRepoSlugIssuesIssueIdGet(issueId, repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugIssuesIssueIdGet");
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
| **issueId** | **String**| The issue id | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**Issue**](Issue.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The issue object. |  -  |
| **403** | When the authenticated user isn&#39;t authorized to access the issue. |  -  |
| **404** | The specified repository or issue does not exist or does not have the issue tracker enabled. |  -  |
| **410** | The specified issue is unavailable. |  -  |

<a id="repositoriesWorkspaceRepoSlugIssuesIssueIdPut"></a>
# **repositoriesWorkspaceRepoSlugIssuesIssueIdPut**
> Issue repositoriesWorkspaceRepoSlugIssuesIssueIdPut(issueId, repoSlug, workspace)

Update an issue

Modifies the issue.  &#x60;&#x60;&#x60; $ curl https://api.bitbucket.org/2.0/repostories/evzijst/dogslow/issues/123 \\   -u evzijst -s -X PUT -H &#39;Content-Type: application/json&#39; \\   -d &#39;{   \&quot;title\&quot;: \&quot;Updated title\&quot;,   \&quot;assignee\&quot;: {     \&quot;account_id\&quot;: \&quot;5d5355e8c6b9320d9ea5b28d\&quot;   },   \&quot;priority\&quot;: \&quot;minor\&quot;,   \&quot;version\&quot;: {     \&quot;name\&quot;: \&quot;1.0\&quot;   },   \&quot;component\&quot;: null }&#39; &#x60;&#x60;&#x60;  This example changes the &#x60;title&#x60;, &#x60;assignee&#x60;, &#x60;priority&#x60; and the &#x60;version&#x60;. It also removes the value of the &#x60;component&#x60; from the issue by setting the field to &#x60;null&#x60;. Any field not present keeps its existing value.  Each time an issue is edited in the UI or through the API, an immutable change record is created under the &#x60;/issues/123/changes&#x60; endpoint. It also has a comment associated with the change.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    String issueId = "issueId_example"; // String | The issue id
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      Issue result = apiInstance.repositoriesWorkspaceRepoSlugIssuesIssueIdPut(issueId, repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugIssuesIssueIdPut");
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
| **issueId** | **String**| The issue id | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**Issue**](Issue.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The updated issue object. |  -  |
| **403** | When the authenticated user isn&#39;t authorized to access the issue. |  -  |
| **404** | The specified repository or issue does not exist or does not have the issue tracker enabled. |  -  |

<a id="repositoriesWorkspaceRepoSlugIssuesIssueIdVoteDelete"></a>
# **repositoriesWorkspaceRepoSlugIssuesIssueIdVoteDelete**
> Error repositoriesWorkspaceRepoSlugIssuesIssueIdVoteDelete(issueId, repoSlug, workspace)

Remove vote for an issue

Retract your vote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    String issueId = "issueId_example"; // String | The issue id
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      Error result = apiInstance.repositoriesWorkspaceRepoSlugIssuesIssueIdVoteDelete(issueId, repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugIssuesIssueIdVoteDelete");
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
| **issueId** | **String**| The issue id | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**Error**](Error.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error. |  -  |

<a id="repositoriesWorkspaceRepoSlugIssuesIssueIdVoteGet"></a>
# **repositoriesWorkspaceRepoSlugIssuesIssueIdVoteGet**
> Error repositoriesWorkspaceRepoSlugIssuesIssueIdVoteGet(issueId, repoSlug, workspace)

Check if current user voted for an issue

Check whether the authenticated user has voted for this issue. A 204 status code indicates that the user has voted, while a 404 implies they haven&#39;t.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    String issueId = "issueId_example"; // String | The issue id
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      Error result = apiInstance.repositoriesWorkspaceRepoSlugIssuesIssueIdVoteGet(issueId, repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugIssuesIssueIdVoteGet");
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
| **issueId** | **String**| The issue id | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**Error**](Error.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | If the authenticated user has not voted for this issue. |  -  |
| **401** | When the request wasn&#39;t authenticated. |  -  |
| **404** | If the authenticated user has not voted for this issue, or when the repo does not exist, or does not have an issue tracker. |  -  |

<a id="repositoriesWorkspaceRepoSlugIssuesIssueIdVotePut"></a>
# **repositoriesWorkspaceRepoSlugIssuesIssueIdVotePut**
> Error repositoriesWorkspaceRepoSlugIssuesIssueIdVotePut(issueId, repoSlug, workspace)

Vote for an issue

Vote for this issue.  To cast your vote, do an empty PUT. The 204 status code indicates that the operation was successful.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    String issueId = "issueId_example"; // String | The issue id
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      Error result = apiInstance.repositoriesWorkspaceRepoSlugIssuesIssueIdVotePut(issueId, repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugIssuesIssueIdVotePut");
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
| **issueId** | **String**| The issue id | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**Error**](Error.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Indicating the authenticated user has cast their vote successfully. |  -  |
| **401** | When the request wasn&#39;t authenticated. |  -  |
| **404** | The specified repository or issue does not exist or does not have the issue tracker enabled. |  -  |

<a id="repositoriesWorkspaceRepoSlugIssuesIssueIdWatchDelete"></a>
# **repositoriesWorkspaceRepoSlugIssuesIssueIdWatchDelete**
> Error repositoriesWorkspaceRepoSlugIssuesIssueIdWatchDelete(issueId, repoSlug, workspace)

Stop watching an issue

Stop watching this issue.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    String issueId = "issueId_example"; // String | The issue id
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      Error result = apiInstance.repositoriesWorkspaceRepoSlugIssuesIssueIdWatchDelete(issueId, repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugIssuesIssueIdWatchDelete");
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
| **issueId** | **String**| The issue id | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**Error**](Error.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Indicates that the authenticated user successfully stopped watching this issue. |  -  |
| **401** | When the request wasn&#39;t authenticated. |  -  |
| **404** | The specified repository or issue does not exist or does not have the issue tracker enabled. |  -  |

<a id="repositoriesWorkspaceRepoSlugIssuesIssueIdWatchGet"></a>
# **repositoriesWorkspaceRepoSlugIssuesIssueIdWatchGet**
> Error repositoriesWorkspaceRepoSlugIssuesIssueIdWatchGet(issueId, repoSlug, workspace)

Check if current user is watching a issue

Indicated whether or not the authenticated user is watching this issue.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    String issueId = "issueId_example"; // String | The issue id
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      Error result = apiInstance.repositoriesWorkspaceRepoSlugIssuesIssueIdWatchGet(issueId, repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugIssuesIssueIdWatchGet");
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
| **issueId** | **String**| The issue id | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**Error**](Error.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | If the authenticated user is watching this issue. |  -  |
| **401** | When the request wasn&#39;t authenticated. |  -  |
| **404** | If the authenticated user is not watching this issue, or when the repo does not exist, or does not have an issue tracker. |  -  |

<a id="repositoriesWorkspaceRepoSlugIssuesIssueIdWatchPut"></a>
# **repositoriesWorkspaceRepoSlugIssuesIssueIdWatchPut**
> Error repositoriesWorkspaceRepoSlugIssuesIssueIdWatchPut(issueId, repoSlug, workspace)

Watch an issue

Start watching this issue.  To start watching this issue, do an empty PUT. The 204 status code indicates that the operation was successful.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    String issueId = "issueId_example"; // String | The issue id
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      Error result = apiInstance.repositoriesWorkspaceRepoSlugIssuesIssueIdWatchPut(issueId, repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugIssuesIssueIdWatchPut");
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
| **issueId** | **String**| The issue id | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**Error**](Error.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Indicates that the authenticated user successfully started watching this issue. |  -  |
| **401** | When the request wasn&#39;t authenticated. |  -  |
| **404** | If the authenticated user is not watching this issue, or when the repo does not exist, or does not have an issue tracker. |  -  |

<a id="repositoriesWorkspaceRepoSlugIssuesPost"></a>
# **repositoriesWorkspaceRepoSlugIssuesPost**
> Issue repositoriesWorkspaceRepoSlugIssuesPost(repoSlug, workspace, issue)

Create an issue

Creates a new issue.  This call requires authentication. Private repositories or private issue trackers require the caller to authenticate with an account that has appropriate authorization.  The authenticated user is used for the issue&#39;s &#x60;reporter&#x60; field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    Issue issue = new Issue(); // Issue | The new issue. The only required element is `title`. All other elements can be omitted from the body.
    try {
      Issue result = apiInstance.repositoriesWorkspaceRepoSlugIssuesPost(repoSlug, workspace, issue);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugIssuesPost");
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
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |
| **issue** | [**Issue**](Issue.md)| The new issue. The only required element is &#x60;title&#x60;. All other elements can be omitted from the body. | |

### Return type

[**Issue**](Issue.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The newly created issue. |  * Location - The location of the project. This header is only provided when the project key is updated. <br>  |
| **401** | When the request wasn&#39;t authenticated. |  -  |
| **403** | When the authenticated user isn&#39;t authorized to create the issue. |  -  |
| **404** | The specified repository does not exist or does not have the issue tracker enabled. |  -  |

<a id="repositoriesWorkspaceRepoSlugMilestonesGet"></a>
# **repositoriesWorkspaceRepoSlugMilestonesGet**
> PaginatedMilestones repositoriesWorkspaceRepoSlugMilestonesGet(repoSlug, workspace)

List milestones

Returns the milestones that have been defined in the issue tracker.  This resource is only available on repositories that have the issue tracker enabled.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      PaginatedMilestones result = apiInstance.repositoriesWorkspaceRepoSlugMilestonesGet(repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugMilestonesGet");
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
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**PaginatedMilestones**](PaginatedMilestones.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The milestones that have been defined in the issue tracker. |  -  |
| **404** | The specified repository does not exist or does not have the issue tracker enabled. |  -  |

<a id="repositoriesWorkspaceRepoSlugMilestonesMilestoneIdGet"></a>
# **repositoriesWorkspaceRepoSlugMilestonesMilestoneIdGet**
> Milestone repositoriesWorkspaceRepoSlugMilestonesMilestoneIdGet(milestoneId, repoSlug, workspace)

Get a milestone

Returns the specified issue tracker milestone object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    Integer milestoneId = 56; // Integer | The milestone's id
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      Milestone result = apiInstance.repositoriesWorkspaceRepoSlugMilestonesMilestoneIdGet(milestoneId, repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugMilestonesMilestoneIdGet");
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
| **milestoneId** | **Integer**| The milestone&#39;s id | |
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**Milestone**](Milestone.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The specified milestone object. |  -  |
| **404** | The specified repository or milestone does not exist or does not have the issue tracker enabled. |  -  |

<a id="repositoriesWorkspaceRepoSlugVersionsGet"></a>
# **repositoriesWorkspaceRepoSlugVersionsGet**
> PaginatedVersions repositoriesWorkspaceRepoSlugVersionsGet(repoSlug, workspace)

List defined versions for issues

Returns the versions that have been defined in the issue tracker.  This resource is only available on repositories that have the issue tracker enabled.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      PaginatedVersions result = apiInstance.repositoriesWorkspaceRepoSlugVersionsGet(repoSlug, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugVersionsGet");
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
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**PaginatedVersions**](PaginatedVersions.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The versions that have been defined in the issue tracker. |  -  |
| **404** | The specified repository does not exist or does not have the issue tracker enabled. |  -  |

<a id="repositoriesWorkspaceRepoSlugVersionsVersionIdGet"></a>
# **repositoriesWorkspaceRepoSlugVersionsVersionIdGet**
> Version repositoriesWorkspaceRepoSlugVersionsVersionIdGet(repoSlug, versionId, workspace)

Get a defined version for issues

Returns the specified issue tracker version object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IssueTrackerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.bitbucket.org/2.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    IssueTrackerApi apiInstance = new IssueTrackerApi(defaultClient);
    String repoSlug = "repoSlug_example"; // String | This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: `{repository UUID}`. 
    Integer versionId = 56; // Integer | The version's id
    String workspace = "workspace_example"; // String | This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: `{workspace UUID}`. 
    try {
      Version result = apiInstance.repositoriesWorkspaceRepoSlugVersionsVersionIdGet(repoSlug, versionId, workspace);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IssueTrackerApi#repositoriesWorkspaceRepoSlugVersionsVersionIdGet");
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
| **repoSlug** | **String**| This can either be the repository slug or the UUID of the repository, surrounded by curly-braces, for example: &#x60;{repository UUID}&#x60;.  | |
| **versionId** | **Integer**| The version&#39;s id | |
| **workspace** | **String**| This can either be the workspace ID (slug) or the workspace UUID surrounded by curly-braces, for example: &#x60;{workspace UUID}&#x60;.  | |

### Return type

[**Version**](Version.md)

### Authorization

[api_key](../README.md#api_key), [oauth2](../README.md#oauth2), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The specified version object. |  -  |
| **404** | The specified repository or version does not exist or does not have the issue tracker enabled. |  -  |

