# PrimaryStateTaxApi

All URIs are relative to *https://api.paylocity.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addOrUpdatePrimaryStateTax**](PrimaryStateTaxApi.md#addOrUpdatePrimaryStateTax) | **PUT** /v2/companies/{companyId}/employees/{employeeId}/primaryStateTax | Add/update primary state tax |


<a id="addOrUpdatePrimaryStateTax"></a>
# **addOrUpdatePrimaryStateTax**
> addOrUpdatePrimaryStateTax(companyId, employeeId, stateTax)

Add/update primary state tax

Sends new or updated employee primary state tax information directly to Web Pay.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrimaryStateTaxApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.paylocity.com/api");
    
    // Configure OAuth2 access token for authorization: paylocity_auth
    OAuth paylocity_auth = (OAuth) defaultClient.getAuthentication("paylocity_auth");
    paylocity_auth.setAccessToken("YOUR ACCESS TOKEN");

    PrimaryStateTaxApi apiInstance = new PrimaryStateTaxApi(defaultClient);
    String companyId = "companyId_example"; // String | Company Id
    String employeeId = "employeeId_example"; // String | Employee Id
    StateTax stateTax = new StateTax(); // StateTax | Primary State Tax Model
    try {
      apiInstance.addOrUpdatePrimaryStateTax(companyId, employeeId, stateTax);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrimaryStateTaxApi#addOrUpdatePrimaryStateTax");
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
| **companyId** | **String**| Company Id | |
| **employeeId** | **String**| Employee Id | |
| **stateTax** | [**StateTax**](StateTax.md)| Primary State Tax Model | |

### Return type

null (empty response body)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully added or updated |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |

