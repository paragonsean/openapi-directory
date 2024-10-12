# InfoApi

All URIs are relative to *https://api.contribly.com/1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**artifactFormatsGet**](InfoApi.md#artifactFormatsGet) | **GET** /artifact-formats | Artifact formats |
| [**changeLogGet**](InfoApi.md#changeLogGet) | **GET** /change-log | Recent changes |
| [**eventTypesGet**](InfoApi.md#eventTypesGet) | **GET** /event-types | Event types |


<a id="artifactFormatsGet"></a>
# **artifactFormatsGet**
> ArtifactFormats artifactFormatsGet()

Artifact formats

List the available artifact formats

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    InfoApi apiInstance = new InfoApi(defaultClient);
    try {
      ArtifactFormats result = apiInstance.artifactFormatsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfoApi#artifactFormatsGet");
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

[**ArtifactFormats**](ArtifactFormats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of artifact formats |  -  |

<a id="changeLogGet"></a>
# **changeLogGet**
> List&lt;ChangeLogItem&gt; changeLogGet()

Recent changes

The Contribly change log.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    InfoApi apiInstance = new InfoApi(defaultClient);
    try {
      List<ChangeLogItem> result = apiInstance.changeLogGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfoApi#changeLogGet");
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

[**List&lt;ChangeLogItem&gt;**](ChangeLogItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of change log items |  -  |

<a id="eventTypesGet"></a>
# **eventTypesGet**
> List&lt;EventType&gt; eventTypesGet()

Event types

List available notification event types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.contribly.com/1");

    InfoApi apiInstance = new InfoApi(defaultClient);
    try {
      List<EventType> result = apiInstance.eventTypesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InfoApi#eventTypesGet");
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

[**List&lt;EventType&gt;**](EventType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of event types |  -  |

