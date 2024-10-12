# ImageRegionProposalApiApi

All URIs are relative to *https://southcentralus.api.cognitive.microsoft.com/customvision/v2.0/Training*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getImageRegionProposals**](ImageRegionProposalApiApi.md#getImageRegionProposals) | **POST** /{projectId}/images/{imageId}/regionproposals | Get region proposals for an image. Returns empty array if no proposals are found. |


<a id="getImageRegionProposals"></a>
# **getImageRegionProposals**
> ImageRegionProposal getImageRegionProposals(projectId, imageId, trainingKey)

Get region proposals for an image. Returns empty array if no proposals are found.

This API will get region proposals for an image along with confidences for the region. It returns an empty array if no proposals are found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImageRegionProposalApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v2.0/Training");

    ImageRegionProposalApiApi apiInstance = new ImageRegionProposalApiApi(defaultClient);
    UUID projectId = UUID.fromString("bc3f7dad-5544-468c-8573-3ef04d55463e"); // UUID | The project id
    UUID imageId = UUID.fromString("4d6eb844-42ee-42bc-bd6f-c32455ef07c9"); // UUID | The image id
    String trainingKey = "{API Key}"; // String | 
    try {
      ImageRegionProposal result = apiInstance.getImageRegionProposals(projectId, imageId, trainingKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImageRegionProposalApiApi#getImageRegionProposals");
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
| **projectId** | **UUID**| The project id | |
| **imageId** | **UUID**| The image id | |
| **trainingKey** | **String**|  | |

### Return type

[**ImageRegionProposal**](ImageRegionProposal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

