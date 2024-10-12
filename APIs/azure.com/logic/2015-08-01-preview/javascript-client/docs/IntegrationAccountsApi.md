# LogicManagementClient.IntegrationAccountsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**integrationAccountsCreateOrUpdate**](IntegrationAccountsApi.md#integrationAccountsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName} | 
[**integrationAccountsDelete**](IntegrationAccountsApi.md#integrationAccountsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName} | 
[**integrationAccountsGet**](IntegrationAccountsApi.md#integrationAccountsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName} | 
[**integrationAccountsListByResourceGroup**](IntegrationAccountsApi.md#integrationAccountsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts | 
[**integrationAccountsListBySubscription**](IntegrationAccountsApi.md#integrationAccountsListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Logic/integrationAccounts | 
[**integrationAccountsListCallbackUrl**](IntegrationAccountsApi.md#integrationAccountsListCallbackUrl) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/listCallbackUrl | 
[**integrationAccountsUpdate**](IntegrationAccountsApi.md#integrationAccountsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName} | 



## integrationAccountsCreateOrUpdate

> IntegrationAccount integrationAccountsCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, integrationAccount)



Creates or updates an integration account.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';

let apiInstance = new LogicManagementClient.IntegrationAccountsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let apiVersion = "apiVersion_example"; // String | The API version.
let integrationAccount = new LogicManagementClient.IntegrationAccount(); // IntegrationAccount | The integration account.
apiInstance.integrationAccountsCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, integrationAccount, (error, data, response) => {
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
 **integrationAccount** | [**IntegrationAccount**](IntegrationAccount.md)| The integration account. | 

### Return type

[**IntegrationAccount**](IntegrationAccount.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## integrationAccountsDelete

> integrationAccountsDelete(subscriptionId, resourceGroupName, integrationAccountName, apiVersion)



Deletes an integration account.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';

let apiInstance = new LogicManagementClient.IntegrationAccountsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationAccountsDelete(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## integrationAccountsGet

> IntegrationAccount integrationAccountsGet(subscriptionId, resourceGroupName, integrationAccountName, apiVersion)



Gets an integration account.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';

let apiInstance = new LogicManagementClient.IntegrationAccountsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationAccountsGet(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, (error, data, response) => {
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

### Return type

[**IntegrationAccount**](IntegrationAccount.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## integrationAccountsListByResourceGroup

> IntegrationAccountListResult integrationAccountsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts)



Gets a list of integration accounts by resource group.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';

let apiInstance = new LogicManagementClient.IntegrationAccountsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let apiVersion = "apiVersion_example"; // String | The API version.
let opts = {
  'top': 56 // Number | The number of items to be included in the result.
};
apiInstance.integrationAccountsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The API version. | 
 **top** | **Number**| The number of items to be included in the result. | [optional] 

### Return type

[**IntegrationAccountListResult**](IntegrationAccountListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## integrationAccountsListBySubscription

> IntegrationAccountListResult integrationAccountsListBySubscription(subscriptionId, apiVersion, opts)



Gets a list of integration accounts by subscription.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';

let apiInstance = new LogicManagementClient.IntegrationAccountsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let apiVersion = "apiVersion_example"; // String | The API version.
let opts = {
  'top': 56 // Number | The number of items to be included in the result.
};
apiInstance.integrationAccountsListBySubscription(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The API version. | 
 **top** | **Number**| The number of items to be included in the result. | [optional] 

### Return type

[**IntegrationAccountListResult**](IntegrationAccountListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## integrationAccountsListCallbackUrl

> CallbackUrl integrationAccountsListCallbackUrl(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, parameters)



Lists the integration account callback URL.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';

let apiInstance = new LogicManagementClient.IntegrationAccountsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let apiVersion = "apiVersion_example"; // String | The API version.
let parameters = new LogicManagementClient.ListCallbackUrlParameters(); // ListCallbackUrlParameters | The callback URL parameters.
apiInstance.integrationAccountsListCallbackUrl(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, parameters, (error, data, response) => {
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
 **parameters** | [**ListCallbackUrlParameters**](ListCallbackUrlParameters.md)| The callback URL parameters. | 

### Return type

[**CallbackUrl**](CallbackUrl.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## integrationAccountsUpdate

> IntegrationAccount integrationAccountsUpdate(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, integrationAccount)



Updates an integration account.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';

let apiInstance = new LogicManagementClient.IntegrationAccountsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let apiVersion = "apiVersion_example"; // String | The API version.
let integrationAccount = new LogicManagementClient.IntegrationAccount(); // IntegrationAccount | The integration account.
apiInstance.integrationAccountsUpdate(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, integrationAccount, (error, data, response) => {
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
 **integrationAccount** | [**IntegrationAccount**](IntegrationAccount.md)| The integration account. | 

### Return type

[**IntegrationAccount**](IntegrationAccount.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

