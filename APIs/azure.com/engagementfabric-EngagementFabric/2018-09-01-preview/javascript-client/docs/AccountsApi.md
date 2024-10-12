# EngagementFabric.AccountsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountsCreateOrUpdate**](AccountsApi.md#accountsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EngagementFabric/Accounts/{accountName} | Create or Update the EngagementFabric account
[**accountsDelete**](AccountsApi.md#accountsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EngagementFabric/Accounts/{accountName} | Delete the EngagementFabric account
[**accountsGet**](AccountsApi.md#accountsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EngagementFabric/Accounts/{accountName} | Get the EngagementFabric account
[**accountsList**](AccountsApi.md#accountsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.EngagementFabric/Accounts | List the EngagementFabric accounts in given subscription
[**accountsListByResourceGroup**](AccountsApi.md#accountsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EngagementFabric/Accounts | List EngagementFabric accounts in given resource group
[**accountsListChannelTypes**](AccountsApi.md#accountsListChannelTypes) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EngagementFabric/Accounts/{accountName}/listChannelTypes | List available EngagementFabric channel types and functions
[**accountsListKeys**](AccountsApi.md#accountsListKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EngagementFabric/Accounts/{accountName}/listKeys | List keys of the EngagementFabric account
[**accountsRegenerateKey**](AccountsApi.md#accountsRegenerateKey) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EngagementFabric/Accounts/{accountName}/regenerateKey | Regenerate key of the EngagementFabric account
[**accountsUpdate**](AccountsApi.md#accountsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EngagementFabric/Accounts/{accountName} | Update EngagementFabric account



## accountsCreateOrUpdate

> Account accountsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, account)

Create or Update the EngagementFabric account

### Example

```javascript
import EngagementFabric from 'engagement_fabric';

let apiInstance = new EngagementFabric.AccountsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | Resource Group Name
let accountName = "accountName_example"; // String | Account Name
let apiVersion = "apiVersion_example"; // String | API version
let account = new EngagementFabric.Account(); // Account | The EngagementFabric account description
apiInstance.accountsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, account, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription ID | 
 **resourceGroupName** | **String**| Resource Group Name | 
 **accountName** | **String**| Account Name | 
 **apiVersion** | **String**| API version | 
 **account** | [**Account**](Account.md)| The EngagementFabric account description | 

### Return type

[**Account**](Account.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## accountsDelete

> accountsDelete(subscriptionId, resourceGroupName, accountName, apiVersion)

Delete the EngagementFabric account

### Example

```javascript
import EngagementFabric from 'engagement_fabric';

let apiInstance = new EngagementFabric.AccountsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | Resource Group Name
let accountName = "accountName_example"; // String | Account Name
let apiVersion = "apiVersion_example"; // String | API version
apiInstance.accountsDelete(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription ID | 
 **resourceGroupName** | **String**| Resource Group Name | 
 **accountName** | **String**| Account Name | 
 **apiVersion** | **String**| API version | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsGet

> Account accountsGet(subscriptionId, resourceGroupName, accountName, apiVersion)

Get the EngagementFabric account

### Example

```javascript
import EngagementFabric from 'engagement_fabric';

let apiInstance = new EngagementFabric.AccountsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | Resource Group Name
let accountName = "accountName_example"; // String | Account Name
let apiVersion = "apiVersion_example"; // String | API version
apiInstance.accountsGet(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription ID | 
 **resourceGroupName** | **String**| Resource Group Name | 
 **accountName** | **String**| Account Name | 
 **apiVersion** | **String**| API version | 

### Return type

[**Account**](Account.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsList

> AccountList accountsList(subscriptionId, apiVersion)

List the EngagementFabric accounts in given subscription

### Example

```javascript
import EngagementFabric from 'engagement_fabric';

let apiInstance = new EngagementFabric.AccountsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription ID
let apiVersion = "apiVersion_example"; // String | API version
apiInstance.accountsList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription ID | 
 **apiVersion** | **String**| API version | 

### Return type

[**AccountList**](AccountList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsListByResourceGroup

> AccountList accountsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)

List EngagementFabric accounts in given resource group

### Example

```javascript
import EngagementFabric from 'engagement_fabric';

let apiInstance = new EngagementFabric.AccountsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | Resource Group Name
let apiVersion = "apiVersion_example"; // String | API version
apiInstance.accountsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription ID | 
 **resourceGroupName** | **String**| Resource Group Name | 
 **apiVersion** | **String**| API version | 

### Return type

[**AccountList**](AccountList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsListChannelTypes

> ChannelTypeDescriptionList accountsListChannelTypes(subscriptionId, resourceGroupName, accountName, apiVersion)

List available EngagementFabric channel types and functions

### Example

```javascript
import EngagementFabric from 'engagement_fabric';

let apiInstance = new EngagementFabric.AccountsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | Resource Group Name
let accountName = "accountName_example"; // String | Account Name
let apiVersion = "apiVersion_example"; // String | API version
apiInstance.accountsListChannelTypes(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription ID | 
 **resourceGroupName** | **String**| Resource Group Name | 
 **accountName** | **String**| Account Name | 
 **apiVersion** | **String**| API version | 

### Return type

[**ChannelTypeDescriptionList**](ChannelTypeDescriptionList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsListKeys

> KeyDescriptionList accountsListKeys(subscriptionId, resourceGroupName, accountName, apiVersion)

List keys of the EngagementFabric account

### Example

```javascript
import EngagementFabric from 'engagement_fabric';

let apiInstance = new EngagementFabric.AccountsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | Resource Group Name
let accountName = "accountName_example"; // String | Account Name
let apiVersion = "apiVersion_example"; // String | API version
apiInstance.accountsListKeys(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription ID | 
 **resourceGroupName** | **String**| Resource Group Name | 
 **accountName** | **String**| Account Name | 
 **apiVersion** | **String**| API version | 

### Return type

[**KeyDescriptionList**](KeyDescriptionList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsRegenerateKey

> KeyDescription accountsRegenerateKey(subscriptionId, resourceGroupName, accountName, apiVersion, parameter)

Regenerate key of the EngagementFabric account

### Example

```javascript
import EngagementFabric from 'engagement_fabric';

let apiInstance = new EngagementFabric.AccountsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | Resource Group Name
let accountName = "accountName_example"; // String | Account Name
let apiVersion = "apiVersion_example"; // String | API version
let parameter = new EngagementFabric.RegenerateKeyParameter(); // RegenerateKeyParameter | Parameters specifying the key to be regenerated
apiInstance.accountsRegenerateKey(subscriptionId, resourceGroupName, accountName, apiVersion, parameter, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription ID | 
 **resourceGroupName** | **String**| Resource Group Name | 
 **accountName** | **String**| Account Name | 
 **apiVersion** | **String**| API version | 
 **parameter** | [**RegenerateKeyParameter**](RegenerateKeyParameter.md)| Parameters specifying the key to be regenerated | 

### Return type

[**KeyDescription**](KeyDescription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## accountsUpdate

> Account accountsUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, accountPatch)

Update EngagementFabric account

### Example

```javascript
import EngagementFabric from 'engagement_fabric';

let apiInstance = new EngagementFabric.AccountsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription ID
let resourceGroupName = "resourceGroupName_example"; // String | Resource Group Name
let accountName = "accountName_example"; // String | Account Name
let apiVersion = "apiVersion_example"; // String | API version
let accountPatch = new EngagementFabric.AccountPatch(); // AccountPatch | The account patch
apiInstance.accountsUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, accountPatch, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription ID | 
 **resourceGroupName** | **String**| Resource Group Name | 
 **accountName** | **String**| Account Name | 
 **apiVersion** | **String**| API version | 
 **accountPatch** | [**AccountPatch**](AccountPatch.md)| The account patch | 

### Return type

[**Account**](Account.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

