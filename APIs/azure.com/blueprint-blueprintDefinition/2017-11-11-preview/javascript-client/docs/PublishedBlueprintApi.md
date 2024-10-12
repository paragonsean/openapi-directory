# BlueprintClient.PublishedBlueprintApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**publishedBlueprintsCreate**](PublishedBlueprintApi.md#publishedBlueprintsCreate) | **PUT** /providers/Microsoft.Management/managementGroups/{managementGroupName}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/versions/{versionId} | 
[**publishedBlueprintsDelete**](PublishedBlueprintApi.md#publishedBlueprintsDelete) | **DELETE** /providers/Microsoft.Management/managementGroups/{managementGroupName}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/versions/{versionId} | 
[**publishedBlueprintsGet**](PublishedBlueprintApi.md#publishedBlueprintsGet) | **GET** /providers/Microsoft.Management/managementGroups/{managementGroupName}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/versions/{versionId} | 
[**publishedBlueprintsList**](PublishedBlueprintApi.md#publishedBlueprintsList) | **GET** /providers/Microsoft.Management/managementGroups/{managementGroupName}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/versions | 



## publishedBlueprintsCreate

> PublishedBlueprint publishedBlueprintsCreate(apiVersion, managementGroupName, blueprintName, versionId)



Publish a new version of the Blueprint with the latest artifacts. Published Blueprints are immutable.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.PublishedBlueprintApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let managementGroupName = "managementGroupName_example"; // String | ManagementGroup where blueprint stores.
let blueprintName = "blueprintName_example"; // String | name of the blueprint.
let versionId = "versionId_example"; // String | version of the published blueprint.
apiInstance.publishedBlueprintsCreate(apiVersion, managementGroupName, blueprintName, versionId, (error, data, response) => {
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

[**PublishedBlueprint**](PublishedBlueprint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## publishedBlueprintsDelete

> PublishedBlueprint publishedBlueprintsDelete(apiVersion, managementGroupName, blueprintName, versionId)



Delete a published Blueprint.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.PublishedBlueprintApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let managementGroupName = "managementGroupName_example"; // String | ManagementGroup where blueprint stores.
let blueprintName = "blueprintName_example"; // String | name of the blueprint.
let versionId = "versionId_example"; // String | version of the published blueprint.
apiInstance.publishedBlueprintsDelete(apiVersion, managementGroupName, blueprintName, versionId, (error, data, response) => {
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

[**PublishedBlueprint**](PublishedBlueprint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## publishedBlueprintsGet

> PublishedBlueprint publishedBlueprintsGet(apiVersion, managementGroupName, blueprintName, versionId)



Get a published Blueprint.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.PublishedBlueprintApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let managementGroupName = "managementGroupName_example"; // String | ManagementGroup where blueprint stores.
let blueprintName = "blueprintName_example"; // String | name of the blueprint.
let versionId = "versionId_example"; // String | version of the published blueprint.
apiInstance.publishedBlueprintsGet(apiVersion, managementGroupName, blueprintName, versionId, (error, data, response) => {
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

[**PublishedBlueprint**](PublishedBlueprint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## publishedBlueprintsList

> PublishedBlueprintList publishedBlueprintsList(apiVersion, managementGroupName, blueprintName)



List published versions of given Blueprint.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.PublishedBlueprintApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let managementGroupName = "managementGroupName_example"; // String | ManagementGroup where blueprint stores.
let blueprintName = "blueprintName_example"; // String | name of the blueprint.
apiInstance.publishedBlueprintsList(apiVersion, managementGroupName, blueprintName, (error, data, response) => {
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

[**PublishedBlueprintList**](PublishedBlueprintList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

