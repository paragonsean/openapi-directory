# CountryNameStandardizationApi

All URIs are relative to *https://api.interzoid.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getcountrystandard**](CountryNameStandardizationApi.md#getcountrystandard) | **GET** /getcountrystandard | Gets country name standard |


<a id="getcountrystandard"></a>
# **getcountrystandard**
> Getcountrystandard200Response getcountrystandard(license, country)

Gets country name standard

Gets a pre-selected country name standard for various permutations of a given country name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CountryNameStandardizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.interzoid.com");

    CountryNameStandardizationApi apiInstance = new CountryNameStandardizationApi(defaultClient);
    String license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
    String country = "country_example"; // String | Country name from which to retrieve the standardized version
    try {
      Getcountrystandard200Response result = apiInstance.getcountrystandard(license, country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CountryNameStandardizationApi#getcountrystandard");
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
| **country** | **String**| Country name from which to retrieve the standardized version | |

### Return type

[**Getcountrystandard200Response**](Getcountrystandard200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Standardized country name data |  -  |
| **400** | bad request - insufficient parameters |  -  |
| **402** | credits exhausted |  -  |
| **403** | invalid license API key |  -  |
| **405** | method not allowed |  -  |
| **500** | internal server error |  -  |

