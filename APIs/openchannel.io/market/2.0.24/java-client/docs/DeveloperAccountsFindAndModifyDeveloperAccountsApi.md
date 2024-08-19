# DeveloperAccountsFindAndModifyDeveloperAccountsApi

All URIs are relative to *https://market.openchannel.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**developerAccountsDeveloperAccountIdDelete**](DeveloperAccountsFindAndModifyDeveloperAccountsApi.md#developerAccountsDeveloperAccountIdDelete) | **DELETE** /developerAccounts/{developerAccountId} | Removes the developer account |
| [**developerAccountsDeveloperAccountIdGet**](DeveloperAccountsFindAndModifyDeveloperAccountsApi.md#developerAccountsDeveloperAccountIdGet) | **GET** /developerAccounts/{developerAccountId} | Returns a single developer account |
| [**developerAccountsDeveloperAccountIdPatch**](DeveloperAccountsFindAndModifyDeveloperAccountsApi.md#developerAccountsDeveloperAccountIdPatch) | **PATCH** /developerAccounts/{developerAccountId} | Updates the developer account fields |
| [**developerAccountsDeveloperAccountIdPost**](DeveloperAccountsFindAndModifyDeveloperAccountsApi.md#developerAccountsDeveloperAccountIdPost) | **POST** /developerAccounts/{developerAccountId} | Updates the developer account or adds the developer account if it doesn&#39;t exist |
| [**developerAccountsGet**](DeveloperAccountsFindAndModifyDeveloperAccountsApi.md#developerAccountsGet) | **GET** /developerAccounts | Returns a paginated list of developerAccounts |


<a id="developerAccountsDeveloperAccountIdDelete"></a>
# **developerAccountsDeveloperAccountIdDelete**
> developerAccountsDeveloperAccountIdDelete(developerAccountId)

Removes the developer account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeveloperAccountsFindAndModifyDeveloperAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DeveloperAccountsFindAndModifyDeveloperAccountsApi apiInstance = new DeveloperAccountsFindAndModifyDeveloperAccountsApi(defaultClient);
    String developerAccountId = "developerAccountId_example"; // String | The id of the developer account to be updated
    try {
      apiInstance.developerAccountsDeveloperAccountIdDelete(developerAccountId);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeveloperAccountsFindAndModifyDeveloperAccountsApi#developerAccountsDeveloperAccountIdDelete");
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
| **developerAccountId** | **String**| The id of the developer account to be updated | |

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

<a id="developerAccountsDeveloperAccountIdGet"></a>
# **developerAccountsDeveloperAccountIdGet**
> DeveloperAccount developerAccountsDeveloperAccountIdGet(developerAccountId)

Returns a single developer account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeveloperAccountsFindAndModifyDeveloperAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DeveloperAccountsFindAndModifyDeveloperAccountsApi apiInstance = new DeveloperAccountsFindAndModifyDeveloperAccountsApi(defaultClient);
    String developerAccountId = "developerAccountId_example"; // String | The id of the developer account to be located
    try {
      DeveloperAccount result = apiInstance.developerAccountsDeveloperAccountIdGet(developerAccountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeveloperAccountsFindAndModifyDeveloperAccountsApi#developerAccountsDeveloperAccountIdGet");
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
| **developerAccountId** | **String**| The id of the developer account to be located | |

### Return type

[**DeveloperAccount**](DeveloperAccount.md)

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

<a id="developerAccountsDeveloperAccountIdPatch"></a>
# **developerAccountsDeveloperAccountIdPatch**
> DeveloperAccount developerAccountsDeveloperAccountIdPatch(developerAccountId, developerId, email, name, customData)

Updates the developer account fields

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeveloperAccountsFindAndModifyDeveloperAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DeveloperAccountsFindAndModifyDeveloperAccountsApi apiInstance = new DeveloperAccountsFindAndModifyDeveloperAccountsApi(defaultClient);
    String developerAccountId = "developerAccountId_example"; // String | The id of the developer account to be updated
    String developerId = "developerId_example"; // String | The id of the developer that this account belongs to
    String email = "email_example"; // String | The contact email address
    String name = "name_example"; // String | The name for the account
    String customData = "customData_example"; // String | A custom JSON object that you can create and attach to this record
    try {
      DeveloperAccount result = apiInstance.developerAccountsDeveloperAccountIdPatch(developerAccountId, developerId, email, name, customData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeveloperAccountsFindAndModifyDeveloperAccountsApi#developerAccountsDeveloperAccountIdPatch");
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
| **developerAccountId** | **String**| The id of the developer account to be updated | |
| **developerId** | **String**| The id of the developer that this account belongs to | |
| **email** | **String**| The contact email address | [optional] |
| **name** | **String**| The name for the account | [optional] |
| **customData** | **String**| A custom JSON object that you can create and attach to this record | [optional] |

### Return type

[**DeveloperAccount**](DeveloperAccount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **400** | Bad Request - Required parameters are missing, malformed or invalid |  -  |
| **404** | Not Found - The developer is not found |  -  |
| **0** | OK |  -  |

<a id="developerAccountsDeveloperAccountIdPost"></a>
# **developerAccountsDeveloperAccountIdPost**
> DeveloperAccount developerAccountsDeveloperAccountIdPost(developerAccountId, developerId, email, name, customData)

Updates the developer account or adds the developer account if it doesn&#39;t exist

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeveloperAccountsFindAndModifyDeveloperAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DeveloperAccountsFindAndModifyDeveloperAccountsApi apiInstance = new DeveloperAccountsFindAndModifyDeveloperAccountsApi(defaultClient);
    String developerAccountId = "developerAccountId_example"; // String | The id of the developer account to be updated
    String developerId = "developerId_example"; // String | The id of the developer that this account belongs to
    String email = "email_example"; // String | The contact email address
    String name = "name_example"; // String | The name for the account
    String customData = "customData_example"; // String | A custom JSON object that you can create and attach to this record
    try {
      DeveloperAccount result = apiInstance.developerAccountsDeveloperAccountIdPost(developerAccountId, developerId, email, name, customData);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeveloperAccountsFindAndModifyDeveloperAccountsApi#developerAccountsDeveloperAccountIdPost");
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
| **developerAccountId** | **String**| The id of the developer account to be updated | |
| **developerId** | **String**| The id of the developer that this account belongs to | |
| **email** | **String**| The contact email address | [optional] |
| **name** | **String**| The name for the account | [optional] |
| **customData** | **String**| A custom JSON object that you can create and attach to this record | [optional] |

### Return type

[**DeveloperAccount**](DeveloperAccount.md)

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

<a id="developerAccountsGet"></a>
# **developerAccountsGet**
> DeveloperAccountPages developerAccountsGet(query, sort, pageNumber, limit)

Returns a paginated list of developerAccounts

- Results are paginated and the default is value is 1000 if no limit is provided 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeveloperAccountsFindAndModifyDeveloperAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://market.openchannel.io/v2");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DeveloperAccountsFindAndModifyDeveloperAccountsApi apiInstance = new DeveloperAccountsFindAndModifyDeveloperAccountsApi(defaultClient);
    String query = "query_example"; // String | A query document. Example: {'name':'NASA'} matches all the developerAccounts that have the name 'NASA'
    String sort = "sort_example"; // String | A sort document. Example: {'name':1} sorts the results by name in ascending order
    Integer pageNumber = 56; // Integer | The result set page number to be returned
    Integer limit = 56; // Integer | The maximum number of results to return per page
    try {
      DeveloperAccountPages result = apiInstance.developerAccountsGet(query, sort, pageNumber, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeveloperAccountsFindAndModifyDeveloperAccountsApi#developerAccountsGet");
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
| **query** | **String**| A query document. Example: {&#39;name&#39;:&#39;NASA&#39;} matches all the developerAccounts that have the name &#39;NASA&#39; | [optional] |
| **sort** | **String**| A sort document. Example: {&#39;name&#39;:1} sorts the results by name in ascending order | [optional] |
| **pageNumber** | **Integer**| The result set page number to be returned | [optional] |
| **limit** | **Integer**| The maximum number of results to return per page | [optional] |

### Return type

[**DeveloperAccountPages**](DeveloperAccountPages.md)

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

