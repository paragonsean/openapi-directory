# DefaultApi

All URIs are relative to *http://techport.nasa.gov/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiGet**](DefaultApi.md#apiGet) | **GET** /api |  |
| [**apiProjectsFormatGet**](DefaultApi.md#apiProjectsFormatGet) | **GET** /api/projects{.format} |  |
| [**apiProjectsIdFormatGet**](DefaultApi.md#apiProjectsIdFormatGet) | **GET** /api/projects/{id}{.format} |  |


<a id="apiGet"></a>
# **apiGet**
> apiGet()



Returns the swagger specification for the API.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://techport.nasa.gov/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    try {
      apiInstance.apiGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiGet");
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
| **200** | Successful response |  -  |
| **0** | Object not found. |  -  |

<a id="apiProjectsFormatGet"></a>
# **apiProjectsFormatGet**
> ApiProjectsFormatGet200Response apiProjectsFormatGet(updatedSince, format, format2)



Returns a list of available technology project IDs.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://techport.nasa.gov/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    LocalDate updatedSince = LocalDate.now(); // LocalDate | ISO 8601 full-date in the format YYYY-MM-DD. Filters the list of available ID values by their lastUpdated parameter.
    String format = "json"; // String | The response type desired.
    String format2 = "format_example"; // String | Automatically added
    try {
      ApiProjectsFormatGet200Response result = apiInstance.apiProjectsFormatGet(updatedSince, format, format2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiProjectsFormatGet");
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
| **updatedSince** | **LocalDate**| ISO 8601 full-date in the format YYYY-MM-DD. Filters the list of available ID values by their lastUpdated parameter. | |
| **format** | **String**| The response type desired. | [default to json] [enum: json, xml] |
| **format2** | **String**| Automatically added | |

### Return type

[**ApiProjectsFormatGet200Response**](ApiProjectsFormatGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **0** | Object not found. |  -  |

<a id="apiProjectsIdFormatGet"></a>
# **apiProjectsIdFormatGet**
> Project apiProjectsIdFormatGet(id, format, format2)



Returns information about a specific technology project.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://techport.nasa.gov/api");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    Long id = 56L; // Long | ID of project to fetch
    String format = "json"; // String | The response type desired.
    String format2 = "format_example"; // String | Automatically added
    try {
      Project result = apiInstance.apiProjectsIdFormatGet(id, format, format2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#apiProjectsIdFormatGet");
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
| **id** | **Long**| ID of project to fetch | |
| **format** | **String**| The response type desired. | [default to xml] [enum: json, xml] |
| **format2** | **String**| Automatically added | |

### Return type

[**Project**](Project.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |
| **0** | Object not found. |  -  |

