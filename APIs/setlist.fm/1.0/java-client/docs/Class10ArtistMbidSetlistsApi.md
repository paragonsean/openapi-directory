# Class10ArtistMbidSetlistsApi

All URIs are relative to */rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resource10ArtistMbidSetlistsGetArtistSetlistsGET**](Class10ArtistMbidSetlistsApi.md#resource10ArtistMbidSetlistsGetArtistSetlistsGET) | **GET** /1.0/artist/{mbid}/setlists | . |


<a id="resource10ArtistMbidSetlistsGetArtistSetlistsGET"></a>
# **resource10ArtistMbidSetlistsGetArtistSetlistsGET**
> JsonSetlists resource10ArtistMbidSetlistsGetArtistSetlistsGET(mbid, p)

.

&lt;p&gt; Get a list of an artist&#39;s setlists. &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class10ArtistMbidSetlistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/rest");

    Class10ArtistMbidSetlistsApi apiInstance = new Class10ArtistMbidSetlistsApi(defaultClient);
    String mbid = "mbid_example"; // String | the Musicbrainz MBID of the artist
    Integer p = 1; // Integer | the number of the result page
    try {
      JsonSetlists result = apiInstance.resource10ArtistMbidSetlistsGetArtistSetlistsGET(mbid, p);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class10ArtistMbidSetlistsApi#resource10ArtistMbidSetlistsGetArtistSetlistsGET");
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
| **mbid** | **String**| the Musicbrainz MBID of the artist | |
| **p** | **Integer**| the number of the result page | [optional] [default to 1] |

### Return type

[**JsonSetlists**](JsonSetlists.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

