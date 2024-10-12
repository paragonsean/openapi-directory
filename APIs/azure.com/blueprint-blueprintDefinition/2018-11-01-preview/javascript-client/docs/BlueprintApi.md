# BlueprintClient.BlueprintApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**blueprintsCreateOrUpdate**](BlueprintApi.md#blueprintsCreateOrUpdate) | **PUT** /{scope}/providers/Microsoft.Blueprint/blueprints/{blueprintName} | 
[**blueprintsDelete**](BlueprintApi.md#blueprintsDelete) | **DELETE** /{scope}/providers/Microsoft.Blueprint/blueprints/{blueprintName} | 
[**blueprintsGet**](BlueprintApi.md#blueprintsGet) | **GET** /{scope}/providers/Microsoft.Blueprint/blueprints/{blueprintName} | 
[**blueprintsList**](BlueprintApi.md#blueprintsList) | **GET** /{scope}/providers/Microsoft.Blueprint/blueprints | 



## blueprintsCreateOrUpdate

> Blueprint blueprintsCreateOrUpdate(apiVersion, scope, blueprintName, blueprint)



Create or update a blueprint definition.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.BlueprintApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
let blueprintName = "blueprintName_example"; // String | Name of the blueprint definition.
let blueprint = new BlueprintClient.Blueprint(); // Blueprint | Blueprint definition.
apiInstance.blueprintsCreateOrUpdate(apiVersion, scope, blueprintName, blueprint, (error, data, response) => {
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
 **blueprint** | [**Blueprint**](Blueprint.md)| Blueprint definition. | 

### Return type

[**Blueprint**](Blueprint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## blueprintsDelete

> Blueprint blueprintsDelete(apiVersion, scope, blueprintName)



Delete a blueprint definition.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.BlueprintApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
let blueprintName = "blueprintName_example"; // String | Name of the blueprint definition.
apiInstance.blueprintsDelete(apiVersion, scope, blueprintName, (error, data, response) => {
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

[**Blueprint**](Blueprint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## blueprintsGet

> Blueprint blueprintsGet(apiVersion, scope, blueprintName)



Get a blueprint definition.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.BlueprintApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
let blueprintName = "blueprintName_example"; // String | Name of the blueprint definition.
apiInstance.blueprintsGet(apiVersion, scope, blueprintName, (error, data, response) => {
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

[**Blueprint**](Blueprint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## blueprintsList

> BlueprintList blueprintsList(apiVersion, scope)



List blueprint definitions.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.BlueprintApi();
let apiVersion = "apiVersion_example"; // String | Client API Version.
let scope = "scope_example"; // String | The scope of the resource. Valid scopes are: management group (format: '/providers/Microsoft.Management/managementGroups/{managementGroup}'), subscription (format: '/subscriptions/{subscriptionId}'). For blueprint assignments management group scope is reserved for future use.
apiInstance.blueprintsList(apiVersion, scope, (error, data, response) => {
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

### Return type

[**BlueprintList**](BlueprintList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

