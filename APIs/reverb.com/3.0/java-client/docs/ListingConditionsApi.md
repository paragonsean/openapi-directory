# ListingConditionsApi

All URIs are relative to *https://api.reverb.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listingConditionsGet**](ListingConditionsApi.md#listingConditionsGet) | **GET** /listing_conditions | List of supported product conditions |


<a id="listingConditionsGet"></a>
# **listingConditionsGet**
> listingConditionsGet()

List of supported product conditions

List of supported product conditions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ListingConditionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    ListingConditionsApi apiInstance = new ListingConditionsApi(defaultClient);
    try {
      apiInstance.listingConditionsGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling ListingConditionsApi#listingConditionsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

