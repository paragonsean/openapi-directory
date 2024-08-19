# EmployeeStagingApi

All URIs are relative to *https://api.paylocity.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addNewEmployeeToWebLink**](EmployeeStagingApi.md#addNewEmployeeToWebLink) | **POST** /v2/weblinkstaging/companies/{companyId}/employees/newemployees | Add new employee to Web Link |


<a id="addNewEmployeeToWebLink"></a>
# **addNewEmployeeToWebLink**
> List&lt;TrackingNumberResponse&gt; addNewEmployeeToWebLink(companyId, stagedEmployee)

Add new employee to Web Link

Add new employee to Web Link will send partially completed or potentially erroneous new hire record to Web Link, where it can be corrected and competed by company administrator or authorized Paylocity Service Bureau employee.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmployeeStagingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.paylocity.com/api");
    
    // Configure OAuth2 access token for authorization: paylocity_auth
    OAuth paylocity_auth = (OAuth) defaultClient.getAuthentication("paylocity_auth");
    paylocity_auth.setAccessToken("YOUR ACCESS TOKEN");

    EmployeeStagingApi apiInstance = new EmployeeStagingApi(defaultClient);
    String companyId = "companyId_example"; // String | Company Id
    StagedEmployee stagedEmployee = new StagedEmployee(); // StagedEmployee | StagedEmployee Model
    try {
      List<TrackingNumberResponse> result = apiInstance.addNewEmployeeToWebLink(companyId, stagedEmployee);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmployeeStagingApi#addNewEmployeeToWebLink");
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
| **stagedEmployee** | [**StagedEmployee**](StagedEmployee.md)| StagedEmployee Model | |

### Return type

[**List&lt;TrackingNumberResponse&gt;**](TrackingNumberResponse.md)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successfully Added |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **429** | Too Many Requests |  -  |
| **500** | Internal Server Error |  -  |

