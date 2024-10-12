# AppCenterClient.CodepushApi

All URIs are relative to *https://api.appcenter.ms*

Method | HTTP request | Description
------------- | ------------- | -------------
[**codePushAcquisitionGetAcquisitionStatus**](CodepushApi.md#codePushAcquisitionGetAcquisitionStatus) | **GET** /v0.1/public/codepush/status | 
[**codePushAcquisitionUpdateCheck**](CodepushApi.md#codePushAcquisitionUpdateCheck) | **GET** /v0.1/public/codepush/update_check | 
[**codePushAcquisitionUpdateDeployStatus**](CodepushApi.md#codePushAcquisitionUpdateDeployStatus) | **POST** /v0.1/public/codepush/report_status/deploy | 
[**codePushAcquisitionUpdateDownloadStatus**](CodepushApi.md#codePushAcquisitionUpdateDownloadStatus) | **POST** /v0.1/public/codepush/report_status/download | 
[**codePushDeploymentMetricsGet**](CodepushApi.md#codePushDeploymentMetricsGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}/metrics | 
[**codePushDeploymentReleaseRollback**](CodepushApi.md#codePushDeploymentReleaseRollback) | **POST** /v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}/rollback_release | 
[**codePushDeploymentReleasesCreate**](CodepushApi.md#codePushDeploymentReleasesCreate) | **POST** /v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}/releases | 
[**codePushDeploymentReleasesDelete**](CodepushApi.md#codePushDeploymentReleasesDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}/releases | 
[**codePushDeploymentReleasesGet**](CodepushApi.md#codePushDeploymentReleasesGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}/releases | 
[**codePushDeploymentUploadCreate**](CodepushApi.md#codePushDeploymentUploadCreate) | **POST** /v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}/uploads | 
[**codePushDeploymentsCreate**](CodepushApi.md#codePushDeploymentsCreate) | **POST** /v0.1/apps/{owner_name}/{app_name}/deployments | 
[**codePushDeploymentsDelete**](CodepushApi.md#codePushDeploymentsDelete) | **DELETE** /v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name} | 
[**codePushDeploymentsGet**](CodepushApi.md#codePushDeploymentsGet) | **GET** /v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name} | 
[**codePushDeploymentsList**](CodepushApi.md#codePushDeploymentsList) | **GET** /v0.1/apps/{owner_name}/{app_name}/deployments | 
[**codePushDeploymentsPromote**](CodepushApi.md#codePushDeploymentsPromote) | **POST** /v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}/promote_release/{promote_deployment_name} | 
[**codePushDeploymentsUpdate**](CodepushApi.md#codePushDeploymentsUpdate) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name} | 
[**deploymentReleasesUpdate**](CodepushApi.md#deploymentReleasesUpdate) | **PATCH** /v0.1/apps/{owner_name}/{app_name}/deployments/{deployment_name}/releases/{release_label} | 
[**legacyCodePushAcquisitionUpdateCheck**](CodepushApi.md#legacyCodePushAcquisitionUpdateCheck) | **GET** /v0.1/legacy/updateCheck | 
[**legacyCodePushAcquisitionUpdateDownloadStatus**](CodepushApi.md#legacyCodePushAcquisitionUpdateDownloadStatus) | **POST** /v0.1/legacy/reportStatus/download | 
[**legacyCodePushAcquisitionUpdateInstallsStatus**](CodepushApi.md#legacyCodePushAcquisitionUpdateInstallsStatus) | **POST** /v0.1/legacy/reportStatus/deploy | 



## codePushAcquisitionGetAcquisitionStatus

> CodePushAcquisitionGetAcquisitionStatus200Response codePushAcquisitionGetAcquisitionStatus()



Returns the acquisition service status to the caller

### Example

```javascript
import AppCenterClient from 'app_center_client';

let apiInstance = new AppCenterClient.CodepushApi();
apiInstance.codePushAcquisitionGetAcquisitionStatus((error, data, response) => {
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

[**CodePushAcquisitionGetAcquisitionStatus200Response**](CodePushAcquisitionGetAcquisitionStatus200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## codePushAcquisitionUpdateCheck

> CodePushAcquisitionUpdateCheck200Response codePushAcquisitionUpdateCheck(deploymentKey, appVersion, opts)



Check for updates

### Example

```javascript
import AppCenterClient from 'app_center_client';

let apiInstance = new AppCenterClient.CodepushApi();
let deploymentKey = "deploymentKey_example"; // String | 
let appVersion = "appVersion_example"; // String | 
let opts = {
  'packageHash': "packageHash_example", // String | 
  'label': "label_example", // String | 
  'clientUniqueId': "clientUniqueId_example", // String | 
  'isCompanion': true, // Boolean | 
  'previousLabelOrAppVersion': "previousLabelOrAppVersion_example", // String | 
  'previousDeploymentKey': "previousDeploymentKey_example" // String | 
};
apiInstance.codePushAcquisitionUpdateCheck(deploymentKey, appVersion, opts, (error, data, response) => {
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
 **deploymentKey** | **String**|  | 
 **appVersion** | **String**|  | 
 **packageHash** | **String**|  | [optional] 
 **label** | **String**|  | [optional] 
 **clientUniqueId** | **String**|  | [optional] 
 **isCompanion** | **Boolean**|  | [optional] 
 **previousLabelOrAppVersion** | **String**|  | [optional] 
 **previousDeploymentKey** | **String**|  | [optional] 

### Return type

[**CodePushAcquisitionUpdateCheck200Response**](CodePushAcquisitionUpdateCheck200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## codePushAcquisitionUpdateDeployStatus

> codePushAcquisitionUpdateDeployStatus(codePushAcquisitionUpdateDeployStatusRequest)



Report Deployment status metric

### Example

```javascript
import AppCenterClient from 'app_center_client';

let apiInstance = new AppCenterClient.CodepushApi();
let codePushAcquisitionUpdateDeployStatusRequest = new AppCenterClient.CodePushAcquisitionUpdateDeployStatusRequest(); // CodePushAcquisitionUpdateDeployStatusRequest | Deployment status metric properties
apiInstance.codePushAcquisitionUpdateDeployStatus(codePushAcquisitionUpdateDeployStatusRequest, (error, data, response) => {
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
 **codePushAcquisitionUpdateDeployStatusRequest** | [**CodePushAcquisitionUpdateDeployStatusRequest**](CodePushAcquisitionUpdateDeployStatusRequest.md)| Deployment status metric properties | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## codePushAcquisitionUpdateDownloadStatus

> codePushAcquisitionUpdateDownloadStatus(codePushAcquisitionUpdateDeployStatusRequest)



Report download of specified release

### Example

```javascript
import AppCenterClient from 'app_center_client';

let apiInstance = new AppCenterClient.CodepushApi();
let codePushAcquisitionUpdateDeployStatusRequest = new AppCenterClient.CodePushAcquisitionUpdateDeployStatusRequest(); // CodePushAcquisitionUpdateDeployStatusRequest | Deployment status metric properties
apiInstance.codePushAcquisitionUpdateDownloadStatus(codePushAcquisitionUpdateDeployStatusRequest, (error, data, response) => {
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
 **codePushAcquisitionUpdateDeployStatusRequest** | [**CodePushAcquisitionUpdateDeployStatusRequest**](CodePushAcquisitionUpdateDeployStatusRequest.md)| Deployment status metric properties | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## codePushDeploymentMetricsGet

> [CodePushDeploymentMetricsGet200ResponseInner] codePushDeploymentMetricsGet(deploymentName, ownerName, appName)



Gets all releases metrics for specified Deployment

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CodepushApi();
let deploymentName = "deploymentName_example"; // String | deployment name
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.codePushDeploymentMetricsGet(deploymentName, ownerName, appName, (error, data, response) => {
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
 **deploymentName** | **String**| deployment name | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**[CodePushDeploymentMetricsGet200ResponseInner]**](CodePushDeploymentMetricsGet200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## codePushDeploymentReleaseRollback

> CodePushDeploymentsList200ResponseInnerLatestRelease codePushDeploymentReleaseRollback(deploymentName, ownerName, appName, opts)



Rollback the latest or a specific release for an app deployment

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CodepushApi();
let deploymentName = "deploymentName_example"; // String | deployment name
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'codePushDeploymentReleaseRollbackRequest': new AppCenterClient.CodePushDeploymentReleaseRollbackRequest() // CodePushDeploymentReleaseRollbackRequest | The specific release label that you want to rollback to
};
apiInstance.codePushDeploymentReleaseRollback(deploymentName, ownerName, appName, opts, (error, data, response) => {
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
 **deploymentName** | **String**| deployment name | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **codePushDeploymentReleaseRollbackRequest** | [**CodePushDeploymentReleaseRollbackRequest**](CodePushDeploymentReleaseRollbackRequest.md)| The specific release label that you want to rollback to | [optional] 

### Return type

[**CodePushDeploymentsList200ResponseInnerLatestRelease**](CodePushDeploymentsList200ResponseInnerLatestRelease.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## codePushDeploymentReleasesCreate

> CodePushDeploymentsList200ResponseInnerLatestRelease codePushDeploymentReleasesCreate(deploymentName, ownerName, appName, codePushDeploymentReleasesCreateRequest)



Create a new CodePush release for the specified deployment

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CodepushApi();
let deploymentName = "deploymentName_example"; // String | deployment name
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let codePushDeploymentReleasesCreateRequest = new AppCenterClient.CodePushDeploymentReleasesCreateRequest(); // CodePushDeploymentReleasesCreateRequest | The necessary information required to download the bundle and being the release process.
apiInstance.codePushDeploymentReleasesCreate(deploymentName, ownerName, appName, codePushDeploymentReleasesCreateRequest, (error, data, response) => {
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
 **deploymentName** | **String**| deployment name | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **codePushDeploymentReleasesCreateRequest** | [**CodePushDeploymentReleasesCreateRequest**](CodePushDeploymentReleasesCreateRequest.md)| The necessary information required to download the bundle and being the release process. | 

### Return type

[**CodePushDeploymentsList200ResponseInnerLatestRelease**](CodePushDeploymentsList200ResponseInnerLatestRelease.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## codePushDeploymentReleasesDelete

> codePushDeploymentReleasesDelete(deploymentName, ownerName, appName)



Clears a Deployment of releases

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CodepushApi();
let deploymentName = "deploymentName_example"; // String | deployment name
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.codePushDeploymentReleasesDelete(deploymentName, ownerName, appName, (error, data, response) => {
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
 **deploymentName** | **String**| deployment name | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## codePushDeploymentReleasesGet

> [CodePushDeploymentsList200ResponseInnerLatestRelease] codePushDeploymentReleasesGet(deploymentName, ownerName, appName)



Gets the history of releases on a Deployment

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CodepushApi();
let deploymentName = "deploymentName_example"; // String | deployment name
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.codePushDeploymentReleasesGet(deploymentName, ownerName, appName, (error, data, response) => {
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
 **deploymentName** | **String**| deployment name | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**[CodePushDeploymentsList200ResponseInnerLatestRelease]**](CodePushDeploymentsList200ResponseInnerLatestRelease.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## codePushDeploymentUploadCreate

> CodePushDeploymentUploadCreate200Response codePushDeploymentUploadCreate(deploymentName, ownerName, appName)



Create a new CodePush release upload for the specified deployment

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CodepushApi();
let deploymentName = "deploymentName_example"; // String | deployment name
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.codePushDeploymentUploadCreate(deploymentName, ownerName, appName, (error, data, response) => {
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
 **deploymentName** | **String**| deployment name | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**CodePushDeploymentUploadCreate200Response**](CodePushDeploymentUploadCreate200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## codePushDeploymentsCreate

> CodePushDeploymentsList200ResponseInner codePushDeploymentsCreate(ownerName, appName, codePushDeploymentsList200ResponseInner)



Creates a CodePush Deployment for the given app

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CodepushApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let codePushDeploymentsList200ResponseInner = new AppCenterClient.CodePushDeploymentsList200ResponseInner(); // CodePushDeploymentsList200ResponseInner | Deployment to be created
apiInstance.codePushDeploymentsCreate(ownerName, appName, codePushDeploymentsList200ResponseInner, (error, data, response) => {
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
 **codePushDeploymentsList200ResponseInner** | [**CodePushDeploymentsList200ResponseInner**](CodePushDeploymentsList200ResponseInner.md)| Deployment to be created | 

### Return type

[**CodePushDeploymentsList200ResponseInner**](CodePushDeploymentsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## codePushDeploymentsDelete

> codePushDeploymentsDelete(deploymentName, ownerName, appName, opts)



Deletes a CodePush Deployment for the given app

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CodepushApi();
let deploymentName = "deploymentName_example"; // String | deployment name
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'body': {key: null} // Object | 
};
apiInstance.codePushDeploymentsDelete(deploymentName, ownerName, appName, opts, (error, data, response) => {
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
 **deploymentName** | **String**| deployment name | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **body** | **Object**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## codePushDeploymentsGet

> CodePushDeploymentsList200ResponseInner codePushDeploymentsGet(deploymentName, ownerName, appName)



Gets a CodePush Deployment for the given app

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CodepushApi();
let deploymentName = "deploymentName_example"; // String | deployment name
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.codePushDeploymentsGet(deploymentName, ownerName, appName, (error, data, response) => {
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
 **deploymentName** | **String**| deployment name | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 

### Return type

[**CodePushDeploymentsList200ResponseInner**](CodePushDeploymentsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## codePushDeploymentsList

> [CodePushDeploymentsList200ResponseInner] codePushDeploymentsList(ownerName, appName)



Gets a list of CodePush deployments for the given app

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CodepushApi();
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
apiInstance.codePushDeploymentsList(ownerName, appName, (error, data, response) => {
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

[**[CodePushDeploymentsList200ResponseInner]**](CodePushDeploymentsList200ResponseInner.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## codePushDeploymentsPromote

> CodePushDeploymentsList200ResponseInnerLatestRelease codePushDeploymentsPromote(deploymentName, promoteDeploymentName, ownerName, appName, opts)



Promote one release (default latest one) from one deployment to another

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CodepushApi();
let deploymentName = "deploymentName_example"; // String | deployment name
let promoteDeploymentName = "promoteDeploymentName_example"; // String | deployment name
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let opts = {
  'codePushDeploymentsPromoteRequest': new AppCenterClient.CodePushDeploymentsPromoteRequest() // CodePushDeploymentsPromoteRequest | Release to be promoted, only needs to provide optional fields, description, label, disabled, mandatory, rollout, targetBinaryVersion
};
apiInstance.codePushDeploymentsPromote(deploymentName, promoteDeploymentName, ownerName, appName, opts, (error, data, response) => {
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
 **deploymentName** | **String**| deployment name | 
 **promoteDeploymentName** | **String**| deployment name | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **codePushDeploymentsPromoteRequest** | [**CodePushDeploymentsPromoteRequest**](CodePushDeploymentsPromoteRequest.md)| Release to be promoted, only needs to provide optional fields, description, label, disabled, mandatory, rollout, targetBinaryVersion | [optional] 

### Return type

[**CodePushDeploymentsList200ResponseInnerLatestRelease**](CodePushDeploymentsList200ResponseInnerLatestRelease.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## codePushDeploymentsUpdate

> codePushDeploymentsUpdate(deploymentName, ownerName, appName, codePushDeploymentsUpdateRequest)



Modifies a CodePush Deployment for the given app

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CodepushApi();
let deploymentName = "deploymentName_example"; // String | deployment name
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let codePushDeploymentsUpdateRequest = new AppCenterClient.CodePushDeploymentsUpdateRequest(); // CodePushDeploymentsUpdateRequest | Deployment modification. All fields are optional and only provided fields will get updated.
apiInstance.codePushDeploymentsUpdate(deploymentName, ownerName, appName, codePushDeploymentsUpdateRequest, (error, data, response) => {
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
 **deploymentName** | **String**| deployment name | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **codePushDeploymentsUpdateRequest** | [**CodePushDeploymentsUpdateRequest**](CodePushDeploymentsUpdateRequest.md)| Deployment modification. All fields are optional and only provided fields will get updated. | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deploymentReleasesUpdate

> CodePushDeploymentsList200ResponseInnerLatestRelease deploymentReleasesUpdate(deploymentName, releaseLabel, ownerName, appName, deploymentReleasesUpdateRequest)



Modifies a CodePush release metadata under the given Deployment

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CodepushApi();
let deploymentName = "deploymentName_example"; // String | deployment name
let releaseLabel = "releaseLabel_example"; // String | release label
let ownerName = "ownerName_example"; // String | The name of the owner
let appName = "appName_example"; // String | The name of the application
let deploymentReleasesUpdateRequest = new AppCenterClient.DeploymentReleasesUpdateRequest(); // DeploymentReleasesUpdateRequest | Release modification. All fields are optional and only provided fields will get updated.
apiInstance.deploymentReleasesUpdate(deploymentName, releaseLabel, ownerName, appName, deploymentReleasesUpdateRequest, (error, data, response) => {
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
 **deploymentName** | **String**| deployment name | 
 **releaseLabel** | **String**| release label | 
 **ownerName** | **String**| The name of the owner | 
 **appName** | **String**| The name of the application | 
 **deploymentReleasesUpdateRequest** | [**DeploymentReleasesUpdateRequest**](DeploymentReleasesUpdateRequest.md)| Release modification. All fields are optional and only provided fields will get updated. | 

### Return type

[**CodePushDeploymentsList200ResponseInnerLatestRelease**](CodePushDeploymentsList200ResponseInnerLatestRelease.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## legacyCodePushAcquisitionUpdateCheck

> LegacyCodePushAcquisitionUpdateCheck200Response legacyCodePushAcquisitionUpdateCheck(opts)



Check for updates

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CodepushApi();
let opts = {
  'deploymentKey': "deploymentKey_example", // String | 
  'appVersion': "appVersion_example", // String | 
  'packageHash': "packageHash_example", // String | 
  'label': "label_example", // String | 
  'clientUniqueId': "clientUniqueId_example", // String | 
  'isCompanion': "isCompanion_example" // String | 
};
apiInstance.legacyCodePushAcquisitionUpdateCheck(opts, (error, data, response) => {
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
 **deploymentKey** | **String**|  | [optional] 
 **appVersion** | **String**|  | [optional] 
 **packageHash** | **String**|  | [optional] 
 **label** | **String**|  | [optional] 
 **clientUniqueId** | **String**|  | [optional] 
 **isCompanion** | **String**|  | [optional] 

### Return type

[**LegacyCodePushAcquisitionUpdateCheck200Response**](LegacyCodePushAcquisitionUpdateCheck200Response.md)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## legacyCodePushAcquisitionUpdateDownloadStatus

> legacyCodePushAcquisitionUpdateDownloadStatus(legacyCodePushAcquisitionUpdateInstallsStatusRequest)



Report download of specified release

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CodepushApi();
let legacyCodePushAcquisitionUpdateInstallsStatusRequest = new AppCenterClient.LegacyCodePushAcquisitionUpdateInstallsStatusRequest(); // LegacyCodePushAcquisitionUpdateInstallsStatusRequest | Deployment status metric properties
apiInstance.legacyCodePushAcquisitionUpdateDownloadStatus(legacyCodePushAcquisitionUpdateInstallsStatusRequest, (error, data, response) => {
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
 **legacyCodePushAcquisitionUpdateInstallsStatusRequest** | [**LegacyCodePushAcquisitionUpdateInstallsStatusRequest**](LegacyCodePushAcquisitionUpdateInstallsStatusRequest.md)| Deployment status metric properties | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## legacyCodePushAcquisitionUpdateInstallsStatus

> legacyCodePushAcquisitionUpdateInstallsStatus(legacyCodePushAcquisitionUpdateInstallsStatusRequest)



Report deploy of specified release

### Example

```javascript
import AppCenterClient from 'app_center_client';
let defaultClient = AppCenterClient.ApiClient.instance;
// Configure API key authorization: APIToken
let APIToken = defaultClient.authentications['APIToken'];
APIToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//APIToken.apiKeyPrefix = 'Token';

let apiInstance = new AppCenterClient.CodepushApi();
let legacyCodePushAcquisitionUpdateInstallsStatusRequest = new AppCenterClient.LegacyCodePushAcquisitionUpdateInstallsStatusRequest(); // LegacyCodePushAcquisitionUpdateInstallsStatusRequest | Deployment status metric properties
apiInstance.legacyCodePushAcquisitionUpdateInstallsStatus(legacyCodePushAcquisitionUpdateInstallsStatusRequest, (error, data, response) => {
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
 **legacyCodePushAcquisitionUpdateInstallsStatusRequest** | [**LegacyCodePushAcquisitionUpdateInstallsStatusRequest**](LegacyCodePushAcquisitionUpdateInstallsStatusRequest.md)| Deployment status metric properties | 

### Return type

null (empty response body)

### Authorization

[APIToken](../README.md#APIToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

