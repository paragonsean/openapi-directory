# ArtifactTypeApi

All URIs are relative to *http://apicurio.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listArtifactTypes**](ArtifactTypeApi.md#listArtifactTypes) | **GET** /admin/artifactTypes | List artifact types |


<a id="listArtifactTypes"></a>
# **listArtifactTypes**
> List&lt;ArtifactTypeInfo&gt; listArtifactTypes()

List artifact types

Gets a list of all the configured artifact types.  This operation can fail for the following reasons:  * A server error occurred (HTTP error &#x60;500&#x60;) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtifactTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://apicurio.local");

    ArtifactTypeApi apiInstance = new ArtifactTypeApi(defaultClient);
    try {
      List<ArtifactTypeInfo> result = apiInstance.listArtifactTypes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtifactTypeApi#listArtifactTypes");
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

[**List&lt;ArtifactTypeInfo&gt;**](ArtifactTypeInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of available artifact types. |  -  |
| **500** | Common response for all operations that can fail with an unexpected server error. |  -  |

