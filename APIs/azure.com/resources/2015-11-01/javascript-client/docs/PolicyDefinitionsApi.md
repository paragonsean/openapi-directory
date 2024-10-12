# ResourceManagementClient.PolicyDefinitionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**policyDefinitionsCreateOrUpdate**](PolicyDefinitionsApi.md#policyDefinitionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policydefinitions/{policyDefinitionName} | 
[**policyDefinitionsDelete**](PolicyDefinitionsApi.md#policyDefinitionsDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policydefinitions/{policyDefinitionName} | 
[**policyDefinitionsGet**](PolicyDefinitionsApi.md#policyDefinitionsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policydefinitions/{policyDefinitionName} | 



## policyDefinitionsCreateOrUpdate

> PolicyDefinition policyDefinitionsCreateOrUpdate(policyDefinitionName, apiVersion, subscriptionId, parameters)



Create or update policy definition.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.PolicyDefinitionsApi();
let policyDefinitionName = "policyDefinitionName_example"; // String | The policy definition name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ResourceManagementClient.PolicyDefinition(); // PolicyDefinition | The policy definition properties
apiInstance.policyDefinitionsCreateOrUpdate(policyDefinitionName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **policyDefinitionName** | **String**| The policy definition name. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**PolicyDefinition**](PolicyDefinition.md)| The policy definition properties | 

### Return type

[**PolicyDefinition**](PolicyDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## policyDefinitionsDelete

> policyDefinitionsDelete(policyDefinitionName, apiVersion, subscriptionId)



Deletes policy definition.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.PolicyDefinitionsApi();
let policyDefinitionName = "policyDefinitionName_example"; // String | The policy definition name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.policyDefinitionsDelete(policyDefinitionName, apiVersion, subscriptionId, (error, data, response) => {
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
 **policyDefinitionName** | **String**| The policy definition name. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## policyDefinitionsGet

> PolicyDefinition policyDefinitionsGet(policyDefinitionName, apiVersion, subscriptionId)



Gets policy definition.

### Example

```javascript
import ResourceManagementClient from 'resource_management_client';
let defaultClient = ResourceManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ResourceManagementClient.PolicyDefinitionsApi();
let policyDefinitionName = "policyDefinitionName_example"; // String | The policy definition name.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.policyDefinitionsGet(policyDefinitionName, apiVersion, subscriptionId, (error, data, response) => {
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
 **policyDefinitionName** | **String**| The policy definition name. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**PolicyDefinition**](PolicyDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

