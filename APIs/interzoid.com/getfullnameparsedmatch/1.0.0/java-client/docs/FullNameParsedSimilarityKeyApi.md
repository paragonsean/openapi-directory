# FullNameParsedSimilarityKeyApi

All URIs are relative to *https://api.interzoid.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getfullnameparsedmatch**](FullNameParsedSimilarityKeyApi.md#getfullnameparsedmatch) | **GET** /getfullnameparsedmatch | Gets a similarity key for matching purposes for parsed full name data |


<a id="getfullnameparsedmatch"></a>
# **getfullnameparsedmatch**
> Getfullnameparsedmatch200Response getfullnameparsedmatch(license, firstname, lastname)

Gets a similarity key for matching purposes for parsed full name data

Gets a similarity key for matching purposes for parsed full name data, where the first name and last name are split into separate fields in the source data rather than combined.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FullNameParsedSimilarityKeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.interzoid.com");

    FullNameParsedSimilarityKeyApi apiInstance = new FullNameParsedSimilarityKeyApi(defaultClient);
    String license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
    String firstname = "firstname_example"; // String | First name from which to generate similarity key
    String lastname = "lastname_example"; // String | Last name from which to generate similarity key
    try {
      Getfullnameparsedmatch200Response result = apiInstance.getfullnameparsedmatch(license, firstname, lastname);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FullNameParsedSimilarityKeyApi#getfullnameparsedmatch");
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
| **firstname** | **String**| First name from which to generate similarity key | |
| **lastname** | **String**| Last name from which to generate similarity key | |

### Return type

[**Getfullnameparsedmatch200Response**](Getfullnameparsedmatch200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Generated similarity key for parsed full name data |  -  |
| **400** | bad request - insufficient parameters |  -  |
| **402** | credits exhausted |  -  |
| **403** | invalid license API key |  -  |
| **405** | method not allowed |  -  |
| **500** | internal server error |  -  |

