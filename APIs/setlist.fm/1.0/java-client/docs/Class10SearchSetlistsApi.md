# Class10SearchSetlistsApi

All URIs are relative to */rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**resource10SearchSetlistsGetSetlistsGET**](Class10SearchSetlistsApi.md#resource10SearchSetlistsGetSetlistsGET) | **GET** /1.0/search/setlists | Search for setlists. |


<a id="resource10SearchSetlistsGetSetlistsGET"></a>
# **resource10SearchSetlistsGetSetlistsGET**
> JsonSetlists resource10SearchSetlistsGetSetlistsGET(artistMbid, artistName, artistTmid, cityId, cityName, countryCode, date, lastFm, lastUpdated, p, state, stateCode, tourName, venueId, venueName, year)

Search for setlists.

Search for setlists.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class10SearchSetlistsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/rest");

    Class10SearchSetlistsApi apiInstance = new Class10SearchSetlistsApi(defaultClient);
    String artistMbid = "artistMbid_example"; // String | the artist's Musicbrainz Identifier (mbid)
    String artistName = "artistName_example"; // String | the artist's name
    Integer artistTmid = 56; // Integer | the artist's Ticketmaster Identifier (tmid)
    String cityId = "cityId_example"; // String | the city's geoId
    String cityName = "cityName_example"; // String | the name of the city
    String countryCode = "countryCode_example"; // String | the country code
    String date = "date_example"; // String | the date of the event (format dd-MM-yyyy)
    Integer lastFm = 56; // Integer | the event's Last.fm Event ID (deprecated)
    String lastUpdated = "lastUpdated_example"; // String | the date and time (UTC) when this setlist was last updated (format yyyyMMddHHmmss) - either edited or reverted. search will return setlists that were updated on or after this date
    Integer p = 1; // Integer | the number of the result page
    String state = "state_example"; // String | the state
    String stateCode = "stateCode_example"; // String | the state code
    String tourName = "tourName_example"; // String | 
    String venueId = "venueId_example"; // String | the venue id
    String venueName = "venueName_example"; // String | the name of the venue
    String year = "year_example"; // String | the year of the event
    try {
      JsonSetlists result = apiInstance.resource10SearchSetlistsGetSetlistsGET(artistMbid, artistName, artistTmid, cityId, cityName, countryCode, date, lastFm, lastUpdated, p, state, stateCode, tourName, venueId, venueName, year);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class10SearchSetlistsApi#resource10SearchSetlistsGetSetlistsGET");
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
| **cityId** | **String**| the city&#39;s geoId | [optional] |
| **cityName** | **String**| the name of the city | [optional] |
| **countryCode** | **String**| the country code | [optional] |
| **date** | **String**| the date of the event (format dd-MM-yyyy) | [optional] |
| **lastFm** | **Integer**| the event&#39;s Last.fm Event ID (deprecated) | [optional] |
| **lastUpdated** | **String**| the date and time (UTC) when this setlist was last updated (format yyyyMMddHHmmss) - either edited or reverted. search will return setlists that were updated on or after this date | [optional] |
| **p** | **Integer**| the number of the result page | [optional] [default to 1] |
| **state** | **String**| the state | [optional] |
| **stateCode** | **String**| the state code | [optional] |
| **tourName** | **String**|  | [optional] |
| **venueId** | **String**| the venue id | [optional] |
| **venueName** | **String**| the name of the venue | [optional] |
| **year** | **String**| the year of the event | [optional] |

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

