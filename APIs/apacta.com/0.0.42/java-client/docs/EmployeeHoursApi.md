# EmployeeHoursApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**employeeHoursGet**](EmployeeHoursApi.md#employeeHoursGet) | **GET** /employee_hours | Used to retrieve details about the logged in user&#39;s hours |


<a id="employeeHoursGet"></a>
# **employeeHoursGet**
> EmployeeHoursGet200Response employeeHoursGet(dateFrom, dateTo)

Used to retrieve details about the logged in user&#39;s hours

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EmployeeHoursApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    EmployeeHoursApi apiInstance = new EmployeeHoursApi(defaultClient);
    String dateFrom = "dateFrom_example"; // String | Date formatted as Y-m-d (2016-06-28)
    String dateTo = "dateTo_example"; // String | Date formatted as Y-m-d (2016-06-28)
    try {
      EmployeeHoursGet200Response result = apiInstance.employeeHoursGet(dateFrom, dateTo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EmployeeHoursApi#employeeHoursGet");
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
| **dateFrom** | **String**| Date formatted as Y-m-d (2016-06-28) | |
| **dateTo** | **String**| Date formatted as Y-m-d (2016-06-28) | |

### Return type

[**EmployeeHoursGet200Response**](EmployeeHoursGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

