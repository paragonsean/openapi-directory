# UserManagementApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAccount**](UserManagementApi.md#createAccount) | **POST** /accounts | Create a new user. Only avaialble to admin user. |
| [**createUser**](UserManagementApi.md#createUser) | **POST** /accounts/{accountname}/users | Create a new user |
| [**createUserCredential**](UserManagementApi.md#createUserCredential) | **POST** /accounts/{accountname}/users/{username}/credentials | add/replace credential |
| [**deleteAccount**](UserManagementApi.md#deleteAccount) | **DELETE** /accounts/{accountname} | Delete the specified account, only allowed if the account is in the disabled state. All users will be deleted along with the account and all resources will be garbage collected |
| [**deleteUser**](UserManagementApi.md#deleteUser) | **DELETE** /accounts/{accountname}/users/{username} | Delete a specific user credential by username of the credential. Cannot be the credential used to authenticate the request. |
| [**deleteUserCredential**](UserManagementApi.md#deleteUserCredential) | **DELETE** /accounts/{accountname}/users/{username}/credentials | Delete a credential by type |
| [**getAccount**](UserManagementApi.md#getAccount) | **GET** /accounts/{accountname} | Get info about an user. Only available to admin user. Uses the main user Id, not a username. |
| [**getAccountUser**](UserManagementApi.md#getAccountUser) | **GET** /accounts/{accountname}/users/{username} | Get a specific user in the specified account |
| [**listAccounts**](UserManagementApi.md#listAccounts) | **GET** /accounts | List user summaries. Only available to the system admin user. |
| [**listUserCredentials**](UserManagementApi.md#listUserCredentials) | **GET** /accounts/{accountname}/users/{username}/credentials | Get current credential summary |
| [**listUsers**](UserManagementApi.md#listUsers) | **GET** /accounts/{accountname}/users | List accounts for the user |
| [**updateAccountState**](UserManagementApi.md#updateAccountState) | **PUT** /accounts/{accountname}/state | Update the state of an account to either enabled or disabled. For deletion use the DELETE route |


<a id="createAccount"></a>
# **createAccount**
> Account createAccount(accountCreationRequest)

Create a new user. Only avaialble to admin user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    UserManagementApi apiInstance = new UserManagementApi(defaultClient);
    AccountCreationRequest accountCreationRequest = new AccountCreationRequest(); // AccountCreationRequest | 
    try {
      Account result = apiInstance.createAccount(accountCreationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserManagementApi#createAccount");
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
| **accountCreationRequest** | [**AccountCreationRequest**](AccountCreationRequest.md)|  | |

### Return type

[**Account**](Account.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account Record |  -  |
| **409** | Conflicting user information. User already exists. |  -  |
| **500** | Internal error |  -  |

<a id="createUser"></a>
# **createUser**
> User createUser(accountname, userCreationRequest)

Create a new user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    UserManagementApi apiInstance = new UserManagementApi(defaultClient);
    String accountname = "accountname_example"; // String | 
    UserCreationRequest userCreationRequest = new UserCreationRequest(); // UserCreationRequest | 
    try {
      User result = apiInstance.createUser(accountname, userCreationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserManagementApi#createUser");
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
| **accountname** | **String**|  | |
| **userCreationRequest** | [**UserCreationRequest**](UserCreationRequest.md)|  | |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Credential summary |  -  |

<a id="createUserCredential"></a>
# **createUserCredential**
> User createUserCredential(accountname, username, accessCredential)

add/replace credential

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    UserManagementApi apiInstance = new UserManagementApi(defaultClient);
    String accountname = "accountname_example"; // String | 
    String username = "username_example"; // String | 
    AccessCredential accessCredential = new AccessCredential(); // AccessCredential | 
    try {
      User result = apiInstance.createUserCredential(accountname, username, accessCredential);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserManagementApi#createUserCredential");
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
| **accountname** | **String**|  | |
| **username** | **String**|  | |
| **accessCredential** | [**AccessCredential**](AccessCredential.md)|  | |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Add a credential, overwritting if already exists |  -  |
| **500** | Internal error |  -  |

<a id="deleteAccount"></a>
# **deleteAccount**
> deleteAccount(accountname)

Delete the specified account, only allowed if the account is in the disabled state. All users will be deleted along with the account and all resources will be garbage collected

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    UserManagementApi apiInstance = new UserManagementApi(defaultClient);
    String accountname = "accountname_example"; // String | 
    try {
      apiInstance.deleteAccount(accountname);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserManagementApi#deleteAccount");
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
| **accountname** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful deletion |  -  |
| **500** | Internal error |  -  |

<a id="deleteUser"></a>
# **deleteUser**
> deleteUser(accountname, username)

Delete a specific user credential by username of the credential. Cannot be the credential used to authenticate the request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    UserManagementApi apiInstance = new UserManagementApi(defaultClient);
    String accountname = "accountname_example"; // String | 
    String username = "username_example"; // String | 
    try {
      apiInstance.deleteUser(accountname, username);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserManagementApi#deleteUser");
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
| **accountname** | **String**|  | |
| **username** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Deleted credential |  -  |
| **500** | Internal error |  -  |

<a id="deleteUserCredential"></a>
# **deleteUserCredential**
> deleteUserCredential(accountname, username, credentialType)

Delete a credential by type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    UserManagementApi apiInstance = new UserManagementApi(defaultClient);
    String accountname = "accountname_example"; // String | 
    String username = "username_example"; // String | 
    String credentialType = "password"; // String | 
    try {
      apiInstance.deleteUserCredential(accountname, username, credentialType);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserManagementApi#deleteUserCredential");
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
| **accountname** | **String**|  | |
| **username** | **String**|  | |
| **credentialType** | **String**|  | [enum: password] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful deletion |  -  |
| **400** | Conflict, cannot delete the credential used to authenticate this request |  -  |
| **500** | Internal error |  -  |

<a id="getAccount"></a>
# **getAccount**
> Account getAccount(accountname)

Get info about an user. Only available to admin user. Uses the main user Id, not a username.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    UserManagementApi apiInstance = new UserManagementApi(defaultClient);
    String accountname = "accountname_example"; // String | 
    try {
      Account result = apiInstance.getAccount(accountname);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserManagementApi#getAccount");
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
| **accountname** | **String**|  | |

### Return type

[**Account**](Account.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get user information |  -  |
| **500** | Internal error |  -  |

<a id="getAccountUser"></a>
# **getAccountUser**
> User getAccountUser(accountname, username)

Get a specific user in the specified account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    UserManagementApi apiInstance = new UserManagementApi(defaultClient);
    String accountname = "accountname_example"; // String | 
    String username = "username_example"; // String | 
    try {
      User result = apiInstance.getAccountUser(accountname, username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserManagementApi#getAccountUser");
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
| **accountname** | **String**|  | |
| **username** | **String**|  | |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User record |  -  |
| **500** | Internal error |  -  |

<a id="listAccounts"></a>
# **listAccounts**
> List&lt;Account&gt; listAccounts(state)

List user summaries. Only available to the system admin user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    UserManagementApi apiInstance = new UserManagementApi(defaultClient);
    String state = "enabled"; // String | Filter accounts by state
    try {
      List<Account> result = apiInstance.listAccounts(state);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserManagementApi#listAccounts");
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
| **state** | **String**| Filter accounts by state | [optional] [enum: enabled, disabled, deleting] |

### Return type

[**List&lt;Account&gt;**](Account.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Accound summary listing |  -  |
| **500** | Internal error |  -  |

<a id="listUserCredentials"></a>
# **listUserCredentials**
> List&lt;AccessCredential&gt; listUserCredentials(accountname, username)

Get current credential summary

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    UserManagementApi apiInstance = new UserManagementApi(defaultClient);
    String accountname = "accountname_example"; // String | 
    String username = "username_example"; // String | 
    try {
      List<AccessCredential> result = apiInstance.listUserCredentials(accountname, username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserManagementApi#listUserCredentials");
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
| **accountname** | **String**|  | |
| **username** | **String**|  | |

### Return type

[**List&lt;AccessCredential&gt;**](AccessCredential.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User credential listing |  -  |
| **500** | Internal error |  -  |

<a id="listUsers"></a>
# **listUsers**
> List&lt;User&gt; listUsers(accountname)

List accounts for the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    UserManagementApi apiInstance = new UserManagementApi(defaultClient);
    String accountname = "accountname_example"; // String | 
    try {
      List<User> result = apiInstance.listUsers(accountname);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserManagementApi#listUsers");
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
| **accountname** | **String**|  | |

### Return type

[**List&lt;User&gt;**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | User listing |  -  |
| **500** | Internal error |  -  |

<a id="updateAccountState"></a>
# **updateAccountState**
> AccountStatus updateAccountState(accountname, accountStatus)

Update the state of an account to either enabled or disabled. For deletion use the DELETE route

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    UserManagementApi apiInstance = new UserManagementApi(defaultClient);
    String accountname = "accountname_example"; // String | 
    AccountStatus accountStatus = new AccountStatus(); // AccountStatus | 
    try {
      AccountStatus result = apiInstance.updateAccountState(accountname, accountStatus);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserManagementApi#updateAccountState");
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
| **accountname** | **String**|  | |
| **accountStatus** | [**AccountStatus**](AccountStatus.md)|  | |

### Return type

[**AccountStatus**](AccountStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Updated state of the account |  -  |
| **400** | State requested is invalid based on current state of the account |  -  |
| **500** | Internal error |  -  |

