# TradesApi

All URIs are relative to *https://www.interactivebrokers.com/tradingapi/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**accountsAccountTradesGet**](TradesApi.md#accountsAccountTradesGet) | **GET** /accounts/{account}/trades | Returns trades in account |


<a id="accountsAccountTradesGet"></a>
# **accountsAccountTradesGet**
> List&lt;AccountsAccountTradesGet200ResponseInner&gt; accountsAccountTradesGet(account, body)

Returns trades in account

Returns a list of trades for the account starting at the given &#39;since&#39; date to the current time (now()). Timezone is UTC. Any request with a future since date or going further than one week will result in an HTTP 400 bad request response. Calling /trades without since will return all trades for the past 24 hours. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TradesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.interactivebrokers.com/tradingapi/v1");
    
    // Configure API key authorization: cookieAuth
    ApiKeyAuth cookieAuth = (ApiKeyAuth) defaultClient.getAuthentication("cookieAuth");
    cookieAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //cookieAuth.setApiKeyPrefix("Token");

    TradesApi apiInstance = new TradesApi(defaultClient);
    String account = "account_example"; // String | Account Number
    String body = "body_example"; // String | Start time specified in UTC. Allowed formats are \"yyyy-MM-dd\" or \"yyyy-MM-dd'T'HH:mm:ss\". Time is optional and is set to midnight if omitted, e.g. \"00:00:00 hh:mm:ss\". 
    try {
      List<AccountsAccountTradesGet200ResponseInner> result = apiInstance.accountsAccountTradesGet(account, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TradesApi#accountsAccountTradesGet");
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
| **body** | **String**| Start time specified in UTC. Allowed formats are \&quot;yyyy-MM-dd\&quot; or \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss\&quot;. Time is optional and is set to midnight if omitted, e.g. \&quot;00:00:00 hh:mm:ss\&quot;.  | [optional] |

### Return type

[**List&lt;AccountsAccountTradesGet200ResponseInner&gt;**](AccountsAccountTradesGet200ResponseInner.md)

### Authorization

[cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Trades |  -  |
| **202** | Unsuccessfull response |  -  |
| **204** | Unsuccessfull response |  -  |
| **400** | Unsuccessfull response |  -  |
| **401** | Unsuccessfull response |  -  |
| **403** | Unsuccessfull response |  -  |
| **408** | Unsuccessfull response |  -  |

