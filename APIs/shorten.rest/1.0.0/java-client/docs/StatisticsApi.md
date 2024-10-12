# StatisticsApi

All URIs are relative to *https://api.shorten.rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getStatistics**](StatisticsApi.md#getStatistics) | **POST** /clicks/pg | Get clicks statistics |


<a id="getStatistics"></a>
# **getStatistics**
> ClickModelPg getStatistics(clicksFilterModel)

Get clicks statistics

Retrieve the raw click statistics for your account. Clicks are retrieved by creation date in descending order.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shorten.rest");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    ClicksFilterModel clicksFilterModel = new ClicksFilterModel(); // ClicksFilterModel | Filter
    try {
      ClickModelPg result = apiInstance.getStatistics(clicksFilterModel);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getStatistics");
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
| **clicksFilterModel** | [**ClicksFilterModel**](ClicksFilterModel.md)| Filter | |

### Return type

[**ClickModelPg**](ClickModelPg.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | returns Array of Click models, also returns lastId |  -  |

