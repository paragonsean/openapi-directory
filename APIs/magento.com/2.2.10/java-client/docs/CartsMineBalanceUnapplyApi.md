# CartsMineBalanceUnapplyApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**customerBalanceBalanceManagementFromQuoteV1UnapplyPost**](CartsMineBalanceUnapplyApi.md#customerBalanceBalanceManagementFromQuoteV1UnapplyPost) | **POST** /V1/carts/mine/balance/unapply | carts/mine/balance/unapply |


<a id="customerBalanceBalanceManagementFromQuoteV1UnapplyPost"></a>
# **customerBalanceBalanceManagementFromQuoteV1UnapplyPost**
> Boolean customerBalanceBalanceManagementFromQuoteV1UnapplyPost()

carts/mine/balance/unapply

Unapply store credit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineBalanceUnapplyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineBalanceUnapplyApi apiInstance = new CartsMineBalanceUnapplyApi(defaultClient);
    try {
      Boolean result = apiInstance.customerBalanceBalanceManagementFromQuoteV1UnapplyPost();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineBalanceUnapplyApi#customerBalanceBalanceManagementFromQuoteV1UnapplyPost");
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

