# PublicApi.MySqlDatabasesApi

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**changeDatabaseUserPassword**](MySqlDatabasesApi.md#changeDatabaseUserPassword) | **PUT** /mysqldatabases/{databaseName}/users/{userName}/password | Change password for mysql user
[**changeDatabaseUserStatus**](MySqlDatabasesApi.md#changeDatabaseUserStatus) | **PUT** /mysqldatabases/{databaseName}/users/{userName}/status | Enable/disable mysql user
[**createMySqlDatabase**](MySqlDatabasesApi.md#createMySqlDatabase) | **POST** /mysqldatabases | Create a new mysql database
[**createMySqlUser**](MySqlDatabasesApi.md#createMySqlUser) | **POST** /mysqldatabases/{databaseName}/users | Create a new mysql user
[**deleteDatabase**](MySqlDatabasesApi.md#deleteDatabase) | **DELETE** /mysqldatabases/{databaseName} | Delete a mysql database
[**deleteDatabaseUser**](MySqlDatabasesApi.md#deleteDatabaseUser) | **DELETE** /mysqldatabases/{databaseName}/users/{userName} | Delete a mysql user
[**getDatabaseUsers**](MySqlDatabasesApi.md#getDatabaseUsers) | **GET** /mysqldatabases/{databaseName}/users | Overview of mysql users
[**getMySqlDatabase**](MySqlDatabasesApi.md#getMySqlDatabase) | **GET** /mysqldatabases/{databaseName} | Get a specific database
[**getMySqlDatabases**](MySqlDatabasesApi.md#getMySqlDatabases) | **GET** /mysqldatabases | Overview of mysql databases



## changeDatabaseUserPassword

> changeDatabaseUserPassword(databaseName, userName, databaseName2, userName2, opts)

Change password for mysql user

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.MySqlDatabasesApi();
let databaseName = "databaseName_example"; // String | Name of the database.
let userName = "userName_example"; // String | Name of the user.
let databaseName2 = "databaseName_example"; // String | Automatically added
let userName2 = "userName_example"; // String | Automatically added
let opts = {
  'updateUserPasswordRequest': new PublicApi.UpdateUserPasswordRequest() // UpdateUserPasswordRequest | Contains the new password.
};
apiInstance.changeDatabaseUserPassword(databaseName, userName, databaseName2, userName2, opts, (error, data, response) => {
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
 **databaseName** | **String**| Name of the database. | 
 **userName** | **String**| Name of the user. | 
 **databaseName2** | **String**| Automatically added | 
 **userName2** | **String**| Automatically added | 
 **updateUserPasswordRequest** | [**UpdateUserPasswordRequest**](UpdateUserPasswordRequest.md)| Contains the new password. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## changeDatabaseUserStatus

> changeDatabaseUserStatus(databaseName, userName, databaseName2, userName2, opts)

Enable/disable mysql user

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.MySqlDatabasesApi();
let databaseName = "databaseName_example"; // String | Name of the database.
let userName = "userName_example"; // String | Name of the user.
let databaseName2 = "databaseName_example"; // String | Automatically added
let userName2 = "userName_example"; // String | Automatically added
let opts = {
  'updateUserStatusRequest': new PublicApi.UpdateUserStatusRequest() // UpdateUserStatusRequest | Whether the user is enabled or not.
};
apiInstance.changeDatabaseUserStatus(databaseName, userName, databaseName2, userName2, opts, (error, data, response) => {
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
 **databaseName** | **String**| Name of the database. | 
 **userName** | **String**| Name of the user. | 
 **databaseName2** | **String**| Automatically added | 
 **userName2** | **String**| Automatically added | 
 **updateUserStatusRequest** | [**UpdateUserStatusRequest**](UpdateUserStatusRequest.md)| Whether the user is enabled or not. | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## createMySqlDatabase

> createMySqlDatabase(opts)

Create a new mysql database

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.MySqlDatabasesApi();
let opts = {
  'createMySqlDatabase': new PublicApi.CreateMySqlDatabase() // CreateMySqlDatabase | 
};
apiInstance.createMySqlDatabase(opts, (error, data, response) => {
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
 **createMySqlDatabase** | [**CreateMySqlDatabase**](CreateMySqlDatabase.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createMySqlUser

> createMySqlUser(databaseName, databaseName2, opts)

Create a new mysql user

The creation of a new mysql user will result in a user with read_only rights.

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.MySqlDatabasesApi();
let databaseName = "databaseName_example"; // String | Name of the database.
let databaseName2 = "databaseName_example"; // String | Automatically added
let opts = {
  'createMySqlUser': new PublicApi.CreateMySqlUser() // CreateMySqlUser | 
};
apiInstance.createMySqlUser(databaseName, databaseName2, opts, (error, data, response) => {
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
 **databaseName** | **String**| Name of the database. | 
 **databaseName2** | **String**| Automatically added | 
 **createMySqlUser** | [**CreateMySqlUser**](CreateMySqlUser.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteDatabase

> deleteDatabase(databaseName, databaseName2)

Delete a mysql database

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.MySqlDatabasesApi();
let databaseName = "databaseName_example"; // String | Name of the database.
let databaseName2 = "databaseName_example"; // String | Automatically added
apiInstance.deleteDatabase(databaseName, databaseName2, (error, data, response) => {
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
 **databaseName** | **String**| Name of the database. | 
 **databaseName2** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteDatabaseUser

> deleteDatabaseUser(databaseName, userName, databaseName2, userName2)

Delete a mysql user

The deletion of a mysql user is allowed for users with read_only rights.

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.MySqlDatabasesApi();
let databaseName = "databaseName_example"; // String | Name of the database.
let userName = "userName_example"; // String | Name of the user.
let databaseName2 = "databaseName_example"; // String | Automatically added
let userName2 = "userName_example"; // String | Automatically added
apiInstance.deleteDatabaseUser(databaseName, userName, databaseName2, userName2, (error, data, response) => {
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
 **databaseName** | **String**| Name of the database. | 
 **userName** | **String**| Name of the user. | 
 **databaseName2** | **String**| Automatically added | 
 **userName2** | **String**| Automatically added | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getDatabaseUsers

> [MySqlUser] getDatabaseUsers(databaseName, databaseName2)

Overview of mysql users

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.MySqlDatabasesApi();
let databaseName = "databaseName_example"; // String | Name of the database.
let databaseName2 = "databaseName_example"; // String | Automatically added
apiInstance.getDatabaseUsers(databaseName, databaseName2, (error, data, response) => {
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
 **databaseName** | **String**| Name of the database. | 
 **databaseName2** | **String**| Automatically added | 

### Return type

[**[MySqlUser]**](MySqlUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMySqlDatabase

> MySqlDatabase getMySqlDatabase(databaseName, databaseName2)

Get a specific database

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.MySqlDatabasesApi();
let databaseName = "databaseName_example"; // String | 
let databaseName2 = "databaseName_example"; // String | Automatically added
apiInstance.getMySqlDatabase(databaseName, databaseName2, (error, data, response) => {
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
 **databaseName** | **String**|  | 
 **databaseName2** | **String**| Automatically added | 

### Return type

[**MySqlDatabase**](MySqlDatabase.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMySqlDatabases

> [MySqlDatabase] getMySqlDatabases(opts)

Overview of mysql databases

### Example

```javascript
import PublicApi from 'public_api';

let apiInstance = new PublicApi.MySqlDatabasesApi();
let opts = {
  'skip': 56, // Number | The number of items to skip in the resultset.
  'take': 56 // Number | The number of items to return in the resultset. The returned count can be equal or less than this number.
};
apiInstance.getMySqlDatabases(opts, (error, data, response) => {
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
 **skip** | **Number**| The number of items to skip in the resultset. | [optional] 
 **take** | **Number**| The number of items to return in the resultset. The returned count can be equal or less than this number. | [optional] 

### Return type

[**[MySqlDatabase]**](MySqlDatabase.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

