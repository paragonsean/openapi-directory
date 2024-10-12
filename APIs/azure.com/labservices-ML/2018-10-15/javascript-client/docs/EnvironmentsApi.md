# ManagedLabsClient.EnvironmentsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**environmentsClaim**](EnvironmentsApi.md#environmentsClaim) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}/environments/{environmentName}/claim | 
[**environmentsCreateOrUpdate**](EnvironmentsApi.md#environmentsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}/environments/{environmentName} | 
[**environmentsDelete**](EnvironmentsApi.md#environmentsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}/environments/{environmentName} | 
[**environmentsGet**](EnvironmentsApi.md#environmentsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}/environments/{environmentName} | 
[**environmentsList**](EnvironmentsApi.md#environmentsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}/environments | 
[**environmentsResetPassword**](EnvironmentsApi.md#environmentsResetPassword) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}/environments/{environmentName}/resetPassword | 
[**environmentsStart**](EnvironmentsApi.md#environmentsStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}/environments/{environmentName}/start | 
[**environmentsStop**](EnvironmentsApi.md#environmentsStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}/environments/{environmentName}/stop | 
[**environmentsUpdate**](EnvironmentsApi.md#environmentsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}/environments/{environmentName} | 



## environmentsClaim

> environmentsClaim(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, environmentName, apiVersion)



Claims the environment and assigns it to the user

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.EnvironmentsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let labName = "labName_example"; // String | The name of the lab.
let environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
let environmentName = "environmentName_example"; // String | The name of the environment.
let apiVersion = "'2018-10-15'"; // String | Client API version.
apiInstance.environmentsClaim(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, environmentName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labAccountName** | **String**| The name of the lab Account. | 
 **labName** | **String**| The name of the lab. | 
 **environmentSettingName** | **String**| The name of the environment Setting. | 
 **environmentName** | **String**| The name of the environment. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## environmentsCreateOrUpdate

> Environment environmentsCreateOrUpdate(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, environmentName, apiVersion, environment)



Create or replace an existing Environment.

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.EnvironmentsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let labName = "labName_example"; // String | The name of the lab.
let environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
let environmentName = "environmentName_example"; // String | The name of the environment.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let environment = new ManagedLabsClient.Environment(); // Environment | Represents an environment instance
apiInstance.environmentsCreateOrUpdate(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, environmentName, apiVersion, environment, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labAccountName** | **String**| The name of the lab Account. | 
 **labName** | **String**| The name of the lab. | 
 **environmentSettingName** | **String**| The name of the environment Setting. | 
 **environmentName** | **String**| The name of the environment. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]
 **environment** | [**Environment**](Environment.md)| Represents an environment instance | 

### Return type

[**Environment**](Environment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## environmentsDelete

> environmentsDelete(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, environmentName, apiVersion)



Delete environment. This operation can take a while to complete

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.EnvironmentsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let labName = "labName_example"; // String | The name of the lab.
let environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
let environmentName = "environmentName_example"; // String | The name of the environment.
let apiVersion = "'2018-10-15'"; // String | Client API version.
apiInstance.environmentsDelete(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, environmentName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labAccountName** | **String**| The name of the lab Account. | 
 **labName** | **String**| The name of the lab. | 
 **environmentSettingName** | **String**| The name of the environment Setting. | 
 **environmentName** | **String**| The name of the environment. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## environmentsGet

> Environment environmentsGet(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, environmentName, apiVersion, opts)



Get environment

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.EnvironmentsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let labName = "labName_example"; // String | The name of the lab.
let environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
let environmentName = "environmentName_example"; // String | The name of the environment.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example" // String | Specify the $expand query. Example: 'properties($expand=networkInterface)'
};
apiInstance.environmentsGet(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, environmentName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labAccountName** | **String**| The name of the lab Account. | 
 **labName** | **String**| The name of the lab. | 
 **environmentSettingName** | **String**| The name of the environment Setting. | 
 **environmentName** | **String**| The name of the environment. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($expand&#x3D;networkInterface)&#39; | [optional] 

### Return type

[**Environment**](Environment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## environmentsList

> ResponseWithContinuationEnvironment environmentsList(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, opts)



List environments in a given environment setting.

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.EnvironmentsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let labName = "labName_example"; // String | The name of the lab.
let environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example", // String | Specify the $expand query. Example: 'properties($expand=networkInterface)'
  'filter': "filter_example", // String | The filter to apply to the operation.
  'top': 56, // Number | The maximum number of resources to return from the operation.
  'orderby': "orderby_example" // String | The ordering expression for the results, using OData notation.
};
apiInstance.environmentsList(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labAccountName** | **String**| The name of the lab Account. | 
 **labName** | **String**| The name of the lab. | 
 **environmentSettingName** | **String**| The name of the environment Setting. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($expand&#x3D;networkInterface)&#39; | [optional] 
 **filter** | **String**| The filter to apply to the operation. | [optional] 
 **top** | **Number**| The maximum number of resources to return from the operation. | [optional] 
 **orderby** | **String**| The ordering expression for the results, using OData notation. | [optional] 

### Return type

[**ResponseWithContinuationEnvironment**](ResponseWithContinuationEnvironment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## environmentsResetPassword

> environmentsResetPassword(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, environmentName, apiVersion, resetPasswordPayload)



Resets the user password on an environment This operation can take a while to complete

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.EnvironmentsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let labName = "labName_example"; // String | The name of the lab.
let environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
let environmentName = "environmentName_example"; // String | The name of the environment.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let resetPasswordPayload = new ManagedLabsClient.ResetPasswordPayload(); // ResetPasswordPayload | Represents the payload for resetting passwords.
apiInstance.environmentsResetPassword(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, environmentName, apiVersion, resetPasswordPayload, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labAccountName** | **String**| The name of the lab Account. | 
 **labName** | **String**| The name of the lab. | 
 **environmentSettingName** | **String**| The name of the environment Setting. | 
 **environmentName** | **String**| The name of the environment. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]
 **resetPasswordPayload** | [**ResetPasswordPayload**](ResetPasswordPayload.md)| Represents the payload for resetting passwords. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## environmentsStart

> environmentsStart(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, environmentName, apiVersion)



Starts an environment by starting all resources inside the environment. This operation can take a while to complete

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.EnvironmentsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let labName = "labName_example"; // String | The name of the lab.
let environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
let environmentName = "environmentName_example"; // String | The name of the environment.
let apiVersion = "'2018-10-15'"; // String | Client API version.
apiInstance.environmentsStart(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, environmentName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labAccountName** | **String**| The name of the lab Account. | 
 **labName** | **String**| The name of the lab. | 
 **environmentSettingName** | **String**| The name of the environment Setting. | 
 **environmentName** | **String**| The name of the environment. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## environmentsStop

> environmentsStop(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, environmentName, apiVersion)



Stops an environment by stopping all resources inside the environment This operation can take a while to complete

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.EnvironmentsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let labName = "labName_example"; // String | The name of the lab.
let environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
let environmentName = "environmentName_example"; // String | The name of the environment.
let apiVersion = "'2018-10-15'"; // String | Client API version.
apiInstance.environmentsStop(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, environmentName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labAccountName** | **String**| The name of the lab Account. | 
 **labName** | **String**| The name of the lab. | 
 **environmentSettingName** | **String**| The name of the environment Setting. | 
 **environmentName** | **String**| The name of the environment. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## environmentsUpdate

> Environment environmentsUpdate(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, environmentName, apiVersion, environment)



Modify properties of environments.

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.EnvironmentsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let labName = "labName_example"; // String | The name of the lab.
let environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
let environmentName = "environmentName_example"; // String | The name of the environment.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let environment = new ManagedLabsClient.EnvironmentFragment(); // EnvironmentFragment | Represents an environment instance
apiInstance.environmentsUpdate(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, environmentName, apiVersion, environment, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group. | 
 **labAccountName** | **String**| The name of the lab Account. | 
 **labName** | **String**| The name of the lab. | 
 **environmentSettingName** | **String**| The name of the environment Setting. | 
 **environmentName** | **String**| The name of the environment. | 
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]
 **environment** | [**EnvironmentFragment**](EnvironmentFragment.md)| Represents an environment instance | 

### Return type

[**Environment**](Environment.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

