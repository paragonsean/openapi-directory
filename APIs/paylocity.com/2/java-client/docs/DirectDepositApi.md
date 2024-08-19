# DirectDepositApi

All URIs are relative to *https://api.paylocity.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAllDirectDeposit**](DirectDepositApi.md#getAllDirectDeposit) | **GET** /v2/companies/{companyId}/employees/{employeeId}/directDeposit | Get All Direct Deposit |


<a id="getAllDirectDeposit"></a>
# **getAllDirectDeposit**
> List&lt;DirectDeposit&gt; getAllDirectDeposit(companyId, employeeId)

Get All Direct Deposit

Get All Direct Deposit returns main direct deposit and all additional direct depositsfor the selected employee.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DirectDepositApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.paylocity.com/api");
    
    // Configure OAuth2 access token for authorization: paylocity_auth
    OAuth paylocity_auth = (OAuth) defaultClient.getAuthentication("paylocity_auth");
    paylocity_auth.setAccessToken("YOUR ACCESS TOKEN");

    DirectDepositApi apiInstance = new DirectDepositApi(defaultClient);
    String companyId = "companyId_example"; // String | Company Id
    String employeeId = "employeeId_example"; // String | Employee Id
    try {
      List<DirectDeposit> result = apiInstance.getAllDirectDeposit(companyId, employeeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DirectDepositApi#getAllDirectDeposit");
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

### Return type

[**List&lt;DirectDeposit&gt;**](DirectDeposit.md)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully Retrieved |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | The employee, or direct deposit does not exist |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |

