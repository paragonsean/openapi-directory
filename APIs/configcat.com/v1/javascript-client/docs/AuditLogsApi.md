# ConfigCatPublicManagementApi.AuditLogsApi

All URIs are relative to *https://api.configcat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAuditlogs**](AuditLogsApi.md#getAuditlogs) | **GET** /v1/products/{productId}/auditlogs | List Audit log items for Product
[**getDeletedSettings**](AuditLogsApi.md#getDeletedSettings) | **GET** /v1/configs/{configId}/deleted-settings | List Deleted Settings
[**getOrganizationAuditlogs**](AuditLogsApi.md#getOrganizationAuditlogs) | **GET** /v1/organizations/{organizationId}/auditlogs | List Audit log items for Organization



## getAuditlogs

> [AuditLogItemModel] getAuditlogs(productId, opts)

List Audit log items for Product

This endpoint returns the list of Audit log items for a given Product  and the result can be optionally filtered by Config and/or Environment.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.AuditLogsApi();
let productId = "productId_example"; // String | The identifier of the Product.
let opts = {
  'configId': "configId_example", // String | The identifier of the Config.
  'environmentId': "environmentId_example", // String | The identifier of the Environment.
  'auditLogType': new ConfigCatPublicManagementApi.AuditLogType(), // AuditLogType | Filter Audit logs by Audit log type.
  'fromUtcDateTime': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter Audit logs by starting UTC date.
  'toUtcDateTime': new Date("2013-10-20T19:20:30+01:00") // Date | Filter Audit logs by ending UTC date.
};
apiInstance.getAuditlogs(productId, opts, (error, data, response) => {
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
 **productId** | **String**| The identifier of the Product. | 
 **configId** | **String**| The identifier of the Config. | [optional] 
 **environmentId** | **String**| The identifier of the Environment. | [optional] 
 **auditLogType** | [**AuditLogType**](.md)| Filter Audit logs by Audit log type. | [optional] 
 **fromUtcDateTime** | **Date**| Filter Audit logs by starting UTC date. | [optional] 
 **toUtcDateTime** | **Date**| Filter Audit logs by ending UTC date. | [optional] 

### Return type

[**[AuditLogItemModel]**](AuditLogItemModel.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json, application/json


## getDeletedSettings

> [SettingModelHaljson] getDeletedSettings(configId)

List Deleted Settings

This endpoint returns the list of Feature Flags and Settings that were deleted from the given Config.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.AuditLogsApi();
let configId = "configId_example"; // String | The identifier of the Config.
apiInstance.getDeletedSettings(configId, (error, data, response) => {
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
 **configId** | **String**| The identifier of the Config. | 

### Return type

[**[SettingModelHaljson]**](SettingModelHaljson.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json, application/json


## getOrganizationAuditlogs

> [AuditLogItemModel] getOrganizationAuditlogs(organizationId, opts)

List Audit log items for Organization

This endpoint returns the list of Audit log items for a given Organization  and the result can be optionally filtered by Product and/or Config and/or Environment.

### Example

```javascript
import ConfigCatPublicManagementApi from 'config_cat_public_management_api';
let defaultClient = ConfigCatPublicManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: Basic
let Basic = defaultClient.authentications['Basic'];
Basic.username = 'YOUR USERNAME';
Basic.password = 'YOUR PASSWORD';

let apiInstance = new ConfigCatPublicManagementApi.AuditLogsApi();
let organizationId = "organizationId_example"; // String | The identifier of the Organization.
let opts = {
  'productId': "productId_example", // String | The identifier of the Product.
  'configId': "configId_example", // String | The identifier of the Config.
  'environmentId': "environmentId_example", // String | The identifier of the Environment.
  'auditLogType': new ConfigCatPublicManagementApi.AuditLogType(), // AuditLogType | Filter Audit logs by Audit log type.
  'fromUtcDateTime': new Date("2013-10-20T19:20:30+01:00"), // Date | Filter Audit logs by starting UTC date.
  'toUtcDateTime': new Date("2013-10-20T19:20:30+01:00") // Date | Filter Audit logs by ending UTC date.
};
apiInstance.getOrganizationAuditlogs(organizationId, opts, (error, data, response) => {
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
 **organizationId** | **String**| The identifier of the Organization. | 
 **productId** | **String**| The identifier of the Product. | [optional] 
 **configId** | **String**| The identifier of the Config. | [optional] 
 **environmentId** | **String**| The identifier of the Environment. | [optional] 
 **auditLogType** | [**AuditLogType**](.md)| Filter Audit logs by Audit log type. | [optional] 
 **fromUtcDateTime** | **Date**| Filter Audit logs by starting UTC date. | [optional] 
 **toUtcDateTime** | **Date**| Filter Audit logs by ending UTC date. | [optional] 

### Return type

[**[AuditLogItemModel]**](AuditLogItemModel.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/hal+json, application/json

