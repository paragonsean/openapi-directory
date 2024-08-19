# DefaultApi

All URIs are relative to *https://crossbrowsertesting.com/api/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**screenshotsTargetScreenshotTestIdTargetVersionIdComparisonBaseResultIdGet**](DefaultApi.md#screenshotsTargetScreenshotTestIdTargetVersionIdComparisonBaseResultIdGet) | **GET** /screenshots/{target_screenshot_test_id}/{target_version_id}/comparison/{base_result_id} | Compare Full Screenshot Test |
| [**screenshotsTargetScreenshotTestIdTargetVersionIdComparisonParallelBaseVersionIdGet**](DefaultApi.md#screenshotsTargetScreenshotTestIdTargetVersionIdComparisonParallelBaseVersionIdGet) | **GET** /screenshots/{target_screenshot_test_id}/{target_version_id}/comparison/parallel/{base_version_id} | Compare Screenshot Test Versions |
| [**screenshotsTargetScreenshotTestIdTargetVersionIdTargetResultIdComparisonBaseResultIdGet**](DefaultApi.md#screenshotsTargetScreenshotTestIdTargetVersionIdTargetResultIdComparisonBaseResultIdGet) | **GET** /screenshots/{target_screenshot_test_id}/{target_version_id}/{target_result_id}/comparison/{base_result_id} | Compare Single Screenshot |


<a id="screenshotsTargetScreenshotTestIdTargetVersionIdComparisonBaseResultIdGet"></a>
# **screenshotsTargetScreenshotTestIdTargetVersionIdComparisonBaseResultIdGet**
> FullComparisonTest screenshotsTargetScreenshotTestIdTargetVersionIdComparisonBaseResultIdGet(targetScreenshotTestId, targetVersionId, baseResultId, format, paramCallback, tolerance)

Compare Full Screenshot Test

Get comparison results for all browsers in target screenshot test against a base screenshot result. The base result can be from the same test or from another test run at an earlier time. This is a one-to-many comparison.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://crossbrowsertesting.com/api/v3");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer targetScreenshotTestId = 56; // Integer | test id of the target Screenshot Test
    Integer targetVersionId = 56; // Integer | version id of the target Screenshot Test
    Integer baseResultId = 56; // Integer | result id of the base Screenshot Test
    String format = "json"; // String | The format of the returned data. Possible values are \"json\" or \"jsonp\".
    String paramCallback = "paramCallback_example"; // String | Name of callback method for JSONP requests.
    BigDecimal tolerance = new BigDecimal("30"); // BigDecimal | Used as the basis for detecting box model differences in element positioning and dimensions that should be flagged and reported back to the comparison results. The default is 30px which is a good basis for finding notable layout differences.
    try {
      FullComparisonTest result = apiInstance.screenshotsTargetScreenshotTestIdTargetVersionIdComparisonBaseResultIdGet(targetScreenshotTestId, targetVersionId, baseResultId, format, paramCallback, tolerance);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#screenshotsTargetScreenshotTestIdTargetVersionIdComparisonBaseResultIdGet");
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
| **targetScreenshotTestId** | **Integer**| test id of the target Screenshot Test | |
| **targetVersionId** | **Integer**| version id of the target Screenshot Test | |
| **baseResultId** | **Integer**| result id of the base Screenshot Test | |
| **format** | **String**| The format of the returned data. Possible values are \&quot;json\&quot; or \&quot;jsonp\&quot;. | [optional] [default to json] |
| **paramCallback** | **String**| Name of callback method for JSONP requests. | [optional] |
| **tolerance** | **BigDecimal**| Used as the basis for detecting box model differences in element positioning and dimensions that should be flagged and reported back to the comparison results. The default is 30px which is a good basis for finding notable layout differences. | [optional] [default to 30] |

### Return type

[**FullComparisonTest**](FullComparisonTest.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of Configuration objects. Within each configuration is an array of browsers |  -  |

<a id="screenshotsTargetScreenshotTestIdTargetVersionIdComparisonParallelBaseVersionIdGet"></a>
# **screenshotsTargetScreenshotTestIdTargetVersionIdComparisonParallelBaseVersionIdGet**
> List&lt;SingleComparisonTest&gt; screenshotsTargetScreenshotTestIdTargetVersionIdComparisonParallelBaseVersionIdGet(targetScreenshotTestId, targetVersionId, baseVersionId, format, paramCallback, tolerance)

Compare Screenshot Test Versions

Get comparison results for all browsers in target screenshot test against the same browser in the base screenshot test. This is a good method for regression testing. For example, you&#39;ve run a screenshot test against a set of browsers that is \&quot;good\&quot;. Then, after some changes, you run a new screenshot test against the same set of browsers. This method will compare each of the same browsers against each other. For example, IE9 will be compared to IE9 from an earlier test. This is a many-to-many comparison where the OS/Browser/Resolution must match between the two test versions in order for the comparison to return results. The two versions can be from the same screenshot_test_id or not.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://crossbrowsertesting.com/api/v3");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer targetScreenshotTestId = 56; // Integer | test id of the target Screenshot Test
    Integer targetVersionId = 56; // Integer | version id of the target Screenshot Test
    Integer baseVersionId = 56; // Integer | version id of the base Screenshot Test
    String format = "json"; // String | The format of the returned data. Possible values are \"json\" or \"jsonp\".
    String paramCallback = "paramCallback_example"; // String | Name of callback method for JSONP requests.
    BigDecimal tolerance = new BigDecimal("30"); // BigDecimal | Used as the basis for detecting box model differences in element positioning and dimensions that should be flagged and reported back to the comparison results. The default is 30px which is a good basis for finding notable layout differences.
    try {
      List<SingleComparisonTest> result = apiInstance.screenshotsTargetScreenshotTestIdTargetVersionIdComparisonParallelBaseVersionIdGet(targetScreenshotTestId, targetVersionId, baseVersionId, format, paramCallback, tolerance);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#screenshotsTargetScreenshotTestIdTargetVersionIdComparisonParallelBaseVersionIdGet");
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
| **targetScreenshotTestId** | **Integer**| test id of the target Screenshot Test | |
| **targetVersionId** | **Integer**| version id of the target Screenshot Test | |
| **baseVersionId** | **Integer**| version id of the base Screenshot Test | |
| **format** | **String**| The format of the returned data. Possible values are \&quot;json\&quot; or \&quot;jsonp\&quot;. | [optional] [default to json] |
| **paramCallback** | **String**| Name of callback method for JSONP requests. | [optional] |
| **tolerance** | **BigDecimal**| Used as the basis for detecting box model differences in element positioning and dimensions that should be flagged and reported back to the comparison results. The default is 30px which is a good basis for finding notable layout differences. | [optional] [default to 30] |

### Return type

[**List&lt;SingleComparisonTest&gt;**](SingleComparisonTest.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of Configuration objects. Within each configuration is an array of browsers |  -  |

<a id="screenshotsTargetScreenshotTestIdTargetVersionIdTargetResultIdComparisonBaseResultIdGet"></a>
# **screenshotsTargetScreenshotTestIdTargetVersionIdTargetResultIdComparisonBaseResultIdGet**
> SingleComparisonTest screenshotsTargetScreenshotTestIdTargetVersionIdTargetResultIdComparisonBaseResultIdGet(targetScreenshotTestId, targetVersionId, targetResultId, baseResultId, format, paramCallback, tolerance)

Compare Single Screenshot

Get comparison results for a single target screenshot result against a base screenshot result. This is a one-to-one comparison.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://crossbrowsertesting.com/api/v3");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Integer targetScreenshotTestId = 56; // Integer | test id of the target Screenshot Test
    Integer targetVersionId = 56; // Integer | version id of the target Screenshot Test
    Integer targetResultId = 56; // Integer | result id of the target Screenshot Test
    Integer baseResultId = 56; // Integer | result id of the base Screenshot Test
    String format = "json"; // String | The format of the returned data. Possible values are \"json\" or \"jsonp\".
    String paramCallback = "paramCallback_example"; // String | Name of callback method for JSONP requests.
    BigDecimal tolerance = new BigDecimal("30"); // BigDecimal | Used as the basis for detecting box model differences in element positioning and dimensions that should be flagged and reported back to the comparison results. The default is 30px which is a good basis for finding notable layout differences.
    try {
      SingleComparisonTest result = apiInstance.screenshotsTargetScreenshotTestIdTargetVersionIdTargetResultIdComparisonBaseResultIdGet(targetScreenshotTestId, targetVersionId, targetResultId, baseResultId, format, paramCallback, tolerance);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#screenshotsTargetScreenshotTestIdTargetVersionIdTargetResultIdComparisonBaseResultIdGet");
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
| **targetScreenshotTestId** | **Integer**| test id of the target Screenshot Test | |
| **targetVersionId** | **Integer**| version id of the target Screenshot Test | |
| **targetResultId** | **Integer**| result id of the target Screenshot Test | |
| **baseResultId** | **Integer**| result id of the base Screenshot Test | |
| **format** | **String**| The format of the returned data. Possible values are \&quot;json\&quot; or \&quot;jsonp\&quot;. | [optional] [default to json] |
| **paramCallback** | **String**| Name of callback method for JSONP requests. | [optional] |
| **tolerance** | **BigDecimal**| Used as the basis for detecting box model differences in element positioning and dimensions that should be flagged and reported back to the comparison results. The default is 30px which is a good basis for finding notable layout differences. | [optional] [default to 30] |

### Return type

[**SingleComparisonTest**](SingleComparisonTest.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of Configuration objects. Within each configuration is an array of browsers |  -  |

