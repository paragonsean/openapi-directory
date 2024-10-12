# AnalyticsApi

All URIs are relative to *https://gateway.seven.io/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**analytics**](AnalyticsApi.md#analytics) | **GET** /analytics |  |


<a id="analytics"></a>
# **analytics**
> Analytics200Response analytics(start, end, label, subaccounts, groupBy)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://gateway.seven.io/api");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    AnalyticsApi apiInstance = new AnalyticsApi(defaultClient);
    String start = "start_example"; // String | Start date of the statistics in the format YYYY-MM-DD. By default, the date of 30 days ago is set.
    String end = "end_example"; // String | End date of the statistics in the format YYYY-MM-DD. By default, the current day.
    String label = "label_example"; // String | Shows only data of a specific label.
    String subaccounts = "subaccounts_example"; // String | Receive the data only for the main account, all your (sub-)accounts or only for specific subaccounts.
    String groupBy = "date"; // String | Defines the grouping of the data.
    try {
      Analytics200Response result = apiInstance.analytics(start, end, label, subaccounts, groupBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsApi#analytics");
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
| **start** | **String**| Start date of the statistics in the format YYYY-MM-DD. By default, the date of 30 days ago is set. | [optional] |
| **end** | **String**| End date of the statistics in the format YYYY-MM-DD. By default, the current day. | [optional] |
| **label** | **String**| Shows only data of a specific label. | [optional] |
| **subaccounts** | **String**| Receive the data only for the main account, all your (sub-)accounts or only for specific subaccounts. | [optional] |
| **groupBy** | **String**| Defines the grouping of the data. | [optional] [enum: date, label, subaccount, country] |

### Return type

[**Analytics200Response**](Analytics200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

