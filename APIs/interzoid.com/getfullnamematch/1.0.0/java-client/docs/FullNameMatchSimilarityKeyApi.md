# FullNameMatchSimilarityKeyApi

All URIs are relative to *https://api.interzoid.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getfullnamematch**](FullNameMatchSimilarityKeyApi.md#getfullnamematch) | **GET** /getfullnamematch | Gets a similarity key for matching purposes for full name data |


<a id="getfullnamematch"></a>
# **getfullnamematch**
> Getfullnamematch200Response getfullnamematch(license, fullname)

Gets a similarity key for matching purposes for full name data

Gets a similarity key for matching purposes for full name data, where first and last name are part of the same field.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FullNameMatchSimilarityKeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.interzoid.com");

    FullNameMatchSimilarityKeyApi apiInstance = new FullNameMatchSimilarityKeyApi(defaultClient);
    String license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
    String fullname = "fullname_example"; // String | Full name from which to generate similarity key
    try {
      Getfullnamematch200Response result = apiInstance.getfullnamematch(license, fullname);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FullNameMatchSimilarityKeyApi#getfullnamematch");
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
| **fullname** | **String**| Full name from which to generate similarity key | |

### Return type

[**Getfullnamematch200Response**](Getfullnamematch200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Generated similarity key for full name data |  -  |
| **400** | bad request - insufficient parameters |  -  |
| **402** | credits exhausted |  -  |
| **403** | invalid license API key |  -  |
| **405** | method not allowed |  -  |
| **500** | internal server error |  -  |

