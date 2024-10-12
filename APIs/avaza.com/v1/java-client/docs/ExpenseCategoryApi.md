# ExpenseCategoryApi

All URIs are relative to *https://api.avaza.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**expenseCategoryGet**](ExpenseCategoryApi.md#expenseCategoryGet) | **GET** /api/ExpenseCategory | Gets list of Expense Categories |


<a id="expenseCategoryGet"></a>
# **expenseCategoryGet**
> ExpenseCategoryList expenseCategoryGet(isEnabled)

Gets list of Expense Categories

The default sort order is by Name asc

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExpenseCategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.avaza.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ExpenseCategoryApi apiInstance = new ExpenseCategoryApi(defaultClient);
    Boolean isEnabled = true; // Boolean | Optional filter on for enabled/disabled categories. Defaults to true.
    try {
      ExpenseCategoryList result = apiInstance.expenseCategoryGet(isEnabled);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExpenseCategoryApi#expenseCategoryGet");
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
| **isEnabled** | **Boolean**| Optional filter on for enabled/disabled categories. Defaults to true. | [optional] |

### Return type

[**ExpenseCategoryList**](ExpenseCategoryList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |

