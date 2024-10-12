# AppCenterClient.BuildApi

All URIs are relative to *https://api.appcenter.ms*

Method | HTTP request | Description
------------- | ------------- | -------------
[**branchConfigurationsCreate**](BuildApi.md#branchConfigurationsCreate) | **POST** /v0.1/apps/{owner_name}/{app_name}/branches/{branch}/config | 
[**branchConfigurationsDelete**](BuildApi.md#branchConfigurationsDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/branches/{branch}/config | 
[**branchConfigurationsGet**](BuildApi.md#branchConfigurationsGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/branches/{branch}/config | 
[**branchConfigurationsUpdate**](BuildApi.md#branchConfigurationsUpdate) | **PUT** /v0.1/apps/{owner_name}/{app_name}/branches/{branch}/config | 
[**buildConfigurationsGet**](BuildApi.md#buildConfigurationsGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/branches/{branch}/export_config | 
[**buildsCreate**](BuildApi.md#buildsCreate) | **POST** /v0.1/apps/{owner_name}/{app_name}/branches/{branch}/builds | 
[**buildsDistribute**](BuildApi.md#buildsDistribute) | **POST** /v0.1/apps/{owner_name}/{app_name}/builds/{build_id}/distribute | 
[**buildsGet**](BuildApi.md#buildsGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/builds/{build_id} | 
[**buildsGetDownloadUri**](BuildApi.md#buildsGetDownloadUri) | **GET** /v0.1/apps/{owner_name}/{app_name}/builds/{build_id}/downloads/{download_type} | 
[**buildsGetLog**](BuildApi.md#buildsGetLog) | **GET** /v0.1/apps/{owner_name}/{app_name}/builds/{build_id}/logs | 
[**buildsGetStatusByAppId**](BuildApi.md#buildsGetStatusByAppId) | **GET** /v0.1/apps/{owner_name}/{app_name}/build_service_status | 
[**buildsListBranches**](BuildApi.md#buildsListBranches) | **GET** /v0.1/apps/{owner_name}/{app_name}/branches | 
[**buildsListByBranch**](BuildApi.md#buildsListByBranch) | **GET** /v0.1/apps/{owner_name}/{app_name}/branches/{branch}/builds | 
[**buildsListToolsetProjects**](BuildApi.md#buildsListToolsetProjects) | **GET** /v0.1/apps/{owner_name}/{app_name}/branches/{branch}/toolset_projects | 
[**buildsListToolsets**](BuildApi.md#buildsListToolsets) | **GET** /v0.1/apps/{owner_name}/{app_name}/toolsets | 
[**buildsListXamarinSDKBundles**](BuildApi.md#buildsListXamarinSDKBundles) | **GET** /v0.1/apps/{owner_name}/{app_name}/xamarin_sdk_bundles | 
[**buildsListXcodeVersions**](BuildApi.md#buildsListXcodeVersions) | **GET** /v0.1/apps/{owner_name}/{app_name}/xcode_versions | 
[**buildsUpdate**](BuildApi.md#buildsUpdate) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/builds/{build_id} | 
[**buildsWebhook**](BuildApi.md#buildsWebhook) | **POST** /v0.1/public/hooks | 
[**commitsListByShaList**](BuildApi.md#commitsListByShaList) | **GET** /v0.1/apps/{owner_name}/{app_name}/commits/batch | 
[**fileAssetsCreate**](BuildApi.md#fileAssetsCreate) | **POST** /v0.1/apps/{owner_name}/{app_name}/file_asset | 
[**repositoriesList**](BuildApi.md#repositoriesList) | **GET** /v0.1/apps/{owner_name}/{app_name}/source_hosts/{source_host}/repositories | 
[**repositoryConfigurationsCreateOrUpdate**](BuildApi.md#repositoryConfigurationsCreateOrUpdate) | **POST** /v0.1/apps/{owner_name}/{app_name}/repo_config | 
[**repositoryConfigurationsDelete**](BuildApi.md#repositoryConfigurationsDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/repo_config | 
[**repositoryConfigurationsList**](BuildApi.md#repositoryConfigurationsList) | **GET** /v0.1/apps/{owner_name}/{app_name}/repo_config | 



## branchConfigurationsCreate

> BranchConfigurationsGet200Response branchConfigurationsCreate(branch, ownerName, appName, branchConfigurationsUpdateRequest)



Configures the branch for build

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.BuildApi();
let branch = "branch_example"; // String | The branch name
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let branchConfigurationsUpdateRequest = new AppCenterClient.BranchConfigurationsUpdateRequest(); // BranchConfigurationsUpdateRequest | Parameters of the configuration
apiInstance.branchConfigurationsCreate(branch, ownerName, appName, branchConfigurationsUpdateRequest, (error, data, response) => {
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
 **branch** | **String**| The branch name | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **branchConfigurationsUpdateRequest** | [**BranchConfigurationsUpdateRequest**](BranchConfigurationsUpdateRequest.md)| Parameters of the configuration | 

### Return type

[**BranchConfigurationsGet200Response**](BranchConfigurationsGet200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## branchConfigurationsDelete

> BranchConfigurationsDelete200Response branchConfigurationsDelete(branch, ownerName, appName, opts)



Deletes the branch build configuration

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.BuildApi();
let branch = "branch_example"; // String | The branch name
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'body': {key: null} // Object | 
};
apiInstance.branchConfigurationsDelete(branch, ownerName, appName, opts, (error, data, response) => {
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
 **branch** | **String**| The branch name | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **body** | **Object**|  | [optional] 

### Return type

[**BranchConfigurationsDelete200Response**](BranchConfigurationsDelete200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## branchConfigurationsGet

> BranchConfigurationsGet200Response branchConfigurationsGet(branch, ownerName, appName)



Gets the branch configuration

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.BuildApi();
let branch = "branch_example"; // String | The branch name
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.branchConfigurationsGet(branch, ownerName, appName, (error, data, response) => {
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
 **branch** | **String**| The branch name | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**BranchConfigurationsGet200Response**](BranchConfigurationsGet200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## branchConfigurationsUpdate

> BranchConfigurationsGet200Response branchConfigurationsUpdate(branch, ownerName, appName, branchConfigurationsUpdateRequest)



Reconfigures the branch for build

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.BuildApi();
let branch = "branch_example"; // String | The branch name
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let branchConfigurationsUpdateRequest = new AppCenterClient.BranchConfigurationsUpdateRequest(); // BranchConfigurationsUpdateRequest | Parameters of the configuration
apiInstance.branchConfigurationsUpdate(branch, ownerName, appName, branchConfigurationsUpdateRequest, (error, data, response) => {
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
 **branch** | **String**| The branch name | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **branchConfigurationsUpdateRequest** | [**BranchConfigurationsUpdateRequest**](BranchConfigurationsUpdateRequest.md)| Parameters of the configuration | 

### Return type

[**BranchConfigurationsGet200Response**](BranchConfigurationsGet200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## buildConfigurationsGet

> BuildConfigurationsGet200Response buildConfigurationsGet(branch, ownerName, appName, opts)



Gets the build configuration in Azure pipeline YAML format

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.BuildApi();
let branch = "branch_example"; // String | The branch name
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'format': "'yaml'" // String | Configuration format
};
apiInstance.buildConfigurationsGet(branch, ownerName, appName, opts, (error, data, response) => {
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
 **branch** | **String**| The branch name | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **format** | **String**| Configuration format | [optional] [default to &#39;yaml&#39;]

### Return type

[**BuildConfigurationsGet200Response**](BuildConfigurationsGet200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildsCreate

> BuildsListBranches200ResponseInnerLastBuild buildsCreate(branch, ownerName, appName, opts)



Create a build

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.BuildApi();
let branch = "branch_example"; // String | The branch name
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'buildsCreateRequest': new AppCenterClient.BuildsCreateRequest() // BuildsCreateRequest | Parameters of the build
};
apiInstance.buildsCreate(branch, ownerName, appName, opts, (error, data, response) => {
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
 **branch** | **String**| The branch name | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **buildsCreateRequest** | [**BuildsCreateRequest**](BuildsCreateRequest.md)| Parameters of the build | [optional] 

### Return type

[**BuildsListBranches200ResponseInnerLastBuild**](BuildsListBranches200ResponseInnerLastBuild.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## buildsDistribute

> BuildsDistribute200Response buildsDistribute(buildId, ownerName, appName, buildsDistributeRequest)



Distribute a build

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.BuildApi();
let buildId = 56; // Number | The build ID
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let buildsDistributeRequest = new AppCenterClient.BuildsDistributeRequest(); // BuildsDistributeRequest | The distribution details
apiInstance.buildsDistribute(buildId, ownerName, appName, buildsDistributeRequest, (error, data, response) => {
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
 **buildId** | **Number**| The build ID | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **buildsDistributeRequest** | [**BuildsDistributeRequest**](BuildsDistributeRequest.md)| The distribution details | 

### Return type

[**BuildsDistribute200Response**](BuildsDistribute200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## buildsGet

> BuildsListBranches200ResponseInnerLastBuild buildsGet(buildId, ownerName, appName)



Returns the build detail for the given build ID

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.BuildApi();
let buildId = 56; // Number | The build ID
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.buildsGet(buildId, ownerName, appName, (error, data, response) => {
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
 **buildId** | **Number**| The build ID | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**BuildsListBranches200ResponseInnerLastBuild**](BuildsListBranches200ResponseInnerLastBuild.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildsGetDownloadUri

> BuildsGetDownloadUri200Response buildsGetDownloadUri(buildId, downloadType, ownerName, appName)



Gets the download URI

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.BuildApi();
let buildId = 56; // Number | The build ID
let downloadType = "downloadType_example"; // String | The download type
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.buildsGetDownloadUri(buildId, downloadType, ownerName, appName, (error, data, response) => {
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
 **buildId** | **Number**| The build ID | 
 **downloadType** | **String**| The download type | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**BuildsGetDownloadUri200Response**](BuildsGetDownloadUri200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildsGetLog

> BuildsGetLog200Response buildsGetLog(buildId, ownerName, appName)



Get the build log

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.BuildApi();
let buildId = 56; // Number | The build ID
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.buildsGetLog(buildId, ownerName, appName, (error, data, response) => {
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
 **buildId** | **Number**| The build ID | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**BuildsGetLog200Response**](BuildsGetLog200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildsGetStatusByAppId

> BuildsGetStatusByAppId200Response buildsGetStatusByAppId(ownerName, appName)



Application specific build service status

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.BuildApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.buildsGetStatusByAppId(ownerName, appName, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**BuildsGetStatusByAppId200Response**](BuildsGetStatusByAppId200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildsListBranches

> [BuildsListBranches200ResponseInner] buildsListBranches(ownerName, appName)



Returns the list of Git branches for this application

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.BuildApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.buildsListBranches(ownerName, appName, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**[BuildsListBranches200ResponseInner]**](BuildsListBranches200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildsListByBranch

> [BuildsListBranches200ResponseInnerLastBuild] buildsListByBranch(branch, ownerName, appName)



Returns the list of builds for the branch

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.BuildApi();
let branch = "branch_example"; // String | The branch name
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.buildsListByBranch(branch, ownerName, appName, (error, data, response) => {
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
 **branch** | **String**| The branch name | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**[BuildsListBranches200ResponseInnerLastBuild]**](BuildsListBranches200ResponseInnerLastBuild.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildsListToolsetProjects

> BuildsListToolsetProjects200Response buildsListToolsetProjects(branch, os, platform, ownerName, appName, opts)



Returns the projects in the repository for the branch, for all toolsets

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.BuildApi();
let branch = "branch_example"; // String | The branch name
let os = "os_example"; // String | The desired OS for the project scan; normally the same as the app OS
let platform = "platform_example"; // String | The desired platform for the project scan
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'maxSearchDepth': 56 // Number | The depth of the repository to search for project files
};
apiInstance.buildsListToolsetProjects(branch, os, platform, ownerName, appName, opts, (error, data, response) => {
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
 **branch** | **String**| The branch name | 
 **os** | **String**| The desired OS for the project scan; normally the same as the app OS | 
 **platform** | **String**| The desired platform for the project scan | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **maxSearchDepth** | **Number**| The depth of the repository to search for project files | [optional] 

### Return type

[**BuildsListToolsetProjects200Response**](BuildsListToolsetProjects200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildsListToolsets

> BuildsListToolsets200Response buildsListToolsets(ownerName, appName, opts)



Returns available toolsets for application

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.BuildApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'tools': "tools_example" // String | Toolset name
};
apiInstance.buildsListToolsets(ownerName, appName, opts, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **tools** | **String**| Toolset name | [optional] 

### Return type

[**BuildsListToolsets200Response**](BuildsListToolsets200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildsListXamarinSDKBundles

> [BuildsListToolsets200ResponseXamarinInner] buildsListXamarinSDKBundles(ownerName, appName)



Gets the Xamarin SDK bundles available to this app

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.BuildApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.buildsListXamarinSDKBundles(ownerName, appName, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**[BuildsListToolsets200ResponseXamarinInner]**](BuildsListToolsets200ResponseXamarinInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildsListXcodeVersions

> [BuildsListToolsets200ResponseXcodeInner] buildsListXcodeVersions(ownerName, appName)



Gets the Xcode versions available to this app

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.BuildApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.buildsListXcodeVersions(ownerName, appName, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**[BuildsListToolsets200ResponseXcodeInner]**](BuildsListToolsets200ResponseXcodeInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildsUpdate

> BuildsListBranches200ResponseInnerLastBuild buildsUpdate(buildId, ownerName, appName, buildsUpdateRequest)



Cancels a build

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.BuildApi();
let buildId = 56; // Number | The build ID
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let buildsUpdateRequest = new AppCenterClient.BuildsUpdateRequest(); // BuildsUpdateRequest | 
apiInstance.buildsUpdate(buildId, ownerName, appName, buildsUpdateRequest, (error, data, response) => {
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
 **buildId** | **Number**| The build ID | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **buildsUpdateRequest** | [**BuildsUpdateRequest**](BuildsUpdateRequest.md)|  | 

### Return type

[**BuildsListBranches200ResponseInnerLastBuild**](BuildsListBranches200ResponseInnerLastBuild.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## buildsWebhook

> buildsWebhook(opts)



Public webhook sink

### Example

```javascript
import AppCenterClient from 'app_center_client';

let apiInstance = new AppCenterClient.BuildApi();
let opts = {
  'body': {key: null} // Object | 
};
apiInstance.buildsWebhook(opts, (error, data, response) => {
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
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## commitsListByShaList

> [CommitsListByShaList200ResponseInner] commitsListByShaList(hashes, ownerName, appName)



Returns commit information for a batch of shas

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.BuildApi();
let hashes = ["null"]; // [String] | A collection of commit SHAs comma-delimited
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.commitsListByShaList(hashes, ownerName, appName, (error, data, response) => {
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
 **hashes** | [**[String]**](String.md)| A collection of commit SHAs comma-delimited | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**[CommitsListByShaList200ResponseInner]**](CommitsListByShaList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fileAssetsCreate

> FileAssetsCreate200Response fileAssetsCreate(ownerName, appName, opts)



Create a new asset to upload a file

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.BuildApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'body': {key: null} // Object | 
};
apiInstance.fileAssetsCreate(ownerName, appName, opts, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **body** | **Object**|  | [optional] 

### Return type

[**FileAssetsCreate200Response**](FileAssetsCreate200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## repositoriesList

> [RepositoriesList200ResponseInner] repositoriesList(sourceHost, ownerName, appName, opts)



Gets the repositories available from the source code host

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.BuildApi();
let sourceHost = "sourceHost_example"; // String | The source host
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'vstsAccountName': "vstsAccountName_example", // String | Filter repositories only for specified account and project, \"vstsProjectId\" is required
  'vstsProjectId': "vstsProjectId_example", // String | Filter repositories only for specified account and project, \"vstsAccountName\" is required
  'serviceConnectionId': "serviceConnectionId_example", // String | The id of the service connection (private). Required for GitLab self-hosted repositories
  'form': "form_example" // String | The selected form of the object
};
apiInstance.repositoriesList(sourceHost, ownerName, appName, opts, (error, data, response) => {
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
 **sourceHost** | **String**| The source host | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **vstsAccountName** | **String**| Filter repositories only for specified account and project, \&quot;vstsProjectId\&quot; is required | [optional] 
 **vstsProjectId** | **String**| Filter repositories only for specified account and project, \&quot;vstsAccountName\&quot; is required | [optional] 
 **serviceConnectionId** | **String**| The id of the service connection (private). Required for GitLab self-hosted repositories | [optional] 
 **form** | **String**| The selected form of the object | [optional] 

### Return type

[**[RepositoriesList200ResponseInner]**](RepositoriesList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoryConfigurationsCreateOrUpdate

> BranchConfigurationsDelete200Response repositoryConfigurationsCreateOrUpdate(ownerName, appName, repositoryConfigurationsCreateOrUpdateRequest)



Configures the repository for build

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.BuildApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let repositoryConfigurationsCreateOrUpdateRequest = new AppCenterClient.RepositoryConfigurationsCreateOrUpdateRequest(); // RepositoryConfigurationsCreateOrUpdateRequest | The repository information
apiInstance.repositoryConfigurationsCreateOrUpdate(ownerName, appName, repositoryConfigurationsCreateOrUpdateRequest, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **repositoryConfigurationsCreateOrUpdateRequest** | [**RepositoryConfigurationsCreateOrUpdateRequest**](RepositoryConfigurationsCreateOrUpdateRequest.md)| The repository information | 

### Return type

[**BranchConfigurationsDelete200Response**](BranchConfigurationsDelete200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## repositoryConfigurationsDelete

> BranchConfigurationsDelete200Response repositoryConfigurationsDelete(ownerName, appName)



Removes the configuration for the repository

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.BuildApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.repositoryConfigurationsDelete(ownerName, appName, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**BranchConfigurationsDelete200Response**](BranchConfigurationsDelete200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## repositoryConfigurationsList

> [RepositoryConfigurationsList200ResponseInner] repositoryConfigurationsList(ownerName, appName, opts)



Returns the repository build configuration status of the app

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.BuildApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'includeInactive': true // Boolean | Include inactive configurations if none are active
};
apiInstance.repositoryConfigurationsList(ownerName, appName, opts, (error, data, response) => {
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
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **includeInactive** | **Boolean**| Include inactive configurations if none are active | [optional] 

### Return type

[**[RepositoryConfigurationsList200ResponseInner]**](RepositoryConfigurationsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

