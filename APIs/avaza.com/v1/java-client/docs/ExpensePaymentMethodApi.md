# ExpensePaymentMethodApi

All URIs are relative to *https://api.avaza.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**expensePaymentMethodLookup**](ExpensePaymentMethodApi.md#expensePaymentMethodLookup) | **GET** /api/ExpensePaymentMethod/Lookup | Gets minimal list of Expense Payment Methods. |


<a id="expensePaymentMethodLookup"></a>
# **expensePaymentMethodLookup**
> ExpensePaymentMethodDropdownList expensePaymentMethodLookup()

Gets minimal list of Expense Payment Methods.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpensePaymentMethodApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ExpensePaymentMethodApi apiInstance = new ExpensePaymentMethodApi(defaultClient);
    try {
      ExpensePaymentMethodDropdownList result = apiInstance.expensePaymentMethodLookup();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpensePaymentMethodApi#expensePaymentMethodLookup");
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

[**ExpensePaymentMethodDropdownList**](ExpensePaymentMethodDropdownList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

