# StateDataStandardizationApi

All URIs are relative to *https://api.interzoid.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getstateabbreviation**](StateDataStandardizationApi.md#getstateabbreviation) | **GET** /getstateabbreviation | Gets a two-letter abbreviation for a state or province name data |


<a id="getstateabbreviation"></a>
# **getstateabbreviation**
> Getstateabbreviation200Response getstateabbreviation(license, state)

Gets a two-letter abbreviation for a state or province name data

Gets a two-letter abbreviation for a state or province given a permutation of state or province data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StateDataStandardizationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.interzoid.com");

    StateDataStandardizationApi apiInstance = new StateDataStandardizationApi(defaultClient);
    String license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
    String state = "state_example"; // String | State (or province) name from which to retrieve the two letter abbreviation.
    try {
      Getstateabbreviation200Response result = apiInstance.getstateabbreviation(license, state);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StateDataStandardizationApi#getstateabbreviation");
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
| **state** | **String**| State (or province) name from which to retrieve the two letter abbreviation. | |

### Return type

[**Getstateabbreviation200Response**](Getstateabbreviation200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | State (or province) standardized two-letter abbreviation |  -  |
| **400** | bad request - insufficient parameters |  -  |
| **402** | credits exhausted |  -  |
| **403** | invalid license API key |  -  |
| **405** | method not allowed |  -  |
| **500** | internal server error |  -  |

