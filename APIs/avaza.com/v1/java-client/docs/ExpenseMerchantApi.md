# ExpenseMerchantApi

All URIs are relative to *https://api.avaza.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**expenseMerchangeLookup**](ExpenseMerchantApi.md#expenseMerchangeLookup) | **GET** /api/ExpenseMerchant/Lookup | Gets minimal list of Expense Merchants. |


<a id="expenseMerchangeLookup"></a>
# **expenseMerchangeLookup**
> ExpenseMerchantDropdownList expenseMerchangeLookup(pageSize, pageNumber, search)

Gets minimal list of Expense Merchants.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpenseMerchantApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ExpenseMerchantApi apiInstance = new ExpenseMerchantApi(defaultClient);
    Integer pageSize = 56; // Integer | Number of items per page (max 1000)
    Integer pageNumber = 56; // Integer | Page to display. Starts from 1.
    String search = "search_example"; // String | Search string to match against Expense Group Name
    try {
      ExpenseMerchantDropdownList result = apiInstance.expenseMerchangeLookup(pageSize, pageNumber, search);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpenseMerchantApi#expenseMerchangeLookup");
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
| **pageSize** | **Integer**| Number of items per page (max 1000) | [optional] |
| **pageNumber** | **Integer**| Page to display. Starts from 1. | [optional] |
| **search** | **String**| Search string to match against Expense Group Name | [optional] |

### Return type

[**ExpenseMerchantDropdownList**](ExpenseMerchantDropdownList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

