# SeriesMembershipApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSeriesMemberships**](SeriesMembershipApi.md#getSeriesMemberships) | **GET** /api/SeriesMembership | Returns all series memberships. |


<a id="getSeriesMemberships"></a>
# **getSeriesMemberships**
> SeriesMembershipResourceCollection getSeriesMemberships()

Returns all series memberships.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SeriesMembershipApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SeriesMembershipApi apiInstance = new SeriesMembershipApi(defaultClient);
    try {
      SeriesMembershipResourceCollection result = apiInstance.getSeriesMemberships();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SeriesMembershipApi#getSeriesMemberships");
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

[**SeriesMembershipResourceCollection**](SeriesMembershipResourceCollection.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

