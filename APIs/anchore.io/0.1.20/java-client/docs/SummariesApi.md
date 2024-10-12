# SummariesApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listImagetags**](SummariesApi.md#listImagetags) | **GET** /summaries/imagetags | List all visible image digests and tags |


<a id="listImagetags"></a>
# **listImagetags**
> List&lt;AnchoreImageTagSummary&gt; listImagetags(imageStatus, xAnchoreAccount)

List all visible image digests and tags

List all image tags visible to the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SummariesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SummariesApi apiInstance = new SummariesApi(defaultClient);
    List<String> imageStatus = Arrays.asList(); // List<String> | Filter images in one or more states such as active, deleting. Defaults to active images only if unspecified
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      List<AnchoreImageTagSummary> result = apiInstance.listImagetags(imageStatus, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SummariesApi#listImagetags");
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
| **imageStatus** | [**List&lt;String&gt;**](String.md)| Filter images in one or more states such as active, deleting. Defaults to active images only if unspecified | [optional] [enum: all, active, deleting] |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**List&lt;AnchoreImageTagSummary&gt;**](AnchoreImageTagSummary.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **500** | Internal Error |  -  |

