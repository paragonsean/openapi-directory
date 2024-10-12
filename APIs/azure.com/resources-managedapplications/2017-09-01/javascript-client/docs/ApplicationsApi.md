# ApplicationClient.ApplicationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applicationsCreateOrUpdate**](ApplicationsApi.md#applicationsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Solutions/applications/{applicationName} | 
[**applicationsCreateOrUpdateById**](ApplicationsApi.md#applicationsCreateOrUpdateById) | **PUT** /{applicationId} | 
[**applicationsDelete**](ApplicationsApi.md#applicationsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Solutions/applications/{applicationName} | 
[**applicationsDeleteById**](ApplicationsApi.md#applicationsDeleteById) | **DELETE** /{applicationId} | 
[**applicationsGet**](ApplicationsApi.md#applicationsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Solutions/applications/{applicationName} | 
[**applicationsGetById**](ApplicationsApi.md#applicationsGetById) | **GET** /{applicationId} | 
[**applicationsListByResourceGroup**](ApplicationsApi.md#applicationsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Solutions/applications | 
[**applicationsListBySubscription**](ApplicationsApi.md#applicationsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Solutions/applications | 
[**applicationsUpdate**](ApplicationsApi.md#applicationsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Solutions/applications/{applicationName} | 
[**applicationsUpdateById**](ApplicationsApi.md#applicationsUpdateById) | **PATCH** /{applicationId} | 



## applicationsCreateOrUpdate

> Application applicationsCreateOrUpdate(resourceGroupName, applicationName, apiVersion, subscriptionId, parameters)



Creates a new managed application.

### Example

```javascript
import ApplicationClient from 'application_client';
let defaultClient = ApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationClient.ApplicationsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let applicationName = "applicationName_example"; // String | The name of the managed application.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let parameters = new ApplicationClient.Application(); // Application | Parameters supplied to the create or update a managed application.
apiInstance.applicationsCreateOrUpdate(resourceGroupName, applicationName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **applicationName** | **String**| The name of the managed application. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **parameters** | [**Application**](Application.md)| Parameters supplied to the create or update a managed application. | 

### Return type

[**Application**](Application.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## applicationsCreateOrUpdateById

> Application applicationsCreateOrUpdateById(applicationId, apiVersion, parameters)



Creates a new managed application.

### Example

```javascript
import ApplicationClient from 'application_client';
let defaultClient = ApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationClient.ApplicationsApi();
let applicationId = "applicationId_example"; // String | The fully qualified ID of the managed application, including the managed application name and the managed application resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/applications/{application-name}
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let parameters = new ApplicationClient.Application(); // Application | Parameters supplied to the create or update a managed application.
apiInstance.applicationsCreateOrUpdateById(applicationId, apiVersion, parameters, (error, data, response) => {
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
 **applicationId** | **String**| The fully qualified ID of the managed application, including the managed application name and the managed application resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/applications/{application-name} | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **parameters** | [**Application**](Application.md)| Parameters supplied to the create or update a managed application. | 

### Return type

[**Application**](Application.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## applicationsDelete

> applicationsDelete(resourceGroupName, applicationName, apiVersion, subscriptionId)



Deletes the managed application.

### Example

```javascript
import ApplicationClient from 'application_client';
let defaultClient = ApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationClient.ApplicationsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let applicationName = "applicationName_example"; // String | The name of the managed application.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.applicationsDelete(resourceGroupName, applicationName, apiVersion, subscriptionId, (error, data, response) => {
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
 **applicationName** | **String**| The name of the managed application. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationsDeleteById

> applicationsDeleteById(applicationId, apiVersion)



Deletes the managed application.

### Example

```javascript
import ApplicationClient from 'application_client';
let defaultClient = ApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationClient.ApplicationsApi();
let applicationId = "applicationId_example"; // String | The fully qualified ID of the managed application, including the managed application name and the managed application resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/applications/{application-name}
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.applicationsDeleteById(applicationId, apiVersion, (error, data, response) => {
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
 **applicationId** | **String**| The fully qualified ID of the managed application, including the managed application name and the managed application resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/applications/{application-name} | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationsGet

> Application applicationsGet(resourceGroupName, applicationName, apiVersion, subscriptionId)



Gets the managed application.

### Example

```javascript
import ApplicationClient from 'application_client';
let defaultClient = ApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationClient.ApplicationsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let applicationName = "applicationName_example"; // String | The name of the managed application.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.applicationsGet(resourceGroupName, applicationName, apiVersion, subscriptionId, (error, data, response) => {
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
 **applicationName** | **String**| The name of the managed application. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**Application**](Application.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationsGetById

> Application applicationsGetById(applicationId, apiVersion)



Gets the managed application.

### Example

```javascript
import ApplicationClient from 'application_client';
let defaultClient = ApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationClient.ApplicationsApi();
let applicationId = "applicationId_example"; // String | The fully qualified ID of the managed application, including the managed application name and the managed application resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/applications/{application-name}
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
apiInstance.applicationsGetById(applicationId, apiVersion, (error, data, response) => {
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
 **applicationId** | **String**| The fully qualified ID of the managed application, including the managed application name and the managed application resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/applications/{application-name} | 
 **apiVersion** | **String**| The API version to use for this operation. | 

### Return type

[**Application**](Application.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationsListByResourceGroup

> ApplicationListResult applicationsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Gets all the applications within a resource group.

### Example

```javascript
import ApplicationClient from 'application_client';
let defaultClient = ApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationClient.ApplicationsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.applicationsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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

[**ApplicationListResult**](ApplicationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationsListBySubscription

> ApplicationListResult applicationsListBySubscription(apiVersion, subscriptionId)



Gets all the applications within a subscription.

### Example

```javascript
import ApplicationClient from 'application_client';
let defaultClient = ApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationClient.ApplicationsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.applicationsListBySubscription(apiVersion, subscriptionId, (error, data, response) => {
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

[**ApplicationListResult**](ApplicationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationsUpdate

> Application applicationsUpdate(resourceGroupName, applicationName, apiVersion, subscriptionId, opts)



Updates an existing managed application. The only value that can be updated via PATCH currently is the tags.

### Example

```javascript
import ApplicationClient from 'application_client';
let defaultClient = ApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationClient.ApplicationsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let applicationName = "applicationName_example"; // String | The name of the managed application.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let opts = {
  'parameters': new ApplicationClient.Application() // Application | Parameters supplied to update an existing managed application.
};
apiInstance.applicationsUpdate(resourceGroupName, applicationName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **applicationName** | **String**| The name of the managed application. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **parameters** | [**Application**](Application.md)| Parameters supplied to update an existing managed application. | [optional] 

### Return type

[**Application**](Application.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## applicationsUpdateById

> Application applicationsUpdateById(applicationId, apiVersion, opts)



Updates an existing managed application. The only value that can be updated via PATCH currently is the tags.

### Example

```javascript
import ApplicationClient from 'application_client';
let defaultClient = ApplicationClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ApplicationClient.ApplicationsApi();
let applicationId = "applicationId_example"; // String | The fully qualified ID of the managed application, including the managed application name and the managed application resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/applications/{application-name}
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let opts = {
  'parameters': new ApplicationClient.Application() // Application | Parameters supplied to update an existing managed application.
};
apiInstance.applicationsUpdateById(applicationId, apiVersion, opts, (error, data, response) => {
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
 **applicationId** | **String**| The fully qualified ID of the managed application, including the managed application name and the managed application resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/applications/{application-name} | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **parameters** | [**Application**](Application.md)| Parameters supplied to update an existing managed application. | [optional] 

### Return type

[**Application**](Application.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

