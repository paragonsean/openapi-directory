# SchemasApi

All URIs are relative to */story*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**storyOutlineSchema**](SchemasApi.md#storyOutlineSchema) | **GET** /outline-schema/{schema_version}/story-outline.json | Story Outline Schema |


<a id="storyOutlineSchema"></a>
# **storyOutlineSchema**
> storyOutlineSchema(schemaVersion)

Story Outline Schema

Json Schema for validating Story Outline objects

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SchemasApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    SchemasApi apiInstance = new SchemasApi(defaultClient);
    String schemaVersion = "schemaVersion_example"; // String | The semanitic version of a schema (e.g. '0.3.1')
    try {
      apiInstance.storyOutlineSchema(schemaVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling SchemasApi#storyOutlineSchema");
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
| **schemaVersion** | **String**| The semanitic version of a schema (e.g. &#39;0.3.1&#39;) | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

