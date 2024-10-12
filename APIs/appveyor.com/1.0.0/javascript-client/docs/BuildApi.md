# AppVeyorRestApi.BuildApi

All URIs are relative to *https://ci.appveyor.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelBuild**](BuildApi.md#cancelBuild) | **DELETE** /builds/{accountName}/{projectSlug}/{buildVersion} | Cancel build
[**getBuildArtifact**](BuildApi.md#getBuildArtifact) | **GET** /buildjobs/{jobId}/artifacts/{artifactFileName} | Download build artifact
[**getBuildArtifacts**](BuildApi.md#getBuildArtifacts) | **GET** /buildjobs/{jobId}/artifacts | Get build artifacts
[**getBuildLog**](BuildApi.md#getBuildLog) | **GET** /buildjobs/{jobId}/log | Download build log
[**reRunBuild**](BuildApi.md#reRunBuild) | **PUT** /builds | Re-run build
[**startBuild**](BuildApi.md#startBuild) | **POST** /builds | Start build of branch most recent commit



## cancelBuild

> cancelBuild(accountName, projectSlug, buildVersion)

Cancel build

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.BuildApi();
let accountName = "accountName_example"; // String | AppVeyor account name on which to operate. Accounts for which a user has access are listed on the [Security page of the user profile](https://ci.appveyor.com/security) (when logged in). The user account is also the `accountName` property of `UserAccount`.
let projectSlug = "projectSlug_example"; // String | Project Slug
let buildVersion = "buildVersion_example"; // String | Build Version (`version` property of `Build`)
apiInstance.cancelBuild(accountName, projectSlug, buildVersion, (error, data, response) => {
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
 **buildVersion** | **String**| Build Version (&#x60;version&#x60; property of &#x60;Build&#x60;) | 

### Return type

null (empty response body)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getBuildArtifact

> File getBuildArtifact(jobId, artifactFileName)

Download build artifact

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';

let apiInstance = new AppVeyorRestApi.BuildApi();
let jobId = "jobId_example"; // String | Build ID (`jobId` property of `BuildJob`)
let artifactFileName = "artifactFileName_example"; // String | File name (or path) of a build artifact file. Corresponds to the `fileName` property of `ArtifactModel`. URL-encoding of slashes in parameter values is optional.
apiInstance.getBuildArtifact(jobId, artifactFileName, (error, data, response) => {
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
 **jobId** | **String**| Build ID (&#x60;jobId&#x60; property of &#x60;BuildJob&#x60;) | 
 **artifactFileName** | **String**| File name (or path) of a build artifact file. Corresponds to the &#x60;fileName&#x60; property of &#x60;ArtifactModel&#x60;. URL-encoding of slashes in parameter values is optional. | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## getBuildArtifacts

> [ArtifactModel] getBuildArtifacts(jobId)

Get build artifacts

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';

let apiInstance = new AppVeyorRestApi.BuildApi();
let jobId = "jobId_example"; // String | Build ID (`jobId` property of `BuildJob`)
apiInstance.getBuildArtifacts(jobId, (error, data, response) => {
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
 **jobId** | **String**| Build ID (&#x60;jobId&#x60; property of &#x60;BuildJob&#x60;) | 

### Return type

[**[ArtifactModel]**](ArtifactModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getBuildLog

> File getBuildLog(jobId)

Download build log

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';

let apiInstance = new AppVeyorRestApi.BuildApi();
let jobId = "jobId_example"; // String | Build ID (`jobId` property of `BuildJob`)
apiInstance.getBuildLog(jobId, (error, data, response) => {
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
 **jobId** | **String**| Build ID (&#x60;jobId&#x60; property of &#x60;BuildJob&#x60;) | 

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream


## reRunBuild

> Build reRunBuild(body)

Re-run build

If &#x60;reRunIncomplete&#x60; is &#x60;true&#x60; and all jobs in the referenced build completed successfully, a 500 Internal Server Error is returned with the message \&quot;No failed or cancelled jobs in build with ID {buildId}\&quot;.

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.BuildApi();
let body = new AppVeyorRestApi.ReRunBuildRequest(); // ReRunBuildRequest | 
apiInstance.reRunBuild(body, (error, data, response) => {
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
 **body** | [**ReRunBuildRequest**](ReRunBuildRequest.md)|  | 

### Return type

[**Build**](Build.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml


## startBuild

> Build startBuild(body)

Start build of branch most recent commit

### Example

```javascript
import AppVeyorRestApi from 'app_veyor_rest_api';
let defaultClient = AppVeyorRestApi.ApiClient.instance;
// Configure API key authorization: apiToken
let apiToken = defaultClient.authentications['apiToken'];
apiToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiToken.apiKeyPrefix = 'Token';

let apiInstance = new AppVeyorRestApi.BuildApi();
let body = new AppVeyorRestApi.BuildStartRequest(); // BuildStartRequest | 
apiInstance.startBuild(body, (error, data, response) => {
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
 **body** | [**BuildStartRequest**](BuildStartRequest.md)|  | 

### Return type

[**Build**](Build.md)

### Authorization

[apiToken](../README.md#apiToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json, application/xml

