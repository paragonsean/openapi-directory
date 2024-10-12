# SectionApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiSectionSectionIdGet**](SectionApi.md#apiSectionSectionIdGet) | **GET** /api/Section/{sectionId} | Returns a section by section id. |
| [**apiSectionSectionIdstepGet**](SectionApi.md#apiSectionSectionIdstepGet) | **GET** /api/Section/{sectionId},{step} | Returns a section overview by section id and step. |


<a id="apiSectionSectionIdGet"></a>
# **apiSectionSectionIdGet**
> ErskineMaySectionDetail apiSectionSectionIdGet(sectionId)

Returns a section by section id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SectionApi apiInstance = new SectionApi(defaultClient);
    Integer sectionId = 56; // Integer | Section by id.
    try {
      ErskineMaySectionDetail result = apiInstance.apiSectionSectionIdGet(sectionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SectionApi#apiSectionSectionIdGet");
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
| **sectionId** | **Integer**| Section by id. | |

### Return type

[**ErskineMaySectionDetail**](ErskineMaySectionDetail.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiSectionSectionIdstepGet"></a>
# **apiSectionSectionIdstepGet**
> ErskineMaySectionOverview apiSectionSectionIdstepGet(sectionId, step)

Returns a section overview by section id and step.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SectionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    SectionApi apiInstance = new SectionApi(defaultClient);
    Integer sectionId = 56; // Integer | Section by id.
    Integer step = 56; // Integer | Number of sections to step over from given section.
    try {
      ErskineMaySectionOverview result = apiInstance.apiSectionSectionIdstepGet(sectionId, step);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SectionApi#apiSectionSectionIdstepGet");
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
| **sectionId** | **Integer**| Section by id. | |
| **step** | **Integer**| Number of sections to step over from given section. | |

### Return type

[**ErskineMaySectionOverview**](ErskineMaySectionOverview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

