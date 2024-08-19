# AccountApi

All URIs are relative to *https://api.idtbeyond.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**iatuBalanceGet**](AccountApi.md#iatuBalanceGet) | **GET** /iatu/balance | Account balance |


<a id="iatuBalanceGet"></a>
# **iatuBalanceGet**
> iatuBalanceGet(xIdtBeyondAppId, xIdtBeyondAppKey)

Account balance

Returns a JSON of the account balance.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.idtbeyond.com/v1");

    AccountApi apiInstance = new AccountApi(defaultClient);
    String xIdtBeyondAppId = "APP_ID"; // String | Application ID you would like to use
    String xIdtBeyondAppKey = "APP_KEY"; // String | Application KEY you would like to use
    try {
      apiInstance.iatuBalanceGet(xIdtBeyondAppId, xIdtBeyondAppKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountApi#iatuBalanceGet");
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
| **xIdtBeyondAppId** | **String**| Application ID you would like to use | [default to APP_ID] |
| **xIdtBeyondAppKey** | **String**| Application KEY you would like to use | [default to APP_KEY] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful balance JSON response |  -  |

