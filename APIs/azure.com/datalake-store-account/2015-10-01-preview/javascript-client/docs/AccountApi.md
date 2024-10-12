# DataLakeStoreAccountManagementClient.AccountApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountCreate**](AccountApi.md#accountCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{name} | 
[**accountCreateOrUpdateFirewallRule**](AccountApi.md#accountCreateOrUpdateFirewallRule) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/firewallRules/{name} | 
[**accountDelete**](AccountApi.md#accountDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName} | 
[**accountDeleteFirewallRule**](AccountApi.md#accountDeleteFirewallRule) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/firewallRules/{firewallRuleName} | 
[**accountEnableKeyVault**](AccountApi.md#accountEnableKeyVault) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/enableKeyVault | 
[**accountGet**](AccountApi.md#accountGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName} | 
[**accountGetFirewallRule**](AccountApi.md#accountGetFirewallRule) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/firewallRules/{firewallRuleName} | 
[**accountList**](AccountApi.md#accountList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DataLakeStore/accounts | 
[**accountListByResourceGroup**](AccountApi.md#accountListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts | 
[**accountListFirewallRules**](AccountApi.md#accountListFirewallRules) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/firewallRules | 
[**accountUpdate**](AccountApi.md#accountUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{name} | 



## accountCreate

> DataLakeStoreAccount accountCreate(resourceGroupName, name, apiVersion, subscriptionId, parameters)



Creates the specified Data Lake Store account.

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.AccountApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group that contains the Data Lake Store account.
let name = "name_example"; // String | The name of the Data Lake Store account to create.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new DataLakeStoreAccountManagementClient.DataLakeStoreAccount(); // DataLakeStoreAccount | Parameters supplied to create the Data Lake Store account.
apiInstance.accountCreate(resourceGroupName, name, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Azure resource group that contains the Data Lake Store account. | 
 **name** | **String**| The name of the Data Lake Store account to create. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**DataLakeStoreAccount**](DataLakeStoreAccount.md)| Parameters supplied to create the Data Lake Store account. | 

### Return type

[**DataLakeStoreAccount**](DataLakeStoreAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/octet-stream
- **Accept**: application/json, text/json, application/octet-stream


## accountCreateOrUpdateFirewallRule

> FirewallRule accountCreateOrUpdateFirewallRule(resourceGroupName, accountName, name, apiVersion, subscriptionId, parameters)



Creates or updates the specified firewall rule.

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.AccountApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group that contains the Data Lake Store account.
let accountName = "accountName_example"; // String | The name of the Data Lake Store account to which to add the firewall rule.
let name = "name_example"; // String | The name of the firewall rule to create or update.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new DataLakeStoreAccountManagementClient.FirewallRule(); // FirewallRule | Parameters supplied to create the create firewall rule.
apiInstance.accountCreateOrUpdateFirewallRule(resourceGroupName, accountName, name, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Azure resource group that contains the Data Lake Store account. | 
 **accountName** | **String**| The name of the Data Lake Store account to which to add the firewall rule. | 
 **name** | **String**| The name of the firewall rule to create or update. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**FirewallRule**](FirewallRule.md)| Parameters supplied to create the create firewall rule. | 

### Return type

[**FirewallRule**](FirewallRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/octet-stream
- **Accept**: application/json, text/json, application/octet-stream


## accountDelete

> accountDelete(resourceGroupName, accountName, apiVersion, subscriptionId)



Deletes the specified Data Lake Store account.

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.AccountApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group that contains the Data Lake Store account.
let accountName = "accountName_example"; // String | The name of the Data Lake Store account to delete.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.accountDelete(resourceGroupName, accountName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Azure resource group that contains the Data Lake Store account. | 
 **accountName** | **String**| The name of the Data Lake Store account to delete. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## accountDeleteFirewallRule

> accountDeleteFirewallRule(resourceGroupName, accountName, firewallRuleName, apiVersion, subscriptionId)



Deletes the specified firewall rule from the specified Data Lake Store account

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.AccountApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group that contains the Data Lake Store account.
let accountName = "accountName_example"; // String | The name of the Data Lake Store account from which to delete the firewall rule.
let firewallRuleName = "firewallRuleName_example"; // String | The name of the firewall rule to delete.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.accountDeleteFirewallRule(resourceGroupName, accountName, firewallRuleName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Azure resource group that contains the Data Lake Store account. | 
 **accountName** | **String**| The name of the Data Lake Store account from which to delete the firewall rule. | 
 **firewallRuleName** | **String**| The name of the firewall rule to delete. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## accountEnableKeyVault

> accountEnableKeyVault(resourceGroupName, accountName, apiVersion, subscriptionId)



Attempts to enable a user managed key vault for encryption of the specified Data Lake Store account.

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.AccountApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group that contains the Data Lake Store account.
let accountName = "accountName_example"; // String | The name of the Data Lake Store account to attempt to enable the Key Vault for.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.accountEnableKeyVault(resourceGroupName, accountName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Azure resource group that contains the Data Lake Store account. | 
 **accountName** | **String**| The name of the Data Lake Store account to attempt to enable the Key Vault for. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## accountGet

> DataLakeStoreAccount accountGet(resourceGroupName, accountName, apiVersion, subscriptionId)



Gets the specified Data Lake Store account.

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.AccountApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group that contains the Data Lake Store account.
let accountName = "accountName_example"; // String | The name of the Data Lake Store account to retrieve.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.accountGet(resourceGroupName, accountName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Azure resource group that contains the Data Lake Store account. | 
 **accountName** | **String**| The name of the Data Lake Store account to retrieve. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**DataLakeStoreAccount**](DataLakeStoreAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/octet-stream


## accountGetFirewallRule

> FirewallRule accountGetFirewallRule(resourceGroupName, accountName, firewallRuleName, apiVersion, subscriptionId)



Gets the specified Data Lake Store firewall rule.

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.AccountApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group that contains the Data Lake Store account.
let accountName = "accountName_example"; // String | The name of the Data Lake Store account from which to get the firewall rule.
let firewallRuleName = "firewallRuleName_example"; // String | The name of the firewall rule to retrieve.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.accountGetFirewallRule(resourceGroupName, accountName, firewallRuleName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Azure resource group that contains the Data Lake Store account. | 
 **accountName** | **String**| The name of the Data Lake Store account from which to get the firewall rule. | 
 **firewallRuleName** | **String**| The name of the firewall rule to retrieve. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**FirewallRule**](FirewallRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/octet-stream


## accountList

> DataLakeStoreAccountListResult accountList(apiVersion, subscriptionId, opts)



Lists the Data Lake Store accounts within the subscription. The response includes a link to the next page of results, if any.

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.AccountApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'filter': "filter_example", // String | OData filter. Optional.
  'top': 56, // Number | The number of items to return. Optional.
  'skip': 56, // Number | The number of items to skip over before returning elements. Optional.
  'expand': "expand_example", // String | OData expansion. Expand related resources in line with the retrieved resources, e.g. Categories/$expand=Products would expand Product data in line with each Category entry. Optional.
  'select': "select_example", // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
  'orderby': "orderby_example", // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
  'count': true, // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
  'search': "search_example", // String | A free form search. A free-text search expression to match for whether a particular entry should be included in the feed, e.g. Categories?$search=blue OR green. Optional.
  'format': "format_example" // String | The desired return format. Return the response in particular format without access to request headers for standard content-type negotiation (e.g Orders?$format=json). Optional.
};
apiInstance.accountList(apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **filter** | **String**| OData filter. Optional. | [optional] 
 **top** | **Number**| The number of items to return. Optional. | [optional] 
 **skip** | **Number**| The number of items to skip over before returning elements. Optional. | [optional] 
 **expand** | **String**| OData expansion. Expand related resources in line with the retrieved resources, e.g. Categories/$expand&#x3D;Products would expand Product data in line with each Category entry. Optional. | [optional] 
 **select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] 
 **orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] 
 **count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] 
 **search** | **String**| A free form search. A free-text search expression to match for whether a particular entry should be included in the feed, e.g. Categories?$search&#x3D;blue OR green. Optional. | [optional] 
 **format** | **String**| The desired return format. Return the response in particular format without access to request headers for standard content-type negotiation (e.g Orders?$format&#x3D;json). Optional. | [optional] 

### Return type

[**DataLakeStoreAccountListResult**](DataLakeStoreAccountListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/octet-stream


## accountListByResourceGroup

> DataLakeStoreAccountListResult accountListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, opts)



Lists the Data Lake Store accounts within a specific resource group. The response includes a link to the next page of results, if any.

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.AccountApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group that contains the Data Lake Store account(s).
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let opts = {
  'filter': "filter_example", // String | OData filter. Optional.
  'top': 56, // Number | The number of items to return. Optional.
  'skip': 56, // Number | The number of items to skip over before returning elements. Optional.
  'expand': "expand_example", // String | OData expansion. Expand related resources in line with the retrieved resources, e.g. Categories/$expand=Products would expand Product data in line with each Category entry. Optional.
  'select': "select_example", // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
  'orderby': "orderby_example", // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
  'count': true, // Boolean | A Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
  'search': "search_example", // String | A free form search. A free-text search expression to match for whether a particular entry should be included in the feed, e.g. Categories?$search=blue OR green. Optional.
  'format': "format_example" // String | The desired return format. Return the response in particular format without access to request headers for standard content-type negotiation (e.g Orders?$format=json). Optional.
};
apiInstance.accountListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Azure resource group that contains the Data Lake Store account(s). | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **filter** | **String**| OData filter. Optional. | [optional] 
 **top** | **Number**| The number of items to return. Optional. | [optional] 
 **skip** | **Number**| The number of items to skip over before returning elements. Optional. | [optional] 
 **expand** | **String**| OData expansion. Expand related resources in line with the retrieved resources, e.g. Categories/$expand&#x3D;Products would expand Product data in line with each Category entry. Optional. | [optional] 
 **select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] 
 **orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] 
 **count** | **Boolean**| A Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] 
 **search** | **String**| A free form search. A free-text search expression to match for whether a particular entry should be included in the feed, e.g. Categories?$search&#x3D;blue OR green. Optional. | [optional] 
 **format** | **String**| The desired return format. Return the response in particular format without access to request headers for standard content-type negotiation (e.g Orders?$format&#x3D;json). Optional. | [optional] 

### Return type

[**DataLakeStoreAccountListResult**](DataLakeStoreAccountListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/octet-stream


## accountListFirewallRules

> DataLakeStoreFirewallRuleListResult accountListFirewallRules(resourceGroupName, accountName, apiVersion, subscriptionId)



Lists the Data Lake Store firewall rules within the specified Data Lake Store account.

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.AccountApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group that contains the Data Lake Store account.
let accountName = "accountName_example"; // String | The name of the Data Lake Store account from which to get the firewall rules.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.accountListFirewallRules(resourceGroupName, accountName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Azure resource group that contains the Data Lake Store account. | 
 **accountName** | **String**| The name of the Data Lake Store account from which to get the firewall rules. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**DataLakeStoreFirewallRuleListResult**](DataLakeStoreFirewallRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/octet-stream


## accountUpdate

> DataLakeStoreAccount accountUpdate(resourceGroupName, name, apiVersion, subscriptionId, parameters)



Updates the specified Data Lake Store account information.

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.AccountApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group that contains the Data Lake Store account.
let name = "name_example"; // String | The name of the Data Lake Store account to update.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new DataLakeStoreAccountManagementClient.DataLakeStoreAccount(); // DataLakeStoreAccount | Parameters supplied to update the Data Lake Store account.
apiInstance.accountUpdate(resourceGroupName, name, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Azure resource group that contains the Data Lake Store account. | 
 **name** | **String**| The name of the Data Lake Store account to update. | 
 **apiVersion** | **String**| Client Api Version. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**DataLakeStoreAccount**](DataLakeStoreAccount.md)| Parameters supplied to update the Data Lake Store account. | 

### Return type

[**DataLakeStoreAccount**](DataLakeStoreAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json, application/octet-stream
- **Accept**: application/json, text/json, application/octet-stream

