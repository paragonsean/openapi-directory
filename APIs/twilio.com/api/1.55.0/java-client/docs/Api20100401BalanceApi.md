# Api20100401BalanceApi

All URIs are relative to *https://api.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchBalance**](Api20100401BalanceApi.md#fetchBalance) | **GET** /2010-04-01/Accounts/{AccountSid}/Balance.json |  |


<a id="fetchBalance"></a>
# **fetchBalance**
> ApiV2010AccountBalance fetchBalance(accountSid)



Fetch the balance for an Account based on Account Sid. Balance changes may not be reflected immediately. Child accounts do not contain balance information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Api20100401BalanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    Api20100401BalanceApi apiInstance = new Api20100401BalanceApi(defaultClient);
    String accountSid = "accountSid_example"; // String | The unique SID identifier of the Account.
    try {
      ApiV2010AccountBalance result = apiInstance.fetchBalance(accountSid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Api20100401BalanceApi#fetchBalance");
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
| **accountSid** | **String**| The unique SID identifier of the Account. | |

### Return type

[**ApiV2010AccountBalance**](ApiV2010AccountBalance.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

