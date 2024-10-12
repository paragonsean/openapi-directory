# BillingManagementClient.AgreementsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agreementsGet**](AgreementsApi.md#agreementsGet) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/agreements/{agreementName} | 
[**agreementsListByBillingAccount**](AgreementsApi.md#agreementsListByBillingAccount) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountName}/agreements | 



## agreementsGet

> Agreement agreementsGet(apiVersion, billingAccountName, agreementName, opts)



Get the agreement by name.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.AgreementsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let agreementName = "agreementName_example"; // String | Agreement Id.
let opts = {
  'expand': "expand_example" // String | May be used to expand the participants.
};
apiInstance.agreementsGet(apiVersion, billingAccountName, agreementName, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | 
 **billingAccountName** | **String**| billing Account Id. | 
 **agreementName** | **String**| Agreement Id. | 
 **expand** | **String**| May be used to expand the participants. | [optional] 

### Return type

[**Agreement**](Agreement.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## agreementsListByBillingAccount

> AgreementListResult agreementsListByBillingAccount(apiVersion, billingAccountName, opts)



Lists all agreements for a billing account.

### Example

```javascript
import BillingManagementClient from 'billing_management_client';
let defaultClient = BillingManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BillingManagementClient.AgreementsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2019-10-01-preview.
let billingAccountName = "billingAccountName_example"; // String | billing Account Id.
let opts = {
  'expand': "expand_example" // String | May be used to expand the participants.
};
apiInstance.agreementsListByBillingAccount(apiVersion, billingAccountName, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2019-10-01-preview. | 
 **billingAccountName** | **String**| billing Account Id. | 
 **expand** | **String**| May be used to expand the participants. | [optional] 

### Return type

[**AgreementListResult**](AgreementListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

