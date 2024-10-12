# SecurityCenter.JitNetworkAccessPoliciesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jitNetworkAccessPoliciesCreateOrUpdate**](JitNetworkAccessPoliciesApi.md#jitNetworkAccessPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/jitNetworkAccessPolicies/{jitNetworkAccessPolicyName} | 
[**jitNetworkAccessPoliciesDelete**](JitNetworkAccessPoliciesApi.md#jitNetworkAccessPoliciesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/jitNetworkAccessPolicies/{jitNetworkAccessPolicyName} | 
[**jitNetworkAccessPoliciesGet**](JitNetworkAccessPoliciesApi.md#jitNetworkAccessPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/jitNetworkAccessPolicies/{jitNetworkAccessPolicyName} | 
[**jitNetworkAccessPoliciesInitiate**](JitNetworkAccessPoliciesApi.md#jitNetworkAccessPoliciesInitiate) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/jitNetworkAccessPolicies/{jitNetworkAccessPolicyName}/{jitNetworkAccessPolicyInitiateType} | 
[**jitNetworkAccessPoliciesList**](JitNetworkAccessPoliciesApi.md#jitNetworkAccessPoliciesList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/jitNetworkAccessPolicies | 
[**jitNetworkAccessPoliciesListByRegion**](JitNetworkAccessPoliciesApi.md#jitNetworkAccessPoliciesListByRegion) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Security/locations/{ascLocation}/jitNetworkAccessPolicies | 
[**jitNetworkAccessPoliciesListByResourceGroup**](JitNetworkAccessPoliciesApi.md#jitNetworkAccessPoliciesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/jitNetworkAccessPolicies | 
[**jitNetworkAccessPoliciesListByResourceGroupAndRegion**](JitNetworkAccessPoliciesApi.md#jitNetworkAccessPoliciesListByResourceGroupAndRegion) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Security/locations/{ascLocation}/jitNetworkAccessPolicies | 



## jitNetworkAccessPoliciesCreateOrUpdate

> JitNetworkAccessPolicy jitNetworkAccessPoliciesCreateOrUpdate(subscriptionId, resourceGroupName, ascLocation, jitNetworkAccessPolicyName, apiVersion, body)



Create a policy for protecting resources using Just-in-Time access control

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.JitNetworkAccessPoliciesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
let jitNetworkAccessPolicyName = "jitNetworkAccessPolicyName_example"; // String | Name of a Just-in-Time access configuration policy.
let apiVersion = "apiVersion_example"; // String | API version for the operation
let body = new SecurityCenter.JitNetworkAccessPolicy(); // JitNetworkAccessPolicy | 
apiInstance.jitNetworkAccessPoliciesCreateOrUpdate(subscriptionId, resourceGroupName, ascLocation, jitNetworkAccessPolicyName, apiVersion, body, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription ID | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | 
 **jitNetworkAccessPolicyName** | **String**| Name of a Just-in-Time access configuration policy. | 
 **apiVersion** | **String**| API version for the operation | 
 **body** | [**JitNetworkAccessPolicy**](JitNetworkAccessPolicy.md)|  | 

### Return type

[**JitNetworkAccessPolicy**](JitNetworkAccessPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## jitNetworkAccessPoliciesDelete

> jitNetworkAccessPoliciesDelete(subscriptionId, resourceGroupName, ascLocation, jitNetworkAccessPolicyName, apiVersion)



Delete a Just-in-Time access control policy.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.JitNetworkAccessPoliciesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
let jitNetworkAccessPolicyName = "jitNetworkAccessPolicyName_example"; // String | Name of a Just-in-Time access configuration policy.
let apiVersion = "apiVersion_example"; // String | API version for the operation
apiInstance.jitNetworkAccessPoliciesDelete(subscriptionId, resourceGroupName, ascLocation, jitNetworkAccessPolicyName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription ID | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | 
 **jitNetworkAccessPolicyName** | **String**| Name of a Just-in-Time access configuration policy. | 
 **apiVersion** | **String**| API version for the operation | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jitNetworkAccessPoliciesGet

> JitNetworkAccessPolicy jitNetworkAccessPoliciesGet(subscriptionId, resourceGroupName, ascLocation, jitNetworkAccessPolicyName, apiVersion)



Policies for protecting resources using Just-in-Time access control for the subscription, location

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.JitNetworkAccessPoliciesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
let jitNetworkAccessPolicyName = "jitNetworkAccessPolicyName_example"; // String | Name of a Just-in-Time access configuration policy.
let apiVersion = "apiVersion_example"; // String | API version for the operation
apiInstance.jitNetworkAccessPoliciesGet(subscriptionId, resourceGroupName, ascLocation, jitNetworkAccessPolicyName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription ID | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | 
 **jitNetworkAccessPolicyName** | **String**| Name of a Just-in-Time access configuration policy. | 
 **apiVersion** | **String**| API version for the operation | 

### Return type

[**JitNetworkAccessPolicy**](JitNetworkAccessPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jitNetworkAccessPoliciesInitiate

> JitNetworkAccessRequest jitNetworkAccessPoliciesInitiate(subscriptionId, resourceGroupName, ascLocation, jitNetworkAccessPolicyName, jitNetworkAccessPolicyInitiateType, apiVersion, body)



Initiate a JIT access from a specific Just-in-Time policy configuration.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.JitNetworkAccessPoliciesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
let jitNetworkAccessPolicyName = "jitNetworkAccessPolicyName_example"; // String | Name of a Just-in-Time access configuration policy.
let jitNetworkAccessPolicyInitiateType = "jitNetworkAccessPolicyInitiateType_example"; // String | Type of the action to do on the Just-in-Time access policy.
let apiVersion = "apiVersion_example"; // String | API version for the operation
let body = new SecurityCenter.JitNetworkAccessPolicyInitiateRequest(); // JitNetworkAccessPolicyInitiateRequest | 
apiInstance.jitNetworkAccessPoliciesInitiate(subscriptionId, resourceGroupName, ascLocation, jitNetworkAccessPolicyName, jitNetworkAccessPolicyInitiateType, apiVersion, body, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription ID | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | 
 **jitNetworkAccessPolicyName** | **String**| Name of a Just-in-Time access configuration policy. | 
 **jitNetworkAccessPolicyInitiateType** | **String**| Type of the action to do on the Just-in-Time access policy. | 
 **apiVersion** | **String**| API version for the operation | 
 **body** | [**JitNetworkAccessPolicyInitiateRequest**](JitNetworkAccessPolicyInitiateRequest.md)|  | 

### Return type

[**JitNetworkAccessRequest**](JitNetworkAccessRequest.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## jitNetworkAccessPoliciesList

> JitNetworkAccessPoliciesList jitNetworkAccessPoliciesList(subscriptionId, apiVersion)



Policies for protecting resources using Just-in-Time access control.

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.JitNetworkAccessPoliciesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let apiVersion = "apiVersion_example"; // String | API version for the operation
apiInstance.jitNetworkAccessPoliciesList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription ID | 
 **apiVersion** | **String**| API version for the operation | 

### Return type

[**JitNetworkAccessPoliciesList**](JitNetworkAccessPoliciesList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jitNetworkAccessPoliciesListByRegion

> JitNetworkAccessPoliciesList jitNetworkAccessPoliciesListByRegion(subscriptionId, ascLocation, apiVersion)



Policies for protecting resources using Just-in-Time access control for the subscription, location

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.JitNetworkAccessPoliciesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
let apiVersion = "apiVersion_example"; // String | API version for the operation
apiInstance.jitNetworkAccessPoliciesListByRegion(subscriptionId, ascLocation, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription ID | 
 **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | 
 **apiVersion** | **String**| API version for the operation | 

### Return type

[**JitNetworkAccessPoliciesList**](JitNetworkAccessPoliciesList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jitNetworkAccessPoliciesListByResourceGroup

> JitNetworkAccessPoliciesList jitNetworkAccessPoliciesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)



Policies for protecting resources using Just-in-Time access control for the subscription, location

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.JitNetworkAccessPoliciesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | API version for the operation
apiInstance.jitNetworkAccessPoliciesListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription ID | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **apiVersion** | **String**| API version for the operation | 

### Return type

[**JitNetworkAccessPoliciesList**](JitNetworkAccessPoliciesList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## jitNetworkAccessPoliciesListByResourceGroupAndRegion

> JitNetworkAccessPoliciesList jitNetworkAccessPoliciesListByResourceGroupAndRegion(subscriptionId, resourceGroupName, ascLocation, apiVersion)



Policies for protecting resources using Just-in-Time access control for the subscription, location

### Example

```javascript
import SecurityCenter from 'security_center';
let defaultClient = SecurityCenter.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SecurityCenter.JitNetworkAccessPoliciesApi();
let subscriptionId = "subscriptionId_example"; // String | Azure subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let ascLocation = "ascLocation_example"; // String | The location where ASC stores the data of the subscription. can be retrieved from Get locations
let apiVersion = "apiVersion_example"; // String | API version for the operation
apiInstance.jitNetworkAccessPoliciesListByResourceGroupAndRegion(subscriptionId, resourceGroupName, ascLocation, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure subscription ID | 
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **ascLocation** | **String**| The location where ASC stores the data of the subscription. can be retrieved from Get locations | 
 **apiVersion** | **String**| API version for the operation | 

### Return type

[**JitNetworkAccessPoliciesList**](JitNetworkAccessPoliciesList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

