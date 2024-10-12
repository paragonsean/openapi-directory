# ManagedApplicationClient.AppliancesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appliancesCreateOrUpdate**](AppliancesApi.md#appliancesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Solutions/appliances/{applianceName} | 
[**appliancesCreateOrUpdateById**](AppliancesApi.md#appliancesCreateOrUpdateById) | **PUT** /{applianceId} | 
[**appliancesDelete**](AppliancesApi.md#appliancesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Solutions/appliances/{applianceName} | 
[**appliancesDeleteById**](AppliancesApi.md#appliancesDeleteById) | **DELETE** /{applianceId} | 
[**appliancesGet**](AppliancesApi.md#appliancesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Solutions/appliances/{applianceName} | 
[**appliancesGetById**](AppliancesApi.md#appliancesGetById) | **GET** /{applianceId} | 
[**appliancesListByResourceGroup**](AppliancesApi.md#appliancesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Solutions/appliances | 
[**appliancesListBySubscription**](AppliancesApi.md#appliancesListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Solutions/appliances | 
[**appliancesUpdate**](AppliancesApi.md#appliancesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Solutions/appliances/{applianceName} | 
[**appliancesUpdateById**](AppliancesApi.md#appliancesUpdateById) | **PATCH** /{applianceId} | 



## appliancesCreateOrUpdate

> Appliance appliancesCreateOrUpdate(resourceGroupName, applianceName, apiVersion, subscriptionId, parameters)



Creates a new appliance.

### Example

```javascript
import ManagedApplicationClient from 'managed_application_client';
let defaultClient = ManagedApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedApplicationClient.AppliancesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let applianceName = "applianceName_example"; // String | The name of the appliance.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let parameters = new ManagedApplicationClient.Appliance(); // Appliance | Parameters supplied to the create or update an appliance.
apiInstance.appliancesCreateOrUpdate(resourceGroupName, applianceName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **applianceName** | **String**| The name of the appliance. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **parameters** | [**Appliance**](Appliance.md)| Parameters supplied to the create or update an appliance. | 

### Return type

[**Appliance**](Appliance.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appliancesCreateOrUpdateById

> Appliance appliancesCreateOrUpdateById(applianceId, apiVersion, parameters)



Creates a new appliance.

### Example

```javascript
import ManagedApplicationClient from 'managed_application_client';
let defaultClient = ManagedApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedApplicationClient.AppliancesApi();
let applianceId = "applianceId_example"; // String | The fully qualified ID of the appliance, including the appliance name and the appliance resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/appliances/{appliance-name}
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let parameters = new ManagedApplicationClient.Appliance(); // Appliance | Parameters supplied to the create or update an appliance.
apiInstance.appliancesCreateOrUpdateById(applianceId, apiVersion, parameters, (error, data, response) => {
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
 **applianceId** | **String**| The fully qualified ID of the appliance, including the appliance name and the appliance resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/appliances/{appliance-name} | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **parameters** | [**Appliance**](Appliance.md)| Parameters supplied to the create or update an appliance. | 

### Return type

[**Appliance**](Appliance.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appliancesDelete

> appliancesDelete(resourceGroupName, applianceName, apiVersion, subscriptionId)



Deletes the appliance.

### Example

```javascript
import ManagedApplicationClient from 'managed_application_client';
let defaultClient = ManagedApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedApplicationClient.AppliancesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let applianceName = "applianceName_example"; // String | The name of the appliance.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.appliancesDelete(resourceGroupName, applianceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **applianceName** | **String**| The name of the appliance. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appliancesDeleteById

> appliancesDeleteById(applianceId, apiVersion)



Deletes the appliance.

### Example

```javascript
import ManagedApplicationClient from 'managed_application_client';
let defaultClient = ManagedApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedApplicationClient.AppliancesApi();
let applianceId = "applianceId_example"; // String | The fully qualified ID of the appliance, including the appliance name and the appliance resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/appliances/{appliance-name}
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.appliancesDeleteById(applianceId, apiVersion, (error, data, response) => {
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
 **applianceId** | **String**| The fully qualified ID of the appliance, including the appliance name and the appliance resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/appliances/{appliance-name} | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appliancesGet

> Appliance appliancesGet(resourceGroupName, applianceName, apiVersion, subscriptionId)



Gets the appliance.

### Example

```javascript
import ManagedApplicationClient from 'managed_application_client';
let defaultClient = ManagedApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedApplicationClient.AppliancesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let applianceName = "applianceName_example"; // String | The name of the appliance.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.appliancesGet(resourceGroupName, applianceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **applianceName** | **String**| The name of the appliance. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**Appliance**](Appliance.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appliancesGetById

> Appliance appliancesGetById(applianceId, apiVersion)



Gets the appliance.

### Example

```javascript
import ManagedApplicationClient from 'managed_application_client';
let defaultClient = ManagedApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedApplicationClient.AppliancesApi();
let applianceId = "applianceId_example"; // String | The fully qualified ID of the appliance, including the appliance name and the appliance resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/appliances/{appliance-name}
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.appliancesGetById(applianceId, apiVersion, (error, data, response) => {
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
 **applianceId** | **String**| The fully qualified ID of the appliance, including the appliance name and the appliance resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/appliances/{appliance-name} | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

[**Appliance**](Appliance.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appliancesListByResourceGroup

> ApplianceListResult appliancesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Gets all the appliances within a resource group.

### Example

```javascript
import ManagedApplicationClient from 'managed_application_client';
let defaultClient = ManagedApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedApplicationClient.AppliancesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.appliancesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**ApplianceListResult**](ApplianceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appliancesListBySubscription

> ApplianceListResult appliancesListBySubscription(apiVersion, subscriptionId)



Gets all the appliances within a subscription.

### Example

```javascript
import ManagedApplicationClient from 'managed_application_client';
let defaultClient = ManagedApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedApplicationClient.AppliancesApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.appliancesListBySubscription(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**ApplianceListResult**](ApplianceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appliancesUpdate

> Appliance appliancesUpdate(resourceGroupName, applianceName, apiVersion, subscriptionId, opts)



Updates an existing appliance. The only value that can be updated via PATCH currently is the tags.

### Example

```javascript
import ManagedApplicationClient from 'managed_application_client';
let defaultClient = ManagedApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedApplicationClient.AppliancesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let applianceName = "applianceName_example"; // String | The name of the appliance.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let opts = {
  'parameters': new ManagedApplicationClient.Appliance() // Appliance | Parameters supplied to update an existing appliance.
};
apiInstance.appliancesUpdate(resourceGroupName, applianceName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **applianceName** | **String**| The name of the appliance. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **parameters** | [**Appliance**](Appliance.md)| Parameters supplied to update an existing appliance. | [optional] 

### Return type

[**Appliance**](Appliance.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appliancesUpdateById

> Appliance appliancesUpdateById(applianceId, apiVersion, opts)



Updates an existing appliance. The only value that can be updated via PATCH currently is the tags.

### Example

```javascript
import ManagedApplicationClient from 'managed_application_client';
let defaultClient = ManagedApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedApplicationClient.AppliancesApi();
let applianceId = "applianceId_example"; // String | The fully qualified ID of the appliance, including the appliance name and the appliance resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/appliances/{appliance-name}
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let opts = {
  'parameters': new ManagedApplicationClient.Appliance() // Appliance | Parameters supplied to update an existing appliance.
};
apiInstance.appliancesUpdateById(applianceId, apiVersion, opts, (error, data, response) => {
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
 **applianceId** | **String**| The fully qualified ID of the appliance, including the appliance name and the appliance resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/appliances/{appliance-name} | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **parameters** | [**Appliance**](Appliance.md)| Parameters supplied to update an existing appliance. | [optional] 

### Return type

[**Appliance**](Appliance.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

