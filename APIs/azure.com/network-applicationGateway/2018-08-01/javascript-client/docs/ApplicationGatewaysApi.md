# NetworkManagementClient.ApplicationGatewaysApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**applicationGatewaysBackendHealth**](ApplicationGatewaysApi.md#applicationGatewaysBackendHealth) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationGateways/{applicationGatewayName}/backendhealth | 
[**applicationGatewaysCreateOrUpdate**](ApplicationGatewaysApi.md#applicationGatewaysCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationGateways/{applicationGatewayName} | 
[**applicationGatewaysDelete**](ApplicationGatewaysApi.md#applicationGatewaysDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationGateways/{applicationGatewayName} | 
[**applicationGatewaysGet**](ApplicationGatewaysApi.md#applicationGatewaysGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationGateways/{applicationGatewayName} | 
[**applicationGatewaysGetSslPredefinedPolicy**](ApplicationGatewaysApi.md#applicationGatewaysGetSslPredefinedPolicy) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/applicationGatewayAvailableSslOptions/default/predefinedPolicies/{predefinedPolicyName} | 
[**applicationGatewaysList**](ApplicationGatewaysApi.md#applicationGatewaysList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationGateways | 
[**applicationGatewaysListAll**](ApplicationGatewaysApi.md#applicationGatewaysListAll) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/applicationGateways | 
[**applicationGatewaysListAvailableSslOptions**](ApplicationGatewaysApi.md#applicationGatewaysListAvailableSslOptions) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/applicationGatewayAvailableSslOptions/default | 
[**applicationGatewaysListAvailableSslPredefinedPolicies**](ApplicationGatewaysApi.md#applicationGatewaysListAvailableSslPredefinedPolicies) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/applicationGatewayAvailableSslOptions/default/predefinedPolicies | 
[**applicationGatewaysListAvailableWafRuleSets**](ApplicationGatewaysApi.md#applicationGatewaysListAvailableWafRuleSets) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/applicationGatewayAvailableWafRuleSets | 
[**applicationGatewaysStart**](ApplicationGatewaysApi.md#applicationGatewaysStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationGateways/{applicationGatewayName}/start | 
[**applicationGatewaysStop**](ApplicationGatewaysApi.md#applicationGatewaysStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationGateways/{applicationGatewayName}/stop | 
[**applicationGatewaysUpdateTags**](ApplicationGatewaysApi.md#applicationGatewaysUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/applicationGateways/{applicationGatewayName} | 



## applicationGatewaysBackendHealth

> ApplicationGatewayBackendHealth applicationGatewaysBackendHealth(resourceGroupName, applicationGatewayName, opts)



Gets the backend health of the specified application gateway in a resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ApplicationGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let applicationGatewayName = "applicationGatewayName_example"; // String | The name of the application gateway.
let opts = {
  'UNKNOWN_PARAMETER_NAME': new NetworkManagementClient.null(), //  | 
  'UNKNOWN_PARAMETER_NAME2': new NetworkManagementClient.null(), //  | 
  'expand': "expand_example" // String | Expands BackendAddressPool and BackendHttpSettings referenced in backend health.
};
apiInstance.applicationGatewaysBackendHealth(resourceGroupName, applicationGatewayName, opts, (error, data, response) => {
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
 **applicationGatewayName** | **String**| The name of the application gateway. | 
 **UNKNOWN_PARAMETER_NAME** | [****](.md)|  | [optional] 
 **UNKNOWN_PARAMETER_NAME2** | [****](.md)|  | [optional] 
 **expand** | **String**| Expands BackendAddressPool and BackendHttpSettings referenced in backend health. | [optional] 

### Return type

[**ApplicationGatewayBackendHealth**](ApplicationGatewayBackendHealth.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationGatewaysCreateOrUpdate

> ApplicationGateway applicationGatewaysCreateOrUpdate(resourceGroupName, applicationGatewayName, parameters, opts)



Creates or updates the specified application gateway.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ApplicationGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let applicationGatewayName = "applicationGatewayName_example"; // String | The name of the application gateway.
let parameters = new NetworkManagementClient.ApplicationGateway(); // ApplicationGateway | Parameters supplied to the create or update application gateway operation.
let opts = {
  'UNKNOWN_PARAMETER_NAME': new NetworkManagementClient.null(), //  | 
  'UNKNOWN_PARAMETER_NAME2': new NetworkManagementClient.null() //  | 
};
apiInstance.applicationGatewaysCreateOrUpdate(resourceGroupName, applicationGatewayName, parameters, opts, (error, data, response) => {
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
 **applicationGatewayName** | **String**| The name of the application gateway. | 
 **parameters** | [**ApplicationGateway**](ApplicationGateway.md)| Parameters supplied to the create or update application gateway operation. | 
 **UNKNOWN_PARAMETER_NAME** | [****](.md)|  | [optional] 
 **UNKNOWN_PARAMETER_NAME2** | [****](.md)|  | [optional] 

### Return type

[**ApplicationGateway**](ApplicationGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## applicationGatewaysDelete

> applicationGatewaysDelete(resourceGroupName, applicationGatewayName, opts)



Deletes the specified application gateway.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ApplicationGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let applicationGatewayName = "applicationGatewayName_example"; // String | The name of the application gateway.
let opts = {
  'UNKNOWN_PARAMETER_NAME': new NetworkManagementClient.null(), //  | 
  'UNKNOWN_PARAMETER_NAME2': new NetworkManagementClient.null() //  | 
};
apiInstance.applicationGatewaysDelete(resourceGroupName, applicationGatewayName, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **applicationGatewayName** | **String**| The name of the application gateway. | 
 **UNKNOWN_PARAMETER_NAME** | [****](.md)|  | [optional] 
 **UNKNOWN_PARAMETER_NAME2** | [****](.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## applicationGatewaysGet

> ApplicationGateway applicationGatewaysGet(resourceGroupName, applicationGatewayName, opts)



Gets the specified application gateway.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ApplicationGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let applicationGatewayName = "applicationGatewayName_example"; // String | The name of the application gateway.
let opts = {
  'UNKNOWN_PARAMETER_NAME': new NetworkManagementClient.null(), //  | 
  'UNKNOWN_PARAMETER_NAME2': new NetworkManagementClient.null() //  | 
};
apiInstance.applicationGatewaysGet(resourceGroupName, applicationGatewayName, opts, (error, data, response) => {
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
 **applicationGatewayName** | **String**| The name of the application gateway. | 
 **UNKNOWN_PARAMETER_NAME** | [****](.md)|  | [optional] 
 **UNKNOWN_PARAMETER_NAME2** | [****](.md)|  | [optional] 

### Return type

[**ApplicationGateway**](ApplicationGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationGatewaysGetSslPredefinedPolicy

> Object applicationGatewaysGetSslPredefinedPolicy(predefinedPolicyName, opts)



Gets Ssl predefined policy with the specified policy name.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ApplicationGatewaysApi();
let predefinedPolicyName = "predefinedPolicyName_example"; // String | Name of Ssl predefined policy.
let opts = {
  'UNKNOWN_PARAMETER_NAME': new NetworkManagementClient.null(), //  | 
  'UNKNOWN_PARAMETER_NAME2': new NetworkManagementClient.null() //  | 
};
apiInstance.applicationGatewaysGetSslPredefinedPolicy(predefinedPolicyName, opts, (error, data, response) => {
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
 **predefinedPolicyName** | **String**| Name of Ssl predefined policy. | 
 **UNKNOWN_PARAMETER_NAME** | [****](.md)|  | [optional] 
 **UNKNOWN_PARAMETER_NAME2** | [****](.md)|  | [optional] 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationGatewaysList

> ApplicationGatewayListResult applicationGatewaysList(resourceGroupName, opts)



Lists all application gateways in a resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ApplicationGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let opts = {
  'UNKNOWN_PARAMETER_NAME': new NetworkManagementClient.null(), //  | 
  'UNKNOWN_PARAMETER_NAME2': new NetworkManagementClient.null() //  | 
};
apiInstance.applicationGatewaysList(resourceGroupName, opts, (error, data, response) => {
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
 **UNKNOWN_PARAMETER_NAME** | [****](.md)|  | [optional] 
 **UNKNOWN_PARAMETER_NAME2** | [****](.md)|  | [optional] 

### Return type

[**ApplicationGatewayListResult**](ApplicationGatewayListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationGatewaysListAll

> ApplicationGatewayListResult applicationGatewaysListAll(opts)



Gets all the application gateways in a subscription.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ApplicationGatewaysApi();
let opts = {
  'UNKNOWN_PARAMETER_NAME': new NetworkManagementClient.null(), //  | 
  'UNKNOWN_PARAMETER_NAME2': new NetworkManagementClient.null() //  | 
};
apiInstance.applicationGatewaysListAll(opts, (error, data, response) => {
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
 **UNKNOWN_PARAMETER_NAME** | [****](.md)|  | [optional] 
 **UNKNOWN_PARAMETER_NAME2** | [****](.md)|  | [optional] 

### Return type

[**ApplicationGatewayListResult**](ApplicationGatewayListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationGatewaysListAvailableSslOptions

> Object applicationGatewaysListAvailableSslOptions(opts)



Lists available Ssl options for configuring Ssl policy.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ApplicationGatewaysApi();
let opts = {
  'UNKNOWN_PARAMETER_NAME': new NetworkManagementClient.null(), //  | 
  'UNKNOWN_PARAMETER_NAME2': new NetworkManagementClient.null() //  | 
};
apiInstance.applicationGatewaysListAvailableSslOptions(opts, (error, data, response) => {
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
 **UNKNOWN_PARAMETER_NAME** | [****](.md)|  | [optional] 
 **UNKNOWN_PARAMETER_NAME2** | [****](.md)|  | [optional] 

### Return type

**Object**

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationGatewaysListAvailableSslPredefinedPolicies

> ApplicationGatewayAvailableSslPredefinedPolicies applicationGatewaysListAvailableSslPredefinedPolicies(opts)



Lists all SSL predefined policies for configuring Ssl policy.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ApplicationGatewaysApi();
let opts = {
  'UNKNOWN_PARAMETER_NAME': new NetworkManagementClient.null(), //  | 
  'UNKNOWN_PARAMETER_NAME2': new NetworkManagementClient.null() //  | 
};
apiInstance.applicationGatewaysListAvailableSslPredefinedPolicies(opts, (error, data, response) => {
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
 **UNKNOWN_PARAMETER_NAME** | [****](.md)|  | [optional] 
 **UNKNOWN_PARAMETER_NAME2** | [****](.md)|  | [optional] 

### Return type

[**ApplicationGatewayAvailableSslPredefinedPolicies**](ApplicationGatewayAvailableSslPredefinedPolicies.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationGatewaysListAvailableWafRuleSets

> ApplicationGatewayAvailableWafRuleSetsResult applicationGatewaysListAvailableWafRuleSets(opts)



Lists all available web application firewall rule sets.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ApplicationGatewaysApi();
let opts = {
  'UNKNOWN_PARAMETER_NAME': new NetworkManagementClient.null(), //  | 
  'UNKNOWN_PARAMETER_NAME2': new NetworkManagementClient.null() //  | 
};
apiInstance.applicationGatewaysListAvailableWafRuleSets(opts, (error, data, response) => {
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
 **UNKNOWN_PARAMETER_NAME** | [****](.md)|  | [optional] 
 **UNKNOWN_PARAMETER_NAME2** | [****](.md)|  | [optional] 

### Return type

[**ApplicationGatewayAvailableWafRuleSetsResult**](ApplicationGatewayAvailableWafRuleSetsResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## applicationGatewaysStart

> applicationGatewaysStart(resourceGroupName, applicationGatewayName, apiVersion, subscriptionId)



Starts the specified application gateway.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ApplicationGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let applicationGatewayName = "applicationGatewayName_example"; // String | The name of the application gateway.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.applicationGatewaysStart(resourceGroupName, applicationGatewayName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **applicationGatewayName** | **String**| The name of the application gateway. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## applicationGatewaysStop

> applicationGatewaysStop(resourceGroupName, applicationGatewayName, opts)



Stops the specified application gateway in a resource group.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ApplicationGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let applicationGatewayName = "applicationGatewayName_example"; // String | The name of the application gateway.
let opts = {
  'UNKNOWN_PARAMETER_NAME': new NetworkManagementClient.null(), //  | 
  'UNKNOWN_PARAMETER_NAME2': new NetworkManagementClient.null() //  | 
};
apiInstance.applicationGatewaysStop(resourceGroupName, applicationGatewayName, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **applicationGatewayName** | **String**| The name of the application gateway. | 
 **UNKNOWN_PARAMETER_NAME** | [****](.md)|  | [optional] 
 **UNKNOWN_PARAMETER_NAME2** | [****](.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## applicationGatewaysUpdateTags

> ApplicationGateway applicationGatewaysUpdateTags(resourceGroupName, applicationGatewayName, parameters, opts)



Updates the specified application gateway tags.

### Example

```javascript
import NetworkManagementClient from 'network_management_client';
let defaultClient = NetworkManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkManagementClient.ApplicationGatewaysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let applicationGatewayName = "applicationGatewayName_example"; // String | The name of the application gateway.
let parameters = new NetworkManagementClient.ApplicationGatewaysUpdateTagsRequest(); // ApplicationGatewaysUpdateTagsRequest | Parameters supplied to update application gateway tags.
let opts = {
  'UNKNOWN_PARAMETER_NAME': new NetworkManagementClient.null(), //  | 
  'UNKNOWN_PARAMETER_NAME2': new NetworkManagementClient.null() //  | 
};
apiInstance.applicationGatewaysUpdateTags(resourceGroupName, applicationGatewayName, parameters, opts, (error, data, response) => {
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
 **applicationGatewayName** | **String**| The name of the application gateway. | 
 **parameters** | [**ApplicationGatewaysUpdateTagsRequest**](ApplicationGatewaysUpdateTagsRequest.md)| Parameters supplied to update application gateway tags. | 
 **UNKNOWN_PARAMETER_NAME** | [****](.md)|  | [optional] 
 **UNKNOWN_PARAMETER_NAME2** | [****](.md)|  | [optional] 

### Return type

[**ApplicationGateway**](ApplicationGateway.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

