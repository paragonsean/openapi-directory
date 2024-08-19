# GitHubV3RestApi.MigrationsApi

All URIs are relative to *https://github.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**migrationsDeleteArchiveForOrg**](MigrationsApi.md#migrationsDeleteArchiveForOrg) | **DELETE** /orgs/{org}/migrations/{migration_id}/archive | Delete an organization migration archive
[**migrationsDownloadArchiveForOrg**](MigrationsApi.md#migrationsDownloadArchiveForOrg) | **GET** /orgs/{org}/migrations/{migration_id}/archive | Download an organization migration archive
[**migrationsGetArchiveForAuthenticatedUser**](MigrationsApi.md#migrationsGetArchiveForAuthenticatedUser) | **GET** /user/migrations/{migration_id}/archive | Download a user migration archive
[**migrationsGetStatusForOrg**](MigrationsApi.md#migrationsGetStatusForOrg) | **GET** /orgs/{org}/migrations/{migration_id} | Get an organization migration status
[**migrationsListForAuthenticatedUser**](MigrationsApi.md#migrationsListForAuthenticatedUser) | **GET** /user/migrations | List user migrations
[**migrationsListForOrg**](MigrationsApi.md#migrationsListForOrg) | **GET** /orgs/{org}/migrations | List organization migrations
[**migrationsListReposForAuthenticatedUser**](MigrationsApi.md#migrationsListReposForAuthenticatedUser) | **GET** /user/migrations/{migration_id}/repositories | List repositories for a user migration
[**migrationsListReposForOrg**](MigrationsApi.md#migrationsListReposForOrg) | **GET** /orgs/{org}/migrations/{migration_id}/repositories | List repositories in an organization migration
[**migrationsStartForAuthenticatedUser**](MigrationsApi.md#migrationsStartForAuthenticatedUser) | **POST** /user/migrations | Start a user migration
[**migrationsStartForOrg**](MigrationsApi.md#migrationsStartForOrg) | **POST** /orgs/{org}/migrations | Start an organization migration
[**migrationsUnlockRepoForOrg**](MigrationsApi.md#migrationsUnlockRepoForOrg) | **DELETE** /orgs/{org}/migrations/{migration_id}/repos/{repo_name}/lock | Unlock an organization repository



## migrationsDeleteArchiveForOrg

> migrationsDeleteArchiveForOrg(org, migrationId)

Delete an organization migration archive

Deletes a previous migration archive. Migration archives are automatically deleted after seven days.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.MigrationsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let migrationId = 56; // Number | The unique identifier of the migration.
apiInstance.migrationsDeleteArchiveForOrg(org, migrationId, (error, data, response) => {
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
 **org** | **String**| The organization name. The name is not case sensitive. | 
 **migrationId** | **Number**| The unique identifier of the migration. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## migrationsDownloadArchiveForOrg

> migrationsDownloadArchiveForOrg(org, migrationId)

Download an organization migration archive

Fetches the URL to a migration archive.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.MigrationsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let migrationId = 56; // Number | The unique identifier of the migration.
apiInstance.migrationsDownloadArchiveForOrg(org, migrationId, (error, data, response) => {
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
 **org** | **String**| The organization name. The name is not case sensitive. | 
 **migrationId** | **Number**| The unique identifier of the migration. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## migrationsGetArchiveForAuthenticatedUser

> migrationsGetArchiveForAuthenticatedUser(migrationId)

Download a user migration archive

Fetches the URL to download the migration archive as a &#x60;tar.gz&#x60; file. Depending on the resources your repository uses, the migration archive can contain JSON files with data for these objects:  *   attachments *   bases *   commit\\_comments *   issue\\_comments *   issue\\_events *   issues *   milestones *   organizations *   projects *   protected\\_branches *   pull\\_request\\_reviews *   pull\\_requests *   releases *   repositories *   review\\_comments *   schema *   users  The archive will also contain an &#x60;attachments&#x60; directory that includes all attachment files uploaded to GitHub.com and a &#x60;repositories&#x60; directory that contains the repository&#39;s Git data.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.MigrationsApi();
let migrationId = 56; // Number | The unique identifier of the migration.
apiInstance.migrationsGetArchiveForAuthenticatedUser(migrationId, (error, data, response) => {
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
 **migrationId** | **Number**| The unique identifier of the migration. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## migrationsGetStatusForOrg

> Migration migrationsGetStatusForOrg(org, migrationId, opts)

Get an organization migration status

Fetches the status of a migration.  The &#x60;state&#x60; of a migration can be one of the following values:  *   &#x60;pending&#x60;, which means the migration hasn&#39;t started yet. *   &#x60;exporting&#x60;, which means the migration is in progress. *   &#x60;exported&#x60;, which means the migration finished successfully. *   &#x60;failed&#x60;, which means the migration failed.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.MigrationsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let migrationId = 56; // Number | The unique identifier of the migration.
let opts = {
  'exclude': ["repositories"] // [String] | Exclude attributes from the API response to improve performance
};
apiInstance.migrationsGetStatusForOrg(org, migrationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**| The organization name. The name is not case sensitive. | 
 **migrationId** | **Number**| The unique identifier of the migration. | 
 **exclude** | [**[String]**](String.md)| Exclude attributes from the API response to improve performance | [optional] 

### Return type

[**Migration**](Migration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## migrationsListForAuthenticatedUser

> [Migration] migrationsListForAuthenticatedUser(opts)

List user migrations

Lists all migrations a user has started.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.MigrationsApi();
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.migrationsListForAuthenticatedUser(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[Migration]**](Migration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## migrationsListForOrg

> [Migration] migrationsListForOrg(org, opts)

List organization migrations

Lists the most recent migrations, including both exports (which can be started through the REST API) and imports (which cannot be started using the REST API).  A list of &#x60;repositories&#x60; is only returned for export migrations.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.MigrationsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1, // Number | Page number of the results to fetch.
  'exclude': ["repositories"] // [String] | Exclude attributes from the API response to improve performance
};
apiInstance.migrationsListForOrg(org, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**| The organization name. The name is not case sensitive. | 
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]
 **exclude** | [**[String]**](String.md)| Exclude attributes from the API response to improve performance | [optional] 

### Return type

[**[Migration]**](Migration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## migrationsListReposForAuthenticatedUser

> [MinimalRepository] migrationsListReposForAuthenticatedUser(migrationId, opts)

List repositories for a user migration

Lists all the repositories for this user migration.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.MigrationsApi();
let migrationId = 56; // Number | The unique identifier of the migration.
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.migrationsListReposForAuthenticatedUser(migrationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **migrationId** | **Number**| The unique identifier of the migration. | 
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[MinimalRepository]**](MinimalRepository.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## migrationsListReposForOrg

> [MinimalRepository] migrationsListReposForOrg(org, migrationId, opts)

List repositories in an organization migration

List all the repositories for this organization migration.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.MigrationsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let migrationId = 56; // Number | The unique identifier of the migration.
let opts = {
  'perPage': 30, // Number | The number of results per page (max 100).
  'page': 1 // Number | Page number of the results to fetch.
};
apiInstance.migrationsListReposForOrg(org, migrationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**| The organization name. The name is not case sensitive. | 
 **migrationId** | **Number**| The unique identifier of the migration. | 
 **perPage** | **Number**| The number of results per page (max 100). | [optional] [default to 30]
 **page** | **Number**| Page number of the results to fetch. | [optional] [default to 1]

### Return type

[**[MinimalRepository]**](MinimalRepository.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## migrationsStartForAuthenticatedUser

> Migration migrationsStartForAuthenticatedUser(migrationsStartForAuthenticatedUserRequest)

Start a user migration

Initiates the generation of a user migration archive.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.MigrationsApi();
let migrationsStartForAuthenticatedUserRequest = {"lock_repositories":true,"repositories":["octocat/Hello-World"]}; // MigrationsStartForAuthenticatedUserRequest | 
apiInstance.migrationsStartForAuthenticatedUser(migrationsStartForAuthenticatedUserRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **migrationsStartForAuthenticatedUserRequest** | [**MigrationsStartForAuthenticatedUserRequest**](MigrationsStartForAuthenticatedUserRequest.md)|  | 

### Return type

[**Migration**](Migration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## migrationsStartForOrg

> Migration migrationsStartForOrg(org, migrationsStartForOrgRequest)

Start an organization migration

Initiates the generation of a migration archive.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.MigrationsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let migrationsStartForOrgRequest = {"lock_repositories":true,"repositories":["github/Hello-World"]}; // MigrationsStartForOrgRequest | 
apiInstance.migrationsStartForOrg(org, migrationsStartForOrgRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org** | **String**| The organization name. The name is not case sensitive. | 
 **migrationsStartForOrgRequest** | [**MigrationsStartForOrgRequest**](MigrationsStartForOrgRequest.md)|  | 

### Return type

[**Migration**](Migration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## migrationsUnlockRepoForOrg

> migrationsUnlockRepoForOrg(org, migrationId, repoName)

Unlock an organization repository

Unlocks a repository that was locked for migration. You should unlock each migrated repository and [delete them](https://docs.github.com/enterprise-server@3.4/rest/repos/repos#delete-a-repository) when the migration is complete and you no longer need the source data.

### Example

```javascript
import GitHubV3RestApi from 'git_hub_v3_rest_api';

let apiInstance = new GitHubV3RestApi.MigrationsApi();
let org = "org_example"; // String | The organization name. The name is not case sensitive.
let migrationId = 56; // Number | The unique identifier of the migration.
let repoName = "repoName_example"; // String | repo_name parameter
apiInstance.migrationsUnlockRepoForOrg(org, migrationId, repoName, (error, data, response) => {
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
 **org** | **String**| The organization name. The name is not case sensitive. | 
 **migrationId** | **Number**| The unique identifier of the migration. | 
 **repoName** | **String**| repo_name parameter | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

