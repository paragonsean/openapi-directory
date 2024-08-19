# AdditionalRatesApi

All URIs are relative to *https://api.paylocity.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addOrUpdateAdditionalRates**](AdditionalRatesApi.md#addOrUpdateAdditionalRates) | **PUT** /v2/companies/{companyId}/employees/{employeeId}/additionalRates | Add/update additional rates |


<a id="addOrUpdateAdditionalRates"></a>
# **addOrUpdateAdditionalRates**
> addOrUpdateAdditionalRates(companyId, employeeId, additionalRate)

Add/update additional rates

Sends new or updated employee additional rates information directly to Web Pay.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AdditionalRatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.paylocity.com/api");
    
    // Configure OAuth2 access token for authorization: paylocity_auth
    OAuth paylocity_auth = (OAuth) defaultClient.getAuthentication("paylocity_auth");
    paylocity_auth.setAccessToken("YOUR ACCESS TOKEN");

    AdditionalRatesApi apiInstance = new AdditionalRatesApi(defaultClient);
    String companyId = "companyId_example"; // String | Company Id
    String employeeId = "employeeId_example"; // String | Employee Id
    AdditionalRate additionalRate = new AdditionalRate(); // AdditionalRate | Additional Rate Model
    try {
      apiInstance.addOrUpdateAdditionalRates(companyId, employeeId, additionalRate);
    } catch (ApiException e) {
      System.err.println("Exception when calling AdditionalRatesApi#addOrUpdateAdditionalRates");
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
| **additionalRate** | [**AdditionalRate**](AdditionalRate.md)| Additional Rate Model | |

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

