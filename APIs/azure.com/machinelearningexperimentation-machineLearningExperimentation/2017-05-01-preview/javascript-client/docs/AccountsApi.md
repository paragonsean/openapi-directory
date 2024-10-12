# MlTeamAccountManagementClient.AccountsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountsCreateOrUpdate**](AccountsApi.md#accountsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningExperimentation/accounts/{accountName} | 
[**accountsDelete**](AccountsApi.md#accountsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningExperimentation/accounts/{accountName} | 
[**accountsGet**](AccountsApi.md#accountsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningExperimentation/accounts/{accountName} | 
[**accountsList**](AccountsApi.md#accountsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.MachineLearningExperimentation/accounts | 
[**accountsListByResourceGroup**](AccountsApi.md#accountsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningExperimentation/accounts | 
[**accountsUpdate**](AccountsApi.md#accountsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningExperimentation/accounts/{accountName} | 



## accountsCreateOrUpdate

> Account accountsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, parameters)



Creates or updates a team account with the specified parameters.

### Example

```javascript
import MlTeamAccountManagementClient from 'ml_team_account_management_client';
let defaultClient = MlTeamAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MlTeamAccountManagementClient.AccountsApi();
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the machine learning team account belongs.
let accountName = "accountName_example"; // String | The name of the machine learning team account.
let parameters = new MlTeamAccountManagementClient.Account(); // Account | The parameters for creating or updating a machine learning team account.
apiInstance.accountsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the machine learning team account belongs. | 
 **accountName** | **String**| The name of the machine learning team account. | 
 **parameters** | [**Account**](Account.md)| The parameters for creating or updating a machine learning team account. | 

### Return type

[**Account**](Account.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## accountsDelete

> accountsDelete(apiVersion, subscriptionId, resourceGroupName, accountName)



Deletes a machine learning team account.

### Example

```javascript
import MlTeamAccountManagementClient from 'ml_team_account_management_client';
let defaultClient = MlTeamAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MlTeamAccountManagementClient.AccountsApi();
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the machine learning team account belongs.
let accountName = "accountName_example"; // String | The name of the machine learning team account.
apiInstance.accountsDelete(apiVersion, subscriptionId, resourceGroupName, accountName, (error, data, response) => {
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
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the machine learning team account belongs. | 
 **accountName** | **String**| The name of the machine learning team account. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsGet

> Account accountsGet(apiVersion, subscriptionId, resourceGroupName, accountName)



Gets the properties of the specified machine learning team account.

### Example

```javascript
import MlTeamAccountManagementClient from 'ml_team_account_management_client';
let defaultClient = MlTeamAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MlTeamAccountManagementClient.AccountsApi();
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the machine learning team account belongs.
let accountName = "accountName_example"; // String | The name of the machine learning team account.
apiInstance.accountsGet(apiVersion, subscriptionId, resourceGroupName, accountName, (error, data, response) => {
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
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the machine learning team account belongs. | 
 **accountName** | **String**| The name of the machine learning team account. | 

### Return type

[**Account**](Account.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsList

> AccountListResult accountsList(apiVersion, subscriptionId)



Lists all the available machine learning team accounts under the specified subscription.

### Example

```javascript
import MlTeamAccountManagementClient from 'ml_team_account_management_client';
let defaultClient = MlTeamAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MlTeamAccountManagementClient.AccountsApi();
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
apiInstance.accountsList(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 

### Return type

[**AccountListResult**](AccountListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsListByResourceGroup

> AccountListResult accountsListByResourceGroup(apiVersion, subscriptionId, resourceGroupName)



Lists all the available machine learning team accounts under the specified resource group.

### Example

```javascript
import MlTeamAccountManagementClient from 'ml_team_account_management_client';
let defaultClient = MlTeamAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MlTeamAccountManagementClient.AccountsApi();
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the machine learning team account belongs.
apiInstance.accountsListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, (error, data, response) => {
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
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the machine learning team account belongs. | 

### Return type

[**AccountListResult**](AccountListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsUpdate

> Account accountsUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, parameters)



Updates a machine learning team account with the specified parameters.

### Example

```javascript
import MlTeamAccountManagementClient from 'ml_team_account_management_client';
let defaultClient = MlTeamAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MlTeamAccountManagementClient.AccountsApi();
let apiVersion = "apiVersion_example"; // String | The client API version.
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the machine learning team account belongs.
let accountName = "accountName_example"; // String | The name of the machine learning team account.
let parameters = new MlTeamAccountManagementClient.AccountUpdateParameters(); // AccountUpdateParameters | The parameters for updating a machine learning team account.
apiInstance.accountsUpdate(apiVersion, subscriptionId, resourceGroupName, accountName, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| The client API version. | 
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the machine learning team account belongs. | 
 **accountName** | **String**| The name of the machine learning team account. | 
 **parameters** | [**AccountUpdateParameters**](AccountUpdateParameters.md)| The parameters for updating a machine learning team account. | 

### Return type

[**Account**](Account.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

