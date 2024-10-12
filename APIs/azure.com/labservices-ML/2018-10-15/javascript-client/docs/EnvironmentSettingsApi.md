# ManagedLabsClient.EnvironmentSettingsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**environmentSettingsClaimAny**](EnvironmentSettingsApi.md#environmentSettingsClaimAny) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}/claimAny | 
[**environmentSettingsCreateOrUpdate**](EnvironmentSettingsApi.md#environmentSettingsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName} | 
[**environmentSettingsDelete**](EnvironmentSettingsApi.md#environmentSettingsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName} | 
[**environmentSettingsGet**](EnvironmentSettingsApi.md#environmentSettingsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName} | 
[**environmentSettingsList**](EnvironmentSettingsApi.md#environmentSettingsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings | 
[**environmentSettingsPublish**](EnvironmentSettingsApi.md#environmentSettingsPublish) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}/publish | 
[**environmentSettingsStart**](EnvironmentSettingsApi.md#environmentSettingsStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}/start | 
[**environmentSettingsStop**](EnvironmentSettingsApi.md#environmentSettingsStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}/stop | 
[**environmentSettingsUpdate**](EnvironmentSettingsApi.md#environmentSettingsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName} | 



## environmentSettingsClaimAny

> environmentSettingsClaimAny(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion)



Claims a random environment for a user in an environment settings

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.EnvironmentSettingsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let labName = "labName_example"; // String | The name of the lab.
let environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
let apiVersion = "'2018-10-15'"; // String | Client API version.
apiInstance.environmentSettingsClaimAny(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## environmentSettingsCreateOrUpdate

> EnvironmentSetting environmentSettingsCreateOrUpdate(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, environmentSetting)



Create or replace an existing Environment Setting. This operation can take a while to complete

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.EnvironmentSettingsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let labName = "labName_example"; // String | The name of the lab.
let environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let environmentSetting = new ManagedLabsClient.EnvironmentSetting(); // EnvironmentSetting | Represents settings of an environment, from which environment instances would be created
apiInstance.environmentSettingsCreateOrUpdate(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, environmentSetting, (error, data, response) => {
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
 **environmentSetting** | [**EnvironmentSetting**](EnvironmentSetting.md)| Represents settings of an environment, from which environment instances would be created | 

### Return type

[**EnvironmentSetting**](EnvironmentSetting.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## environmentSettingsDelete

> environmentSettingsDelete(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion)



Delete environment setting. This operation can take a while to complete

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.EnvironmentSettingsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let labName = "labName_example"; // String | The name of the lab.
let environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
let apiVersion = "'2018-10-15'"; // String | Client API version.
apiInstance.environmentSettingsDelete(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## environmentSettingsGet

> EnvironmentSetting environmentSettingsGet(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, opts)



Get environment setting

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.EnvironmentSettingsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let labName = "labName_example"; // String | The name of the lab.
let environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example" // String | Specify the $expand query. Example: 'properties($select=publishingState)'
};
apiInstance.environmentSettingsGet(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, opts, (error, data, response) => {
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
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;publishingState)&#39; | [optional] 

### Return type

[**EnvironmentSetting**](EnvironmentSetting.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## environmentSettingsList

> ResponseWithContinuationEnvironmentSetting environmentSettingsList(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion, opts)



List environment setting in a given lab.

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.EnvironmentSettingsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let labName = "labName_example"; // String | The name of the lab.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let opts = {
  'expand': "expand_example", // String | Specify the $expand query. Example: 'properties($select=publishingState)'
  'filter': "filter_example", // String | The filter to apply to the operation.
  'top': 56, // Number | The maximum number of resources to return from the operation.
  'orderby': "orderby_example" // String | The ordering expression for the results, using OData notation.
};
apiInstance.environmentSettingsList(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]
 **expand** | **String**| Specify the $expand query. Example: &#39;properties($select&#x3D;publishingState)&#39; | [optional] 
 **filter** | **String**| The filter to apply to the operation. | [optional] 
 **top** | **Number**| The maximum number of resources to return from the operation. | [optional] 
 **orderby** | **String**| The ordering expression for the results, using OData notation. | [optional] 

### Return type

[**ResponseWithContinuationEnvironmentSetting**](ResponseWithContinuationEnvironmentSetting.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## environmentSettingsPublish

> environmentSettingsPublish(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, publishPayload)



Provisions/deprovisions required resources for an environment setting based on current state of the lab/environment setting.

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.EnvironmentSettingsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let labName = "labName_example"; // String | The name of the lab.
let environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let publishPayload = new ManagedLabsClient.PublishPayload(); // PublishPayload | Payload for Publish operation on EnvironmentSetting.
apiInstance.environmentSettingsPublish(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, publishPayload, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]
 **publishPayload** | [**PublishPayload**](PublishPayload.md)| Payload for Publish operation on EnvironmentSetting. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## environmentSettingsStart

> environmentSettingsStart(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion)



Starts a template by starting all resources inside the template. This operation can take a while to complete

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.EnvironmentSettingsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let labName = "labName_example"; // String | The name of the lab.
let environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
let apiVersion = "'2018-10-15'"; // String | Client API version.
apiInstance.environmentSettingsStart(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## environmentSettingsStop

> environmentSettingsStop(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion)



Starts a template by starting all resources inside the template. This operation can take a while to complete

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.EnvironmentSettingsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let labName = "labName_example"; // String | The name of the lab.
let environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
let apiVersion = "'2018-10-15'"; // String | Client API version.
apiInstance.environmentSettingsStop(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | [default to &#39;2018-10-15&#39;]

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## environmentSettingsUpdate

> EnvironmentSetting environmentSettingsUpdate(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, environmentSetting)



Modify properties of environment setting.

### Example

```javascript
import ManagedLabsClient from 'managed_labs_client';
let defaultClient = ManagedLabsClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ManagedLabsClient.EnvironmentSettingsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let labAccountName = "labAccountName_example"; // String | The name of the lab Account.
let labName = "labName_example"; // String | The name of the lab.
let environmentSettingName = "environmentSettingName_example"; // String | The name of the environment Setting.
let apiVersion = "'2018-10-15'"; // String | Client API version.
let environmentSetting = new ManagedLabsClient.EnvironmentSettingFragment(); // EnvironmentSettingFragment | Represents settings of an environment, from which environment instances would be created
apiInstance.environmentSettingsUpdate(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, environmentSetting, (error, data, response) => {
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
 **environmentSetting** | [**EnvironmentSettingFragment**](EnvironmentSettingFragment.md)| Represents settings of an environment, from which environment instances would be created | 

### Return type

[**EnvironmentSetting**](EnvironmentSetting.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

