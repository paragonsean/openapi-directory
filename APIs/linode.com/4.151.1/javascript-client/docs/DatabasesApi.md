# LinodeApi.DatabasesApi

All URIs are relative to *https://api.linode.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteDatabaseMongoDBInstanceBackup**](DatabasesApi.md#deleteDatabaseMongoDBInstanceBackup) | **DELETE** /databases/mongodb/instances/{instanceId}/backups/{backupId} | Managed MongoDB Database Backup Delete
[**deleteDatabaseMySQLInstanceBackup**](DatabasesApi.md#deleteDatabaseMySQLInstanceBackup) | **DELETE** /databases/mysql/instances/{instanceId}/backups/{backupId} | Managed MySQL Database Backup Delete
[**deleteDatabasePostgreSQLInstanceBackup**](DatabasesApi.md#deleteDatabasePostgreSQLInstanceBackup) | **DELETE** /databases/postgresql/instances/{instanceId}/backups/{backupId} | Managed PostgreSQL Database Backup Delete
[**deleteDatabasesMongoDBInstance**](DatabasesApi.md#deleteDatabasesMongoDBInstance) | **DELETE** /databases/mongodb/instances/{instanceId} | Managed MongoDB Database Delete
[**deleteDatabasesMySQLInstance**](DatabasesApi.md#deleteDatabasesMySQLInstance) | **DELETE** /databases/mysql/instances/{instanceId} | Managed MySQL Database Delete
[**deleteDatabasesPostgreSQLInstance**](DatabasesApi.md#deleteDatabasesPostgreSQLInstance) | **DELETE** /databases/postgresql/instances/{instanceId} | Managed PostgreSQL Database Delete
[**getDatabasesEngine**](DatabasesApi.md#getDatabasesEngine) | **GET** /databases/engines/{engineId} | Managed Database Engine View
[**getDatabasesEngines**](DatabasesApi.md#getDatabasesEngines) | **GET** /databases/engines | Managed Database Engines List
[**getDatabasesInstances**](DatabasesApi.md#getDatabasesInstances) | **GET** /databases/instances | Managed Databases List All
[**getDatabasesMongoDBInstance**](DatabasesApi.md#getDatabasesMongoDBInstance) | **GET** /databases/mongodb/instances/{instanceId} | Managed MongoDB Database View
[**getDatabasesMongoDBInstanceBackup**](DatabasesApi.md#getDatabasesMongoDBInstanceBackup) | **GET** /databases/mongodb/instances/{instanceId}/backups/{backupId} | Managed MongoDB Database Backup View
[**getDatabasesMongoDBInstanceBackups**](DatabasesApi.md#getDatabasesMongoDBInstanceBackups) | **GET** /databases/mongodb/instances/{instanceId}/backups | Managed MongoDB Database Backups List
[**getDatabasesMongoDBInstanceCredentials**](DatabasesApi.md#getDatabasesMongoDBInstanceCredentials) | **GET** /databases/mongodb/instances/{instanceId}/credentials | Managed MongoDB Database Credentials View
[**getDatabasesMongoDBInstanceSSL**](DatabasesApi.md#getDatabasesMongoDBInstanceSSL) | **GET** /databases/mongodb/instances/{instanceId}/ssl | Managed MongoDB Database SSL Certificate View
[**getDatabasesMongoDBInstances**](DatabasesApi.md#getDatabasesMongoDBInstances) | **GET** /databases/mongodb/instances | Managed MongoDB Databases List
[**getDatabasesMySQLInstance**](DatabasesApi.md#getDatabasesMySQLInstance) | **GET** /databases/mysql/instances/{instanceId} | Managed MySQL Database View
[**getDatabasesMySQLInstanceBackup**](DatabasesApi.md#getDatabasesMySQLInstanceBackup) | **GET** /databases/mysql/instances/{instanceId}/backups/{backupId} | Managed MySQL Database Backup View
[**getDatabasesMySQLInstanceBackups**](DatabasesApi.md#getDatabasesMySQLInstanceBackups) | **GET** /databases/mysql/instances/{instanceId}/backups | Managed MySQL Database Backups List
[**getDatabasesMySQLInstanceCredentials**](DatabasesApi.md#getDatabasesMySQLInstanceCredentials) | **GET** /databases/mysql/instances/{instanceId}/credentials | Managed MySQL Database Credentials View
[**getDatabasesMySQLInstanceSSL**](DatabasesApi.md#getDatabasesMySQLInstanceSSL) | **GET** /databases/mysql/instances/{instanceId}/ssl | Managed MySQL Database SSL Certificate View
[**getDatabasesMySQLInstances**](DatabasesApi.md#getDatabasesMySQLInstances) | **GET** /databases/mysql/instances | Managed MySQL Databases List
[**getDatabasesPostgreSQLInstance**](DatabasesApi.md#getDatabasesPostgreSQLInstance) | **GET** /databases/postgresql/instances/{instanceId} | Managed PostgreSQL Database View
[**getDatabasesPostgreSQLInstanceBackup**](DatabasesApi.md#getDatabasesPostgreSQLInstanceBackup) | **GET** /databases/postgresql/instances/{instanceId}/backups/{backupId} | Managed PostgreSQL Database Backup View
[**getDatabasesPostgreSQLInstanceBackups**](DatabasesApi.md#getDatabasesPostgreSQLInstanceBackups) | **GET** /databases/postgresql/instances/{instanceId}/backups | Managed PostgreSQL Database Backups List
[**getDatabasesPostgreSQLInstanceCredentials**](DatabasesApi.md#getDatabasesPostgreSQLInstanceCredentials) | **GET** /databases/postgresql/instances/{instanceId}/credentials | Managed PostgreSQL Database Credentials View
[**getDatabasesPostgreSQLInstanceSSL**](DatabasesApi.md#getDatabasesPostgreSQLInstanceSSL) | **GET** /databases/postgresql/instances/{instanceId}/ssl | Managed PostgreSQL Database SSL Certificate View
[**getDatabasesPostgreSQLInstances**](DatabasesApi.md#getDatabasesPostgreSQLInstances) | **GET** /databases/postgresql/instances | Managed PostgreSQL Databases List
[**getDatabasesType**](DatabasesApi.md#getDatabasesType) | **GET** /databases/types/{typeId} | Managed Database Type View
[**getDatabasesTypes**](DatabasesApi.md#getDatabasesTypes) | **GET** /databases/types | Managed Database Types List
[**postDatabasesMongoDBInstanceBackup**](DatabasesApi.md#postDatabasesMongoDBInstanceBackup) | **POST** /databases/mongodb/instances/{instanceId}/backups | Managed MongoDB Database Backup Snapshot Create
[**postDatabasesMongoDBInstanceBackupRestore**](DatabasesApi.md#postDatabasesMongoDBInstanceBackupRestore) | **POST** /databases/mongodb/instances/{instanceId}/backups/{backupId}/restore | Managed MongoDB Database Backup Restore
[**postDatabasesMongoDBInstanceCredentialsReset**](DatabasesApi.md#postDatabasesMongoDBInstanceCredentialsReset) | **POST** /databases/mongodb/instances/{instanceId}/credentials/reset | Managed MongoDB Database Credentials Reset
[**postDatabasesMongoDBInstancePatch**](DatabasesApi.md#postDatabasesMongoDBInstancePatch) | **POST** /databases/mongodb/instances/{instanceId}/patch | Managed MongoDB Database Patch
[**postDatabasesMySQLInstanceBackup**](DatabasesApi.md#postDatabasesMySQLInstanceBackup) | **POST** /databases/mysql/instances/{instanceId}/backups | Managed MySQL Database Backup Snapshot Create
[**postDatabasesMySQLInstanceBackupRestore**](DatabasesApi.md#postDatabasesMySQLInstanceBackupRestore) | **POST** /databases/mysql/instances/{instanceId}/backups/{backupId}/restore | Managed MySQL Database Backup Restore
[**postDatabasesMySQLInstanceCredentialsReset**](DatabasesApi.md#postDatabasesMySQLInstanceCredentialsReset) | **POST** /databases/mysql/instances/{instanceId}/credentials/reset | Managed MySQL Database Credentials Reset
[**postDatabasesMySQLInstancePatch**](DatabasesApi.md#postDatabasesMySQLInstancePatch) | **POST** /databases/mysql/instances/{instanceId}/patch | Managed MySQL Database Patch
[**postDatabasesMySQLInstances**](DatabasesApi.md#postDatabasesMySQLInstances) | **POST** /databases/mysql/instances | Managed MySQL Database Create
[**postDatabasesPostgreSQLInstanceBackup**](DatabasesApi.md#postDatabasesPostgreSQLInstanceBackup) | **POST** /databases/postgresql/instances/{instanceId}/backups | Managed PostgreSQL Database Backup Snapshot Create
[**postDatabasesPostgreSQLInstanceBackupRestore**](DatabasesApi.md#postDatabasesPostgreSQLInstanceBackupRestore) | **POST** /databases/postgresql/instances/{instanceId}/backups/{backupId}/restore | Managed PostgreSQL Database Backup Restore
[**postDatabasesPostgreSQLInstanceCredentialsReset**](DatabasesApi.md#postDatabasesPostgreSQLInstanceCredentialsReset) | **POST** /databases/postgresql/instances/{instanceId}/credentials/reset | Managed PostgreSQL Database Credentials Reset
[**postDatabasesPostgreSQLInstancePatch**](DatabasesApi.md#postDatabasesPostgreSQLInstancePatch) | **POST** /databases/postgresql/instances/{instanceId}/patch | Managed PostgreSQL Database Patch
[**postDatabasesPostgreSQLInstances**](DatabasesApi.md#postDatabasesPostgreSQLInstances) | **POST** /databases/postgresql/instances | Managed PostgreSQL Database Create
[**putDatabasesMongoDBInstance**](DatabasesApi.md#putDatabasesMongoDBInstance) | **PUT** /databases/mongodb/instances/{instanceId} | Managed MongoDB Database Update
[**putDatabasesMySQLInstance**](DatabasesApi.md#putDatabasesMySQLInstance) | **PUT** /databases/mysql/instances/{instanceId} | Managed MySQL Database Update
[**putDatabasesPostgreSQLInstance**](DatabasesApi.md#putDatabasesPostgreSQLInstance) | **PUT** /databases/postgresql/instances/{instanceId} | Managed PostgreSQL Database Update



## deleteDatabaseMongoDBInstanceBackup

> Object deleteDatabaseMongoDBInstanceBackup(instanceId, backupId)

Managed MongoDB Database Backup Delete

Delete a single backup for an accessible Managed MongoDB Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must not be provisioning to perform this command.  **Note**: New MongoDB Databases cannot currently be created. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed MongoDB Database.
let backupId = 56; // Number | The ID of the Managed MongoDB Database backup.
apiInstance.deleteDatabaseMongoDBInstanceBackup(instanceId, backupId, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed MongoDB Database. | 
 **backupId** | **Number**| The ID of the Managed MongoDB Database backup. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteDatabaseMySQLInstanceBackup

> Object deleteDatabaseMySQLInstanceBackup(instanceId, backupId)

Managed MySQL Database Backup Delete

Delete a single backup for an accessible Managed MySQL Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must not be provisioning to perform this command. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed MySQL Database.
let backupId = 56; // Number | The ID of the Managed MySQL Database backup.
apiInstance.deleteDatabaseMySQLInstanceBackup(instanceId, backupId, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed MySQL Database. | 
 **backupId** | **Number**| The ID of the Managed MySQL Database backup. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteDatabasePostgreSQLInstanceBackup

> Object deleteDatabasePostgreSQLInstanceBackup(instanceId, backupId)

Managed PostgreSQL Database Backup Delete

Delete a single backup for an accessible Managed PostgreSQL Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must not be provisioning to perform this command. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed PostgreSQL Database.
let backupId = 56; // Number | The ID of the Managed PostgreSQL Database backup.
apiInstance.deleteDatabasePostgreSQLInstanceBackup(instanceId, backupId, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed PostgreSQL Database. | 
 **backupId** | **Number**| The ID of the Managed PostgreSQL Database backup. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteDatabasesMongoDBInstance

> Object deleteDatabasesMongoDBInstance(instanceId)

Managed MongoDB Database Delete

Remove a Managed MongoDB Database from your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60;, &#x60;failed&#x60;, or &#x60;degraded&#x60; status to perform this command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes.  **Note**: New MongoDB Databases cannot currently be created. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed MongoDB Database.
apiInstance.deleteDatabasesMongoDBInstance(instanceId, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed MongoDB Database. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteDatabasesMySQLInstance

> Object deleteDatabasesMySQLInstance(instanceId)

Managed MySQL Database Delete

Remove a Managed MySQL Database from your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60;, &#x60;failed&#x60;, or &#x60;degraded&#x60; status to perform this command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed MySQL Database.
apiInstance.deleteDatabasesMySQLInstance(instanceId, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed MySQL Database. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteDatabasesPostgreSQLInstance

> Object deleteDatabasesPostgreSQLInstance(instanceId)

Managed PostgreSQL Database Delete

Remove a Managed PostgreSQL Database from your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60;, &#x60;failed&#x60;, or &#x60;degraded&#x60; status to perform this command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed PostgreSQL Database.
apiInstance.deleteDatabasesPostgreSQLInstance(instanceId, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed PostgreSQL Database. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDatabasesEngine

> DatabaseEngine getDatabasesEngine(engineId, opts)

Managed Database Engine View

Display information for a single Managed Database engine type and version. 

### Example

```javascript
import LinodeApi from 'linode_api';

let apiInstance = new LinodeApi.DatabasesApi();
let engineId = "engineId_example"; // String | The ID of the Managed Database engine.
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getDatabasesEngine(engineId, opts, (error, data, response) => {
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
 **engineId** | **String**| The ID of the Managed Database engine. | 
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**DatabaseEngine**](DatabaseEngine.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDatabasesEngines

> GetDatabasesEngines200Response getDatabasesEngines(opts)

Managed Database Engines List

Display all available Managed Database engine types and versions. Engine IDs are used when creating new Managed Databases. 

### Example

```javascript
import LinodeApi from 'linode_api';

let apiInstance = new LinodeApi.DatabasesApi();
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getDatabasesEngines(opts, (error, data, response) => {
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
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetDatabasesEngines200Response**](GetDatabasesEngines200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDatabasesInstances

> GetDatabasesInstances200Response getDatabasesInstances(opts)

Managed Databases List All

Display all Managed Databases that are accessible by your User, regardless of engine type.  For more detailed information on a particular Database instance, make a request to its &#x60;instance_uri&#x60;. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getDatabasesInstances(opts, (error, data, response) => {
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
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetDatabasesInstances200Response**](GetDatabasesInstances200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDatabasesMongoDBInstance

> DatabaseMongoDB getDatabasesMongoDBInstance(instanceId)

Managed MongoDB Database View

Display information for a single, accessible Managed MongoDB Database.  **Note**: New MongoDB Databases cannot currently be created. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed MongoDB Database.
apiInstance.getDatabasesMongoDBInstance(instanceId, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed MongoDB Database. | 

### Return type

[**DatabaseMongoDB**](DatabaseMongoDB.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDatabasesMongoDBInstanceBackup

> DatabaseBackup getDatabasesMongoDBInstanceBackup(instanceId, backupId)

Managed MongoDB Database Backup View

Display information for a single backup for an accessible Managed MongoDB Database.  The Database must not be provisioning to perform this command.  **Note**: New MongoDB Databases cannot currently be created. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed MongoDB Database.
let backupId = 56; // Number | The ID of the Managed MongoDB Database backup.
apiInstance.getDatabasesMongoDBInstanceBackup(instanceId, backupId, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed MongoDB Database. | 
 **backupId** | **Number**| The ID of the Managed MongoDB Database backup. | 

### Return type

[**DatabaseBackup**](DatabaseBackup.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDatabasesMongoDBInstanceBackups

> GetDatabasesMongoDBInstanceBackups200Response getDatabasesMongoDBInstanceBackups(instanceId, opts)

Managed MongoDB Database Backups List

Display all backups for an accessible Managed MongoDB Database.  The Database must not be provisioning to perform this command.  Database &#x60;auto&#x60; type backups are created every 24 hours at 0:00 UTC. Each &#x60;auto&#x60; backup is retained for 7 days.  Database &#x60;snapshot&#x60; type backups are created by accessing the **Managed MongoDB Database Backup Snapshot Create** ([POST /databases/mongodb/instances/{instanceId}/backups](/docs/api/databases/#managed-mongodb-database-backup-snapshot-create)) command.  **Note**: New MongoDB Databases cannot currently be created. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed MongoDB Database.
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getDatabasesMongoDBInstanceBackups(instanceId, opts, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed MongoDB Database. | 
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetDatabasesMongoDBInstanceBackups200Response**](GetDatabasesMongoDBInstanceBackups200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDatabasesMongoDBInstanceCredentials

> DatabaseCredentials getDatabasesMongoDBInstanceCredentials(instanceId)

Managed MongoDB Database Credentials View

Display the root username and password for an accessible Managed MongoDB Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**: New MongoDB Databases cannot currently be created. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed MongoDB Database.
apiInstance.getDatabasesMongoDBInstanceCredentials(instanceId, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed MongoDB Database. | 

### Return type

[**DatabaseCredentials**](DatabaseCredentials.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDatabasesMongoDBInstanceSSL

> DatabaseSSL getDatabasesMongoDBInstanceSSL(instanceId)

Managed MongoDB Database SSL Certificate View

Display the SSL CA certificate for an accessible Managed MongoDB Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**: New MongoDB Databases cannot currently be created. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed MongoDB Database.
apiInstance.getDatabasesMongoDBInstanceSSL(instanceId, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed MongoDB Database. | 

### Return type

[**DatabaseSSL**](DatabaseSSL.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDatabasesMongoDBInstances

> GetDatabasesMongoDBInstances200Response getDatabasesMongoDBInstances(opts)

Managed MongoDB Databases List

Display all accessible Managed MongoDB Databases.  **Note**: New MongoDB Databases cannot currently be created. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getDatabasesMongoDBInstances(opts, (error, data, response) => {
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
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetDatabasesMongoDBInstances200Response**](GetDatabasesMongoDBInstances200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDatabasesMySQLInstance

> DatabaseMySQL getDatabasesMySQLInstance(instanceId)

Managed MySQL Database View

Display information for a single, accessible Managed MySQL Database. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed MySQL Database.
apiInstance.getDatabasesMySQLInstance(instanceId, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed MySQL Database. | 

### Return type

[**DatabaseMySQL**](DatabaseMySQL.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDatabasesMySQLInstanceBackup

> DatabaseBackup getDatabasesMySQLInstanceBackup(instanceId, backupId)

Managed MySQL Database Backup View

Display information for a single backup for an accessible Managed MySQL Database.  The Database must not be provisioning to perform this command. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed MySQL Database.
let backupId = 56; // Number | The ID of the Managed MySQL Database backup.
apiInstance.getDatabasesMySQLInstanceBackup(instanceId, backupId, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed MySQL Database. | 
 **backupId** | **Number**| The ID of the Managed MySQL Database backup. | 

### Return type

[**DatabaseBackup**](DatabaseBackup.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDatabasesMySQLInstanceBackups

> GetDatabasesMongoDBInstanceBackups200Response getDatabasesMySQLInstanceBackups(instanceId, opts)

Managed MySQL Database Backups List

Display all backups for an accessible Managed MySQL Database.  The Database must not be provisioning to perform this command.  Database &#x60;auto&#x60; type backups are created every 24 hours at 0:00 UTC. Each &#x60;auto&#x60; backup is retained for 7 days.  Database &#x60;snapshot&#x60; type backups are created by accessing the **Managed MySQL Database Backup Snapshot Create** ([POST /databases/mysql/instances/{instanceId}/backups](/docs/api/databases/#managed-mysql-database-backup-snapshot-create)) command. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed MySQL Database.
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getDatabasesMySQLInstanceBackups(instanceId, opts, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed MySQL Database. | 
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetDatabasesMongoDBInstanceBackups200Response**](GetDatabasesMongoDBInstanceBackups200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDatabasesMySQLInstanceCredentials

> DatabaseCredentials getDatabasesMySQLInstanceCredentials(instanceId)

Managed MySQL Database Credentials View

Display the root username and password for an accessible Managed MySQL Database.  The Database must have an &#x60;active&#x60; status to perform this command. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed MySQL Database.
apiInstance.getDatabasesMySQLInstanceCredentials(instanceId, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed MySQL Database. | 

### Return type

[**DatabaseCredentials**](DatabaseCredentials.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDatabasesMySQLInstanceSSL

> DatabaseSSL getDatabasesMySQLInstanceSSL(instanceId)

Managed MySQL Database SSL Certificate View

Display the SSL CA certificate for an accessible Managed MySQL Database.  The Database must have an &#x60;active&#x60; status to perform this command. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed MySQL Database.
apiInstance.getDatabasesMySQLInstanceSSL(instanceId, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed MySQL Database. | 

### Return type

[**DatabaseSSL**](DatabaseSSL.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDatabasesMySQLInstances

> GetDatabasesMySQLInstances200Response getDatabasesMySQLInstances(opts)

Managed MySQL Databases List

Display all accessible Managed MySQL Databases. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getDatabasesMySQLInstances(opts, (error, data, response) => {
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
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetDatabasesMySQLInstances200Response**](GetDatabasesMySQLInstances200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDatabasesPostgreSQLInstance

> DatabasePostgreSQL getDatabasesPostgreSQLInstance(instanceId)

Managed PostgreSQL Database View

Display information for a single, accessible Managed PostgreSQL Database. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed PostgreSQL Database.
apiInstance.getDatabasesPostgreSQLInstance(instanceId, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed PostgreSQL Database. | 

### Return type

[**DatabasePostgreSQL**](DatabasePostgreSQL.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDatabasesPostgreSQLInstanceBackup

> DatabaseBackup getDatabasesPostgreSQLInstanceBackup(instanceId, backupId)

Managed PostgreSQL Database Backup View

Display information for a single backup for an accessible Managed PostgreSQL Database.  The Database must not be provisioning to perform this command. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed PostgreSQL Database.
let backupId = 56; // Number | The ID of the Managed PostgreSQL Database backup.
apiInstance.getDatabasesPostgreSQLInstanceBackup(instanceId, backupId, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed PostgreSQL Database. | 
 **backupId** | **Number**| The ID of the Managed PostgreSQL Database backup. | 

### Return type

[**DatabaseBackup**](DatabaseBackup.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDatabasesPostgreSQLInstanceBackups

> GetDatabasesMongoDBInstanceBackups200Response getDatabasesPostgreSQLInstanceBackups(instanceId, opts)

Managed PostgreSQL Database Backups List

Display all backups for an accessible Managed PostgreSQL Database.  The Database must not be provisioning to perform this command.  Database &#x60;auto&#x60; type backups are created every 24 hours at 0:00 UTC. Each &#x60;auto&#x60; backup is retained for 7 days.  Database &#x60;snapshot&#x60; type backups are created by accessing the **Managed PostgreSQL Database Backup Snapshot Create** ([POST /databases/postgresql/instances/{instanceId}/backups](/docs/api/databases/#managed-postgresql-database-backup-snapshot-create)) command. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed PostgreSQL Database.
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getDatabasesPostgreSQLInstanceBackups(instanceId, opts, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed PostgreSQL Database. | 
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetDatabasesMongoDBInstanceBackups200Response**](GetDatabasesMongoDBInstanceBackups200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDatabasesPostgreSQLInstanceCredentials

> DatabaseCredentials getDatabasesPostgreSQLInstanceCredentials(instanceId)

Managed PostgreSQL Database Credentials View

Display the root username and password for an accessible Managed PostgreSQL Database.  The Database must have an &#x60;active&#x60; status to perform this command. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed PostgreSQL Database.
apiInstance.getDatabasesPostgreSQLInstanceCredentials(instanceId, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed PostgreSQL Database. | 

### Return type

[**DatabaseCredentials**](DatabaseCredentials.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDatabasesPostgreSQLInstanceSSL

> DatabaseSSL getDatabasesPostgreSQLInstanceSSL(instanceId)

Managed PostgreSQL Database SSL Certificate View

Display the SSL CA certificate for an accessible Managed PostgreSQL Database.  The Database must have an &#x60;active&#x60; status to perform this command. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed PostgreSQL Database.
apiInstance.getDatabasesPostgreSQLInstanceSSL(instanceId, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed PostgreSQL Database. | 

### Return type

[**DatabaseSSL**](DatabaseSSL.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDatabasesPostgreSQLInstances

> GetDatabasesPostgreSQLInstances200Response getDatabasesPostgreSQLInstances(opts)

Managed PostgreSQL Databases List

Display all accessible Managed PostgreSQL Databases. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getDatabasesPostgreSQLInstances(opts, (error, data, response) => {
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
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetDatabasesPostgreSQLInstances200Response**](GetDatabasesPostgreSQLInstances200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDatabasesType

> DatabaseType getDatabasesType(typeId, opts)

Managed Database Type View

Display the details of a single Managed Database type. The type and number of nodes determine the resources and price of a Managed Database instance. 

### Example

```javascript
import LinodeApi from 'linode_api';

let apiInstance = new LinodeApi.DatabasesApi();
let typeId = "typeId_example"; // String | The ID of the Managed Database type.
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getDatabasesType(typeId, opts, (error, data, response) => {
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
 **typeId** | **String**| The ID of the Managed Database type. | 
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**DatabaseType**](DatabaseType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDatabasesTypes

> GetDatabasesTypes200Response getDatabasesTypes(opts)

Managed Database Types List

Display all Managed Database node types. The type and number of nodes determine the resources and price of a Managed Database instance.  Each Managed Database can have one node type. In the case of a high availabilty Database, all nodes are provisioned according to the chosen type. 

### Example

```javascript
import LinodeApi from 'linode_api';

let apiInstance = new LinodeApi.DatabasesApi();
let opts = {
  'page': 1, // Number | The page of a collection to return.
  'pageSize': 100 // Number | The number of items to return per page.
};
apiInstance.getDatabasesTypes(opts, (error, data, response) => {
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
 **page** | **Number**| The page of a collection to return. | [optional] [default to 1]
 **pageSize** | **Number**| The number of items to return per page. | [optional] [default to 100]

### Return type

[**GetDatabasesTypes200Response**](GetDatabasesTypes200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postDatabasesMongoDBInstanceBackup

> Object postDatabasesMongoDBInstanceBackup(instanceId, opts)

Managed MongoDB Database Backup Snapshot Create

Creates a snapshot backup of a Managed MongoDB Database.  Requires &#x60;read_write&#x60; access to the Database.  Up to 3 snapshot backups for each Database can be stored at a time. If 3 snapshots have been created for a Database, one must be deleted before another can be made.  Backups generated by this command have the type &#x60;snapshot&#x60;. Snapshot backups may take several minutes to complete, after which they will be accessible to view or restore.  The Database must have an &#x60;active&#x60; status to perform this command. If another backup is in progress, it must complete before a new backup can be initiated.  **Note**: New MongoDB Databases cannot currently be created. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed MongoDB Database.
let opts = {
  'databaseBackupSnapshot': new LinodeApi.DatabaseBackupSnapshot() // DatabaseBackupSnapshot | Information about the snapshot backup to create.
};
apiInstance.postDatabasesMongoDBInstanceBackup(instanceId, opts, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed MongoDB Database. | 
 **databaseBackupSnapshot** | [**DatabaseBackupSnapshot**](DatabaseBackupSnapshot.md)| Information about the snapshot backup to create. | [optional] 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postDatabasesMongoDBInstanceBackupRestore

> Object postDatabasesMongoDBInstanceBackupRestore(instanceId, backupId)

Managed MongoDB Database Backup Restore

Restore a backup to a Managed MongoDB Database on your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**: Restoring from a backup will erase all existing data on the database instance and replace it with backup data.  **Note**: Currently, restoring a backup after resetting Managed Database credentials results in a failed cluster. Please contact Customer Support if this occurs.  **Note**: New MongoDB Databases cannot currently be created. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed MongoDB Database.
let backupId = 56; // Number | The ID of the Managed MongoDB Database backup.
apiInstance.postDatabasesMongoDBInstanceBackupRestore(instanceId, backupId, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed MongoDB Database. | 
 **backupId** | **Number**| The ID of the Managed MongoDB Database backup. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postDatabasesMongoDBInstanceCredentialsReset

> Object postDatabasesMongoDBInstanceCredentialsReset(instanceId)

Managed MongoDB Database Credentials Reset

Reset the root password for a Managed MongoDB Database.  Requires &#x60;read_write&#x60; access to the Database.  A new root password is randomly generated and accessible with the **Managed MongoDB Database Credentials View** ([GET /databases/mongodb/instances/{instanceId}/credentials](/docs/api/databases/#managed-mongodb-database-credentials-view)) command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes.  **Note**: Note that it may take several seconds for credentials to reset.  **Note**: New MongoDB Databases cannot currently be created. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed MongoDB Database.
apiInstance.postDatabasesMongoDBInstanceCredentialsReset(instanceId, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed MongoDB Database. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postDatabasesMongoDBInstancePatch

> Object postDatabasesMongoDBInstancePatch(instanceId)

Managed MongoDB Database Patch

Apply security patches and updates to the underlying operating system of the Managed MongoDB Database. This function runs during regular maintenance windows, which are configurable with the **Managed MongoDB Database Update** ([PUT /databases/mongodb/instances/{instanceId}](/docs/api/databases/#managed-mongodb-database-update)) command. Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**:  * If your database cluster is configured with a single node, you will experience downtime during this maintenance. Consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one.  **Note**: New MongoDB Databases cannot currently be created. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed MongoDB Database.
apiInstance.postDatabasesMongoDBInstancePatch(instanceId, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed MongoDB Database. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postDatabasesMySQLInstanceBackup

> Object postDatabasesMySQLInstanceBackup(instanceId, opts)

Managed MySQL Database Backup Snapshot Create

Creates a snapshot backup of a Managed MySQL Database.  Requires &#x60;read_write&#x60; access to the Database.  Up to 3 snapshot backups for each Database can be stored at a time. If 3 snapshots have been created for a Database, one must be deleted before another can be made.  Backups generated by this command have the type &#x60;snapshot&#x60;. Snapshot backups may take several minutes to complete, after which they will be accessible to view or restore.  The Database must have an &#x60;active&#x60; status to perform this command. If another backup is in progress, it must complete before a new backup can be initiated. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed MySQL Database.
let opts = {
  'databaseBackupSnapshot': new LinodeApi.DatabaseBackupSnapshot() // DatabaseBackupSnapshot | Information about the snapshot backup to create.
};
apiInstance.postDatabasesMySQLInstanceBackup(instanceId, opts, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed MySQL Database. | 
 **databaseBackupSnapshot** | [**DatabaseBackupSnapshot**](DatabaseBackupSnapshot.md)| Information about the snapshot backup to create. | [optional] 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postDatabasesMySQLInstanceBackupRestore

> Object postDatabasesMySQLInstanceBackupRestore(instanceId, backupId)

Managed MySQL Database Backup Restore

Restore a backup to a Managed MySQL Database on your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**: Restoring from a backup will erase all existing data on the database instance and replace it with backup data.  **Note**: Currently, restoring a backup after resetting Managed Database credentials results in a failed cluster. Please contact Customer Support if this occurs. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed MySQL Database.
let backupId = 56; // Number | The ID of the Managed MySQL Database backup.
apiInstance.postDatabasesMySQLInstanceBackupRestore(instanceId, backupId, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed MySQL Database. | 
 **backupId** | **Number**| The ID of the Managed MySQL Database backup. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postDatabasesMySQLInstanceCredentialsReset

> Object postDatabasesMySQLInstanceCredentialsReset(instanceId)

Managed MySQL Database Credentials Reset

Reset the root password for a Managed MySQL Database.  Requires &#x60;read_write&#x60; access to the Database.  A new root password is randomly generated and accessible with the **Managed MySQL Database Credentials View** ([GET /databases/mysql/instances/{instanceId}/credentials](/docs/api/databases/#managed-mysql-database-credentials-view)) command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes.  **Note**: Note that it may take several seconds for credentials to reset. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed MySQL Database.
apiInstance.postDatabasesMySQLInstanceCredentialsReset(instanceId, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed MySQL Database. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postDatabasesMySQLInstancePatch

> Object postDatabasesMySQLInstancePatch(instanceId)

Managed MySQL Database Patch

Apply security patches and updates to the underlying operating system of the Managed MySQL Database. This function runs during regular maintenance windows, which are configurable with the **Managed MySQL Database Update** ([PUT /databases/mysql/instances/{instanceId}](/docs/api/databases/#managed-mysql-database-update)) command.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**  * If your database cluster is configured with a single node, you will experience downtime during this maintenance. Consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then [migrate your databases](/docs/products/databases/managed-databases/guides/migrate-mysql/) from the original Managed Database cluster to the new one. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed MySQL Database.
apiInstance.postDatabasesMySQLInstancePatch(instanceId, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed MySQL Database. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postDatabasesMySQLInstances

> DatabaseMySQL postDatabasesMySQLInstances(databaseMySQLRequest)

Managed MySQL Database Create

Provision a Managed MySQL Database.  Restricted Users must have the &#x60;add_databases&#x60; grant to use this command.  New instances can take approximately 15 to 30 minutes to provision.  The &#x60;allow_list&#x60; is used to control access to the Managed Database.  * IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.  * If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (&#x60;[]&#x60;) blocks all connections (both public and private) to the Managed Database.  All Managed Databases include automatic, daily backups. Up to seven backups are automatically stored for each Managed Database, providing restore points for each day of the past week.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed MySQL Database during configurable maintenance windows.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It&#39;s recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then [migrate your databases](/docs/products/databases/managed-databases/guides/migrate-mysql/) from the original Managed Database cluster to the new one.  * To modify update the maintenance window for a Database, use the **Managed MySQL Database Update** ([PUT /databases/mysql/instances/{instanceId}](/docs/api/databases/#managed-mysql-database-update)) command. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let databaseMySQLRequest = new LinodeApi.DatabaseMySQLRequest(); // DatabaseMySQLRequest | Information about the Managed MySQL Database you are creating.
apiInstance.postDatabasesMySQLInstances(databaseMySQLRequest, (error, data, response) => {
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
 **databaseMySQLRequest** | [**DatabaseMySQLRequest**](DatabaseMySQLRequest.md)| Information about the Managed MySQL Database you are creating. | 

### Return type

[**DatabaseMySQL**](DatabaseMySQL.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postDatabasesPostgreSQLInstanceBackup

> Object postDatabasesPostgreSQLInstanceBackup(instanceId, opts)

Managed PostgreSQL Database Backup Snapshot Create

Creates a snapshot backup of a Managed PostgreSQL Database.  Requires &#x60;read_write&#x60; access to the Database.  Up to 3 snapshot backups for each Database can be stored at a time. If 3 snapshots have been created for a Database, one must be deleted before another can be made.  Backups generated by this command have the type &#x60;snapshot&#x60;. Snapshot backups may take several minutes to complete, after which they will be accessible to view or restore.  The Database must have an &#x60;active&#x60; status to perform this command. If another backup is in progress, it must complete before a new backup can be initiated. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed PostgreSQL Database.
let opts = {
  'databaseBackupSnapshot': new LinodeApi.DatabaseBackupSnapshot() // DatabaseBackupSnapshot | Information about the snapshot backup to create.
};
apiInstance.postDatabasesPostgreSQLInstanceBackup(instanceId, opts, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed PostgreSQL Database. | 
 **databaseBackupSnapshot** | [**DatabaseBackupSnapshot**](DatabaseBackupSnapshot.md)| Information about the snapshot backup to create. | [optional] 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postDatabasesPostgreSQLInstanceBackupRestore

> Object postDatabasesPostgreSQLInstanceBackupRestore(instanceId, backupId)

Managed PostgreSQL Database Backup Restore

Restore a backup to a Managed PostgreSQL Database on your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**: Restoring from a backup will erase all existing data on the database instance and replace it with backup data.  **Note**: Currently, restoring a backup after resetting Managed Database credentials results in a failed cluster. Please contact Customer Support if this occurs. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed PostgreSQL Database.
let backupId = 56; // Number | The ID of the Managed PostgreSQL Database backup.
apiInstance.postDatabasesPostgreSQLInstanceBackupRestore(instanceId, backupId, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed PostgreSQL Database. | 
 **backupId** | **Number**| The ID of the Managed PostgreSQL Database backup. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postDatabasesPostgreSQLInstanceCredentialsReset

> Object postDatabasesPostgreSQLInstanceCredentialsReset(instanceId)

Managed PostgreSQL Database Credentials Reset

Reset the root password for a Managed PostgreSQL Database.  Requires &#x60;read_write&#x60; access to the Database.  A new root password is randomly generated and accessible with the **Managed PostgreSQL Database Credentials View** ([GET /databases/postgresql/instances/{instanceId}/credentials](/docs/api/databases/#managed-postgresql-database-credentials-view)) command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes.  **Note**: Note that it may take several seconds for credentials to reset. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed PostgreSQL Database.
apiInstance.postDatabasesPostgreSQLInstanceCredentialsReset(instanceId, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed PostgreSQL Database. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postDatabasesPostgreSQLInstancePatch

> Object postDatabasesPostgreSQLInstancePatch(instanceId)

Managed PostgreSQL Database Patch

Apply security patches and updates to the underlying operating system of the Managed PostgreSQL Database. This function runs during regular maintenance windows, which are configurable with the **Managed PostgreSQL Database Update** ([PUT /databases/postgresql/instances/{instanceId}](/docs/api/databases/#managed-postgresql-database-update)) command.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**  * If your database cluster is configured with a single node, you will experience downtime during this maintenance. Consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed PostgreSQL Database.
apiInstance.postDatabasesPostgreSQLInstancePatch(instanceId, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed PostgreSQL Database. | 

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postDatabasesPostgreSQLInstances

> DatabasePostgreSQL postDatabasesPostgreSQLInstances(databasePostgreSQLRequest)

Managed PostgreSQL Database Create

Provision a Managed PostgreSQL Database.  Restricted Users must have the &#x60;add_databases&#x60; grant to use this command.  New instances can take approximately 15 to 30 minutes to provision.  The &#x60;allow_list&#x60; is used to control access to the Managed Database.  * IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.  * If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (&#x60;[]&#x60;) blocks all connections (both public and private) to the Managed Database.  All Managed Databases include automatic, daily backups. Up to seven backups are automatically stored for each Managed Database, providing restore points for each day of the past week.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed PostgreSQL Database during configurable maintenance windows.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It&#39;s recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one.  * To modify update the maintenance window for a Database, use the **Managed PostgreSQL Database Update** ([PUT /databases/postgresql/instances/{instanceId}](/docs/api/databases/#managed-postgresql-database-update)) command. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let databasePostgreSQLRequest = new LinodeApi.DatabasePostgreSQLRequest(); // DatabasePostgreSQLRequest | Information about the Managed PostgreSQL Database you are creating.
apiInstance.postDatabasesPostgreSQLInstances(databasePostgreSQLRequest, (error, data, response) => {
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
 **databasePostgreSQLRequest** | [**DatabasePostgreSQLRequest**](DatabasePostgreSQLRequest.md)| Information about the Managed PostgreSQL Database you are creating. | 

### Return type

[**DatabasePostgreSQL**](DatabasePostgreSQL.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putDatabasesMongoDBInstance

> DatabaseMongoDB putDatabasesMongoDBInstance(instanceId, putDatabasesMongoDBInstanceRequest)

Managed MongoDB Database Update

Update a Managed MongoDB Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  Updating addresses in the &#x60;allow_list&#x60; overwrites any existing addresses.  * IP addresses and ranges on this list can access the Managed Database. All other sources are blocked.  * If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (&#x60;[]&#x60;) blocks all connections (both public and private) to the Managed Database.  * **Note**: Updates to the &#x60;allow_list&#x60; may take a short period of time to complete, making this command inappropriate for rapid successive updates to this property.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed MongoDB Database. The maintenance window for these updates is configured with the Managed Database&#39;s &#x60;updates&#x60; property.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It&#39;s recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one.  **Note**: New MongoDB Databases cannot currently be created. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed MongoDB Database.
let putDatabasesMongoDBInstanceRequest = new LinodeApi.PutDatabasesMongoDBInstanceRequest(); // PutDatabasesMongoDBInstanceRequest | Updated information for the Managed MongoDB Database.
apiInstance.putDatabasesMongoDBInstance(instanceId, putDatabasesMongoDBInstanceRequest, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed MongoDB Database. | 
 **putDatabasesMongoDBInstanceRequest** | [**PutDatabasesMongoDBInstanceRequest**](PutDatabasesMongoDBInstanceRequest.md)| Updated information for the Managed MongoDB Database. | 

### Return type

[**DatabaseMongoDB**](DatabaseMongoDB.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putDatabasesMySQLInstance

> DatabaseMySQL putDatabasesMySQLInstance(instanceId, putDatabasesMySQLInstanceRequest)

Managed MySQL Database Update

Update a Managed MySQL Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  Updating addresses in the &#x60;allow_list&#x60; overwrites any existing addresses.  * IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.  * If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (&#x60;[]&#x60;) blocks all connections (both public and private) to the Managed Database.  * **Note**: Updates to the &#x60;allow_list&#x60; may take a short period of time to complete, making this command inappropriate for rapid successive updates to this property.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed MySQL Database. The maintenance window for these updates is configured with the Managed Database&#39;s &#x60;updates&#x60; property.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It&#39;s recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then [migrate your databases](/docs/products/databases/managed-databases/guides/migrate-mysql/) from the original Managed Database cluster to the new one. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed MySQL Database.
let putDatabasesMySQLInstanceRequest = new LinodeApi.PutDatabasesMySQLInstanceRequest(); // PutDatabasesMySQLInstanceRequest | Updated information for the Managed MySQL Database.
apiInstance.putDatabasesMySQLInstance(instanceId, putDatabasesMySQLInstanceRequest, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed MySQL Database. | 
 **putDatabasesMySQLInstanceRequest** | [**PutDatabasesMySQLInstanceRequest**](PutDatabasesMySQLInstanceRequest.md)| Updated information for the Managed MySQL Database. | 

### Return type

[**DatabaseMySQL**](DatabaseMySQL.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putDatabasesPostgreSQLInstance

> DatabasePostgreSQL putDatabasesPostgreSQLInstance(instanceId, putDatabasesPostgreSQLInstanceRequest)

Managed PostgreSQL Database Update

Update a Managed PostgreSQL Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  Updating addresses in the &#x60;allow_list&#x60; overwrites any existing addresses.  * IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.  * If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (&#x60;[]&#x60;) blocks all connections (both public and private) to the Managed Database.  * **Note**: Updates to the &#x60;allow_list&#x60; may take a short period of time to complete, making this command inappropriate for rapid successive updates to this property.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed PostgreSQL Database. The maintenance window for these updates is configured with the Managed Database&#39;s &#x60;updates&#x60; property.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It&#39;s recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one. 

### Example

```javascript
import LinodeApi from 'linode_api';
let defaultClient = LinodeApi.ApiClient.instance;
// Configure Bearer access token for authorization: personalAccessToken
let personalAccessToken = defaultClient.authentications['personalAccessToken'];
personalAccessToken.accessToken = "YOUR ACCESS TOKEN"
// Configure OAuth2 access token for authorization: oauth
let oauth = defaultClient.authentications['oauth'];
oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LinodeApi.DatabasesApi();
let instanceId = 56; // Number | The ID of the Managed PostgreSQL Database.
let putDatabasesPostgreSQLInstanceRequest = new LinodeApi.PutDatabasesPostgreSQLInstanceRequest(); // PutDatabasesPostgreSQLInstanceRequest | Updated information for the Managed PostgreSQL Database.
apiInstance.putDatabasesPostgreSQLInstance(instanceId, putDatabasesPostgreSQLInstanceRequest, (error, data, response) => {
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
 **instanceId** | **Number**| The ID of the Managed PostgreSQL Database. | 
 **putDatabasesPostgreSQLInstanceRequest** | [**PutDatabasesPostgreSQLInstanceRequest**](PutDatabasesPostgreSQLInstanceRequest.md)| Updated information for the Managed PostgreSQL Database. | 

### Return type

[**DatabasePostgreSQL**](DatabasePostgreSQL.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

