# AccountsApi

All URIs are relative to *https://api.pocketsmith.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountsIdDelete**](AccountsApi.md#accountsIdDelete) | **DELETE** /accounts/{id} | Delete account |
| [**accountsIdGet**](AccountsApi.md#accountsIdGet) | **GET** /accounts/{id} | Get account |
| [**accountsIdPut**](AccountsApi.md#accountsIdPut) | **PUT** /accounts/{id} | Update account |
| [**institutionsIdAccountsGet**](AccountsApi.md#institutionsIdAccountsGet) | **GET** /institutions/{id}/accounts | List accounts in institution |
| [**usersIdAccountsGet**](AccountsApi.md#usersIdAccountsGet) | **GET** /users/{id}/accounts | List accounts in user |
| [**usersIdAccountsPost**](AccountsApi.md#usersIdAccountsPost) | **POST** /users/{id}/accounts | Create an account in user |
| [**usersIdAccountsPut**](AccountsApi.md#usersIdAccountsPut) | **PUT** /users/{id}/accounts | Update the display order of accounts in user |


<a id="accountsIdDelete"></a>
# **accountsIdDelete**
> accountsIdDelete(id)

Delete account

Deletes an account and all its data by ID, optionally merge scenarios into another account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the account.
    try {
      apiInstance.accountsIdDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsIdDelete");
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
| **id** | **Integer**| The unique identifier of the account. | |

### Return type

null (empty response body)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |
| **422** | Validation Error |  -  |

<a id="accountsIdGet"></a>
# **accountsIdGet**
> Account accountsIdGet(id)

Get account

Gets an account by its ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the account.
    try {
      Account result = apiInstance.accountsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsIdGet");
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
| **id** | **Integer**| The unique identifier of the account. | |

### Return type

[**Account**](Account.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |

<a id="accountsIdPut"></a>
# **accountsIdPut**
> Account accountsIdPut(id, accountsIdPutRequest)

Update account

Updates and returns an account by its ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the account.
    AccountsIdPutRequest accountsIdPutRequest = new AccountsIdPutRequest(); // AccountsIdPutRequest | 
    try {
      Account result = apiInstance.accountsIdPut(id, accountsIdPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#accountsIdPut");
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
| **id** | **Integer**| The unique identifier of the account. | |
| **accountsIdPutRequest** | [**AccountsIdPutRequest**](AccountsIdPutRequest.md)|  | [optional] |

### Return type

[**Account**](Account.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |
| **422** | Validation Error |  -  |

<a id="institutionsIdAccountsGet"></a>
# **institutionsIdAccountsGet**
> List&lt;Account&gt; institutionsIdAccountsGet(id)

List accounts in institution

Lists accounts belonging to an institution by its ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the institution.
    try {
      List<Account> result = apiInstance.institutionsIdAccountsGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#institutionsIdAccountsGet");
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
| **id** | **Integer**| The unique identifier of the institution. | |

### Return type

[**List&lt;Account&gt;**](Account.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |

<a id="usersIdAccountsGet"></a>
# **usersIdAccountsGet**
> List&lt;Account&gt; usersIdAccountsGet(id)

List accounts in user

Lists all accounts belonging to the user by their ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the user.
    try {
      List<Account> result = apiInstance.usersIdAccountsGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#usersIdAccountsGet");
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
| **id** | **Integer**| The unique identifier of the user. | |

### Return type

[**List&lt;Account&gt;**](Account.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |

<a id="usersIdAccountsPost"></a>
# **usersIdAccountsPost**
> Account usersIdAccountsPost(id, usersIdAccountsPostRequest)

Create an account in user

Creates and returns an account belonging to the user by their ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the user.
    UsersIdAccountsPostRequest usersIdAccountsPostRequest = new UsersIdAccountsPostRequest(); // UsersIdAccountsPostRequest | 
    try {
      Account result = apiInstance.usersIdAccountsPost(id, usersIdAccountsPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#usersIdAccountsPost");
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
| **id** | **Integer**| The unique identifier of the user. | |
| **usersIdAccountsPostRequest** | [**UsersIdAccountsPostRequest**](UsersIdAccountsPostRequest.md)|  | [optional] |

### Return type

[**Account**](Account.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |
| **422** | Validation Error |  -  |

<a id="usersIdAccountsPut"></a>
# **usersIdAccountsPut**
> List&lt;Account&gt; usersIdAccountsPut(id, usersIdAccountsPutRequest)

Update the display order of accounts in user

Updates the display order of accounts belonging to the user, by accepting an array of accounts in their new display order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the user.
    UsersIdAccountsPutRequest usersIdAccountsPutRequest = new UsersIdAccountsPutRequest(); // UsersIdAccountsPutRequest | 
    try {
      List<Account> result = apiInstance.usersIdAccountsPut(id, usersIdAccountsPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#usersIdAccountsPut");
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
| **id** | **Integer**| The unique identifier of the user. | |
| **usersIdAccountsPutRequest** | [**UsersIdAccountsPutRequest**](UsersIdAccountsPutRequest.md)|  | [optional] |

### Return type

[**List&lt;Account&gt;**](Account.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |

