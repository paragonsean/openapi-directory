# DatabasesApi

All URIs are relative to *https://api.linode.com/v4*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteDatabaseMongoDBInstanceBackup**](DatabasesApi.md#deleteDatabaseMongoDBInstanceBackup) | **DELETE** /databases/mongodb/instances/{instanceId}/backups/{backupId} | Managed MongoDB Database Backup Delete |
| [**deleteDatabaseMySQLInstanceBackup**](DatabasesApi.md#deleteDatabaseMySQLInstanceBackup) | **DELETE** /databases/mysql/instances/{instanceId}/backups/{backupId} | Managed MySQL Database Backup Delete |
| [**deleteDatabasePostgreSQLInstanceBackup**](DatabasesApi.md#deleteDatabasePostgreSQLInstanceBackup) | **DELETE** /databases/postgresql/instances/{instanceId}/backups/{backupId} | Managed PostgreSQL Database Backup Delete |
| [**deleteDatabasesMongoDBInstance**](DatabasesApi.md#deleteDatabasesMongoDBInstance) | **DELETE** /databases/mongodb/instances/{instanceId} | Managed MongoDB Database Delete |
| [**deleteDatabasesMySQLInstance**](DatabasesApi.md#deleteDatabasesMySQLInstance) | **DELETE** /databases/mysql/instances/{instanceId} | Managed MySQL Database Delete |
| [**deleteDatabasesPostgreSQLInstance**](DatabasesApi.md#deleteDatabasesPostgreSQLInstance) | **DELETE** /databases/postgresql/instances/{instanceId} | Managed PostgreSQL Database Delete |
| [**getDatabasesEngine**](DatabasesApi.md#getDatabasesEngine) | **GET** /databases/engines/{engineId} | Managed Database Engine View |
| [**getDatabasesEngines**](DatabasesApi.md#getDatabasesEngines) | **GET** /databases/engines | Managed Database Engines List |
| [**getDatabasesInstances**](DatabasesApi.md#getDatabasesInstances) | **GET** /databases/instances | Managed Databases List All |
| [**getDatabasesMongoDBInstance**](DatabasesApi.md#getDatabasesMongoDBInstance) | **GET** /databases/mongodb/instances/{instanceId} | Managed MongoDB Database View |
| [**getDatabasesMongoDBInstanceBackup**](DatabasesApi.md#getDatabasesMongoDBInstanceBackup) | **GET** /databases/mongodb/instances/{instanceId}/backups/{backupId} | Managed MongoDB Database Backup View |
| [**getDatabasesMongoDBInstanceBackups**](DatabasesApi.md#getDatabasesMongoDBInstanceBackups) | **GET** /databases/mongodb/instances/{instanceId}/backups | Managed MongoDB Database Backups List |
| [**getDatabasesMongoDBInstanceCredentials**](DatabasesApi.md#getDatabasesMongoDBInstanceCredentials) | **GET** /databases/mongodb/instances/{instanceId}/credentials | Managed MongoDB Database Credentials View |
| [**getDatabasesMongoDBInstanceSSL**](DatabasesApi.md#getDatabasesMongoDBInstanceSSL) | **GET** /databases/mongodb/instances/{instanceId}/ssl | Managed MongoDB Database SSL Certificate View |
| [**getDatabasesMongoDBInstances**](DatabasesApi.md#getDatabasesMongoDBInstances) | **GET** /databases/mongodb/instances | Managed MongoDB Databases List |
| [**getDatabasesMySQLInstance**](DatabasesApi.md#getDatabasesMySQLInstance) | **GET** /databases/mysql/instances/{instanceId} | Managed MySQL Database View |
| [**getDatabasesMySQLInstanceBackup**](DatabasesApi.md#getDatabasesMySQLInstanceBackup) | **GET** /databases/mysql/instances/{instanceId}/backups/{backupId} | Managed MySQL Database Backup View |
| [**getDatabasesMySQLInstanceBackups**](DatabasesApi.md#getDatabasesMySQLInstanceBackups) | **GET** /databases/mysql/instances/{instanceId}/backups | Managed MySQL Database Backups List |
| [**getDatabasesMySQLInstanceCredentials**](DatabasesApi.md#getDatabasesMySQLInstanceCredentials) | **GET** /databases/mysql/instances/{instanceId}/credentials | Managed MySQL Database Credentials View |
| [**getDatabasesMySQLInstanceSSL**](DatabasesApi.md#getDatabasesMySQLInstanceSSL) | **GET** /databases/mysql/instances/{instanceId}/ssl | Managed MySQL Database SSL Certificate View |
| [**getDatabasesMySQLInstances**](DatabasesApi.md#getDatabasesMySQLInstances) | **GET** /databases/mysql/instances | Managed MySQL Databases List |
| [**getDatabasesPostgreSQLInstance**](DatabasesApi.md#getDatabasesPostgreSQLInstance) | **GET** /databases/postgresql/instances/{instanceId} | Managed PostgreSQL Database View |
| [**getDatabasesPostgreSQLInstanceBackup**](DatabasesApi.md#getDatabasesPostgreSQLInstanceBackup) | **GET** /databases/postgresql/instances/{instanceId}/backups/{backupId} | Managed PostgreSQL Database Backup View |
| [**getDatabasesPostgreSQLInstanceBackups**](DatabasesApi.md#getDatabasesPostgreSQLInstanceBackups) | **GET** /databases/postgresql/instances/{instanceId}/backups | Managed PostgreSQL Database Backups List |
| [**getDatabasesPostgreSQLInstanceCredentials**](DatabasesApi.md#getDatabasesPostgreSQLInstanceCredentials) | **GET** /databases/postgresql/instances/{instanceId}/credentials | Managed PostgreSQL Database Credentials View |
| [**getDatabasesPostgreSQLInstanceSSL**](DatabasesApi.md#getDatabasesPostgreSQLInstanceSSL) | **GET** /databases/postgresql/instances/{instanceId}/ssl | Managed PostgreSQL Database SSL Certificate View |
| [**getDatabasesPostgreSQLInstances**](DatabasesApi.md#getDatabasesPostgreSQLInstances) | **GET** /databases/postgresql/instances | Managed PostgreSQL Databases List |
| [**getDatabasesType**](DatabasesApi.md#getDatabasesType) | **GET** /databases/types/{typeId} | Managed Database Type View |
| [**getDatabasesTypes**](DatabasesApi.md#getDatabasesTypes) | **GET** /databases/types | Managed Database Types List |
| [**postDatabasesMongoDBInstanceBackup**](DatabasesApi.md#postDatabasesMongoDBInstanceBackup) | **POST** /databases/mongodb/instances/{instanceId}/backups | Managed MongoDB Database Backup Snapshot Create |
| [**postDatabasesMongoDBInstanceBackupRestore**](DatabasesApi.md#postDatabasesMongoDBInstanceBackupRestore) | **POST** /databases/mongodb/instances/{instanceId}/backups/{backupId}/restore | Managed MongoDB Database Backup Restore |
| [**postDatabasesMongoDBInstanceCredentialsReset**](DatabasesApi.md#postDatabasesMongoDBInstanceCredentialsReset) | **POST** /databases/mongodb/instances/{instanceId}/credentials/reset | Managed MongoDB Database Credentials Reset |
| [**postDatabasesMongoDBInstancePatch**](DatabasesApi.md#postDatabasesMongoDBInstancePatch) | **POST** /databases/mongodb/instances/{instanceId}/patch | Managed MongoDB Database Patch |
| [**postDatabasesMySQLInstanceBackup**](DatabasesApi.md#postDatabasesMySQLInstanceBackup) | **POST** /databases/mysql/instances/{instanceId}/backups | Managed MySQL Database Backup Snapshot Create |
| [**postDatabasesMySQLInstanceBackupRestore**](DatabasesApi.md#postDatabasesMySQLInstanceBackupRestore) | **POST** /databases/mysql/instances/{instanceId}/backups/{backupId}/restore | Managed MySQL Database Backup Restore |
| [**postDatabasesMySQLInstanceCredentialsReset**](DatabasesApi.md#postDatabasesMySQLInstanceCredentialsReset) | **POST** /databases/mysql/instances/{instanceId}/credentials/reset | Managed MySQL Database Credentials Reset |
| [**postDatabasesMySQLInstancePatch**](DatabasesApi.md#postDatabasesMySQLInstancePatch) | **POST** /databases/mysql/instances/{instanceId}/patch | Managed MySQL Database Patch |
| [**postDatabasesMySQLInstances**](DatabasesApi.md#postDatabasesMySQLInstances) | **POST** /databases/mysql/instances | Managed MySQL Database Create |
| [**postDatabasesPostgreSQLInstanceBackup**](DatabasesApi.md#postDatabasesPostgreSQLInstanceBackup) | **POST** /databases/postgresql/instances/{instanceId}/backups | Managed PostgreSQL Database Backup Snapshot Create |
| [**postDatabasesPostgreSQLInstanceBackupRestore**](DatabasesApi.md#postDatabasesPostgreSQLInstanceBackupRestore) | **POST** /databases/postgresql/instances/{instanceId}/backups/{backupId}/restore | Managed PostgreSQL Database Backup Restore |
| [**postDatabasesPostgreSQLInstanceCredentialsReset**](DatabasesApi.md#postDatabasesPostgreSQLInstanceCredentialsReset) | **POST** /databases/postgresql/instances/{instanceId}/credentials/reset | Managed PostgreSQL Database Credentials Reset |
| [**postDatabasesPostgreSQLInstancePatch**](DatabasesApi.md#postDatabasesPostgreSQLInstancePatch) | **POST** /databases/postgresql/instances/{instanceId}/patch | Managed PostgreSQL Database Patch |
| [**postDatabasesPostgreSQLInstances**](DatabasesApi.md#postDatabasesPostgreSQLInstances) | **POST** /databases/postgresql/instances | Managed PostgreSQL Database Create |
| [**putDatabasesMongoDBInstance**](DatabasesApi.md#putDatabasesMongoDBInstance) | **PUT** /databases/mongodb/instances/{instanceId} | Managed MongoDB Database Update |
| [**putDatabasesMySQLInstance**](DatabasesApi.md#putDatabasesMySQLInstance) | **PUT** /databases/mysql/instances/{instanceId} | Managed MySQL Database Update |
| [**putDatabasesPostgreSQLInstance**](DatabasesApi.md#putDatabasesPostgreSQLInstance) | **PUT** /databases/postgresql/instances/{instanceId} | Managed PostgreSQL Database Update |


<a id="deleteDatabaseMongoDBInstanceBackup"></a>
# **deleteDatabaseMongoDBInstanceBackup**
> Object deleteDatabaseMongoDBInstanceBackup(instanceId, backupId)

Managed MongoDB Database Backup Delete

Delete a single backup for an accessible Managed MongoDB Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must not be provisioning to perform this command.  **Note**: New MongoDB Databases cannot currently be created. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed MongoDB Database.
    Integer backupId = 56; // Integer | The ID of the Managed MongoDB Database backup.
    try {
      Object result = apiInstance.deleteDatabaseMongoDBInstanceBackup(instanceId, backupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#deleteDatabaseMongoDBInstanceBackup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed MongoDB Database. | |
| **backupId** | **Integer**| The ID of the Managed MongoDB Database backup. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request to delete Database backup successful. |  -  |
| **0** | Error |  -  |

<a id="deleteDatabaseMySQLInstanceBackup"></a>
# **deleteDatabaseMySQLInstanceBackup**
> Object deleteDatabaseMySQLInstanceBackup(instanceId, backupId)

Managed MySQL Database Backup Delete

Delete a single backup for an accessible Managed MySQL Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must not be provisioning to perform this command. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed MySQL Database.
    Integer backupId = 56; // Integer | The ID of the Managed MySQL Database backup.
    try {
      Object result = apiInstance.deleteDatabaseMySQLInstanceBackup(instanceId, backupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#deleteDatabaseMySQLInstanceBackup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed MySQL Database. | |
| **backupId** | **Integer**| The ID of the Managed MySQL Database backup. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request to delete Database backup successful. |  -  |
| **0** | Error |  -  |

<a id="deleteDatabasePostgreSQLInstanceBackup"></a>
# **deleteDatabasePostgreSQLInstanceBackup**
> Object deleteDatabasePostgreSQLInstanceBackup(instanceId, backupId)

Managed PostgreSQL Database Backup Delete

Delete a single backup for an accessible Managed PostgreSQL Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must not be provisioning to perform this command. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed PostgreSQL Database.
    Integer backupId = 56; // Integer | The ID of the Managed PostgreSQL Database backup.
    try {
      Object result = apiInstance.deleteDatabasePostgreSQLInstanceBackup(instanceId, backupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#deleteDatabasePostgreSQLInstanceBackup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed PostgreSQL Database. | |
| **backupId** | **Integer**| The ID of the Managed PostgreSQL Database backup. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request to delete Database backup successful. |  -  |
| **0** | Error |  -  |

<a id="deleteDatabasesMongoDBInstance"></a>
# **deleteDatabasesMongoDBInstance**
> Object deleteDatabasesMongoDBInstance(instanceId)

Managed MongoDB Database Delete

Remove a Managed MongoDB Database from your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60;, &#x60;failed&#x60;, or &#x60;degraded&#x60; status to perform this command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes.  **Note**: New MongoDB Databases cannot currently be created. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed MongoDB Database.
    try {
      Object result = apiInstance.deleteDatabasesMongoDBInstance(instanceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#deleteDatabasesMongoDBInstance");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed MongoDB Database. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Managed MongoDB Database successfully deleted. |  -  |
| **0** | Error |  -  |

<a id="deleteDatabasesMySQLInstance"></a>
# **deleteDatabasesMySQLInstance**
> Object deleteDatabasesMySQLInstance(instanceId)

Managed MySQL Database Delete

Remove a Managed MySQL Database from your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60;, &#x60;failed&#x60;, or &#x60;degraded&#x60; status to perform this command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed MySQL Database.
    try {
      Object result = apiInstance.deleteDatabasesMySQLInstance(instanceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#deleteDatabasesMySQLInstance");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed MySQL Database. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Managed MySQL Database successfully deleted. |  -  |
| **0** | Error |  -  |

<a id="deleteDatabasesPostgreSQLInstance"></a>
# **deleteDatabasesPostgreSQLInstance**
> Object deleteDatabasesPostgreSQLInstance(instanceId)

Managed PostgreSQL Database Delete

Remove a Managed PostgreSQL Database from your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60;, &#x60;failed&#x60;, or &#x60;degraded&#x60; status to perform this command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed PostgreSQL Database.
    try {
      Object result = apiInstance.deleteDatabasesPostgreSQLInstance(instanceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#deleteDatabasesPostgreSQLInstance");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed PostgreSQL Database. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Managed PostgreSQL Database successfully deleted. |  -  |
| **0** | Error |  -  |

<a id="getDatabasesEngine"></a>
# **getDatabasesEngine**
> DatabaseEngine getDatabasesEngine(engineId, page, pageSize)

Managed Database Engine View

Display information for a single Managed Database engine type and version. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    String engineId = "engineId_example"; // String | The ID of the Managed Database engine.
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      DatabaseEngine result = apiInstance.getDatabasesEngine(engineId, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#getDatabasesEngine");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **engineId** | **String**| The ID of the Managed Database engine. | |
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**DatabaseEngine**](DatabaseEngine.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns information for a single Managed Database engine type and version. |  -  |
| **0** | Error |  -  |

<a id="getDatabasesEngines"></a>
# **getDatabasesEngines**
> GetDatabasesEngines200Response getDatabasesEngines(page, pageSize)

Managed Database Engines List

Display all available Managed Database engine types and versions. Engine IDs are used when creating new Managed Databases. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetDatabasesEngines200Response result = apiInstance.getDatabasesEngines(page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#getDatabasesEngines");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetDatabasesEngines200Response**](GetDatabasesEngines200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a paginated list of all available Managed Database engines and versions. |  -  |
| **0** | Error |  -  |

<a id="getDatabasesInstances"></a>
# **getDatabasesInstances**
> GetDatabasesInstances200Response getDatabasesInstances(page, pageSize)

Managed Databases List All

Display all Managed Databases that are accessible by your User, regardless of engine type.  For more detailed information on a particular Database instance, make a request to its &#x60;instance_uri&#x60;. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetDatabasesInstances200Response result = apiInstance.getDatabasesInstances(page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#getDatabasesInstances");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetDatabasesInstances200Response**](GetDatabasesInstances200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a paginated list of all accessible Managed Databases on your Account. |  -  |
| **0** | Error |  -  |

<a id="getDatabasesMongoDBInstance"></a>
# **getDatabasesMongoDBInstance**
> DatabaseMongoDB getDatabasesMongoDBInstance(instanceId)

Managed MongoDB Database View

Display information for a single, accessible Managed MongoDB Database.  **Note**: New MongoDB Databases cannot currently be created. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed MongoDB Database.
    try {
      DatabaseMongoDB result = apiInstance.getDatabasesMongoDBInstance(instanceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#getDatabasesMongoDBInstance");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed MongoDB Database. | |

### Return type

[**DatabaseMongoDB**](DatabaseMongoDB.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns information for a single Managed MongoDB Database. |  -  |
| **0** | Error |  -  |

<a id="getDatabasesMongoDBInstanceBackup"></a>
# **getDatabasesMongoDBInstanceBackup**
> DatabaseBackup getDatabasesMongoDBInstanceBackup(instanceId, backupId)

Managed MongoDB Database Backup View

Display information for a single backup for an accessible Managed MongoDB Database.  The Database must not be provisioning to perform this command.  **Note**: New MongoDB Databases cannot currently be created. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed MongoDB Database.
    Integer backupId = 56; // Integer | The ID of the Managed MongoDB Database backup.
    try {
      DatabaseBackup result = apiInstance.getDatabasesMongoDBInstanceBackup(instanceId, backupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#getDatabasesMongoDBInstanceBackup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed MongoDB Database. | |
| **backupId** | **Integer**| The ID of the Managed MongoDB Database backup. | |

### Return type

[**DatabaseBackup**](DatabaseBackup.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a single backup for the Managed MongoDB Database. |  -  |
| **0** | Error |  -  |

<a id="getDatabasesMongoDBInstanceBackups"></a>
# **getDatabasesMongoDBInstanceBackups**
> GetDatabasesMongoDBInstanceBackups200Response getDatabasesMongoDBInstanceBackups(instanceId, page, pageSize)

Managed MongoDB Database Backups List

Display all backups for an accessible Managed MongoDB Database.  The Database must not be provisioning to perform this command.  Database &#x60;auto&#x60; type backups are created every 24 hours at 0:00 UTC. Each &#x60;auto&#x60; backup is retained for 7 days.  Database &#x60;snapshot&#x60; type backups are created by accessing the **Managed MongoDB Database Backup Snapshot Create** ([POST /databases/mongodb/instances/{instanceId}/backups](/docs/api/databases/#managed-mongodb-database-backup-snapshot-create)) command.  **Note**: New MongoDB Databases cannot currently be created. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed MongoDB Database.
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetDatabasesMongoDBInstanceBackups200Response result = apiInstance.getDatabasesMongoDBInstanceBackups(instanceId, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#getDatabasesMongoDBInstanceBackups");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed MongoDB Database. | |
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetDatabasesMongoDBInstanceBackups200Response**](GetDatabasesMongoDBInstanceBackups200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a paginated list of backups for the Managed MongoDB Database. |  -  |
| **0** | Error |  -  |

<a id="getDatabasesMongoDBInstanceCredentials"></a>
# **getDatabasesMongoDBInstanceCredentials**
> DatabaseCredentials getDatabasesMongoDBInstanceCredentials(instanceId)

Managed MongoDB Database Credentials View

Display the root username and password for an accessible Managed MongoDB Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**: New MongoDB Databases cannot currently be created. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed MongoDB Database.
    try {
      DatabaseCredentials result = apiInstance.getDatabasesMongoDBInstanceCredentials(instanceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#getDatabasesMongoDBInstanceCredentials");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed MongoDB Database. | |

### Return type

[**DatabaseCredentials**](DatabaseCredentials.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Managed Database root username and password. |  -  |
| **0** | Error |  -  |

<a id="getDatabasesMongoDBInstanceSSL"></a>
# **getDatabasesMongoDBInstanceSSL**
> DatabaseSSL getDatabasesMongoDBInstanceSSL(instanceId)

Managed MongoDB Database SSL Certificate View

Display the SSL CA certificate for an accessible Managed MongoDB Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**: New MongoDB Databases cannot currently be created. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed MongoDB Database.
    try {
      DatabaseSSL result = apiInstance.getDatabasesMongoDBInstanceSSL(instanceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#getDatabasesMongoDBInstanceSSL");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed MongoDB Database. | |

### Return type

[**DatabaseSSL**](DatabaseSSL.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the SSL CA certificate of a single Managed MongoDB Database. |  -  |
| **0** | Error |  -  |

<a id="getDatabasesMongoDBInstances"></a>
# **getDatabasesMongoDBInstances**
> GetDatabasesMongoDBInstances200Response getDatabasesMongoDBInstances(page, pageSize)

Managed MongoDB Databases List

Display all accessible Managed MongoDB Databases.  **Note**: New MongoDB Databases cannot currently be created. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetDatabasesMongoDBInstances200Response result = apiInstance.getDatabasesMongoDBInstances(page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#getDatabasesMongoDBInstances");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetDatabasesMongoDBInstances200Response**](GetDatabasesMongoDBInstances200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a paginated list of all accessible Managed MongoDB Databases on your Account. |  -  |
| **0** | Error |  -  |

<a id="getDatabasesMySQLInstance"></a>
# **getDatabasesMySQLInstance**
> DatabaseMySQL getDatabasesMySQLInstance(instanceId)

Managed MySQL Database View

Display information for a single, accessible Managed MySQL Database. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed MySQL Database.
    try {
      DatabaseMySQL result = apiInstance.getDatabasesMySQLInstance(instanceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#getDatabasesMySQLInstance");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed MySQL Database. | |

### Return type

[**DatabaseMySQL**](DatabaseMySQL.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns information for a single Managed MySQL Database. |  -  |
| **0** | Error |  -  |

<a id="getDatabasesMySQLInstanceBackup"></a>
# **getDatabasesMySQLInstanceBackup**
> DatabaseBackup getDatabasesMySQLInstanceBackup(instanceId, backupId)

Managed MySQL Database Backup View

Display information for a single backup for an accessible Managed MySQL Database.  The Database must not be provisioning to perform this command. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed MySQL Database.
    Integer backupId = 56; // Integer | The ID of the Managed MySQL Database backup.
    try {
      DatabaseBackup result = apiInstance.getDatabasesMySQLInstanceBackup(instanceId, backupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#getDatabasesMySQLInstanceBackup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed MySQL Database. | |
| **backupId** | **Integer**| The ID of the Managed MySQL Database backup. | |

### Return type

[**DatabaseBackup**](DatabaseBackup.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a single backup for the Managed MySQL Database. |  -  |
| **0** | Error |  -  |

<a id="getDatabasesMySQLInstanceBackups"></a>
# **getDatabasesMySQLInstanceBackups**
> GetDatabasesMongoDBInstanceBackups200Response getDatabasesMySQLInstanceBackups(instanceId, page, pageSize)

Managed MySQL Database Backups List

Display all backups for an accessible Managed MySQL Database.  The Database must not be provisioning to perform this command.  Database &#x60;auto&#x60; type backups are created every 24 hours at 0:00 UTC. Each &#x60;auto&#x60; backup is retained for 7 days.  Database &#x60;snapshot&#x60; type backups are created by accessing the **Managed MySQL Database Backup Snapshot Create** ([POST /databases/mysql/instances/{instanceId}/backups](/docs/api/databases/#managed-mysql-database-backup-snapshot-create)) command. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed MySQL Database.
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetDatabasesMongoDBInstanceBackups200Response result = apiInstance.getDatabasesMySQLInstanceBackups(instanceId, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#getDatabasesMySQLInstanceBackups");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed MySQL Database. | |
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetDatabasesMongoDBInstanceBackups200Response**](GetDatabasesMongoDBInstanceBackups200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a paginated list of backups for the Managed MySQL Database. |  -  |
| **0** | Error |  -  |

<a id="getDatabasesMySQLInstanceCredentials"></a>
# **getDatabasesMySQLInstanceCredentials**
> DatabaseCredentials getDatabasesMySQLInstanceCredentials(instanceId)

Managed MySQL Database Credentials View

Display the root username and password for an accessible Managed MySQL Database.  The Database must have an &#x60;active&#x60; status to perform this command. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed MySQL Database.
    try {
      DatabaseCredentials result = apiInstance.getDatabasesMySQLInstanceCredentials(instanceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#getDatabasesMySQLInstanceCredentials");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed MySQL Database. | |

### Return type

[**DatabaseCredentials**](DatabaseCredentials.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Managed Database root username and password. |  -  |
| **0** | Error |  -  |

<a id="getDatabasesMySQLInstanceSSL"></a>
# **getDatabasesMySQLInstanceSSL**
> DatabaseSSL getDatabasesMySQLInstanceSSL(instanceId)

Managed MySQL Database SSL Certificate View

Display the SSL CA certificate for an accessible Managed MySQL Database.  The Database must have an &#x60;active&#x60; status to perform this command. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed MySQL Database.
    try {
      DatabaseSSL result = apiInstance.getDatabasesMySQLInstanceSSL(instanceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#getDatabasesMySQLInstanceSSL");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed MySQL Database. | |

### Return type

[**DatabaseSSL**](DatabaseSSL.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the SSL CA certificate of a single Managed MySQL Database. |  -  |
| **0** | Error |  -  |

<a id="getDatabasesMySQLInstances"></a>
# **getDatabasesMySQLInstances**
> GetDatabasesMySQLInstances200Response getDatabasesMySQLInstances(page, pageSize)

Managed MySQL Databases List

Display all accessible Managed MySQL Databases. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetDatabasesMySQLInstances200Response result = apiInstance.getDatabasesMySQLInstances(page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#getDatabasesMySQLInstances");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetDatabasesMySQLInstances200Response**](GetDatabasesMySQLInstances200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a paginated list of all accessible Managed MySQL Databases on your Account. |  -  |
| **0** | Error |  -  |

<a id="getDatabasesPostgreSQLInstance"></a>
# **getDatabasesPostgreSQLInstance**
> DatabasePostgreSQL getDatabasesPostgreSQLInstance(instanceId)

Managed PostgreSQL Database View

Display information for a single, accessible Managed PostgreSQL Database. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed PostgreSQL Database.
    try {
      DatabasePostgreSQL result = apiInstance.getDatabasesPostgreSQLInstance(instanceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#getDatabasesPostgreSQLInstance");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed PostgreSQL Database. | |

### Return type

[**DatabasePostgreSQL**](DatabasePostgreSQL.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns information for a single Managed PostgreSQL Database. |  -  |
| **0** | Error |  -  |

<a id="getDatabasesPostgreSQLInstanceBackup"></a>
# **getDatabasesPostgreSQLInstanceBackup**
> DatabaseBackup getDatabasesPostgreSQLInstanceBackup(instanceId, backupId)

Managed PostgreSQL Database Backup View

Display information for a single backup for an accessible Managed PostgreSQL Database.  The Database must not be provisioning to perform this command. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed PostgreSQL Database.
    Integer backupId = 56; // Integer | The ID of the Managed PostgreSQL Database backup.
    try {
      DatabaseBackup result = apiInstance.getDatabasesPostgreSQLInstanceBackup(instanceId, backupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#getDatabasesPostgreSQLInstanceBackup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed PostgreSQL Database. | |
| **backupId** | **Integer**| The ID of the Managed PostgreSQL Database backup. | |

### Return type

[**DatabaseBackup**](DatabaseBackup.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a single backup for the Managed PostgreSQL Database. |  -  |
| **0** | Error |  -  |

<a id="getDatabasesPostgreSQLInstanceBackups"></a>
# **getDatabasesPostgreSQLInstanceBackups**
> GetDatabasesMongoDBInstanceBackups200Response getDatabasesPostgreSQLInstanceBackups(instanceId, page, pageSize)

Managed PostgreSQL Database Backups List

Display all backups for an accessible Managed PostgreSQL Database.  The Database must not be provisioning to perform this command.  Database &#x60;auto&#x60; type backups are created every 24 hours at 0:00 UTC. Each &#x60;auto&#x60; backup is retained for 7 days.  Database &#x60;snapshot&#x60; type backups are created by accessing the **Managed PostgreSQL Database Backup Snapshot Create** ([POST /databases/postgresql/instances/{instanceId}/backups](/docs/api/databases/#managed-postgresql-database-backup-snapshot-create)) command. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed PostgreSQL Database.
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetDatabasesMongoDBInstanceBackups200Response result = apiInstance.getDatabasesPostgreSQLInstanceBackups(instanceId, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#getDatabasesPostgreSQLInstanceBackups");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed PostgreSQL Database. | |
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetDatabasesMongoDBInstanceBackups200Response**](GetDatabasesMongoDBInstanceBackups200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a paginated list of backups for the Managed PostgreSQL Database. |  -  |
| **0** | Error |  -  |

<a id="getDatabasesPostgreSQLInstanceCredentials"></a>
# **getDatabasesPostgreSQLInstanceCredentials**
> DatabaseCredentials getDatabasesPostgreSQLInstanceCredentials(instanceId)

Managed PostgreSQL Database Credentials View

Display the root username and password for an accessible Managed PostgreSQL Database.  The Database must have an &#x60;active&#x60; status to perform this command. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed PostgreSQL Database.
    try {
      DatabaseCredentials result = apiInstance.getDatabasesPostgreSQLInstanceCredentials(instanceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#getDatabasesPostgreSQLInstanceCredentials");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed PostgreSQL Database. | |

### Return type

[**DatabaseCredentials**](DatabaseCredentials.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Managed Database root username and password. |  -  |
| **0** | Error |  -  |

<a id="getDatabasesPostgreSQLInstanceSSL"></a>
# **getDatabasesPostgreSQLInstanceSSL**
> DatabaseSSL getDatabasesPostgreSQLInstanceSSL(instanceId)

Managed PostgreSQL Database SSL Certificate View

Display the SSL CA certificate for an accessible Managed PostgreSQL Database.  The Database must have an &#x60;active&#x60; status to perform this command. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed PostgreSQL Database.
    try {
      DatabaseSSL result = apiInstance.getDatabasesPostgreSQLInstanceSSL(instanceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#getDatabasesPostgreSQLInstanceSSL");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed PostgreSQL Database. | |

### Return type

[**DatabaseSSL**](DatabaseSSL.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the SSL CA certificate of a single Managed PostgreSQL Database. |  -  |
| **0** | Error |  -  |

<a id="getDatabasesPostgreSQLInstances"></a>
# **getDatabasesPostgreSQLInstances**
> GetDatabasesPostgreSQLInstances200Response getDatabasesPostgreSQLInstances(page, pageSize)

Managed PostgreSQL Databases List

Display all accessible Managed PostgreSQL Databases. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetDatabasesPostgreSQLInstances200Response result = apiInstance.getDatabasesPostgreSQLInstances(page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#getDatabasesPostgreSQLInstances");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetDatabasesPostgreSQLInstances200Response**](GetDatabasesPostgreSQLInstances200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a paginated list of all accessible Managed PostgreSQL Databases on your Account. |  -  |
| **0** | Error |  -  |

<a id="getDatabasesType"></a>
# **getDatabasesType**
> DatabaseType getDatabasesType(typeId, page, pageSize)

Managed Database Type View

Display the details of a single Managed Database type. The type and number of nodes determine the resources and price of a Managed Database instance. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    String typeId = "typeId_example"; // String | The ID of the Managed Database type.
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      DatabaseType result = apiInstance.getDatabasesType(typeId, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#getDatabasesType");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **typeId** | **String**| The ID of the Managed Database type. | |
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**DatabaseType**](DatabaseType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a single Managed Database type. |  -  |
| **0** | Error |  -  |

<a id="getDatabasesTypes"></a>
# **getDatabasesTypes**
> GetDatabasesTypes200Response getDatabasesTypes(page, pageSize)

Managed Database Types List

Display all Managed Database node types. The type and number of nodes determine the resources and price of a Managed Database instance.  Each Managed Database can have one node type. In the case of a high availabilty Database, all nodes are provisioned according to the chosen type. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer page = 1; // Integer | The page of a collection to return.
    Integer pageSize = 100; // Integer | The number of items to return per page.
    try {
      GetDatabasesTypes200Response result = apiInstance.getDatabasesTypes(page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#getDatabasesTypes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **page** | **Integer**| The page of a collection to return. | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of items to return per page. | [optional] [default to 100] |

### Return type

[**GetDatabasesTypes200Response**](GetDatabasesTypes200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a paginated list of all Managed Database types. |  -  |
| **0** | Error |  -  |

<a id="postDatabasesMongoDBInstanceBackup"></a>
# **postDatabasesMongoDBInstanceBackup**
> Object postDatabasesMongoDBInstanceBackup(instanceId, databaseBackupSnapshot)

Managed MongoDB Database Backup Snapshot Create

Creates a snapshot backup of a Managed MongoDB Database.  Requires &#x60;read_write&#x60; access to the Database.  Up to 3 snapshot backups for each Database can be stored at a time. If 3 snapshots have been created for a Database, one must be deleted before another can be made.  Backups generated by this command have the type &#x60;snapshot&#x60;. Snapshot backups may take several minutes to complete, after which they will be accessible to view or restore.  The Database must have an &#x60;active&#x60; status to perform this command. If another backup is in progress, it must complete before a new backup can be initiated.  **Note**: New MongoDB Databases cannot currently be created. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed MongoDB Database.
    DatabaseBackupSnapshot databaseBackupSnapshot = new DatabaseBackupSnapshot(); // DatabaseBackupSnapshot | Information about the snapshot backup to create.
    try {
      Object result = apiInstance.postDatabasesMongoDBInstanceBackup(instanceId, databaseBackupSnapshot);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#postDatabasesMongoDBInstanceBackup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed MongoDB Database. | |
| **databaseBackupSnapshot** | [**DatabaseBackupSnapshot**](DatabaseBackupSnapshot.md)| Information about the snapshot backup to create. | [optional] |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Database snapshot backup request successful. |  -  |
| **0** | Error |  -  |

<a id="postDatabasesMongoDBInstanceBackupRestore"></a>
# **postDatabasesMongoDBInstanceBackupRestore**
> Object postDatabasesMongoDBInstanceBackupRestore(instanceId, backupId)

Managed MongoDB Database Backup Restore

Restore a backup to a Managed MongoDB Database on your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**: Restoring from a backup will erase all existing data on the database instance and replace it with backup data.  **Note**: Currently, restoring a backup after resetting Managed Database credentials results in a failed cluster. Please contact Customer Support if this occurs.  **Note**: New MongoDB Databases cannot currently be created. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed MongoDB Database.
    Integer backupId = 56; // Integer | The ID of the Managed MongoDB Database backup.
    try {
      Object result = apiInstance.postDatabasesMongoDBInstanceBackupRestore(instanceId, backupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#postDatabasesMongoDBInstanceBackupRestore");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed MongoDB Database. | |
| **backupId** | **Integer**| The ID of the Managed MongoDB Database backup. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request to restore backup successful. |  -  |
| **0** | Error |  -  |

<a id="postDatabasesMongoDBInstanceCredentialsReset"></a>
# **postDatabasesMongoDBInstanceCredentialsReset**
> Object postDatabasesMongoDBInstanceCredentialsReset(instanceId)

Managed MongoDB Database Credentials Reset

Reset the root password for a Managed MongoDB Database.  Requires &#x60;read_write&#x60; access to the Database.  A new root password is randomly generated and accessible with the **Managed MongoDB Database Credentials View** ([GET /databases/mongodb/instances/{instanceId}/credentials](/docs/api/databases/#managed-mongodb-database-credentials-view)) command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes.  **Note**: Note that it may take several seconds for credentials to reset.  **Note**: New MongoDB Databases cannot currently be created. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed MongoDB Database.
    try {
      Object result = apiInstance.postDatabasesMongoDBInstanceCredentialsReset(instanceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#postDatabasesMongoDBInstanceCredentialsReset");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed MongoDB Database. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Managed Database instance credentials successfully reset. |  -  |
| **0** | Error |  -  |

<a id="postDatabasesMongoDBInstancePatch"></a>
# **postDatabasesMongoDBInstancePatch**
> Object postDatabasesMongoDBInstancePatch(instanceId)

Managed MongoDB Database Patch

Apply security patches and updates to the underlying operating system of the Managed MongoDB Database. This function runs during regular maintenance windows, which are configurable with the **Managed MongoDB Database Update** ([PUT /databases/mongodb/instances/{instanceId}](/docs/api/databases/#managed-mongodb-database-update)) command. Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**:  * If your database cluster is configured with a single node, you will experience downtime during this maintenance. Consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one.  **Note**: New MongoDB Databases cannot currently be created. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed MongoDB Database.
    try {
      Object result = apiInstance.postDatabasesMongoDBInstancePatch(instanceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#postDatabasesMongoDBInstancePatch");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed MongoDB Database. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Managed Database instance patch request successful. |  -  |
| **0** | Error |  -  |

<a id="postDatabasesMySQLInstanceBackup"></a>
# **postDatabasesMySQLInstanceBackup**
> Object postDatabasesMySQLInstanceBackup(instanceId, databaseBackupSnapshot)

Managed MySQL Database Backup Snapshot Create

Creates a snapshot backup of a Managed MySQL Database.  Requires &#x60;read_write&#x60; access to the Database.  Up to 3 snapshot backups for each Database can be stored at a time. If 3 snapshots have been created for a Database, one must be deleted before another can be made.  Backups generated by this command have the type &#x60;snapshot&#x60;. Snapshot backups may take several minutes to complete, after which they will be accessible to view or restore.  The Database must have an &#x60;active&#x60; status to perform this command. If another backup is in progress, it must complete before a new backup can be initiated. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed MySQL Database.
    DatabaseBackupSnapshot databaseBackupSnapshot = new DatabaseBackupSnapshot(); // DatabaseBackupSnapshot | Information about the snapshot backup to create.
    try {
      Object result = apiInstance.postDatabasesMySQLInstanceBackup(instanceId, databaseBackupSnapshot);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#postDatabasesMySQLInstanceBackup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed MySQL Database. | |
| **databaseBackupSnapshot** | [**DatabaseBackupSnapshot**](DatabaseBackupSnapshot.md)| Information about the snapshot backup to create. | [optional] |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Database snapshot backup request successful. |  -  |
| **0** | Error |  -  |

<a id="postDatabasesMySQLInstanceBackupRestore"></a>
# **postDatabasesMySQLInstanceBackupRestore**
> Object postDatabasesMySQLInstanceBackupRestore(instanceId, backupId)

Managed MySQL Database Backup Restore

Restore a backup to a Managed MySQL Database on your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**: Restoring from a backup will erase all existing data on the database instance and replace it with backup data.  **Note**: Currently, restoring a backup after resetting Managed Database credentials results in a failed cluster. Please contact Customer Support if this occurs. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed MySQL Database.
    Integer backupId = 56; // Integer | The ID of the Managed MySQL Database backup.
    try {
      Object result = apiInstance.postDatabasesMySQLInstanceBackupRestore(instanceId, backupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#postDatabasesMySQLInstanceBackupRestore");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed MySQL Database. | |
| **backupId** | **Integer**| The ID of the Managed MySQL Database backup. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request to restore backup successful. |  -  |
| **0** | Error |  -  |

<a id="postDatabasesMySQLInstanceCredentialsReset"></a>
# **postDatabasesMySQLInstanceCredentialsReset**
> Object postDatabasesMySQLInstanceCredentialsReset(instanceId)

Managed MySQL Database Credentials Reset

Reset the root password for a Managed MySQL Database.  Requires &#x60;read_write&#x60; access to the Database.  A new root password is randomly generated and accessible with the **Managed MySQL Database Credentials View** ([GET /databases/mysql/instances/{instanceId}/credentials](/docs/api/databases/#managed-mysql-database-credentials-view)) command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes.  **Note**: Note that it may take several seconds for credentials to reset. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed MySQL Database.
    try {
      Object result = apiInstance.postDatabasesMySQLInstanceCredentialsReset(instanceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#postDatabasesMySQLInstanceCredentialsReset");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed MySQL Database. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Managed Database instance credentials successfully reset. |  -  |
| **0** | Error |  -  |

<a id="postDatabasesMySQLInstancePatch"></a>
# **postDatabasesMySQLInstancePatch**
> Object postDatabasesMySQLInstancePatch(instanceId)

Managed MySQL Database Patch

Apply security patches and updates to the underlying operating system of the Managed MySQL Database. This function runs during regular maintenance windows, which are configurable with the **Managed MySQL Database Update** ([PUT /databases/mysql/instances/{instanceId}](/docs/api/databases/#managed-mysql-database-update)) command.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**  * If your database cluster is configured with a single node, you will experience downtime during this maintenance. Consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then [migrate your databases](/docs/products/databases/managed-databases/guides/migrate-mysql/) from the original Managed Database cluster to the new one. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed MySQL Database.
    try {
      Object result = apiInstance.postDatabasesMySQLInstancePatch(instanceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#postDatabasesMySQLInstancePatch");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed MySQL Database. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Managed Database instance patch request successful. |  -  |
| **0** | Error |  -  |

<a id="postDatabasesMySQLInstances"></a>
# **postDatabasesMySQLInstances**
> DatabaseMySQL postDatabasesMySQLInstances(databaseMySQLRequest)

Managed MySQL Database Create

Provision a Managed MySQL Database.  Restricted Users must have the &#x60;add_databases&#x60; grant to use this command.  New instances can take approximately 15 to 30 minutes to provision.  The &#x60;allow_list&#x60; is used to control access to the Managed Database.  * IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.  * If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (&#x60;[]&#x60;) blocks all connections (both public and private) to the Managed Database.  All Managed Databases include automatic, daily backups. Up to seven backups are automatically stored for each Managed Database, providing restore points for each day of the past week.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed MySQL Database during configurable maintenance windows.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It&#39;s recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then [migrate your databases](/docs/products/databases/managed-databases/guides/migrate-mysql/) from the original Managed Database cluster to the new one.  * To modify update the maintenance window for a Database, use the **Managed MySQL Database Update** ([PUT /databases/mysql/instances/{instanceId}](/docs/api/databases/#managed-mysql-database-update)) command. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    DatabaseMySQLRequest databaseMySQLRequest = new DatabaseMySQLRequest(); // DatabaseMySQLRequest | Information about the Managed MySQL Database you are creating.
    try {
      DatabaseMySQL result = apiInstance.postDatabasesMySQLInstances(databaseMySQLRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#postDatabasesMySQLInstances");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databaseMySQLRequest** | [**DatabaseMySQLRequest**](DatabaseMySQLRequest.md)| Information about the Managed MySQL Database you are creating. | |

### Return type

[**DatabaseMySQL**](DatabaseMySQL.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A new Managed MySQL Database is provisioning. |  -  |
| **0** | Error |  -  |

<a id="postDatabasesPostgreSQLInstanceBackup"></a>
# **postDatabasesPostgreSQLInstanceBackup**
> Object postDatabasesPostgreSQLInstanceBackup(instanceId, databaseBackupSnapshot)

Managed PostgreSQL Database Backup Snapshot Create

Creates a snapshot backup of a Managed PostgreSQL Database.  Requires &#x60;read_write&#x60; access to the Database.  Up to 3 snapshot backups for each Database can be stored at a time. If 3 snapshots have been created for a Database, one must be deleted before another can be made.  Backups generated by this command have the type &#x60;snapshot&#x60;. Snapshot backups may take several minutes to complete, after which they will be accessible to view or restore.  The Database must have an &#x60;active&#x60; status to perform this command. If another backup is in progress, it must complete before a new backup can be initiated. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed PostgreSQL Database.
    DatabaseBackupSnapshot databaseBackupSnapshot = new DatabaseBackupSnapshot(); // DatabaseBackupSnapshot | Information about the snapshot backup to create.
    try {
      Object result = apiInstance.postDatabasesPostgreSQLInstanceBackup(instanceId, databaseBackupSnapshot);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#postDatabasesPostgreSQLInstanceBackup");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed PostgreSQL Database. | |
| **databaseBackupSnapshot** | [**DatabaseBackupSnapshot**](DatabaseBackupSnapshot.md)| Information about the snapshot backup to create. | [optional] |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Database snapshot backup request successful. |  -  |
| **0** | Error |  -  |

<a id="postDatabasesPostgreSQLInstanceBackupRestore"></a>
# **postDatabasesPostgreSQLInstanceBackupRestore**
> Object postDatabasesPostgreSQLInstanceBackupRestore(instanceId, backupId)

Managed PostgreSQL Database Backup Restore

Restore a backup to a Managed PostgreSQL Database on your Account.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**: Restoring from a backup will erase all existing data on the database instance and replace it with backup data.  **Note**: Currently, restoring a backup after resetting Managed Database credentials results in a failed cluster. Please contact Customer Support if this occurs. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed PostgreSQL Database.
    Integer backupId = 56; // Integer | The ID of the Managed PostgreSQL Database backup.
    try {
      Object result = apiInstance.postDatabasesPostgreSQLInstanceBackupRestore(instanceId, backupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#postDatabasesPostgreSQLInstanceBackupRestore");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed PostgreSQL Database. | |
| **backupId** | **Integer**| The ID of the Managed PostgreSQL Database backup. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request to restore backup successful. |  -  |
| **0** | Error |  -  |

<a id="postDatabasesPostgreSQLInstanceCredentialsReset"></a>
# **postDatabasesPostgreSQLInstanceCredentialsReset**
> Object postDatabasesPostgreSQLInstanceCredentialsReset(instanceId)

Managed PostgreSQL Database Credentials Reset

Reset the root password for a Managed PostgreSQL Database.  Requires &#x60;read_write&#x60; access to the Database.  A new root password is randomly generated and accessible with the **Managed PostgreSQL Database Credentials View** ([GET /databases/postgresql/instances/{instanceId}/credentials](/docs/api/databases/#managed-postgresql-database-credentials-view)) command.  Only unrestricted Users can access this command, and have access regardless of the acting token&#39;s OAuth scopes.  **Note**: Note that it may take several seconds for credentials to reset. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed PostgreSQL Database.
    try {
      Object result = apiInstance.postDatabasesPostgreSQLInstanceCredentialsReset(instanceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#postDatabasesPostgreSQLInstanceCredentialsReset");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed PostgreSQL Database. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Managed Database instance credentials successfully reset. |  -  |
| **0** | Error |  -  |

<a id="postDatabasesPostgreSQLInstancePatch"></a>
# **postDatabasesPostgreSQLInstancePatch**
> Object postDatabasesPostgreSQLInstancePatch(instanceId)

Managed PostgreSQL Database Patch

Apply security patches and updates to the underlying operating system of the Managed PostgreSQL Database. This function runs during regular maintenance windows, which are configurable with the **Managed PostgreSQL Database Update** ([PUT /databases/postgresql/instances/{instanceId}](/docs/api/databases/#managed-postgresql-database-update)) command.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  **Note**  * If your database cluster is configured with a single node, you will experience downtime during this maintenance. Consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed PostgreSQL Database.
    try {
      Object result = apiInstance.postDatabasesPostgreSQLInstancePatch(instanceId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#postDatabasesPostgreSQLInstancePatch");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed PostgreSQL Database. | |

### Return type

**Object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Managed Database instance patch request successful. |  -  |
| **0** | Error |  -  |

<a id="postDatabasesPostgreSQLInstances"></a>
# **postDatabasesPostgreSQLInstances**
> DatabasePostgreSQL postDatabasesPostgreSQLInstances(databasePostgreSQLRequest)

Managed PostgreSQL Database Create

Provision a Managed PostgreSQL Database.  Restricted Users must have the &#x60;add_databases&#x60; grant to use this command.  New instances can take approximately 15 to 30 minutes to provision.  The &#x60;allow_list&#x60; is used to control access to the Managed Database.  * IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.  * If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (&#x60;[]&#x60;) blocks all connections (both public and private) to the Managed Database.  All Managed Databases include automatic, daily backups. Up to seven backups are automatically stored for each Managed Database, providing restore points for each day of the past week.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed PostgreSQL Database during configurable maintenance windows.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It&#39;s recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one.  * To modify update the maintenance window for a Database, use the **Managed PostgreSQL Database Update** ([PUT /databases/postgresql/instances/{instanceId}](/docs/api/databases/#managed-postgresql-database-update)) command. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    DatabasePostgreSQLRequest databasePostgreSQLRequest = new DatabasePostgreSQLRequest(); // DatabasePostgreSQLRequest | Information about the Managed PostgreSQL Database you are creating.
    try {
      DatabasePostgreSQL result = apiInstance.postDatabasesPostgreSQLInstances(databasePostgreSQLRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#postDatabasesPostgreSQLInstances");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **databasePostgreSQLRequest** | [**DatabasePostgreSQLRequest**](DatabasePostgreSQLRequest.md)| Information about the Managed PostgreSQL Database you are creating. | |

### Return type

[**DatabasePostgreSQL**](DatabasePostgreSQL.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A new Managed PostgreSQL Database is provisioning. |  -  |
| **0** | Error |  -  |

<a id="putDatabasesMongoDBInstance"></a>
# **putDatabasesMongoDBInstance**
> DatabaseMongoDB putDatabasesMongoDBInstance(instanceId, putDatabasesMongoDBInstanceRequest)

Managed MongoDB Database Update

Update a Managed MongoDB Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  Updating addresses in the &#x60;allow_list&#x60; overwrites any existing addresses.  * IP addresses and ranges on this list can access the Managed Database. All other sources are blocked.  * If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (&#x60;[]&#x60;) blocks all connections (both public and private) to the Managed Database.  * **Note**: Updates to the &#x60;allow_list&#x60; may take a short period of time to complete, making this command inappropriate for rapid successive updates to this property.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed MongoDB Database. The maintenance window for these updates is configured with the Managed Database&#39;s &#x60;updates&#x60; property.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It&#39;s recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one.  **Note**: New MongoDB Databases cannot currently be created. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed MongoDB Database.
    PutDatabasesMongoDBInstanceRequest putDatabasesMongoDBInstanceRequest = new PutDatabasesMongoDBInstanceRequest(); // PutDatabasesMongoDBInstanceRequest | Updated information for the Managed MongoDB Database.
    try {
      DatabaseMongoDB result = apiInstance.putDatabasesMongoDBInstance(instanceId, putDatabasesMongoDBInstanceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#putDatabasesMongoDBInstance");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed MongoDB Database. | |
| **putDatabasesMongoDBInstanceRequest** | [**PutDatabasesMongoDBInstanceRequest**](PutDatabasesMongoDBInstanceRequest.md)| Updated information for the Managed MongoDB Database. | |

### Return type

[**DatabaseMongoDB**](DatabaseMongoDB.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Managed Database updated successfully. |  -  |
| **0** | Error |  -  |

<a id="putDatabasesMySQLInstance"></a>
# **putDatabasesMySQLInstance**
> DatabaseMySQL putDatabasesMySQLInstance(instanceId, putDatabasesMySQLInstanceRequest)

Managed MySQL Database Update

Update a Managed MySQL Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  Updating addresses in the &#x60;allow_list&#x60; overwrites any existing addresses.  * IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.  * If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (&#x60;[]&#x60;) blocks all connections (both public and private) to the Managed Database.  * **Note**: Updates to the &#x60;allow_list&#x60; may take a short period of time to complete, making this command inappropriate for rapid successive updates to this property.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed MySQL Database. The maintenance window for these updates is configured with the Managed Database&#39;s &#x60;updates&#x60; property.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It&#39;s recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then [migrate your databases](/docs/products/databases/managed-databases/guides/migrate-mysql/) from the original Managed Database cluster to the new one. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed MySQL Database.
    PutDatabasesMySQLInstanceRequest putDatabasesMySQLInstanceRequest = new PutDatabasesMySQLInstanceRequest(); // PutDatabasesMySQLInstanceRequest | Updated information for the Managed MySQL Database.
    try {
      DatabaseMySQL result = apiInstance.putDatabasesMySQLInstance(instanceId, putDatabasesMySQLInstanceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#putDatabasesMySQLInstance");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed MySQL Database. | |
| **putDatabasesMySQLInstanceRequest** | [**PutDatabasesMySQLInstanceRequest**](PutDatabasesMySQLInstanceRequest.md)| Updated information for the Managed MySQL Database. | |

### Return type

[**DatabaseMySQL**](DatabaseMySQL.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Managed Database updated successfully. |  -  |
| **0** | Error |  -  |

<a id="putDatabasesPostgreSQLInstance"></a>
# **putDatabasesPostgreSQLInstance**
> DatabasePostgreSQL putDatabasesPostgreSQLInstance(instanceId, putDatabasesPostgreSQLInstanceRequest)

Managed PostgreSQL Database Update

Update a Managed PostgreSQL Database.  Requires &#x60;read_write&#x60; access to the Database.  The Database must have an &#x60;active&#x60; status to perform this command.  Updating addresses in the &#x60;allow_list&#x60; overwrites any existing addresses.  * IP addresses and ranges in this list can access the Managed Database. All other sources are blocked.  * If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database.  * Entering an empty array (&#x60;[]&#x60;) blocks all connections (both public and private) to the Managed Database.  * **Note**: Updates to the &#x60;allow_list&#x60; may take a short period of time to complete, making this command inappropriate for rapid successive updates to this property.  All Managed Databases include automatic patch updates, which apply security patches and updates to the underlying operating system of the Managed PostgreSQL Database. The maintenance window for these updates is configured with the Managed Database&#39;s &#x60;updates&#x60; property.  * If your database cluster is configured with a single node, you will experience downtime during this maintenance window when any updates occur. It&#39;s recommended that you adjust this window to match a time that will be the least disruptive for your application and users. You may also want to consider upgrading to a high availability plan to avoid any downtime due to maintenance.  * **The database software is not updated automatically.** To upgrade to a new database engine version, consider deploying a new Managed Database with your preferred version. You can then migrate your databases from the original Managed Database cluster to the new one. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.linode.com/v4");
    
    // Configure HTTP bearer authorization: personalAccessToken
    HttpBearerAuth personalAccessToken = (HttpBearerAuth) defaultClient.getAuthentication("personalAccessToken");
    personalAccessToken.setBearerToken("BEARER TOKEN");

    // Configure OAuth2 access token for authorization: oauth
    OAuth oauth = (OAuth) defaultClient.getAuthentication("oauth");
    oauth.setAccessToken("YOUR ACCESS TOKEN");

    DatabasesApi apiInstance = new DatabasesApi(defaultClient);
    Integer instanceId = 56; // Integer | The ID of the Managed PostgreSQL Database.
    PutDatabasesPostgreSQLInstanceRequest putDatabasesPostgreSQLInstanceRequest = new PutDatabasesPostgreSQLInstanceRequest(); // PutDatabasesPostgreSQLInstanceRequest | Updated information for the Managed PostgreSQL Database.
    try {
      DatabasePostgreSQL result = apiInstance.putDatabasesPostgreSQLInstance(instanceId, putDatabasesPostgreSQLInstanceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DatabasesApi#putDatabasesPostgreSQLInstance");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **instanceId** | **Integer**| The ID of the Managed PostgreSQL Database. | |
| **putDatabasesPostgreSQLInstanceRequest** | [**PutDatabasesPostgreSQLInstanceRequest**](PutDatabasesPostgreSQLInstanceRequest.md)| Updated information for the Managed PostgreSQL Database. | |

### Return type

[**DatabasePostgreSQL**](DatabasePostgreSQL.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Managed Database updated successfully. |  -  |
| **0** | Error |  -  |

