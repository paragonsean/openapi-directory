# DataLakeStoreAccountManagementClient.VirtualNetworkRulesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualNetworkRulesCreateOrUpdate**](VirtualNetworkRulesApi.md#virtualNetworkRulesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/virtualNetworkRules/{virtualNetworkRuleName} | 
[**virtualNetworkRulesDelete**](VirtualNetworkRulesApi.md#virtualNetworkRulesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/virtualNetworkRules/{virtualNetworkRuleName} | 
[**virtualNetworkRulesGet**](VirtualNetworkRulesApi.md#virtualNetworkRulesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/virtualNetworkRules/{virtualNetworkRuleName} | 
[**virtualNetworkRulesListByAccount**](VirtualNetworkRulesApi.md#virtualNetworkRulesListByAccount) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/virtualNetworkRules | 
[**virtualNetworkRulesUpdate**](VirtualNetworkRulesApi.md#virtualNetworkRulesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/virtualNetworkRules/{virtualNetworkRuleName} | 



## virtualNetworkRulesCreateOrUpdate

> VirtualNetworkRule virtualNetworkRulesCreateOrUpdate(subscriptionId, resourceGroupName, accountName, virtualNetworkRuleName, apiVersion, parameters)



Creates or updates the specified virtual network rule. During update, the virtual network rule with the specified name will be replaced with this new virtual network rule.

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.VirtualNetworkRulesApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
let accountName = "accountName_example"; // String | The name of the Data Lake Store account.
let virtualNetworkRuleName = "virtualNetworkRuleName_example"; // String | The name of the virtual network rule to create or update.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new DataLakeStoreAccountManagementClient.CreateOrUpdateVirtualNetworkRuleParameters(); // CreateOrUpdateVirtualNetworkRuleParameters | Parameters supplied to create or update the virtual network rule.
apiInstance.virtualNetworkRulesCreateOrUpdate(subscriptionId, resourceGroupName, accountName, virtualNetworkRuleName, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the Azure resource group. | 
 **accountName** | **String**| The name of the Data Lake Store account. | 
 **virtualNetworkRuleName** | **String**| The name of the virtual network rule to create or update. | 
 **apiVersion** | **String**| Client Api Version. | 
 **parameters** | [**CreateOrUpdateVirtualNetworkRuleParameters**](CreateOrUpdateVirtualNetworkRuleParameters.md)| Parameters supplied to create or update the virtual network rule. | 

### Return type

[**VirtualNetworkRule**](VirtualNetworkRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## virtualNetworkRulesDelete

> virtualNetworkRulesDelete(subscriptionId, resourceGroupName, accountName, virtualNetworkRuleName, apiVersion)



Deletes the specified virtual network rule from the specified Data Lake Store account.

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.VirtualNetworkRulesApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
let accountName = "accountName_example"; // String | The name of the Data Lake Store account.
let virtualNetworkRuleName = "virtualNetworkRuleName_example"; // String | The name of the virtual network rule to delete.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.virtualNetworkRulesDelete(subscriptionId, resourceGroupName, accountName, virtualNetworkRuleName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the Azure resource group. | 
 **accountName** | **String**| The name of the Data Lake Store account. | 
 **virtualNetworkRuleName** | **String**| The name of the virtual network rule to delete. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## virtualNetworkRulesGet

> VirtualNetworkRule virtualNetworkRulesGet(subscriptionId, resourceGroupName, accountName, virtualNetworkRuleName, apiVersion)



Gets the specified Data Lake Store virtual network rule.

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.VirtualNetworkRulesApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
let accountName = "accountName_example"; // String | The name of the Data Lake Store account.
let virtualNetworkRuleName = "virtualNetworkRuleName_example"; // String | The name of the virtual network rule to retrieve.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.virtualNetworkRulesGet(subscriptionId, resourceGroupName, accountName, virtualNetworkRuleName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the Azure resource group. | 
 **accountName** | **String**| The name of the Data Lake Store account. | 
 **virtualNetworkRuleName** | **String**| The name of the virtual network rule to retrieve. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**VirtualNetworkRule**](VirtualNetworkRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualNetworkRulesListByAccount

> VirtualNetworkRuleListResult virtualNetworkRulesListByAccount(subscriptionId, resourceGroupName, accountName, apiVersion)



Lists the Data Lake Store virtual network rules within the specified Data Lake Store account.

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.VirtualNetworkRulesApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
let accountName = "accountName_example"; // String | The name of the Data Lake Store account.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.virtualNetworkRulesListByAccount(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the Azure resource group. | 
 **accountName** | **String**| The name of the Data Lake Store account. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**VirtualNetworkRuleListResult**](VirtualNetworkRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## virtualNetworkRulesUpdate

> VirtualNetworkRule virtualNetworkRulesUpdate(subscriptionId, resourceGroupName, accountName, virtualNetworkRuleName, apiVersion, opts)



Updates the specified virtual network rule.

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.VirtualNetworkRulesApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
let accountName = "accountName_example"; // String | The name of the Data Lake Store account.
let virtualNetworkRuleName = "virtualNetworkRuleName_example"; // String | The name of the virtual network rule to update.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'parameters': new DataLakeStoreAccountManagementClient.UpdateVirtualNetworkRuleParameters() // UpdateVirtualNetworkRuleParameters | Parameters supplied to update the virtual network rule.
};
apiInstance.virtualNetworkRulesUpdate(subscriptionId, resourceGroupName, accountName, virtualNetworkRuleName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the Azure resource group. | 
 **accountName** | **String**| The name of the Data Lake Store account. | 
 **virtualNetworkRuleName** | **String**| The name of the virtual network rule to update. | 
 **apiVersion** | **String**| Client Api Version. | 
 **parameters** | [**UpdateVirtualNetworkRuleParameters**](UpdateVirtualNetworkRuleParameters.md)| Parameters supplied to update the virtual network rule. | [optional] 

### Return type

[**VirtualNetworkRule**](VirtualNetworkRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

