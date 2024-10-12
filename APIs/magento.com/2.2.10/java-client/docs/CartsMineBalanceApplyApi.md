# CartsMineBalanceApplyApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerBalanceBalanceManagementFromQuoteV1ApplyPost**](CartsMineBalanceApplyApi.md#customerBalanceBalanceManagementFromQuoteV1ApplyPost) | **POST** /V1/carts/mine/balance/apply | carts/mine/balance/apply |


<a id="customerBalanceBalanceManagementFromQuoteV1ApplyPost"></a>
# **customerBalanceBalanceManagementFromQuoteV1ApplyPost**
> Boolean customerBalanceBalanceManagementFromQuoteV1ApplyPost()

carts/mine/balance/apply

Apply store credit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineBalanceApplyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineBalanceApplyApi apiInstance = new CartsMineBalanceApplyApi(defaultClient);
    try {
      Boolean result = apiInstance.customerBalanceBalanceManagementFromQuoteV1ApplyPost();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineBalanceApplyApi#customerBalanceBalanceManagementFromQuoteV1ApplyPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

