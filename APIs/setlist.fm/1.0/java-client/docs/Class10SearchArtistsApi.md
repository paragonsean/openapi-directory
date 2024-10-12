# Class10SearchArtistsApi

All URIs are relative to */rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resource10SearchArtistsGetArtistsGET**](Class10SearchArtistsApi.md#resource10SearchArtistsGetArtistsGET) | **GET** /1.0/search/artists | Search for artists. |


<a id="resource10SearchArtistsGetArtistsGET"></a>
# **resource10SearchArtistsGetArtistsGET**
> JsonArtists resource10SearchArtistsGetArtistsGET(artistMbid, artistName, artistTmid, p, sort)

Search for artists.

Search for artists.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class10SearchArtistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/rest");

    Class10SearchArtistsApi apiInstance = new Class10SearchArtistsApi(defaultClient);
    String artistMbid = "artistMbid_example"; // String | the artist's Musicbrainz Identifier (mbid)
    String artistName = "artistName_example"; // String | the artist's name
    Integer artistTmid = 56; // Integer | the artist's Ticketmaster Identifier (tmid)
    Integer p = 1; // Integer | the number of the result page you'd like to have
    String sort = "sortName"; // String | the sort of the result, either sortName (default) or relevance
    try {
      JsonArtists result = apiInstance.resource10SearchArtistsGetArtistsGET(artistMbid, artistName, artistTmid, p, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class10SearchArtistsApi#resource10SearchArtistsGetArtistsGET");
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
| **artistMbid** | **String**| the artist&#39;s Musicbrainz Identifier (mbid) | [optional] |
| **artistName** | **String**| the artist&#39;s name | [optional] |
| **artistTmid** | **Integer**| the artist&#39;s Ticketmaster Identifier (tmid) | [optional] |
| **p** | **Integer**| the number of the result page you&#39;d like to have | [optional] [default to 1] |
| **sort** | **String**| the sort of the result, either sortName (default) or relevance | [optional] [default to sortName] |

### Return type

[**JsonArtists**](JsonArtists.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

