# CommunityContentApi

All URIs are relative to *https://www.bungie.net/Platform*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**communityContentGetCommunityContent**](CommunityContentApi.md#communityContentGetCommunityContent) | **GET** /CommunityContent/Get/{sort}/{mediaFilter}/{page}/ |  |


<a id="communityContentGetCommunityContent"></a>
# **communityContentGetCommunityContent**
> CommunityContentGetCommunityContent200Response communityContentGetCommunityContent(mediaFilter, page, sort)



Returns community content.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommunityContentApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    CommunityContentApi apiInstance = new CommunityContentApi(defaultClient);
    Integer mediaFilter = 56; // Integer | The type of media to get
    Integer page = 56; // Integer | Zero based page
    Integer sort = 56; // Integer | The sort mode.
    try {
      CommunityContentGetCommunityContent200Response result = apiInstance.communityContentGetCommunityContent(mediaFilter, page, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommunityContentApi#communityContentGetCommunityContent");
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
| **mediaFilter** | **Integer**| The type of media to get | |
| **page** | **Integer**| Zero based page | |
| **sort** | **Integer**| The sort mode. | |

### Return type

[**CommunityContentGetCommunityContent200Response**](CommunityContentGetCommunityContent200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

