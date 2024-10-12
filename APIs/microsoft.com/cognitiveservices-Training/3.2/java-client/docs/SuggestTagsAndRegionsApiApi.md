# SuggestTagsAndRegionsApiApi

All URIs are relative to *https://southcentralus.api.cognitive.microsoft.com/customvision/v3.2/training*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**suggestTagsAndRegions**](SuggestTagsAndRegionsApiApi.md#suggestTagsAndRegions) | **POST** /projects/{projectId}/tagsandregions/suggestions | Suggest tags and regions for an array/batch of untagged images. Returns empty array if no tags are found. |


<a id="suggestTagsAndRegions"></a>
# **suggestTagsAndRegions**
> List&lt;SuggestedTagAndRegion&gt; suggestTagsAndRegions(projectId, iterationId, imageIds)

Suggest tags and regions for an array/batch of untagged images. Returns empty array if no tags are found.

This API will get suggested tags and regions for an array/batch of untagged images along with confidences for the tags. It returns an empty array if no tags are found.  There is a limit of 64 images in the batch.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SuggestTagsAndRegionsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.2/training");
    
    // Configure API key authorization: apim_key
    ApiKeyAuth apim_key = (ApiKeyAuth) defaultClient.getAuthentication("apim_key");
    apim_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apim_key.setApiKeyPrefix("Token");

    SuggestTagsAndRegionsApiApi apiInstance = new SuggestTagsAndRegionsApiApi(defaultClient);
    UUID projectId = UUID.fromString("bc3f7dad-5544-468c-8573-3ef04d55463e"); // UUID | The project id.
    UUID iterationId = UUID.fromString("4d6eb844-42ee-42bc-bd6f-c32455ef07c9"); // UUID | IterationId to use for tag and region suggestion.
    List<UUID> imageIds = Arrays.asList(); // List<UUID> | Array of image ids tag suggestion are needed for. Use GetUntaggedImages API to get imageIds.
    try {
      List<SuggestedTagAndRegion> result = apiInstance.suggestTagsAndRegions(projectId, iterationId, imageIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SuggestTagsAndRegionsApiApi#suggestTagsAndRegions");
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
| **projectId** | **UUID**| The project id. | |
| **iterationId** | **UUID**| IterationId to use for tag and region suggestion. | |
| **imageIds** | [**List&lt;UUID&gt;**](UUID.md)| Array of image ids tag suggestion are needed for. Use GetUntaggedImages API to get imageIds. | |

### Return type

[**List&lt;SuggestedTagAndRegion&gt;**](SuggestedTagAndRegion.md)

### Authorization

[apim_key](../README.md#apim_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

