# GeneralApi

All URIs are relative to *https://pal-test.adyen.com/pal/servlet/BalanceControl/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postBalanceTransfer**](GeneralApi.md#postBalanceTransfer) | **POST** /balanceTransfer | Start a balance transfer |


<a id="postBalanceTransfer"></a>
# **postBalanceTransfer**
> BalanceTransferResponse postBalanceTransfer(balanceTransferRequest)

Start a balance transfer

Starts a balance transfer request between merchant accounts. The following conditions must be met before you can successfully transfer balances:  * The source and destination merchant accounts must be under the same company account and legal entity.  * The source merchant account must have sufficient funds.  * The source and destination merchant accounts must have at least one common processing currency.  When sending multiple API requests with the same source and destination merchant accounts, send the requests sequentially and *not* in parallel. Some requests may not be processed if the requests are sent in parallel. 

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
    defaultClient.setBasePath("https://pal-test.adyen.com/pal/servlet/BalanceControl/v1");
    
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
    BalanceTransferRequest balanceTransferRequest = new BalanceTransferRequest(); // BalanceTransferRequest | 
    try {
      BalanceTransferResponse result = apiInstance.postBalanceTransfer(balanceTransferRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#postBalanceTransfer");
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
| **balanceTransferRequest** | [**BalanceTransferRequest**](BalanceTransferRequest.md)|  | [optional] |

### Return type

[**BalanceTransferResponse**](BalanceTransferResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |

