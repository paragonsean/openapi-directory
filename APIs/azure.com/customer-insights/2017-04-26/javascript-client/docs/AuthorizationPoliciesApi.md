# CustomerInsightsManagementClient.AuthorizationPoliciesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorizationPoliciesCreateOrUpdate**](AuthorizationPoliciesApi.md#authorizationPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomerInsights/hubs/{hubName}/authorizationPolicies/{authorizationPolicyName} | 
[**authorizationPoliciesGet**](AuthorizationPoliciesApi.md#authorizationPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomerInsights/hubs/{hubName}/authorizationPolicies/{authorizationPolicyName} | 
[**authorizationPoliciesListByHub**](AuthorizationPoliciesApi.md#authorizationPoliciesListByHub) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomerInsights/hubs/{hubName}/authorizationPolicies | 
[**authorizationPoliciesRegeneratePrimaryKey**](AuthorizationPoliciesApi.md#authorizationPoliciesRegeneratePrimaryKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomerInsights/hubs/{hubName}/authorizationPolicies/{authorizationPolicyName}/regeneratePrimaryKey | 
[**authorizationPoliciesRegenerateSecondaryKey**](AuthorizationPoliciesApi.md#authorizationPoliciesRegenerateSecondaryKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomerInsights/hubs/{hubName}/authorizationPolicies/{authorizationPolicyName}/regenerateSecondaryKey | 



## authorizationPoliciesCreateOrUpdate

> AuthorizationPolicyResourceFormat authorizationPoliciesCreateOrUpdate(resourceGroupName, hubName, authorizationPolicyName, apiVersion, subscriptionId, parameters)



Creates an authorization policy or updates an existing authorization policy.

### Example

```javascript
import CustomerInsightsManagementClient from 'customer_insights_management_client';
let defaultClient = CustomerInsightsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CustomerInsightsManagementClient.AuthorizationPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let hubName = "hubName_example"; // String | The name of the hub.
let authorizationPolicyName = "authorizationPolicyName_example"; // String | The name of the policy.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new CustomerInsightsManagementClient.AuthorizationPolicyResourceFormat(); // AuthorizationPolicyResourceFormat | Parameters supplied to the CreateOrUpdate authorization policy operation.
apiInstance.authorizationPoliciesCreateOrUpdate(resourceGroupName, hubName, authorizationPolicyName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **hubName** | **String**| The name of the hub. | 
 **authorizationPolicyName** | **String**| The name of the policy. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**AuthorizationPolicyResourceFormat**](AuthorizationPolicyResourceFormat.md)| Parameters supplied to the CreateOrUpdate authorization policy operation. | 

### Return type

[**AuthorizationPolicyResourceFormat**](AuthorizationPolicyResourceFormat.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## authorizationPoliciesGet

> AuthorizationPolicyResourceFormat authorizationPoliciesGet(resourceGroupName, hubName, authorizationPolicyName, apiVersion, subscriptionId)



Gets an authorization policy in the hub.

### Example

```javascript
import CustomerInsightsManagementClient from 'customer_insights_management_client';
let defaultClient = CustomerInsightsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CustomerInsightsManagementClient.AuthorizationPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let hubName = "hubName_example"; // String | The name of the hub.
let authorizationPolicyName = "authorizationPolicyName_example"; // String | The name of the policy.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.authorizationPoliciesGet(resourceGroupName, hubName, authorizationPolicyName, apiVersion, subscriptionId, (error, data, response) => {
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
 **hubName** | **String**| The name of the hub. | 
 **authorizationPolicyName** | **String**| The name of the policy. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**AuthorizationPolicyResourceFormat**](AuthorizationPolicyResourceFormat.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## authorizationPoliciesListByHub

> AuthorizationPolicyListResult authorizationPoliciesListByHub(resourceGroupName, hubName, apiVersion, subscriptionId)



Gets all the authorization policies in a specified hub.

### Example

```javascript
import CustomerInsightsManagementClient from 'customer_insights_management_client';
let defaultClient = CustomerInsightsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CustomerInsightsManagementClient.AuthorizationPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let hubName = "hubName_example"; // String | The name of the hub.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.authorizationPoliciesListByHub(resourceGroupName, hubName, apiVersion, subscriptionId, (error, data, response) => {
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
 **hubName** | **String**| The name of the hub. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**AuthorizationPolicyListResult**](AuthorizationPolicyListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## authorizationPoliciesRegeneratePrimaryKey

> AuthorizationPolicy authorizationPoliciesRegeneratePrimaryKey(resourceGroupName, hubName, authorizationPolicyName, apiVersion, subscriptionId)



Regenerates the primary policy key of the specified authorization policy.

### Example

```javascript
import CustomerInsightsManagementClient from 'customer_insights_management_client';
let defaultClient = CustomerInsightsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CustomerInsightsManagementClient.AuthorizationPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let hubName = "hubName_example"; // String | The name of the hub.
let authorizationPolicyName = "authorizationPolicyName_example"; // String | The name of the policy.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.authorizationPoliciesRegeneratePrimaryKey(resourceGroupName, hubName, authorizationPolicyName, apiVersion, subscriptionId, (error, data, response) => {
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
 **hubName** | **String**| The name of the hub. | 
 **authorizationPolicyName** | **String**| The name of the policy. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**AuthorizationPolicy**](AuthorizationPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## authorizationPoliciesRegenerateSecondaryKey

> AuthorizationPolicy authorizationPoliciesRegenerateSecondaryKey(resourceGroupName, hubName, authorizationPolicyName, apiVersion, subscriptionId)



Regenerates the secondary policy key of the specified authorization policy.

### Example

```javascript
import CustomerInsightsManagementClient from 'customer_insights_management_client';
let defaultClient = CustomerInsightsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CustomerInsightsManagementClient.AuthorizationPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let hubName = "hubName_example"; // String | The name of the hub.
let authorizationPolicyName = "authorizationPolicyName_example"; // String | The name of the policy.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.authorizationPoliciesRegenerateSecondaryKey(resourceGroupName, hubName, authorizationPolicyName, apiVersion, subscriptionId, (error, data, response) => {
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
 **hubName** | **String**| The name of the hub. | 
 **authorizationPolicyName** | **String**| The name of the policy. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**AuthorizationPolicy**](AuthorizationPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

