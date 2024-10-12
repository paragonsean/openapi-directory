# DataLakeStoreAccountManagementClient.AccountsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountsCheckNameAvailability**](AccountsApi.md#accountsCheckNameAvailability) | **POST** /subscriptions/{subscriptionId}/providers/Microsoft.DataLakeStore/locations/{location}/checkNameAvailability | 
[**accountsCreate**](AccountsApi.md#accountsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName} | 
[**accountsDelete**](AccountsApi.md#accountsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName} | 
[**accountsEnableKeyVault**](AccountsApi.md#accountsEnableKeyVault) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/enableKeyVault | 
[**accountsGet**](AccountsApi.md#accountsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName} | 
[**accountsList**](AccountsApi.md#accountsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.DataLakeStore/accounts | 
[**accountsListByResourceGroup**](AccountsApi.md#accountsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts | 
[**accountsUpdate**](AccountsApi.md#accountsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName} | 



## accountsCheckNameAvailability

> NameAvailabilityInformation accountsCheckNameAvailability(subscriptionId, location, apiVersion, parameters)



Checks whether the specified account name is available or taken.

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.AccountsApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let location = "location_example"; // String | The resource location without whitespace.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new DataLakeStoreAccountManagementClient.CheckNameAvailabilityParameters(); // CheckNameAvailabilityParameters | Parameters supplied to check the Data Lake Store account name availability.
apiInstance.accountsCheckNameAvailability(subscriptionId, location, apiVersion, parameters, (error, data, response) => {
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
 **location** | **String**| The resource location without whitespace. | 
 **apiVersion** | **String**| Client Api Version. | 
 **parameters** | [**CheckNameAvailabilityParameters**](CheckNameAvailabilityParameters.md)| Parameters supplied to check the Data Lake Store account name availability. | 

### Return type

[**NameAvailabilityInformation**](NameAvailabilityInformation.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## accountsCreate

> DataLakeStoreAccount accountsCreate(subscriptionId, resourceGroupName, accountName, apiVersion, parameters)



Creates the specified Data Lake Store account.

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.AccountsApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
let accountName = "accountName_example"; // String | The name of the Data Lake Store account.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new DataLakeStoreAccountManagementClient.CreateDataLakeStoreAccountParameters(); // CreateDataLakeStoreAccountParameters | Parameters supplied to create the Data Lake Store account.
apiInstance.accountsCreate(subscriptionId, resourceGroupName, accountName, apiVersion, parameters, (error, data, response) => {
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
 **parameters** | [**CreateDataLakeStoreAccountParameters**](CreateDataLakeStoreAccountParameters.md)| Parameters supplied to create the Data Lake Store account. | 

### Return type

[**DataLakeStoreAccount**](DataLakeStoreAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## accountsDelete

> accountsDelete(subscriptionId, resourceGroupName, accountName, apiVersion)



Deletes the specified Data Lake Store account.

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.AccountsApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
let accountName = "accountName_example"; // String | The name of the Data Lake Store account.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the Azure resource group. | 
 **accountName** | **String**| The name of the Data Lake Store account. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## accountsEnableKeyVault

> accountsEnableKeyVault(subscriptionId, resourceGroupName, accountName, apiVersion)



Attempts to enable a user managed Key Vault for encryption of the specified Data Lake Store account.

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.AccountsApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
let accountName = "accountName_example"; // String | The name of the Data Lake Store account.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.accountsEnableKeyVault(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## accountsGet

> DataLakeStoreAccount accountsGet(subscriptionId, resourceGroupName, accountName, apiVersion)



Gets the specified Data Lake Store account.

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.AccountsApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
let accountName = "accountName_example"; // String | The name of the Data Lake Store account.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
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
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **resourceGroupName** | **String**| The name of the Azure resource group. | 
 **accountName** | **String**| The name of the Data Lake Store account. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**DataLakeStoreAccount**](DataLakeStoreAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsList

> DataLakeStoreAccountListResult accountsList(subscriptionId, apiVersion, opts)



Lists the Data Lake Store accounts within the subscription. The response includes a link to the next page of results, if any.

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.AccountsApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | OData filter. Optional.
  'top': 56, // Number | The number of items to return. Optional.
  'skip': 56, // Number | The number of items to skip over before returning elements. Optional.
  'select': "select_example", // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
  'orderby': "orderby_example", // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
  'count': true // Boolean | The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
};
apiInstance.accountsList(subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| OData filter. Optional. | [optional] 
 **top** | **Number**| The number of items to return. Optional. | [optional] 
 **skip** | **Number**| The number of items to skip over before returning elements. Optional. | [optional] 
 **select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] 
 **orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] 
 **count** | **Boolean**| The Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] 

### Return type

[**DataLakeStoreAccountListResult**](DataLakeStoreAccountListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsListByResourceGroup

> DataLakeStoreAccountListResult accountsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts)



Lists the Data Lake Store accounts within a specific resource group. The response includes a link to the next page of results, if any.

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.AccountsApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'filter': "filter_example", // String | OData filter. Optional.
  'top': 56, // Number | The number of items to return. Optional.
  'skip': 56, // Number | The number of items to skip over before returning elements. Optional.
  'select': "select_example", // String | OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select=CategoryName,Description. Optional.
  'orderby': "orderby_example", // String | OrderBy clause. One or more comma-separated expressions with an optional \"asc\" (the default) or \"desc\" depending on the order you'd like the values sorted, e.g. Categories?$orderby=CategoryName desc. Optional.
  'count': true // Boolean | A Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count=true. Optional.
};
apiInstance.accountsListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **filter** | **String**| OData filter. Optional. | [optional] 
 **top** | **Number**| The number of items to return. Optional. | [optional] 
 **skip** | **Number**| The number of items to skip over before returning elements. Optional. | [optional] 
 **select** | **String**| OData Select statement. Limits the properties on each entry to just those requested, e.g. Categories?$select&#x3D;CategoryName,Description. Optional. | [optional] 
 **orderby** | **String**| OrderBy clause. One or more comma-separated expressions with an optional \&quot;asc\&quot; (the default) or \&quot;desc\&quot; depending on the order you&#39;d like the values sorted, e.g. Categories?$orderby&#x3D;CategoryName desc. Optional. | [optional] 
 **count** | **Boolean**| A Boolean value of true or false to request a count of the matching resources included with the resources in the response, e.g. Categories?$count&#x3D;true. Optional. | [optional] 

### Return type

[**DataLakeStoreAccountListResult**](DataLakeStoreAccountListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountsUpdate

> DataLakeStoreAccount accountsUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, parameters)



Updates the specified Data Lake Store account information.

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.AccountsApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
let accountName = "accountName_example"; // String | The name of the Data Lake Store account.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new DataLakeStoreAccountManagementClient.UpdateDataLakeStoreAccountParameters(); // UpdateDataLakeStoreAccountParameters | Parameters supplied to update the Data Lake Store account.
apiInstance.accountsUpdate(subscriptionId, resourceGroupName, accountName, apiVersion, parameters, (error, data, response) => {
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
 **parameters** | [**UpdateDataLakeStoreAccountParameters**](UpdateDataLakeStoreAccountParameters.md)| Parameters supplied to update the Data Lake Store account. | 

### Return type

[**DataLakeStoreAccount**](DataLakeStoreAccount.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

