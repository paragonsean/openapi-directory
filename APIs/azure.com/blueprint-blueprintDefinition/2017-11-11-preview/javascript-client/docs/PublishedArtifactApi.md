# BlueprintClient.PublishedArtifactApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**publishedArtifactsGet**](PublishedArtifactApi.md#publishedArtifactsGet) | **GET** /providers/Microsoft.Management/managementGroups/{managementGroupName}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/versions/{versionId}/artifacts/{artifactName} | 
[**publishedArtifactsList**](PublishedArtifactApi.md#publishedArtifactsList) | **GET** /providers/Microsoft.Management/managementGroups/{managementGroupName}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/versions/{versionId}/artifacts | 



## publishedArtifactsGet

> Artifact publishedArtifactsGet(apiVersion, managementGroupName, blueprintName, versionId, artifactName)



Get an artifact for a published Blueprint.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.PublishedArtifactApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let managementGroupName = "managementGroupName_example"; // String | ManagementGroup where blueprint stores.
let blueprintName = "blueprintName_example"; // String | name of the blueprint.
let versionId = "versionId_example"; // String | version of the published blueprint.
let artifactName = "artifactName_example"; // String | name of the artifact.
apiInstance.publishedArtifactsGet(apiVersion, managementGroupName, blueprintName, versionId, artifactName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **managementGroupName** | **String**| ManagementGroup where blueprint stores. | 
 **blueprintName** | **String**| name of the blueprint. | 
 **versionId** | **String**| version of the published blueprint. | 
 **artifactName** | **String**| name of the artifact. | 

### Return type

[**Artifact**](Artifact.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## publishedArtifactsList

> ArtifactList publishedArtifactsList(apiVersion, managementGroupName, blueprintName, versionId)



List artifacts for a published Blueprint.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.PublishedArtifactApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let managementGroupName = "managementGroupName_example"; // String | ManagementGroup where blueprint stores.
let blueprintName = "blueprintName_example"; // String | name of the blueprint.
let versionId = "versionId_example"; // String | version of the published blueprint.
apiInstance.publishedArtifactsList(apiVersion, managementGroupName, blueprintName, versionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **managementGroupName** | **String**| ManagementGroup where blueprint stores. | 
 **blueprintName** | **String**| name of the blueprint. | 
 **versionId** | **String**| version of the published blueprint. | 

### Return type

[**ArtifactList**](ArtifactList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

