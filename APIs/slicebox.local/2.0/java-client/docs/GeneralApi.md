# GeneralApi

All URIs are relative to *http://slicebox.local/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**destinationsGet**](GeneralApi.md#destinationsGet) | **GET** /destinations |  |
| [**sourcesGet**](GeneralApi.md#sourcesGet) | **GET** /sources |  |
| [**systemHealthGet**](GeneralApi.md#systemHealthGet) | **GET** /system/health |  |
| [**systemStopPost**](GeneralApi.md#systemStopPost) | **POST** /system/stop |  |


<a id="destinationsGet"></a>
# **destinationsGet**
> List&lt;Destination&gt; destinationsGet()



Returns a list of currently available destinations. Possible destinations are box - sending data to a remote box, and scu - sending data a receiving SCP.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    try {
      List<Destination> result = apiInstance.destinationsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#destinationsGet");
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

[**List&lt;Destination&gt;**](Destination.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | currently available destinations |  -  |

<a id="sourcesGet"></a>
# **sourcesGet**
> List&lt;Source&gt; sourcesGet()



Returns a list of currently available data sources. Possible source types are user - data imported by an API call by a user, box - data received from a remote box, directory - data imported via a watched directory, import - data imported into slicebox using import sessions, or scp - data received from a PACS.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    try {
      List<Source> result = apiInstance.sourcesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#sourcesGet");
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

[**List&lt;Source&gt;**](Source.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | currently available sources |  -  |

<a id="systemHealthGet"></a>
# **systemHealthGet**
> systemHealthGet()



No-op route for checking whether the service is alive or not

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    try {
      apiInstance.systemHealthGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#systemHealthGet");
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
| **200** | The service is up and running |  -  |

<a id="systemStopPost"></a>
# **systemStopPost**
> systemStopPost()



stop and shut down slicebox

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeneralApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://slicebox.local/api");

    GeneralApi apiInstance = new GeneralApi(defaultClient);
    try {
      apiInstance.systemStopPost();
    } catch (ApiException e) {
      System.err.println("Exception when calling GeneralApi#systemStopPost");
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
| **200** | shutdown message |  -  |

