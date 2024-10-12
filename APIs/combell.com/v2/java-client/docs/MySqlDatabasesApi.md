# MySqlDatabasesApi

All URIs are relative to */v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**changeDatabaseUserPassword**](MySqlDatabasesApi.md#changeDatabaseUserPassword) | **PUT** /mysqldatabases/{databaseName}/users/{userName}/password | Change password for mysql user |
| [**changeDatabaseUserStatus**](MySqlDatabasesApi.md#changeDatabaseUserStatus) | **PUT** /mysqldatabases/{databaseName}/users/{userName}/status | Enable/disable mysql user |
| [**createMySqlDatabase**](MySqlDatabasesApi.md#createMySqlDatabase) | **POST** /mysqldatabases | Create a new mysql database |
| [**createMySqlUser**](MySqlDatabasesApi.md#createMySqlUser) | **POST** /mysqldatabases/{databaseName}/users | Create a new mysql user |
| [**deleteDatabase**](MySqlDatabasesApi.md#deleteDatabase) | **DELETE** /mysqldatabases/{databaseName} | Delete a mysql database |
| [**deleteDatabaseUser**](MySqlDatabasesApi.md#deleteDatabaseUser) | **DELETE** /mysqldatabases/{databaseName}/users/{userName} | Delete a mysql user |
| [**getDatabaseUsers**](MySqlDatabasesApi.md#getDatabaseUsers) | **GET** /mysqldatabases/{databaseName}/users | Overview of mysql users |
| [**getMySqlDatabase**](MySqlDatabasesApi.md#getMySqlDatabase) | **GET** /mysqldatabases/{databaseName} | Get a specific database |
| [**getMySqlDatabases**](MySqlDatabasesApi.md#getMySqlDatabases) | **GET** /mysqldatabases | Overview of mysql databases |


<a id="changeDatabaseUserPassword"></a>
# **changeDatabaseUserPassword**
> changeDatabaseUserPassword(databaseName, userName, databaseName2, userName2, updateUserPasswordRequest)

Change password for mysql user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MySqlDatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    MySqlDatabasesApi apiInstance = new MySqlDatabasesApi(defaultClient);
    String databaseName = "databaseName_example"; // String | Name of the database.
    String userName = "userName_example"; // String | Name of the user.
    String databaseName2 = "databaseName_example"; // String | Automatically added
    String userName2 = "userName_example"; // String | Automatically added
    UpdateUserPasswordRequest updateUserPasswordRequest = new UpdateUserPasswordRequest(); // UpdateUserPasswordRequest | Contains the new password.
    try {
      apiInstance.changeDatabaseUserPassword(databaseName, userName, databaseName2, userName2, updateUserPasswordRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MySqlDatabasesApi#changeDatabaseUserPassword");
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
| **databaseName** | **String**| Name of the database. | |
| **userName** | **String**| Name of the user. | |
| **databaseName2** | **String**| Automatically added | |
| **userName2** | **String**| Automatically added | |
| **updateUserPasswordRequest** | [**UpdateUserPasswordRequest**](UpdateUserPasswordRequest.md)| Contains the new password. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="changeDatabaseUserStatus"></a>
# **changeDatabaseUserStatus**
> changeDatabaseUserStatus(databaseName, userName, databaseName2, userName2, updateUserStatusRequest)

Enable/disable mysql user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MySqlDatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    MySqlDatabasesApi apiInstance = new MySqlDatabasesApi(defaultClient);
    String databaseName = "databaseName_example"; // String | Name of the database.
    String userName = "userName_example"; // String | Name of the user.
    String databaseName2 = "databaseName_example"; // String | Automatically added
    String userName2 = "userName_example"; // String | Automatically added
    UpdateUserStatusRequest updateUserStatusRequest = new UpdateUserStatusRequest(); // UpdateUserStatusRequest | Whether the user is enabled or not.
    try {
      apiInstance.changeDatabaseUserStatus(databaseName, userName, databaseName2, userName2, updateUserStatusRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling MySqlDatabasesApi#changeDatabaseUserStatus");
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
| **databaseName** | **String**| Name of the database. | |
| **userName** | **String**| Name of the user. | |
| **databaseName2** | **String**| Automatically added | |
| **userName2** | **String**| Automatically added | |
| **updateUserStatusRequest** | [**UpdateUserStatusRequest**](UpdateUserStatusRequest.md)| Whether the user is enabled or not. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |

<a id="createMySqlDatabase"></a>
# **createMySqlDatabase**
> createMySqlDatabase(createMySqlDatabase)

Create a new mysql database

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MySqlDatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    MySqlDatabasesApi apiInstance = new MySqlDatabasesApi(defaultClient);
    CreateMySqlDatabase createMySqlDatabase = new CreateMySqlDatabase(); // CreateMySqlDatabase | 
    try {
      apiInstance.createMySqlDatabase(createMySqlDatabase);
    } catch (ApiException e) {
      System.err.println("Exception when calling MySqlDatabasesApi#createMySqlDatabase");
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
| **createMySqlDatabase** | [**CreateMySqlDatabase**](CreateMySqlDatabase.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="createMySqlUser"></a>
# **createMySqlUser**
> createMySqlUser(databaseName, databaseName2, createMySqlUser)

Create a new mysql user

The creation of a new mysql user will result in a user with read_only rights.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MySqlDatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    MySqlDatabasesApi apiInstance = new MySqlDatabasesApi(defaultClient);
    String databaseName = "databaseName_example"; // String | Name of the database.
    String databaseName2 = "databaseName_example"; // String | Automatically added
    CreateMySqlUser createMySqlUser = new CreateMySqlUser(); // CreateMySqlUser | 
    try {
      apiInstance.createMySqlUser(databaseName, databaseName2, createMySqlUser);
    } catch (ApiException e) {
      System.err.println("Exception when calling MySqlDatabasesApi#createMySqlUser");
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
| **databaseName** | **String**| Name of the database. | |
| **databaseName2** | **String**| Automatically added | |
| **createMySqlUser** | [**CreateMySqlUser**](CreateMySqlUser.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **202** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="deleteDatabase"></a>
# **deleteDatabase**
> deleteDatabase(databaseName, databaseName2)

Delete a mysql database

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MySqlDatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    MySqlDatabasesApi apiInstance = new MySqlDatabasesApi(defaultClient);
    String databaseName = "databaseName_example"; // String | Name of the database.
    String databaseName2 = "databaseName_example"; // String | Automatically added
    try {
      apiInstance.deleteDatabase(databaseName, databaseName2);
    } catch (ApiException e) {
      System.err.println("Exception when calling MySqlDatabasesApi#deleteDatabase");
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
| **databaseName** | **String**| Name of the database. | |
| **databaseName2** | **String**| Automatically added | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="deleteDatabaseUser"></a>
# **deleteDatabaseUser**
> deleteDatabaseUser(databaseName, userName, databaseName2, userName2)

Delete a mysql user

The deletion of a mysql user is allowed for users with read_only rights.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MySqlDatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    MySqlDatabasesApi apiInstance = new MySqlDatabasesApi(defaultClient);
    String databaseName = "databaseName_example"; // String | Name of the database.
    String userName = "userName_example"; // String | Name of the user.
    String databaseName2 = "databaseName_example"; // String | Automatically added
    String userName2 = "userName_example"; // String | Automatically added
    try {
      apiInstance.deleteDatabaseUser(databaseName, userName, databaseName2, userName2);
    } catch (ApiException e) {
      System.err.println("Exception when calling MySqlDatabasesApi#deleteDatabaseUser");
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
| **databaseName** | **String**| Name of the database. | |
| **userName** | **String**| Name of the user. | |
| **databaseName2** | **String**| Automatically added | |
| **userName2** | **String**| Automatically added | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="getDatabaseUsers"></a>
# **getDatabaseUsers**
> List&lt;MySqlUser&gt; getDatabaseUsers(databaseName, databaseName2)

Overview of mysql users

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MySqlDatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    MySqlDatabasesApi apiInstance = new MySqlDatabasesApi(defaultClient);
    String databaseName = "databaseName_example"; // String | Name of the database.
    String databaseName2 = "databaseName_example"; // String | Automatically added
    try {
      List<MySqlUser> result = apiInstance.getDatabaseUsers(databaseName, databaseName2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MySqlDatabasesApi#getDatabaseUsers");
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
| **databaseName** | **String**| Name of the database. | |
| **databaseName2** | **String**| Automatically added | |

### Return type

[**List&lt;MySqlUser&gt;**](MySqlUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getMySqlDatabase"></a>
# **getMySqlDatabase**
> MySqlDatabase getMySqlDatabase(databaseName, databaseName2)

Get a specific database

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MySqlDatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    MySqlDatabasesApi apiInstance = new MySqlDatabasesApi(defaultClient);
    String databaseName = "databaseName_example"; // String | 
    String databaseName2 = "databaseName_example"; // String | Automatically added
    try {
      MySqlDatabase result = apiInstance.getMySqlDatabase(databaseName, databaseName2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MySqlDatabasesApi#getMySqlDatabase");
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
| **databaseName** | **String**|  | |
| **databaseName2** | **String**| Automatically added | |

### Return type

[**MySqlDatabase**](MySqlDatabase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getMySqlDatabases"></a>
# **getMySqlDatabases**
> List&lt;MySqlDatabase&gt; getMySqlDatabases(skip, take)

Overview of mysql databases

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MySqlDatabasesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/v2");

    MySqlDatabasesApi apiInstance = new MySqlDatabasesApi(defaultClient);
    Integer skip = 56; // Integer | The number of items to skip in the resultset.
    Integer take = 56; // Integer | The number of items to return in the resultset. The returned count can be equal or less than this number.
    try {
      List<MySqlDatabase> result = apiInstance.getMySqlDatabases(skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MySqlDatabasesApi#getMySqlDatabases");
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
| **skip** | **Integer**| The number of items to skip in the resultset. | [optional] |
| **take** | **Integer**| The number of items to return in the resultset. The returned count can be equal or less than this number. | [optional] |

### Return type

[**List&lt;MySqlDatabase&gt;**](MySqlDatabase.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  * X-Paging-Skipped - The number of results that have been skipped. <br>  * X-Paging-Take - The number of items in the current take. The number might differ from the requested take. It represents the actual number of items returned in the response. <br>  * X-Paging-TotalResults - The total number of results regardless of paging. <br>  |

