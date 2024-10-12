# CostManagementClient.ShowbackRulesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**showbackRuleCreateUpdateRule**](ShowbackRulesApi.md#showbackRuleCreateUpdateRule) | **PUT** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/showbackRules/{ruleName} | 
[**showbackRuleGetBillingAccountId**](ShowbackRulesApi.md#showbackRuleGetBillingAccountId) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/showbackRules/{ruleName} | 
[**showbackRulesList**](ShowbackRulesApi.md#showbackRulesList) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/showbackRules | 



## showbackRuleCreateUpdateRule

> ShowbackRule showbackRuleCreateUpdateRule(apiVersion, billingAccountId, ruleName, showbackRule)



Create/Update showback rule for billing account.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ShowbackRulesApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let ruleName = "ruleName_example"; // String | Showback rule name
let showbackRule = new CostManagementClient.ShowbackRule(); // ShowbackRule | Showback rule to create or update.
apiInstance.showbackRuleCreateUpdateRule(apiVersion, billingAccountId, ruleName, showbackRule, (error, data, response) => {
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
 **billingAccountId** | **String**| BillingAccount ID | 
 **ruleName** | **String**| Showback rule name | 
 **showbackRule** | [**ShowbackRule**](ShowbackRule.md)| Showback rule to create or update. | 

### Return type

[**ShowbackRule**](ShowbackRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## showbackRuleGetBillingAccountId

> ShowbackRule showbackRuleGetBillingAccountId(apiVersion, billingAccountId, ruleName)



Gets the showback rule by rule name.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ShowbackRulesApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let ruleName = "ruleName_example"; // String | Showback rule name
apiInstance.showbackRuleGetBillingAccountId(apiVersion, billingAccountId, ruleName, (error, data, response) => {
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
 **billingAccountId** | **String**| BillingAccount ID | 
 **ruleName** | **String**| Showback rule name | 

### Return type

[**ShowbackRule**](ShowbackRule.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## showbackRulesList

> ShowbackRuleListResult showbackRulesList(apiVersion, billingAccountId)



Get list all Showback Rules.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ShowbackRulesApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-03-01-preview
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
apiInstance.showbackRulesList(apiVersion, billingAccountId, (error, data, response) => {
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
 **billingAccountId** | **String**| BillingAccount ID | 

### Return type

[**ShowbackRuleListResult**](ShowbackRuleListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

