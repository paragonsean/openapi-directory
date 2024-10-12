# RemediationsClient.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**remediationsCancelAtManagementGroup**](DefaultApi.md#remediationsCancelAtManagementGroup) | **POST** /providers/{managementGroupsNamespace}/managementGroups/{managementGroupId}/providers/Microsoft.PolicyInsights/remediations/{remediationName}/cancel | 
[**remediationsCancelAtResource**](DefaultApi.md#remediationsCancelAtResource) | **POST** /{resourceId}/providers/Microsoft.PolicyInsights/remediations/{remediationName}/cancel | 
[**remediationsCancelAtResourceGroup**](DefaultApi.md#remediationsCancelAtResourceGroup) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PolicyInsights/remediations/{remediationName}/cancel | 
[**remediationsCancelAtSubscription**](DefaultApi.md#remediationsCancelAtSubscription) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.PolicyInsights/remediations/{remediationName}/cancel | 
[**remediationsCreateOrUpdateAtManagementGroup**](DefaultApi.md#remediationsCreateOrUpdateAtManagementGroup) | **PUT** /providers/{managementGroupsNamespace}/managementGroups/{managementGroupId}/providers/Microsoft.PolicyInsights/remediations/{remediationName} | 
[**remediationsCreateOrUpdateAtResource**](DefaultApi.md#remediationsCreateOrUpdateAtResource) | **PUT** /{resourceId}/providers/Microsoft.PolicyInsights/remediations/{remediationName} | 
[**remediationsCreateOrUpdateAtResourceGroup**](DefaultApi.md#remediationsCreateOrUpdateAtResourceGroup) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PolicyInsights/remediations/{remediationName} | 
[**remediationsCreateOrUpdateAtSubscription**](DefaultApi.md#remediationsCreateOrUpdateAtSubscription) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.PolicyInsights/remediations/{remediationName} | 
[**remediationsDeleteAtManagementGroup**](DefaultApi.md#remediationsDeleteAtManagementGroup) | **DELETE** /providers/{managementGroupsNamespace}/managementGroups/{managementGroupId}/providers/Microsoft.PolicyInsights/remediations/{remediationName} | 
[**remediationsDeleteAtResource**](DefaultApi.md#remediationsDeleteAtResource) | **DELETE** /{resourceId}/providers/Microsoft.PolicyInsights/remediations/{remediationName} | 
[**remediationsDeleteAtResourceGroup**](DefaultApi.md#remediationsDeleteAtResourceGroup) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PolicyInsights/remediations/{remediationName} | 
[**remediationsDeleteAtSubscription**](DefaultApi.md#remediationsDeleteAtSubscription) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.PolicyInsights/remediations/{remediationName} | 
[**remediationsGetAtManagementGroup**](DefaultApi.md#remediationsGetAtManagementGroup) | **GET** /providers/{managementGroupsNamespace}/managementGroups/{managementGroupId}/providers/Microsoft.PolicyInsights/remediations/{remediationName} | 
[**remediationsGetAtResource**](DefaultApi.md#remediationsGetAtResource) | **GET** /{resourceId}/providers/Microsoft.PolicyInsights/remediations/{remediationName} | 
[**remediationsGetAtResourceGroup**](DefaultApi.md#remediationsGetAtResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PolicyInsights/remediations/{remediationName} | 
[**remediationsGetAtSubscription**](DefaultApi.md#remediationsGetAtSubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.PolicyInsights/remediations/{remediationName} | 
[**remediationsListDeploymentsAtManagementGroup**](DefaultApi.md#remediationsListDeploymentsAtManagementGroup) | **POST** /providers/{managementGroupsNamespace}/managementGroups/{managementGroupId}/providers/Microsoft.PolicyInsights/remediations/{remediationName}/listDeployments | 
[**remediationsListDeploymentsAtResource**](DefaultApi.md#remediationsListDeploymentsAtResource) | **POST** /{resourceId}/providers/Microsoft.PolicyInsights/remediations/{remediationName}/listDeployments | 
[**remediationsListDeploymentsAtResourceGroup**](DefaultApi.md#remediationsListDeploymentsAtResourceGroup) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PolicyInsights/remediations/{remediationName}/listDeployments | 
[**remediationsListDeploymentsAtSubscription**](DefaultApi.md#remediationsListDeploymentsAtSubscription) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.PolicyInsights/remediations/{remediationName}/listDeployments | 
[**remediationsListForManagementGroup**](DefaultApi.md#remediationsListForManagementGroup) | **GET** /providers/{managementGroupsNamespace}/managementGroups/{managementGroupId}/providers/Microsoft.PolicyInsights/remediations | 
[**remediationsListForResource**](DefaultApi.md#remediationsListForResource) | **GET** /{resourceId}/providers/Microsoft.PolicyInsights/remediations | 
[**remediationsListForResourceGroup**](DefaultApi.md#remediationsListForResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.PolicyInsights/remediations | 
[**remediationsListForSubscription**](DefaultApi.md#remediationsListForSubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.PolicyInsights/remediations | 



## remediationsCancelAtManagementGroup

> Remediation remediationsCancelAtManagementGroup(managementGroupsNamespace, managementGroupId, remediationName, apiVersion)



Cancels a remediation at management group scope.

### Example

```javascript
import RemediationsClient from 'remediations_client';
let defaultClient = RemediationsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RemediationsClient.DefaultApi();
let managementGroupsNamespace = "managementGroupsNamespace_example"; // String | The namespace for Microsoft Management RP; only \"Microsoft.Management\" is allowed.
let managementGroupId = "managementGroupId_example"; // String | Management group ID.
let remediationName = "remediationName_example"; // String | The name of the remediation.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.remediationsCancelAtManagementGroup(managementGroupsNamespace, managementGroupId, remediationName, apiVersion, (error, data, response) => {
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
 **managementGroupsNamespace** | **String**| The namespace for Microsoft Management RP; only \&quot;Microsoft.Management\&quot; is allowed. | 
 **managementGroupId** | **String**| Management group ID. | 
 **remediationName** | **String**| The name of the remediation. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**Remediation**](Remediation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## remediationsCancelAtResource

> Remediation remediationsCancelAtResource(resourceId, remediationName, apiVersion)



Cancel a remediation at resource scope.

### Example

```javascript
import RemediationsClient from 'remediations_client';
let defaultClient = RemediationsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RemediationsClient.DefaultApi();
let resourceId = "resourceId_example"; // String | Resource ID.
let remediationName = "remediationName_example"; // String | The name of the remediation.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.remediationsCancelAtResource(resourceId, remediationName, apiVersion, (error, data, response) => {
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
 **resourceId** | **String**| Resource ID. | 
 **remediationName** | **String**| The name of the remediation. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**Remediation**](Remediation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## remediationsCancelAtResourceGroup

> Remediation remediationsCancelAtResourceGroup(subscriptionId, resourceGroupName, remediationName, apiVersion)



Cancels a remediation at resource group scope.

### Example

```javascript
import RemediationsClient from 'remediations_client';
let defaultClient = RemediationsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RemediationsClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let remediationName = "remediationName_example"; // String | The name of the remediation.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.remediationsCancelAtResourceGroup(subscriptionId, resourceGroupName, remediationName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| Resource group name. | 
 **remediationName** | **String**| The name of the remediation. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**Remediation**](Remediation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## remediationsCancelAtSubscription

> Remediation remediationsCancelAtSubscription(subscriptionId, remediationName, apiVersion)



Cancels a remediation at subscription scope.

### Example

```javascript
import RemediationsClient from 'remediations_client';
let defaultClient = RemediationsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RemediationsClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
let remediationName = "remediationName_example"; // String | The name of the remediation.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.remediationsCancelAtSubscription(subscriptionId, remediationName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Microsoft Azure subscription ID. | 
 **remediationName** | **String**| The name of the remediation. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**Remediation**](Remediation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## remediationsCreateOrUpdateAtManagementGroup

> Remediation remediationsCreateOrUpdateAtManagementGroup(managementGroupsNamespace, managementGroupId, remediationName, apiVersion, parameters)



Creates or updates a remediation at management group scope.

### Example

```javascript
import RemediationsClient from 'remediations_client';
let defaultClient = RemediationsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RemediationsClient.DefaultApi();
let managementGroupsNamespace = "managementGroupsNamespace_example"; // String | The namespace for Microsoft Management RP; only \"Microsoft.Management\" is allowed.
let managementGroupId = "managementGroupId_example"; // String | Management group ID.
let remediationName = "remediationName_example"; // String | The name of the remediation.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new RemediationsClient.Remediation(); // Remediation | The remediation parameters.
apiInstance.remediationsCreateOrUpdateAtManagementGroup(managementGroupsNamespace, managementGroupId, remediationName, apiVersion, parameters, (error, data, response) => {
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
 **managementGroupsNamespace** | **String**| The namespace for Microsoft Management RP; only \&quot;Microsoft.Management\&quot; is allowed. | 
 **managementGroupId** | **String**| Management group ID. | 
 **remediationName** | **String**| The name of the remediation. | 
 **apiVersion** | **String**| Client Api Version. | 
 **parameters** | [**Remediation**](Remediation.md)| The remediation parameters. | 

### Return type

[**Remediation**](Remediation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## remediationsCreateOrUpdateAtResource

> Remediation remediationsCreateOrUpdateAtResource(resourceId, remediationName, apiVersion, parameters)



Creates or updates a remediation at resource scope.

### Example

```javascript
import RemediationsClient from 'remediations_client';
let defaultClient = RemediationsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RemediationsClient.DefaultApi();
let resourceId = "resourceId_example"; // String | Resource ID.
let remediationName = "remediationName_example"; // String | The name of the remediation.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new RemediationsClient.Remediation(); // Remediation | The remediation parameters.
apiInstance.remediationsCreateOrUpdateAtResource(resourceId, remediationName, apiVersion, parameters, (error, data, response) => {
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
 **resourceId** | **String**| Resource ID. | 
 **remediationName** | **String**| The name of the remediation. | 
 **apiVersion** | **String**| Client Api Version. | 
 **parameters** | [**Remediation**](Remediation.md)| The remediation parameters. | 

### Return type

[**Remediation**](Remediation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## remediationsCreateOrUpdateAtResourceGroup

> Remediation remediationsCreateOrUpdateAtResourceGroup(subscriptionId, resourceGroupName, remediationName, apiVersion, parameters)



Creates or updates a remediation at resource group scope.

### Example

```javascript
import RemediationsClient from 'remediations_client';
let defaultClient = RemediationsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RemediationsClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let remediationName = "remediationName_example"; // String | The name of the remediation.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new RemediationsClient.Remediation(); // Remediation | The remediation parameters.
apiInstance.remediationsCreateOrUpdateAtResourceGroup(subscriptionId, resourceGroupName, remediationName, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| Resource group name. | 
 **remediationName** | **String**| The name of the remediation. | 
 **apiVersion** | **String**| Client Api Version. | 
 **parameters** | [**Remediation**](Remediation.md)| The remediation parameters. | 

### Return type

[**Remediation**](Remediation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## remediationsCreateOrUpdateAtSubscription

> Remediation remediationsCreateOrUpdateAtSubscription(subscriptionId, remediationName, apiVersion, parameters)



Creates or updates a remediation at subscription scope.

### Example

```javascript
import RemediationsClient from 'remediations_client';
let defaultClient = RemediationsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RemediationsClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
let remediationName = "remediationName_example"; // String | The name of the remediation.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new RemediationsClient.Remediation(); // Remediation | The remediation parameters.
apiInstance.remediationsCreateOrUpdateAtSubscription(subscriptionId, remediationName, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| Microsoft Azure subscription ID. | 
 **remediationName** | **String**| The name of the remediation. | 
 **apiVersion** | **String**| Client Api Version. | 
 **parameters** | [**Remediation**](Remediation.md)| The remediation parameters. | 

### Return type

[**Remediation**](Remediation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## remediationsDeleteAtManagementGroup

> Remediation remediationsDeleteAtManagementGroup(managementGroupsNamespace, managementGroupId, remediationName, apiVersion)



Deletes an existing remediation at management group scope.

### Example

```javascript
import RemediationsClient from 'remediations_client';
let defaultClient = RemediationsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RemediationsClient.DefaultApi();
let managementGroupsNamespace = "managementGroupsNamespace_example"; // String | The namespace for Microsoft Management RP; only \"Microsoft.Management\" is allowed.
let managementGroupId = "managementGroupId_example"; // String | Management group ID.
let remediationName = "remediationName_example"; // String | The name of the remediation.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.remediationsDeleteAtManagementGroup(managementGroupsNamespace, managementGroupId, remediationName, apiVersion, (error, data, response) => {
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
 **managementGroupsNamespace** | **String**| The namespace for Microsoft Management RP; only \&quot;Microsoft.Management\&quot; is allowed. | 
 **managementGroupId** | **String**| Management group ID. | 
 **remediationName** | **String**| The name of the remediation. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**Remediation**](Remediation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## remediationsDeleteAtResource

> Remediation remediationsDeleteAtResource(resourceId, remediationName, apiVersion)



Deletes an existing remediation at individual resource scope.

### Example

```javascript
import RemediationsClient from 'remediations_client';
let defaultClient = RemediationsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RemediationsClient.DefaultApi();
let resourceId = "resourceId_example"; // String | Resource ID.
let remediationName = "remediationName_example"; // String | The name of the remediation.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.remediationsDeleteAtResource(resourceId, remediationName, apiVersion, (error, data, response) => {
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
 **resourceId** | **String**| Resource ID. | 
 **remediationName** | **String**| The name of the remediation. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**Remediation**](Remediation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## remediationsDeleteAtResourceGroup

> Remediation remediationsDeleteAtResourceGroup(subscriptionId, resourceGroupName, remediationName, apiVersion)



Deletes an existing remediation at resource group scope.

### Example

```javascript
import RemediationsClient from 'remediations_client';
let defaultClient = RemediationsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RemediationsClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let remediationName = "remediationName_example"; // String | The name of the remediation.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.remediationsDeleteAtResourceGroup(subscriptionId, resourceGroupName, remediationName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| Resource group name. | 
 **remediationName** | **String**| The name of the remediation. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**Remediation**](Remediation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## remediationsDeleteAtSubscription

> Remediation remediationsDeleteAtSubscription(subscriptionId, remediationName, apiVersion)



Deletes an existing remediation at subscription scope.

### Example

```javascript
import RemediationsClient from 'remediations_client';
let defaultClient = RemediationsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RemediationsClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
let remediationName = "remediationName_example"; // String | The name of the remediation.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.remediationsDeleteAtSubscription(subscriptionId, remediationName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Microsoft Azure subscription ID. | 
 **remediationName** | **String**| The name of the remediation. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**Remediation**](Remediation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## remediationsGetAtManagementGroup

> Remediation remediationsGetAtManagementGroup(managementGroupsNamespace, managementGroupId, remediationName, apiVersion)



Gets an existing remediation at management group scope.

### Example

```javascript
import RemediationsClient from 'remediations_client';
let defaultClient = RemediationsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RemediationsClient.DefaultApi();
let managementGroupsNamespace = "managementGroupsNamespace_example"; // String | The namespace for Microsoft Management RP; only \"Microsoft.Management\" is allowed.
let managementGroupId = "managementGroupId_example"; // String | Management group ID.
let remediationName = "remediationName_example"; // String | The name of the remediation.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.remediationsGetAtManagementGroup(managementGroupsNamespace, managementGroupId, remediationName, apiVersion, (error, data, response) => {
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
 **managementGroupsNamespace** | **String**| The namespace for Microsoft Management RP; only \&quot;Microsoft.Management\&quot; is allowed. | 
 **managementGroupId** | **String**| Management group ID. | 
 **remediationName** | **String**| The name of the remediation. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**Remediation**](Remediation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## remediationsGetAtResource

> Remediation remediationsGetAtResource(resourceId, remediationName, apiVersion)



Gets an existing remediation at resource scope.

### Example

```javascript
import RemediationsClient from 'remediations_client';
let defaultClient = RemediationsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RemediationsClient.DefaultApi();
let resourceId = "resourceId_example"; // String | Resource ID.
let remediationName = "remediationName_example"; // String | The name of the remediation.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.remediationsGetAtResource(resourceId, remediationName, apiVersion, (error, data, response) => {
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
 **resourceId** | **String**| Resource ID. | 
 **remediationName** | **String**| The name of the remediation. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**Remediation**](Remediation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## remediationsGetAtResourceGroup

> Remediation remediationsGetAtResourceGroup(subscriptionId, resourceGroupName, remediationName, apiVersion)



Gets an existing remediation at resource group scope.

### Example

```javascript
import RemediationsClient from 'remediations_client';
let defaultClient = RemediationsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RemediationsClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let remediationName = "remediationName_example"; // String | The name of the remediation.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.remediationsGetAtResourceGroup(subscriptionId, resourceGroupName, remediationName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| Resource group name. | 
 **remediationName** | **String**| The name of the remediation. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**Remediation**](Remediation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## remediationsGetAtSubscription

> Remediation remediationsGetAtSubscription(subscriptionId, remediationName, apiVersion)



Gets an existing remediation at subscription scope.

### Example

```javascript
import RemediationsClient from 'remediations_client';
let defaultClient = RemediationsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RemediationsClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
let remediationName = "remediationName_example"; // String | The name of the remediation.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.remediationsGetAtSubscription(subscriptionId, remediationName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Microsoft Azure subscription ID. | 
 **remediationName** | **String**| The name of the remediation. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**Remediation**](Remediation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## remediationsListDeploymentsAtManagementGroup

> RemediationDeploymentsListResult remediationsListDeploymentsAtManagementGroup(managementGroupsNamespace, managementGroupId, remediationName, apiVersion, opts)



Gets all deployments for a remediation at management group scope.

### Example

```javascript
import RemediationsClient from 'remediations_client';
let defaultClient = RemediationsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RemediationsClient.DefaultApi();
let managementGroupsNamespace = "managementGroupsNamespace_example"; // String | The namespace for Microsoft Management RP; only \"Microsoft.Management\" is allowed.
let managementGroupId = "managementGroupId_example"; // String | Management group ID.
let remediationName = "remediationName_example"; // String | The name of the remediation.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'top': 56 // Number | Maximum number of records to return.
};
apiInstance.remediationsListDeploymentsAtManagementGroup(managementGroupsNamespace, managementGroupId, remediationName, apiVersion, opts, (error, data, response) => {
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
 **managementGroupsNamespace** | **String**| The namespace for Microsoft Management RP; only \&quot;Microsoft.Management\&quot; is allowed. | 
 **managementGroupId** | **String**| Management group ID. | 
 **remediationName** | **String**| The name of the remediation. | 
 **apiVersion** | **String**| Client Api Version. | 
 **top** | **Number**| Maximum number of records to return. | [optional] 

### Return type

[**RemediationDeploymentsListResult**](RemediationDeploymentsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## remediationsListDeploymentsAtResource

> RemediationDeploymentsListResult remediationsListDeploymentsAtResource(resourceId, remediationName, apiVersion, opts)



Gets all deployments for a remediation at resource scope.

### Example

```javascript
import RemediationsClient from 'remediations_client';
let defaultClient = RemediationsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RemediationsClient.DefaultApi();
let resourceId = "resourceId_example"; // String | Resource ID.
let remediationName = "remediationName_example"; // String | The name of the remediation.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'top': 56 // Number | Maximum number of records to return.
};
apiInstance.remediationsListDeploymentsAtResource(resourceId, remediationName, apiVersion, opts, (error, data, response) => {
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
 **resourceId** | **String**| Resource ID. | 
 **remediationName** | **String**| The name of the remediation. | 
 **apiVersion** | **String**| Client Api Version. | 
 **top** | **Number**| Maximum number of records to return. | [optional] 

### Return type

[**RemediationDeploymentsListResult**](RemediationDeploymentsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## remediationsListDeploymentsAtResourceGroup

> RemediationDeploymentsListResult remediationsListDeploymentsAtResourceGroup(subscriptionId, resourceGroupName, remediationName, apiVersion, opts)



Gets all deployments for a remediation at resource group scope.

### Example

```javascript
import RemediationsClient from 'remediations_client';
let defaultClient = RemediationsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RemediationsClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let remediationName = "remediationName_example"; // String | The name of the remediation.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'top': 56 // Number | Maximum number of records to return.
};
apiInstance.remediationsListDeploymentsAtResourceGroup(subscriptionId, resourceGroupName, remediationName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| Resource group name. | 
 **remediationName** | **String**| The name of the remediation. | 
 **apiVersion** | **String**| Client Api Version. | 
 **top** | **Number**| Maximum number of records to return. | [optional] 

### Return type

[**RemediationDeploymentsListResult**](RemediationDeploymentsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## remediationsListDeploymentsAtSubscription

> RemediationDeploymentsListResult remediationsListDeploymentsAtSubscription(subscriptionId, remediationName, apiVersion, opts)



Gets all deployments for a remediation at subscription scope.

### Example

```javascript
import RemediationsClient from 'remediations_client';
let defaultClient = RemediationsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RemediationsClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
let remediationName = "remediationName_example"; // String | The name of the remediation.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'top': 56 // Number | Maximum number of records to return.
};
apiInstance.remediationsListDeploymentsAtSubscription(subscriptionId, remediationName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Microsoft Azure subscription ID. | 
 **remediationName** | **String**| The name of the remediation. | 
 **apiVersion** | **String**| Client Api Version. | 
 **top** | **Number**| Maximum number of records to return. | [optional] 

### Return type

[**RemediationDeploymentsListResult**](RemediationDeploymentsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## remediationsListForManagementGroup

> RemediationListResult remediationsListForManagementGroup(managementGroupsNamespace, managementGroupId, apiVersion, opts)



Gets all remediations for the management group.

### Example

```javascript
import RemediationsClient from 'remediations_client';
let defaultClient = RemediationsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RemediationsClient.DefaultApi();
let managementGroupsNamespace = "managementGroupsNamespace_example"; // String | The namespace for Microsoft Management RP; only \"Microsoft.Management\" is allowed.
let managementGroupId = "managementGroupId_example"; // String | Management group ID.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'top': 56, // Number | Maximum number of records to return.
  'filter': "filter_example" // String | OData filter expression.
};
apiInstance.remediationsListForManagementGroup(managementGroupsNamespace, managementGroupId, apiVersion, opts, (error, data, response) => {
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
 **managementGroupsNamespace** | **String**| The namespace for Microsoft Management RP; only \&quot;Microsoft.Management\&quot; is allowed. | 
 **managementGroupId** | **String**| Management group ID. | 
 **apiVersion** | **String**| Client Api Version. | 
 **top** | **Number**| Maximum number of records to return. | [optional] 
 **filter** | **String**| OData filter expression. | [optional] 

### Return type

[**RemediationListResult**](RemediationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## remediationsListForResource

> RemediationListResult remediationsListForResource(resourceId, apiVersion, opts)



Gets all remediations for a resource.

### Example

```javascript
import RemediationsClient from 'remediations_client';
let defaultClient = RemediationsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RemediationsClient.DefaultApi();
let resourceId = "resourceId_example"; // String | Resource ID.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'top': 56, // Number | Maximum number of records to return.
  'filter': "filter_example" // String | OData filter expression.
};
apiInstance.remediationsListForResource(resourceId, apiVersion, opts, (error, data, response) => {
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
 **resourceId** | **String**| Resource ID. | 
 **apiVersion** | **String**| Client Api Version. | 
 **top** | **Number**| Maximum number of records to return. | [optional] 
 **filter** | **String**| OData filter expression. | [optional] 

### Return type

[**RemediationListResult**](RemediationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## remediationsListForResourceGroup

> RemediationListResult remediationsListForResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts)



Gets all remediations for the subscription.

### Example

```javascript
import RemediationsClient from 'remediations_client';
let defaultClient = RemediationsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RemediationsClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Resource group name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'top': 56, // Number | Maximum number of records to return.
  'filter': "filter_example" // String | OData filter expression.
};
apiInstance.remediationsListForResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| Resource group name. | 
 **apiVersion** | **String**| Client Api Version. | 
 **top** | **Number**| Maximum number of records to return. | [optional] 
 **filter** | **String**| OData filter expression. | [optional] 

### Return type

[**RemediationListResult**](RemediationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## remediationsListForSubscription

> RemediationListResult remediationsListForSubscription(subscriptionId, apiVersion, opts)



Gets all remediations for the subscription.

### Example

```javascript
import RemediationsClient from 'remediations_client';
let defaultClient = RemediationsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RemediationsClient.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | Microsoft Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'top': 56, // Number | Maximum number of records to return.
  'filter': "filter_example" // String | OData filter expression.
};
apiInstance.remediationsListForSubscription(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Microsoft Azure subscription ID. | 
 **apiVersion** | **String**| Client Api Version. | 
 **top** | **Number**| Maximum number of records to return. | [optional] 
 **filter** | **String**| OData filter expression. | [optional] 

### Return type

[**RemediationListResult**](RemediationListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

