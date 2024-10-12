# BlueprintClient.ArtifactApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**artifactsCreateOrUpdate**](ArtifactApi.md#artifactsCreateOrUpdate) | **PUT** /providers/Microsoft.Management/managementGroups/{managementGroupName}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/artifacts/{artifactName} | 
[**artifactsDelete**](ArtifactApi.md#artifactsDelete) | **DELETE** /providers/Microsoft.Management/managementGroups/{managementGroupName}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/artifacts/{artifactName} | 
[**artifactsGet**](ArtifactApi.md#artifactsGet) | **GET** /providers/Microsoft.Management/managementGroups/{managementGroupName}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/artifacts/{artifactName} | 
[**artifactsList**](ArtifactApi.md#artifactsList) | **GET** /providers/Microsoft.Management/managementGroups/{managementGroupName}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/artifacts | 



## artifactsCreateOrUpdate

> Artifact artifactsCreateOrUpdate(apiVersion, managementGroupName, blueprintName, artifactName, artifact)



Create or update Blueprint artifact.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.ArtifactApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let managementGroupName = "managementGroupName_example"; // String | ManagementGroup where blueprint stores.
let blueprintName = "blueprintName_example"; // String | name of the blueprint.
let artifactName = "artifactName_example"; // String | name of the artifact.
let artifact = new BlueprintClient.Artifact(); // Artifact | Blueprint artifact to save.
apiInstance.artifactsCreateOrUpdate(apiVersion, managementGroupName, blueprintName, artifactName, artifact, (error, data, response) => {
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
 **artifactName** | **String**| name of the artifact. | 
 **artifact** | [**Artifact**](Artifact.md)| Blueprint artifact to save. | 

### Return type

[**Artifact**](Artifact.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## artifactsDelete

> Artifact artifactsDelete(apiVersion, managementGroupName, blueprintName, artifactName)



Delete a Blueprint artifact.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.ArtifactApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let managementGroupName = "managementGroupName_example"; // String | ManagementGroup where blueprint stores.
let blueprintName = "blueprintName_example"; // String | name of the blueprint.
let artifactName = "artifactName_example"; // String | name of the artifact.
apiInstance.artifactsDelete(apiVersion, managementGroupName, blueprintName, artifactName, (error, data, response) => {
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
 **artifactName** | **String**| name of the artifact. | 

### Return type

[**Artifact**](Artifact.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## artifactsGet

> Artifact artifactsGet(apiVersion, managementGroupName, blueprintName, artifactName)



Get a Blueprint artifact.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.ArtifactApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let managementGroupName = "managementGroupName_example"; // String | ManagementGroup where blueprint stores.
let blueprintName = "blueprintName_example"; // String | name of the blueprint.
let artifactName = "artifactName_example"; // String | name of the artifact.
apiInstance.artifactsGet(apiVersion, managementGroupName, blueprintName, artifactName, (error, data, response) => {
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
 **artifactName** | **String**| name of the artifact. | 

### Return type

[**Artifact**](Artifact.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## artifactsList

> ArtifactList artifactsList(apiVersion, managementGroupName, blueprintName)



List artifacts for a given Blueprint.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.ArtifactApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let managementGroupName = "managementGroupName_example"; // String | ManagementGroup where blueprint stores.
let blueprintName = "blueprintName_example"; // String | name of the blueprint.
apiInstance.artifactsList(apiVersion, managementGroupName, blueprintName, (error, data, response) => {
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

### Return type

[**ArtifactList**](ArtifactList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

