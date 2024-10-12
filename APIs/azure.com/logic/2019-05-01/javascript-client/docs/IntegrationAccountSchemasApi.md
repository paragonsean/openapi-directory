# LogicManagementClient.IntegrationAccountSchemasApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**integrationAccountSchemasCreateOrUpdate**](IntegrationAccountSchemasApi.md#integrationAccountSchemasCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/schemas/{schemaName} | 
[**integrationAccountSchemasDelete**](IntegrationAccountSchemasApi.md#integrationAccountSchemasDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/schemas/{schemaName} | 
[**integrationAccountSchemasGet**](IntegrationAccountSchemasApi.md#integrationAccountSchemasGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/schemas/{schemaName} | 
[**integrationAccountSchemasList**](IntegrationAccountSchemasApi.md#integrationAccountSchemasList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/schemas | 
[**integrationAccountSchemasListContentCallbackUrl**](IntegrationAccountSchemasApi.md#integrationAccountSchemasListContentCallbackUrl) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/schemas/{schemaName}/listContentCallbackUrl | 



## integrationAccountSchemasCreateOrUpdate

> IntegrationAccountSchema integrationAccountSchemasCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, schemaName, apiVersion, schema)



Creates or updates an integration account schema.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationAccountSchemasApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let schemaName = "schemaName_example"; // String | The integration account schema name.
let apiVersion = "apiVersion_example"; // String | The API version.
let schema = new LogicManagementClient.IntegrationAccountSchema(); // IntegrationAccountSchema | The integration account schema.
apiInstance.integrationAccountSchemasCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, schemaName, apiVersion, schema, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **integrationAccountName** | **String**| The integration account name. | 
 **schemaName** | **String**| The integration account schema name. | 
 **apiVersion** | **String**| The API version. | 
 **schema** | [**IntegrationAccountSchema**](IntegrationAccountSchema.md)| The integration account schema. | 

### Return type

[**IntegrationAccountSchema**](IntegrationAccountSchema.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## integrationAccountSchemasDelete

> integrationAccountSchemasDelete(subscriptionId, resourceGroupName, integrationAccountName, schemaName, apiVersion)



Deletes an integration account schema.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationAccountSchemasApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let schemaName = "schemaName_example"; // String | The integration account schema name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationAccountSchemasDelete(subscriptionId, resourceGroupName, integrationAccountName, schemaName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **integrationAccountName** | **String**| The integration account name. | 
 **schemaName** | **String**| The integration account schema name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## integrationAccountSchemasGet

> IntegrationAccountSchema integrationAccountSchemasGet(subscriptionId, resourceGroupName, integrationAccountName, schemaName, apiVersion)



Gets an integration account schema.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationAccountSchemasApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let schemaName = "schemaName_example"; // String | The integration account schema name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationAccountSchemasGet(subscriptionId, resourceGroupName, integrationAccountName, schemaName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **integrationAccountName** | **String**| The integration account name. | 
 **schemaName** | **String**| The integration account schema name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**IntegrationAccountSchema**](IntegrationAccountSchema.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## integrationAccountSchemasList

> IntegrationAccountSchemaListResult integrationAccountSchemasList(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, opts)



Gets a list of integration account schemas.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationAccountSchemasApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let apiVersion = "apiVersion_example"; // String | The API version.
let opts = {
  'top': 56, // Number | The number of items to be included in the result.
  'filter': "filter_example" // String | The filter to apply on the operation. Options for filters include: SchemaType.
};
apiInstance.integrationAccountSchemasList(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **integrationAccountName** | **String**| The integration account name. | 
 **apiVersion** | **String**| The API version. | 
 **top** | **Number**| The number of items to be included in the result. | [optional] 
 **filter** | **String**| The filter to apply on the operation. Options for filters include: SchemaType. | [optional] 

### Return type

[**IntegrationAccountSchemaListResult**](IntegrationAccountSchemaListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## integrationAccountSchemasListContentCallbackUrl

> WorkflowTriggerCallbackUrl integrationAccountSchemasListContentCallbackUrl(subscriptionId, resourceGroupName, integrationAccountName, schemaName, apiVersion, listContentCallbackUrl)



Get the content callback url.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationAccountSchemasApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let schemaName = "schemaName_example"; // String | The integration account schema name.
let apiVersion = "apiVersion_example"; // String | The API version.
let listContentCallbackUrl = new LogicManagementClient.GetCallbackUrlParameters(); // GetCallbackUrlParameters | 
apiInstance.integrationAccountSchemasListContentCallbackUrl(subscriptionId, resourceGroupName, integrationAccountName, schemaName, apiVersion, listContentCallbackUrl, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **integrationAccountName** | **String**| The integration account name. | 
 **schemaName** | **String**| The integration account schema name. | 
 **apiVersion** | **String**| The API version. | 
 **listContentCallbackUrl** | [**GetCallbackUrlParameters**](GetCallbackUrlParameters.md)|  | 

### Return type

[**WorkflowTriggerCallbackUrl**](WorkflowTriggerCallbackUrl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

