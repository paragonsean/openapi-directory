# BlueprintClient.PublishedArtifactApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**publishedArtifactsGet**](PublishedArtifactApi.md#publishedArtifactsGet) | **GET** /{scope}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/versions/{versionId}/artifacts/{artifactName} | 
[**publishedArtifactsList**](PublishedArtifactApi.md#publishedArtifactsList) | **GET** /{scope}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/versions/{versionId}/artifacts | 



## publishedArtifactsGet

> Artifact publishedArtifactsGet(apiVersion, scope, blueprintName, versionId, artifactName)



Get an artifact for a published blueprint definition.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.PublishedArtifactApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
let blueprintName = "blueprintName_example"; // String | Name of the blueprint definition.
let versionId = "versionId_example"; // String | Version of the published blueprint definition.
let artifactName = "artifactName_example"; // String | Name of the blueprint artifact.
apiInstance.publishedArtifactsGet(apiVersion, scope, blueprintName, versionId, artifactName, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | 
 **scope** | **String**| The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use. | 
 **blueprintName** | **String**| Name of the blueprint definition. | 
 **versionId** | **String**| Version of the published blueprint definition. | 
 **artifactName** | **String**| Name of the blueprint artifact. | 

### Return type

[**Artifact**](Artifact.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## publishedArtifactsList

> ArtifactList publishedArtifactsList(apiVersion, scope, blueprintName, versionId)



List artifacts for a version of a published blueprint definition.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.PublishedArtifactApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
let blueprintName = "blueprintName_example"; // String | Name of the blueprint definition.
let versionId = "versionId_example"; // String | Version of the published blueprint definition.
apiInstance.publishedArtifactsList(apiVersion, scope, blueprintName, versionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API Version. | 
 **scope** | **String**| The scope of the resource. Valid scopes are: management group (format: &#39;/providers/Microsoft.Management/managementGroups/{managementGroup}&#39;), subscription (format: &#39;/subscriptions/{subscriptionId}&#39;). For blueprint assignments management group scope is reserved for future use. | 
 **blueprintName** | **String**| Name of the blueprint definition. | 
 **versionId** | **String**| Version of the published blueprint definition. | 

### Return type

[**ArtifactList**](ArtifactList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

