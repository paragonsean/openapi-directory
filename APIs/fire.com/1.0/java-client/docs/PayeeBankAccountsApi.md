# PayeeBankAccountsApi

All URIs are relative to *https://api.fire.com/business*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPayees**](PayeeBankAccountsApi.md#getPayees) | **GET** /v1/payees | List all Payee Bank Accounts |


<a id="getPayees"></a>
# **getPayees**
> PayeeBankAccounts getPayees()

List all Payee Bank Accounts

Returns all your payee bank accounts.   Ordered by payee name ascending.   Can be paginated. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PayeeBankAccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fire.com/business");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    PayeeBankAccountsApi apiInstance = new PayeeBankAccountsApi(defaultClient);
    try {
      PayeeBankAccounts result = apiInstance.getPayees();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PayeeBankAccountsApi#getPayees");
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

[**PayeeBankAccounts**](PayeeBankAccounts.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of Payee Bank Accounts |  -  |

