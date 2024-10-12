# SqlManagementClient.BlobAuditingApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**databaseBlobAuditingPoliciesCreateOrUpdate**](BlobAuditingApi.md#databaseBlobAuditingPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/auditingSettings/{blobAuditingPolicyName} | 
[**databaseBlobAuditingPoliciesGet**](BlobAuditingApi.md#databaseBlobAuditingPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/auditingSettings/{blobAuditingPolicyName} | 
[**databaseBlobAuditingPoliciesListByDatabase**](BlobAuditingApi.md#databaseBlobAuditingPoliciesListByDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/auditingSettings | 
[**extendedDatabaseBlobAuditingPoliciesCreateOrUpdate**](BlobAuditingApi.md#extendedDatabaseBlobAuditingPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/extendedAuditingSettings/{blobAuditingPolicyName} | 
[**extendedDatabaseBlobAuditingPoliciesGet**](BlobAuditingApi.md#extendedDatabaseBlobAuditingPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/extendedAuditingSettings/{blobAuditingPolicyName} | 
[**extendedServerBlobAuditingPoliciesCreateOrUpdate**](BlobAuditingApi.md#extendedServerBlobAuditingPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/extendedAuditingSettings/{blobAuditingPolicyName} | 
[**extendedServerBlobAuditingPoliciesGet**](BlobAuditingApi.md#extendedServerBlobAuditingPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/extendedAuditingSettings/{blobAuditingPolicyName} | 
[**serverBlobAuditingPoliciesCreateOrUpdate**](BlobAuditingApi.md#serverBlobAuditingPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/auditingSettings/{blobAuditingPolicyName} | 
[**serverBlobAuditingPoliciesGet**](BlobAuditingApi.md#serverBlobAuditingPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/auditingSettings/{blobAuditingPolicyName} | 
[**serverBlobAuditingPoliciesListByServer**](BlobAuditingApi.md#serverBlobAuditingPoliciesListByServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/auditingSettings | 



## databaseBlobAuditingPoliciesCreateOrUpdate

> DatabaseBlobAuditingPolicy databaseBlobAuditingPoliciesCreateOrUpdate(resourceGroupName, serverName, databaseName, blobAuditingPolicyName, subscriptionId, apiVersion, parameters)



Creates or updates a database&#39;s blob auditing policy.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.BlobAuditingApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database.
let blobAuditingPolicyName = "blobAuditingPolicyName_example"; // String | The name of the blob auditing policy.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let parameters = new SqlManagementClient.DatabaseBlobAuditingPolicy(); // DatabaseBlobAuditingPolicy | The database blob auditing policy.
apiInstance.databaseBlobAuditingPoliciesCreateOrUpdate(resourceGroupName, serverName, databaseName, blobAuditingPolicyName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **databaseName** | **String**| The name of the database. | 
 **blobAuditingPolicyName** | **String**| The name of the blob auditing policy. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **parameters** | [**DatabaseBlobAuditingPolicy**](DatabaseBlobAuditingPolicy.md)| The database blob auditing policy. | 

### Return type

[**DatabaseBlobAuditingPolicy**](DatabaseBlobAuditingPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databaseBlobAuditingPoliciesGet

> DatabaseBlobAuditingPolicy databaseBlobAuditingPoliciesGet(resourceGroupName, serverName, databaseName, blobAuditingPolicyName, subscriptionId, apiVersion)



Gets a database&#39;s blob auditing policy.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.BlobAuditingApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database.
let blobAuditingPolicyName = "blobAuditingPolicyName_example"; // String | The name of the blob auditing policy.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.databaseBlobAuditingPoliciesGet(resourceGroupName, serverName, databaseName, blobAuditingPolicyName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **databaseName** | **String**| The name of the database. | 
 **blobAuditingPolicyName** | **String**| The name of the blob auditing policy. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**DatabaseBlobAuditingPolicy**](DatabaseBlobAuditingPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseBlobAuditingPoliciesListByDatabase

> DatabaseBlobAuditingPolicyListResult databaseBlobAuditingPoliciesListByDatabase(resourceGroupName, serverName, databaseName, subscriptionId, apiVersion)



Lists auditing settings of a database.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.BlobAuditingApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.databaseBlobAuditingPoliciesListByDatabase(resourceGroupName, serverName, databaseName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **databaseName** | **String**| The name of the database. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**DatabaseBlobAuditingPolicyListResult**](DatabaseBlobAuditingPolicyListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## extendedDatabaseBlobAuditingPoliciesCreateOrUpdate

> ExtendedDatabaseBlobAuditingPolicy extendedDatabaseBlobAuditingPoliciesCreateOrUpdate(resourceGroupName, serverName, databaseName, blobAuditingPolicyName, subscriptionId, apiVersion, parameters)



Creates or updates an extended database&#39;s blob auditing policy.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.BlobAuditingApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database.
let blobAuditingPolicyName = "blobAuditingPolicyName_example"; // String | The name of the blob auditing policy.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let parameters = new SqlManagementClient.ExtendedDatabaseBlobAuditingPolicy(); // ExtendedDatabaseBlobAuditingPolicy | The extended database blob auditing policy.
apiInstance.extendedDatabaseBlobAuditingPoliciesCreateOrUpdate(resourceGroupName, serverName, databaseName, blobAuditingPolicyName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **databaseName** | **String**| The name of the database. | 
 **blobAuditingPolicyName** | **String**| The name of the blob auditing policy. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **parameters** | [**ExtendedDatabaseBlobAuditingPolicy**](ExtendedDatabaseBlobAuditingPolicy.md)| The extended database blob auditing policy. | 

### Return type

[**ExtendedDatabaseBlobAuditingPolicy**](ExtendedDatabaseBlobAuditingPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## extendedDatabaseBlobAuditingPoliciesGet

> ExtendedDatabaseBlobAuditingPolicy extendedDatabaseBlobAuditingPoliciesGet(resourceGroupName, serverName, databaseName, blobAuditingPolicyName, subscriptionId, apiVersion)



Gets an extended database&#39;s blob auditing policy.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.BlobAuditingApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database.
let blobAuditingPolicyName = "blobAuditingPolicyName_example"; // String | The name of the blob auditing policy.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.extendedDatabaseBlobAuditingPoliciesGet(resourceGroupName, serverName, databaseName, blobAuditingPolicyName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **databaseName** | **String**| The name of the database. | 
 **blobAuditingPolicyName** | **String**| The name of the blob auditing policy. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**ExtendedDatabaseBlobAuditingPolicy**](ExtendedDatabaseBlobAuditingPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## extendedServerBlobAuditingPoliciesCreateOrUpdate

> ExtendedServerBlobAuditingPolicy extendedServerBlobAuditingPoliciesCreateOrUpdate(resourceGroupName, serverName, blobAuditingPolicyName, subscriptionId, apiVersion, parameters)



Creates or updates an extended server&#39;s blob auditing policy.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.BlobAuditingApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let blobAuditingPolicyName = "blobAuditingPolicyName_example"; // String | The name of the blob auditing policy.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let parameters = new SqlManagementClient.ExtendedServerBlobAuditingPolicy(); // ExtendedServerBlobAuditingPolicy | Properties of extended blob auditing policy
apiInstance.extendedServerBlobAuditingPoliciesCreateOrUpdate(resourceGroupName, serverName, blobAuditingPolicyName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **blobAuditingPolicyName** | **String**| The name of the blob auditing policy. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **parameters** | [**ExtendedServerBlobAuditingPolicy**](ExtendedServerBlobAuditingPolicy.md)| Properties of extended blob auditing policy | 

### Return type

[**ExtendedServerBlobAuditingPolicy**](ExtendedServerBlobAuditingPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## extendedServerBlobAuditingPoliciesGet

> ExtendedServerBlobAuditingPolicy extendedServerBlobAuditingPoliciesGet(resourceGroupName, serverName, blobAuditingPolicyName, subscriptionId, apiVersion)



Gets an extended server&#39;s blob auditing policy.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.BlobAuditingApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let blobAuditingPolicyName = "blobAuditingPolicyName_example"; // String | The name of the blob auditing policy.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.extendedServerBlobAuditingPoliciesGet(resourceGroupName, serverName, blobAuditingPolicyName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **blobAuditingPolicyName** | **String**| The name of the blob auditing policy. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**ExtendedServerBlobAuditingPolicy**](ExtendedServerBlobAuditingPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serverBlobAuditingPoliciesCreateOrUpdate

> ServerBlobAuditingPolicy serverBlobAuditingPoliciesCreateOrUpdate(resourceGroupName, serverName, blobAuditingPolicyName, subscriptionId, apiVersion, parameters)



Creates or updates a server&#39;s blob auditing policy.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.BlobAuditingApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let blobAuditingPolicyName = "blobAuditingPolicyName_example"; // String | The name of the blob auditing policy.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let parameters = new SqlManagementClient.ServerBlobAuditingPolicy(); // ServerBlobAuditingPolicy | Properties of blob auditing policy
apiInstance.serverBlobAuditingPoliciesCreateOrUpdate(resourceGroupName, serverName, blobAuditingPolicyName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **blobAuditingPolicyName** | **String**| The name of the blob auditing policy. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **parameters** | [**ServerBlobAuditingPolicy**](ServerBlobAuditingPolicy.md)| Properties of blob auditing policy | 

### Return type

[**ServerBlobAuditingPolicy**](ServerBlobAuditingPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## serverBlobAuditingPoliciesGet

> ServerBlobAuditingPolicy serverBlobAuditingPoliciesGet(resourceGroupName, serverName, blobAuditingPolicyName, subscriptionId, apiVersion)



Gets a server&#39;s blob auditing policy.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.BlobAuditingApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let blobAuditingPolicyName = "blobAuditingPolicyName_example"; // String | The name of the blob auditing policy.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.serverBlobAuditingPoliciesGet(resourceGroupName, serverName, blobAuditingPolicyName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **blobAuditingPolicyName** | **String**| The name of the blob auditing policy. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**ServerBlobAuditingPolicy**](ServerBlobAuditingPolicy.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serverBlobAuditingPoliciesListByServer

> ServerBlobAuditingPolicyListResult serverBlobAuditingPoliciesListByServer(resourceGroupName, serverName, subscriptionId, apiVersion)



Lists auditing settings of a server.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.BlobAuditingApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.serverBlobAuditingPoliciesListByServer(resourceGroupName, serverName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**ServerBlobAuditingPolicyListResult**](ServerBlobAuditingPolicyListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

