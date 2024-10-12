# TypeUfoSightingsApi

All URIs are relative to *https://geodesystems.com:443*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchUfoSightings**](TypeUfoSightingsApi.md#searchUfoSightings) | **GET** /repository/search/type/ufo_sightings | Search API for &#39;Ufo Sightings&#39; entry type |


<a id="searchUfoSightings"></a>
# **searchUfoSightings**
> searchUfoSightings(text, name, description, fromdate, todate, createdateFrom, createdateTo, changedateFrom, changedateTo, group, filesuffix, maxlatitude, minlongitude, minlatitude, maxlongitude, max, skip, searchDbUfoSightingsDatetime, searchDbUfoSightingsCity, searchDbUfoSightingsState, searchDbUfoSightingsCountry, searchDbUfoSightingsShape, searchDbUfoSightingsDurationSeconds, searchDbUfoSightingsDurationHoursMin, searchDbUfoSightingsComments, searchDbUfoSightingsDatePosted, searchDbUfoSightingsLatitude, searchDbUfoSightingsLongitude)

Search API for &#39;Ufo Sightings&#39; entry type

API to search for entries of type Ufo Sightings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TypeUfoSightingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://geodesystems.com:443");

    TypeUfoSightingsApi apiInstance = new TypeUfoSightingsApi(defaultClient);
    String text = "text_example"; // String | Search text
    String name = "name_example"; // String | Search name
    String description = "description_example"; // String | Search description
    OffsetDateTime fromdate = OffsetDateTime.now(); // OffsetDateTime | From date
    OffsetDateTime todate = OffsetDateTime.now(); // OffsetDateTime | To date
    OffsetDateTime createdateFrom = OffsetDateTime.now(); // OffsetDateTime | Archive create date from
    OffsetDateTime createdateTo = OffsetDateTime.now(); // OffsetDateTime | Archive create date to
    OffsetDateTime changedateFrom = OffsetDateTime.now(); // OffsetDateTime | Archive change date from
    OffsetDateTime changedateTo = OffsetDateTime.now(); // OffsetDateTime | Archive change date to
    String group = "group_example"; // String | Parent entry
    String filesuffix = "filesuffix_example"; // String | File suffix
    Float maxlatitude = 3.4F; // Float | Northern bounds of search
    Float minlongitude = 3.4F; // Float | Western bounds of search
    Float minlatitude = 3.4F; // Float | Southern bounds of search
    Float maxlongitude = 3.4F; // Float | Eastern bounds of search
    Integer max = 56; // Integer | Max number of results
    Integer skip = 56; // Integer | Number to skip
    String searchDbUfoSightingsDatetime = "searchDbUfoSightingsDatetime_example"; // String | Datetime
    String searchDbUfoSightingsCity = "searchDbUfoSightingsCity_example"; // String | City
    String searchDbUfoSightingsState = "searchDbUfoSightingsState_example"; // String | State
    String searchDbUfoSightingsCountry = "searchDbUfoSightingsCountry_example"; // String | Country
    String searchDbUfoSightingsShape = "searchDbUfoSightingsShape_example"; // String | Shape
    Double searchDbUfoSightingsDurationSeconds = 3.4D; // Double | Duration (seconds)
    String searchDbUfoSightingsDurationHoursMin = "searchDbUfoSightingsDurationHoursMin_example"; // String | Duration (hours/min)
    String searchDbUfoSightingsComments = "searchDbUfoSightingsComments_example"; // String | Comments
    String searchDbUfoSightingsDatePosted = "searchDbUfoSightingsDatePosted_example"; // String | Date Posted
    Double searchDbUfoSightingsLatitude = 3.4D; // Double | Latitude
    Double searchDbUfoSightingsLongitude = 3.4D; // Double | Longitude
    try {
      apiInstance.searchUfoSightings(text, name, description, fromdate, todate, createdateFrom, createdateTo, changedateFrom, changedateTo, group, filesuffix, maxlatitude, minlongitude, minlatitude, maxlongitude, max, skip, searchDbUfoSightingsDatetime, searchDbUfoSightingsCity, searchDbUfoSightingsState, searchDbUfoSightingsCountry, searchDbUfoSightingsShape, searchDbUfoSightingsDurationSeconds, searchDbUfoSightingsDurationHoursMin, searchDbUfoSightingsComments, searchDbUfoSightingsDatePosted, searchDbUfoSightingsLatitude, searchDbUfoSightingsLongitude);
    } catch (ApiException e) {
      System.err.println("Exception when calling TypeUfoSightingsApi#searchUfoSightings");
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
| **text** | **String**| Search text | [optional] |
| **name** | **String**| Search name | [optional] |
| **description** | **String**| Search description | [optional] |
| **fromdate** | **OffsetDateTime**| From date | [optional] |
| **todate** | **OffsetDateTime**| To date | [optional] |
| **createdateFrom** | **OffsetDateTime**| Archive create date from | [optional] |
| **createdateTo** | **OffsetDateTime**| Archive create date to | [optional] |
| **changedateFrom** | **OffsetDateTime**| Archive change date from | [optional] |
| **changedateTo** | **OffsetDateTime**| Archive change date to | [optional] |
| **group** | **String**| Parent entry | [optional] |
| **filesuffix** | **String**| File suffix | [optional] |
| **maxlatitude** | **Float**| Northern bounds of search | [optional] |
| **minlongitude** | **Float**| Western bounds of search | [optional] |
| **minlatitude** | **Float**| Southern bounds of search | [optional] |
| **maxlongitude** | **Float**| Eastern bounds of search | [optional] |
| **max** | **Integer**| Max number of results | [optional] |
| **skip** | **Integer**| Number to skip | [optional] |
| **searchDbUfoSightingsDatetime** | **String**| Datetime | [optional] |
| **searchDbUfoSightingsCity** | **String**| City | [optional] |
| **searchDbUfoSightingsState** | **String**| State | [optional] |
| **searchDbUfoSightingsCountry** | **String**| Country | [optional] |
| **searchDbUfoSightingsShape** | **String**| Shape | [optional] |
| **searchDbUfoSightingsDurationSeconds** | **Double**| Duration (seconds) | [optional] |
| **searchDbUfoSightingsDurationHoursMin** | **String**| Duration (hours/min) | [optional] |
| **searchDbUfoSightingsComments** | **String**| Comments | [optional] |
| **searchDbUfoSightingsDatePosted** | **String**| Date Posted | [optional] |
| **searchDbUfoSightingsLatitude** | **Double**| Latitude | [optional] |
| **searchDbUfoSightingsLongitude** | **Double**| Longitude | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

