# AccountApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountstatements**](AccountApi.md#accountstatements) | **GET** /api/creditcontrol/accounts/{creditAccountId}/statements | Account statements |
| [**addanaccountHolder**](AccountApi.md#addanaccountHolder) | **POST** /api/creditcontrol/accounts/{creditAccountId}/holders | Add an account Holder |
| [**cancelaPreAuthorization**](AccountApi.md#cancelaPreAuthorization) | **DELETE** /api/creditcontrol/accounts/{creditAccountId}/transactions/{transactionId} | Cancel a Pre Authorization |
| [**changecreditlimitofanAccount**](AccountApi.md#changecreditlimitofanAccount) | **PUT** /api/creditcontrol/accounts/{creditAccountId}/creditlimit | Change credit limit of an Account |
| [**changetoleranceofanaccount**](AccountApi.md#changetoleranceofanaccount) | **PUT** /api/creditcontrol/accounts/{creditAccountId}/tolerance | Change tolerance of an account |
| [**closeanAccount**](AccountApi.md#closeanAccount) | **DELETE** /api/creditcontrol/accounts/{creditAccountId} | Close an Account |
| [**createaPreAuthorization**](AccountApi.md#createaPreAuthorization) | **POST** /api/creditcontrol/accounts/{creditAccountId}/transaction | Create a Pre Authorization |
| [**createaPreAuthorizationUsingid**](AccountApi.md#createaPreAuthorizationUsingid) | **PUT** /api/creditcontrol/accounts/{creditAccountId}/transactions/{transactionId} | Create a Pre Authorization (using id) |
| [**createorUpdateSettlement**](AccountApi.md#createorUpdateSettlement) | **PUT** /api/creditcontrol/accounts/{creditAccountId}/transactions/{transactionId}/settlement | Create or Update Settlement |
| [**decreasebalanceofanaccount**](AccountApi.md#decreasebalanceofanaccount) | **PUT** /api/creditcontrol/accounts/{creditAccountId}/statements/{statementId} | Decrease balance of an account |
| [**deleteanaccountholder**](AccountApi.md#deleteanaccountholder) | **DELETE** /api/creditcontrol/accounts/{creditAccountId}/holders/{holderId} | Delete an account holder |
| [**openanAccount**](AccountApi.md#openanAccount) | **POST** /api/creditcontrol/accounts | Open an Account |
| [**openorChangeAccount**](AccountApi.md#openorChangeAccount) | **PUT** /api/creditcontrol/accounts/{accountId} | Open or Change Account |
| [**partialorTotalRefundaSettlement**](AccountApi.md#partialorTotalRefundaSettlement) | **POST** /api/creditcontrol/accounts/{creditAccountId}/transactions/{transactionId}/refunds | Partial or Total Refund a Settlement |
| [**retrieveaAccountbyId**](AccountApi.md#retrieveaAccountbyId) | **GET** /api/creditcontrol/accounts/{creditAccountId} | Retrieve an Account by Id |
| [**searchallaccounts**](AccountApi.md#searchallaccounts) | **GET** /api/creditcontrol/accounts | Search all accounts |
| [**updateemailanddescriptionofaaccount**](AccountApi.md#updateemailanddescriptionofaaccount) | **PUT** /api/creditcontrol/accounts/{creditAccountId} | Update email and description of a account |


<a id="accountstatements"></a>
# **accountstatements**
> Statements1 accountstatements(contentType, accept, creditAccountId)

Account statements

Get the account statements.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String creditAccountId = "insert identifier here"; // String | 
    try {
      Statements1 result = apiInstance.accountstatements(contentType, accept, creditAccountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#accountstatements");
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
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **creditAccountId** | **String**|  | [default to insert identifier here] |

### Return type

[**Statements1**](Statements1.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * Server -  <br>  * Vary -  <br>  * X-CDNIgnore -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-Translate -  <br>  * X-Translate-BackEnd -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  |

<a id="addanaccountHolder"></a>
# **addanaccountHolder**
> Searchcheckingaccounts1 addanaccountHolder(creditAccountId, accept, contentType, addanaccountHolderRequest1)

Add an account Holder



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String creditAccountId = "insert identifier here"; // String | Credit account's identification
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    AddanaccountHolderRequest1 addanaccountHolderRequest1 = new AddanaccountHolderRequest1(); // AddanaccountHolderRequest1 | 
    try {
      Searchcheckingaccounts1 result = apiInstance.addanaccountHolder(creditAccountId, accept, contentType, addanaccountHolderRequest1);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#addanaccountHolder");
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
| **creditAccountId** | **String**| Credit account&#39;s identification | [default to insert identifier here] |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **addanaccountHolderRequest1** | [**AddanaccountHolderRequest1**](AddanaccountHolderRequest1.md)|  | |

### Return type

[**Searchcheckingaccounts1**](Searchcheckingaccounts1.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Connection -  <br>  * Content-Length -  <br>  * Date -  <br>  * Server -  <br>  * X-CDNIgnore -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-Translate -  <br>  * X-Translate-BackEnd -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  |

<a id="cancelaPreAuthorization"></a>
# **cancelaPreAuthorization**
> cancelaPreAuthorization(contentType, accept, creditAccountId, transactionId)

Cancel a Pre Authorization



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String creditAccountId = "insert identifier here"; // String | Credit account's identification
    String transactionId = "insert identifier here"; // String | 
    try {
      apiInstance.cancelaPreAuthorization(contentType, accept, creditAccountId, transactionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#cancelaPreAuthorization");
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
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **creditAccountId** | **String**| Credit account&#39;s identification | [default to insert identifier here] |
| **transactionId** | **String**|  | [default to insert identifier here] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="changecreditlimitofanAccount"></a>
# **changecreditlimitofanAccount**
> Object changecreditlimitofanAccount(creditAccountId, accept, contentType, changecreditlimitofanAccountRequest1)

Change credit limit of an Account

Increase the credit limit of an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String creditAccountId = "insert identifier here"; // String | Credit account's identifier
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    ChangecreditlimitofanAccountRequest1 changecreditlimitofanAccountRequest1 = new ChangecreditlimitofanAccountRequest1(); // ChangecreditlimitofanAccountRequest1 | 
    try {
      Object result = apiInstance.changecreditlimitofanAccount(creditAccountId, accept, contentType, changecreditlimitofanAccountRequest1);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#changecreditlimitofanAccount");
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
| **creditAccountId** | **String**| Credit account&#39;s identifier | [default to insert identifier here] |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **changecreditlimitofanAccountRequest1** | [**ChangecreditlimitofanAccountRequest1**](ChangecreditlimitofanAccountRequest1.md)|  | |

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * connection -  <br>  * content-length -  <br>  * date -  <br>  * server -  <br>  * via -  <br>  * x-cache -  <br>  * x-cache-lookup -  <br>  * x-powered-by -  <br>  * x-vtex-janus-router-backend-app -  <br>  |

<a id="changetoleranceofanaccount"></a>
# **changetoleranceofanaccount**
> Object changetoleranceofanaccount(creditAccountId, accept, contentType, changetoleranceofanaccountRequest1)

Change tolerance of an account

Increase the credit limit of a checking account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String creditAccountId = "insert identifier here"; // String | Credit account's identification
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    ChangetoleranceofanaccountRequest1 changetoleranceofanaccountRequest1 = new ChangetoleranceofanaccountRequest1(); // ChangetoleranceofanaccountRequest1 | 
    try {
      Object result = apiInstance.changetoleranceofanaccount(creditAccountId, accept, contentType, changetoleranceofanaccountRequest1);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#changetoleranceofanaccount");
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
| **creditAccountId** | **String**| Credit account&#39;s identification | [default to insert identifier here] |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **changetoleranceofanaccountRequest1** | [**ChangetoleranceofanaccountRequest1**](ChangetoleranceofanaccountRequest1.md)|  | |

### Return type

**Object**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * connection -  <br>  * content-length -  <br>  * date -  <br>  * server -  <br>  * via -  <br>  * x-cache -  <br>  * x-cache-lookup -  <br>  * x-powered-by -  <br>  * x-vtex-janus-router-backend-app -  <br>  |

<a id="closeanAccount"></a>
# **closeanAccount**
> closeanAccount(creditAccountId, accept, contentType, closeanAccountRequest1)

Close an Account

Closes an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String creditAccountId = "insert identifier here"; // String | Credit account's identifier
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    CloseanAccountRequest1 closeanAccountRequest1 = new CloseanAccountRequest1(); // CloseanAccountRequest1 | 
    try {
      apiInstance.closeanAccount(creditAccountId, accept, contentType, closeanAccountRequest1);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#closeanAccount");
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
| **creditAccountId** | **String**| Credit account&#39;s identifier | [default to insert identifier here] |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **closeanAccountRequest1** | [**CloseanAccountRequest1**](CloseanAccountRequest1.md)|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="createaPreAuthorization"></a>
# **createaPreAuthorization**
> createaPreAuthorization(creditAccountId, accept, contentType, createaPreAuthorizationRequest1)

Create a Pre Authorization



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String creditAccountId = "insert identifier here"; // String | Credit account's identification
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    CreateaPreAuthorizationRequest1 createaPreAuthorizationRequest1 = new CreateaPreAuthorizationRequest1(); // CreateaPreAuthorizationRequest1 | 
    try {
      apiInstance.createaPreAuthorization(creditAccountId, accept, contentType, createaPreAuthorizationRequest1);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#createaPreAuthorization");
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
| **creditAccountId** | **String**| Credit account&#39;s identification | [default to insert identifier here] |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **createaPreAuthorizationRequest1** | [**CreateaPreAuthorizationRequest1**](CreateaPreAuthorizationRequest1.md)|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="createaPreAuthorizationUsingid"></a>
# **createaPreAuthorizationUsingid**
> createaPreAuthorizationUsingid(creditAccountId, transactionId, accept, contentType, createaPreAuthorizationUsingidRequest)

Create a Pre Authorization (using id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String creditAccountId = "insert identifier here"; // String | Credit account's identification
    String transactionId = "insert identifier here"; // String | 
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    CreateaPreAuthorizationUsingidRequest createaPreAuthorizationUsingidRequest = new CreateaPreAuthorizationUsingidRequest(); // CreateaPreAuthorizationUsingidRequest | 
    try {
      apiInstance.createaPreAuthorizationUsingid(creditAccountId, transactionId, accept, contentType, createaPreAuthorizationUsingidRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#createaPreAuthorizationUsingid");
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
| **creditAccountId** | **String**| Credit account&#39;s identification | [default to insert identifier here] |
| **transactionId** | **String**|  | [default to insert identifier here] |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **createaPreAuthorizationUsingidRequest** | [**CreateaPreAuthorizationUsingidRequest**](CreateaPreAuthorizationUsingidRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="createorUpdateSettlement"></a>
# **createorUpdateSettlement**
> ThisoperationcausesthecreationofNinvoicesWhereNisthenumberofinstallmentsThefirstinvoicewillhaveaduedatewith30daysandthenextinvoiceswillhaveaduedate30daysawayfrompreviousinvoice createorUpdateSettlement(creditAccountId, transactionId, accept, contentType, createorUpdateSettlementRequest1)

Create or Update Settlement

Debit a value from checking account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String creditAccountId = "insert identifier here"; // String | Credit account's identification
    String transactionId = "insert identifier here"; // String | 
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    CreateorUpdateSettlementRequest1 createorUpdateSettlementRequest1 = new CreateorUpdateSettlementRequest1(); // CreateorUpdateSettlementRequest1 | 
    try {
      ThisoperationcausesthecreationofNinvoicesWhereNisthenumberofinstallmentsThefirstinvoicewillhaveaduedatewith30daysandthenextinvoiceswillhaveaduedate30daysawayfrompreviousinvoice result = apiInstance.createorUpdateSettlement(creditAccountId, transactionId, accept, contentType, createorUpdateSettlementRequest1);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#createorUpdateSettlement");
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
| **creditAccountId** | **String**| Credit account&#39;s identification | [default to insert identifier here] |
| **transactionId** | **String**|  | [default to insert identifier here] |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **createorUpdateSettlementRequest1** | [**CreateorUpdateSettlementRequest1**](CreateorUpdateSettlementRequest1.md)|  | |

### Return type

[**ThisoperationcausesthecreationofNinvoicesWhereNisthenumberofinstallmentsThefirstinvoicewillhaveaduedatewith30daysandthenextinvoiceswillhaveaduedate30daysawayfrompreviousinvoice**](ThisoperationcausesthecreationofNinvoicesWhereNisthenumberofinstallmentsThefirstinvoicewillhaveaduedatewith30daysandthenextinvoiceswillhaveaduedate30daysawayfrompreviousinvoice.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * connection -  <br>  * content-length -  <br>  * content-type -  <br>  * date -  <br>  * server -  <br>  * x-powered-by -  <br>  * x-vtex-janus-router-backend-app -  <br>  |

<a id="decreasebalanceofanaccount"></a>
# **decreasebalanceofanaccount**
> decreasebalanceofanaccount(creditAccountId, statementId, accept, contentType, decreasebalanceofanaccountRequest1)

Decrease balance of an account

Create a debit value updating the account BALANCE.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String creditAccountId = "insert example here"; // String | Credit account's identification
    String statementId = "insert example here"; // String | 
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    DecreasebalanceofanaccountRequest1 decreasebalanceofanaccountRequest1 = new DecreasebalanceofanaccountRequest1(); // DecreasebalanceofanaccountRequest1 | 
    try {
      apiInstance.decreasebalanceofanaccount(creditAccountId, statementId, accept, contentType, decreasebalanceofanaccountRequest1);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#decreasebalanceofanaccount");
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
| **creditAccountId** | **String**| Credit account&#39;s identification | [default to insert example here] |
| **statementId** | **String**|  | [default to insert example here] |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **decreasebalanceofanaccountRequest1** | [**DecreasebalanceofanaccountRequest1**](DecreasebalanceofanaccountRequest1.md)|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="deleteanaccountholder"></a>
# **deleteanaccountholder**
> Searchcheckingaccounts1 deleteanaccountholder(contentType, accept, creditAccountId, holderId)

Delete an account holder



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String creditAccountId = "insert identifier here"; // String | Credit account's identification
    String holderId = "insert identifier here"; // String | 
    try {
      Searchcheckingaccounts1 result = apiInstance.deleteanaccountholder(contentType, accept, creditAccountId, holderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#deleteanaccountholder");
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
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **creditAccountId** | **String**| Credit account&#39;s identification | [default to insert identifier here] |
| **holderId** | **String**|  | [default to insert identifier here] |

### Return type

[**Searchcheckingaccounts1**](Searchcheckingaccounts1.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Connection -  <br>  * Content-Length -  <br>  * Date -  <br>  * Server -  <br>  * X-CDNIgnore -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-Translate -  <br>  * X-Translate-BackEnd -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  |

<a id="openanAccount"></a>
# **openanAccount**
> String openanAccount(accept, contentType, openanAccountRequest1)

Open an Account

Open an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    OpenanAccountRequest1 openanAccountRequest1 = new OpenanAccountRequest1(); // OpenanAccountRequest1 | 
    try {
      String result = apiInstance.openanAccount(accept, contentType, openanAccountRequest1);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#openanAccount");
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
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **openanAccountRequest1** | [**OpenanAccountRequest1**](OpenanAccountRequest1.md)|  | |

### Return type

**String**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Connection -  <br>  * Content-Length -  <br>  * Date -  <br>  * Server -  <br>  * X-CDNIgnore -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-Translate -  <br>  * X-Translate-BackEnd -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  |

<a id="openorChangeAccount"></a>
# **openorChangeAccount**
> String openorChangeAccount(accountId, accept, contentType, openorChangeAccountRequest1)

Open or Change Account

Open or Change an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String accountId = "insert identifier here"; // String | It must be an alphanumeric value
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    OpenorChangeAccountRequest1 openorChangeAccountRequest1 = new OpenorChangeAccountRequest1(); // OpenorChangeAccountRequest1 | 
    try {
      String result = apiInstance.openorChangeAccount(accountId, accept, contentType, openorChangeAccountRequest1);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#openorChangeAccount");
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
| **accountId** | **String**| It must be an alphanumeric value | [default to insert identifier here] |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **openorChangeAccountRequest1** | [**OpenorChangeAccountRequest1**](OpenorChangeAccountRequest1.md)|  | [optional] |

### Return type

**String**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Connection -  <br>  * Content-Length -  <br>  * Date -  <br>  * Server -  <br>  * X-CDNIgnore -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-Translate -  <br>  * X-Translate-BackEnd -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  |

<a id="partialorTotalRefundaSettlement"></a>
# **partialorTotalRefundaSettlement**
> ThisoperationcausesthecreationofNinvoicesWhereNisthenumberofinstallmentsThefirstinvoicewillhaveaduedatewith30daysandthenextinvoiceswillhaveaduedate30daysawayfrompreviousinvoice partialorTotalRefundaSettlement(creditAccountId, transactionId, accept, contentType, partialorTotalRefundaSettlementRequest1)

Partial or Total Refund a Settlement

Refund a value from a already settled transaction.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String creditAccountId = "insert identifier here"; // String | Credit account's identification
    String transactionId = "insert identifier here"; // String | 
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    PartialorTotalRefundaSettlementRequest1 partialorTotalRefundaSettlementRequest1 = new PartialorTotalRefundaSettlementRequest1(); // PartialorTotalRefundaSettlementRequest1 | 
    try {
      ThisoperationcausesthecreationofNinvoicesWhereNisthenumberofinstallmentsThefirstinvoicewillhaveaduedatewith30daysandthenextinvoiceswillhaveaduedate30daysawayfrompreviousinvoice result = apiInstance.partialorTotalRefundaSettlement(creditAccountId, transactionId, accept, contentType, partialorTotalRefundaSettlementRequest1);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#partialorTotalRefundaSettlement");
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
| **creditAccountId** | **String**| Credit account&#39;s identification | [default to insert identifier here] |
| **transactionId** | **String**|  | [default to insert identifier here] |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **partialorTotalRefundaSettlementRequest1** | [**PartialorTotalRefundaSettlementRequest1**](PartialorTotalRefundaSettlementRequest1.md)|  | |

### Return type

[**ThisoperationcausesthecreationofNinvoicesWhereNisthenumberofinstallmentsThefirstinvoicewillhaveaduedatewith30daysandthenextinvoiceswillhaveaduedate30daysawayfrompreviousinvoice**](ThisoperationcausesthecreationofNinvoicesWhereNisthenumberofinstallmentsThefirstinvoicewillhaveaduedatewith30daysandthenextinvoiceswillhaveaduedate30daysawayfrompreviousinvoice.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * connection -  <br>  * content-length -  <br>  * content-type -  <br>  * date -  <br>  * server -  <br>  * x-powered-by -  <br>  * x-vtex-janus-router-backend-app -  <br>  |

<a id="retrieveaAccountbyId"></a>
# **retrieveaAccountbyId**
> Getaccount1 retrieveaAccountbyId(contentType, accept, creditAccountId)

Retrieve an Account by Id

Retrieve an account by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String creditAccountId = "insert identifier here"; // String | 
    try {
      Getaccount1 result = apiInstance.retrieveaAccountbyId(contentType, accept, creditAccountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#retrieveaAccountbyId");
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
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **creditAccountId** | **String**|  | [default to insert identifier here] |

### Return type

[**Getaccount1**](Getaccount1.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Connection -  <br>  * Content-Length -  <br>  * Date -  <br>  * Server -  <br>  * X-CDNIgnore -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  |

<a id="searchallaccounts"></a>
# **searchallaccounts**
> Searchaccounts1 searchallaccounts(contentType, accept)

Search all accounts



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    try {
      Searchaccounts1 result = apiInstance.searchallaccounts(contentType, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#searchallaccounts");
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
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |

### Return type

[**Searchaccounts1**](Searchaccounts1.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Connection -  <br>  * Content-Length -  <br>  * Date -  <br>  * Server -  <br>  * X-CDNIgnore -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-Translate -  <br>  * X-Translate-BackEnd -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  |

<a id="updateemailanddescriptionofaaccount"></a>
# **updateemailanddescriptionofaaccount**
> String updateemailanddescriptionofaaccount(creditAccountId, accept, contentType, updateemailanddescriptionofaaccountRequest1)

Update email and description of a account

Update a checking account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String creditAccountId = "insert identifier here"; // String | Credit account's identification
    String accept = "application/json"; // String | Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json
    String contentType = "application/json"; // String | The Media type of the body of the request. Default value for payment provider protocol is application/json
    UpdateemailanddescriptionofaaccountRequest1 updateemailanddescriptionofaaccountRequest1 = new UpdateemailanddescriptionofaaccountRequest1(); // UpdateemailanddescriptionofaaccountRequest1 | 
    try {
      String result = apiInstance.updateemailanddescriptionofaaccount(creditAccountId, accept, contentType, updateemailanddescriptionofaaccountRequest1);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#updateemailanddescriptionofaaccount");
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
| **creditAccountId** | **String**| Credit account&#39;s identification | [default to insert identifier here] |
| **accept** | **String**| Media type(s) that is/are acceptable for the response. Default value for payment provider protocol is application/json | [default to application/json] |
| **contentType** | **String**| The Media type of the body of the request. Default value for payment provider protocol is application/json | [default to application/json] |
| **updateemailanddescriptionofaaccountRequest1** | [**UpdateemailanddescriptionofaaccountRequest1**](UpdateemailanddescriptionofaaccountRequest1.md)|  | |

### Return type

**String**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  * Connection -  <br>  * Content-Length -  <br>  * Date -  <br>  * Server -  <br>  * X-CDNIgnore -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Track -  <br>  * X-Translate -  <br>  * X-Translate-BackEnd -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  |

