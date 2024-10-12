# AccountPortfolioApi

All URIs are relative to *https://www.interactivebrokers.com/tradingapi/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountsAccountPositionsGet**](AccountPortfolioApi.md#accountsAccountPositionsGet) | **GET** /accounts/{account}/positions | Account Positions |
| [**accountsAccountSummaryGet**](AccountPortfolioApi.md#accountsAccountSummaryGet) | **GET** /accounts/{account}/summary | Account Values Summary |
| [**accountsGet**](AccountPortfolioApi.md#accountsGet) | **GET** /accounts | Brokerage Accounts |


<a id="accountsAccountPositionsGet"></a>
# **accountsAccountPositionsGet**
> List&lt;AccountsAccountPositionsGet200ResponseInner&gt; accountsAccountPositionsGet(account)

Account Positions

Returns a list of positions for the indicated account. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountPortfolioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.interactivebrokers.com/tradingapi/v1");
    
    // Configure API key authorization: cookieAuth
    ApiKeyAuth cookieAuth = (ApiKeyAuth) defaultClient.getAuthentication("cookieAuth");
    cookieAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cookieAuth.setApiKeyPrefix("Token");

    AccountPortfolioApi apiInstance = new AccountPortfolioApi(defaultClient);
    String account = "account_example"; // String | Account Number
    try {
      List<AccountsAccountPositionsGet200ResponseInner> result = apiInstance.accountsAccountPositionsGet(account);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountPortfolioApi#accountsAccountPositionsGet");
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
| **account** | **String**| Account Number | |

### Return type

[**List&lt;AccountsAccountPositionsGet200ResponseInner&gt;**](AccountsAccountPositionsGet200ResponseInner.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a list of positions for the indicated account |  -  |
| **202** | Unsuccessfull response |  -  |
| **204** | Unsuccessfull response |  -  |
| **400** | Unsuccessfull response |  -  |
| **401** | Unsuccessfull response |  -  |
| **403** | Unsuccessfull response |  -  |
| **408** | Unsuccessfull response |  -  |

<a id="accountsAccountSummaryGet"></a>
# **accountsAccountSummaryGet**
> AccountsAccountSummaryGet200Response accountsAccountSummaryGet(account)

Account Values Summary

Returns a list of account and margin balances associated with the account passed in the URL

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountPortfolioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.interactivebrokers.com/tradingapi/v1");
    
    // Configure API key authorization: cookieAuth
    ApiKeyAuth cookieAuth = (ApiKeyAuth) defaultClient.getAuthentication("cookieAuth");
    cookieAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cookieAuth.setApiKeyPrefix("Token");

    AccountPortfolioApi apiInstance = new AccountPortfolioApi(defaultClient);
    String account = "account_example"; // String | Account Number
    try {
      AccountsAccountSummaryGet200Response result = apiInstance.accountsAccountSummaryGet(account);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountPortfolioApi#accountsAccountSummaryGet");
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
| **account** | **String**| Account Number | |

### Return type

[**AccountsAccountSummaryGet200Response**](AccountsAccountSummaryGet200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns object for account summary with multiple properties.  A property is sufficed with -c if it provides commodity value, -s if it provides security value, and -c if its UKL segment value.  \&quot;These values correspond to the TWS Account Window: https://www.interactivebrokers.com/en/software/tws/usersguidebook/realtimeactivitymonitoring/account_window.htm\&quot;  |  -  |
| **202** | Unsuccessfull response |  -  |
| **204** | Unsuccessfull response |  -  |
| **400** | Unsuccessfull response |  -  |
| **401** | Unsuccessfull response |  -  |
| **403** | Unsuccessfull response |  -  |
| **408** | Unsuccessfull response |  -  |

<a id="accountsGet"></a>
# **accountsGet**
> AccountsGet200Response accountsGet(account)

Brokerage Accounts

Allows the caller to request a list of accounts associated with the session.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountPortfolioApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.interactivebrokers.com/tradingapi/v1");
    
    // Configure API key authorization: cookieAuth
    ApiKeyAuth cookieAuth = (ApiKeyAuth) defaultClient.getAuthentication("cookieAuth");
    cookieAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cookieAuth.setApiKeyPrefix("Token");

    AccountPortfolioApi apiInstance = new AccountPortfolioApi(defaultClient);
    String account = "account_example"; // String | Account Number
    try {
      AccountsGet200Response result = apiInstance.accountsGet(account);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountPortfolioApi#accountsGet");
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
| **account** | **String**| Account Number | |

### Return type

[**AccountsGet200Response**](AccountsGet200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of accounts |  -  |
| **202** | Unsuccessfull response |  -  |
| **204** | Unsuccessfull response |  -  |
| **401** | Unsuccessfull response |  -  |
| **403** | Unsuccessfull response |  -  |
| **408** | Unsuccessfull response |  -  |

