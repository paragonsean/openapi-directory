# CountryMatchSimilarityKeyApi

All URIs are relative to *https://api.interzoid.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getcountrymatch**](CountryMatchSimilarityKeyApi.md#getcountrymatch) | **GET** /getcountrymatch | Gets a similarity key for matching purposes for country name data |


<a id="getcountrymatch"></a>
# **getcountrymatch**
> Getcountrymatch200Response getcountrymatch(license, country)

Gets a similarity key for matching purposes for country name data

Gets a similarity key to use for matching purposes for country name data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CountryMatchSimilarityKeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.interzoid.com");

    CountryMatchSimilarityKeyApi apiInstance = new CountryMatchSimilarityKeyApi(defaultClient);
    String license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
    String country = "country_example"; // String | Country name from which to generate similarity key
    try {
      Getcountrymatch200Response result = apiInstance.getcountrymatch(license, country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CountryMatchSimilarityKeyApi#getcountrymatch");
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
| **country** | **String**| Country name from which to generate similarity key | |

### Return type

[**Getcountrymatch200Response**](Getcountrymatch200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Generated similarity key for country name data |  -  |
| **400** | bad request - insufficient parameters |  -  |
| **402** | credits exhausted |  -  |
| **403** | invalid license API key |  -  |
| **405** | method not allowed |  -  |
| **500** | internal server error |  -  |

