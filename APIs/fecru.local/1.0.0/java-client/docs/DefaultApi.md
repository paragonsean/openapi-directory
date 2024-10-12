# DefaultApi

All URIs are relative to *http://fecru.local/context*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addAllowedReviewerGroup**](DefaultApi.md#addAllowedReviewerGroup) | **PUT** /rest-service-fecru/admin/projects/{key}/allowed-reviewer-groups |  |
| [**addAllowedReviewerUser**](DefaultApi.md#addAllowedReviewerUser) | **PUT** /rest-service-fecru/admin/projects/{key}/allowed-reviewer-users |  |
| [**addDefaultReviewerGroup**](DefaultApi.md#addDefaultReviewerGroup) | **PUT** /rest-service-fecru/admin/projects/{key}/default-reviewer-groups |  |
| [**addDefaultReviewerUser**](DefaultApi.md#addDefaultReviewerUser) | **PUT** /rest-service-fecru/admin/projects/{key}/default-reviewer-users |  |
| [**addGroupToPermissions**](DefaultApi.md#addGroupToPermissions) | **PUT** /rest-service-fecru/admin/repositories/{repository}/permissions/groups |  |
| [**addPermissionSchemeAnonymousUsers**](DefaultApi.md#addPermissionSchemeAnonymousUsers) | **PUT** /rest-service-fecru/admin/permission-schemes/{name}/anonymous-users |  |
| [**addPermissionSchemeGroup**](DefaultApi.md#addPermissionSchemeGroup) | **PUT** /rest-service-fecru/admin/permission-schemes/{name}/groups |  |
| [**addPermissionSchemeLoggedUsers**](DefaultApi.md#addPermissionSchemeLoggedUsers) | **PUT** /rest-service-fecru/admin/permission-schemes/{name}/logged-in-users |  |
| [**addPermissionSchemeReviewRole**](DefaultApi.md#addPermissionSchemeReviewRole) | **PUT** /rest-service-fecru/admin/permission-schemes/{name}/review-roles |  |
| [**addPermissionSchemeUser**](DefaultApi.md#addPermissionSchemeUser) | **PUT** /rest-service-fecru/admin/permission-schemes/{name}/users |  |
| [**addRepository**](DefaultApi.md#addRepository) | **POST** /rest-service-fecru/admin/repositories-v1 |  |
| [**allowedReviewerGroups**](DefaultApi.md#allowedReviewerGroups) | **GET** /rest-service-fecru/admin/projects/{key}/allowed-reviewer-groups |  |
| [**allowedReviewerUsers**](DefaultApi.md#allowedReviewerUsers) | **GET** /rest-service-fecru/admin/projects/{key}/allowed-reviewer-users |  |
| [**defaultPermissions**](DefaultApi.md#defaultPermissions) | **GET** /rest-service-fecru/admin/repositories/~defaults/permissions |  |
| [**defaultReviewerGroups**](DefaultApi.md#defaultReviewerGroups) | **GET** /rest-service-fecru/admin/projects/{key}/default-reviewer-groups |  |
| [**deleteAllowedReviewerGroup**](DefaultApi.md#deleteAllowedReviewerGroup) | **DELETE** /rest-service-fecru/admin/projects/{key}/allowed-reviewer-groups |  |
| [**deleteAllowedReviewerUser**](DefaultApi.md#deleteAllowedReviewerUser) | **DELETE** /rest-service-fecru/admin/projects/{key}/allowed-reviewer-users |  |
| [**deleteDefaultReviewerGroup**](DefaultApi.md#deleteDefaultReviewerGroup) | **DELETE** /rest-service-fecru/admin/projects/{key}/default-reviewer-groups |  |
| [**deleteDefaultReviewerUser**](DefaultApi.md#deleteDefaultReviewerUser) | **DELETE** /rest-service-fecru/admin/projects/{key}/default-reviewer-users |  |
| [**deletePermissionSchemeAnonymousUsers**](DefaultApi.md#deletePermissionSchemeAnonymousUsers) | **DELETE** /rest-service-fecru/admin/permission-schemes/{name}/anonymous-users |  |
| [**deletePermissionSchemeGroup**](DefaultApi.md#deletePermissionSchemeGroup) | **DELETE** /rest-service-fecru/admin/permission-schemes/{name}/groups |  |
| [**deletePermissionSchemeLoggedUsers**](DefaultApi.md#deletePermissionSchemeLoggedUsers) | **DELETE** /rest-service-fecru/admin/permission-schemes/{name}/logged-in-users |  |
| [**deletePermissionSchemeRole**](DefaultApi.md#deletePermissionSchemeRole) | **DELETE** /rest-service-fecru/admin/permission-schemes/{name}/review-roles |  |
| [**deletePermissionSchemeUser**](DefaultApi.md#deletePermissionSchemeUser) | **DELETE** /rest-service-fecru/admin/permission-schemes/{name}/users |  |
| [**deleteRepository**](DefaultApi.md#deleteRepository) | **DELETE** /rest-service-fecru/admin/repositories-v1/{repository}/ |  |
| [**disableRepository**](DefaultApi.md#disableRepository) | **POST** /rest-service-fecru/admin/repositories-v1/{repository}/disable |  |
| [**doReviewRevisionReindex**](DefaultApi.md#doReviewRevisionReindex) | **POST** /rest-service-fecru/admin/repositories-v1/{repository}/reindex-reviews |  |
| [**doShareContent**](DefaultApi.md#doShareContent) | **POST** /rest-service-fecru/share-content-v1/share |  |
| [**enableRepository**](DefaultApi.md#enableRepository) | **POST** /rest-service-fecru/admin/repositories-v1/{repository}/enable |  |
| [**fullIncrementalIndex**](DefaultApi.md#fullIncrementalIndex) | **PUT** /rest-service-fecru/admin/repositories/{repository}/full-incremental-index |  |
| [**getGlobalPref**](DefaultApi.md#getGlobalPref) | **GET** /rest-service-fecru/user-prefs-v1/{property} |  |
| [**getInfo**](DefaultApi.md#getInfo) | **GET** /rest-service-fecru/server-v1 |  |
| [**getRecent**](DefaultApi.md#getRecent) | **GET** /rest-service-fecru/recently-visited-v1 |  |
| [**getRecentDetailed**](DefaultApi.md#getRecentDetailed) | **GET** /rest-service-fecru/recently-visited-v1/detailed |  |
| [**getRecentProjects**](DefaultApi.md#getRecentProjects) | **GET** /rest-service-fecru/recently-visited-v1/projects |  |
| [**getRecentProjectsDetailed**](DefaultApi.md#getRecentProjectsDetailed) | **GET** /rest-service-fecru/recently-visited-v1/projects/detailed |  |
| [**getRecentRepositories**](DefaultApi.md#getRecentRepositories) | **GET** /rest-service-fecru/recently-visited-v1/repositories |  |
| [**getRecentRepositoriesDetailed**](DefaultApi.md#getRecentRepositoriesDetailed) | **GET** /rest-service-fecru/recently-visited-v1/repositories/detailed |  |
| [**getRecentReviews**](DefaultApi.md#getRecentReviews) | **GET** /rest-service-fecru/recently-visited-v1/reviews |  |
| [**getRecentReviewsDetailed**](DefaultApi.md#getRecentReviewsDetailed) | **GET** /rest-service-fecru/recently-visited-v1/reviews/detailed |  |
| [**getRecentSnippets**](DefaultApi.md#getRecentSnippets) | **GET** /rest-service-fecru/recently-visited-v1/snippets |  |
| [**getRecentSnippetsDetailed**](DefaultApi.md#getRecentSnippetsDetailed) | **GET** /rest-service-fecru/recently-visited-v1/snippets/detailed |  |
| [**getRecentUsers**](DefaultApi.md#getRecentUsers) | **GET** /rest-service-fecru/recently-visited-v1/users |  |
| [**getRecentUsersDetailed**](DefaultApi.md#getRecentUsersDetailed) | **GET** /rest-service-fecru/recently-visited-v1/users/detailed |  |
| [**getRepoPref**](DefaultApi.md#getRepoPref) | **GET** /rest-service-fecru/user-prefs-v1/{repository}/{property} |  |
| [**incrementalIndex**](DefaultApi.md#incrementalIndex) | **PUT** /rest-service-fecru/admin/repositories/{repository}/incremental-index |  |
| [**listAnonymousUsersPrincipalAssociation**](DefaultApi.md#listAnonymousUsersPrincipalAssociation) | **GET** /rest-service-fecru/admin/permission-schemes/{name}/anonymous-users |  |
| [**listDefaultReviewerUsers**](DefaultApi.md#listDefaultReviewerUsers) | **GET** /rest-service-fecru/admin/projects/{key}/default-reviewer-users |  |
| [**listGroupPrincipalAssociation**](DefaultApi.md#listGroupPrincipalAssociation) | **GET** /rest-service-fecru/admin/permission-schemes/{name}/groups |  |
| [**listGroupUsers**](DefaultApi.md#listGroupUsers) | **GET** /rest-service-fecru/admin/groups/{name}/users |  |
| [**listLoggedUsersPrincipalAssociation**](DefaultApi.md#listLoggedUsersPrincipalAssociation) | **GET** /rest-service-fecru/admin/permission-schemes/{name}/logged-in-users |  |
| [**listProjects**](DefaultApi.md#listProjects) | **GET** /rest-service-fecru/admin/permission-schemes/{name}/projects |  |
| [**listRolesPrincipalAssociation**](DefaultApi.md#listRolesPrincipalAssociation) | **GET** /rest-service-fecru/admin/permission-schemes/{name}/review-roles |  |
| [**listUserGroups**](DefaultApi.md#listUserGroups) | **GET** /rest-service-fecru/admin/users/{name}/groups |  |
| [**listUserPrincipalAssociation**](DefaultApi.md#listUserPrincipalAssociation) | **GET** /rest-service-fecru/admin/permission-schemes/{name}/users |  |
| [**login**](DefaultApi.md#login) | **POST** /rest-service-fecru/auth/login |  |
| [**moveAllReviews**](DefaultApi.md#moveAllReviews) | **PUT** /rest-service-fecru/admin/projects/{sourceProjectKey}/move-reviews/{destinationProjectKey} |  |
| [**permissions**](DefaultApi.md#permissions) | **GET** /rest-service-fecru/admin/repositories/{repository}/permissions |  |
| [**permissionsGroups**](DefaultApi.md#permissionsGroups) | **GET** /rest-service-fecru/admin/repositories/{repository}/permissions/groups |  |
| [**rebuildSearchIndex**](DefaultApi.md#rebuildSearchIndex) | **POST** /rest-service-fecru/admin/repositories-v1/{repository}/reindex-search |  |
| [**reindexChangesetComments**](DefaultApi.md#reindexChangesetComments) | **POST** /rest-service-fecru/admin/repositories-v1/{repository}/reindex-discussions |  |
| [**reindexChangesetDiscussion**](DefaultApi.md#reindexChangesetDiscussion) | **PUT** /rest-service-fecru/admin/repositories/{repository}/reindex-changeset-discussion |  |
| [**reindexReviews**](DefaultApi.md#reindexReviews) | **PUT** /rest-service-fecru/admin/repositories/{repository}/reindex-reviews |  |
| [**reindexSearch**](DefaultApi.md#reindexSearch) | **PUT** /rest-service-fecru/admin/repositories/{repository}/reindex-search |  |
| [**removeGroupToPermissions**](DefaultApi.md#removeGroupToPermissions) | **DELETE** /rest-service-fecru/admin/repositories/{repository}/permissions/groups |  |
| [**repositoryUpdates**](DefaultApi.md#repositoryUpdates) | **GET** /rest-service-fecru/admin/repositories/{repository}/updates |  |
| [**restServiceFecruAdminGroupsGet**](DefaultApi.md#restServiceFecruAdminGroupsGet) | **GET** /rest-service-fecru/admin/groups/ |  |
| [**restServiceFecruAdminGroupsNameDelete**](DefaultApi.md#restServiceFecruAdminGroupsNameDelete) | **DELETE** /rest-service-fecru/admin/groups/{name} |  |
| [**restServiceFecruAdminGroupsNameGet**](DefaultApi.md#restServiceFecruAdminGroupsNameGet) | **GET** /rest-service-fecru/admin/groups/{name} |  |
| [**restServiceFecruAdminGroupsNamePut**](DefaultApi.md#restServiceFecruAdminGroupsNamePut) | **PUT** /rest-service-fecru/admin/groups/{name} |  |
| [**restServiceFecruAdminGroupsNameUsersDelete**](DefaultApi.md#restServiceFecruAdminGroupsNameUsersDelete) | **DELETE** /rest-service-fecru/admin/groups/{name}/users |  |
| [**restServiceFecruAdminGroupsNameUsersPut**](DefaultApi.md#restServiceFecruAdminGroupsNameUsersPut) | **PUT** /rest-service-fecru/admin/groups/{name}/users |  |
| [**restServiceFecruAdminGroupsPost**](DefaultApi.md#restServiceFecruAdminGroupsPost) | **POST** /rest-service-fecru/admin/groups/ |  |
| [**restServiceFecruAdminPermissionSchemesGet**](DefaultApi.md#restServiceFecruAdminPermissionSchemesGet) | **GET** /rest-service-fecru/admin/permission-schemes |  |
| [**restServiceFecruAdminPermissionSchemesNameDelete**](DefaultApi.md#restServiceFecruAdminPermissionSchemesNameDelete) | **DELETE** /rest-service-fecru/admin/permission-schemes/{name} |  |
| [**restServiceFecruAdminPermissionSchemesNameGet**](DefaultApi.md#restServiceFecruAdminPermissionSchemesNameGet) | **GET** /rest-service-fecru/admin/permission-schemes/{name} |  |
| [**restServiceFecruAdminPermissionSchemesNamePut**](DefaultApi.md#restServiceFecruAdminPermissionSchemesNamePut) | **PUT** /rest-service-fecru/admin/permission-schemes/{name} |  |
| [**restServiceFecruAdminPermissionSchemesPost**](DefaultApi.md#restServiceFecruAdminPermissionSchemesPost) | **POST** /rest-service-fecru/admin/permission-schemes |  |
| [**restServiceFecruAdminProjectsGet**](DefaultApi.md#restServiceFecruAdminProjectsGet) | **GET** /rest-service-fecru/admin/projects |  |
| [**restServiceFecruAdminProjectsKeyDelete**](DefaultApi.md#restServiceFecruAdminProjectsKeyDelete) | **DELETE** /rest-service-fecru/admin/projects/{key} |  |
| [**restServiceFecruAdminProjectsKeyGet**](DefaultApi.md#restServiceFecruAdminProjectsKeyGet) | **GET** /rest-service-fecru/admin/projects/{key} |  |
| [**restServiceFecruAdminProjectsKeyPut**](DefaultApi.md#restServiceFecruAdminProjectsKeyPut) | **PUT** /rest-service-fecru/admin/projects/{key} |  |
| [**restServiceFecruAdminProjectsPost**](DefaultApi.md#restServiceFecruAdminProjectsPost) | **POST** /rest-service-fecru/admin/projects |  |
| [**restServiceFecruAdminRepositoriesGet**](DefaultApi.md#restServiceFecruAdminRepositoriesGet) | **GET** /rest-service-fecru/admin/repositories |  |
| [**restServiceFecruAdminRepositoriesPost**](DefaultApi.md#restServiceFecruAdminRepositoriesPost) | **POST** /rest-service-fecru/admin/repositories |  |
| [**restServiceFecruAdminRepositoriesRepositoryDelete**](DefaultApi.md#restServiceFecruAdminRepositoriesRepositoryDelete) | **DELETE** /rest-service-fecru/admin/repositories/{repository} |  |
| [**restServiceFecruAdminRepositoriesRepositoryGet**](DefaultApi.md#restServiceFecruAdminRepositoriesRepositoryGet) | **GET** /rest-service-fecru/admin/repositories/{repository} |  |
| [**restServiceFecruAdminRepositoriesRepositoryPut**](DefaultApi.md#restServiceFecruAdminRepositoriesRepositoryPut) | **PUT** /rest-service-fecru/admin/repositories/{repository} |  |
| [**restServiceFecruAdminRepositoriesRepositoryReindexLinecountPut**](DefaultApi.md#restServiceFecruAdminRepositoriesRepositoryReindexLinecountPut) | **PUT** /rest-service-fecru/admin/repositories/{repository}/reindex-linecount |  |
| [**restServiceFecruAdminRepositoriesRepositoryReindexSourcePut**](DefaultApi.md#restServiceFecruAdminRepositoriesRepositoryReindexSourcePut) | **PUT** /rest-service-fecru/admin/repositories/{repository}/reindex-source |  |
| [**restServiceFecruAdminRepositoriesRepositoryRescanMetadataPut**](DefaultApi.md#restServiceFecruAdminRepositoriesRepositoryRescanMetadataPut) | **PUT** /rest-service-fecru/admin/repositories/{repository}/rescan-metadata |  |
| [**restServiceFecruAdminRepositoriesV1RepositoryGet**](DefaultApi.md#restServiceFecruAdminRepositoriesV1RepositoryGet) | **GET** /rest-service-fecru/admin/repositories-v1/{repository} |  |
| [**restServiceFecruAdminRepositoriesV1RepositoryReindexLinecountPost**](DefaultApi.md#restServiceFecruAdminRepositoriesV1RepositoryReindexLinecountPost) | **POST** /rest-service-fecru/admin/repositories-v1/{repository}/reindex-linecount |  |
| [**restServiceFecruAdminRepositoriesV1RepositoryReindexSourcePost**](DefaultApi.md#restServiceFecruAdminRepositoriesV1RepositoryReindexSourcePost) | **POST** /rest-service-fecru/admin/repositories-v1/{repository}/reindex-source |  |
| [**restServiceFecruAdminRepositoriesV1RepositoryRescanMetadataPost**](DefaultApi.md#restServiceFecruAdminRepositoriesV1RepositoryRescanMetadataPost) | **POST** /rest-service-fecru/admin/repositories-v1/{repository}/rescan-metadata |  |
| [**restServiceFecruAdminUsersGet**](DefaultApi.md#restServiceFecruAdminUsersGet) | **GET** /rest-service-fecru/admin/users/ |  |
| [**restServiceFecruAdminUsersNameDelete**](DefaultApi.md#restServiceFecruAdminUsersNameDelete) | **DELETE** /rest-service-fecru/admin/users/{name} |  |
| [**restServiceFecruAdminUsersNameGet**](DefaultApi.md#restServiceFecruAdminUsersNameGet) | **GET** /rest-service-fecru/admin/users/{name} |  |
| [**restServiceFecruAdminUsersNameGroupsDelete**](DefaultApi.md#restServiceFecruAdminUsersNameGroupsDelete) | **DELETE** /rest-service-fecru/admin/users/{name}/groups |  |
| [**restServiceFecruAdminUsersNameGroupsPut**](DefaultApi.md#restServiceFecruAdminUsersNameGroupsPut) | **PUT** /rest-service-fecru/admin/users/{name}/groups |  |
| [**restServiceFecruAdminUsersNamePut**](DefaultApi.md#restServiceFecruAdminUsersNamePut) | **PUT** /rest-service-fecru/admin/users/{name} |  |
| [**restServiceFecruAdminUsersPost**](DefaultApi.md#restServiceFecruAdminUsersPost) | **POST** /rest-service-fecru/admin/users/ |  |
| [**restServiceFecruIndexingStatusV1StatusRepositoryGet**](DefaultApi.md#restServiceFecruIndexingStatusV1StatusRepositoryGet) | **GET** /rest-service-fecru/indexing-status-v1/status/{repository} |  |
| [**scan**](DefaultApi.md#scan) | **POST** /rest-service-fecru/admin/repositories-v1/{repository}/scan |  |
| [**scanCvs**](DefaultApi.md#scanCvs) | **POST** /rest-service-fecru/admin/repositories-v1/{repository}/scan-cvs |  |
| [**setPref**](DefaultApi.md#setPref) | **POST** /rest-service-fecru/user-prefs-v1 |  |
| [**start**](DefaultApi.md#start) | **PUT** /rest-service-fecru/admin/repositories/{repository}/start |  |
| [**startRepository**](DefaultApi.md#startRepository) | **POST** /rest-service-fecru/admin/repositories-v1/{repository}/start |  |
| [**stop**](DefaultApi.md#stop) | **PUT** /rest-service-fecru/admin/repositories/{repository}/stop |  |
| [**stopRepository**](DefaultApi.md#stopRepository) | **POST** /rest-service-fecru/admin/repositories-v1/{repository}/stop |  |
| [**updateDefaultPermissions**](DefaultApi.md#updateDefaultPermissions) | **PUT** /rest-service-fecru/admin/repositories/~defaults/permissions |  |
| [**updatePermissions**](DefaultApi.md#updatePermissions) | **PUT** /rest-service-fecru/admin/repositories/{repository}/permissions |  |
| [**updateRepositoryUpdates**](DefaultApi.md#updateRepositoryUpdates) | **PUT** /rest-service-fecru/admin/repositories/{repository}/updates |  |


<a id="addAllowedReviewerGroup"></a>
# **addAllowedReviewerGroup**
> addAllowedReviewerGroup(key)



Add group to project&#39;s allowed reviewer group list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "key_example"; // String | project key
    try {
      apiInstance.addAllowedReviewerGroup(key);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addAllowedReviewerGroup");
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
| **key** | **String**| project key | |

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
| **200** | Successful Response |  -  |

<a id="addAllowedReviewerUser"></a>
# **addAllowedReviewerUser**
> addAllowedReviewerUser(key)



Add user to project&#39;s allowed reviewer users list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "key_example"; // String | project key
    try {
      apiInstance.addAllowedReviewerUser(key);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addAllowedReviewerUser");
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
| **key** | **String**| project key | |

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
| **200** | Successful Response |  -  |

<a id="addDefaultReviewerGroup"></a>
# **addDefaultReviewerGroup**
> addDefaultReviewerGroup(key)



Add group to project&#39;s default reviewer group list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "key_example"; // String | project key
    try {
      apiInstance.addDefaultReviewerGroup(key);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addDefaultReviewerGroup");
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
| **key** | **String**| project key | |

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
| **200** | Successful Response |  -  |

<a id="addDefaultReviewerUser"></a>
# **addDefaultReviewerUser**
> addDefaultReviewerUser(key)



Add user to project&#39;s default reviewer users list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "key_example"; // String | project key
    try {
      apiInstance.addDefaultReviewerUser(key);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addDefaultReviewerUser");
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
| **key** | **String**| project key | |

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
| **200** | Successful Response |  -  |

<a id="addGroupToPermissions"></a>
# **addGroupToPermissions**
> addGroupToPermissions(repository)



Note: use /rest-service-fecru/admin/repository-permissions/ endpoint for full repository permission administration functionality  Adds group to repository allowed groups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository
    try {
      apiInstance.addGroupToPermissions(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addGroupToPermissions");
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
| **repository** | **String**| the key of the repository | |

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
| **200** | Successful Response |  -  |

<a id="addPermissionSchemeAnonymousUsers"></a>
# **addPermissionSchemeAnonymousUsers**
> addPermissionSchemeAnonymousUsers(name)



Add anonymous-user permission [action name] to given permission scheme  List of available action names:

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | permission scheme name
    try {
      apiInstance.addPermissionSchemeAnonymousUsers(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addPermissionSchemeAnonymousUsers");
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
| **name** | **String**| permission scheme name | |

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
| **200** | Successful Response |  -  |

<a id="addPermissionSchemeGroup"></a>
# **addPermissionSchemeGroup**
> addPermissionSchemeGroup(name)



Add group permission [group name, action name] to given permission scheme  List of available action names:

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | permission scheme name
    try {
      apiInstance.addPermissionSchemeGroup(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addPermissionSchemeGroup");
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
| **name** | **String**| permission scheme name | |

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
| **200** | Successful Response |  -  |

<a id="addPermissionSchemeLoggedUsers"></a>
# **addPermissionSchemeLoggedUsers**
> addPermissionSchemeLoggedUsers(name)



Add logged-in-users permission [action name] to given permission scheme  List of available action names:

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | permission scheme name
    try {
      apiInstance.addPermissionSchemeLoggedUsers(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addPermissionSchemeLoggedUsers");
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
| **name** | **String**| permission scheme name | |

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
| **200** | Successful Response |  -  |

<a id="addPermissionSchemeReviewRole"></a>
# **addPermissionSchemeReviewRole**
> addPermissionSchemeReviewRole(name)



Add review-role permission [role name, action name] to given permission scheme  List of available action names:     List of available role names:

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | permission scheme name
    try {
      apiInstance.addPermissionSchemeReviewRole(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addPermissionSchemeReviewRole");
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
| **name** | **String**| permission scheme name | |

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
| **200** | Successful Response |  -  |

<a id="addPermissionSchemeUser"></a>
# **addPermissionSchemeUser**
> addPermissionSchemeUser(name)



Add user permission [username, action name] to given permission scheme  List of available action names:

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | permission scheme name
    try {
      apiInstance.addPermissionSchemeUser(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addPermissionSchemeUser");
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
| **name** | **String**| permission scheme name | |

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
| **200** | Successful Response |  -  |

<a id="addRepository"></a>
# **addRepository**
> addRepository()



Adds repository

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.addRepository();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#addRepository");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="allowedReviewerGroups"></a>
# **allowedReviewerGroups**
> allowedReviewerGroups(key)



Retrieves project&#39;s allowed reviewer groups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "key_example"; // String | project key
    try {
      apiInstance.allowedReviewerGroups(key);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#allowedReviewerGroups");
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
| **key** | **String**| project key | |

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
| **200** | Successful Response |  -  |

<a id="allowedReviewerUsers"></a>
# **allowedReviewerUsers**
> allowedReviewerUsers(key)



Retrieves project&#39;s allowed reviewer users

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "key_example"; // String | project key
    try {
      apiInstance.allowedReviewerUsers(key);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#allowedReviewerUsers");
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
| **key** | **String**| project key | |

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
| **200** | Successful Response |  -  |

<a id="defaultPermissions"></a>
# **defaultPermissions**
> defaultPermissions()



Retrieve default repository permissions properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.defaultPermissions();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#defaultPermissions");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="defaultReviewerGroups"></a>
# **defaultReviewerGroups**
> defaultReviewerGroups(key)



Retrieves project&#39;s default reviewer groups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "key_example"; // String | project key
    try {
      apiInstance.defaultReviewerGroups(key);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#defaultReviewerGroups");
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
| **key** | **String**| project key | |

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
| **200** | Successful Response |  -  |

<a id="deleteAllowedReviewerGroup"></a>
# **deleteAllowedReviewerGroup**
> deleteAllowedReviewerGroup(key)



Delete group from project&#39;s allowed reviewer group list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "key_example"; // String | project key
    try {
      apiInstance.deleteAllowedReviewerGroup(key);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteAllowedReviewerGroup");
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
| **key** | **String**| project key | |

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
| **200** | Successful Response |  -  |

<a id="deleteAllowedReviewerUser"></a>
# **deleteAllowedReviewerUser**
> deleteAllowedReviewerUser(key)



Remove user from project&#39;s allowed reviewer users list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "key_example"; // String | project key
    try {
      apiInstance.deleteAllowedReviewerUser(key);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteAllowedReviewerUser");
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
| **key** | **String**| project key | |

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
| **200** | Successful Response |  -  |

<a id="deleteDefaultReviewerGroup"></a>
# **deleteDefaultReviewerGroup**
> deleteDefaultReviewerGroup(key)



Delete group from project&#39;s default reviewer group list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "key_example"; // String | project key
    try {
      apiInstance.deleteDefaultReviewerGroup(key);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteDefaultReviewerGroup");
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
| **key** | **String**| project key | |

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
| **200** | Successful Response |  -  |

<a id="deleteDefaultReviewerUser"></a>
# **deleteDefaultReviewerUser**
> deleteDefaultReviewerUser(key)



Remove user from project&#39;s default reviewer users list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "key_example"; // String | project key
    try {
      apiInstance.deleteDefaultReviewerUser(key);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteDefaultReviewerUser");
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
| **key** | **String**| project key | |

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
| **200** | Successful Response |  -  |

<a id="deletePermissionSchemeAnonymousUsers"></a>
# **deletePermissionSchemeAnonymousUsers**
> deletePermissionSchemeAnonymousUsers(name)



Removes anonymous-user permission [action name] from given permission scheme

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | permission scheme name
    try {
      apiInstance.deletePermissionSchemeAnonymousUsers(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deletePermissionSchemeAnonymousUsers");
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
| **name** | **String**| permission scheme name | |

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
| **200** | Successful Response |  -  |

<a id="deletePermissionSchemeGroup"></a>
# **deletePermissionSchemeGroup**
> deletePermissionSchemeGroup(name)



Removes group permission [group name, action name] from given permission scheme

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | permission scheme name
    try {
      apiInstance.deletePermissionSchemeGroup(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deletePermissionSchemeGroup");
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
| **name** | **String**| permission scheme name | |

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
| **200** | Successful Response |  -  |

<a id="deletePermissionSchemeLoggedUsers"></a>
# **deletePermissionSchemeLoggedUsers**
> deletePermissionSchemeLoggedUsers(name)



Removes logged-in-users permission [action name] from given permission scheme

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | permission scheme name
    try {
      apiInstance.deletePermissionSchemeLoggedUsers(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deletePermissionSchemeLoggedUsers");
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
| **name** | **String**| permission scheme name | |

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
| **200** | Successful Response |  -  |

<a id="deletePermissionSchemeRole"></a>
# **deletePermissionSchemeRole**
> deletePermissionSchemeRole(name)



Removes review-role permission [role name, action name] from given permission scheme

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | permission scheme name
    try {
      apiInstance.deletePermissionSchemeRole(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deletePermissionSchemeRole");
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
| **name** | **String**| permission scheme name | |

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
| **200** | Successful Response |  -  |

<a id="deletePermissionSchemeUser"></a>
# **deletePermissionSchemeUser**
> deletePermissionSchemeUser(name)



Removes user permission [username, action name] from given permission scheme

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | permission scheme name
    try {
      apiInstance.deletePermissionSchemeUser(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deletePermissionSchemeUser");
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
| **name** | **String**| permission scheme name | |

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
| **200** | Successful Response |  -  |

<a id="deleteRepository"></a>
# **deleteRepository**
> deleteRepository(repository)



Deletes repository.  Warning: you can not undo this operation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository to delete
    try {
      apiInstance.deleteRepository(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#deleteRepository");
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
| **repository** | **String**| the key of the repository to delete | |

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
| **200** | Successful Response |  -  |

<a id="disableRepository"></a>
# **disableRepository**
> disableRepository(repository)



Disables repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository to disable
    try {
      apiInstance.disableRepository(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#disableRepository");
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
| **repository** | **String**| the key of the repository to disable | |

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
| **200** | Successful Response |  -  |

<a id="doReviewRevisionReindex"></a>
# **doReviewRevisionReindex**
> doReviewRevisionReindex(repository, synchronous)



Re-indexes all the Crucible revision data (which revisions have been reviewed)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository to reindex
    Boolean synchronous = false; // Boolean | if true will wait for the indexing to finish before returning
    try {
      apiInstance.doReviewRevisionReindex(repository, synchronous);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#doReviewRevisionReindex");
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
| **repository** | **String**| the key of the repository to reindex | |
| **synchronous** | **Boolean**| if true will wait for the indexing to finish before returning | [optional] [default to false] |

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
| **200** | Successful Response |  -  |

<a id="doShareContent"></a>
# **doShareContent**
> doShareContent()



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.doShareContent();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#doShareContent");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="enableRepository"></a>
# **enableRepository**
> enableRepository(repository)



Enables repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository to enable
    try {
      apiInstance.enableRepository(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#enableRepository");
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
| **repository** | **String**| the key of the repository to enable | |

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
| **200** | Successful Response |  -  |

<a id="fullIncrementalIndex"></a>
# **fullIncrementalIndex**
> fullIncrementalIndex(repository)



Runs an full incremental repository index.  For CVS: scans the whole CVS repository for any changes since the last scan.  For other repository types will trigger an incremental index.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository to scan
    try {
      apiInstance.fullIncrementalIndex(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#fullIncrementalIndex");
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
| **repository** | **String**| the key of the repository to scan | |

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
| **200** | Successful Response |  -  |

<a id="getGlobalPref"></a>
# **getGlobalPref**
> getGlobalPref(property)



Getting user&#39;s global preference

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String property = "property_example"; // String | the property(preference) name
    try {
      apiInstance.getGlobalPref(property);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getGlobalPref");
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
| **property** | **String**| the property(preference) name | |

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
| **200** | Successful Response |  -  |

<a id="getInfo"></a>
# **getInfo**
> getInfo()



Provides general information about the server&#39;s configuration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getInfo();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getInfo");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getRecent"></a>
# **getRecent**
> getRecent()



Get a list of recently visited items for the currently logged in user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getRecent();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRecent");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getRecentDetailed"></a>
# **getRecentDetailed**
> getRecentDetailed()



Get a list of recently visisted items for the currently logged in user, including the detailed entities.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getRecentDetailed();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRecentDetailed");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getRecentProjects"></a>
# **getRecentProjects**
> getRecentProjects()



Get a list of recently visited projects for the currently logged in user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getRecentProjects();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRecentProjects");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getRecentProjectsDetailed"></a>
# **getRecentProjectsDetailed**
> getRecentProjectsDetailed()



Get a list of recently visited projects for the currently logged in Project, including the detailed entities.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getRecentProjectsDetailed();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRecentProjectsDetailed");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getRecentRepositories"></a>
# **getRecentRepositories**
> getRecentRepositories()



Get a list of recently visited repositories for the currently logged in user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getRecentRepositories();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRecentRepositories");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getRecentRepositoriesDetailed"></a>
# **getRecentRepositoriesDetailed**
> getRecentRepositoriesDetailed()



Get a list of recently visisted repositories for the currently logged in user, including the detailed entities.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getRecentRepositoriesDetailed();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRecentRepositoriesDetailed");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getRecentReviews"></a>
# **getRecentReviews**
> getRecentReviews()



Get a list of recently visited reviews for the currently logged in user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getRecentReviews();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRecentReviews");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getRecentReviewsDetailed"></a>
# **getRecentReviewsDetailed**
> getRecentReviewsDetailed()



Get a list of recently visited reviews for the currently logged in user, including the detailed entities.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getRecentReviewsDetailed();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRecentReviewsDetailed");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getRecentSnippets"></a>
# **getRecentSnippets**
> getRecentSnippets()



Get a list of recently visited snippets for the currently logged in user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getRecentSnippets();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRecentSnippets");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getRecentSnippetsDetailed"></a>
# **getRecentSnippetsDetailed**
> getRecentSnippetsDetailed()



Get a list of recently visited snippets for the currently logged in user, including the detailed entities.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getRecentSnippetsDetailed();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRecentSnippetsDetailed");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getRecentUsers"></a>
# **getRecentUsers**
> getRecentUsers()



Get a list of recently visited users for the currently logged in user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getRecentUsers();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRecentUsers");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getRecentUsersDetailed"></a>
# **getRecentUsersDetailed**
> getRecentUsersDetailed()



Get a list of recently visited users for the currently logged in user, including the detailed entities.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.getRecentUsersDetailed();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRecentUsersDetailed");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="getRepoPref"></a>
# **getRepoPref**
> getRepoPref(property, repository)



Getting user&#39;s preference related to a certain repository

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String property = "property_example"; // String | the property(preference) name
    String repository = "repository_example"; // String | the key of the repository
    try {
      apiInstance.getRepoPref(property, repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getRepoPref");
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
| **property** | **String**| the property(preference) name | |
| **repository** | **String**| the key of the repository | |

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
| **200** | Successful Response |  -  |

<a id="incrementalIndex"></a>
# **incrementalIndex**
> incrementalIndex(repository, wait)



Runs an incremental repository index.  This is the same operation as triggered by scheduled indexing.  Can be called using the REST API Token to authorize.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository to stop
    Boolean wait = false; // Boolean | if true will wait for the indexing to finish before returning
    try {
      apiInstance.incrementalIndex(repository, wait);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#incrementalIndex");
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
| **repository** | **String**| the key of the repository to stop | |
| **wait** | **Boolean**| if true will wait for the indexing to finish before returning | [optional] [default to false] |

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
| **200** | Successful Response |  -  |

<a id="listAnonymousUsersPrincipalAssociation"></a>
# **listAnonymousUsersPrincipalAssociation**
> listAnonymousUsersPrincipalAssociation(name, action)



Retrieve a page of anonymous users permissions [action name] for given permission scheme.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | permission scheme name
    String action = "action_example"; // String | action name
    try {
      apiInstance.listAnonymousUsersPrincipalAssociation(name, action);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listAnonymousUsersPrincipalAssociation");
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
| **name** | **String**| permission scheme name | |
| **action** | **String**| action name | [optional] |

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
| **200** | Successful Response |  -  |

<a id="listDefaultReviewerUsers"></a>
# **listDefaultReviewerUsers**
> listDefaultReviewerUsers(key)



Retrieves project&#39;s default reviewer users

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "key_example"; // String | project key
    try {
      apiInstance.listDefaultReviewerUsers(key);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listDefaultReviewerUsers");
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
| **key** | **String**| project key | |

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
| **200** | Successful Response |  -  |

<a id="listGroupPrincipalAssociation"></a>
# **listGroupPrincipalAssociation**
> listGroupPrincipalAssociation(name, name2, action)



Retrieve a page of group permissions [group name, action name] for given permission scheme.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | permission scheme name
    String name2 = "name_example"; // String | group name
    String action = "action_example"; // String | action name
    try {
      apiInstance.listGroupPrincipalAssociation(name, name2, action);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listGroupPrincipalAssociation");
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
| **name** | **String**| permission scheme name | |
| **name2** | **String**| group name | [optional] |
| **action** | **String**| action name | [optional] |

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
| **200** | Successful Response |  -  |

<a id="listGroupUsers"></a>
# **listGroupUsers**
> listGroupUsers(name)



Lists group&#39;s user names

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | group name
    try {
      apiInstance.listGroupUsers(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listGroupUsers");
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
| **name** | **String**| group name | |

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
| **200** | Successful Response |  -  |

<a id="listLoggedUsersPrincipalAssociation"></a>
# **listLoggedUsersPrincipalAssociation**
> listLoggedUsersPrincipalAssociation(name, action)



Retrieve a page of logged in users permissions [action name] for given permission scheme.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | permission scheme name
    String action = "action_example"; // String | action name
    try {
      apiInstance.listLoggedUsersPrincipalAssociation(name, action);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listLoggedUsersPrincipalAssociation");
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
| **name** | **String**| permission scheme name | |
| **action** | **String**| action name | [optional] |

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
| **200** | Successful Response |  -  |

<a id="listProjects"></a>
# **listProjects**
> listProjects(name)



Retrieve a page of projects for given permission scheme.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | permission scheme name
    try {
      apiInstance.listProjects(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listProjects");
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
| **name** | **String**| permission scheme name | |

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
| **200** | Successful Response |  -  |

<a id="listRolesPrincipalAssociation"></a>
# **listRolesPrincipalAssociation**
> listRolesPrincipalAssociation(name, name2, action)



Retrieve a page of review-roles permissions [role name, action name] for given permission scheme.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | permission scheme name
    String name2 = "name_example"; // String | role name
    String action = "action_example"; // String | action name
    try {
      apiInstance.listRolesPrincipalAssociation(name, name2, action);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listRolesPrincipalAssociation");
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
| **name** | **String**| permission scheme name | |
| **name2** | **String**| role name | [optional] |
| **action** | **String**| action name | [optional] |

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
| **200** | Successful Response |  -  |

<a id="listUserGroups"></a>
# **listUserGroups**
> listUserGroups(name)



Lists user&#39;s group names

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | user name
    try {
      apiInstance.listUserGroups(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listUserGroups");
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
| **name** | **String**| user name | |

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
| **200** | Successful Response |  -  |

<a id="listUserPrincipalAssociation"></a>
# **listUserPrincipalAssociation**
> listUserPrincipalAssociation(name, name2, action)



Retrieve a page of user permissions [username, action name] for given permission scheme.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | permission scheme name
    String name2 = "name_example"; // String | permission scheme name
    String action = "action_example"; // String | action name
    try {
      apiInstance.listUserPrincipalAssociation(name, name2, action);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#listUserPrincipalAssociation");
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
| **name** | **String**| permission scheme name | |
| **name2** | **String**| permission scheme name | [optional] |
| **action** | **String**| action name | [optional] |

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
| **200** | Successful Response |  -  |

<a id="login"></a>
# **login**
> login()



Get the user authentication token.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.login();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#login");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="moveAllReviews"></a>
# **moveAllReviews**
> moveAllReviews(sourceProjectKey, destinationProjectKey)



Move reviews and snippets from source project to destination project

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String sourceProjectKey = "sourceProjectKey_example"; // String | project key of reviews and snippets source project
    String destinationProjectKey = "destinationProjectKey_example"; // String | project key of reviews and snippets destination project
    try {
      apiInstance.moveAllReviews(sourceProjectKey, destinationProjectKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#moveAllReviews");
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
| **sourceProjectKey** | **String**| project key of reviews and snippets source project | |
| **destinationProjectKey** | **String**| project key of reviews and snippets destination project | |

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
| **200** | Successful Response |  -  |

<a id="permissions"></a>
# **permissions**
> permissions(repository)



Retrieve repository permissions properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository
    try {
      apiInstance.permissions(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#permissions");
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
| **repository** | **String**| the key of the repository | |

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
| **200** | Successful Response |  -  |

<a id="permissionsGroups"></a>
# **permissionsGroups**
> permissionsGroups(repository)



Note: use /rest-service-fecru/admin/repository-permissions/ endpoint for full repository permission administration functionality  Lists groups allowed to access repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository
    try {
      apiInstance.permissionsGroups(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#permissionsGroups");
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
| **repository** | **String**| the key of the repository | |

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
| **200** | Successful Response |  -  |

<a id="rebuildSearchIndex"></a>
# **rebuildSearchIndex**
> rebuildSearchIndex(repository)



Rebuilds the search index data for the given repository. This will rebuild the data used to search by path,  commit message and comitter, also used for activity streams and JIRA integration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository to re-index.
    try {
      apiInstance.rebuildSearchIndex(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#rebuildSearchIndex");
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
| **repository** | **String**| the key of the repository to re-index. | |

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
| **200** | Successful Response |  -  |

<a id="reindexChangesetComments"></a>
# **reindexChangesetComments**
> reindexChangesetComments(repository)



Rebuilds the changeset discussion index for the specified repository. The index is used to display changeset  discussions in activity streams.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository to perform the operation for
    try {
      apiInstance.reindexChangesetComments(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#reindexChangesetComments");
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
| **repository** | **String**| the key of the repository to perform the operation for | |

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
| **200** | Successful Response |  -  |

<a id="reindexChangesetDiscussion"></a>
# **reindexChangesetDiscussion**
> reindexChangesetDiscussion(repository)



Rebuilds the changeset discussion index for the specified repository. The index is used to display changeset  discussions in activity streams.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository to perform the operation for
    try {
      apiInstance.reindexChangesetDiscussion(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#reindexChangesetDiscussion");
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
| **repository** | **String**| the key of the repository to perform the operation for | |

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
| **200** | Successful Response |  -  |

<a id="reindexReviews"></a>
# **reindexReviews**
> reindexReviews(repository)



Re-indexes all the Crucible revision data (which revisions have been reviewed)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository to reindex
    try {
      apiInstance.reindexReviews(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#reindexReviews");
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
| **repository** | **String**| the key of the repository to reindex | |

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
| **200** | Successful Response |  -  |

<a id="reindexSearch"></a>
# **reindexSearch**
> reindexSearch(repository)



Rebuilds the search index data for the given repository. This will rebuild the data used to search by path,  commit message and committer, also used for activity streams and JIRA integration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository to re-index.
    try {
      apiInstance.reindexSearch(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#reindexSearch");
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
| **repository** | **String**| the key of the repository to re-index. | |

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
| **200** | Successful Response |  -  |

<a id="removeGroupToPermissions"></a>
# **removeGroupToPermissions**
> removeGroupToPermissions(repository)



Delete group from repository allowed groups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository
    try {
      apiInstance.removeGroupToPermissions(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#removeGroupToPermissions");
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
| **repository** | **String**| the key of the repository | |

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
| **200** | Successful Response |  -  |

<a id="repositoryUpdates"></a>
# **repositoryUpdates**
> repositoryUpdates(repository)



Retrieves repository updates properties.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | repository key
    try {
      apiInstance.repositoryUpdates(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#repositoryUpdates");
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
| **repository** | **String**| repository key | |

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
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminGroupsGet"></a>
# **restServiceFecruAdminGroupsGet**
> restServiceFecruAdminGroupsGet(prefix)



Retrieve a page of groups.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String prefix = "prefix_example"; // String | filter groups by name prefix
    try {
      apiInstance.restServiceFecruAdminGroupsGet(prefix);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminGroupsGet");
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
| **prefix** | **String**| filter groups by name prefix | [optional] |

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
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminGroupsNameDelete"></a>
# **restServiceFecruAdminGroupsNameDelete**
> restServiceFecruAdminGroupsNameDelete(name)



Deletes a group by name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | group name
    try {
      apiInstance.restServiceFecruAdminGroupsNameDelete(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminGroupsNameDelete");
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
| **name** | **String**| group name | |

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
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminGroupsNameGet"></a>
# **restServiceFecruAdminGroupsNameGet**
> restServiceFecruAdminGroupsNameGet(name)



Retrieve a group by name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | group name
    try {
      apiInstance.restServiceFecruAdminGroupsNameGet(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminGroupsNameGet");
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
| **name** | **String**| group name | |

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
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminGroupsNamePut"></a>
# **restServiceFecruAdminGroupsNamePut**
> restServiceFecruAdminGroupsNamePut(name)



Updates an existing group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | group name
    try {
      apiInstance.restServiceFecruAdminGroupsNamePut(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminGroupsNamePut");
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
| **name** | **String**| group name | |

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
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminGroupsNameUsersDelete"></a>
# **restServiceFecruAdminGroupsNameUsersDelete**
> restServiceFecruAdminGroupsNameUsersDelete(name)



Removes user from group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | group name
    try {
      apiInstance.restServiceFecruAdminGroupsNameUsersDelete(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminGroupsNameUsersDelete");
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
| **name** | **String**| group name | |

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
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminGroupsNameUsersPut"></a>
# **restServiceFecruAdminGroupsNameUsersPut**
> restServiceFecruAdminGroupsNameUsersPut(name)



Adds user to group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | group name
    try {
      apiInstance.restServiceFecruAdminGroupsNameUsersPut(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminGroupsNameUsersPut");
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
| **name** | **String**| group name | |

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
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminGroupsPost"></a>
# **restServiceFecruAdminGroupsPost**
> restServiceFecruAdminGroupsPost()



Creates a new user group.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.restServiceFecruAdminGroupsPost();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminGroupsPost");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminPermissionSchemesGet"></a>
# **restServiceFecruAdminPermissionSchemesGet**
> restServiceFecruAdminPermissionSchemesGet(name)



Retrieve a page of permission schemes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | permission scheme name part filter, case insensitive, optional
    try {
      apiInstance.restServiceFecruAdminPermissionSchemesGet(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminPermissionSchemesGet");
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
| **name** | **String**| permission scheme name part filter, case insensitive, optional | [optional] |

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
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminPermissionSchemesNameDelete"></a>
# **restServiceFecruAdminPermissionSchemesNameDelete**
> restServiceFecruAdminPermissionSchemesNameDelete(name)



Deletes a permission scheme by name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | permission scheme name
    try {
      apiInstance.restServiceFecruAdminPermissionSchemesNameDelete(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminPermissionSchemesNameDelete");
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
| **name** | **String**| permission scheme name | |

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
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminPermissionSchemesNameGet"></a>
# **restServiceFecruAdminPermissionSchemesNameGet**
> restServiceFecruAdminPermissionSchemesNameGet(name)



Retrieve a permission scheme by name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | permission scheme name
    try {
      apiInstance.restServiceFecruAdminPermissionSchemesNameGet(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminPermissionSchemesNameGet");
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
| **name** | **String**| permission scheme name | |

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
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminPermissionSchemesNamePut"></a>
# **restServiceFecruAdminPermissionSchemesNamePut**
> restServiceFecruAdminPermissionSchemesNamePut(name)



Updates an existing permission scheme.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | permission scheme name
    try {
      apiInstance.restServiceFecruAdminPermissionSchemesNamePut(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminPermissionSchemesNamePut");
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
| **name** | **String**| permission scheme name | |

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
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminPermissionSchemesPost"></a>
# **restServiceFecruAdminPermissionSchemesPost**
> restServiceFecruAdminPermissionSchemesPost(copyFrom)



Creates a new permission scheme. The new permission scheme is blank or can be created from another existing permission scheme.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String copyFrom = "copyFrom_example"; // String | if set, the new permission scheme will be a copy of permissionSchemeName
    try {
      apiInstance.restServiceFecruAdminPermissionSchemesPost(copyFrom);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminPermissionSchemesPost");
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
| **copyFrom** | **String**| if set, the new permission scheme will be a copy of permissionSchemeName | [optional] |

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
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminProjectsGet"></a>
# **restServiceFecruAdminProjectsGet**
> restServiceFecruAdminProjectsGet(name, key, defaultRepositoryName, permissionSchemeName)



Retrieve a page of projects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | project's name part filter, optional
    String key = "key_example"; // String | project's key part filter, optional
    String defaultRepositoryName = "defaultRepositoryName_example"; // String | project's default repository key part filter, optional
    String permissionSchemeName = "permissionSchemeName_example"; // String | project's permission scheme pare name filter, optional
    try {
      apiInstance.restServiceFecruAdminProjectsGet(name, key, defaultRepositoryName, permissionSchemeName);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminProjectsGet");
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
| **name** | **String**| project&#39;s name part filter, optional | [optional] |
| **key** | **String**| project&#39;s key part filter, optional | [optional] |
| **defaultRepositoryName** | **String**| project&#39;s default repository key part filter, optional | [optional] |
| **permissionSchemeName** | **String**| project&#39;s permission scheme pare name filter, optional | [optional] |

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
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminProjectsKeyDelete"></a>
# **restServiceFecruAdminProjectsKeyDelete**
> restServiceFecruAdminProjectsKeyDelete(key, deleteProjectReviews)



Deletes a project by key (including all reviews in this project).  Use   to move reviews to another project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "key_example"; // String | project key
    Boolean deleteProjectReviews = false; // Boolean | if true deletes reviews in project
    try {
      apiInstance.restServiceFecruAdminProjectsKeyDelete(key, deleteProjectReviews);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminProjectsKeyDelete");
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
| **key** | **String**| project key | |
| **deleteProjectReviews** | **Boolean**| if true deletes reviews in project | [optional] [default to false] |

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
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminProjectsKeyGet"></a>
# **restServiceFecruAdminProjectsKeyGet**
> restServiceFecruAdminProjectsKeyGet(key)



Retrieve a project by key.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "key_example"; // String | project key
    try {
      apiInstance.restServiceFecruAdminProjectsKeyGet(key);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminProjectsKeyGet");
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
| **key** | **String**| project key | |

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
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminProjectsKeyPut"></a>
# **restServiceFecruAdminProjectsKeyPut**
> restServiceFecruAdminProjectsKeyPut(key)



Updates an existing project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String key = "key_example"; // String | project key
    try {
      apiInstance.restServiceFecruAdminProjectsKeyPut(key);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminProjectsKeyPut");
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
| **key** | **String**| project key | |

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
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminProjectsPost"></a>
# **restServiceFecruAdminProjectsPost**
> restServiceFecruAdminProjectsPost()



Creates a new project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.restServiceFecruAdminProjectsPost();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminProjectsPost");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminRepositoriesGet"></a>
# **restServiceFecruAdminRepositoriesGet**
> restServiceFecruAdminRepositoriesGet(type, enabled, started)



Retrieve a page of repositories. Repository properties with default values may not be returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String type = "type_example"; // String | filter repositories by repository type: svn, git, hg, cvs, p4, ...
    Boolean enabled = true; // Boolean | filter repositories by enabled flag
    Boolean started = true; // Boolean | filter repositories by started flag
    try {
      apiInstance.restServiceFecruAdminRepositoriesGet(type, enabled, started);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminRepositoriesGet");
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
| **type** | **String**| filter repositories by repository type: svn, git, hg, cvs, p4, ... | [optional] |
| **enabled** | **Boolean**| filter repositories by enabled flag | [optional] |
| **started** | **Boolean**| filter repositories by started flag | [optional] |

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
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminRepositoriesPost"></a>
# **restServiceFecruAdminRepositoriesPost**
> restServiceFecruAdminRepositoriesPost()



Creates a repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.restServiceFecruAdminRepositoriesPost();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminRepositoriesPost");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminRepositoriesRepositoryDelete"></a>
# **restServiceFecruAdminRepositoriesRepositoryDelete**
> restServiceFecruAdminRepositoriesRepositoryDelete(repository)



Deletes a repository by key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository
    try {
      apiInstance.restServiceFecruAdminRepositoriesRepositoryDelete(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminRepositoriesRepositoryDelete");
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
| **repository** | **String**| the key of the repository | |

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
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminRepositoriesRepositoryGet"></a>
# **restServiceFecruAdminRepositoriesRepositoryGet**
> restServiceFecruAdminRepositoriesRepositoryGet(repository)



Retrieve a repository by key. Repository properties with default values may not be returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository
    try {
      apiInstance.restServiceFecruAdminRepositoriesRepositoryGet(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminRepositoriesRepositoryGet");
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
| **repository** | **String**| the key of the repository | |

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
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminRepositoriesRepositoryPut"></a>
# **restServiceFecruAdminRepositoriesRepositoryPut**
> restServiceFecruAdminRepositoriesRepositoryPut(repository)



Updates an existing repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository
    try {
      apiInstance.restServiceFecruAdminRepositoriesRepositoryPut(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminRepositoriesRepositoryPut");
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
| **repository** | **String**| the key of the repository | |

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
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminRepositoriesRepositoryReindexLinecountPut"></a>
# **restServiceFecruAdminRepositoriesRepositoryReindexLinecountPut**
> restServiceFecruAdminRepositoriesRepositoryReindexLinecountPut(repository)



Re-indexes the linecount data used to generate the LOC graphs. The linecount data will be recalculated in daily  buckets based on the server timezone.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository to re-index
    try {
      apiInstance.restServiceFecruAdminRepositoriesRepositoryReindexLinecountPut(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminRepositoriesRepositoryReindexLinecountPut");
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
| **repository** | **String**| the key of the repository to re-index | |

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
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminRepositoriesRepositoryReindexSourcePut"></a>
# **restServiceFecruAdminRepositoriesRepositoryReindexSourcePut**
> restServiceFecruAdminRepositoriesRepositoryReindexSourcePut(repository, clone)



Deletes the existing cache and re-indexes the repository from scratch.  For large or slow repositories this may take some time, during which some functionality will be unavailable.  This action will also restart the repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository to reindex
    Boolean clone = false; // Boolean | if true and the repository is a dvcs repository (git or mercurial) it will re-clone the repository before re-indexing
    try {
      apiInstance.restServiceFecruAdminRepositoriesRepositoryReindexSourcePut(repository, clone);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminRepositoriesRepositoryReindexSourcePut");
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
| **repository** | **String**| the key of the repository to reindex | |
| **clone** | **Boolean**| if true and the repository is a dvcs repository (git or mercurial) it will re-clone the repository before re-indexing | [optional] [default to false] |

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
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminRepositoriesRepositoryRescanMetadataPut"></a>
# **restServiceFecruAdminRepositoriesRepositoryRescanMetadataPut**
> restServiceFecruAdminRepositoriesRepositoryRescanMetadataPut(repository, from, to)



Re-scans the repository metadata. Only valid for Perforce and SVN repositories.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository to re-scan
    String from = "from_example"; // String | the revision number to start at
    String to = "to_example"; // String | the revision number to end at
    try {
      apiInstance.restServiceFecruAdminRepositoriesRepositoryRescanMetadataPut(repository, from, to);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminRepositoriesRepositoryRescanMetadataPut");
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
| **repository** | **String**| the key of the repository to re-scan | |
| **from** | **String**| the revision number to start at | [optional] |
| **to** | **String**| the revision number to end at | [optional] |

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
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminRepositoriesV1RepositoryGet"></a>
# **restServiceFecruAdminRepositoriesV1RepositoryGet**
> restServiceFecruAdminRepositoriesV1RepositoryGet(repository)



Returns information about the status of the repository and the current indexing status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository
    try {
      apiInstance.restServiceFecruAdminRepositoriesV1RepositoryGet(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminRepositoriesV1RepositoryGet");
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
| **repository** | **String**| the key of the repository | |

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
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminRepositoriesV1RepositoryReindexLinecountPost"></a>
# **restServiceFecruAdminRepositoriesV1RepositoryReindexLinecountPost**
> restServiceFecruAdminRepositoriesV1RepositoryReindexLinecountPost(repository)



Re-indexes the linecount data used to generate the LOC graphs. The linecount data will be recalculated in daily  buckets based on the server timezone.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository to re-index
    try {
      apiInstance.restServiceFecruAdminRepositoriesV1RepositoryReindexLinecountPost(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminRepositoriesV1RepositoryReindexLinecountPost");
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
| **repository** | **String**| the key of the repository to re-index | |

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
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminRepositoriesV1RepositoryReindexSourcePost"></a>
# **restServiceFecruAdminRepositoriesV1RepositoryReindexSourcePost**
> restServiceFecruAdminRepositoriesV1RepositoryReindexSourcePost(repository, clone)



Deletes the existing cache and re-indexes the repository from scratch.  For large or slow repositories this may take some time, during which some functionality will be unavailable.  This action will also restart the repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository to reindex
    Boolean clone = false; // Boolean | if true and the repository is a dvcs repository (git or mercurial) it will re-clone the repository  before re-indexing
    try {
      apiInstance.restServiceFecruAdminRepositoriesV1RepositoryReindexSourcePost(repository, clone);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminRepositoriesV1RepositoryReindexSourcePost");
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
| **repository** | **String**| the key of the repository to reindex | |
| **clone** | **Boolean**| if true and the repository is a dvcs repository (git or mercurial) it will re-clone the repository  before re-indexing | [optional] [default to false] |

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
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminRepositoriesV1RepositoryRescanMetadataPost"></a>
# **restServiceFecruAdminRepositoriesV1RepositoryRescanMetadataPost**
> restServiceFecruAdminRepositoriesV1RepositoryRescanMetadataPost(repository, from, to)



Re-scans the repository metadata for SVN and Perforce repositories. Only valid for Perforce and SVN repositories.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository to re-scan
    Long from = 56L; // Long | the revision number to start at
    Long to = 56L; // Long | the revision number to end at
    try {
      apiInstance.restServiceFecruAdminRepositoriesV1RepositoryRescanMetadataPost(repository, from, to);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminRepositoriesV1RepositoryRescanMetadataPost");
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
| **repository** | **String**| the key of the repository to re-scan | |
| **from** | **Long**| the revision number to start at | [optional] |
| **to** | **Long**| the revision number to end at | [optional] |

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
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminUsersGet"></a>
# **restServiceFecruAdminUsersGet**
> restServiceFecruAdminUsersGet()



Retrieve a page of users.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.restServiceFecruAdminUsersGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminUsersGet");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminUsersNameDelete"></a>
# **restServiceFecruAdminUsersNameDelete**
> restServiceFecruAdminUsersNameDelete(name)



Deletes a user by name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | user name
    try {
      apiInstance.restServiceFecruAdminUsersNameDelete(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminUsersNameDelete");
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
| **name** | **String**| user name | |

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
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminUsersNameGet"></a>
# **restServiceFecruAdminUsersNameGet**
> restServiceFecruAdminUsersNameGet(name)



Retrieve a user by name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | user name
    try {
      apiInstance.restServiceFecruAdminUsersNameGet(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminUsersNameGet");
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
| **name** | **String**| user name | |

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
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminUsersNameGroupsDelete"></a>
# **restServiceFecruAdminUsersNameGroupsDelete**
> restServiceFecruAdminUsersNameGroupsDelete(name)



Removes user from group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | user name
    try {
      apiInstance.restServiceFecruAdminUsersNameGroupsDelete(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminUsersNameGroupsDelete");
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
| **name** | **String**| user name | |

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
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminUsersNameGroupsPut"></a>
# **restServiceFecruAdminUsersNameGroupsPut**
> restServiceFecruAdminUsersNameGroupsPut(name)



Adds user to group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | user name
    try {
      apiInstance.restServiceFecruAdminUsersNameGroupsPut(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminUsersNameGroupsPut");
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
| **name** | **String**| user name | |

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
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminUsersNamePut"></a>
# **restServiceFecruAdminUsersNamePut**
> restServiceFecruAdminUsersNamePut(name)



Updates an existing user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String name = "name_example"; // String | user name
    try {
      apiInstance.restServiceFecruAdminUsersNamePut(name);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminUsersNamePut");
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
| **name** | **String**| user name | |

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
| **200** | Successful Response |  -  |

<a id="restServiceFecruAdminUsersPost"></a>
# **restServiceFecruAdminUsersPost**
> restServiceFecruAdminUsersPost()



Creates a new user. Tries to add the user to fisheye-users and crucible-users groups if those exist.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.restServiceFecruAdminUsersPost();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruAdminUsersPost");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="restServiceFecruIndexingStatusV1StatusRepositoryGet"></a>
# **restServiceFecruIndexingStatusV1StatusRepositoryGet**
> restServiceFecruIndexingStatusV1StatusRepositoryGet(repository)



Returns indexing status of given repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository to get status of
    try {
      apiInstance.restServiceFecruIndexingStatusV1StatusRepositoryGet(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#restServiceFecruIndexingStatusV1StatusRepositoryGet");
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
| **repository** | **String**| the key of the repository to get status of | |

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
| **200** | Successful Response |  -  |

<a id="scan"></a>
# **scan**
> scan(repository, synchronous)



Runs an incremental repository index now.  This is the same operation as triggered by scheduled indexing.  Can be called using the REST Api Token to authorize.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository to run scan for
    Boolean synchronous = false; // Boolean | if true will wait for the indexing to finish before returning
    try {
      apiInstance.scan(repository, synchronous);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#scan");
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
| **repository** | **String**| the key of the repository to run scan for | |
| **synchronous** | **Boolean**| if true will wait for the indexing to finish before returning | [optional] [default to false] |

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
| **200** | Successful Response |  -  |

<a id="scanCvs"></a>
# **scanCvs**
> scanCvs(repository)



Scans the whole CVS repository for any changes since the last scan. Only valid for CVS repositories.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository to scan
    try {
      apiInstance.scanCvs(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#scanCvs");
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
| **repository** | **String**| the key of the repository to scan | |

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
| **200** | Successful Response |  -  |

<a id="setPref"></a>
# **setPref**
> setPref()



Using POST method to set a user preference.  If repo is not set, the preference will be recognised as a global preference.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.setPref();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#setPref");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="start"></a>
# **start**
> start(repository)



Starts repository. Does not wait for the repository to start before returning.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository to start
    try {
      apiInstance.start(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#start");
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
| **repository** | **String**| the key of the repository to start | |

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
| **200** | Successful Response |  -  |

<a id="startRepository"></a>
# **startRepository**
> startRepository(repository)



Starts the repository.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository to start
    try {
      apiInstance.startRepository(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#startRepository");
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
| **repository** | **String**| the key of the repository to start | |

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
| **200** | Successful Response |  -  |

<a id="stop"></a>
# **stop**
> stop(repository)



Stops repository. Does not wait for the repository to stop before returning.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository to stop
    try {
      apiInstance.stop(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#stop");
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
| **repository** | **String**| the key of the repository to stop | |

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
| **200** | Successful Response |  -  |

<a id="stopRepository"></a>
# **stopRepository**
> stopRepository(repository)



Stops the repository. Does not wait for the repository to stop before returning.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository to stop
    try {
      apiInstance.stopRepository(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#stopRepository");
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
| **repository** | **String**| the key of the repository to stop | |

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
| **200** | Successful Response |  -  |

<a id="updateDefaultPermissions"></a>
# **updateDefaultPermissions**
> updateDefaultPermissions()



Updates default repository permissions properties.   Valid permission settings: any combination of allowAnonymous, allowLoggedIn

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.updateDefaultPermissions();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateDefaultPermissions");
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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |

<a id="updatePermissions"></a>
# **updatePermissions**
> updatePermissions(repository)



Updates repository permissions properties.   Valid permission settings: any combination of useDefaults, allowAnonymous, allowLoggedIn.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | the key of the repository
    try {
      apiInstance.updatePermissions(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updatePermissions");
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
| **repository** | **String**| the key of the repository | |

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
| **200** | Successful Response |  -  |

<a id="updateRepositoryUpdates"></a>
# **updateRepositoryUpdates**
> updateRepositoryUpdates(repository)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://fecru.local/context");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String repository = "repository_example"; // String | repository key
    try {
      apiInstance.updateRepositoryUpdates(repository);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#updateRepositoryUpdates");
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
| **repository** | **String**| repository key | |

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
| **200** | Successful Response |  -  |

