# AppConfigurationManagementClient.ConfigurationStoresApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configurationStoresCreate**](ConfigurationStoresApi.md#configurationStoresCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName} | 
[**configurationStoresDelete**](ConfigurationStoresApi.md#configurationStoresDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName} | 
[**configurationStoresGet**](ConfigurationStoresApi.md#configurationStoresGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName} | 
[**configurationStoresList**](ConfigurationStoresApi.md#configurationStoresList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.AppConfiguration/configurationStores | 
[**configurationStoresListByResourceGroup**](ConfigurationStoresApi.md#configurationStoresListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores | 
[**configurationStoresListKeyValue**](ConfigurationStoresApi.md#configurationStoresListKeyValue) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName}/listKeyValue | 
[**configurationStoresListKeys**](ConfigurationStoresApi.md#configurationStoresListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName}/ListKeys | 
[**configurationStoresRegenerateKey**](ConfigurationStoresApi.md#configurationStoresRegenerateKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName}/RegenerateKey | 
[**configurationStoresUpdate**](ConfigurationStoresApi.md#configurationStoresUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName} | 



## configurationStoresCreate

> ConfigurationStore configurationStoresCreate(subscriptionId, resourceGroupName, configStoreName, apiVersion, configStoreCreationParameters)



Creates a configuration store with the specified parameters.

### Example

```javascript
import AppConfigurationManagementClient from 'app_configuration_management_client';
let defaultClient = AppConfigurationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppConfigurationManagementClient.ConfigurationStoresApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let configStoreName = "configStoreName_example"; // String | The name of the configuration store.
let apiVersion = "apiVersion_example"; // String | The client API version.
let configStoreCreationParameters = new AppConfigurationManagementClient.ConfigurationStore(); // ConfigurationStore | The parameters for creating a configuration store.
apiInstance.configurationStoresCreate(subscriptionId, resourceGroupName, configStoreName, apiVersion, configStoreCreationParameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | 
 **configStoreName** | **String**| The name of the configuration store. | 
 **apiVersion** | **String**| The client API version. | 
 **configStoreCreationParameters** | [**ConfigurationStore**](ConfigurationStore.md)| The parameters for creating a configuration store. | 

### Return type

[**ConfigurationStore**](ConfigurationStore.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## configurationStoresDelete

> configurationStoresDelete(subscriptionId, resourceGroupName, configStoreName, apiVersion)



Deletes a configuration store.

### Example

```javascript
import AppConfigurationManagementClient from 'app_configuration_management_client';
let defaultClient = AppConfigurationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppConfigurationManagementClient.ConfigurationStoresApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let configStoreName = "configStoreName_example"; // String | The name of the configuration store.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.configurationStoresDelete(subscriptionId, resourceGroupName, configStoreName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | 
 **configStoreName** | **String**| The name of the configuration store. | 
 **apiVersion** | **String**| The client API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## configurationStoresGet

> ConfigurationStore configurationStoresGet(subscriptionId, resourceGroupName, configStoreName, apiVersion)



Gets the properties of the specified configuration store.

### Example

```javascript
import AppConfigurationManagementClient from 'app_configuration_management_client';
let defaultClient = AppConfigurationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppConfigurationManagementClient.ConfigurationStoresApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let configStoreName = "configStoreName_example"; // String | The name of the configuration store.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.configurationStoresGet(subscriptionId, resourceGroupName, configStoreName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | 
 **configStoreName** | **String**| The name of the configuration store. | 
 **apiVersion** | **String**| The client API version. | 

### Return type

[**ConfigurationStore**](ConfigurationStore.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## configurationStoresList

> ConfigurationStoreListResult configurationStoresList(subscriptionId, apiVersion, opts)



Lists the configuration stores for a given subscription.

### Example

```javascript
import AppConfigurationManagementClient from 'app_configuration_management_client';
let defaultClient = AppConfigurationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppConfigurationManagementClient.ConfigurationStoresApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let apiVersion = "apiVersion_example"; // String | The client API version.
let opts = {
  'skipToken': "skipToken_example" // String | A skip token is used to continue retrieving items after an operation returns a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skipToken parameter that specifies a starting point to use for subsequent calls.
};
apiInstance.configurationStoresList(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **apiVersion** | **String**| The client API version. | 
 **skipToken** | **String**| A skip token is used to continue retrieving items after an operation returns a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skipToken parameter that specifies a starting point to use for subsequent calls. | [optional] 

### Return type

[**ConfigurationStoreListResult**](ConfigurationStoreListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## configurationStoresListByResourceGroup

> ConfigurationStoreListResult configurationStoresListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts)



Lists the configuration stores for a given resource group.

### Example

```javascript
import AppConfigurationManagementClient from 'app_configuration_management_client';
let defaultClient = AppConfigurationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppConfigurationManagementClient.ConfigurationStoresApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let apiVersion = "apiVersion_example"; // String | The client API version.
let opts = {
  'skipToken': "skipToken_example" // String | A skip token is used to continue retrieving items after an operation returns a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skipToken parameter that specifies a starting point to use for subsequent calls.
};
apiInstance.configurationStoresListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | 
 **apiVersion** | **String**| The client API version. | 
 **skipToken** | **String**| A skip token is used to continue retrieving items after an operation returns a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skipToken parameter that specifies a starting point to use for subsequent calls. | [optional] 

### Return type

[**ConfigurationStoreListResult**](ConfigurationStoreListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## configurationStoresListKeyValue

> KeyValue configurationStoresListKeyValue(subscriptionId, resourceGroupName, configStoreName, apiVersion, listKeyValueParameters)



Lists a configuration store key-value.

### Example

```javascript
import AppConfigurationManagementClient from 'app_configuration_management_client';
let defaultClient = AppConfigurationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppConfigurationManagementClient.ConfigurationStoresApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let configStoreName = "configStoreName_example"; // String | The name of the configuration store.
let apiVersion = "apiVersion_example"; // String | The client API version.
let listKeyValueParameters = new AppConfigurationManagementClient.ListKeyValueParameters(); // ListKeyValueParameters | The parameters for retrieving a key-value.
apiInstance.configurationStoresListKeyValue(subscriptionId, resourceGroupName, configStoreName, apiVersion, listKeyValueParameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | 
 **configStoreName** | **String**| The name of the configuration store. | 
 **apiVersion** | **String**| The client API version. | 
 **listKeyValueParameters** | [**ListKeyValueParameters**](ListKeyValueParameters.md)| The parameters for retrieving a key-value. | 

### Return type

[**KeyValue**](KeyValue.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## configurationStoresListKeys

> ApiKeyListResult configurationStoresListKeys(subscriptionId, resourceGroupName, configStoreName, apiVersion, opts)



Lists the access key for the specified configuration store.

### Example

```javascript
import AppConfigurationManagementClient from 'app_configuration_management_client';
let defaultClient = AppConfigurationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppConfigurationManagementClient.ConfigurationStoresApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let configStoreName = "configStoreName_example"; // String | The name of the configuration store.
let apiVersion = "apiVersion_example"; // String | The client API version.
let opts = {
  'skipToken': "skipToken_example" // String | A skip token is used to continue retrieving items after an operation returns a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skipToken parameter that specifies a starting point to use for subsequent calls.
};
apiInstance.configurationStoresListKeys(subscriptionId, resourceGroupName, configStoreName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | 
 **configStoreName** | **String**| The name of the configuration store. | 
 **apiVersion** | **String**| The client API version. | 
 **skipToken** | **String**| A skip token is used to continue retrieving items after an operation returns a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skipToken parameter that specifies a starting point to use for subsequent calls. | [optional] 

### Return type

[**ApiKeyListResult**](ApiKeyListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## configurationStoresRegenerateKey

> ApiKey configurationStoresRegenerateKey(subscriptionId, resourceGroupName, configStoreName, apiVersion, regenerateKeyParameters)



Regenerates an access key for the specified configuration store.

### Example

```javascript
import AppConfigurationManagementClient from 'app_configuration_management_client';
let defaultClient = AppConfigurationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppConfigurationManagementClient.ConfigurationStoresApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let configStoreName = "configStoreName_example"; // String | The name of the configuration store.
let apiVersion = "apiVersion_example"; // String | The client API version.
let regenerateKeyParameters = new AppConfigurationManagementClient.RegenerateKeyParameters(); // RegenerateKeyParameters | The parameters for regenerating an access key.
apiInstance.configurationStoresRegenerateKey(subscriptionId, resourceGroupName, configStoreName, apiVersion, regenerateKeyParameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | 
 **configStoreName** | **String**| The name of the configuration store. | 
 **apiVersion** | **String**| The client API version. | 
 **regenerateKeyParameters** | [**RegenerateKeyParameters**](RegenerateKeyParameters.md)| The parameters for regenerating an access key. | 

### Return type

[**ApiKey**](ApiKey.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## configurationStoresUpdate

> ConfigurationStore configurationStoresUpdate(subscriptionId, resourceGroupName, configStoreName, apiVersion, configStoreUpdateParameters)



Updates a configuration store with the specified parameters.

### Example

```javascript
import AppConfigurationManagementClient from 'app_configuration_management_client';
let defaultClient = AppConfigurationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppConfigurationManagementClient.ConfigurationStoresApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let configStoreName = "configStoreName_example"; // String | The name of the configuration store.
let apiVersion = "apiVersion_example"; // String | The client API version.
let configStoreUpdateParameters = new AppConfigurationManagementClient.ConfigurationStoreUpdateParameters(); // ConfigurationStoreUpdateParameters | The parameters for updating a configuration store.
apiInstance.configurationStoresUpdate(subscriptionId, resourceGroupName, configStoreName, apiVersion, configStoreUpdateParameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | 
 **configStoreName** | **String**| The name of the configuration store. | 
 **apiVersion** | **String**| The client API version. | 
 **configStoreUpdateParameters** | [**ConfigurationStoreUpdateParameters**](ConfigurationStoreUpdateParameters.md)| The parameters for updating a configuration store. | 

### Return type

[**ConfigurationStore**](ConfigurationStore.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

