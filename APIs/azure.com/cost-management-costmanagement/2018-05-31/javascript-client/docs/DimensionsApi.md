# CostManagementClient.DimensionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billingAccountDimensionsList**](DimensionsApi.md#billingAccountDimensionsList) | **GET** /providers/Microsoft.Billing/billingAccounts/{billingAccountId}/providers/Microsoft.CostManagement/dimensions | 
[**resourceGroupDimensionsList**](DimensionsApi.md#resourceGroupDimensionsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CostManagement/dimensions | 
[**subscriptionDimensionsList**](DimensionsApi.md#subscriptionDimensionsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/dimensions | 



## billingAccountDimensionsList

> DimensionsListResult billingAccountDimensionsList(apiVersion, billingAccountId, opts)



Lists the dimensions by billingAccount Id.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.DimensionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
let billingAccountId = "billingAccountId_example"; // String | BillingAccount ID
let opts = {
  'filter': "filter_example", // String | May be used to filter dimensions by properties/category, properties/usageStart, properties/usageEnd. Supported operators are 'eq','lt', 'gt', 'le', 'ge'.
  'expand': "expand_example", // String | May be used to expand the properties/data within a dimension category. By default, data is not included when listing dimensions.
  'skiptoken': "skiptoken_example", // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
  'top': 56 // Number | May be used to limit the number of results to the most recent N dimension data.
};
apiInstance.billingAccountDimensionsList(apiVersion, billingAccountId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-05-31. | 
 **billingAccountId** | **String**| BillingAccount ID | 
 **filter** | **String**| May be used to filter dimensions by properties/category, properties/usageStart, properties/usageEnd. Supported operators are &#39;eq&#39;,&#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;. | [optional] 
 **expand** | **String**| May be used to expand the properties/data within a dimension category. By default, data is not included when listing dimensions. | [optional] 
 **skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] 
 **top** | **Number**| May be used to limit the number of results to the most recent N dimension data. | [optional] 

### Return type

[**DimensionsListResult**](DimensionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resourceGroupDimensionsList

> DimensionsListResult resourceGroupDimensionsList(apiVersion, subscriptionId, resourceGroupName, opts)



Lists the dimensions by resource group Id.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.DimensionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
let opts = {
  'filter': "filter_example", // String | May be used to filter dimensions by properties/category, properties/usageStart, properties/usageEnd. Supported operators are 'eq','lt', 'gt', 'le', 'ge'.
  'expand': "expand_example", // String | May be used to expand the properties/data within a dimension category. By default, data is not included when listing dimensions.
  'skiptoken': "skiptoken_example", // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
  'top': 56 // Number | May be used to limit the number of results to the most recent N dimension data.
};
apiInstance.resourceGroupDimensionsList(apiVersion, subscriptionId, resourceGroupName, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-05-31. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **resourceGroupName** | **String**| Azure Resource Group Name. | 
 **filter** | **String**| May be used to filter dimensions by properties/category, properties/usageStart, properties/usageEnd. Supported operators are &#39;eq&#39;,&#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;. | [optional] 
 **expand** | **String**| May be used to expand the properties/data within a dimension category. By default, data is not included when listing dimensions. | [optional] 
 **skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] 
 **top** | **Number**| May be used to limit the number of results to the most recent N dimension data. | [optional] 

### Return type

[**DimensionsListResult**](DimensionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## subscriptionDimensionsList

> DimensionsListResult subscriptionDimensionsList(apiVersion, subscriptionId, opts)



Lists the dimensions by subscription Id.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.DimensionsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let opts = {
  'filter': "filter_example", // String | May be used to filter dimensions by properties/category, properties/usageStart, properties/usageEnd. Supported operators are 'eq','lt', 'gt', 'le', 'ge'.
  'expand': "expand_example", // String | May be used to expand the properties/data within a dimension category. By default, data is not included when listing dimensions.
  'skiptoken': "skiptoken_example", // String | Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
  'top': 56 // Number | May be used to limit the number of results to the most recent N dimension data.
};
apiInstance.subscriptionDimensionsList(apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-05-31. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **filter** | **String**| May be used to filter dimensions by properties/category, properties/usageStart, properties/usageEnd. Supported operators are &#39;eq&#39;,&#39;lt&#39;, &#39;gt&#39;, &#39;le&#39;, &#39;ge&#39;. | [optional] 
 **expand** | **String**| May be used to expand the properties/data within a dimension category. By default, data is not included when listing dimensions. | [optional] 
 **skiptoken** | **String**| Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls. | [optional] 
 **top** | **Number**| May be used to limit the number of results to the most recent N dimension data. | [optional] 

### Return type

[**DimensionsListResult**](DimensionsListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

