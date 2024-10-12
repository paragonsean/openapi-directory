# ConnectionsApi

All URIs are relative to *https://api.codat.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createPartnerExpenseConnection**](ConnectionsApi.md#createPartnerExpenseConnection) | **POST** /companies/{companyId}/sync/expenses/connections/partnerExpense | Create Partner Expense connection |


<a id="createPartnerExpenseConnection"></a>
# **createPartnerExpenseConnection**
> DataConnection createPartnerExpenseConnection(companyId)

Create Partner Expense connection

Creates a Partner Expense data connection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ConnectionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.codat.io");
    
    // Configure API key authorization: auth_header
    ApiKeyAuth auth_header = (ApiKeyAuth) defaultClient.getAuthentication("auth_header");
    auth_header.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //auth_header.setApiKeyPrefix("Token");

    ConnectionsApi apiInstance = new ConnectionsApi(defaultClient);
    UUID companyId = UUID.fromString("8a210b68-6988-11ed-a1eb-0242ac120002"); // UUID | 
    try {
      DataConnection result = apiInstance.createPartnerExpenseConnection(companyId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ConnectionsApi#createPartnerExpenseConnection");
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
| **companyId** | **UUID**|  | |

### Return type

[**DataConnection**](DataConnection.md)

### Authorization

[auth_header](../README.md#auth_header)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

