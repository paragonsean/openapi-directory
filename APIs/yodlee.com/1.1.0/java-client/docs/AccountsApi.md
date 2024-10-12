# AccountsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createManualAccount**](AccountsApi.md#createManualAccount) | **POST** /accounts | Add Manual Account |
| [**deleteAccount**](AccountsApi.md#deleteAccount) | **DELETE** /accounts/{accountId} | Delete Account |
| [**evaluateAddress**](AccountsApi.md#evaluateAddress) | **POST** /accounts/evaluateAddress | Evaluate Address |
| [**getAccount**](AccountsApi.md#getAccount) | **GET** /accounts/{accountId} | Get Account Details |
| [**getAllAccounts**](AccountsApi.md#getAllAccounts) | **GET** /accounts | Get Accounts |
| [**getHistoricalBalances**](AccountsApi.md#getHistoricalBalances) | **GET** /accounts/historicalBalances | Get Historical Balances |
| [**updateAccount**](AccountsApi.md#updateAccount) | **PUT** /accounts/{accountId} | Update Account |


<a id="createManualAccount"></a>
# **createManualAccount**
> CreatedAccountResponse createManualAccount(createAccountRequest)

Add Manual Account

The add account service is used to add manual accounts.&lt;br&gt;The response of add account service includes the account name , account number and Yodlee generated account id.&lt;br&gt;All manual accounts added will be included as part of networth calculation by default.&lt;br&gt;Add manual account support is available for bank, card, investment, insurance and loan container only.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; &lt;li&gt;A real estate account addition is only supported for SYSTEM and MANUAL valuation type.&lt;/li&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    CreateAccountRequest createAccountRequest = new CreateAccountRequest(); // CreateAccountRequest | accountParam
    try {
      CreatedAccountResponse result = apiInstance.createManualAccount(createAccountRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#createManualAccount");
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
| **createAccountRequest** | [**CreateAccountRequest**](CreateAccountRequest.md)| accountParam | |

### Return type

[**CreatedAccountResponse**](CreatedAccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Y800 : Invalid value for accountParam&lt;br&gt;Y811 : Real Estate Property value already exists&lt;br&gt;Y862 : The provided address is invalid, or the valuation is not available&lt;br&gt;Y869 : Multiple matches found. Provide the complete address or call the POST /accounts/evaluateAddress API to retrieve the list of matched addresses&lt;br&gt; |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="deleteAccount"></a>
# **deleteAccount**
> deleteAccount(accountId)

Delete Account

The delete account service allows an account to be deleted.&lt;br&gt;This service does not return a response. The HTTP response code is 204 (Success with no content).&lt;br&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    Long accountId = 56L; // Long | accountId
    try {
      apiInstance.deleteAccount(accountId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#deleteAccount");
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
| **accountId** | **Long**| accountId | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | OK |  -  |
| **400** | Y800 : Invalid value for accountId&lt;br&gt;Y807 : Resource not found&lt;br&gt;Y868 : No action is allowed, as the data is being migrated to the Open Banking provider&lt;br&gt; |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="evaluateAddress"></a>
# **evaluateAddress**
> EvaluateAddressResponse evaluateAddress(evaluateAddressRequest)

Evaluate Address

Use this service to validate the address before adding the real estate account.&lt;br&gt;If the address is valid, the service will return the complete address information.&lt;br&gt;The response will contain multiple addresses if the user-provided input matches with multiple entries in the vendor database.&lt;br&gt;In the case of multiple matches, the user can select the appropriate address from the list and then invoke the add account service with the complete address.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt; &lt;li&gt;Yodlee recommends to use this service before adding the real estate account to avoid failures.&lt;/li&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    EvaluateAddressRequest evaluateAddressRequest = new EvaluateAddressRequest(); // EvaluateAddressRequest | addressParam
    try {
      EvaluateAddressResponse result = apiInstance.evaluateAddress(evaluateAddressRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#evaluateAddress");
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
| **evaluateAddressRequest** | [**EvaluateAddressRequest**](EvaluateAddressRequest.md)| addressParam | |

### Return type

[**EvaluateAddressResponse**](EvaluateAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Y806 : Invalid input&lt;br&gt;Y800 : Invalid value for zip&lt;br&gt;Y812 : Required field/value - address missing in the request&lt;br&gt;Y812 : Required field/value - street missing in the request&lt;br&gt;Y812 : Required field/value - state &amp; city / zip missing in the request |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="getAccount"></a>
# **getAccount**
> AccountResponse getAccount(accountId, include)

Get Account Details

The get account details service provides detailed information of an account.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt;&lt;li&gt;fullAccountNumber is deprecated and is replaced with fullAccountNumberList in include parameter and response.&lt;/li&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    Long accountId = 56L; // Long | accountId
    String include = "include_example"; // String | profile, holder, fullAccountNumber, fullAccountNumberList, paymentProfile, autoRefresh<br><b>Note:</b>fullAccountNumber is deprecated and is replaced with fullAccountNumberList in include parameter and response.
    try {
      AccountResponse result = apiInstance.getAccount(accountId, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#getAccount");
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
| **accountId** | **Long**| accountId | |
| **include** | **String**| profile, holder, fullAccountNumber, fullAccountNumberList, paymentProfile, autoRefresh&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt;fullAccountNumber is deprecated and is replaced with fullAccountNumberList in include parameter and response. | [optional] |

### Return type

[**AccountResponse**](AccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="getAllAccounts"></a>
# **getAllAccounts**
> AccountResponse getAllAccounts(accountId, container, include, providerAccountId, requestId, status)

Get Accounts

The get accounts service provides information about accounts added by the user.&lt;br&gt;By default, this service returns information for active and to be closed accounts.&lt;br&gt;If requestId is provided, the accounts that are updated in the context of the requestId will be provided in the response.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt;&lt;br&gt;&lt;li&gt;fullAccountNumber is deprecated and is replaced with fullAccountNumberList in include parameter and response.&lt;/li&gt;&lt;li&gt;fullAccountNumberList, PII (Personal Identifiable Information) and holder details are not available by default, as it is a premium feature that needs security approval. This will not be available for testing in Sandbox environment.&lt;/li&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String accountId = "accountId_example"; // String | Comma separated accountIds.
    String container = "container_example"; // String | bank/creditCard/investment/insurance/loan/reward/realEstate/otherAssets/otherLiabilities
    String include = "include_example"; // String | profile, holder, fullAccountNumber, fullAccountNumberList, paymentProfile, autoRefresh<br><b>Note:</b>fullAccountNumber is deprecated and is replaced with fullAccountNumberList in include parameter and response.
    String providerAccountId = "providerAccountId_example"; // String | Comma separated providerAccountIds.
    String requestId = "requestId_example"; // String | The unique identifier that returns contextual data
    String status = "status_example"; // String | ACTIVE,INACTIVE,TO_BE_CLOSED,CLOSED
    try {
      AccountResponse result = apiInstance.getAllAccounts(accountId, container, include, providerAccountId, requestId, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#getAllAccounts");
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
| **accountId** | **String**| Comma separated accountIds. | [optional] |
| **container** | **String**| bank/creditCard/investment/insurance/loan/reward/realEstate/otherAssets/otherLiabilities | [optional] |
| **include** | **String**| profile, holder, fullAccountNumber, fullAccountNumberList, paymentProfile, autoRefresh&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt;fullAccountNumber is deprecated and is replaced with fullAccountNumberList in include parameter and response. | [optional] |
| **providerAccountId** | **String**| Comma separated providerAccountIds. | [optional] |
| **requestId** | **String**| The unique identifier that returns contextual data | [optional] |
| **status** | **String**| ACTIVE,INACTIVE,TO_BE_CLOSED,CLOSED | [optional] |

### Return type

[**AccountResponse**](AccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Y800 : Invalid value for status&lt;br&gt;Y800 : Invalid value for container&lt;br&gt;Y800 : Invalid value for providerAccountId&lt;br&gt;Y824 : The maximum number of accountIds permitted is 100 |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="getHistoricalBalances"></a>
# **getHistoricalBalances**
> AccountHistoricalBalancesResponse getHistoricalBalances(accountId, fromDate, includeCF, interval, skip, toDate, top)

Get Historical Balances

The historical balances service is used to retrieve the historical balances for an account or a user.&lt;br&gt;Historical balances are daily (D), weekly (W), and monthly (M). &lt;br&gt;The interval input should be passed as D, W, and M to retrieve the desired historical balances. The default interval is daily (D). &lt;br&gt;When no account id is provided, historical balances of the accounts that are active, to be closed, and closed are provided in the response. &lt;br&gt;If the fromDate and toDate are not passed, the last 90 days of data will be provided. &lt;br&gt;The fromDate and toDate should be passed in the YYYY-MM-DD format. &lt;br&gt;The date field in the response denotes the date for which the balance is requested.&lt;br&gt;includeCF needs to be sent as true if the customer wants to return carried forward balances for a date when the data is not available. &lt;br&gt;asofDate field in the response denotes the date as of which the balance was updated for that account.&lt;br&gt;When there is no balance available for a requested date and if includeCF is sent as true, the previous date for which the balance is available is provided in the response. &lt;br&gt;When there is no previous balance available, no data will be sent.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String accountId = "accountId_example"; // String | accountId
    String fromDate = "fromDate_example"; // String | from date for balance retrieval (YYYY-MM-DD)
    Boolean includeCF = true; // Boolean | Consider carry forward logic for missing balances
    String interval = "interval_example"; // String | D-daily, W-weekly or M-monthly
    Integer skip = 56; // Integer | skip (Min 0)
    String toDate = "toDate_example"; // String | toDate for balance retrieval (YYYY-MM-DD)
    Integer top = 56; // Integer | top (Max 500)
    try {
      AccountHistoricalBalancesResponse result = apiInstance.getHistoricalBalances(accountId, fromDate, includeCF, interval, skip, toDate, top);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#getHistoricalBalances");
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
| **accountId** | **String**| accountId | [optional] |
| **fromDate** | **String**| from date for balance retrieval (YYYY-MM-DD) | [optional] |
| **includeCF** | **Boolean**| Consider carry forward logic for missing balances | [optional] |
| **interval** | **String**| D-daily, W-weekly or M-monthly | [optional] |
| **skip** | **Integer**| skip (Min 0) | [optional] |
| **toDate** | **String**| toDate for balance retrieval (YYYY-MM-DD) | [optional] |
| **top** | **Integer**| top (Max 500) | [optional] |

### Return type

[**AccountHistoricalBalancesResponse**](AccountHistoricalBalancesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Y800 : Invalid value for accountId&lt;br&gt;Y800 : Invalid value for fromDate&lt;br&gt;Y800 : Invalid value for toDate&lt;br&gt;Y809 : Invalid date range&lt;br&gt;Y800 : Invalid value for interval&lt;br&gt;Y802 : Future date not allowed |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

<a id="updateAccount"></a>
# **updateAccount**
> updateAccount(accountId, updateAccountRequest)

Update Account

The update account service is used to update manual and aggregated accounts.&lt;br&gt;The HTTP response code is 204 (Success without content).&lt;br&gt;Update manual account support is available for bank, card, investment, insurance, loan, otherAssets, otherLiabilities and realEstate containers only.&lt;br&gt;&lt;br&gt;&lt;b&gt;Note:&lt;/b&gt;&lt;li&gt; A real estate account update is only supported for SYSTEM and MANUAL valuation type.&lt;/li&gt;&lt;li&gt; Attribute &lt;b&gt;isEbillEnrolled&lt;/b&gt; is deprecated as it is applicable for bill accounts only.&lt;/li&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    Long accountId = 56L; // Long | accountId
    UpdateAccountRequest updateAccountRequest = new UpdateAccountRequest(); // UpdateAccountRequest | accountRequest
    try {
      apiInstance.updateAccount(accountId, updateAccountRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#updateAccount");
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
| **accountId** | **Long**| accountId | |
| **updateAccountRequest** | [**UpdateAccountRequest**](UpdateAccountRequest.md)| accountRequest | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | OK |  -  |
| **400** | Y800 : Invalid value for accountId&lt;br&gt;Y800 : Invalid value for updateParam&lt;br&gt;Y862 : The provided address is invalid, or the valuation is not available&lt;br&gt;Y868 : No action is allowed, as the data is being migrated to the Open Banking provider&lt;br&gt;Y869 : Multiple matches found. Provide the complete address or call the POST /accounts/evaluateAddress API to retrieve the list of matched addresses&lt;br&gt; |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |

