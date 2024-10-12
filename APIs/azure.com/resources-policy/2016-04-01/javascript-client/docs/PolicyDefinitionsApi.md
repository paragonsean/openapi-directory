# PolicyClient.PolicyDefinitionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**policyDefinitionsCreateOrUpdate**](PolicyDefinitionsApi.md#policyDefinitionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policydefinitions/{policyDefinitionName} | 
[**policyDefinitionsDelete**](PolicyDefinitionsApi.md#policyDefinitionsDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policydefinitions/{policyDefinitionName} | 
[**policyDefinitionsGet**](PolicyDefinitionsApi.md#policyDefinitionsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policydefinitions/{policyDefinitionName} | 
[**policyDefinitionsList**](PolicyDefinitionsApi.md#policyDefinitionsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Authorization/policydefinitions | 



## policyDefinitionsCreateOrUpdate

> PolicyDefinition policyDefinitionsCreateOrUpdate(policyDefinitionName, apiVersion, subscriptionId, parameters)



Creates or updates a policy definition.

### Example

```javascript
import PolicyClient from 'policy_client';
let defaultClient = PolicyClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyClient.PolicyDefinitionsApi();
let policyDefinitionName = "policyDefinitionName_example"; // String | The name of the policy definition to create.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let parameters = new PolicyClient.PolicyDefinition(); // PolicyDefinition | The policy definition properties.
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
 **policyDefinitionName** | **String**| The name of the policy definition to create. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **parameters** | [**PolicyDefinition**](PolicyDefinition.md)| The policy definition properties. | 

### Return type

[**PolicyDefinition**](PolicyDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## policyDefinitionsDelete

> policyDefinitionsDelete(policyDefinitionName, apiVersion, subscriptionId)



Deletes a policy definition.

### Example

```javascript
import PolicyClient from 'policy_client';
let defaultClient = PolicyClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyClient.PolicyDefinitionsApi();
let policyDefinitionName = "policyDefinitionName_example"; // String | The name of the policy definition to delete.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
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
 **policyDefinitionName** | **String**| The name of the policy definition to delete. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## policyDefinitionsGet

> PolicyDefinition policyDefinitionsGet(policyDefinitionName, apiVersion, subscriptionId)



Gets the policy definition.

### Example

```javascript
import PolicyClient from 'policy_client';
let defaultClient = PolicyClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyClient.PolicyDefinitionsApi();
let policyDefinitionName = "policyDefinitionName_example"; // String | The name of the policy definition to get.
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
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
 **policyDefinitionName** | **String**| The name of the policy definition to get. | 
 **apiVersion** | **String**| The API version to use for the operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**PolicyDefinition**](PolicyDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## policyDefinitionsList

> PolicyDefinitionListResult policyDefinitionsList(apiVersion, subscriptionId, opts)



Gets all the policy definitions for a subscription.

### Example

```javascript
import PolicyClient from 'policy_client';
let defaultClient = PolicyClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PolicyClient.PolicyDefinitionsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let opts = {
  'filter': "filter_example" // String | The filter to apply on the operation.
};
apiInstance.policyDefinitionsList(apiVersion, subscriptionId, opts, (error, data, response) => {
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

[**PolicyDefinitionListResult**](PolicyDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

