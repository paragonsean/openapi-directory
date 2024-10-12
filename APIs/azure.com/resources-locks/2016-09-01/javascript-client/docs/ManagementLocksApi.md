# ManagementLockClient.ManagementLocksApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**managementLocksCreateOrUpdateAtResourceGroupLevel**](ManagementLocksApi.md#managementLocksCreateOrUpdateAtResourceGroupLevel) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Authorization/locks/{lockName} | Creates or updates a management lock at the resource group level.
[**managementLocksCreateOrUpdateAtResourceLevel**](ManagementLocksApi.md#managementLocksCreateOrUpdateAtResourceLevel) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}/providers/Microsoft.Authorization/locks/{lockName} | Creates or updates a management lock at the resource level or any level below the resource.
[**managementLocksCreateOrUpdateAtSubscriptionLevel**](ManagementLocksApi.md#managementLocksCreateOrUpdateAtSubscriptionLevel) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/locks/{lockName} | Creates or updates a management lock at the subscription level.
[**managementLocksCreateOrUpdateByScope**](ManagementLocksApi.md#managementLocksCreateOrUpdateByScope) | **PUT** /{scope}/providers/Microsoft.Authorization/locks/{lockName} | 
[**managementLocksDeleteAtResourceGroupLevel**](ManagementLocksApi.md#managementLocksDeleteAtResourceGroupLevel) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Authorization/locks/{lockName} | Deletes a management lock at the resource group level.
[**managementLocksDeleteAtResourceLevel**](ManagementLocksApi.md#managementLocksDeleteAtResourceLevel) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}/providers/Microsoft.Authorization/locks/{lockName} | Deletes the management lock of a resource or any level below the resource.
[**managementLocksDeleteAtSubscriptionLevel**](ManagementLocksApi.md#managementLocksDeleteAtSubscriptionLevel) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/locks/{lockName} | Deletes the management lock at the subscription level.
[**managementLocksDeleteByScope**](ManagementLocksApi.md#managementLocksDeleteByScope) | **DELETE** /{scope}/providers/Microsoft.Authorization/locks/{lockName} | 
[**managementLocksGetAtResourceGroupLevel**](ManagementLocksApi.md#managementLocksGetAtResourceGroupLevel) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Authorization/locks/{lockName} | 
[**managementLocksGetAtResourceLevel**](ManagementLocksApi.md#managementLocksGetAtResourceLevel) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}/providers/Microsoft.Authorization/locks/{lockName} | 
[**managementLocksGetAtSubscriptionLevel**](ManagementLocksApi.md#managementLocksGetAtSubscriptionLevel) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/locks/{lockName} | 
[**managementLocksGetByScope**](ManagementLocksApi.md#managementLocksGetByScope) | **GET** /{scope}/providers/Microsoft.Authorization/locks/{lockName} | 
[**managementLocksListAtResourceGroupLevel**](ManagementLocksApi.md#managementLocksListAtResourceGroupLevel) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Authorization/locks | 
[**managementLocksListAtResourceLevel**](ManagementLocksApi.md#managementLocksListAtResourceLevel) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}/providers/Microsoft.Authorization/locks | 
[**managementLocksListAtSubscriptionLevel**](ManagementLocksApi.md#managementLocksListAtSubscriptionLevel) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/locks | 
[**managementLocksListByScope**](ManagementLocksApi.md#managementLocksListByScope) | **GET** /{scope}/providers/Microsoft.Authorization/locks | 



## managementLocksCreateOrUpdateAtResourceGroupLevel

> ManagementLockObject managementLocksCreateOrUpdateAtResourceGroupLevel(resourceGroupName, lockName, apiVersion, subscriptionId, parameters)

Creates or updates a management lock at the resource group level.

When you apply a lock at a parent scope, all child resources inherit the same lock. To create management locks, you must have access to Microsoft.Authorization/_* or Microsoft.Authorization/locks/_* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.

### Example

```javascript
import ManagementLockClient from 'management_lock_client';
let defaultClient = ManagementLockClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementLockClient.ManagementLocksApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to lock.
let lockName = "lockName_example"; // String | The lock name. The lock name can be a maximum of 260 characters. It cannot contain <, > %, &, :, \\, ?, /, or any control characters.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let parameters = new ManagementLockClient.ManagementLockObject(); // ManagementLockObject | The management lock parameters.
apiInstance.managementLocksCreateOrUpdateAtResourceGroupLevel(resourceGroupName, lockName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group to lock. | 
 **lockName** | **String**| The lock name. The lock name can be a maximum of 260 characters. It cannot contain &lt;, &gt; %, &amp;, :, \\, ?, /, or any control characters. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **parameters** | [**ManagementLockObject**](ManagementLockObject.md)| The management lock parameters. | 

### Return type

[**ManagementLockObject**](ManagementLockObject.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## managementLocksCreateOrUpdateAtResourceLevel

> ManagementLockObject managementLocksCreateOrUpdateAtResourceLevel(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, lockName, apiVersion, subscriptionId, parameters)

Creates or updates a management lock at the resource level or any level below the resource.

When you apply a lock at a parent scope, all child resources inherit the same lock. To create management locks, you must have access to Microsoft.Authorization/_* or Microsoft.Authorization/locks/_* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.

### Example

```javascript
import ManagementLockClient from 'management_lock_client';
let defaultClient = ManagementLockClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementLockClient.ManagementLocksApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the resource to lock. 
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The resource provider namespace of the resource to lock.
let parentResourcePath = "parentResourcePath_example"; // String | The parent resource identity.
let resourceType = "resourceType_example"; // String | The resource type of the resource to lock.
let resourceName = "resourceName_example"; // String | The name of the resource to lock.
let lockName = "lockName_example"; // String | The name of lock. The lock name can be a maximum of 260 characters. It cannot contain <, > %, &, :, \\, ?, /, or any control characters.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let parameters = new ManagementLockClient.ManagementLockObject(); // ManagementLockObject | Parameters for creating or updating a  management lock.
apiInstance.managementLocksCreateOrUpdateAtResourceLevel(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, lockName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the resource to lock.  | 
 **resourceProviderNamespace** | **String**| The resource provider namespace of the resource to lock. | 
 **parentResourcePath** | **String**| The parent resource identity. | 
 **resourceType** | **String**| The resource type of the resource to lock. | 
 **resourceName** | **String**| The name of the resource to lock. | 
 **lockName** | **String**| The name of lock. The lock name can be a maximum of 260 characters. It cannot contain &lt;, &gt; %, &amp;, :, \\, ?, /, or any control characters. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **parameters** | [**ManagementLockObject**](ManagementLockObject.md)| Parameters for creating or updating a  management lock. | 

### Return type

[**ManagementLockObject**](ManagementLockObject.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## managementLocksCreateOrUpdateAtSubscriptionLevel

> ManagementLockObject managementLocksCreateOrUpdateAtSubscriptionLevel(lockName, apiVersion, subscriptionId, parameters)

Creates or updates a management lock at the subscription level.

When you apply a lock at a parent scope, all child resources inherit the same lock. To create management locks, you must have access to Microsoft.Authorization/_* or Microsoft.Authorization/locks/_* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.

### Example

```javascript
import ManagementLockClient from 'management_lock_client';
let defaultClient = ManagementLockClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementLockClient.ManagementLocksApi();
let lockName = "lockName_example"; // String | The name of lock. The lock name can be a maximum of 260 characters. It cannot contain <, > %, &, :, \\, ?, /, or any control characters.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let parameters = new ManagementLockClient.ManagementLockObject(); // ManagementLockObject | The management lock parameters.
apiInstance.managementLocksCreateOrUpdateAtSubscriptionLevel(lockName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **lockName** | **String**| The name of lock. The lock name can be a maximum of 260 characters. It cannot contain &lt;, &gt; %, &amp;, :, \\, ?, /, or any control characters. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **parameters** | [**ManagementLockObject**](ManagementLockObject.md)| The management lock parameters. | 

### Return type

[**ManagementLockObject**](ManagementLockObject.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## managementLocksCreateOrUpdateByScope

> ManagementLockObject managementLocksCreateOrUpdateByScope(scope, lockName, apiVersion, parameters)



Create or update a management lock by scope.

### Example

```javascript
import ManagementLockClient from 'management_lock_client';
let defaultClient = ManagementLockClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementLockClient.ManagementLocksApi();
let scope = "scope_example"; // String | The scope for the lock. When providing a scope for the assignment, use '/subscriptions/{subscriptionId}' for subscriptions, '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}' for resource groups, and '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePathIfPresent}/{resourceType}/{resourceName}' for resources.
let lockName = "lockName_example"; // String | The name of lock.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let parameters = new ManagementLockClient.ManagementLockObject(); // ManagementLockObject | Create or update management lock parameters.
apiInstance.managementLocksCreateOrUpdateByScope(scope, lockName, apiVersion, parameters, (error, data, response) => {
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
 **scope** | **String**| The scope for the lock. When providing a scope for the assignment, use &#39;/subscriptions/{subscriptionId}&#39; for subscriptions, &#39;/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}&#39; for resource groups, and &#39;/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePathIfPresent}/{resourceType}/{resourceName}&#39; for resources. | 
 **lockName** | **String**| The name of lock. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **parameters** | [**ManagementLockObject**](ManagementLockObject.md)| Create or update management lock parameters. | 

### Return type

[**ManagementLockObject**](ManagementLockObject.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## managementLocksDeleteAtResourceGroupLevel

> managementLocksDeleteAtResourceGroupLevel(resourceGroupName, lockName, apiVersion, subscriptionId)

Deletes a management lock at the resource group level.

To delete management locks, you must have access to Microsoft.Authorization/_* or Microsoft.Authorization/locks/_* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.

### Example

```javascript
import ManagementLockClient from 'management_lock_client';
let defaultClient = ManagementLockClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementLockClient.ManagementLocksApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the lock.
let lockName = "lockName_example"; // String | The name of lock to delete.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.managementLocksDeleteAtResourceGroupLevel(resourceGroupName, lockName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the lock. | 
 **lockName** | **String**| The name of lock to delete. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## managementLocksDeleteAtResourceLevel

> managementLocksDeleteAtResourceLevel(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, lockName, apiVersion, subscriptionId)

Deletes the management lock of a resource or any level below the resource.

To delete management locks, you must have access to Microsoft.Authorization/_* or Microsoft.Authorization/locks/_* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.

### Example

```javascript
import ManagementLockClient from 'management_lock_client';
let defaultClient = ManagementLockClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementLockClient.ManagementLocksApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the resource with the lock to delete. 
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The resource provider namespace of the resource with the lock to delete.
let parentResourcePath = "parentResourcePath_example"; // String | The parent resource identity.
let resourceType = "resourceType_example"; // String | The resource type of the resource with the lock to delete.
let resourceName = "resourceName_example"; // String | The name of the resource with the lock to delete.
let lockName = "lockName_example"; // String | The name of the lock to delete.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.managementLocksDeleteAtResourceLevel(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, lockName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the resource with the lock to delete.  | 
 **resourceProviderNamespace** | **String**| The resource provider namespace of the resource with the lock to delete. | 
 **parentResourcePath** | **String**| The parent resource identity. | 
 **resourceType** | **String**| The resource type of the resource with the lock to delete. | 
 **resourceName** | **String**| The name of the resource with the lock to delete. | 
 **lockName** | **String**| The name of the lock to delete. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## managementLocksDeleteAtSubscriptionLevel

> managementLocksDeleteAtSubscriptionLevel(lockName, apiVersion, subscriptionId)

Deletes the management lock at the subscription level.

To delete management locks, you must have access to Microsoft.Authorization/_* or Microsoft.Authorization/locks/_* actions. Of the built-in roles, only Owner and User Access Administrator are granted those actions.

### Example

```javascript
import ManagementLockClient from 'management_lock_client';
let defaultClient = ManagementLockClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementLockClient.ManagementLocksApi();
let lockName = "lockName_example"; // String | The name of lock to delete.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.managementLocksDeleteAtSubscriptionLevel(lockName, apiVersion, subscriptionId, (error, data, response) => {
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
 **lockName** | **String**| The name of lock to delete. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## managementLocksDeleteByScope

> managementLocksDeleteByScope(scope, lockName, apiVersion)



Delete a management lock by scope.

### Example

```javascript
import ManagementLockClient from 'management_lock_client';
let defaultClient = ManagementLockClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementLockClient.ManagementLocksApi();
let scope = "scope_example"; // String | The scope for the lock. 
let lockName = "lockName_example"; // String | The name of lock.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
apiInstance.managementLocksDeleteByScope(scope, lockName, apiVersion, (error, data, response) => {
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
 **scope** | **String**| The scope for the lock.  | 
 **lockName** | **String**| The name of lock. | 
 **apiVersion** | **String**| The API version to use for the operation. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## managementLocksGetAtResourceGroupLevel

> ManagementLockObject managementLocksGetAtResourceGroupLevel(resourceGroupName, lockName, apiVersion, subscriptionId)



Gets a management lock at the resource group level.

### Example

```javascript
import ManagementLockClient from 'management_lock_client';
let defaultClient = ManagementLockClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementLockClient.ManagementLocksApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the locked resource group.
let lockName = "lockName_example"; // String | The name of the lock to get.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.managementLocksGetAtResourceGroupLevel(resourceGroupName, lockName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the locked resource group. | 
 **lockName** | **String**| The name of the lock to get. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**ManagementLockObject**](ManagementLockObject.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## managementLocksGetAtResourceLevel

> ManagementLockObject managementLocksGetAtResourceLevel(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, lockName, apiVersion, subscriptionId)



Get the management lock of a resource or any level below resource.

### Example

```javascript
import ManagementLockClient from 'management_lock_client';
let defaultClient = ManagementLockClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementLockClient.ManagementLocksApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. 
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider.
let parentResourcePath = "parentResourcePath_example"; // String | An extra path parameter needed in some services, like SQL Databases.
let resourceType = "resourceType_example"; // String | The type of the resource.
let resourceName = "resourceName_example"; // String | The name of the resource.
let lockName = "lockName_example"; // String | The name of lock.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.managementLocksGetAtResourceLevel(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, lockName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group.  | 
 **resourceProviderNamespace** | **String**| The namespace of the resource provider. | 
 **parentResourcePath** | **String**| An extra path parameter needed in some services, like SQL Databases. | 
 **resourceType** | **String**| The type of the resource. | 
 **resourceName** | **String**| The name of the resource. | 
 **lockName** | **String**| The name of lock. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**ManagementLockObject**](ManagementLockObject.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## managementLocksGetAtSubscriptionLevel

> ManagementLockObject managementLocksGetAtSubscriptionLevel(lockName, apiVersion, subscriptionId)



Gets a management lock at the subscription level.

### Example

```javascript
import ManagementLockClient from 'management_lock_client';
let defaultClient = ManagementLockClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementLockClient.ManagementLocksApi();
let lockName = "lockName_example"; // String | The name of the lock to get.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.managementLocksGetAtSubscriptionLevel(lockName, apiVersion, subscriptionId, (error, data, response) => {
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
 **lockName** | **String**| The name of the lock to get. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**ManagementLockObject**](ManagementLockObject.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## managementLocksGetByScope

> ManagementLockObject managementLocksGetByScope(scope, lockName, apiVersion)



Get a management lock by scope.

### Example

```javascript
import ManagementLockClient from 'management_lock_client';
let defaultClient = ManagementLockClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementLockClient.ManagementLocksApi();
let scope = "scope_example"; // String | The scope for the lock. 
let lockName = "lockName_example"; // String | The name of lock.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
apiInstance.managementLocksGetByScope(scope, lockName, apiVersion, (error, data, response) => {
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
 **scope** | **String**| The scope for the lock.  | 
 **lockName** | **String**| The name of lock. | 
 **apiVersion** | **String**| The API version to use for the operation. | 

### Return type

[**ManagementLockObject**](ManagementLockObject.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## managementLocksListAtResourceGroupLevel

> ManagementLockListResult managementLocksListAtResourceGroupLevel(resourceGroupName, apiVersion, subscriptionId, opts)



Gets all the management locks for a resource group.

### Example

```javascript
import ManagementLockClient from 'management_lock_client';
let defaultClient = ManagementLockClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementLockClient.ManagementLocksApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the locks to get.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the operation.
};
apiInstance.managementLocksListAtResourceGroupLevel(resourceGroupName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the locks to get. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **filter** | **String**| The filter to apply on the operation. | [optional] 

### Return type

[**ManagementLockListResult**](ManagementLockListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## managementLocksListAtResourceLevel

> ManagementLockListResult managementLocksListAtResourceLevel(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId, opts)



Gets all the management locks for a resource or any level below resource.

### Example

```javascript
import ManagementLockClient from 'management_lock_client';
let defaultClient = ManagementLockClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementLockClient.ManagementLocksApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the locked resource. The name is case insensitive.
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | The namespace of the resource provider.
let parentResourcePath = "parentResourcePath_example"; // String | The parent resource identity.
let resourceType = "resourceType_example"; // String | The resource type of the locked resource.
let resourceName = "resourceName_example"; // String | The name of the locked resource.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the operation.
};
apiInstance.managementLocksListAtResourceLevel(resourceGroupName, resourceProviderNamespace, parentResourcePath, resourceType, resourceName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the locked resource. The name is case insensitive. | 
 **resourceProviderNamespace** | **String**| The namespace of the resource provider. | 
 **parentResourcePath** | **String**| The parent resource identity. | 
 **resourceType** | **String**| The resource type of the locked resource. | 
 **resourceName** | **String**| The name of the locked resource. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **filter** | **String**| The filter to apply on the operation. | [optional] 

### Return type

[**ManagementLockListResult**](ManagementLockListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## managementLocksListAtSubscriptionLevel

> ManagementLockListResult managementLocksListAtSubscriptionLevel(apiVersion, subscriptionId, opts)



Gets all the management locks for a subscription.

### Example

```javascript
import ManagementLockClient from 'management_lock_client';
let defaultClient = ManagementLockClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementLockClient.ManagementLocksApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the operation.
};
apiInstance.managementLocksListAtSubscriptionLevel(apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for the operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **filter** | **String**| The filter to apply on the operation. | [optional] 

### Return type

[**ManagementLockListResult**](ManagementLockListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## managementLocksListByScope

> ManagementLockListResult managementLocksListByScope(scope, apiVersion, opts)



Gets all the management locks for a scope.

### Example

```javascript
import ManagementLockClient from 'management_lock_client';
let defaultClient = ManagementLockClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementLockClient.ManagementLocksApi();
let scope = "scope_example"; // String | The scope for the lock. When providing a scope for the assignment, use '/subscriptions/{subscriptionId}' for subscriptions, '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}' for resource groups, and '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePathIfPresent}/{resourceType}/{resourceName}' for resources.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the operation.
};
apiInstance.managementLocksListByScope(scope, apiVersion, opts, (error, data, response) => {
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
 **scope** | **String**| The scope for the lock. When providing a scope for the assignment, use &#39;/subscriptions/{subscriptionId}&#39; for subscriptions, &#39;/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}&#39; for resource groups, and &#39;/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePathIfPresent}/{resourceType}/{resourceName}&#39; for resources. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **filter** | **String**| The filter to apply on the operation. | [optional] 

### Return type

[**ManagementLockListResult**](ManagementLockListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

