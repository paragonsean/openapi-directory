# BalanceApi

All URIs are relative to *https://api.bintable.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**balanceLookup**](BalanceApi.md#balanceLookup) | **GET** /balance | Check Balance |


<a id="balanceLookup"></a>
# **balanceLookup**
> List&lt;ResponseItem&gt; balanceLookup(apiKey)

Check Balance

Get Account balance and expiry

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
    defaultClient.setBasePath("https://api.bintable.com/v1");

    BalanceApi apiInstance = new BalanceApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key, which you can get from bintable.com website.
    try {
      List<ResponseItem> result = apiInstance.balanceLookup(apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BalanceApi#balanceLookup");
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
| **apiKey** | **String**| The API key, which you can get from bintable.com website. | |

### Return type

[**List&lt;ResponseItem&gt;**](ResponseItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Balance reponse |  -  |
| **401** | Your balance is exhausted,or package expired |  -  |
| **403** | Invalid API Key |  -  |
| **422** | API key is missing |  -  |

