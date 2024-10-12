# CourseDesignsApi

All URIs are relative to *http://learnifier.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**coursedesignsGet**](CourseDesignsApi.md#coursedesignsGet) | **GET** /coursedesigns | Lists all global course design templates |


<a id="coursedesignsGet"></a>
# **coursedesignsGet**
> List&lt;CourseDesign&gt; coursedesignsGet()

Lists all global course design templates

Lists all global course design templates. Only api callers that have full access can call this method.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CourseDesignsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://learnifier.com");

    CourseDesignsApi apiInstance = new CourseDesignsApi(defaultClient);
    try {
      List<CourseDesign> result = apiInstance.coursedesignsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CourseDesignsApi#coursedesignsGet");
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

[**List&lt;CourseDesign&gt;**](CourseDesign.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List with course design templates |  -  |
| **0** | Unexpected error |  -  |

