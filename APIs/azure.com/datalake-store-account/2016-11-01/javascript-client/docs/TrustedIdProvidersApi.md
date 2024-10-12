# DataLakeStoreAccountManagementClient.TrustedIdProvidersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trustedIdProvidersCreateOrUpdate**](TrustedIdProvidersApi.md#trustedIdProvidersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/trustedIdProviders/{trustedIdProviderName} | 
[**trustedIdProvidersDelete**](TrustedIdProvidersApi.md#trustedIdProvidersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/trustedIdProviders/{trustedIdProviderName} | 
[**trustedIdProvidersGet**](TrustedIdProvidersApi.md#trustedIdProvidersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/trustedIdProviders/{trustedIdProviderName} | 
[**trustedIdProvidersListByAccount**](TrustedIdProvidersApi.md#trustedIdProvidersListByAccount) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/trustedIdProviders | 
[**trustedIdProvidersUpdate**](TrustedIdProvidersApi.md#trustedIdProvidersUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataLakeStore/accounts/{accountName}/trustedIdProviders/{trustedIdProviderName} | 



## trustedIdProvidersCreateOrUpdate

> TrustedIdProvider trustedIdProvidersCreateOrUpdate(subscriptionId, resourceGroupName, accountName, trustedIdProviderName, apiVersion, parameters)



Creates or updates the specified trusted identity provider. During update, the trusted identity provider with the specified name will be replaced with this new provider

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.TrustedIdProvidersApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
let accountName = "accountName_example"; // String | The name of the Data Lake Store account.
let trustedIdProviderName = "trustedIdProviderName_example"; // String | The name of the trusted identity provider. This is used for differentiation of providers in the account.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let parameters = new DataLakeStoreAccountManagementClient.CreateOrUpdateTrustedIdProviderParameters(); // CreateOrUpdateTrustedIdProviderParameters | Parameters supplied to create or replace the trusted identity provider.
apiInstance.trustedIdProvidersCreateOrUpdate(subscriptionId, resourceGroupName, accountName, trustedIdProviderName, apiVersion, parameters, (error, data, response) => {
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
 **trustedIdProviderName** | **String**| The name of the trusted identity provider. This is used for differentiation of providers in the account. | 
 **apiVersion** | **String**| Client Api Version. | 
 **parameters** | [**CreateOrUpdateTrustedIdProviderParameters**](CreateOrUpdateTrustedIdProviderParameters.md)| Parameters supplied to create or replace the trusted identity provider. | 

### Return type

[**TrustedIdProvider**](TrustedIdProvider.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## trustedIdProvidersDelete

> trustedIdProvidersDelete(subscriptionId, resourceGroupName, accountName, trustedIdProviderName, apiVersion)



Deletes the specified trusted identity provider from the specified Data Lake Store account

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.TrustedIdProvidersApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
let accountName = "accountName_example"; // String | The name of the Data Lake Store account.
let trustedIdProviderName = "trustedIdProviderName_example"; // String | The name of the trusted identity provider to delete.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.trustedIdProvidersDelete(subscriptionId, resourceGroupName, accountName, trustedIdProviderName, apiVersion, (error, data, response) => {
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
 **trustedIdProviderName** | **String**| The name of the trusted identity provider to delete. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## trustedIdProvidersGet

> TrustedIdProvider trustedIdProvidersGet(subscriptionId, resourceGroupName, accountName, trustedIdProviderName, apiVersion)



Gets the specified Data Lake Store trusted identity provider.

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.TrustedIdProvidersApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
let accountName = "accountName_example"; // String | The name of the Data Lake Store account.
let trustedIdProviderName = "trustedIdProviderName_example"; // String | The name of the trusted identity provider to retrieve.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.trustedIdProvidersGet(subscriptionId, resourceGroupName, accountName, trustedIdProviderName, apiVersion, (error, data, response) => {
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
 **trustedIdProviderName** | **String**| The name of the trusted identity provider to retrieve. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**TrustedIdProvider**](TrustedIdProvider.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trustedIdProvidersListByAccount

> TrustedIdProviderListResult trustedIdProvidersListByAccount(subscriptionId, resourceGroupName, accountName, apiVersion)



Lists the Data Lake Store trusted identity providers within the specified Data Lake Store account.

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.TrustedIdProvidersApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
let accountName = "accountName_example"; // String | The name of the Data Lake Store account.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.trustedIdProvidersListByAccount(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
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

[**TrustedIdProviderListResult**](TrustedIdProviderListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trustedIdProvidersUpdate

> TrustedIdProvider trustedIdProvidersUpdate(subscriptionId, resourceGroupName, accountName, trustedIdProviderName, apiVersion, opts)



Updates the specified trusted identity provider.

### Example

```javascript
import DataLakeStoreAccountManagementClient from 'data_lake_store_account_management_client';
let defaultClient = DataLakeStoreAccountManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DataLakeStoreAccountManagementClient.TrustedIdProvidersApi();
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Azure resource group.
let accountName = "accountName_example"; // String | The name of the Data Lake Store account.
let trustedIdProviderName = "trustedIdProviderName_example"; // String | The name of the trusted identity provider. This is used for differentiation of providers in the account.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let opts = {
  'parameters': new DataLakeStoreAccountManagementClient.UpdateTrustedIdProviderParameters() // UpdateTrustedIdProviderParameters | Parameters supplied to update the trusted identity provider.
};
apiInstance.trustedIdProvidersUpdate(subscriptionId, resourceGroupName, accountName, trustedIdProviderName, apiVersion, opts, (error, data, response) => {
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
 **trustedIdProviderName** | **String**| The name of the trusted identity provider. This is used for differentiation of providers in the account. | 
 **apiVersion** | **String**| Client Api Version. | 
 **parameters** | [**UpdateTrustedIdProviderParameters**](UpdateTrustedIdProviderParameters.md)| Parameters supplied to update the trusted identity provider. | [optional] 

### Return type

[**TrustedIdProvider**](TrustedIdProvider.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

