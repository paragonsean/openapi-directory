# FisheyeCrucible.DefaultApi

All URIs are relative to *http://fecru.local/context*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addAllowedReviewerGroup**](DefaultApi.md#addAllowedReviewerGroup) | **PUT** /rest-service-fecru/admin/projects/{key}/allowed-reviewer-groups | 
[**addAllowedReviewerUser**](DefaultApi.md#addAllowedReviewerUser) | **PUT** /rest-service-fecru/admin/projects/{key}/allowed-reviewer-users | 
[**addDefaultReviewerGroup**](DefaultApi.md#addDefaultReviewerGroup) | **PUT** /rest-service-fecru/admin/projects/{key}/default-reviewer-groups | 
[**addDefaultReviewerUser**](DefaultApi.md#addDefaultReviewerUser) | **PUT** /rest-service-fecru/admin/projects/{key}/default-reviewer-users | 
[**addGroupToPermissions**](DefaultApi.md#addGroupToPermissions) | **PUT** /rest-service-fecru/admin/repositories/{repository}/permissions/groups | 
[**addPermissionSchemeAnonymousUsers**](DefaultApi.md#addPermissionSchemeAnonymousUsers) | **PUT** /rest-service-fecru/admin/permission-schemes/{name}/anonymous-users | 
[**addPermissionSchemeGroup**](DefaultApi.md#addPermissionSchemeGroup) | **PUT** /rest-service-fecru/admin/permission-schemes/{name}/groups | 
[**addPermissionSchemeLoggedUsers**](DefaultApi.md#addPermissionSchemeLoggedUsers) | **PUT** /rest-service-fecru/admin/permission-schemes/{name}/logged-in-users | 
[**addPermissionSchemeReviewRole**](DefaultApi.md#addPermissionSchemeReviewRole) | **PUT** /rest-service-fecru/admin/permission-schemes/{name}/review-roles | 
[**addPermissionSchemeUser**](DefaultApi.md#addPermissionSchemeUser) | **PUT** /rest-service-fecru/admin/permission-schemes/{name}/users | 
[**addRepository**](DefaultApi.md#addRepository) | **POST** /rest-service-fecru/admin/repositories-v1 | 
[**allowedReviewerGroups**](DefaultApi.md#allowedReviewerGroups) | **GET** /rest-service-fecru/admin/projects/{key}/allowed-reviewer-groups | 
[**allowedReviewerUsers**](DefaultApi.md#allowedReviewerUsers) | **GET** /rest-service-fecru/admin/projects/{key}/allowed-reviewer-users | 
[**defaultPermissions**](DefaultApi.md#defaultPermissions) | **GET** /rest-service-fecru/admin/repositories/~defaults/permissions | 
[**defaultReviewerGroups**](DefaultApi.md#defaultReviewerGroups) | **GET** /rest-service-fecru/admin/projects/{key}/default-reviewer-groups | 
[**deleteAllowedReviewerGroup**](DefaultApi.md#deleteAllowedReviewerGroup) | **DELETE** /rest-service-fecru/admin/projects/{key}/allowed-reviewer-groups | 
[**deleteAllowedReviewerUser**](DefaultApi.md#deleteAllowedReviewerUser) | **DELETE** /rest-service-fecru/admin/projects/{key}/allowed-reviewer-users | 
[**deleteDefaultReviewerGroup**](DefaultApi.md#deleteDefaultReviewerGroup) | **DELETE** /rest-service-fecru/admin/projects/{key}/default-reviewer-groups | 
[**deleteDefaultReviewerUser**](DefaultApi.md#deleteDefaultReviewerUser) | **DELETE** /rest-service-fecru/admin/projects/{key}/default-reviewer-users | 
[**deletePermissionSchemeAnonymousUsers**](DefaultApi.md#deletePermissionSchemeAnonymousUsers) | **DELETE** /rest-service-fecru/admin/permission-schemes/{name}/anonymous-users | 
[**deletePermissionSchemeGroup**](DefaultApi.md#deletePermissionSchemeGroup) | **DELETE** /rest-service-fecru/admin/permission-schemes/{name}/groups | 
[**deletePermissionSchemeLoggedUsers**](DefaultApi.md#deletePermissionSchemeLoggedUsers) | **DELETE** /rest-service-fecru/admin/permission-schemes/{name}/logged-in-users | 
[**deletePermissionSchemeRole**](DefaultApi.md#deletePermissionSchemeRole) | **DELETE** /rest-service-fecru/admin/permission-schemes/{name}/review-roles | 
[**deletePermissionSchemeUser**](DefaultApi.md#deletePermissionSchemeUser) | **DELETE** /rest-service-fecru/admin/permission-schemes/{name}/users | 
[**deleteRepository**](DefaultApi.md#deleteRepository) | **DELETE** /rest-service-fecru/admin/repositories-v1/{repository}/ | 
[**disableRepository**](DefaultApi.md#disableRepository) | **POST** /rest-service-fecru/admin/repositories-v1/{repository}/disable | 
[**doReviewRevisionReindex**](DefaultApi.md#doReviewRevisionReindex) | **POST** /rest-service-fecru/admin/repositories-v1/{repository}/reindex-reviews | 
[**doShareContent**](DefaultApi.md#doShareContent) | **POST** /rest-service-fecru/share-content-v1/share | 
[**enableRepository**](DefaultApi.md#enableRepository) | **POST** /rest-service-fecru/admin/repositories-v1/{repository}/enable | 
[**fullIncrementalIndex**](DefaultApi.md#fullIncrementalIndex) | **PUT** /rest-service-fecru/admin/repositories/{repository}/full-incremental-index | 
[**getGlobalPref**](DefaultApi.md#getGlobalPref) | **GET** /rest-service-fecru/user-prefs-v1/{property} | 
[**getInfo**](DefaultApi.md#getInfo) | **GET** /rest-service-fecru/server-v1 | 
[**getRecent**](DefaultApi.md#getRecent) | **GET** /rest-service-fecru/recently-visited-v1 | 
[**getRecentDetailed**](DefaultApi.md#getRecentDetailed) | **GET** /rest-service-fecru/recently-visited-v1/detailed | 
[**getRecentProjects**](DefaultApi.md#getRecentProjects) | **GET** /rest-service-fecru/recently-visited-v1/projects | 
[**getRecentProjectsDetailed**](DefaultApi.md#getRecentProjectsDetailed) | **GET** /rest-service-fecru/recently-visited-v1/projects/detailed | 
[**getRecentRepositories**](DefaultApi.md#getRecentRepositories) | **GET** /rest-service-fecru/recently-visited-v1/repositories | 
[**getRecentRepositoriesDetailed**](DefaultApi.md#getRecentRepositoriesDetailed) | **GET** /rest-service-fecru/recently-visited-v1/repositories/detailed | 
[**getRecentReviews**](DefaultApi.md#getRecentReviews) | **GET** /rest-service-fecru/recently-visited-v1/reviews | 
[**getRecentReviewsDetailed**](DefaultApi.md#getRecentReviewsDetailed) | **GET** /rest-service-fecru/recently-visited-v1/reviews/detailed | 
[**getRecentSnippets**](DefaultApi.md#getRecentSnippets) | **GET** /rest-service-fecru/recently-visited-v1/snippets | 
[**getRecentSnippetsDetailed**](DefaultApi.md#getRecentSnippetsDetailed) | **GET** /rest-service-fecru/recently-visited-v1/snippets/detailed | 
[**getRecentUsers**](DefaultApi.md#getRecentUsers) | **GET** /rest-service-fecru/recently-visited-v1/users | 
[**getRecentUsersDetailed**](DefaultApi.md#getRecentUsersDetailed) | **GET** /rest-service-fecru/recently-visited-v1/users/detailed | 
[**getRepoPref**](DefaultApi.md#getRepoPref) | **GET** /rest-service-fecru/user-prefs-v1/{repository}/{property} | 
[**incrementalIndex**](DefaultApi.md#incrementalIndex) | **PUT** /rest-service-fecru/admin/repositories/{repository}/incremental-index | 
[**listAnonymousUsersPrincipalAssociation**](DefaultApi.md#listAnonymousUsersPrincipalAssociation) | **GET** /rest-service-fecru/admin/permission-schemes/{name}/anonymous-users | 
[**listDefaultReviewerUsers**](DefaultApi.md#listDefaultReviewerUsers) | **GET** /rest-service-fecru/admin/projects/{key}/default-reviewer-users | 
[**listGroupPrincipalAssociation**](DefaultApi.md#listGroupPrincipalAssociation) | **GET** /rest-service-fecru/admin/permission-schemes/{name}/groups | 
[**listGroupUsers**](DefaultApi.md#listGroupUsers) | **GET** /rest-service-fecru/admin/groups/{name}/users | 
[**listLoggedUsersPrincipalAssociation**](DefaultApi.md#listLoggedUsersPrincipalAssociation) | **GET** /rest-service-fecru/admin/permission-schemes/{name}/logged-in-users | 
[**listProjects**](DefaultApi.md#listProjects) | **GET** /rest-service-fecru/admin/permission-schemes/{name}/projects | 
[**listRolesPrincipalAssociation**](DefaultApi.md#listRolesPrincipalAssociation) | **GET** /rest-service-fecru/admin/permission-schemes/{name}/review-roles | 
[**listUserGroups**](DefaultApi.md#listUserGroups) | **GET** /rest-service-fecru/admin/users/{name}/groups | 
[**listUserPrincipalAssociation**](DefaultApi.md#listUserPrincipalAssociation) | **GET** /rest-service-fecru/admin/permission-schemes/{name}/users | 
[**login**](DefaultApi.md#login) | **POST** /rest-service-fecru/auth/login | 
[**moveAllReviews**](DefaultApi.md#moveAllReviews) | **PUT** /rest-service-fecru/admin/projects/{sourceProjectKey}/move-reviews/{destinationProjectKey} | 
[**permissions**](DefaultApi.md#permissions) | **GET** /rest-service-fecru/admin/repositories/{repository}/permissions | 
[**permissionsGroups**](DefaultApi.md#permissionsGroups) | **GET** /rest-service-fecru/admin/repositories/{repository}/permissions/groups | 
[**rebuildSearchIndex**](DefaultApi.md#rebuildSearchIndex) | **POST** /rest-service-fecru/admin/repositories-v1/{repository}/reindex-search | 
[**reindexChangesetComments**](DefaultApi.md#reindexChangesetComments) | **POST** /rest-service-fecru/admin/repositories-v1/{repository}/reindex-discussions | 
[**reindexChangesetDiscussion**](DefaultApi.md#reindexChangesetDiscussion) | **PUT** /rest-service-fecru/admin/repositories/{repository}/reindex-changeset-discussion | 
[**reindexReviews**](DefaultApi.md#reindexReviews) | **PUT** /rest-service-fecru/admin/repositories/{repository}/reindex-reviews | 
[**reindexSearch**](DefaultApi.md#reindexSearch) | **PUT** /rest-service-fecru/admin/repositories/{repository}/reindex-search | 
[**removeGroupToPermissions**](DefaultApi.md#removeGroupToPermissions) | **DELETE** /rest-service-fecru/admin/repositories/{repository}/permissions/groups | 
[**repositoryUpdates**](DefaultApi.md#repositoryUpdates) | **GET** /rest-service-fecru/admin/repositories/{repository}/updates | 
[**restServiceFecruAdminGroupsGet**](DefaultApi.md#restServiceFecruAdminGroupsGet) | **GET** /rest-service-fecru/admin/groups/ | 
[**restServiceFecruAdminGroupsNameDelete**](DefaultApi.md#restServiceFecruAdminGroupsNameDelete) | **DELETE** /rest-service-fecru/admin/groups/{name} | 
[**restServiceFecruAdminGroupsNameGet**](DefaultApi.md#restServiceFecruAdminGroupsNameGet) | **GET** /rest-service-fecru/admin/groups/{name} | 
[**restServiceFecruAdminGroupsNamePut**](DefaultApi.md#restServiceFecruAdminGroupsNamePut) | **PUT** /rest-service-fecru/admin/groups/{name} | 
[**restServiceFecruAdminGroupsNameUsersDelete**](DefaultApi.md#restServiceFecruAdminGroupsNameUsersDelete) | **DELETE** /rest-service-fecru/admin/groups/{name}/users | 
[**restServiceFecruAdminGroupsNameUsersPut**](DefaultApi.md#restServiceFecruAdminGroupsNameUsersPut) | **PUT** /rest-service-fecru/admin/groups/{name}/users | 
[**restServiceFecruAdminGroupsPost**](DefaultApi.md#restServiceFecruAdminGroupsPost) | **POST** /rest-service-fecru/admin/groups/ | 
[**restServiceFecruAdminPermissionSchemesGet**](DefaultApi.md#restServiceFecruAdminPermissionSchemesGet) | **GET** /rest-service-fecru/admin/permission-schemes | 
[**restServiceFecruAdminPermissionSchemesNameDelete**](DefaultApi.md#restServiceFecruAdminPermissionSchemesNameDelete) | **DELETE** /rest-service-fecru/admin/permission-schemes/{name} | 
[**restServiceFecruAdminPermissionSchemesNameGet**](DefaultApi.md#restServiceFecruAdminPermissionSchemesNameGet) | **GET** /rest-service-fecru/admin/permission-schemes/{name} | 
[**restServiceFecruAdminPermissionSchemesNamePut**](DefaultApi.md#restServiceFecruAdminPermissionSchemesNamePut) | **PUT** /rest-service-fecru/admin/permission-schemes/{name} | 
[**restServiceFecruAdminPermissionSchemesPost**](DefaultApi.md#restServiceFecruAdminPermissionSchemesPost) | **POST** /rest-service-fecru/admin/permission-schemes | 
[**restServiceFecruAdminProjectsGet**](DefaultApi.md#restServiceFecruAdminProjectsGet) | **GET** /rest-service-fecru/admin/projects | 
[**restServiceFecruAdminProjectsKeyDelete**](DefaultApi.md#restServiceFecruAdminProjectsKeyDelete) | **DELETE** /rest-service-fecru/admin/projects/{key} | 
[**restServiceFecruAdminProjectsKeyGet**](DefaultApi.md#restServiceFecruAdminProjectsKeyGet) | **GET** /rest-service-fecru/admin/projects/{key} | 
[**restServiceFecruAdminProjectsKeyPut**](DefaultApi.md#restServiceFecruAdminProjectsKeyPut) | **PUT** /rest-service-fecru/admin/projects/{key} | 
[**restServiceFecruAdminProjectsPost**](DefaultApi.md#restServiceFecruAdminProjectsPost) | **POST** /rest-service-fecru/admin/projects | 
[**restServiceFecruAdminRepositoriesGet**](DefaultApi.md#restServiceFecruAdminRepositoriesGet) | **GET** /rest-service-fecru/admin/repositories | 
[**restServiceFecruAdminRepositoriesPost**](DefaultApi.md#restServiceFecruAdminRepositoriesPost) | **POST** /rest-service-fecru/admin/repositories | 
[**restServiceFecruAdminRepositoriesRepositoryDelete**](DefaultApi.md#restServiceFecruAdminRepositoriesRepositoryDelete) | **DELETE** /rest-service-fecru/admin/repositories/{repository} | 
[**restServiceFecruAdminRepositoriesRepositoryGet**](DefaultApi.md#restServiceFecruAdminRepositoriesRepositoryGet) | **GET** /rest-service-fecru/admin/repositories/{repository} | 
[**restServiceFecruAdminRepositoriesRepositoryPut**](DefaultApi.md#restServiceFecruAdminRepositoriesRepositoryPut) | **PUT** /rest-service-fecru/admin/repositories/{repository} | 
[**restServiceFecruAdminRepositoriesRepositoryReindexLinecountPut**](DefaultApi.md#restServiceFecruAdminRepositoriesRepositoryReindexLinecountPut) | **PUT** /rest-service-fecru/admin/repositories/{repository}/reindex-linecount | 
[**restServiceFecruAdminRepositoriesRepositoryReindexSourcePut**](DefaultApi.md#restServiceFecruAdminRepositoriesRepositoryReindexSourcePut) | **PUT** /rest-service-fecru/admin/repositories/{repository}/reindex-source | 
[**restServiceFecruAdminRepositoriesRepositoryRescanMetadataPut**](DefaultApi.md#restServiceFecruAdminRepositoriesRepositoryRescanMetadataPut) | **PUT** /rest-service-fecru/admin/repositories/{repository}/rescan-metadata | 
[**restServiceFecruAdminRepositoriesV1RepositoryGet**](DefaultApi.md#restServiceFecruAdminRepositoriesV1RepositoryGet) | **GET** /rest-service-fecru/admin/repositories-v1/{repository} | 
[**restServiceFecruAdminRepositoriesV1RepositoryReindexLinecountPost**](DefaultApi.md#restServiceFecruAdminRepositoriesV1RepositoryReindexLinecountPost) | **POST** /rest-service-fecru/admin/repositories-v1/{repository}/reindex-linecount | 
[**restServiceFecruAdminRepositoriesV1RepositoryReindexSourcePost**](DefaultApi.md#restServiceFecruAdminRepositoriesV1RepositoryReindexSourcePost) | **POST** /rest-service-fecru/admin/repositories-v1/{repository}/reindex-source | 
[**restServiceFecruAdminRepositoriesV1RepositoryRescanMetadataPost**](DefaultApi.md#restServiceFecruAdminRepositoriesV1RepositoryRescanMetadataPost) | **POST** /rest-service-fecru/admin/repositories-v1/{repository}/rescan-metadata | 
[**restServiceFecruAdminUsersGet**](DefaultApi.md#restServiceFecruAdminUsersGet) | **GET** /rest-service-fecru/admin/users/ | 
[**restServiceFecruAdminUsersNameDelete**](DefaultApi.md#restServiceFecruAdminUsersNameDelete) | **DELETE** /rest-service-fecru/admin/users/{name} | 
[**restServiceFecruAdminUsersNameGet**](DefaultApi.md#restServiceFecruAdminUsersNameGet) | **GET** /rest-service-fecru/admin/users/{name} | 
[**restServiceFecruAdminUsersNameGroupsDelete**](DefaultApi.md#restServiceFecruAdminUsersNameGroupsDelete) | **DELETE** /rest-service-fecru/admin/users/{name}/groups | 
[**restServiceFecruAdminUsersNameGroupsPut**](DefaultApi.md#restServiceFecruAdminUsersNameGroupsPut) | **PUT** /rest-service-fecru/admin/users/{name}/groups | 
[**restServiceFecruAdminUsersNamePut**](DefaultApi.md#restServiceFecruAdminUsersNamePut) | **PUT** /rest-service-fecru/admin/users/{name} | 
[**restServiceFecruAdminUsersPost**](DefaultApi.md#restServiceFecruAdminUsersPost) | **POST** /rest-service-fecru/admin/users/ | 
[**restServiceFecruIndexingStatusV1StatusRepositoryGet**](DefaultApi.md#restServiceFecruIndexingStatusV1StatusRepositoryGet) | **GET** /rest-service-fecru/indexing-status-v1/status/{repository} | 
[**scan**](DefaultApi.md#scan) | **POST** /rest-service-fecru/admin/repositories-v1/{repository}/scan | 
[**scanCvs**](DefaultApi.md#scanCvs) | **POST** /rest-service-fecru/admin/repositories-v1/{repository}/scan-cvs | 
[**setPref**](DefaultApi.md#setPref) | **POST** /rest-service-fecru/user-prefs-v1 | 
[**start**](DefaultApi.md#start) | **PUT** /rest-service-fecru/admin/repositories/{repository}/start | 
[**startRepository**](DefaultApi.md#startRepository) | **POST** /rest-service-fecru/admin/repositories-v1/{repository}/start | 
[**stop**](DefaultApi.md#stop) | **PUT** /rest-service-fecru/admin/repositories/{repository}/stop | 
[**stopRepository**](DefaultApi.md#stopRepository) | **POST** /rest-service-fecru/admin/repositories-v1/{repository}/stop | 
[**updateDefaultPermissions**](DefaultApi.md#updateDefaultPermissions) | **PUT** /rest-service-fecru/admin/repositories/~defaults/permissions | 
[**updatePermissions**](DefaultApi.md#updatePermissions) | **PUT** /rest-service-fecru/admin/repositories/{repository}/permissions | 
[**updateRepositoryUpdates**](DefaultApi.md#updateRepositoryUpdates) | **PUT** /rest-service-fecru/admin/repositories/{repository}/updates | 



## addAllowedReviewerGroup

> addAllowedReviewerGroup(key)



Add group to project&#39;s allowed reviewer group list

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let key = "key_example"; // String | project key
apiInstance.addAllowedReviewerGroup(key, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **String**| project key | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addAllowedReviewerUser

> addAllowedReviewerUser(key)



Add user to project&#39;s allowed reviewer users list

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let key = "key_example"; // String | project key
apiInstance.addAllowedReviewerUser(key, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **String**| project key | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addDefaultReviewerGroup

> addDefaultReviewerGroup(key)



Add group to project&#39;s default reviewer group list

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let key = "key_example"; // String | project key
apiInstance.addDefaultReviewerGroup(key, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **String**| project key | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addDefaultReviewerUser

> addDefaultReviewerUser(key)



Add user to project&#39;s default reviewer users list

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let key = "key_example"; // String | project key
apiInstance.addDefaultReviewerUser(key, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **String**| project key | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addGroupToPermissions

> addGroupToPermissions(repository)



Note: use /rest-service-fecru/admin/repository-permissions/ endpoint for full repository permission administration functionality  Adds group to repository allowed groups

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository
apiInstance.addGroupToPermissions(repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addPermissionSchemeAnonymousUsers

> addPermissionSchemeAnonymousUsers(name)



Add anonymous-user permission [action name] to given permission scheme  List of available action names:

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let name = "name_example"; // String | permission scheme name
apiInstance.addPermissionSchemeAnonymousUsers(name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| permission scheme name | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addPermissionSchemeGroup

> addPermissionSchemeGroup(name)



Add group permission [group name, action name] to given permission scheme  List of available action names:

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let name = "name_example"; // String | permission scheme name
apiInstance.addPermissionSchemeGroup(name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| permission scheme name | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addPermissionSchemeLoggedUsers

> addPermissionSchemeLoggedUsers(name)



Add logged-in-users permission [action name] to given permission scheme  List of available action names:

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let name = "name_example"; // String | permission scheme name
apiInstance.addPermissionSchemeLoggedUsers(name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| permission scheme name | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addPermissionSchemeReviewRole

> addPermissionSchemeReviewRole(name)



Add review-role permission [role name, action name] to given permission scheme  List of available action names:     List of available role names:

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let name = "name_example"; // String | permission scheme name
apiInstance.addPermissionSchemeReviewRole(name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| permission scheme name | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addPermissionSchemeUser

> addPermissionSchemeUser(name)



Add user permission [username, action name] to given permission scheme  List of available action names:

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let name = "name_example"; // String | permission scheme name
apiInstance.addPermissionSchemeUser(name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| permission scheme name | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addRepository

> addRepository()



Adds repository

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
apiInstance.addRepository((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## allowedReviewerGroups

> allowedReviewerGroups(key)



Retrieves project&#39;s allowed reviewer groups

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let key = "key_example"; // String | project key
apiInstance.allowedReviewerGroups(key, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **String**| project key | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## allowedReviewerUsers

> allowedReviewerUsers(key)



Retrieves project&#39;s allowed reviewer users

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let key = "key_example"; // String | project key
apiInstance.allowedReviewerUsers(key, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **String**| project key | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## defaultPermissions

> defaultPermissions()



Retrieve default repository permissions properties.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
apiInstance.defaultPermissions((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## defaultReviewerGroups

> defaultReviewerGroups(key)



Retrieves project&#39;s default reviewer groups

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let key = "key_example"; // String | project key
apiInstance.defaultReviewerGroups(key, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **String**| project key | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteAllowedReviewerGroup

> deleteAllowedReviewerGroup(key)



Delete group from project&#39;s allowed reviewer group list

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let key = "key_example"; // String | project key
apiInstance.deleteAllowedReviewerGroup(key, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **String**| project key | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteAllowedReviewerUser

> deleteAllowedReviewerUser(key)



Remove user from project&#39;s allowed reviewer users list

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let key = "key_example"; // String | project key
apiInstance.deleteAllowedReviewerUser(key, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **String**| project key | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteDefaultReviewerGroup

> deleteDefaultReviewerGroup(key)



Delete group from project&#39;s default reviewer group list

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let key = "key_example"; // String | project key
apiInstance.deleteDefaultReviewerGroup(key, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **String**| project key | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteDefaultReviewerUser

> deleteDefaultReviewerUser(key)



Remove user from project&#39;s default reviewer users list

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let key = "key_example"; // String | project key
apiInstance.deleteDefaultReviewerUser(key, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **String**| project key | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deletePermissionSchemeAnonymousUsers

> deletePermissionSchemeAnonymousUsers(name)



Removes anonymous-user permission [action name] from given permission scheme

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let name = "name_example"; // String | permission scheme name
apiInstance.deletePermissionSchemeAnonymousUsers(name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| permission scheme name | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deletePermissionSchemeGroup

> deletePermissionSchemeGroup(name)



Removes group permission [group name, action name] from given permission scheme

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let name = "name_example"; // String | permission scheme name
apiInstance.deletePermissionSchemeGroup(name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| permission scheme name | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deletePermissionSchemeLoggedUsers

> deletePermissionSchemeLoggedUsers(name)



Removes logged-in-users permission [action name] from given permission scheme

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let name = "name_example"; // String | permission scheme name
apiInstance.deletePermissionSchemeLoggedUsers(name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| permission scheme name | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deletePermissionSchemeRole

> deletePermissionSchemeRole(name)



Removes review-role permission [role name, action name] from given permission scheme

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let name = "name_example"; // String | permission scheme name
apiInstance.deletePermissionSchemeRole(name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| permission scheme name | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deletePermissionSchemeUser

> deletePermissionSchemeUser(name)



Removes user permission [username, action name] from given permission scheme

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let name = "name_example"; // String | permission scheme name
apiInstance.deletePermissionSchemeUser(name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| permission scheme name | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteRepository

> deleteRepository(repository)



Deletes repository.  Warning: you can not undo this operation

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository to delete
apiInstance.deleteRepository(repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository to delete | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## disableRepository

> disableRepository(repository)



Disables repository.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository to disable
apiInstance.disableRepository(repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository to disable | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## doReviewRevisionReindex

> doReviewRevisionReindex(repository, opts)



Re-indexes all the Crucible revision data (which revisions have been reviewed)

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository to reindex
let opts = {
  'synchronous': false // Boolean | if true will wait for the indexing to finish before returning
};
apiInstance.doReviewRevisionReindex(repository, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository to reindex | 
 **synchronous** | **Boolean**| if true will wait for the indexing to finish before returning | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## doShareContent

> doShareContent()



### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
apiInstance.doShareContent((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## enableRepository

> enableRepository(repository)



Enables repository.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository to enable
apiInstance.enableRepository(repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository to enable | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fullIncrementalIndex

> fullIncrementalIndex(repository)



Runs an full incremental repository index.  For CVS: scans the whole CVS repository for any changes since the last scan.  For other repository types will trigger an incremental index.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository to scan
apiInstance.fullIncrementalIndex(repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository to scan | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getGlobalPref

> getGlobalPref(property)



Getting user&#39;s global preference

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let property = "property_example"; // String | the property(preference) name
apiInstance.getGlobalPref(property, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property** | **String**| the property(preference) name | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getInfo

> getInfo()



Provides general information about the server&#39;s configuration.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
apiInstance.getInfo((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getRecent

> getRecent()



Get a list of recently visited items for the currently logged in user.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
apiInstance.getRecent((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getRecentDetailed

> getRecentDetailed()



Get a list of recently visisted items for the currently logged in user, including the detailed entities.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
apiInstance.getRecentDetailed((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getRecentProjects

> getRecentProjects()



Get a list of recently visited projects for the currently logged in user.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
apiInstance.getRecentProjects((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getRecentProjectsDetailed

> getRecentProjectsDetailed()



Get a list of recently visited projects for the currently logged in Project, including the detailed entities.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
apiInstance.getRecentProjectsDetailed((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getRecentRepositories

> getRecentRepositories()



Get a list of recently visited repositories for the currently logged in user.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
apiInstance.getRecentRepositories((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getRecentRepositoriesDetailed

> getRecentRepositoriesDetailed()



Get a list of recently visisted repositories for the currently logged in user, including the detailed entities.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
apiInstance.getRecentRepositoriesDetailed((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getRecentReviews

> getRecentReviews()



Get a list of recently visited reviews for the currently logged in user.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
apiInstance.getRecentReviews((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getRecentReviewsDetailed

> getRecentReviewsDetailed()



Get a list of recently visited reviews for the currently logged in user, including the detailed entities.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
apiInstance.getRecentReviewsDetailed((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getRecentSnippets

> getRecentSnippets()



Get a list of recently visited snippets for the currently logged in user.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
apiInstance.getRecentSnippets((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getRecentSnippetsDetailed

> getRecentSnippetsDetailed()



Get a list of recently visited snippets for the currently logged in user, including the detailed entities.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
apiInstance.getRecentSnippetsDetailed((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getRecentUsers

> getRecentUsers()



Get a list of recently visited users for the currently logged in user.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
apiInstance.getRecentUsers((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getRecentUsersDetailed

> getRecentUsersDetailed()



Get a list of recently visited users for the currently logged in user, including the detailed entities.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
apiInstance.getRecentUsersDetailed((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## getRepoPref

> getRepoPref(property, repository)



Getting user&#39;s preference related to a certain repository

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let property = "property_example"; // String | the property(preference) name
let repository = "repository_example"; // String | the key of the repository
apiInstance.getRepoPref(property, repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **property** | **String**| the property(preference) name | 
 **repository** | **String**| the key of the repository | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## incrementalIndex

> incrementalIndex(repository, opts)



Runs an incremental repository index.  This is the same operation as triggered by scheduled indexing.  Can be called using the REST API Token to authorize.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository to stop
let opts = {
  'wait': false // Boolean | if true will wait for the indexing to finish before returning
};
apiInstance.incrementalIndex(repository, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository to stop | 
 **wait** | **Boolean**| if true will wait for the indexing to finish before returning | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listAnonymousUsersPrincipalAssociation

> listAnonymousUsersPrincipalAssociation(name, opts)



Retrieve a page of anonymous users permissions [action name] for given permission scheme.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let name = "name_example"; // String | permission scheme name
let opts = {
  'action': "action_example" // String | action name
};
apiInstance.listAnonymousUsersPrincipalAssociation(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| permission scheme name | 
 **action** | **String**| action name | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listDefaultReviewerUsers

> listDefaultReviewerUsers(key)



Retrieves project&#39;s default reviewer users

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let key = "key_example"; // String | project key
apiInstance.listDefaultReviewerUsers(key, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **String**| project key | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listGroupPrincipalAssociation

> listGroupPrincipalAssociation(name, opts)



Retrieve a page of group permissions [group name, action name] for given permission scheme.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let name = "name_example"; // String | permission scheme name
let opts = {
  'name2': "name_example", // String | group name
  'action': "action_example" // String | action name
};
apiInstance.listGroupPrincipalAssociation(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| permission scheme name | 
 **name2** | **String**| group name | [optional] 
 **action** | **String**| action name | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listGroupUsers

> listGroupUsers(name)



Lists group&#39;s user names

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let name = "name_example"; // String | group name
apiInstance.listGroupUsers(name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| group name | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listLoggedUsersPrincipalAssociation

> listLoggedUsersPrincipalAssociation(name, opts)



Retrieve a page of logged in users permissions [action name] for given permission scheme.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let name = "name_example"; // String | permission scheme name
let opts = {
  'action': "action_example" // String | action name
};
apiInstance.listLoggedUsersPrincipalAssociation(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| permission scheme name | 
 **action** | **String**| action name | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listProjects

> listProjects(name)



Retrieve a page of projects for given permission scheme.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let name = "name_example"; // String | permission scheme name
apiInstance.listProjects(name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| permission scheme name | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listRolesPrincipalAssociation

> listRolesPrincipalAssociation(name, opts)



Retrieve a page of review-roles permissions [role name, action name] for given permission scheme.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let name = "name_example"; // String | permission scheme name
let opts = {
  'name2': "name_example", // String | role name
  'action': "action_example" // String | action name
};
apiInstance.listRolesPrincipalAssociation(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| permission scheme name | 
 **name2** | **String**| role name | [optional] 
 **action** | **String**| action name | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listUserGroups

> listUserGroups(name)



Lists user&#39;s group names

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let name = "name_example"; // String | user name
apiInstance.listUserGroups(name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| user name | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listUserPrincipalAssociation

> listUserPrincipalAssociation(name, opts)



Retrieve a page of user permissions [username, action name] for given permission scheme.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let name = "name_example"; // String | permission scheme name
let opts = {
  'name2': "name_example", // String | permission scheme name
  'action': "action_example" // String | action name
};
apiInstance.listUserPrincipalAssociation(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| permission scheme name | 
 **name2** | **String**| permission scheme name | [optional] 
 **action** | **String**| action name | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## login

> login()



Get the user authentication token.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
apiInstance.login((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## moveAllReviews

> moveAllReviews(sourceProjectKey, destinationProjectKey)



Move reviews and snippets from source project to destination project

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let sourceProjectKey = "sourceProjectKey_example"; // String | project key of reviews and snippets source project
let destinationProjectKey = "destinationProjectKey_example"; // String | project key of reviews and snippets destination project
apiInstance.moveAllReviews(sourceProjectKey, destinationProjectKey, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sourceProjectKey** | **String**| project key of reviews and snippets source project | 
 **destinationProjectKey** | **String**| project key of reviews and snippets destination project | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## permissions

> permissions(repository)



Retrieve repository permissions properties.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository
apiInstance.permissions(repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## permissionsGroups

> permissionsGroups(repository)



Note: use /rest-service-fecru/admin/repository-permissions/ endpoint for full repository permission administration functionality  Lists groups allowed to access repository.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository
apiInstance.permissionsGroups(repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## rebuildSearchIndex

> rebuildSearchIndex(repository)



Rebuilds the search index data for the given repository. This will rebuild the data used to search by path,  commit message and comitter, also used for activity streams and JIRA integration.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository to re-index.
apiInstance.rebuildSearchIndex(repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository to re-index. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## reindexChangesetComments

> reindexChangesetComments(repository)



Rebuilds the changeset discussion index for the specified repository. The index is used to display changeset  discussions in activity streams.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository to perform the operation for
apiInstance.reindexChangesetComments(repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository to perform the operation for | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## reindexChangesetDiscussion

> reindexChangesetDiscussion(repository)



Rebuilds the changeset discussion index for the specified repository. The index is used to display changeset  discussions in activity streams.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository to perform the operation for
apiInstance.reindexChangesetDiscussion(repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository to perform the operation for | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## reindexReviews

> reindexReviews(repository)



Re-indexes all the Crucible revision data (which revisions have been reviewed)

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository to reindex
apiInstance.reindexReviews(repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository to reindex | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## reindexSearch

> reindexSearch(repository)



Rebuilds the search index data for the given repository. This will rebuild the data used to search by path,  commit message and committer, also used for activity streams and JIRA integration.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository to re-index.
apiInstance.reindexSearch(repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository to re-index. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## removeGroupToPermissions

> removeGroupToPermissions(repository)



Delete group from repository allowed groups

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository
apiInstance.removeGroupToPermissions(repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## repositoryUpdates

> repositoryUpdates(repository)



Retrieves repository updates properties.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | repository key
apiInstance.repositoryUpdates(repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| repository key | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## restServiceFecruAdminGroupsGet

> restServiceFecruAdminGroupsGet(opts)



Retrieve a page of groups.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let opts = {
  'prefix': "prefix_example" // String | filter groups by name prefix
};
apiInstance.restServiceFecruAdminGroupsGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **String**| filter groups by name prefix | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## restServiceFecruAdminGroupsNameDelete

> restServiceFecruAdminGroupsNameDelete(name)



Deletes a group by name

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let name = "name_example"; // String | group name
apiInstance.restServiceFecruAdminGroupsNameDelete(name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| group name | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## restServiceFecruAdminGroupsNameGet

> restServiceFecruAdminGroupsNameGet(name)



Retrieve a group by name.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let name = "name_example"; // String | group name
apiInstance.restServiceFecruAdminGroupsNameGet(name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| group name | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## restServiceFecruAdminGroupsNamePut

> restServiceFecruAdminGroupsNamePut(name)



Updates an existing group.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let name = "name_example"; // String | group name
apiInstance.restServiceFecruAdminGroupsNamePut(name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| group name | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## restServiceFecruAdminGroupsNameUsersDelete

> restServiceFecruAdminGroupsNameUsersDelete(name)



Removes user from group

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let name = "name_example"; // String | group name
apiInstance.restServiceFecruAdminGroupsNameUsersDelete(name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| group name | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## restServiceFecruAdminGroupsNameUsersPut

> restServiceFecruAdminGroupsNameUsersPut(name)



Adds user to group

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let name = "name_example"; // String | group name
apiInstance.restServiceFecruAdminGroupsNameUsersPut(name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| group name | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## restServiceFecruAdminGroupsPost

> restServiceFecruAdminGroupsPost()



Creates a new user group.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
apiInstance.restServiceFecruAdminGroupsPost((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## restServiceFecruAdminPermissionSchemesGet

> restServiceFecruAdminPermissionSchemesGet(opts)



Retrieve a page of permission schemes.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let opts = {
  'name': "name_example" // String | permission scheme name part filter, case insensitive, optional
};
apiInstance.restServiceFecruAdminPermissionSchemesGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| permission scheme name part filter, case insensitive, optional | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## restServiceFecruAdminPermissionSchemesNameDelete

> restServiceFecruAdminPermissionSchemesNameDelete(name)



Deletes a permission scheme by name

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let name = "name_example"; // String | permission scheme name
apiInstance.restServiceFecruAdminPermissionSchemesNameDelete(name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| permission scheme name | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## restServiceFecruAdminPermissionSchemesNameGet

> restServiceFecruAdminPermissionSchemesNameGet(name)



Retrieve a permission scheme by name

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let name = "name_example"; // String | permission scheme name
apiInstance.restServiceFecruAdminPermissionSchemesNameGet(name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| permission scheme name | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## restServiceFecruAdminPermissionSchemesNamePut

> restServiceFecruAdminPermissionSchemesNamePut(name)



Updates an existing permission scheme.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let name = "name_example"; // String | permission scheme name
apiInstance.restServiceFecruAdminPermissionSchemesNamePut(name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| permission scheme name | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## restServiceFecruAdminPermissionSchemesPost

> restServiceFecruAdminPermissionSchemesPost(opts)



Creates a new permission scheme. The new permission scheme is blank or can be created from another existing permission scheme.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let opts = {
  'copyFrom': "copyFrom_example" // String | if set, the new permission scheme will be a copy of permissionSchemeName
};
apiInstance.restServiceFecruAdminPermissionSchemesPost(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **copyFrom** | **String**| if set, the new permission scheme will be a copy of permissionSchemeName | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## restServiceFecruAdminProjectsGet

> restServiceFecruAdminProjectsGet(opts)



Retrieve a page of projects.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let opts = {
  'name': "name_example", // String | project's name part filter, optional
  'key': "key_example", // String | project's key part filter, optional
  'defaultRepositoryName': "defaultRepositoryName_example", // String | project's default repository key part filter, optional
  'permissionSchemeName': "permissionSchemeName_example" // String | project's permission scheme pare name filter, optional
};
apiInstance.restServiceFecruAdminProjectsGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| project&#39;s name part filter, optional | [optional] 
 **key** | **String**| project&#39;s key part filter, optional | [optional] 
 **defaultRepositoryName** | **String**| project&#39;s default repository key part filter, optional | [optional] 
 **permissionSchemeName** | **String**| project&#39;s permission scheme pare name filter, optional | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## restServiceFecruAdminProjectsKeyDelete

> restServiceFecruAdminProjectsKeyDelete(key, opts)



Deletes a project by key (including all reviews in this project).  Use   to move reviews to another project.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let key = "key_example"; // String | project key
let opts = {
  'deleteProjectReviews': false // Boolean | if true deletes reviews in project
};
apiInstance.restServiceFecruAdminProjectsKeyDelete(key, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **String**| project key | 
 **deleteProjectReviews** | **Boolean**| if true deletes reviews in project | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## restServiceFecruAdminProjectsKeyGet

> restServiceFecruAdminProjectsKeyGet(key)



Retrieve a project by key.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let key = "key_example"; // String | project key
apiInstance.restServiceFecruAdminProjectsKeyGet(key, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **String**| project key | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## restServiceFecruAdminProjectsKeyPut

> restServiceFecruAdminProjectsKeyPut(key)



Updates an existing project.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let key = "key_example"; // String | project key
apiInstance.restServiceFecruAdminProjectsKeyPut(key, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **String**| project key | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## restServiceFecruAdminProjectsPost

> restServiceFecruAdminProjectsPost()



Creates a new project.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
apiInstance.restServiceFecruAdminProjectsPost((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## restServiceFecruAdminRepositoriesGet

> restServiceFecruAdminRepositoriesGet(opts)



Retrieve a page of repositories. Repository properties with default values may not be returned.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let opts = {
  'type': "type_example", // String | filter repositories by repository type: svn, git, hg, cvs, p4, ...
  'enabled': true, // Boolean | filter repositories by enabled flag
  'started': true // Boolean | filter repositories by started flag
};
apiInstance.restServiceFecruAdminRepositoriesGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **String**| filter repositories by repository type: svn, git, hg, cvs, p4, ... | [optional] 
 **enabled** | **Boolean**| filter repositories by enabled flag | [optional] 
 **started** | **Boolean**| filter repositories by started flag | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## restServiceFecruAdminRepositoriesPost

> restServiceFecruAdminRepositoriesPost()



Creates a repository.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
apiInstance.restServiceFecruAdminRepositoriesPost((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## restServiceFecruAdminRepositoriesRepositoryDelete

> restServiceFecruAdminRepositoriesRepositoryDelete(repository)



Deletes a repository by key

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository
apiInstance.restServiceFecruAdminRepositoriesRepositoryDelete(repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## restServiceFecruAdminRepositoriesRepositoryGet

> restServiceFecruAdminRepositoriesRepositoryGet(repository)



Retrieve a repository by key. Repository properties with default values may not be returned.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository
apiInstance.restServiceFecruAdminRepositoriesRepositoryGet(repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## restServiceFecruAdminRepositoriesRepositoryPut

> restServiceFecruAdminRepositoriesRepositoryPut(repository)



Updates an existing repository.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository
apiInstance.restServiceFecruAdminRepositoriesRepositoryPut(repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## restServiceFecruAdminRepositoriesRepositoryReindexLinecountPut

> restServiceFecruAdminRepositoriesRepositoryReindexLinecountPut(repository)



Re-indexes the linecount data used to generate the LOC graphs. The linecount data will be recalculated in daily  buckets based on the server timezone.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository to re-index
apiInstance.restServiceFecruAdminRepositoriesRepositoryReindexLinecountPut(repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository to re-index | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## restServiceFecruAdminRepositoriesRepositoryReindexSourcePut

> restServiceFecruAdminRepositoriesRepositoryReindexSourcePut(repository, opts)



Deletes the existing cache and re-indexes the repository from scratch.  For large or slow repositories this may take some time, during which some functionality will be unavailable.  This action will also restart the repository.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository to reindex
let opts = {
  'clone': false // Boolean | if true and the repository is a dvcs repository (git or mercurial) it will re-clone the repository before re-indexing
};
apiInstance.restServiceFecruAdminRepositoriesRepositoryReindexSourcePut(repository, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository to reindex | 
 **clone** | **Boolean**| if true and the repository is a dvcs repository (git or mercurial) it will re-clone the repository before re-indexing | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## restServiceFecruAdminRepositoriesRepositoryRescanMetadataPut

> restServiceFecruAdminRepositoriesRepositoryRescanMetadataPut(repository, opts)



Re-scans the repository metadata. Only valid for Perforce and SVN repositories.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository to re-scan
let opts = {
  'from': "from_example", // String | the revision number to start at
  'to': "to_example" // String | the revision number to end at
};
apiInstance.restServiceFecruAdminRepositoriesRepositoryRescanMetadataPut(repository, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository to re-scan | 
 **from** | **String**| the revision number to start at | [optional] 
 **to** | **String**| the revision number to end at | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## restServiceFecruAdminRepositoriesV1RepositoryGet

> restServiceFecruAdminRepositoriesV1RepositoryGet(repository)



Returns information about the status of the repository and the current indexing status

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository
apiInstance.restServiceFecruAdminRepositoriesV1RepositoryGet(repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## restServiceFecruAdminRepositoriesV1RepositoryReindexLinecountPost

> restServiceFecruAdminRepositoriesV1RepositoryReindexLinecountPost(repository)



Re-indexes the linecount data used to generate the LOC graphs. The linecount data will be recalculated in daily  buckets based on the server timezone.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository to re-index
apiInstance.restServiceFecruAdminRepositoriesV1RepositoryReindexLinecountPost(repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository to re-index | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## restServiceFecruAdminRepositoriesV1RepositoryReindexSourcePost

> restServiceFecruAdminRepositoriesV1RepositoryReindexSourcePost(repository, opts)



Deletes the existing cache and re-indexes the repository from scratch.  For large or slow repositories this may take some time, during which some functionality will be unavailable.  This action will also restart the repository.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository to reindex
let opts = {
  'clone': false // Boolean | if true and the repository is a dvcs repository (git or mercurial) it will re-clone the repository  before re-indexing
};
apiInstance.restServiceFecruAdminRepositoriesV1RepositoryReindexSourcePost(repository, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository to reindex | 
 **clone** | **Boolean**| if true and the repository is a dvcs repository (git or mercurial) it will re-clone the repository  before re-indexing | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## restServiceFecruAdminRepositoriesV1RepositoryRescanMetadataPost

> restServiceFecruAdminRepositoriesV1RepositoryRescanMetadataPost(repository, opts)



Re-scans the repository metadata for SVN and Perforce repositories. Only valid for Perforce and SVN repositories.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository to re-scan
let opts = {
  'from': 789, // Number | the revision number to start at
  'to': 789 // Number | the revision number to end at
};
apiInstance.restServiceFecruAdminRepositoriesV1RepositoryRescanMetadataPost(repository, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository to re-scan | 
 **from** | **Number**| the revision number to start at | [optional] 
 **to** | **Number**| the revision number to end at | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## restServiceFecruAdminUsersGet

> restServiceFecruAdminUsersGet()



Retrieve a page of users.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
apiInstance.restServiceFecruAdminUsersGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## restServiceFecruAdminUsersNameDelete

> restServiceFecruAdminUsersNameDelete(name)



Deletes a user by name

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let name = "name_example"; // String | user name
apiInstance.restServiceFecruAdminUsersNameDelete(name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| user name | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## restServiceFecruAdminUsersNameGet

> restServiceFecruAdminUsersNameGet(name)



Retrieve a user by name.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let name = "name_example"; // String | user name
apiInstance.restServiceFecruAdminUsersNameGet(name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| user name | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## restServiceFecruAdminUsersNameGroupsDelete

> restServiceFecruAdminUsersNameGroupsDelete(name)



Removes user from group

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let name = "name_example"; // String | user name
apiInstance.restServiceFecruAdminUsersNameGroupsDelete(name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| user name | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## restServiceFecruAdminUsersNameGroupsPut

> restServiceFecruAdminUsersNameGroupsPut(name)



Adds user to group

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let name = "name_example"; // String | user name
apiInstance.restServiceFecruAdminUsersNameGroupsPut(name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| user name | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## restServiceFecruAdminUsersNamePut

> restServiceFecruAdminUsersNamePut(name)



Updates an existing user.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let name = "name_example"; // String | user name
apiInstance.restServiceFecruAdminUsersNamePut(name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| user name | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## restServiceFecruAdminUsersPost

> restServiceFecruAdminUsersPost()



Creates a new user. Tries to add the user to fisheye-users and crucible-users groups if those exist.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
apiInstance.restServiceFecruAdminUsersPost((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## restServiceFecruIndexingStatusV1StatusRepositoryGet

> restServiceFecruIndexingStatusV1StatusRepositoryGet(repository)



Returns indexing status of given repository.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository to get status of
apiInstance.restServiceFecruIndexingStatusV1StatusRepositoryGet(repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository to get status of | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## scan

> scan(repository, opts)



Runs an incremental repository index now.  This is the same operation as triggered by scheduled indexing.  Can be called using the REST Api Token to authorize.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository to run scan for
let opts = {
  'synchronous': false // Boolean | if true will wait for the indexing to finish before returning
};
apiInstance.scan(repository, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository to run scan for | 
 **synchronous** | **Boolean**| if true will wait for the indexing to finish before returning | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## scanCvs

> scanCvs(repository)



Scans the whole CVS repository for any changes since the last scan. Only valid for CVS repositories.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository to scan
apiInstance.scanCvs(repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository to scan | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## setPref

> setPref()



Using POST method to set a user preference.  If repo is not set, the preference will be recognised as a global preference.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
apiInstance.setPref((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## start

> start(repository)



Starts repository. Does not wait for the repository to start before returning.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository to start
apiInstance.start(repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository to start | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## startRepository

> startRepository(repository)



Starts the repository.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository to start
apiInstance.startRepository(repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository to start | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## stop

> stop(repository)



Stops repository. Does not wait for the repository to stop before returning.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository to stop
apiInstance.stop(repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository to stop | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## stopRepository

> stopRepository(repository)



Stops the repository. Does not wait for the repository to stop before returning.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository to stop
apiInstance.stopRepository(repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository to stop | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateDefaultPermissions

> updateDefaultPermissions()



Updates default repository permissions properties.   Valid permission settings: any combination of allowAnonymous, allowLoggedIn

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
apiInstance.updateDefaultPermissions((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
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


## updatePermissions

> updatePermissions(repository)



Updates repository permissions properties.   Valid permission settings: any combination of useDefaults, allowAnonymous, allowLoggedIn.

### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | the key of the repository
apiInstance.updatePermissions(repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| the key of the repository | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## updateRepositoryUpdates

> updateRepositoryUpdates(repository)



### Example

```javascript
import FisheyeCrucible from 'fisheye_crucible';

let apiInstance = new FisheyeCrucible.DefaultApi();
let repository = "repository_example"; // String | repository key
apiInstance.updateRepositoryUpdates(repository, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **String**| repository key | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

