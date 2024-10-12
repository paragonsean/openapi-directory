# CostManagementClient.ReportsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reportConfigCreateOrUpdate**](ReportsApi.md#reportConfigCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/reportconfigs/{reportConfigName} | 
[**reportConfigCreateOrUpdateByResourceGroupName**](ReportsApi.md#reportConfigCreateOrUpdateByResourceGroupName) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CostManagement/reportconfigs/{reportConfigName} | 
[**reportConfigDelete**](ReportsApi.md#reportConfigDelete) | **DELETE** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/reportconfigs/{reportConfigName} | 
[**reportConfigDeleteByResourceGroupName**](ReportsApi.md#reportConfigDeleteByResourceGroupName) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CostManagement/reportconfigs/{reportConfigName} | 
[**reportConfigGet**](ReportsApi.md#reportConfigGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/reportconfigs/{reportConfigName} | 
[**reportConfigGetByResourceGroupName**](ReportsApi.md#reportConfigGetByResourceGroupName) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CostManagement/reportconfigs/{reportConfigName} | 
[**reportConfigList**](ReportsApi.md#reportConfigList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.CostManagement/reportconfigs | 
[**reportConfigListByResourceGroupName**](ReportsApi.md#reportConfigListByResourceGroupName) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CostManagement/reportconfigs | 



## reportConfigCreateOrUpdate

> ReportConfig reportConfigCreateOrUpdate(apiVersion, subscriptionId, reportConfigName, parameters)



The operation to create or update a report config. Update operation requires latest eTag to be set in the request mandatorily. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ReportsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let reportConfigName = "reportConfigName_example"; // String | Report Config Name.
let parameters = new CostManagementClient.ReportConfig(); // ReportConfig | Parameters supplied to the CreateOrUpdate Report Config operation.
apiInstance.reportConfigCreateOrUpdate(apiVersion, subscriptionId, reportConfigName, parameters, (error, data, response) => {
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
 **reportConfigName** | **String**| Report Config Name. | 
 **parameters** | [**ReportConfig**](ReportConfig.md)| Parameters supplied to the CreateOrUpdate Report Config operation. | 

### Return type

[**ReportConfig**](ReportConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## reportConfigCreateOrUpdateByResourceGroupName

> ReportConfig reportConfigCreateOrUpdateByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, reportConfigName, parameters)



The operation to create or update a report config. Update operation requires latest eTag to be set in the request mandatorily. You may obtain the latest eTag by performing a get operation. Create operation does not require eTag.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ReportsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
let reportConfigName = "reportConfigName_example"; // String | Report Config Name.
let parameters = new CostManagementClient.ReportConfig(); // ReportConfig | Parameters supplied to the CreateOrUpdate Report Config operation.
apiInstance.reportConfigCreateOrUpdateByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, reportConfigName, parameters, (error, data, response) => {
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
 **reportConfigName** | **String**| Report Config Name. | 
 **parameters** | [**ReportConfig**](ReportConfig.md)| Parameters supplied to the CreateOrUpdate Report Config operation. | 

### Return type

[**ReportConfig**](ReportConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## reportConfigDelete

> reportConfigDelete(apiVersion, subscriptionId, reportConfigName)



The operation to delete a report.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ReportsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let reportConfigName = "reportConfigName_example"; // String | Report Config Name.
apiInstance.reportConfigDelete(apiVersion, subscriptionId, reportConfigName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-05-31. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **reportConfigName** | **String**| Report Config Name. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportConfigDeleteByResourceGroupName

> reportConfigDeleteByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, reportConfigName)



The operation to delete a report config.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ReportsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
let reportConfigName = "reportConfigName_example"; // String | Report Config Name.
apiInstance.reportConfigDeleteByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, reportConfigName, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. The current version is 2018-05-31. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **resourceGroupName** | **String**| Azure Resource Group Name. | 
 **reportConfigName** | **String**| Report Config Name. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportConfigGet

> ReportConfig reportConfigGet(apiVersion, subscriptionId, reportConfigName)



Gets the report config for a subscription by report config name.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ReportsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let reportConfigName = "reportConfigName_example"; // String | Report Config Name.
apiInstance.reportConfigGet(apiVersion, subscriptionId, reportConfigName, (error, data, response) => {
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
 **reportConfigName** | **String**| Report Config Name. | 

### Return type

[**ReportConfig**](ReportConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportConfigGetByResourceGroupName

> ReportConfig reportConfigGetByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, reportConfigName)



Gets the report config for a resource group under a subscription by report config name.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ReportsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
let reportConfigName = "reportConfigName_example"; // String | Report Config Name.
apiInstance.reportConfigGetByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, reportConfigName, (error, data, response) => {
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
 **reportConfigName** | **String**| Report Config Name. | 

### Return type

[**ReportConfig**](ReportConfig.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportConfigList

> ReportConfigListResult reportConfigList(apiVersion, subscriptionId)



Lists all report configs for a subscription.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ReportsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
apiInstance.reportConfigList(apiVersion, subscriptionId, (error, data, response) => {
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

### Return type

[**ReportConfigListResult**](ReportConfigListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportConfigListByResourceGroupName

> ReportConfigListResult reportConfigListByResourceGroupName(apiVersion, subscriptionId, resourceGroupName)



Lists all report configs for a resource group under a subscription.

### Example

```javascript
import CostManagementClient from 'cost_management_client';
let defaultClient = CostManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CostManagementClient.ReportsApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. The current version is 2018-05-31.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | Azure Resource Group Name.
apiInstance.reportConfigListByResourceGroupName(apiVersion, subscriptionId, resourceGroupName, (error, data, response) => {
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

### Return type

[**ReportConfigListResult**](ReportConfigListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

