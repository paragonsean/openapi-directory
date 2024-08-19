# UserAccountsFindAndModifyUserAccountsApi

All URIs are relative to *https://market.openchannel.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**userAccountsGet**](UserAccountsFindAndModifyUserAccountsApi.md#userAccountsGet) | **GET** /userAccounts | Returns a paginated list of userAccounts |
| [**userAccountsUserAccountIdDelete**](UserAccountsFindAndModifyUserAccountsApi.md#userAccountsUserAccountIdDelete) | **DELETE** /userAccounts/{userAccountId} | Removes the user account |
| [**userAccountsUserAccountIdGet**](UserAccountsFindAndModifyUserAccountsApi.md#userAccountsUserAccountIdGet) | **GET** /userAccounts/{userAccountId} | Returns a single user account |
| [**userAccountsUserAccountIdPatch**](UserAccountsFindAndModifyUserAccountsApi.md#userAccountsUserAccountIdPatch) | **PATCH** /userAccounts/{userAccountId} | Updates the user account fields |
| [**userAccountsUserAccountIdPost**](UserAccountsFindAndModifyUserAccountsApi.md#userAccountsUserAccountIdPost) | **POST** /userAccounts/{userAccountId} | Updates the user account or adds the user account if it doesn&#39;t exist |


<a id="userAccountsGet"></a>
# **userAccountsGet**
> UserAccountPages userAccountsGet(query, sort, pageNumber, limit)

Returns a paginated list of userAccounts

- Results are paginated and the default is value is 1000 if no limit is provided 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserAccountsFindAndModifyUserAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    UserAccountsFindAndModifyUserAccountsApi apiInstance = new UserAccountsFindAndModifyUserAccountsApi(defaultClient);
    String query = "query_example"; // String | A query document. Example: {'name':'NASA'} matches all the userAccounts that have the name 'NASA'
    String sort = "sort_example"; // String | A sort document. Example: {'name':1} sorts the results by name in ascending order
    Integer pageNumber = 56; // Integer | The result set page number to be returned
    Integer limit = 56; // Integer | The maximum number of results to return per page
    try {
      UserAccountPages result = apiInstance.userAccountsGet(query, sort, pageNumber, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserAccountsFindAndModifyUserAccountsApi#userAccountsGet");
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
| **query** | **String**| A query document. Example: {&#39;name&#39;:&#39;NASA&#39;} matches all the userAccounts that have the name &#39;NASA&#39; | [optional] |
| **sort** | **String**| A sort document. Example: {&#39;name&#39;:1} sorts the results by name in ascending order | [optional] |
| **pageNumber** | **Integer**| The result set page number to be returned | [optional] |
| **limit** | **Integer**| The maximum number of results to return per page | [optional] |

### Return type

[**UserAccountPages**](UserAccountPages.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **0** | OK |  -  |

<a id="userAccountsUserAccountIdDelete"></a>
# **userAccountsUserAccountIdDelete**
> userAccountsUserAccountIdDelete(userAccountId)

Removes the user account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserAccountsFindAndModifyUserAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    UserAccountsFindAndModifyUserAccountsApi apiInstance = new UserAccountsFindAndModifyUserAccountsApi(defaultClient);
    String userAccountId = "userAccountId_example"; // String | The id of the user account to be removed
    try {
      apiInstance.userAccountsUserAccountIdDelete(userAccountId);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserAccountsFindAndModifyUserAccountsApi#userAccountsUserAccountIdDelete");
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
| **userAccountId** | **String**| The id of the user account to be removed | |

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **0** | OK |  -  |

<a id="userAccountsUserAccountIdGet"></a>
# **userAccountsUserAccountIdGet**
> UserAccount userAccountsUserAccountIdGet(userAccountId)

Returns a single user account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserAccountsFindAndModifyUserAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    UserAccountsFindAndModifyUserAccountsApi apiInstance = new UserAccountsFindAndModifyUserAccountsApi(defaultClient);
    String userAccountId = "userAccountId_example"; // String | The id of the user account to be located
    try {
      UserAccount result = apiInstance.userAccountsUserAccountIdGet(userAccountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserAccountsFindAndModifyUserAccountsApi#userAccountsUserAccountIdGet");
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
| **userAccountId** | **String**| The id of the user account to be located | |

### Return type

[**UserAccount**](UserAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **404** | Not Found - Developer account is not found |  -  |
| **0** | OK |  -  |

<a id="userAccountsUserAccountIdPatch"></a>
# **userAccountsUserAccountIdPatch**
> UserAccount userAccountsUserAccountIdPatch(userAccountId, userId, email, name, customData)

Updates the user account fields

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserAccountsFindAndModifyUserAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    UserAccountsFindAndModifyUserAccountsApi apiInstance = new UserAccountsFindAndModifyUserAccountsApi(defaultClient);
    String userAccountId = "userAccountId_example"; // String | The id of the user account to be updated
    String userId = "userId_example"; // String | The Id of the user that this account belongs to
    String email = "email_example"; // String | The contact email address
    String name = "name_example"; // String | The user account name
    String customData = "customData_example"; // String | A custom JSON object that you can create and attach to this record
    try {
      UserAccount result = apiInstance.userAccountsUserAccountIdPatch(userAccountId, userId, email, name, customData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserAccountsFindAndModifyUserAccountsApi#userAccountsUserAccountIdPatch");
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
| **userAccountId** | **String**| The id of the user account to be updated | |
| **userId** | **String**| The Id of the user that this account belongs to | |
| **email** | **String**| The contact email address | [optional] |
| **name** | **String**| The user account name | [optional] |
| **customData** | **String**| A custom JSON object that you can create and attach to this record | [optional] |

### Return type

[**UserAccount**](UserAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **404** | Not Found - User account is not found |  -  |
| **0** | OK |  -  |

<a id="userAccountsUserAccountIdPost"></a>
# **userAccountsUserAccountIdPost**
> UserAccount userAccountsUserAccountIdPost(userAccountId, userId, email, name, customData)

Updates the user account or adds the user account if it doesn&#39;t exist

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserAccountsFindAndModifyUserAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    UserAccountsFindAndModifyUserAccountsApi apiInstance = new UserAccountsFindAndModifyUserAccountsApi(defaultClient);
    String userAccountId = "userAccountId_example"; // String | The id of the user account to be updated
    String userId = "userId_example"; // String | The Id of the user that this account belongs to
    String email = "email_example"; // String | The contact email address
    String name = "name_example"; // String | The user account name
    String customData = "customData_example"; // String | A custom JSON object that you can create and attach to this record
    try {
      UserAccount result = apiInstance.userAccountsUserAccountIdPost(userAccountId, userId, email, name, customData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserAccountsFindAndModifyUserAccountsApi#userAccountsUserAccountIdPost");
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
| **userAccountId** | **String**| The id of the user account to be updated | |
| **userId** | **String**| The Id of the user that this account belongs to | |
| **email** | **String**| The contact email address | [optional] |
| **name** | **String**| The user account name | [optional] |
| **customData** | **String**| A custom JSON object that you can create and attach to this record | [optional] |

### Return type

[**UserAccount**](UserAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **0** | OK |  -  |

