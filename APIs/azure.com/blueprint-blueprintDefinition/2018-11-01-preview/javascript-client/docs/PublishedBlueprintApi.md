# BlueprintClient.PublishedBlueprintApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**publishedBlueprintsCreate**](PublishedBlueprintApi.md#publishedBlueprintsCreate) | **PUT** /{scope}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/versions/{versionId} | 
[**publishedBlueprintsDelete**](PublishedBlueprintApi.md#publishedBlueprintsDelete) | **DELETE** /{scope}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/versions/{versionId} | 
[**publishedBlueprintsGet**](PublishedBlueprintApi.md#publishedBlueprintsGet) | **GET** /{scope}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/versions/{versionId} | 
[**publishedBlueprintsList**](PublishedBlueprintApi.md#publishedBlueprintsList) | **GET** /{scope}/providers/Microsoft.Blueprint/blueprints/{blueprintName}/versions | 



## publishedBlueprintsCreate

> PublishedBlueprint publishedBlueprintsCreate(apiVersion, scope, blueprintName, versionId, opts)



Publish a new version of the blueprint definition with the latest artifacts. Published blueprint definitions are immutable.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.PublishedBlueprintApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
let blueprintName = "blueprintName_example"; // String | Name of the blueprint definition.
let versionId = "versionId_example"; // String | Version of the published blueprint definition.
let opts = {
  'publishedBlueprint': new BlueprintClient.PublishedBlueprint() // PublishedBlueprint | Published Blueprint to create or update.
};
apiInstance.publishedBlueprintsCreate(apiVersion, scope, blueprintName, versionId, opts, (error, data, response) => {
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
 **publishedBlueprint** | [**PublishedBlueprint**](PublishedBlueprint.md)| Published Blueprint to create or update. | [optional] 

### Return type

[**PublishedBlueprint**](PublishedBlueprint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## publishedBlueprintsDelete

> PublishedBlueprint publishedBlueprintsDelete(apiVersion, scope, blueprintName, versionId)



Delete a published version of a blueprint definition.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.PublishedBlueprintApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
let blueprintName = "blueprintName_example"; // String | Name of the blueprint definition.
let versionId = "versionId_example"; // String | Version of the published blueprint definition.
apiInstance.publishedBlueprintsDelete(apiVersion, scope, blueprintName, versionId, (error, data, response) => {
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

[**PublishedBlueprint**](PublishedBlueprint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## publishedBlueprintsGet

> PublishedBlueprint publishedBlueprintsGet(apiVersion, scope, blueprintName, versionId)



Get a published version of a blueprint definition.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.PublishedBlueprintApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
let blueprintName = "blueprintName_example"; // String | Name of the blueprint definition.
let versionId = "versionId_example"; // String | Version of the published blueprint definition.
apiInstance.publishedBlueprintsGet(apiVersion, scope, blueprintName, versionId, (error, data, response) => {
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

[**PublishedBlueprint**](PublishedBlueprint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## publishedBlueprintsList

> PublishedBlueprintList publishedBlueprintsList(apiVersion, scope, blueprintName)



List published versions of given blueprint definition.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.PublishedBlueprintApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
let blueprintName = "blueprintName_example"; // String | Name of the blueprint definition.
apiInstance.publishedBlueprintsList(apiVersion, scope, blueprintName, (error, data, response) => {
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

[**PublishedBlueprintList**](PublishedBlueprintList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

