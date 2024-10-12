# SummaryApi

All URIs are relative to *http://data.orghunter.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSummary**](SummaryApi.md#getSummary) | **POST** /v1/charitysearch | Get summary data! |


<a id="getSummary"></a>
# **getSummary**
> getSummary(ein, searchTerm, city, state, zipCode, category, eligible, start, rows)

Get summary data!

&lt;p&gt;This operation provides summary data.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SummaryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://data.orghunter.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    SummaryApi apiInstance = new SummaryApi(defaultClient);
    String ein = "ein_example"; // String | Employer Identification Number (EIN)
    String searchTerm = "searchTerm_example"; // String | Charity Name or Keyword. Example: humane society or cancer
    String city = "city_example"; // String | City Name. Example: Miami
    String state = "state_example"; // String | State Name - Two letter state abbreviation
    String zipCode = "zipCode_example"; // String | Zipcode Value - 5 digit zipcode value
    String category = "category_example"; // String | Category Value Selected from Categories API
    String eligible = "eligible_example"; // String | eligible=1 will return only organizations that are tax deductible and in good standing with the IRS
    String start = "start_example"; // String | Record Set Start Position
    String rows = "rows_example"; // String | Records Per Page. Default Value = 20
    try {
      apiInstance.getSummary(ein, searchTerm, city, state, zipCode, category, eligible, start, rows);
    } catch (ApiException e) {
      System.err.println("Exception when calling SummaryApi#getSummary");
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
| **ein** | **String**| Employer Identification Number (EIN) | [optional] |
| **searchTerm** | **String**| Charity Name or Keyword. Example: humane society or cancer | [optional] |
| **city** | **String**| City Name. Example: Miami | [optional] |
| **state** | **String**| State Name - Two letter state abbreviation | [optional] |
| **zipCode** | **String**| Zipcode Value - 5 digit zipcode value | [optional] |
| **category** | **String**| Category Value Selected from Categories API | [optional] |
| **eligible** | **String**| eligible&#x3D;1 will return only organizations that are tax deductible and in good standing with the IRS | [optional] |
| **start** | **String**| Record Set Start Position | [optional] |
| **rows** | **String**| Records Per Page. Default Value &#x3D; 20 | [optional] |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

