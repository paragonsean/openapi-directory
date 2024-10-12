# HackathonsApi

All URIs are relative to *http://www.hackathonwatch.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**gETHackathonsComingFormat**](HackathonsApi.md#gETHackathonsComingFormat) | **GET** /hackathons/coming.json | Return a list of coming hackathons |
| [**gETHackathonsIdFormat**](HackathonsApi.md#gETHackathonsIdFormat) | **GET** /hackathons/{id}.json | Return the detail of a given hackathon |


<a id="gETHackathonsComingFormat"></a>
# **gETHackathonsComingFormat**
> gETHackathonsComingFormat(page)

Return a list of coming hackathons

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HackathonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.hackathonwatch.com/api");

    HackathonsApi apiInstance = new HackathonsApi(defaultClient);
    Integer page = 1; // Integer | Specify the page of coming hackathons.
    try {
      apiInstance.gETHackathonsComingFormat(page);
    } catch (ApiException e) {
      System.err.println("Exception when calling HackathonsApi#gETHackathonsComingFormat");
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
| **page** | **Integer**| Specify the page of coming hackathons. | [optional] [default to 1] |

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
| **200** | No response was specified |  -  |

<a id="gETHackathonsIdFormat"></a>
# **gETHackathonsIdFormat**
> gETHackathonsIdFormat(id)

Return the detail of a given hackathon

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HackathonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.hackathonwatch.com/api");

    HackathonsApi apiInstance = new HackathonsApi(defaultClient);
    Integer id = 56; // Integer | ID of the hackathon for detail information
    try {
      apiInstance.gETHackathonsIdFormat(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling HackathonsApi#gETHackathonsIdFormat");
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
| **id** | **Integer**| ID of the hackathon for detail information | |

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
| **200** | No response was specified |  -  |

