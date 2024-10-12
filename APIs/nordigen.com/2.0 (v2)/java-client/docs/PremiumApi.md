# PremiumApi

All URIs are relative to *https://ob.nordigen.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**retrieveAccountTransactionsV2**](PremiumApi.md#retrieveAccountTransactionsV2) | **GET** /api/v2/accounts/premium/{id}/transactions/ |  |


<a id="retrieveAccountTransactionsV2"></a>
# **retrieveAccountTransactionsV2**
> Map&lt;String, Object&gt; retrieveAccountTransactionsV2(id, country, dateFrom, dateTo)



Access account premium transactions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PremiumApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ob.nordigen.com");
    
    // Configure HTTP bearer authorization: jwtAuth
    HttpBearerAuth jwtAuth = (HttpBearerAuth) defaultClient.getAuthentication("jwtAuth");
    jwtAuth.setBearerToken("BEARER TOKEN");

    PremiumApi apiInstance = new PremiumApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    String country = "AT"; // String | ISO 3166 two-character country code
    LocalDate dateFrom = LocalDate.parse("2023-01-21"); // LocalDate | 
    LocalDate dateTo = LocalDate.parse("2023-04-21"); // LocalDate | 
    try {
      Map<String, Object> result = apiInstance.retrieveAccountTransactionsV2(id, country, dateFrom, dateTo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PremiumApi#retrieveAccountTransactionsV2");
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
| **id** | **UUID**|  | |
| **country** | **String**| ISO 3166 two-character country code | [optional] |
| **dateFrom** | **LocalDate**|  | [optional] |
| **dateTo** | **LocalDate**|  | [optional] |

### Return type

**Map&lt;String, Object&gt;**

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Retrieve account transactions |  -  |
| **400** | Date range error |  -  |
| **401** | Failed Authentication |  -  |
| **403** | Account Access Forbidden |  -  |
| **404** | Account not found error |  -  |
| **409** | Account state error |  -  |
| **429** | Rate Limit Error |  -  |
| **500** | Unknown Request Error |  -  |
| **503** | Connection Error |  -  |

