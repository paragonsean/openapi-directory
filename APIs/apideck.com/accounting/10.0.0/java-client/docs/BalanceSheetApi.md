# BalanceSheetApi

All URIs are relative to *https://unify.apideck.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**balanceSheetOne**](BalanceSheetApi.md#balanceSheetOne) | **GET** /accounting/balance-sheet | Get BalanceSheet |


<a id="balanceSheetOne"></a>
# **balanceSheetOne**
> GetBalanceSheetResponse balanceSheetOne(xApideckConsumerId, xApideckAppId, xApideckServiceId, passThrough, filter, raw)

Get BalanceSheet

Get BalanceSheet

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BalanceSheetApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://unify.apideck.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    BalanceSheetApi apiInstance = new BalanceSheetApi(defaultClient);
    String xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
    String xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
    String xApideckServiceId = "xApideckServiceId_example"; // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    PassThroughQuery passThrough = null; // PassThroughQuery | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads
    BalanceSheetFilter filter = new BalanceSheetFilter(); // BalanceSheetFilter | Apply filters
    Boolean raw = false; // Boolean | Include raw response. Mostly used for debugging purposes
    try {
      GetBalanceSheetResponse result = apiInstance.balanceSheetOne(xApideckConsumerId, xApideckAppId, xApideckServiceId, passThrough, filter, raw);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BalanceSheetApi#balanceSheetOne");
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
| **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | |
| **xApideckAppId** | **String**| The ID of your Unify application | |
| **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] |
| **passThrough** | [**PassThroughQuery**](Object.md)| Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]&#x3D;leads becomes ?search&#x3D;leads | [optional] |
| **filter** | [**BalanceSheetFilter**](.md)| Apply filters | [optional] |
| **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false] |

### Return type

[**GetBalanceSheetResponse**](GetBalanceSheetResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | BalanceSheet |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **402** | Payment Required |  -  |
| **404** | The specified resource was not found |  -  |
| **422** | Unprocessable |  -  |
| **0** | Unexpected error |  -  |

