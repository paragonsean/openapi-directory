# CostManagementClient.ExternalBillingAccountsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**externalBillingAccountGet**](ExternalBillingAccountsApi.md#externalBillingAccountGet) | **GET** /providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName} | 
[**externalBillingAccountList**](ExternalBillingAccountsApi.md#externalBillingAccountList) | **GET** /providers/Microsoft.CostManagement/externalBillingAccounts | 



## externalBillingAccountGet

> ExternalBillingAccountDefinition externalBillingAccountGet(apiVersion, externalBillingAccountName, opts)



Get a ExternalBillingAccount definition

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ExternalBillingAccountsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
let externalBillingAccountName = "externalBillingAccountName_example"; // String | External Billing Account Name. (eg 'aws-{PayerAccountId}')
let opts = {
  'expand': "expand_example" // String | May be used to expand the collectionInfo property. By default, collectionInfo is not included.
};
apiInstance.externalBillingAccountGet(apiVersion, externalBillingAccountName, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-03-01-preview | 
 **externalBillingAccountName** | **String**| External Billing Account Name. (eg &#39;aws-{PayerAccountId}&#39;) | 
 **expand** | **String**| May be used to expand the collectionInfo property. By default, collectionInfo is not included. | [optional] 

### Return type

[**ExternalBillingAccountDefinition**](ExternalBillingAccountDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## externalBillingAccountList

> ExternalBillingAccountDefinitionListResult externalBillingAccountList(apiVersion)



List all ExternalBillingAccount definitions

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ExternalBillingAccountsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
apiInstance.externalBillingAccountList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-03-01-preview | 

### Return type

[**ExternalBillingAccountDefinitionListResult**](ExternalBillingAccountDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

