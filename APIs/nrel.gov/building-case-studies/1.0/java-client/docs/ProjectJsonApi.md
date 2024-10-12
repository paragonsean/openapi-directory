# ProjectJsonApi

All URIs are relative to *http://localhost/api/building-case-studies*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**document**](ProjectJsonApi.md#document) | **GET** /project/{project_id}.{output_format} | Project Details |
| [**project**](ProjectJsonApi.md#project) | **GET** /project.{output_format} | A filterable list of projects. |


<a id="document"></a>
# **document**
> document(outputFormat, apiKey, projectId)

Project Details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectJsonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost/api/building-case-studies");

    ProjectJsonApi apiInstance = new ProjectJsonApi(defaultClient);
    String outputFormat = "json"; // String | Response Format
    String apiKey = "DEMO_KEY"; // String | API Key
    Integer projectId = 56; // Integer | Project ID
    try {
      apiInstance.document(outputFormat, apiKey, projectId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectJsonApi#document");
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
| **outputFormat** | **String**| Response Format | [default to json] [enum: json, xml] |
| **apiKey** | **String**| API Key | [default to DEMO_KEY] |
| **projectId** | **Integer**| Project ID | |

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
| **200** | Successful request |  -  |

<a id="project"></a>
# **project**
> project(outputFormat, apiKey, search, portal, page, city, province, region)

A filterable list of projects.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProjectJsonApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost/api/building-case-studies");

    ProjectJsonApi apiInstance = new ProjectJsonApi(defaultClient);
    String outputFormat = "json"; // String | Response Format
    String apiKey = "DEMO_KEY"; // String | API Key
    String search = "search_example"; // String | Search Text
    String portal = "portal_example"; // String | Portal ID
    Integer page = 56; // Integer | Page Number
    String city = "city_example"; // String | City
    String province = "province_example"; // String | State or Province (ex: 'CO', 'AZ')
    String region = "region_example"; // String | Climate Region.  Use integer from mapping (256: '1A: Very Hot - Humid', 257: '1B: Very Hot - Dry', 258: '2A: Hot - Humid', 259: '2B: Hot - Dry', 260: '3A: Warm - Humid', 261: '3B: Warm - Dry', 262: '3C: Warm - Marine', 263: '4A: Mixed - Humid', 264: '4B: Mixed - Dry', 265: '4C: Mixed - Marine', 266: '5A: Cool - Humid', 267: '5B: Cool - Dry', 268: '5C: Cool - Marine', 269: '6A: Cold - Humid', 270: '6B: Cold - Dry', 271: '7: Very Cold', 272: '8: Subarctic')
    try {
      apiInstance.project(outputFormat, apiKey, search, portal, page, city, province, region);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProjectJsonApi#project");
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
| **outputFormat** | **String**| Response Format | [default to xml] [enum: json, xml] |
| **apiKey** | **String**| API Key | [default to DEMO_KEY] |
| **search** | **String**| Search Text | [optional] |
| **portal** | **String**| Portal ID | [optional] |
| **page** | **Integer**| Page Number | [optional] |
| **city** | **String**| City | [optional] |
| **province** | **String**| State or Province (ex: &#39;CO&#39;, &#39;AZ&#39;) | [optional] |
| **region** | **String**| Climate Region.  Use integer from mapping (256: &#39;1A: Very Hot - Humid&#39;, 257: &#39;1B: Very Hot - Dry&#39;, 258: &#39;2A: Hot - Humid&#39;, 259: &#39;2B: Hot - Dry&#39;, 260: &#39;3A: Warm - Humid&#39;, 261: &#39;3B: Warm - Dry&#39;, 262: &#39;3C: Warm - Marine&#39;, 263: &#39;4A: Mixed - Humid&#39;, 264: &#39;4B: Mixed - Dry&#39;, 265: &#39;4C: Mixed - Marine&#39;, 266: &#39;5A: Cool - Humid&#39;, 267: &#39;5B: Cool - Dry&#39;, 268: &#39;5C: Cool - Marine&#39;, 269: &#39;6A: Cold - Humid&#39;, 270: &#39;6B: Cold - Dry&#39;, 271: &#39;7: Very Cold&#39;, 272: &#39;8: Subarctic&#39;) | [optional] |

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
| **200** | Successful request |  -  |

