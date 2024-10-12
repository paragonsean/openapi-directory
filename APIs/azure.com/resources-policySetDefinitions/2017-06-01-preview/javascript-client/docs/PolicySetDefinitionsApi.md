# PolicyClient.PolicySetDefinitionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**policySetDefinitionsCreateOrUpdate**](PolicySetDefinitionsApi.md#policySetDefinitionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policySetDefinitions/{policySetDefinitionName} | 
[**policySetDefinitionsCreateOrUpdateAtManagementGroup**](PolicySetDefinitionsApi.md#policySetDefinitionsCreateOrUpdateAtManagementGroup) | **PUT** /providers/Microsoft.Management/managementgroups/{managementGroupId}/providers/Microsoft.Authorization/policySetDefinitions/{policySetDefinitionName} | 
[**policySetDefinitionsDelete**](PolicySetDefinitionsApi.md#policySetDefinitionsDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policySetDefinitions/{policySetDefinitionName} | 
[**policySetDefinitionsDeleteAtManagementGroup**](PolicySetDefinitionsApi.md#policySetDefinitionsDeleteAtManagementGroup) | **DELETE** /providers/Microsoft.Management/managementgroups/{managementGroupId}/providers/Microsoft.Authorization/policySetDefinitions/{policySetDefinitionName} | 
[**policySetDefinitionsGet**](PolicySetDefinitionsApi.md#policySetDefinitionsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policySetDefinitions/{policySetDefinitionName} | 
[**policySetDefinitionsGetAtManagementGroup**](PolicySetDefinitionsApi.md#policySetDefinitionsGetAtManagementGroup) | **GET** /providers/Microsoft.Management/managementgroups/{managementGroupId}/providers/Microsoft.Authorization/policySetDefinitions/{policySetDefinitionName} | 
[**policySetDefinitionsGetBuiltIn**](PolicySetDefinitionsApi.md#policySetDefinitionsGetBuiltIn) | **GET** /providers/Microsoft.Authorization/policySetDefinitions/{policySetDefinitionName} | 
[**policySetDefinitionsList**](PolicySetDefinitionsApi.md#policySetDefinitionsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policySetDefinitions | 
[**policySetDefinitionsListBuiltIn**](PolicySetDefinitionsApi.md#policySetDefinitionsListBuiltIn) | **GET** /providers/Microsoft.Authorization/policySetDefinitions | 
[**policySetDefinitionsListByManagementGroup**](PolicySetDefinitionsApi.md#policySetDefinitionsListByManagementGroup) | **GET** /providers/Microsoft.Management/managementgroups/{managementGroupId}/providers/Microsoft.Authorization/policySetDefinitions | 



## policySetDefinitionsCreateOrUpdate

> PolicySetDefinition policySetDefinitionsCreateOrUpdate(policySetDefinitionName, apiVersion, subscriptionId, parameters)



Creates or updates a policy set definition.

### Example

```javascript
import PolicyClient from 'policy_client';
let defaultClient = PolicyClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyClient.PolicySetDefinitionsApi();
let policySetDefinitionName = "policySetDefinitionName_example"; // String | The name of the policy set definition to create.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let parameters = new PolicyClient.PolicySetDefinition(); // PolicySetDefinition | The policy set definition properties.
apiInstance.policySetDefinitionsCreateOrUpdate(policySetDefinitionName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **policySetDefinitionName** | **String**| The name of the policy set definition to create. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **parameters** | [**PolicySetDefinition**](PolicySetDefinition.md)| The policy set definition properties. | 

### Return type

[**PolicySetDefinition**](PolicySetDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## policySetDefinitionsCreateOrUpdateAtManagementGroup

> PolicySetDefinition policySetDefinitionsCreateOrUpdateAtManagementGroup(policySetDefinitionName, apiVersion, managementGroupId, parameters)



Creates or updates a policy set definition at management group level.

### Example

```javascript
import PolicyClient from 'policy_client';
let defaultClient = PolicyClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyClient.PolicySetDefinitionsApi();
let policySetDefinitionName = "policySetDefinitionName_example"; // String | The name of the policy set definition to create.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let managementGroupId = "managementGroupId_example"; // String | The ID of the management group.
let parameters = new PolicyClient.PolicySetDefinition(); // PolicySetDefinition | The policy set definition properties.
apiInstance.policySetDefinitionsCreateOrUpdateAtManagementGroup(policySetDefinitionName, apiVersion, managementGroupId, parameters, (error, data, response) => {
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
 **policySetDefinitionName** | **String**| The name of the policy set definition to create. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **managementGroupId** | **String**| The ID of the management group. | 
 **parameters** | [**PolicySetDefinition**](PolicySetDefinition.md)| The policy set definition properties. | 

### Return type

[**PolicySetDefinition**](PolicySetDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## policySetDefinitionsDelete

> policySetDefinitionsDelete(policySetDefinitionName, apiVersion, subscriptionId)



Deletes a policy set definition.

### Example

```javascript
import PolicyClient from 'policy_client';
let defaultClient = PolicyClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyClient.PolicySetDefinitionsApi();
let policySetDefinitionName = "policySetDefinitionName_example"; // String | The name of the policy set definition to delete.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.policySetDefinitionsDelete(policySetDefinitionName, apiVersion, subscriptionId, (error, data, response) => {
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
 **policySetDefinitionName** | **String**| The name of the policy set definition to delete. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## policySetDefinitionsDeleteAtManagementGroup

> policySetDefinitionsDeleteAtManagementGroup(policySetDefinitionName, apiVersion, managementGroupId)



Deletes a policy set definition at management group level.

### Example

```javascript
import PolicyClient from 'policy_client';
let defaultClient = PolicyClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyClient.PolicySetDefinitionsApi();
let policySetDefinitionName = "policySetDefinitionName_example"; // String | The name of the policy set definition to delete.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let managementGroupId = "managementGroupId_example"; // String | The ID of the management group.
apiInstance.policySetDefinitionsDeleteAtManagementGroup(policySetDefinitionName, apiVersion, managementGroupId, (error, data, response) => {
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
 **policySetDefinitionName** | **String**| The name of the policy set definition to delete. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **managementGroupId** | **String**| The ID of the management group. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## policySetDefinitionsGet

> PolicySetDefinition policySetDefinitionsGet(policySetDefinitionName, apiVersion, subscriptionId)



Gets the policy set definition.

### Example

```javascript
import PolicyClient from 'policy_client';
let defaultClient = PolicyClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyClient.PolicySetDefinitionsApi();
let policySetDefinitionName = "policySetDefinitionName_example"; // String | The name of the policy set definition to get.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.policySetDefinitionsGet(policySetDefinitionName, apiVersion, subscriptionId, (error, data, response) => {
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
 **policySetDefinitionName** | **String**| The name of the policy set definition to get. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**PolicySetDefinition**](PolicySetDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## policySetDefinitionsGetAtManagementGroup

> PolicySetDefinition policySetDefinitionsGetAtManagementGroup(policySetDefinitionName, apiVersion, managementGroupId)



Gets the policy set definition at management group level.

### Example

```javascript
import PolicyClient from 'policy_client';
let defaultClient = PolicyClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyClient.PolicySetDefinitionsApi();
let policySetDefinitionName = "policySetDefinitionName_example"; // String | The name of the policy set definition to get.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let managementGroupId = "managementGroupId_example"; // String | The ID of the management group.
apiInstance.policySetDefinitionsGetAtManagementGroup(policySetDefinitionName, apiVersion, managementGroupId, (error, data, response) => {
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
 **policySetDefinitionName** | **String**| The name of the policy set definition to get. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **managementGroupId** | **String**| The ID of the management group. | 

### Return type

[**PolicySetDefinition**](PolicySetDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## policySetDefinitionsGetBuiltIn

> PolicySetDefinition policySetDefinitionsGetBuiltIn(policySetDefinitionName, apiVersion)



Gets the built in policy set definition.

### Example

```javascript
import PolicyClient from 'policy_client';
let defaultClient = PolicyClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyClient.PolicySetDefinitionsApi();
let policySetDefinitionName = "policySetDefinitionName_example"; // String | The name of the policy set definition to get.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
apiInstance.policySetDefinitionsGetBuiltIn(policySetDefinitionName, apiVersion, (error, data, response) => {
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
 **policySetDefinitionName** | **String**| The name of the policy set definition to get. | 
 **apiVersion** | **String**| The API version to use for the operation. | 

### Return type

[**PolicySetDefinition**](PolicySetDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## policySetDefinitionsList

> PolicySetDefinitionListResult policySetDefinitionsList(apiVersion, subscriptionId)



Gets all the policy set definitions for a subscription.

### Example

```javascript
import PolicyClient from 'policy_client';
let defaultClient = PolicyClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyClient.PolicySetDefinitionsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.policySetDefinitionsList(apiVersion, subscriptionId, (error, data, response) => {
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

### Return type

[**PolicySetDefinitionListResult**](PolicySetDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## policySetDefinitionsListBuiltIn

> PolicySetDefinitionListResult policySetDefinitionsListBuiltIn(apiVersion)



Gets all the built in policy set definitions.

### Example

```javascript
import PolicyClient from 'policy_client';
let defaultClient = PolicyClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyClient.PolicySetDefinitionsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
apiInstance.policySetDefinitionsListBuiltIn(apiVersion, (error, data, response) => {
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

### Return type

[**PolicySetDefinitionListResult**](PolicySetDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## policySetDefinitionsListByManagementGroup

> PolicySetDefinitionListResult policySetDefinitionsListByManagementGroup(apiVersion, managementGroupId)



Gets all the policy set definitions for a subscription at management group.

### Example

```javascript
import PolicyClient from 'policy_client';
let defaultClient = PolicyClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyClient.PolicySetDefinitionsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let managementGroupId = "managementGroupId_example"; // String | The ID of the management group.
apiInstance.policySetDefinitionsListByManagementGroup(apiVersion, managementGroupId, (error, data, response) => {
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
 **managementGroupId** | **String**| The ID of the management group. | 

### Return type

[**PolicySetDefinitionListResult**](PolicySetDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

