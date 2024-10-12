# BlueprintClient.BlueprintApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**blueprintsCreateOrUpdate**](BlueprintApi.md#blueprintsCreateOrUpdate) | **PUT** /providers/Microsoft.Management/managementGroups/{managementGroupName}/providers/Microsoft.Blueprint/blueprints/{blueprintName} | 
[**blueprintsDelete**](BlueprintApi.md#blueprintsDelete) | **DELETE** /providers/Microsoft.Management/managementGroups/{managementGroupName}/providers/Microsoft.Blueprint/blueprints/{blueprintName} | 
[**blueprintsGet**](BlueprintApi.md#blueprintsGet) | **GET** /providers/Microsoft.Management/managementGroups/{managementGroupName}/providers/Microsoft.Blueprint/blueprints/{blueprintName} | 
[**blueprintsList**](BlueprintApi.md#blueprintsList) | **GET** /providers/Microsoft.Management/managementGroups/{managementGroupName}/providers/Microsoft.Blueprint/blueprints | 



## blueprintsCreateOrUpdate

> Blueprint blueprintsCreateOrUpdate(apiVersion, managementGroupName, blueprintName, blueprint)



Create or update Blueprint definition.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.BlueprintApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let managementGroupName = "managementGroupName_example"; // String | ManagementGroup where blueprint stores.
let blueprintName = "blueprintName_example"; // String | name of the blueprint.
let blueprint = new BlueprintClient.Blueprint(); // Blueprint | Blueprint definition.
apiInstance.blueprintsCreateOrUpdate(apiVersion, managementGroupName, blueprintName, blueprint, (error, data, response) => {
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
 **blueprint** | [**Blueprint**](Blueprint.md)| Blueprint definition. | 

### Return type

[**Blueprint**](Blueprint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## blueprintsDelete

> Blueprint blueprintsDelete(apiVersion, managementGroupName, blueprintName)



Delete a blueprint definition.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.BlueprintApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let managementGroupName = "managementGroupName_example"; // String | ManagementGroup where blueprint stores.
let blueprintName = "blueprintName_example"; // String | name of the blueprint.
apiInstance.blueprintsDelete(apiVersion, managementGroupName, blueprintName, (error, data, response) => {
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

[**Blueprint**](Blueprint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## blueprintsGet

> Blueprint blueprintsGet(apiVersion, managementGroupName, blueprintName)



Get a blueprint definition.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.BlueprintApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let managementGroupName = "managementGroupName_example"; // String | ManagementGroup where blueprint stores.
let blueprintName = "blueprintName_example"; // String | name of the blueprint.
apiInstance.blueprintsGet(apiVersion, managementGroupName, blueprintName, (error, data, response) => {
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

[**Blueprint**](Blueprint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## blueprintsList

> BlueprintList blueprintsList(apiVersion, managementGroupName)



List Blueprint definitions within a Management Group.

### Example

```javascript
import BlueprintClient from 'blueprint_client';
let defaultClient = BlueprintClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BlueprintClient.BlueprintApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let managementGroupName = "managementGroupName_example"; // String | ManagementGroup where blueprint stores.
apiInstance.blueprintsList(apiVersion, managementGroupName, (error, data, response) => {
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

### Return type

[**BlueprintList**](BlueprintList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

