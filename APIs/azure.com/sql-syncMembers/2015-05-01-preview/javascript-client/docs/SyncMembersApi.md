# SqlManagementClient.SyncMembersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**syncMembersCreateOrUpdate**](SyncMembersApi.md#syncMembersCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/syncGroups/{syncGroupName}/syncMembers/{syncMemberName} | 
[**syncMembersDelete**](SyncMembersApi.md#syncMembersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/syncGroups/{syncGroupName}/syncMembers/{syncMemberName} | 
[**syncMembersGet**](SyncMembersApi.md#syncMembersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/syncGroups/{syncGroupName}/syncMembers/{syncMemberName} | 
[**syncMembersListBySyncGroup**](SyncMembersApi.md#syncMembersListBySyncGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/syncGroups/{syncGroupName}/syncMembers | 
[**syncMembersListMemberSchemas**](SyncMembersApi.md#syncMembersListMemberSchemas) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/syncGroups/{syncGroupName}/syncMembers/{syncMemberName}/schemas | 
[**syncMembersRefreshMemberSchema**](SyncMembersApi.md#syncMembersRefreshMemberSchema) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/syncGroups/{syncGroupName}/syncMembers/{syncMemberName}/refreshSchema | 
[**syncMembersUpdate**](SyncMembersApi.md#syncMembersUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/syncGroups/{syncGroupName}/syncMembers/{syncMemberName} | 



## syncMembersCreateOrUpdate

> SyncMember syncMembersCreateOrUpdate(resourceGroupName, serverName, databaseName, syncGroupName, syncMemberName, subscriptionId, apiVersion, parameters)



Creates or updates a sync member.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.SyncMembersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database on which the sync group is hosted.
let syncGroupName = "syncGroupName_example"; // String | The name of the sync group on which the sync member is hosted.
let syncMemberName = "syncMemberName_example"; // String | The name of the sync member.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let parameters = new SqlManagementClient.SyncMember(); // SyncMember | The requested sync member resource state.
apiInstance.syncMembersCreateOrUpdate(resourceGroupName, serverName, databaseName, syncGroupName, syncMemberName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **databaseName** | **String**| The name of the database on which the sync group is hosted. | 
 **syncGroupName** | **String**| The name of the sync group on which the sync member is hosted. | 
 **syncMemberName** | **String**| The name of the sync member. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **parameters** | [**SyncMember**](SyncMember.md)| The requested sync member resource state. | 

### Return type

[**SyncMember**](SyncMember.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## syncMembersDelete

> syncMembersDelete(resourceGroupName, serverName, databaseName, syncGroupName, syncMemberName, subscriptionId, apiVersion)



Deletes a sync member.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.SyncMembersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database on which the sync group is hosted.
let syncGroupName = "syncGroupName_example"; // String | The name of the sync group on which the sync member is hosted.
let syncMemberName = "syncMemberName_example"; // String | The name of the sync member.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.syncMembersDelete(resourceGroupName, serverName, databaseName, syncGroupName, syncMemberName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **databaseName** | **String**| The name of the database on which the sync group is hosted. | 
 **syncGroupName** | **String**| The name of the sync group on which the sync member is hosted. | 
 **syncMemberName** | **String**| The name of the sync member. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## syncMembersGet

> SyncMember syncMembersGet(resourceGroupName, serverName, databaseName, syncGroupName, syncMemberName, subscriptionId, apiVersion)



Gets a sync member.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.SyncMembersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database on which the sync group is hosted.
let syncGroupName = "syncGroupName_example"; // String | The name of the sync group on which the sync member is hosted.
let syncMemberName = "syncMemberName_example"; // String | The name of the sync member.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.syncMembersGet(resourceGroupName, serverName, databaseName, syncGroupName, syncMemberName, subscriptionId, apiVersion, (error, data, response) => {
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
 **databaseName** | **String**| The name of the database on which the sync group is hosted. | 
 **syncGroupName** | **String**| The name of the sync group on which the sync member is hosted. | 
 **syncMemberName** | **String**| The name of the sync member. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**SyncMember**](SyncMember.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## syncMembersListBySyncGroup

> SyncMemberListResult syncMembersListBySyncGroup(resourceGroupName, serverName, databaseName, syncGroupName, subscriptionId, apiVersion)



Lists sync members in the given sync group.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.SyncMembersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database on which the sync group is hosted.
let syncGroupName = "syncGroupName_example"; // String | The name of the sync group.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.syncMembersListBySyncGroup(resourceGroupName, serverName, databaseName, syncGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **databaseName** | **String**| The name of the database on which the sync group is hosted. | 
 **syncGroupName** | **String**| The name of the sync group. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**SyncMemberListResult**](SyncMemberListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## syncMembersListMemberSchemas

> SyncFullSchemaPropertiesListResult syncMembersListMemberSchemas(resourceGroupName, serverName, databaseName, syncGroupName, syncMemberName, subscriptionId, apiVersion)



Gets a sync member database schema.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.SyncMembersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database on which the sync group is hosted.
let syncGroupName = "syncGroupName_example"; // String | The name of the sync group on which the sync member is hosted.
let syncMemberName = "syncMemberName_example"; // String | The name of the sync member.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.syncMembersListMemberSchemas(resourceGroupName, serverName, databaseName, syncGroupName, syncMemberName, subscriptionId, apiVersion, (error, data, response) => {
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
 **databaseName** | **String**| The name of the database on which the sync group is hosted. | 
 **syncGroupName** | **String**| The name of the sync group on which the sync member is hosted. | 
 **syncMemberName** | **String**| The name of the sync member. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**SyncFullSchemaPropertiesListResult**](SyncFullSchemaPropertiesListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## syncMembersRefreshMemberSchema

> syncMembersRefreshMemberSchema(resourceGroupName, serverName, databaseName, syncGroupName, syncMemberName, subscriptionId, apiVersion)



Refreshes a sync member database schema.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.SyncMembersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database on which the sync group is hosted.
let syncGroupName = "syncGroupName_example"; // String | The name of the sync group on which the sync member is hosted.
let syncMemberName = "syncMemberName_example"; // String | The name of the sync member.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.syncMembersRefreshMemberSchema(resourceGroupName, serverName, databaseName, syncGroupName, syncMemberName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **databaseName** | **String**| The name of the database on which the sync group is hosted. | 
 **syncGroupName** | **String**| The name of the sync group on which the sync member is hosted. | 
 **syncMemberName** | **String**| The name of the sync member. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## syncMembersUpdate

> SyncMember syncMembersUpdate(resourceGroupName, serverName, databaseName, syncGroupName, syncMemberName, subscriptionId, apiVersion, parameters)



Updates an existing sync member.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.SyncMembersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of the database on which the sync group is hosted.
let syncGroupName = "syncGroupName_example"; // String | The name of the sync group on which the sync member is hosted.
let syncMemberName = "syncMemberName_example"; // String | The name of the sync member.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let parameters = new SqlManagementClient.SyncMember(); // SyncMember | The requested sync member resource state.
apiInstance.syncMembersUpdate(resourceGroupName, serverName, databaseName, syncGroupName, syncMemberName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **databaseName** | **String**| The name of the database on which the sync group is hosted. | 
 **syncGroupName** | **String**| The name of the sync group on which the sync member is hosted. | 
 **syncMemberName** | **String**| The name of the sync member. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **parameters** | [**SyncMember**](SyncMember.md)| The requested sync member resource state. | 

### Return type

[**SyncMember**](SyncMember.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

