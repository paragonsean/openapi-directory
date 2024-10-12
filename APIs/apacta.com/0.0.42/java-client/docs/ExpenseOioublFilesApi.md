# ExpenseOioublFilesApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**expensesExpenseIdOriginalFilesFileIdGet**](ExpenseOioublFilesApi.md#expensesExpenseIdOriginalFilesFileIdGet) | **GET** /expenses/{expense_id}/original_files/{file_id} | Show OIOUBL file |
| [**expensesExpenseIdOriginalFilesGet**](ExpenseOioublFilesApi.md#expensesExpenseIdOriginalFilesGet) | **GET** /expenses/{expense_id}/original_files | Show list of all OIOUBL files for the expense |


<a id="expensesExpenseIdOriginalFilesFileIdGet"></a>
# **expensesExpenseIdOriginalFilesFileIdGet**
> ClockingRecordsCheckoutPost201Response expensesExpenseIdOriginalFilesFileIdGet(expenseId, fileId)

Show OIOUBL file

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpenseOioublFilesApi;

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

    ExpenseOioublFilesApi apiInstance = new ExpenseOioublFilesApi(defaultClient);
    String expenseId = "expenseId_example"; // String | 
    String fileId = "fileId_example"; // String | 
    try {
      ClockingRecordsCheckoutPost201Response result = apiInstance.expensesExpenseIdOriginalFilesFileIdGet(expenseId, fileId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpenseOioublFilesApi#expensesExpenseIdOriginalFilesFileIdGet");
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
| **expenseId** | **String**|  | |
| **fileId** | **String**|  | |

### Return type

[**ClockingRecordsCheckoutPost201Response**](ClockingRecordsCheckoutPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **404** | Not found |  -  |

<a id="expensesExpenseIdOriginalFilesGet"></a>
# **expensesExpenseIdOriginalFilesGet**
> ClockingRecordsCheckoutPost201Response expensesExpenseIdOriginalFilesGet(expenseId)

Show list of all OIOUBL files for the expense

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpenseOioublFilesApi;

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

    ExpenseOioublFilesApi apiInstance = new ExpenseOioublFilesApi(defaultClient);
    String expenseId = "expenseId_example"; // String | 
    try {
      ClockingRecordsCheckoutPost201Response result = apiInstance.expensesExpenseIdOriginalFilesGet(expenseId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpenseOioublFilesApi#expensesExpenseIdOriginalFilesGet");
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
| **expenseId** | **String**|  | |

### Return type

[**ClockingRecordsCheckoutPost201Response**](ClockingRecordsCheckoutPost201Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

