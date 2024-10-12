# TestnetFaucetApi

All URIs are relative to *https://ntp1node.nebl.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**testnetGetFaucet**](TestnetFaucetApi.md#testnetGetFaucet) | **GET** /testnet/faucet | Withdraws testnet NEBL to the specified address |


<a id="testnetGetFaucet"></a>
# **testnetGetFaucet**
> GetFaucetResponse testnetGetFaucet(address, amount)

Withdraws testnet NEBL to the specified address

Withdraw testnet NEBL to your Neblio Testnet address. By default amount is 1500000000 or 15 NEBL and has a max of 50 NEBL. Only 2 withdrawals allowed per 24 hour period. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TestnetFaucetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ntp1node.nebl.io");

    TestnetFaucetApi apiInstance = new TestnetFaucetApi(defaultClient);
    String address = "address_example"; // String | Your Neblio Testnet Address
    BigDecimal amount = new BigDecimal(78); // BigDecimal | Amount of NEBL to withdrawal in satoshis
    try {
      GetFaucetResponse result = apiInstance.testnetGetFaucet(address, amount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TestnetFaucetApi#testnetGetFaucet");
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
| **address** | **String**| Your Neblio Testnet Address | |
| **amount** | **BigDecimal**| Amount of NEBL to withdrawal in satoshis | [optional] |

### Return type

[**GetFaucetResponse**](GetFaucetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Object containing the transaction ID of the withdrawal. |  -  |

