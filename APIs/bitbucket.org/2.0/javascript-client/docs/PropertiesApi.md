# BitbucketApi.PropertiesApi

All URIs are relative to *https://api.bitbucket.org/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteCommitHostedPropertyValue**](PropertiesApi.md#deleteCommitHostedPropertyValue) | **DELETE** /repositories/{workspace}/{repo_slug}/commit/{commit}/properties/{app_key}/{property_name} | Delete a commit application property
[**deletePullRequestHostedPropertyValue**](PropertiesApi.md#deletePullRequestHostedPropertyValue) | **DELETE** /repositories/{workspace}/{repo_slug}/pullrequests/{pullrequest_id}/properties/{app_key}/{property_name} | Delete a pull request application property
[**deleteRepositoryHostedPropertyValue**](PropertiesApi.md#deleteRepositoryHostedPropertyValue) | **DELETE** /repositories/{workspace}/{repo_slug}/properties/{app_key}/{property_name} | Delete a repository application property
[**deleteUserHostedPropertyValue**](PropertiesApi.md#deleteUserHostedPropertyValue) | **DELETE** /users/{selected_user}/properties/{app_key}/{property_name} | Delete a user application property
[**getCommitHostedPropertyValue**](PropertiesApi.md#getCommitHostedPropertyValue) | **GET** /repositories/{workspace}/{repo_slug}/commit/{commit}/properties/{app_key}/{property_name} | Get a commit application property
[**getPullRequestHostedPropertyValue**](PropertiesApi.md#getPullRequestHostedPropertyValue) | **GET** /repositories/{workspace}/{repo_slug}/pullrequests/{pullrequest_id}/properties/{app_key}/{property_name} | Get a pull request application property
[**getRepositoryHostedPropertyValue**](PropertiesApi.md#getRepositoryHostedPropertyValue) | **GET** /repositories/{workspace}/{repo_slug}/properties/{app_key}/{property_name} | Get a repository application property
[**retrieveUserHostedPropertyValue**](PropertiesApi.md#retrieveUserHostedPropertyValue) | **GET** /users/{selected_user}/properties/{app_key}/{property_name} | Get a user application property
[**updateCommitHostedPropertyValue**](PropertiesApi.md#updateCommitHostedPropertyValue) | **PUT** /repositories/{workspace}/{repo_slug}/commit/{commit}/properties/{app_key}/{property_name} | Update a commit application property
[**updatePullRequestHostedPropertyValue**](PropertiesApi.md#updatePullRequestHostedPropertyValue) | **PUT** /repositories/{workspace}/{repo_slug}/pullrequests/{pullrequest_id}/properties/{app_key}/{property_name} | Update a pull request application property
[**updateRepositoryHostedPropertyValue**](PropertiesApi.md#updateRepositoryHostedPropertyValue) | **PUT** /repositories/{workspace}/{repo_slug}/properties/{app_key}/{property_name} | Update a repository application property
[**updateUserHostedPropertyValue**](PropertiesApi.md#updateUserHostedPropertyValue) | **PUT** /users/{selected_user}/properties/{app_key}/{property_name} | Update a user application property



## deleteCommitHostedPropertyValue

> deleteCommitHostedPropertyValue(workspace, repoSlug, commit, appKey, propertyName)

Delete a commit application property

Delete an [application property](/cloud/bitbucket/application-properties/) value stored against a commit.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PropertiesApi();
let workspace = "workspace_example"; // String | The repository container; either the workspace slug or the UUID in curly braces.
let repoSlug = "repoSlug_example"; // String | The repository.
let commit = "commit_example"; // String | The commit.
let appKey = "appKey_example"; // String | The key of the Connect app.
let propertyName = "propertyName_example"; // String | The name of the property.
apiInstance.deleteCommitHostedPropertyValue(workspace, repoSlug, commit, appKey, propertyName, (error, data, response) => {
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
 **workspace** | **String**| The repository container; either the workspace slug or the UUID in curly braces. | 
 **repoSlug** | **String**| The repository. | 
 **commit** | **String**| The commit. | 
 **appKey** | **String**| The key of the Connect app. | 
 **propertyName** | **String**| The name of the property. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deletePullRequestHostedPropertyValue

> deletePullRequestHostedPropertyValue(workspace, repoSlug, pullrequestId, appKey, propertyName)

Delete a pull request application property

Delete an [application property](/cloud/bitbucket/application-properties/) value stored against a pull request.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PropertiesApi();
let workspace = "workspace_example"; // String | The repository container; either the workspace slug or the UUID in curly braces.
let repoSlug = "repoSlug_example"; // String | The repository.
let pullrequestId = "pullrequestId_example"; // String | The pull request ID.
let appKey = "appKey_example"; // String | The key of the Connect app.
let propertyName = "propertyName_example"; // String | The name of the property.
apiInstance.deletePullRequestHostedPropertyValue(workspace, repoSlug, pullrequestId, appKey, propertyName, (error, data, response) => {
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
 **workspace** | **String**| The repository container; either the workspace slug or the UUID in curly braces. | 
 **repoSlug** | **String**| The repository. | 
 **pullrequestId** | **String**| The pull request ID. | 
 **appKey** | **String**| The key of the Connect app. | 
 **propertyName** | **String**| The name of the property. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteRepositoryHostedPropertyValue

> deleteRepositoryHostedPropertyValue(workspace, repoSlug, appKey, propertyName)

Delete a repository application property

Delete an [application property](/cloud/bitbucket/application-properties/) value stored against a repository.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PropertiesApi();
let workspace = "workspace_example"; // String | The repository container; either the workspace slug or the UUID in curly braces.
let repoSlug = "repoSlug_example"; // String | The repository.
let appKey = "appKey_example"; // String | The key of the Connect app.
let propertyName = "propertyName_example"; // String | The name of the property.
apiInstance.deleteRepositoryHostedPropertyValue(workspace, repoSlug, appKey, propertyName, (error, data, response) => {
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
 **workspace** | **String**| The repository container; either the workspace slug or the UUID in curly braces. | 
 **repoSlug** | **String**| The repository. | 
 **appKey** | **String**| The key of the Connect app. | 
 **propertyName** | **String**| The name of the property. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteUserHostedPropertyValue

> deleteUserHostedPropertyValue(selectedUser, appKey, propertyName)

Delete a user application property

Delete an [application property](/cloud/bitbucket/application-properties/) value stored against a user.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PropertiesApi();
let selectedUser = "selectedUser_example"; // String | Either the UUID of the account surrounded by curly-braces, for example `{account UUID}`, OR an Atlassian Account ID.
let appKey = "appKey_example"; // String | The key of the Connect app.
let propertyName = "propertyName_example"; // String | The name of the property.
apiInstance.deleteUserHostedPropertyValue(selectedUser, appKey, propertyName, (error, data, response) => {
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
 **selectedUser** | **String**| Either the UUID of the account surrounded by curly-braces, for example &#x60;{account UUID}&#x60;, OR an Atlassian Account ID. | 
 **appKey** | **String**| The key of the Connect app. | 
 **propertyName** | **String**| The name of the property. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getCommitHostedPropertyValue

> ApplicationProperty getCommitHostedPropertyValue(workspace, repoSlug, commit, appKey, propertyName)

Get a commit application property

Retrieve an [application property](/cloud/bitbucket/application-properties/) value stored against a commit.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PropertiesApi();
let workspace = "workspace_example"; // String | The repository container; either the workspace slug or the UUID in curly braces.
let repoSlug = "repoSlug_example"; // String | The repository.
let commit = "commit_example"; // String | The commit.
let appKey = "appKey_example"; // String | The key of the Connect app.
let propertyName = "propertyName_example"; // String | The name of the property.
apiInstance.getCommitHostedPropertyValue(workspace, repoSlug, commit, appKey, propertyName, (error, data, response) => {
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
 **workspace** | **String**| The repository container; either the workspace slug or the UUID in curly braces. | 
 **repoSlug** | **String**| The repository. | 
 **commit** | **String**| The commit. | 
 **appKey** | **String**| The key of the Connect app. | 
 **propertyName** | **String**| The name of the property. | 

### Return type

[**ApplicationProperty**](ApplicationProperty.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPullRequestHostedPropertyValue

> ApplicationProperty getPullRequestHostedPropertyValue(workspace, repoSlug, pullrequestId, appKey, propertyName)

Get a pull request application property

Retrieve an [application property](/cloud/bitbucket/application-properties/) value stored against a pull request.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PropertiesApi();
let workspace = "workspace_example"; // String | The repository container; either the workspace slug or the UUID in curly braces.
let repoSlug = "repoSlug_example"; // String | The repository.
let pullrequestId = "pullrequestId_example"; // String | The pull request ID.
let appKey = "appKey_example"; // String | The key of the Connect app.
let propertyName = "propertyName_example"; // String | The name of the property.
apiInstance.getPullRequestHostedPropertyValue(workspace, repoSlug, pullrequestId, appKey, propertyName, (error, data, response) => {
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
 **workspace** | **String**| The repository container; either the workspace slug or the UUID in curly braces. | 
 **repoSlug** | **String**| The repository. | 
 **pullrequestId** | **String**| The pull request ID. | 
 **appKey** | **String**| The key of the Connect app. | 
 **propertyName** | **String**| The name of the property. | 

### Return type

[**ApplicationProperty**](ApplicationProperty.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRepositoryHostedPropertyValue

> ApplicationProperty getRepositoryHostedPropertyValue(workspace, repoSlug, appKey, propertyName)

Get a repository application property

Retrieve an [application property](/cloud/bitbucket/application-properties/) value stored against a repository.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PropertiesApi();
let workspace = "workspace_example"; // String | The repository container; either the workspace slug or the UUID in curly braces.
let repoSlug = "repoSlug_example"; // String | The repository.
let appKey = "appKey_example"; // String | The key of the Connect app.
let propertyName = "propertyName_example"; // String | The name of the property.
apiInstance.getRepositoryHostedPropertyValue(workspace, repoSlug, appKey, propertyName, (error, data, response) => {
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
 **workspace** | **String**| The repository container; either the workspace slug or the UUID in curly braces. | 
 **repoSlug** | **String**| The repository. | 
 **appKey** | **String**| The key of the Connect app. | 
 **propertyName** | **String**| The name of the property. | 

### Return type

[**ApplicationProperty**](ApplicationProperty.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveUserHostedPropertyValue

> ApplicationProperty retrieveUserHostedPropertyValue(selectedUser, appKey, propertyName)

Get a user application property

Retrieve an [application property](/cloud/bitbucket/application-properties/) value stored against a user.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PropertiesApi();
let selectedUser = "selectedUser_example"; // String | Either the UUID of the account surrounded by curly-braces, for example `{account UUID}`, OR an Atlassian Account ID.
let appKey = "appKey_example"; // String | The key of the Connect app.
let propertyName = "propertyName_example"; // String | The name of the property.
apiInstance.retrieveUserHostedPropertyValue(selectedUser, appKey, propertyName, (error, data, response) => {
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
 **selectedUser** | **String**| Either the UUID of the account surrounded by curly-braces, for example &#x60;{account UUID}&#x60;, OR an Atlassian Account ID. | 
 **appKey** | **String**| The key of the Connect app. | 
 **propertyName** | **String**| The name of the property. | 

### Return type

[**ApplicationProperty**](ApplicationProperty.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateCommitHostedPropertyValue

> updateCommitHostedPropertyValue(workspace, repoSlug, commit, appKey, propertyName, applicationProperty)

Update a commit application property

Update an [application property](/cloud/bitbucket/application-properties/) value stored against a commit.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PropertiesApi();
let workspace = "workspace_example"; // String | The repository container; either the workspace slug or the UUID in curly braces.
let repoSlug = "repoSlug_example"; // String | The repository.
let commit = "commit_example"; // String | The commit.
let appKey = "appKey_example"; // String | The key of the Connect app.
let propertyName = "propertyName_example"; // String | The name of the property.
let applicationProperty = new BitbucketApi.ApplicationProperty(); // ApplicationProperty | The application property to create or update.
apiInstance.updateCommitHostedPropertyValue(workspace, repoSlug, commit, appKey, propertyName, applicationProperty, (error, data, response) => {
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
 **workspace** | **String**| The repository container; either the workspace slug or the UUID in curly braces. | 
 **repoSlug** | **String**| The repository. | 
 **commit** | **String**| The commit. | 
 **appKey** | **String**| The key of the Connect app. | 
 **propertyName** | **String**| The name of the property. | 
 **applicationProperty** | [**ApplicationProperty**](ApplicationProperty.md)| The application property to create or update. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updatePullRequestHostedPropertyValue

> updatePullRequestHostedPropertyValue(workspace, repoSlug, pullrequestId, appKey, propertyName, applicationProperty)

Update a pull request application property

Update an [application property](/cloud/bitbucket/application-properties/) value stored against a pull request.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PropertiesApi();
let workspace = "workspace_example"; // String | The repository container; either the workspace slug or the UUID in curly braces.
let repoSlug = "repoSlug_example"; // String | The repository.
let pullrequestId = "pullrequestId_example"; // String | The pull request ID.
let appKey = "appKey_example"; // String | The key of the Connect app.
let propertyName = "propertyName_example"; // String | The name of the property.
let applicationProperty = new BitbucketApi.ApplicationProperty(); // ApplicationProperty | The application property to create or update.
apiInstance.updatePullRequestHostedPropertyValue(workspace, repoSlug, pullrequestId, appKey, propertyName, applicationProperty, (error, data, response) => {
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
 **workspace** | **String**| The repository container; either the workspace slug or the UUID in curly braces. | 
 **repoSlug** | **String**| The repository. | 
 **pullrequestId** | **String**| The pull request ID. | 
 **appKey** | **String**| The key of the Connect app. | 
 **propertyName** | **String**| The name of the property. | 
 **applicationProperty** | [**ApplicationProperty**](ApplicationProperty.md)| The application property to create or update. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateRepositoryHostedPropertyValue

> updateRepositoryHostedPropertyValue(workspace, repoSlug, appKey, propertyName, applicationProperty)

Update a repository application property

Update an [application property](/cloud/bitbucket/application-properties/) value stored against a repository.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PropertiesApi();
let workspace = "workspace_example"; // String | The repository container; either the workspace slug or the UUID in curly braces.
let repoSlug = "repoSlug_example"; // String | The repository.
let appKey = "appKey_example"; // String | The key of the Connect app.
let propertyName = "propertyName_example"; // String | The name of the property.
let applicationProperty = new BitbucketApi.ApplicationProperty(); // ApplicationProperty | The application property to create or update.
apiInstance.updateRepositoryHostedPropertyValue(workspace, repoSlug, appKey, propertyName, applicationProperty, (error, data, response) => {
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
 **workspace** | **String**| The repository container; either the workspace slug or the UUID in curly braces. | 
 **repoSlug** | **String**| The repository. | 
 **appKey** | **String**| The key of the Connect app. | 
 **propertyName** | **String**| The name of the property. | 
 **applicationProperty** | [**ApplicationProperty**](ApplicationProperty.md)| The application property to create or update. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateUserHostedPropertyValue

> updateUserHostedPropertyValue(selectedUser, appKey, propertyName, applicationProperty)

Update a user application property

Update an [application property](/cloud/bitbucket/application-properties/) value stored against a user.

### Example

```javascript
import BitbucketApi from 'bitbucket_api';

let apiInstance = new BitbucketApi.PropertiesApi();
let selectedUser = "selectedUser_example"; // String | Either the UUID of the account surrounded by curly-braces, for example `{account UUID}`, OR an Atlassian Account ID.
let appKey = "appKey_example"; // String | The key of the Connect app.
let propertyName = "propertyName_example"; // String | The name of the property.
let applicationProperty = new BitbucketApi.ApplicationProperty(); // ApplicationProperty | The application property to create or update.
apiInstance.updateUserHostedPropertyValue(selectedUser, appKey, propertyName, applicationProperty, (error, data, response) => {
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
 **selectedUser** | **String**| Either the UUID of the account surrounded by curly-braces, for example &#x60;{account UUID}&#x60;, OR an Atlassian Account ID. | 
 **appKey** | **String**| The key of the Connect app. | 
 **propertyName** | **String**| The name of the property. | 
 **applicationProperty** | [**ApplicationProperty**](ApplicationProperty.md)| The application property to create or update. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

