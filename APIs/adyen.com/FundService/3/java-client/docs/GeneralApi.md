# GeneralApi

All URIs are relative to *https://cal-test.adyen.com/cal/services/Fund/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postAccountHolderBalance**](GeneralApi.md#postAccountHolderBalance) | **POST** /accountHolderBalance | Get the balances of an account holder |
| [**postAccountHolderTransactionList**](GeneralApi.md#postAccountHolderTransactionList) | **POST** /accountHolderTransactionList | Get a list of transactions |
| [**postDebitAccountHolder**](GeneralApi.md#postDebitAccountHolder) | **POST** /debitAccountHolder | Send a direct debit request |
| [**postPayoutAccountHolder**](GeneralApi.md#postPayoutAccountHolder) | **POST** /payoutAccountHolder | Pay out from an account to the account holder |
| [**postRefundFundsTransfer**](GeneralApi.md#postRefundFundsTransfer) | **POST** /refundFundsTransfer | Refund a funds transfer |
| [**postRefundNotPaidOutTransfers**](GeneralApi.md#postRefundNotPaidOutTransfers) | **POST** /refundNotPaidOutTransfers | Refund all transactions of an account since the most recent payout |
| [**postSetupBeneficiary**](GeneralApi.md#postSetupBeneficiary) | **POST** /setupBeneficiary | Designate a beneficiary account and transfer the benefactor&#39;s current balance |
| [**postTransferFunds**](GeneralApi.md#postTransferFunds) | **POST** /transferFunds | Transfer funds between platform accounts |


<a id="postAccountHolderBalance"></a>
# **postAccountHolderBalance**
> AccountHolderBalanceResponse postAccountHolderBalance(accountHolderBalanceRequest)

Get the balances of an account holder

Returns the account balances of an account holder. An account&#39;s balances are organized according by currencies. This mean that an account may have multiple balances: one for each currency.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Fund/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    AccountHolderBalanceRequest accountHolderBalanceRequest = new AccountHolderBalanceRequest(); // AccountHolderBalanceRequest | 
    try {
      AccountHolderBalanceResponse result = apiInstance.postAccountHolderBalance(accountHolderBalanceRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#postAccountHolderBalance");
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
| **accountHolderBalanceRequest** | [**AccountHolderBalanceRequest**](AccountHolderBalanceRequest.md)|  | [optional] |

### Return type

[**AccountHolderBalanceResponse**](AccountHolderBalanceResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **202** | Accepted - the request has been accepted for processing, but the processing has not been completed. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postAccountHolderTransactionList"></a>
# **postAccountHolderTransactionList**
> AccountHolderTransactionListResponse postAccountHolderTransactionList(accountHolderTransactionListRequest)

Get a list of transactions

Returns a list of transactions for an account holder&#39;s accounts. You can specify the accounts and transaction statuses to be included on the list. The call returns a maximum of 50 transactions for each account. To retrieve all transactions, you must make another call with the &#39;page&#39; value incremented. Transactions are listed in chronological order, with the most recent transaction first.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Fund/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    AccountHolderTransactionListRequest accountHolderTransactionListRequest = new AccountHolderTransactionListRequest(); // AccountHolderTransactionListRequest | 
    try {
      AccountHolderTransactionListResponse result = apiInstance.postAccountHolderTransactionList(accountHolderTransactionListRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#postAccountHolderTransactionList");
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
| **accountHolderTransactionListRequest** | [**AccountHolderTransactionListRequest**](AccountHolderTransactionListRequest.md)|  | [optional] |

### Return type

[**AccountHolderTransactionListResponse**](AccountHolderTransactionListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **202** | Accepted - the request has been accepted for processing, but the processing has not been completed. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postDebitAccountHolder"></a>
# **postDebitAccountHolder**
> DebitAccountHolderResponse postDebitAccountHolder(debitAccountHolderRequest)

Send a direct debit request

Sends a direct debit request to an account holder&#39;s bank account. If the direct debit is successful, the funds are settled in the accounts specified in the split instructions. Adyen sends the result of the direct debit in a [&#x60;DIRECT_DEBIT_INITIATED&#x60;](https://docs.adyen.com/api-explorer/#/NotificationService/latest/post/DIRECT_DEBIT_INITIATED) notification webhook.   To learn more about direct debits, see [Top up accounts](https://docs.adyen.com/marketplaces-and-platforms/classic/top-up-accounts).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Fund/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    DebitAccountHolderRequest debitAccountHolderRequest = new DebitAccountHolderRequest(); // DebitAccountHolderRequest | 
    try {
      DebitAccountHolderResponse result = apiInstance.postDebitAccountHolder(debitAccountHolderRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#postDebitAccountHolder");
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
| **debitAccountHolderRequest** | [**DebitAccountHolderRequest**](DebitAccountHolderRequest.md)|  | [optional] |

### Return type

[**DebitAccountHolderResponse**](DebitAccountHolderResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **202** | Accepted - the request has been accepted for processing, but the processing has not been completed. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postPayoutAccountHolder"></a>
# **postPayoutAccountHolder**
> PayoutAccountHolderResponse postPayoutAccountHolder(payoutAccountHolderRequest)

Pay out from an account to the account holder

Pays out a specified amount from an account to the bank account of account holder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Fund/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    PayoutAccountHolderRequest payoutAccountHolderRequest = new PayoutAccountHolderRequest(); // PayoutAccountHolderRequest | 
    try {
      PayoutAccountHolderResponse result = apiInstance.postPayoutAccountHolder(payoutAccountHolderRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#postPayoutAccountHolder");
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
| **payoutAccountHolderRequest** | [**PayoutAccountHolderRequest**](PayoutAccountHolderRequest.md)|  | [optional] |

### Return type

[**PayoutAccountHolderResponse**](PayoutAccountHolderResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **202** | Accepted - the request has been accepted for processing, but the processing has not been completed. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postRefundFundsTransfer"></a>
# **postRefundFundsTransfer**
> RefundFundsTransferResponse postRefundFundsTransfer(refundFundsTransferRequest)

Refund a funds transfer

Refunds funds transferred from one account to another. Both accounts must be in the same platform, but can have different account holders. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Fund/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    RefundFundsTransferRequest refundFundsTransferRequest = new RefundFundsTransferRequest(); // RefundFundsTransferRequest | 
    try {
      RefundFundsTransferResponse result = apiInstance.postRefundFundsTransfer(refundFundsTransferRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#postRefundFundsTransfer");
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
| **refundFundsTransferRequest** | [**RefundFundsTransferRequest**](RefundFundsTransferRequest.md)|  | [optional] |

### Return type

[**RefundFundsTransferResponse**](RefundFundsTransferResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **202** | Accepted - the request has been accepted for processing, but the processing has not been completed. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postRefundNotPaidOutTransfers"></a>
# **postRefundNotPaidOutTransfers**
> RefundNotPaidOutTransfersResponse postRefundNotPaidOutTransfers(refundNotPaidOutTransfersRequest)

Refund all transactions of an account since the most recent payout

Refunds all the transactions of an account that have taken place since the most recent payout. This request is on a account basis (as opposed to a payment basis), so only the portion of the payment that was made to the specified account is refunded. The commissions, fees, and payments to other accounts remain in the accounts to which they were sent as designated by the original payment&#39;s split details.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Fund/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    RefundNotPaidOutTransfersRequest refundNotPaidOutTransfersRequest = new RefundNotPaidOutTransfersRequest(); // RefundNotPaidOutTransfersRequest | 
    try {
      RefundNotPaidOutTransfersResponse result = apiInstance.postRefundNotPaidOutTransfers(refundNotPaidOutTransfersRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#postRefundNotPaidOutTransfers");
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
| **refundNotPaidOutTransfersRequest** | [**RefundNotPaidOutTransfersRequest**](RefundNotPaidOutTransfersRequest.md)|  | [optional] |

### Return type

[**RefundNotPaidOutTransfersResponse**](RefundNotPaidOutTransfersResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **202** | Accepted - the request has been accepted for processing, but the processing has not been completed. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postSetupBeneficiary"></a>
# **postSetupBeneficiary**
> SetupBeneficiaryResponse postSetupBeneficiary(setupBeneficiaryRequest)

Designate a beneficiary account and transfer the benefactor&#39;s current balance

Defines a benefactor and a beneficiary relationship between two accounts. At the time of benefactor/beneficiary setup, the funds in the benefactor account are transferred to the beneficiary account, and any further payments to the benefactor account are automatically sent to the beneficiary account. A series of benefactor/beneficiaries may not exceed four beneficiaries and may not have a cycle in it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Fund/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    SetupBeneficiaryRequest setupBeneficiaryRequest = new SetupBeneficiaryRequest(); // SetupBeneficiaryRequest | 
    try {
      SetupBeneficiaryResponse result = apiInstance.postSetupBeneficiary(setupBeneficiaryRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#postSetupBeneficiary");
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
| **setupBeneficiaryRequest** | [**SetupBeneficiaryRequest**](SetupBeneficiaryRequest.md)|  | [optional] |

### Return type

[**SetupBeneficiaryResponse**](SetupBeneficiaryResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **202** | Accepted - the request has been accepted for processing, but the processing has not been completed. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postTransferFunds"></a>
# **postTransferFunds**
> TransferFundsResponse postTransferFunds(transferFundsRequest)

Transfer funds between platform accounts

Transfers funds from one account to another account. Both accounts must be in the same platform, but can have different account holders. The transfer must include a transfer code, which should be determined by the platform, in compliance with local regulations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://cal-test.adyen.com/cal/services/Fund/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    TransferFundsRequest transferFundsRequest = new TransferFundsRequest(); // TransferFundsRequest | 
    try {
      TransferFundsResponse result = apiInstance.postTransferFunds(transferFundsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#postTransferFunds");
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
| **transferFundsRequest** | [**TransferFundsRequest**](TransferFundsRequest.md)|  | [optional] |

### Return type

[**TransferFundsResponse**](TransferFundsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **202** | Accepted - the request has been accepted for processing, but the processing has not been completed. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

