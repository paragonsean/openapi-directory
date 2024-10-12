# ConsumptionManagementClient.CostTagsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**costTagsCreateOrUpdate**](CostTagsApi.md#costTagsCreateOrUpdate) | **PUT** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.Consumption/costTags | 
[**costTagsGet**](CostTagsApi.md#costTagsGet) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.Consumption/costTags | 



## costTagsCreateOrUpdate

> CostTags costTagsCreateOrUpdate(apiVersion, billingAccountId, parameters)



The operation to create or update cost tags associated with a billing account. Update operation requires latest eTag to be set in the request mandatorily. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.CostTagsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-03-31.
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let parameters = new ConsumptionManagementClient.CostTags(); // CostTags | Parameters supplied to the Create cost tags operation.
apiInstance.costTagsCreateOrUpdate(apiVersion, billingAccountId, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-03-31. | 
 **billingAccountId** | **String**| BillingAccount ID | 
 **parameters** | [**CostTags**](CostTags.md)| Parameters supplied to the Create cost tags operation. | 

### Return type

[**CostTags**](CostTags.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## costTagsGet

> CostTags costTagsGet(apiVersion, billingAccountId)



Get cost tags for a billing account.

### Example

```javascript
import ConsumptionManagementClient from 'consumption_management_client';
let defaultClient = ConsumptionManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ConsumptionManagementClient.CostTagsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-03-31.
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
apiInstance.costTagsGet(apiVersion, billingAccountId, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-03-31. | 
 **billingAccountId** | **String**| BillingAccount ID | 

### Return type

[**CostTags**](CostTags.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

