# ManagementLockClient.ManagementLocksApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**managementLocksCreateOrUpdateAtResourceGroupLevel**](ManagementLocksApi.md#managementLocksCreateOrUpdateAtResourceGroupLevel) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Authorization/locks/{lockName} | 
[**managementLocksCreateOrUpdateAtResourceLevel**](ManagementLocksApi.md#managementLocksCreateOrUpdateAtResourceLevel) | **PUT** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}/providers/Microsoft.Authorization/locks/{lockName} | 
[**managementLocksCreateOrUpdateAtSubscriptionLevel**](ManagementLocksApi.md#managementLocksCreateOrUpdateAtSubscriptionLevel) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/locks/{lockName} | 
[**managementLocksDeleteAtResourceGroupLevel**](ManagementLocksApi.md#managementLocksDeleteAtResourceGroupLevel) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Authorization/locks/{lockName} | 
[**managementLocksDeleteAtResourceLevel**](ManagementLocksApi.md#managementLocksDeleteAtResourceLevel) | **DELETE** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}/providers/Microsoft.Authorization/locks/{lockName} | 
[**managementLocksDeleteAtSubscriptionLevel**](ManagementLocksApi.md#managementLocksDeleteAtSubscriptionLevel) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/locks/{lockName} | 
[**managementLocksGet**](ManagementLocksApi.md#managementLocksGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/locks/{lockName} | 
[**managementLocksGetAtResourceGroupLevel**](ManagementLocksApi.md#managementLocksGetAtResourceGroupLevel) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Authorization/locks/{lockName} | 
[**managementLocksListAtResourceGroupLevel**](ManagementLocksApi.md#managementLocksListAtResourceGroupLevel) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Authorization/locks | 
[**managementLocksListAtResourceLevel**](ManagementLocksApi.md#managementLocksListAtResourceLevel) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{parentResourcePath}/{resourceType}/{resourceName}/providers/Microsoft.Authorization/locks | 
[**managementLocksListAtSubscriptionLevel**](ManagementLocksApi.md#managementLocksListAtSubscriptionLevel) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/locks | 



## managementLocksCreateOrUpdateAtResourceGroupLevel

> ManagementLockObject managementLocksCreateOrUpdateAtResourceGroupLevel(resourceGroupName, lockName, apiVersion, subscriptionId, parameters)



Create or update a management lock at the resource group level.

### Example

```javascript
import ManagementLockClient from 'management_lock_client';
let defaultClient = ManagementLockClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementLockClient.ManagementLocksApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let lockName = "lockName_example"; // String | The lock name.
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
 **resourceGroupName** | **String**| The resource group name. | 
 **lockName** | **String**| The lock name. | 
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



Create or update a management lock at the resource level or any level below resource.

### Example

```javascript
import ManagementLockClient from 'management_lock_client';
let defaultClient = ManagementLockClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementLockClient.ManagementLocksApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. 
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | Resource identity.
let parentResourcePath = "parentResourcePath_example"; // String | Resource identity.
let resourceType = "resourceType_example"; // String | Resource identity.
let resourceName = "resourceName_example"; // String | Resource identity.
let lockName = "lockName_example"; // String | The name of lock.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let parameters = new ManagementLockClient.ManagementLockObject(); // ManagementLockObject | Create or update management lock parameters.
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
 **resourceGroupName** | **String**| The name of the resource group.  | 
 **resourceProviderNamespace** | **String**| Resource identity. | 
 **parentResourcePath** | **String**| Resource identity. | 
 **resourceType** | **String**| Resource identity. | 
 **resourceName** | **String**| Resource identity. | 
 **lockName** | **String**| The name of lock. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **parameters** | [**ManagementLockObject**](ManagementLockObject.md)| Create or update management lock parameters. | 

### Return type

[**ManagementLockObject**](ManagementLockObject.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## managementLocksCreateOrUpdateAtSubscriptionLevel

> ManagementLockObject managementLocksCreateOrUpdateAtSubscriptionLevel(lockName, apiVersion, subscriptionId, parameters)



Create or update a management lock at the subscription level.

### Example

```javascript
import ManagementLockClient from 'management_lock_client';
let defaultClient = ManagementLockClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementLockClient.ManagementLocksApi();
let lockName = "lockName_example"; // String | The name of lock.
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
 **lockName** | **String**| The name of lock. | 
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


## managementLocksDeleteAtResourceGroupLevel

> managementLocksDeleteAtResourceGroupLevel(resourceGroupName, lockName, apiVersion, subscriptionId)



Deletes the management lock of a resource group.

### Example

```javascript
import ManagementLockClient from 'management_lock_client';
let defaultClient = ManagementLockClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementLockClient.ManagementLocksApi();
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let lockName = "lockName_example"; // String | The name of lock.
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
 **resourceGroupName** | **String**| The resource group name. | 
 **lockName** | **String**| The name of lock. | 
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



Deletes the management lock of a resource or any level below resource.

### Example

```javascript
import ManagementLockClient from 'management_lock_client';
let defaultClient = ManagementLockClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementLockClient.ManagementLocksApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. 
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | Resource identity.
let parentResourcePath = "parentResourcePath_example"; // String | Resource identity.
let resourceType = "resourceType_example"; // String | Resource identity.
let resourceName = "resourceName_example"; // String | Resource identity.
let lockName = "lockName_example"; // String | The name of lock.
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
 **resourceGroupName** | **String**| The name of the resource group.  | 
 **resourceProviderNamespace** | **String**| Resource identity. | 
 **parentResourcePath** | **String**| Resource identity. | 
 **resourceType** | **String**| Resource identity. | 
 **resourceName** | **String**| Resource identity. | 
 **lockName** | **String**| The name of lock. | 
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



Deletes the management lock of a subscription.

### Example

```javascript
import ManagementLockClient from 'management_lock_client';
let defaultClient = ManagementLockClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementLockClient.ManagementLocksApi();
let lockName = "lockName_example"; // String | The name of lock.
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
 **lockName** | **String**| The name of lock. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## managementLocksGet

> ManagementLockObject managementLocksGet(lockName, apiVersion, subscriptionId)



Gets the management lock of a scope.

### Example

```javascript
import ManagementLockClient from 'management_lock_client';
let defaultClient = ManagementLockClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementLockClient.ManagementLocksApi();
let lockName = "lockName_example"; // String | Name of the management lock.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.managementLocksGet(lockName, apiVersion, subscriptionId, (error, data, response) => {
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
 **lockName** | **String**| Name of the management lock. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**ManagementLockObject**](ManagementLockObject.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


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
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let lockName = "lockName_example"; // String | The lock name.
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
 **resourceGroupName** | **String**| The resource group name. | 
 **lockName** | **String**| The lock name. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**ManagementLockObject**](ManagementLockObject.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## managementLocksListAtResourceGroupLevel

> ManagementLockListResult managementLocksListAtResourceGroupLevel(resourceGroupName, apiVersion, subscriptionId, opts)



Gets all the management locks of a resource group.

### Example

```javascript
import ManagementLockClient from 'management_lock_client';
let defaultClient = ManagementLockClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementLockClient.ManagementLocksApi();
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
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
 **resourceGroupName** | **String**| Resource group name. | 
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



Gets all the management locks of a resource or any level below resource.

### Example

```javascript
import ManagementLockClient from 'management_lock_client';
let defaultClient = ManagementLockClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagementLockClient.ManagementLocksApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let resourceProviderNamespace = "resourceProviderNamespace_example"; // String | Resource identity.
let parentResourcePath = "parentResourcePath_example"; // String | Resource identity.
let resourceType = "resourceType_example"; // String | Resource identity.
let resourceName = "resourceName_example"; // String | Resource identity.
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **resourceProviderNamespace** | **String**| Resource identity. | 
 **parentResourcePath** | **String**| Resource identity. | 
 **resourceType** | **String**| Resource identity. | 
 **resourceName** | **String**| Resource identity. | 
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



Gets all the management locks of a subscription.

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

