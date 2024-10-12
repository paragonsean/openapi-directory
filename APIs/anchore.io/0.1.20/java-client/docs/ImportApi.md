# ImportApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**importImageArchive**](ImportApi.md#importImageArchive) | **POST** /import/images | Import an anchore image tar.gz archive file. This is a deprecated API replaced by the \&quot;/imports/images\&quot; route |


<a id="importImageArchive"></a>
# **importImageArchive**
> List&lt;AnchoreImage&gt; importImageArchive(archiveFile)

Import an anchore image tar.gz archive file. This is a deprecated API replaced by the \&quot;/imports/images\&quot; route

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ImportApi apiInstance = new ImportApi(defaultClient);
    File archiveFile = new File("/path/to/file"); // File | anchore image tar archive.
    try {
      List<AnchoreImage> result = apiInstance.importImageArchive(archiveFile);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportApi#importImageArchive");
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
| **archiveFile** | **File**| anchore image tar archive. | |

### Return type

[**List&lt;AnchoreImage&gt;**](AnchoreImage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully imported image to the engine |  -  |
| **500** | Internal Error |  -  |

