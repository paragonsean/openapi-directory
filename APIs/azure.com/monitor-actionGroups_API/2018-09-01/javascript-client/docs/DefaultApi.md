# AzureActionGroups.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**actionGroupsCreateOrUpdate**](DefaultApi.md#actionGroupsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/actionGroups/{actionGroupName} | 
[**actionGroupsDelete**](DefaultApi.md#actionGroupsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/actionGroups/{actionGroupName} | 
[**actionGroupsEnableReceiver**](DefaultApi.md#actionGroupsEnableReceiver) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/actionGroups/{actionGroupName}/subscribe | 
[**actionGroupsGet**](DefaultApi.md#actionGroupsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/actionGroups/{actionGroupName} | 
[**actionGroupsListByResourceGroup**](DefaultApi.md#actionGroupsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/actionGroups | 
[**actionGroupsListBySubscriptionId**](DefaultApi.md#actionGroupsListBySubscriptionId) | **GET** /subscriptions/{subscriptionId}/providers/microsoft.insights/actionGroups | 
[**actionGroupsUpdate**](DefaultApi.md#actionGroupsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/actionGroups/{actionGroupName} | 



## actionGroupsCreateOrUpdate

> ActionGroupResource actionGroupsCreateOrUpdate(resourceGroupName, actionGroupName, subscriptionId, apiVersion, actionGroup)



Create a new action group or update an existing one.

### Example

```javascript
import AzureActionGroups from 'azure_action_groups';
let defaultClient = AzureActionGroups.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureActionGroups.DefaultApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let actionGroupName = "actionGroupName_example"; // String | The name of the action group.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let actionGroup = new AzureActionGroups.ActionGroupResource(); // ActionGroupResource | The action group to create or use for the update.
apiInstance.actionGroupsCreateOrUpdate(resourceGroupName, actionGroupName, subscriptionId, apiVersion, actionGroup, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **actionGroupName** | **String**| The name of the action group. | 
 **subscriptionId** | **String**| The Azure subscription Id. | 
 **apiVersion** | **String**| Client Api Version. | 
 **actionGroup** | [**ActionGroupResource**](ActionGroupResource.md)| The action group to create or use for the update. | 

### Return type

[**ActionGroupResource**](ActionGroupResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## actionGroupsDelete

> actionGroupsDelete(resourceGroupName, actionGroupName, subscriptionId, apiVersion)



Delete an action group.

### Example

```javascript
import AzureActionGroups from 'azure_action_groups';
let defaultClient = AzureActionGroups.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureActionGroups.DefaultApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let actionGroupName = "actionGroupName_example"; // String | The name of the action group.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.actionGroupsDelete(resourceGroupName, actionGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **actionGroupName** | **String**| The name of the action group. | 
 **subscriptionId** | **String**| The Azure subscription Id. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## actionGroupsEnableReceiver

> actionGroupsEnableReceiver(resourceGroupName, actionGroupName, subscriptionId, apiVersion, enableRequest)



Enable a receiver in an action group. This changes the receiver&#39;s status from Disabled to Enabled. This operation is only supported for Email or SMS receivers.

### Example

```javascript
import AzureActionGroups from 'azure_action_groups';
let defaultClient = AzureActionGroups.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureActionGroups.DefaultApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let actionGroupName = "actionGroupName_example"; // String | The name of the action group.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let enableRequest = new AzureActionGroups.EnableRequest(); // EnableRequest | The receiver to re-enable.
apiInstance.actionGroupsEnableReceiver(resourceGroupName, actionGroupName, subscriptionId, apiVersion, enableRequest, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **actionGroupName** | **String**| The name of the action group. | 
 **subscriptionId** | **String**| The Azure subscription Id. | 
 **apiVersion** | **String**| Client Api Version. | 
 **enableRequest** | [**EnableRequest**](EnableRequest.md)| The receiver to re-enable. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## actionGroupsGet

> ActionGroupResource actionGroupsGet(resourceGroupName, actionGroupName, subscriptionId, apiVersion)



Get an action group.

### Example

```javascript
import AzureActionGroups from 'azure_action_groups';
let defaultClient = AzureActionGroups.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureActionGroups.DefaultApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let actionGroupName = "actionGroupName_example"; // String | The name of the action group.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.actionGroupsGet(resourceGroupName, actionGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **actionGroupName** | **String**| The name of the action group. | 
 **subscriptionId** | **String**| The Azure subscription Id. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**ActionGroupResource**](ActionGroupResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## actionGroupsListByResourceGroup

> ActionGroupList actionGroupsListByResourceGroup(resourceGroupName, subscriptionId, apiVersion)



Get a list of all action groups in a resource group.

### Example

```javascript
import AzureActionGroups from 'azure_action_groups';
let defaultClient = AzureActionGroups.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureActionGroups.DefaultApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.actionGroupsListByResourceGroup(resourceGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **subscriptionId** | **String**| The Azure subscription Id. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**ActionGroupList**](ActionGroupList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## actionGroupsListBySubscriptionId

> ActionGroupList actionGroupsListBySubscriptionId(subscriptionId, apiVersion)



Get a list of all action groups in a subscription.

### Example

```javascript
import AzureActionGroups from 'azure_action_groups';
let defaultClient = AzureActionGroups.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureActionGroups.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.actionGroupsListBySubscriptionId(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription Id. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**ActionGroupList**](ActionGroupList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## actionGroupsUpdate

> ActionGroupResource actionGroupsUpdate(subscriptionId, resourceGroupName, actionGroupName, apiVersion, actionGroupPatch)



Updates an existing action group&#39;s tags. To update other fields use the CreateOrUpdate method.

### Example

```javascript
import AzureActionGroups from 'azure_action_groups';
let defaultClient = AzureActionGroups.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureActionGroups.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The Azure subscription Id.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let actionGroupName = "actionGroupName_example"; // String | The name of the action group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let actionGroupPatch = new AzureActionGroups.ActionGroupPatchBody(); // ActionGroupPatchBody | Parameters supplied to the operation.
apiInstance.actionGroupsUpdate(subscriptionId, resourceGroupName, actionGroupName, apiVersion, actionGroupPatch, (error, data, response) => {
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
 **subscriptionId** | **String**| The Azure subscription Id. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **actionGroupName** | **String**| The name of the action group. | 
 **apiVersion** | **String**| Client Api Version. | 
 **actionGroupPatch** | [**ActionGroupPatchBody**](ActionGroupPatchBody.md)| Parameters supplied to the operation. | 

### Return type

[**ActionGroupResource**](ActionGroupResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

