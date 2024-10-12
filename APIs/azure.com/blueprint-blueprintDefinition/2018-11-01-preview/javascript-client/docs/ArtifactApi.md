# BlueprintClient.ArtifactApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**artifactsCreateOrUpdate**](ArtifactApi.md#artifactsCreateOrUpdate) | **PUT** /{scope}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/artifacts/{artifactName} | 
[**artifactsDelete**](ArtifactApi.md#artifactsDelete) | **DELETE** /{scope}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/artifacts/{artifactName} | 
[**artifactsGet**](ArtifactApi.md#artifactsGet) | **GET** /{scope}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/artifacts/{artifactName} | 
[**artifactsList**](ArtifactApi.md#artifactsList) | **GET** /{scope}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/artifacts | 



## artifactsCreateOrUpdate

> Artifact artifactsCreateOrUpdate(apiVersion, scope, blueprintName, artifactName, artifact)



Create or update blueprint artifact.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.ArtifactApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
let blueprintName = "blueprintName_example"; // String | Name of the blueprint definition.
let artifactName = "artifactName_example"; // String | Name of the blueprint artifact.
let artifact = new BlueprintClient.Artifact(); // Artifact | Blueprint artifact to create or update.
apiInstance.artifactsCreateOrUpdate(apiVersion, scope, blueprintName, artifactName, artifact, (error, data, response) => {
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
 **artifactName** | **String**| Name of the blueprint artifact. | 
 **artifact** | [**Artifact**](Artifact.md)| Blueprint artifact to create or update. | 

### Return type

[**Artifact**](Artifact.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## artifactsDelete

> Artifact artifactsDelete(apiVersion, scope, blueprintName, artifactName)



Delete a blueprint artifact.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.ArtifactApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
let blueprintName = "blueprintName_example"; // String | Name of the blueprint definition.
let artifactName = "artifactName_example"; // String | Name of the blueprint artifact.
apiInstance.artifactsDelete(apiVersion, scope, blueprintName, artifactName, (error, data, response) => {
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
 **artifactName** | **String**| Name of the blueprint artifact. | 

### Return type

[**Artifact**](Artifact.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## artifactsGet

> Artifact artifactsGet(apiVersion, scope, blueprintName, artifactName)



Get a blueprint artifact.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.ArtifactApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
let blueprintName = "blueprintName_example"; // String | Name of the blueprint definition.
let artifactName = "artifactName_example"; // String | Name of the blueprint artifact.
apiInstance.artifactsGet(apiVersion, scope, blueprintName, artifactName, (error, data, response) => {
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
 **artifactName** | **String**| Name of the blueprint artifact. | 

### Return type

[**Artifact**](Artifact.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## artifactsList

> ArtifactList artifactsList(apiVersion, scope, blueprintName)



List artifacts for a given blueprint definition.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.ArtifactApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
let blueprintName = "blueprintName_example"; // String | Name of the blueprint definition.
apiInstance.artifactsList(apiVersion, scope, blueprintName, (error, data, response) => {
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

### Return type

[**ArtifactList**](ArtifactList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

