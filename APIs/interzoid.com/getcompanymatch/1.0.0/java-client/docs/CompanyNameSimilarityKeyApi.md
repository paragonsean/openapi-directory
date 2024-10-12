# CompanyNameSimilarityKeyApi

All URIs are relative to *https://api.interzoid.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getcompanymatch**](CompanyNameSimilarityKeyApi.md#getcompanymatch) | **GET** /getcompanymatch | Gets a similarity key for matching purposes for company name data |


<a id="getcompanymatch"></a>
# **getcompanymatch**
> Getcompanymatch200Response getcompanymatch(license, company)

Gets a similarity key for matching purposes for company name data

Gets a similarity key for matching purposes for company name data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CompanyNameSimilarityKeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.interzoid.com");

    CompanyNameSimilarityKeyApi apiInstance = new CompanyNameSimilarityKeyApi(defaultClient);
    String license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
    String company = "company_example"; // String | Company name from which to generate similarity key
    try {
      Getcompanymatch200Response result = apiInstance.getcompanymatch(license, company);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CompanyNameSimilarityKeyApi#getcompanymatch");
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
| **license** | **String**| Your Interzoid license API key. Register at www.interzoid.com/register | |
| **company** | **String**| Company name from which to generate similarity key | |

### Return type

[**Getcompanymatch200Response**](Getcompanymatch200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Generated similarity key for company name data |  -  |
| **400** | bad request - insufficient parameters |  -  |
| **402** | credits exhausted |  -  |
| **403** | invalid license API key |  -  |
| **405** | method not allowed |  -  |
| **500** | internal server error |  -  |

