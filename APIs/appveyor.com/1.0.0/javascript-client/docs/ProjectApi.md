# AppVeyorRestApi.ProjectApi

All URIs are relative to *https://ci.appveyor.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addProject**](ProjectApi.md#addProject) | **POST** /projects | Add project
[**deleteProject**](ProjectApi.md#deleteProject) | **DELETE** /projects/{accountName}/{projectSlug} | Delete project
[**deleteProjectBuildCache**](ProjectApi.md#deleteProjectBuildCache) | **DELETE** /projects/{accountName}/{projectSlug}/buildcache | Delete project build cache
[**encryptValue**](ProjectApi.md#encryptValue) | **POST** /account/encrypt | Encrypt a value for use in StoredValue.
[**getProjectArtifact**](ProjectApi.md#getProjectArtifact) | **GET** /projects/{accountName}/{projectSlug}/artifacts/{artifactFileName} | Get last successful build artifact
[**getProjectBranchStatusBadge**](ProjectApi.md#getProjectBranchStatusBadge) | **GET** /projects/status/{statusBadgeId}/branch/{buildBranch} | Get project branch status badge image
[**getProjectBuildByVersion**](ProjectApi.md#getProjectBuildByVersion) | **GET** /projects/{accountName}/{projectSlug}/build/{buildVersion} | Get project build by version
[**getProjectDeployments**](ProjectApi.md#getProjectDeployments) | **GET** /projects/{accountName}/{projectSlug}/deployments | Get project deployments
[**getProjectEnvironmentVariables**](ProjectApi.md#getProjectEnvironmentVariables) | **GET** /projects/{accountName}/{projectSlug}/settings/environment-variables | Get project environment variables
[**getProjectHistory**](ProjectApi.md#getProjectHistory) | **GET** /projects/{accountName}/{projectSlug}/history | Get project history
[**getProjectLastBuild**](ProjectApi.md#getProjectLastBuild) | **GET** /projects/{accountName}/{projectSlug} | Get project last build
[**getProjectLastBuildBranch**](ProjectApi.md#getProjectLastBuildBranch) | **GET** /projects/{accountName}/{projectSlug}/branch/{buildBranch} | Get project last branch build
[**getProjectSettings**](ProjectApi.md#getProjectSettings) | **GET** /projects/{accountName}/{projectSlug}/settings | Get project settings
[**getProjectSettingsYaml**](ProjectApi.md#getProjectSettingsYaml) | **GET** /projects/{accountName}/{projectSlug}/settings/yaml | Get project settings in YAML
[**getProjectStatusBadge**](ProjectApi.md#getProjectStatusBadge) | **GET** /projects/status/{statusBadgeId} | Get project status badge image
[**getProjects**](ProjectApi.md#getProjects) | **GET** /projects | Get projects
[**getPublicProjectStatusBadge**](ProjectApi.md#getPublicProjectStatusBadge) | **GET** /projects/status/{badgeRepoProvider}/{repoAccountName}/{repoSlug} | Get status badge image for a project with a public repository
[**updateProject**](ProjectApi.md#updateProject) | **PUT** /projects | Update project
[**updateProjectBuildNumber**](ProjectApi.md#updateProjectBuildNumber) | **PUT** /projects/{accountName}/{projectSlug}/settings/build-number | Update project build number
[**updateProjectEnvironmentVariables**](ProjectApi.md#updateProjectEnvironmentVariables) | **PUT** /projects/{accountName}/{projectSlug}/settings/environment-variables | Update project environment variables
[**updateProjectSettingsYaml**](ProjectApi.md#updateProjectSettingsYaml) | **PUT** /projects/{accountName}/{projectSlug}/settings/yaml | Update project settings in YAML



## addProject

> Project addProject(body)

Add project

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.ProjectApi();
let body = new AppVeyorRestApi.ProjectAddition(); // ProjectAddition | 
apiInstance.addProject(body, (error, data, response) => {
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
 **body** | [**ProjectAddition**](ProjectAddition.md)|  | 

### Return type

[**Project**](Project.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml


## deleteProject

> deleteProject(accountName, projectSlug)

Delete project

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.ProjectApi();
let accountName = "accountName_example"; // String | AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the `accountName` property of `UserAccount`.
let projectSlug = "projectSlug_example"; // String | Project Slug
apiInstance.deleteProject(accountName, projectSlug, (error, data, response) => {
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
 **accountName** | **String**| AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;. | 
 **projectSlug** | **String**| Project Slug | 

### Return type

null (empty response body)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## deleteProjectBuildCache

> deleteProjectBuildCache(accountName, projectSlug)

Delete project build cache

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.ProjectApi();
let accountName = "accountName_example"; // String | AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the `accountName` property of `UserAccount`.
let projectSlug = "projectSlug_example"; // String | Project Slug
apiInstance.deleteProjectBuildCache(accountName, projectSlug, (error, data, response) => {
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
 **accountName** | **String**| AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;. | 
 **projectSlug** | **String**| Project Slug | 

### Return type

null (empty response body)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## encryptValue

> String encryptValue(body)

Encrypt a value for use in StoredValue.

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.ProjectApi();
let body = new AppVeyorRestApi.EncryptRequest(); // EncryptRequest | 
apiInstance.encryptValue(body, (error, data, response) => {
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
 **body** | [**EncryptRequest**](EncryptRequest.md)|  | 

### Return type

**String**

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: text/plain


## getProjectArtifact

> File getProjectArtifact(accountName, projectSlug, artifactFileName, opts)

Get last successful build artifact

The &#x60;job&#x60; parameter is mandatory if the build contains multiple jobs.

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';

let apiInstance = new AppVeyorRestApi.ProjectApi();
let accountName = "accountName_example"; // String | AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the `accountName` property of `UserAccount`.
let projectSlug = "projectSlug_example"; // String | Project Slug
let artifactFileName = "artifactFileName_example"; // String | File name (or path) of a build artifact file. Corresponds to the `fileName` property of `ArtifactModel`. URL-encoding of slashes in parameter values is optional.
let opts = {
  'branch': "branch_example", // String | Repository Branch
  'tag': "tag_example", // String | A git (or other VCS) tag
  'job': "job_example", // String | Name of the build job.
  'all': false, // Boolean | Include not only `successful`, but also jobs with `failed`, and `cancelled` status.
  'pr': true // Boolean | Include PR builds in the search results? `true` - take artifact from PR builds only; `false` - do not look for artifact in PR builds; default/unspecified - look for artifact in both PR an non-PR builds. 
};
apiInstance.getProjectArtifact(accountName, projectSlug, artifactFileName, opts, (error, data, response) => {
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
 **accountName** | **String**| AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;. | 
 **projectSlug** | **String**| Project Slug | 
 **artifactFileName** | **String**| File name (or path) of a build artifact file. Corresponds to the &#x60;fileName&#x60; property of &#x60;ArtifactModel&#x60;. URL-encoding of slashes in parameter values is optional. | 
 **branch** | **String**| Repository Branch | [optional] 
 **tag** | **String**| A git (or other VCS) tag | [optional] 
 **job** | **String**| Name of the build job. | [optional] 
 **all** | **Boolean**| Include not only &#x60;successful&#x60;, but also jobs with &#x60;failed&#x60;, and &#x60;cancelled&#x60; status. | [optional] [default to false]
 **pr** | **Boolean**| Include PR builds in the search results? &#x60;true&#x60; - take artifact from PR builds only; &#x60;false&#x60; - do not look for artifact in PR builds; default/unspecified - look for artifact in both PR an non-PR builds.  | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## getProjectBranchStatusBadge

> File getProjectBranchStatusBadge(statusBadgeId, buildBranch, opts)

Get project branch status badge image

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';

let apiInstance = new AppVeyorRestApi.ProjectApi();
let statusBadgeId = "statusBadgeId_example"; // String | ID of the status badge (`statusBadgeId` from `ProjectWithConfiguration`).
let buildBranch = "buildBranch_example"; // String | Build Branch
let opts = {
  'svg': false, // Boolean | Return an SVG image instead of PNG?  Exclusive with `retina`.
  'retina': false, // Boolean | Return a larger image suitable for retina displays?  Exclusive with `svg`.
  'passingText': "passingText_example", // String | Text to show in badge when build is passing.
  'failingText': "failingText_example", // String | Text to show in badge when build is failing.
  'pendingText': "pendingText_example" // String | Text to show in badge when build is pending.
};
apiInstance.getProjectBranchStatusBadge(statusBadgeId, buildBranch, opts, (error, data, response) => {
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
 **statusBadgeId** | **String**| ID of the status badge (&#x60;statusBadgeId&#x60; from &#x60;ProjectWithConfiguration&#x60;). | 
 **buildBranch** | **String**| Build Branch | 
 **svg** | **Boolean**| Return an SVG image instead of PNG?  Exclusive with &#x60;retina&#x60;. | [optional] [default to false]
 **retina** | **Boolean**| Return a larger image suitable for retina displays?  Exclusive with &#x60;svg&#x60;. | [optional] [default to false]
 **passingText** | **String**| Text to show in badge when build is passing. | [optional] 
 **failingText** | **String**| Text to show in badge when build is failing. | [optional] 
 **pendingText** | **String**| Text to show in badge when build is pending. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/svg+xml, image/png


## getProjectBuildByVersion

> ProjectBuildResults getProjectBuildByVersion(accountName, projectSlug, buildVersion)

Get project build by version

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';

let apiInstance = new AppVeyorRestApi.ProjectApi();
let accountName = "accountName_example"; // String | AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the `accountName` property of `UserAccount`.
let projectSlug = "projectSlug_example"; // String | Project Slug
let buildVersion = "buildVersion_example"; // String | Build Version (`version` property of `Build`)
apiInstance.getProjectBuildByVersion(accountName, projectSlug, buildVersion, (error, data, response) => {
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
 **accountName** | **String**| AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;. | 
 **projectSlug** | **String**| Project Slug | 
 **buildVersion** | **String**| Build Version (&#x60;version&#x60; property of &#x60;Build&#x60;) | 

### Return type

[**ProjectBuildResults**](ProjectBuildResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getProjectDeployments

> ProjectDeploymentsResults getProjectDeployments(accountName, projectSlug, recordsNumber)

Get project deployments

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.ProjectApi();
let accountName = "accountName_example"; // String | AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the `accountName` property of `UserAccount`.
let projectSlug = "projectSlug_example"; // String | Project Slug
let recordsNumber = 56; // Number | Number of results to include in the response. getProjectDeployments is documented to have a maximum of 20. It currently returns 500 Internal Server Error for recordsNumber <= 5. In the past it has returned 500 Internal Server Error for many different values which did not match the value used by the ci.appveyor.com web interface at the time.  As of 2018-09-08, the value used by the web interface is 10.
apiInstance.getProjectDeployments(accountName, projectSlug, recordsNumber, (error, data, response) => {
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
 **accountName** | **String**| AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;. | 
 **projectSlug** | **String**| Project Slug | 
 **recordsNumber** | **Number**| Number of results to include in the response. getProjectDeployments is documented to have a maximum of 20. It currently returns 500 Internal Server Error for recordsNumber &lt;&#x3D; 5. In the past it has returned 500 Internal Server Error for many different values which did not match the value used by the ci.appveyor.com web interface at the time.  As of 2018-09-08, the value used by the web interface is 10. | 

### Return type

[**ProjectDeploymentsResults**](ProjectDeploymentsResults.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getProjectEnvironmentVariables

> [StoredNameValue] getProjectEnvironmentVariables(accountName, projectSlug)

Get project environment variables

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.ProjectApi();
let accountName = "accountName_example"; // String | AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the `accountName` property of `UserAccount`.
let projectSlug = "projectSlug_example"; // String | Project Slug
apiInstance.getProjectEnvironmentVariables(accountName, projectSlug, (error, data, response) => {
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
 **accountName** | **String**| AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;. | 
 **projectSlug** | **String**| Project Slug | 

### Return type

[**[StoredNameValue]**](StoredNameValue.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getProjectHistory

> ProjectHistory getProjectHistory(accountName, projectSlug, recordsNumber, opts)

Get project history

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';

let apiInstance = new AppVeyorRestApi.ProjectApi();
let accountName = "accountName_example"; // String | AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the `accountName` property of `UserAccount`.
let projectSlug = "projectSlug_example"; // String | Project Slug
let recordsNumber = 56; // Number | Number of results to include in the response. getProjectDeployments is documented to have a maximum of 20. It currently returns 500 Internal Server Error for recordsNumber <= 5. In the past it has returned 500 Internal Server Error for many different values which did not match the value used by the ci.appveyor.com web interface at the time.  As of 2018-09-08, the value used by the web interface is 10.
let opts = {
  'startBuildId': 56, // Number | Maximum `buildId` to include in the results (exclusive).
  'branch': "branch_example" // String | Repository Branch
};
apiInstance.getProjectHistory(accountName, projectSlug, recordsNumber, opts, (error, data, response) => {
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
 **accountName** | **String**| AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;. | 
 **projectSlug** | **String**| Project Slug | 
 **recordsNumber** | **Number**| Number of results to include in the response. getProjectDeployments is documented to have a maximum of 20. It currently returns 500 Internal Server Error for recordsNumber &lt;&#x3D; 5. In the past it has returned 500 Internal Server Error for many different values which did not match the value used by the ci.appveyor.com web interface at the time.  As of 2018-09-08, the value used by the web interface is 10. | 
 **startBuildId** | **Number**| Maximum &#x60;buildId&#x60; to include in the results (exclusive). | [optional] 
 **branch** | **String**| Repository Branch | [optional] 

### Return type

[**ProjectHistory**](ProjectHistory.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getProjectLastBuild

> ProjectBuildResults getProjectLastBuild(accountName, projectSlug)

Get project last build

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';

let apiInstance = new AppVeyorRestApi.ProjectApi();
let accountName = "accountName_example"; // String | AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the `accountName` property of `UserAccount`.
let projectSlug = "projectSlug_example"; // String | Project Slug
apiInstance.getProjectLastBuild(accountName, projectSlug, (error, data, response) => {
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
 **accountName** | **String**| AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;. | 
 **projectSlug** | **String**| Project Slug | 

### Return type

[**ProjectBuildResults**](ProjectBuildResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getProjectLastBuildBranch

> ProjectBuildResults getProjectLastBuildBranch(accountName, projectSlug, buildBranch)

Get project last branch build

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';

let apiInstance = new AppVeyorRestApi.ProjectApi();
let accountName = "accountName_example"; // String | AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the `accountName` property of `UserAccount`.
let projectSlug = "projectSlug_example"; // String | Project Slug
let buildBranch = "buildBranch_example"; // String | Build Branch
apiInstance.getProjectLastBuildBranch(accountName, projectSlug, buildBranch, (error, data, response) => {
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
 **accountName** | **String**| AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;. | 
 **projectSlug** | **String**| Project Slug | 
 **buildBranch** | **String**| Build Branch | 

### Return type

[**ProjectBuildResults**](ProjectBuildResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getProjectSettings

> ProjectSettingsResults getProjectSettings(accountName, projectSlug)

Get project settings

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.ProjectApi();
let accountName = "accountName_example"; // String | AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the `accountName` property of `UserAccount`.
let projectSlug = "projectSlug_example"; // String | Project Slug
apiInstance.getProjectSettings(accountName, projectSlug, (error, data, response) => {
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
 **accountName** | **String**| AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;. | 
 **projectSlug** | **String**| Project Slug | 

### Return type

[**ProjectSettingsResults**](ProjectSettingsResults.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getProjectSettingsYaml

> String getProjectSettingsYaml(accountName, projectSlug)

Get project settings in YAML

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.ProjectApi();
let accountName = "accountName_example"; // String | AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the `accountName` property of `UserAccount`.
let projectSlug = "projectSlug_example"; // String | Project Slug
apiInstance.getProjectSettingsYaml(accountName, projectSlug, (error, data, response) => {
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
 **accountName** | **String**| AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;. | 
 **projectSlug** | **String**| Project Slug | 

### Return type

**String**

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain


## getProjectStatusBadge

> File getProjectStatusBadge(statusBadgeId, opts)

Get project status badge image

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';

let apiInstance = new AppVeyorRestApi.ProjectApi();
let statusBadgeId = "statusBadgeId_example"; // String | ID of the status badge (`statusBadgeId` from `ProjectWithConfiguration`).
let opts = {
  'svg': false, // Boolean | Return an SVG image instead of PNG?  Exclusive with `retina`.
  'retina': false, // Boolean | Return a larger image suitable for retina displays?  Exclusive with `svg`.
  'passingText': "passingText_example", // String | Text to show in badge when build is passing.
  'failingText': "failingText_example", // String | Text to show in badge when build is failing.
  'pendingText': "pendingText_example" // String | Text to show in badge when build is pending.
};
apiInstance.getProjectStatusBadge(statusBadgeId, opts, (error, data, response) => {
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
 **statusBadgeId** | **String**| ID of the status badge (&#x60;statusBadgeId&#x60; from &#x60;ProjectWithConfiguration&#x60;). | 
 **svg** | **Boolean**| Return an SVG image instead of PNG?  Exclusive with &#x60;retina&#x60;. | [optional] [default to false]
 **retina** | **Boolean**| Return a larger image suitable for retina displays?  Exclusive with &#x60;svg&#x60;. | [optional] [default to false]
 **passingText** | **String**| Text to show in badge when build is passing. | [optional] 
 **failingText** | **String**| Text to show in badge when build is failing. | [optional] 
 **pendingText** | **String**| Text to show in badge when build is pending. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/svg+xml, image/png


## getProjects

> [Project] getProjects()

Get projects

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.ProjectApi();
apiInstance.getProjects((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Project]**](Project.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getPublicProjectStatusBadge

> File getPublicProjectStatusBadge(badgeRepoProvider, repoAccountName, repoSlug, opts)

Get status badge image for a project with a public repository

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';

let apiInstance = new AppVeyorRestApi.ProjectApi();
let badgeRepoProvider = "badgeRepoProvider_example"; // String | Repository provider supported for badges
let repoAccountName = "repoAccountName_example"; // String | Account name with repository provider
let repoSlug = "repoSlug_example"; // String | Slug (URL component) of repository.
let opts = {
  'branch': "branch_example", // String | Repository Branch
  'svg': false, // Boolean | Return an SVG image instead of PNG?  Exclusive with `retina`.
  'retina': false, // Boolean | Return a larger image suitable for retina displays?  Exclusive with `svg`.
  'passingText': "passingText_example", // String | Text to show in badge when build is passing.
  'failingText': "failingText_example", // String | Text to show in badge when build is failing.
  'pendingText': "pendingText_example" // String | Text to show in badge when build is pending.
};
apiInstance.getPublicProjectStatusBadge(badgeRepoProvider, repoAccountName, repoSlug, opts, (error, data, response) => {
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
 **badgeRepoProvider** | **String**| Repository provider supported for badges | 
 **repoAccountName** | **String**| Account name with repository provider | 
 **repoSlug** | **String**| Slug (URL component) of repository. | 
 **branch** | **String**| Repository Branch | [optional] 
 **svg** | **Boolean**| Return an SVG image instead of PNG?  Exclusive with &#x60;retina&#x60;. | [optional] [default to false]
 **retina** | **Boolean**| Return a larger image suitable for retina displays?  Exclusive with &#x60;svg&#x60;. | [optional] [default to false]
 **passingText** | **String**| Text to show in badge when build is passing. | [optional] 
 **failingText** | **String**| Text to show in badge when build is failing. | [optional] 
 **pendingText** | **String**| Text to show in badge when build is pending. | [optional] 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/svg+xml, image/png


## updateProject

> updateProject(body)

Update project

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.ProjectApi();
let body = new AppVeyorRestApi.ProjectWithConfiguration(); // ProjectWithConfiguration | 
apiInstance.updateProject(body, (error, data, response) => {
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
 **body** | [**ProjectWithConfiguration**](ProjectWithConfiguration.md)|  | 

### Return type

null (empty response body)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml


## updateProjectBuildNumber

> updateProjectBuildNumber(accountName, projectSlug, body)

Update project build number

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.ProjectApi();
let accountName = "accountName_example"; // String | AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the `accountName` property of `UserAccount`.
let projectSlug = "projectSlug_example"; // String | Project Slug
let body = new AppVeyorRestApi.ProjectBuildNumberUpdate(); // ProjectBuildNumberUpdate | 
apiInstance.updateProjectBuildNumber(accountName, projectSlug, body, (error, data, response) => {
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
 **accountName** | **String**| AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;. | 
 **projectSlug** | **String**| Project Slug | 
 **body** | [**ProjectBuildNumberUpdate**](ProjectBuildNumberUpdate.md)|  | 

### Return type

null (empty response body)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml


## updateProjectEnvironmentVariables

> updateProjectEnvironmentVariables(accountName, projectSlug, body)

Update project environment variables

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.ProjectApi();
let accountName = "accountName_example"; // String | AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the `accountName` property of `UserAccount`.
let projectSlug = "projectSlug_example"; // String | Project Slug
let body = [new AppVeyorRestApi.StoredNameValue()]; // [StoredNameValue] | 
apiInstance.updateProjectEnvironmentVariables(accountName, projectSlug, body, (error, data, response) => {
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
 **accountName** | **String**| AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;. | 
 **projectSlug** | **String**| Project Slug | 
 **body** | [**[StoredNameValue]**](StoredNameValue.md)|  | 

### Return type

null (empty response body)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml


## updateProjectSettingsYaml

> updateProjectSettingsYaml(accountName, projectSlug, body)

Update project settings in YAML

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.ProjectApi();
let accountName = "accountName_example"; // String | AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the `accountName` property of `UserAccount`.
let projectSlug = "projectSlug_example"; // String | Project Slug
let body = "/path/to/file"; // File | The body of requests should contain YAML data.  It is unclear how to specify this since the OpenAPI spec requires `schema` without `type` for `in: body` parameters and does not allow `type: file` in `schema`.  See https://github.com/OAI/OpenAPI-Specification/issues/326 swagger-codegen (for Java, probably others) allows a binary string body parameter with non-application/json `consumes` to be passed through in the request body without conversion to JSON. 
apiInstance.updateProjectSettingsYaml(accountName, projectSlug, body, (error, data, response) => {
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
 **accountName** | **String**| AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the &#x60;accountName&#x60; property of &#x60;UserAccount&#x60;. | 
 **projectSlug** | **String**| Project Slug | 
 **body** | **File**| The body of requests should contain YAML data.  It is unclear how to specify this since the OpenAPI spec requires &#x60;schema&#x60; without &#x60;type&#x60; for &#x60;in: body&#x60; parameters and does not allow &#x60;type: file&#x60; in &#x60;schema&#x60;.  See https://github.com/OAI/OpenAPI-Specification/issues/326 swagger-codegen (for Java, probably others) allows a binary string body parameter with non-application/json &#x60;consumes&#x60; to be passed through in the request body without conversion to JSON.  | 

### Return type

null (empty response body)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: text/plain
- **Accept**: application/json, application/xml

