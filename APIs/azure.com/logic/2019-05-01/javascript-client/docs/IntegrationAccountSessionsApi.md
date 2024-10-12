# LogicManagementClient.IntegrationAccountSessionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**integrationAccountSessionsCreateOrUpdate**](IntegrationAccountSessionsApi.md#integrationAccountSessionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/sessions/{sessionName} | 
[**integrationAccountSessionsDelete**](IntegrationAccountSessionsApi.md#integrationAccountSessionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/sessions/{sessionName} | 
[**integrationAccountSessionsGet**](IntegrationAccountSessionsApi.md#integrationAccountSessionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/sessions/{sessionName} | 
[**integrationAccountSessionsList**](IntegrationAccountSessionsApi.md#integrationAccountSessionsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/sessions | 



## integrationAccountSessionsCreateOrUpdate

> IntegrationAccountSession integrationAccountSessionsCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, sessionName, apiVersion, session)



Creates or updates an integration account session.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationAccountSessionsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let sessionName = "sessionName_example"; // String | The integration account session name.
let apiVersion = "apiVersion_example"; // String | The API version.
let session = new LogicManagementClient.IntegrationAccountSession(); // IntegrationAccountSession | The integration account session.
apiInstance.integrationAccountSessionsCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, sessionName, apiVersion, session, (error, data, response) => {
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
 **sessionName** | **String**| The integration account session name. | 
 **apiVersion** | **String**| The API version. | 
 **session** | [**IntegrationAccountSession**](IntegrationAccountSession.md)| The integration account session. | 

### Return type

[**IntegrationAccountSession**](IntegrationAccountSession.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## integrationAccountSessionsDelete

> integrationAccountSessionsDelete(subscriptionId, resourceGroupName, integrationAccountName, sessionName, apiVersion)



Deletes an integration account session.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationAccountSessionsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let sessionName = "sessionName_example"; // String | The integration account session name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationAccountSessionsDelete(subscriptionId, resourceGroupName, integrationAccountName, sessionName, apiVersion, (error, data, response) => {
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
 **sessionName** | **String**| The integration account session name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## integrationAccountSessionsGet

> IntegrationAccountSession integrationAccountSessionsGet(subscriptionId, resourceGroupName, integrationAccountName, sessionName, apiVersion)



Gets an integration account session.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationAccountSessionsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let sessionName = "sessionName_example"; // String | The integration account session name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationAccountSessionsGet(subscriptionId, resourceGroupName, integrationAccountName, sessionName, apiVersion, (error, data, response) => {
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
 **sessionName** | **String**| The integration account session name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**IntegrationAccountSession**](IntegrationAccountSession.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## integrationAccountSessionsList

> IntegrationAccountSessionListResult integrationAccountSessionsList(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, opts)



Gets a list of integration account sessions.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationAccountSessionsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let apiVersion = "apiVersion_example"; // String | The API version.
let opts = {
  'top': 56, // Number | The number of items to be included in the result.
  'filter': "filter_example" // String | The filter to apply on the operation. Options for filters include: ChangedTime.
};
apiInstance.integrationAccountSessionsList(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, opts, (error, data, response) => {
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
 **filter** | **String**| The filter to apply on the operation. Options for filters include: ChangedTime. | [optional] 

### Return type

[**IntegrationAccountSessionListResult**](IntegrationAccountSessionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

