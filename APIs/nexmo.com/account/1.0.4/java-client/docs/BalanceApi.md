# BalanceApi

All URIs are relative to *https://api.nexmo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAccountBalance**](BalanceApi.md#getAccountBalance) | **GET** /account/get-balance | Get Account Balance |
| [**topUpAccountBalance**](BalanceApi.md#topUpAccountBalance) | **POST** /account/top-up | Top Up Account Balance |


<a id="getAccountBalance"></a>
# **getAccountBalance**
> AccountBalance getAccountBalance(apiKey, apiSecret)

Get Account Balance

Retrieve the current balance of your Vonage API account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BalanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com");

    BalanceApi apiInstance = new BalanceApi(defaultClient);
    String apiKey = "abcd1234"; // String | Your Vonage API key. You can find this in the [dashboard](https://dashboard.nexmo.com)
    String apiSecret = "ABCDEFGH01234abc"; // String | Your Vonage API secret. You can find this in the [dashboard](https://dashboard.nexmo.com)
    try {
      AccountBalance result = apiInstance.getAccountBalance(apiKey, apiSecret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BalanceApi#getAccountBalance");
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
| **apiKey** | **String**| Your Vonage API key. You can find this in the [dashboard](https://dashboard.nexmo.com) | |
| **apiSecret** | **String**| Your Vonage API secret. You can find this in the [dashboard](https://dashboard.nexmo.com) | |

### Return type

[**AccountBalance**](AccountBalance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The current balance of your account |  -  |
| **401** | Not Authorised. You must supply your &#x60;api_key&#x60; and &#x60;api_secret&#x60; as query parameters to this request |  -  |

<a id="topUpAccountBalance"></a>
# **topUpAccountBalance**
> Success topUpAccountBalance(apiKey, apiSecret, trx)

Top Up Account Balance

You can top up your account using this API when you have enabled auto-reload in the dashboard. The amount added by the top-up operation will be the same amount as was added in the payment when auto-reload was enabled. Your account balance is checked every 5-10 minutes and if it falls below the threshold and auto-reload is enabled, then it will be topped up automatically. Use this endpoint  if you need to top up at times when your credit may be exhausted more quickly than the auto-reload may occur.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BalanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com");

    BalanceApi apiInstance = new BalanceApi(defaultClient);
    String apiKey = "abcd1234"; // String | Your Vonage API key. You can find this in the [dashboard](https://dashboard.nexmo.com)
    String apiSecret = "ABCDEFGH01234abc"; // String | Your Vonage API secret. You can find this in the [dashboard](https://dashboard.nexmo.com)
    String trx = "trx_example"; // String | The transaction reference of the transaction when balance was added and auto-reload was enabled on your account.
    try {
      Success result = apiInstance.topUpAccountBalance(apiKey, apiSecret, trx);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BalanceApi#topUpAccountBalance");
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
| **apiKey** | **String**| Your Vonage API key. You can find this in the [dashboard](https://dashboard.nexmo.com) | |
| **apiSecret** | **String**| Your Vonage API secret. You can find this in the [dashboard](https://dashboard.nexmo.com) | |
| **trx** | **String**| The transaction reference of the transaction when balance was added and auto-reload was enabled on your account. | |

### Return type

[**Success**](Success.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Not Authorised |  -  |

