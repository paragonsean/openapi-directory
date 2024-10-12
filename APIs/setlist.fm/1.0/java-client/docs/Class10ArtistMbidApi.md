# Class10ArtistMbidApi

All URIs are relative to */rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resource10ArtistMbidGetArtistGET**](Class10ArtistMbidApi.md#resource10ArtistMbidGetArtistGET) | **GET** /1.0/artist/{mbid} | . |


<a id="resource10ArtistMbidGetArtistGET"></a>
# **resource10ArtistMbidGetArtistGET**
> JsonArtist resource10ArtistMbidGetArtistGET(mbid)

.

&lt;p&gt; Returns an artist for a given Musicbrainz MBID &lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class10ArtistMbidApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/rest");

    Class10ArtistMbidApi apiInstance = new Class10ArtistMbidApi(defaultClient);
    String mbid = "mbid_example"; // String | a Musicbrainz MBID, e.g. 0bfba3d3-6a04-4779-bb0a-df07df5b0558
    try {
      JsonArtist result = apiInstance.resource10ArtistMbidGetArtistGET(mbid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class10ArtistMbidApi#resource10ArtistMbidGetArtistGET");
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
| **mbid** | **String**| a Musicbrainz MBID, e.g. 0bfba3d3-6a04-4779-bb0a-df07df5b0558 | |

### Return type

[**JsonArtist**](JsonArtist.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

