# SegmentApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSegment**](SegmentApi.md#getSegment) | **GET** /segments | Get Segment |


<a id="getSegment"></a>
# **getSegment**
> getSegment()

Get Segment

You can add certain public fields in the query string and the system will attempt to fulfill it. Values such as &#x60;cultureInfo&#x60; and &#x60;utm&#x60; are overwriteable, just keep in mind such changes will not be reflected in the client&#39;s session.    If you wish to change the value on the session (and thus be reflected on the segment without special query strings), then use the PATCH request to session.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SegmentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    SegmentApi apiInstance = new SegmentApi(defaultClient);
    try {
      apiInstance.getSegment();
    } catch (ApiException e) {
      System.err.println("Exception when calling SegmentApi#getSegment");
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
| **200** |  |  -  |

