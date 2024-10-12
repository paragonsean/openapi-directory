# CostManagementClient.ExternalSubscriptionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**externalSubscriptionGet**](ExternalSubscriptionsApi.md#externalSubscriptionGet) | **GET** /providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName} | 
[**externalSubscriptionList**](ExternalSubscriptionsApi.md#externalSubscriptionList) | **GET** /providers/Microsoft.CostManagement/externalSubscriptions | 
[**externalSubscriptionListByExternalBillingAccount**](ExternalSubscriptionsApi.md#externalSubscriptionListByExternalBillingAccount) | **GET** /providers/Microsoft.CostManagement/externalBillingAccounts/{externalBillingAccountName}/externalSubscriptions | 
[**externalSubscriptionListByManagementGroup**](ExternalSubscriptionsApi.md#externalSubscriptionListByManagementGroup) | **GET** /providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.CostManagement/externalSubscriptions | 
[**externalSubscriptionUpdateManagementGroup**](ExternalSubscriptionsApi.md#externalSubscriptionUpdateManagementGroup) | **PUT** /providers/Microsoft.Management/managementGroups/{managementGroupId}/providers/Microsoft.CostManagement/externalSubscriptions/{externalSubscriptionName} | 



## externalSubscriptionGet

> ExternalSubscriptionDefinition externalSubscriptionGet(apiVersion, externalSubscriptionName, opts)



Get an ExternalSubscription definition

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ExternalSubscriptionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
let externalSubscriptionName = "externalSubscriptionName_example"; // String | External Subscription Name. (eg 'aws-{UsageAccountId}')
let opts = {
  'expand': "expand_example" // String | May be used to expand the collectionInfo property. By default, collectionInfo is not included.
};
apiInstance.externalSubscriptionGet(apiVersion, externalSubscriptionName, opts, (error, data, response) => {
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
 **externalSubscriptionName** | **String**| External Subscription Name. (eg &#39;aws-{UsageAccountId}&#39;) | 
 **expand** | **String**| May be used to expand the collectionInfo property. By default, collectionInfo is not included. | [optional] 

### Return type

[**ExternalSubscriptionDefinition**](ExternalSubscriptionDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## externalSubscriptionList

> ExternalSubscriptionDefinitionListResult externalSubscriptionList(apiVersion)



List all ExternalSubscription definitions

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ExternalSubscriptionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
apiInstance.externalSubscriptionList(apiVersion, (error, data, response) => {
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

[**ExternalSubscriptionDefinitionListResult**](ExternalSubscriptionDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## externalSubscriptionListByExternalBillingAccount

> ExternalSubscriptionDefinitionListResult externalSubscriptionListByExternalBillingAccount(apiVersion, externalBillingAccountName)



List all ExternalSubscriptions by ExternalBillingAccount definitions

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ExternalSubscriptionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
let externalBillingAccountName = "externalBillingAccountName_example"; // String | External Billing Account Name. (eg 'aws-{PayerAccountId}')
apiInstance.externalSubscriptionListByExternalBillingAccount(apiVersion, externalBillingAccountName, (error, data, response) => {
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

### Return type

[**ExternalSubscriptionDefinitionListResult**](ExternalSubscriptionDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## externalSubscriptionListByManagementGroup

> ExternalSubscriptionDefinitionListResult externalSubscriptionListByManagementGroup(apiVersion, managementGroupId, opts)



List all ExternalSubscription definitions for Management Group

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ExternalSubscriptionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
let managementGroupId = "managementGroupId_example"; // String | ManagementGroup ID
let opts = {
  'recurse': true // Boolean | The $recurse=true query string parameter allows returning externalSubscriptions associated with the specified managementGroup, or any of its descendants.
};
apiInstance.externalSubscriptionListByManagementGroup(apiVersion, managementGroupId, opts, (error, data, response) => {
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
 **managementGroupId** | **String**| ManagementGroup ID | 
 **recurse** | **Boolean**| The $recurse&#x3D;true query string parameter allows returning externalSubscriptions associated with the specified managementGroup, or any of its descendants. | [optional] 

### Return type

[**ExternalSubscriptionDefinitionListResult**](ExternalSubscriptionDefinitionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## externalSubscriptionUpdateManagementGroup

> externalSubscriptionUpdateManagementGroup(apiVersion, managementGroupId, externalSubscriptionName)



Updates the management group of an ExternalSubscription

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ExternalSubscriptionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
let managementGroupId = "managementGroupId_example"; // String | ManagementGroup ID
let externalSubscriptionName = "externalSubscriptionName_example"; // String | External Subscription Name. (eg 'aws-{UsageAccountId}')
apiInstance.externalSubscriptionUpdateManagementGroup(apiVersion, managementGroupId, externalSubscriptionName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-03-01-preview | 
 **managementGroupId** | **String**| ManagementGroup ID | 
 **externalSubscriptionName** | **String**| External Subscription Name. (eg &#39;aws-{UsageAccountId}&#39;) | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

