# HotelsApi

All URIs are relative to *https://sandbox.impala.travel/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listHotels**](HotelsApi.md#listHotels) | **GET** /hotels | List all hotels |
| [**retrieveHotel**](HotelsApi.md#retrieveHotel) | **GET** /hotels/{hotelId} | Retrieve a hotel |


<a id="listHotels"></a>
# **listHotels**
> ListHotels200Response listHotels(name, starRating, country, start, end, latitude, longitude, radius, hotelIds, created, updated, size, offset, sortBy)

List all hotels

Returns a list of all hotels worldwide that can be booked through Impala.  You can **filter** the results:  * Adding &#x60;longitude&#x60;, &#x60;latitude&#x60; and a &#x60;radius&#x60; (in meters) query parameters will filter the results to hotels around this location. * Adding &#x60;start&#x60; and &#x60;end&#x60; dates (in ISO 8601 notation, e.g. &#x60;2021-12-31&#x60;) for the expected arrival and departure dates of your guests will limit the results to hotels that have at least one room bookable for this timeframe. * Adding &#x60;starRating&#x60;, &#x60;name&#x60; or &#x60;country&#x60; allows you to filter to hotels based on these values (e.g. &#x60;?starRating[gte]&#x3D;4&amp;name[like]&#x3D;palace&#x60; for hotels with a rating of 4 or up with a name containing \&quot;palace\&quot;) * Adding &#x60;hotelIds&#x60; allows you to limit the results to include only hotels with the ids listed. Its value should be a comma-separated list of hotel ids (e.g. &#x60;?hotelIds[]&#x3D;hotelIdA,hotelIdB&#x60;)  * Adding &#x60;contractable&#x60; allows you to filter to hotels that you can directly negotiate with through our [deals feature](https://docs.impala.travel/docs/booking-api/ZG9jOjcyNjgzMTA-contracting-with-hotels). (e.g &#x60;?contractable&#x3D;true&#x60; or &#x60;?contractable&#x3D;false&#x60;)  You can specify the **sorting order** in which hotels are returned: * This is done by using the &#x60;sortBy&#x60; query parameter. * Results can be sorted by &#x60;name&#x60; alphabetically, star &#x60;rating&#x60; and &#x60;distance_m&#x60; (in meters from the specified latitude/longitude location). * The parameter allows for a comma-separated list of arguments with optional &#x60;:asc&#x60; (ascending, the default if the modifier is omitted) and &#x60;:desc&#x60; (descending) modifiers.  If no hotels match your filter criteria, an empty array will be returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HotelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox.impala.travel/v1");
    
    // Configure API key authorization: API_Key_Authentication
    ApiKeyAuth API_Key_Authentication = (ApiKeyAuth) defaultClient.getAuthentication("API_Key_Authentication");
    API_Key_Authentication.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API_Key_Authentication.setApiKeyPrefix("Token");

    HotelsApi apiInstance = new HotelsApi(defaultClient);
    Object name = new HashMap(); // Object | Allows for filtering based on the property name. Available modifiers include equal to (`eq`) or case insensitive search (`like`). Usage example: `?name[like]=palace`
    Object starRating = new HashMap(); // Object | Allows for filtering based on the starRating of a property. Available modifiers include less than (`lt`), greater than (`gt`), less than or equal to (`lte`), greater than or equal to (`gte`) and equal to (`eq`). Usage example: `?starRating[gt]=3&starRating[lt]=5`
    Object country = new HashMap(); // Object | Allows for filtering based on the country of a property. The only available modifier for this parameter is equal to (`eq`). Usage example: `?country[eq]=GBR`
    String start = "2021-05-20"; // String | The arrival day of the desired stay range in ISO 8601 format (`YYYY-MM-DD`).
    String end = "2021-05-22"; // String | The departure day of the desired stay range in ISO 8601 format (`YYYY-MM-DD`).
    Double latitude = 58.386186D; // Double | The WGS 84 latitude of the location to search around (e.g. `58.386186`).
    Double longitude = -9.952549D; // Double | The WGS 84 longitude of the location to search around (e.g. `-9.952549`).
    Integer radius = 25000; // Integer | The distance (in meters) to search around the specified location (e.g. `10000` for 10 km).
    List<String> hotelIds = Arrays.asList(); // List<String> | A comma-separated list of hotel ids you wish to filter by (e.g. `60a06628-2c71-44bf-9685-efbd2df4179e,60a06628-2c71-44bf-9685-efbd2df4179e`).
    Object created = new HashMap(); // Object | Allows for filtering based on the date and time when this hotel was first added to the Impala platform, in ISO 8601 format (e.g. `2020-11-04T17:37:37Z`) and UTC timezone. Available modifiers include less than (`lt`), greater than (`gt`), lower than or equal to (`lte`), greater than or equal to (`gte`) and equal to (`eq`). Usage example: `?created[lte]=2020-11-04T19:37:37Z&created[gte]=2020-11-04T15:56:37.000Z`
    Object updated = new HashMap(); // Object | Allows for filtering based on the date and time the content of this hotel was last updated, in ISO 8601 format (e.g. `2020-11-04T17:37:37Z`) and UTC timezone. Available modifiers include less than (`lt`), greater than (`gt`), lower than or equal to (`lte`), greater than or equal to (`gte`) and equal to (`eq`). Usage example: `?updated[lte]=2020-11-04T19:37:37Z&updated[gte]=2020-11-04T15:56:37.000Z`
    BigDecimal size = new BigDecimal("25"); // BigDecimal | Number of hotels returned on a given page (pagination).
    BigDecimal offset = new BigDecimal("0"); // BigDecimal | Offset from the first hotel in the result (for pagination).
    String sortBy = "createdAt:desc"; // String | Order in which the results should be sorted. Currently allows you to sort by `name` (alphabetical), star `rating`, and `distance_m` in meters from the specified latitude/longitude. Allows for a comma-separated list of of arguments with modifiers for `:asc` (ascending) and `:desc` (descending) ordering.
    try {
      ListHotels200Response result = apiInstance.listHotels(name, starRating, country, start, end, latitude, longitude, radius, hotelIds, created, updated, size, offset, sortBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HotelsApi#listHotels");
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
| **name** | [**Object**](.md)| Allows for filtering based on the property name. Available modifiers include equal to (&#x60;eq&#x60;) or case insensitive search (&#x60;like&#x60;). Usage example: &#x60;?name[like]&#x3D;palace&#x60; | [optional] |
| **starRating** | [**Object**](.md)| Allows for filtering based on the starRating of a property. Available modifiers include less than (&#x60;lt&#x60;), greater than (&#x60;gt&#x60;), less than or equal to (&#x60;lte&#x60;), greater than or equal to (&#x60;gte&#x60;) and equal to (&#x60;eq&#x60;). Usage example: &#x60;?starRating[gt]&#x3D;3&amp;starRating[lt]&#x3D;5&#x60; | [optional] |
| **country** | [**Object**](.md)| Allows for filtering based on the country of a property. The only available modifier for this parameter is equal to (&#x60;eq&#x60;). Usage example: &#x60;?country[eq]&#x3D;GBR&#x60; | [optional] |
| **start** | **String**| The arrival day of the desired stay range in ISO 8601 format (&#x60;YYYY-MM-DD&#x60;). | [optional] |
| **end** | **String**| The departure day of the desired stay range in ISO 8601 format (&#x60;YYYY-MM-DD&#x60;). | [optional] |
| **latitude** | **Double**| The WGS 84 latitude of the location to search around (e.g. &#x60;58.386186&#x60;). | [optional] |
| **longitude** | **Double**| The WGS 84 longitude of the location to search around (e.g. &#x60;-9.952549&#x60;). | [optional] |
| **radius** | **Integer**| The distance (in meters) to search around the specified location (e.g. &#x60;10000&#x60; for 10 km). | [optional] |
| **hotelIds** | [**List&lt;String&gt;**](String.md)| A comma-separated list of hotel ids you wish to filter by (e.g. &#x60;60a06628-2c71-44bf-9685-efbd2df4179e,60a06628-2c71-44bf-9685-efbd2df4179e&#x60;). | [optional] |
| **created** | [**Object**](.md)| Allows for filtering based on the date and time when this hotel was first added to the Impala platform, in ISO 8601 format (e.g. &#x60;2020-11-04T17:37:37Z&#x60;) and UTC timezone. Available modifiers include less than (&#x60;lt&#x60;), greater than (&#x60;gt&#x60;), lower than or equal to (&#x60;lte&#x60;), greater than or equal to (&#x60;gte&#x60;) and equal to (&#x60;eq&#x60;). Usage example: &#x60;?created[lte]&#x3D;2020-11-04T19:37:37Z&amp;created[gte]&#x3D;2020-11-04T15:56:37.000Z&#x60; | [optional] |
| **updated** | [**Object**](.md)| Allows for filtering based on the date and time the content of this hotel was last updated, in ISO 8601 format (e.g. &#x60;2020-11-04T17:37:37Z&#x60;) and UTC timezone. Available modifiers include less than (&#x60;lt&#x60;), greater than (&#x60;gt&#x60;), lower than or equal to (&#x60;lte&#x60;), greater than or equal to (&#x60;gte&#x60;) and equal to (&#x60;eq&#x60;). Usage example: &#x60;?updated[lte]&#x3D;2020-11-04T19:37:37Z&amp;updated[gte]&#x3D;2020-11-04T15:56:37.000Z&#x60; | [optional] |
| **size** | **BigDecimal**| Number of hotels returned on a given page (pagination). | [optional] [default to 25] |
| **offset** | **BigDecimal**| Offset from the first hotel in the result (for pagination). | [optional] [default to 0] |
| **sortBy** | **String**| Order in which the results should be sorted. Currently allows you to sort by &#x60;name&#x60; (alphabetical), star &#x60;rating&#x60;, and &#x60;distance_m&#x60; in meters from the specified latitude/longitude. Allows for a comma-separated list of of arguments with modifiers for &#x60;:asc&#x60; (ascending) and &#x60;:desc&#x60; (descending) ordering. | [optional] [default to createdAt:desc] |

### Return type

[**ListHotels200Response**](ListHotels200Response.md)

### Authorization

[API_Key_Authentication](../README.md#API_Key_Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a paginated list of hotels. |  -  |
| **400** | Your request wasn&#39;t formatted correctly and therefore couldn&#39;t be processed. This most frequently happens when query parameters or request body values are missing, incorrectly formatted or added where they don&#39;t exist (e.g. due to typos). We&#39;re including a list of &#x60;validations&#x60; to point out where things are going wrong and should be fixed. |  -  |
| **401** | Your request was sent without or with an incorrect API key. This most frequently happens when the &#x60;x-api-key&#x60; header wasn&#39;t added or contains an incorrect value. This might also happen if you&#39;re trying to access the production API endpoints with a sandbox API key or vice versa. |  -  |
| **500** | An internal server error within the Impala platform has occurred. Our team will investigate the error. We recommend that you contact us at support@impala.travel with the x-correlation-id value contained within the response headers. Sending us this value will allow us to identify the precise error you encountered. |  -  |

<a id="retrieveHotel"></a>
# **retrieveHotel**
> HotelFullDetail retrieveHotel(hotelId, start, end)

Retrieve a hotel

Returns the full content, room types and rates for the specified hotel.  When querying the hotels API you can query with or without dates. Where querying with dates requires providing valid values for the &#x60;start&#x60; and &#x60;end&#x60; parameters. Requests without these values will be considered a query without dates.  **Querying without dates:**  When you query without dates, the search result will include all properties that match your request. Including all content that is associated with those properties. However you will find that the &#x60;rates&#x60; attribute for each room will always be empty.  **Querying with dates:**  When you query with dates, the search result will include all properties that match your request, including all content that is associated with those properties. Rooms which do not have available prices for the provided dates will appear with an empty &#x60;rates&#x60; array.  For rooms where there are available prices the &#x60;rates&#x60; array will include both the public rates of the hotel, along with prices that come from deals in which you are participating. This would include private deals which you have negotiated with a hotel, along with Impala deals which you have been verified for.  Using the &#x60;rateId&#x60; of any of those rates, you can use the [Create a booking](https://docs.impala.travel/docs/booking-api/spec/openapi.seller.yaml/paths/~1bookings/post) endpoint to make a booking.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HotelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://sandbox.impala.travel/v1");
    
    // Configure API key authorization: API_Key_Authentication
    ApiKeyAuth API_Key_Authentication = (ApiKeyAuth) defaultClient.getAuthentication("API_Key_Authentication");
    API_Key_Authentication.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API_Key_Authentication.setApiKeyPrefix("Token");

    HotelsApi apiInstance = new HotelsApi(defaultClient);
    UUID hotelId = UUID.randomUUID(); // UUID | The unique identifier of this hotel on the Impala platform.
    String start = "2021-05-20"; // String | The arrival day of the desired stay range in ISO 8601 format (`YYYY-MM-DD`).
    String end = "2021-05-22"; // String | The departure day of the desired stay range in ISO 8601 format (`YYYY-MM-DD`).
    try {
      HotelFullDetail result = apiInstance.retrieveHotel(hotelId, start, end);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HotelsApi#retrieveHotel");
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
| **hotelId** | **UUID**| The unique identifier of this hotel on the Impala platform. | |
| **start** | **String**| The arrival day of the desired stay range in ISO 8601 format (&#x60;YYYY-MM-DD&#x60;). | [optional] |
| **end** | **String**| The departure day of the desired stay range in ISO 8601 format (&#x60;YYYY-MM-DD&#x60;). | [optional] |

### Return type

[**HotelFullDetail**](HotelFullDetail.md)

### Authorization

[API_Key_Authentication](../README.md#API_Key_Authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the requested hotel. |  -  |
| **400** | Your request wasn&#39;t formatted correctly and therefore couldn&#39;t be processed. This most frequently happens when query parameters or request body values are missing, incorrectly formatted or added where they don&#39;t exist (e.g. due to typos). We&#39;re including a list of &#x60;validations&#x60; to point out where things are going wrong and should be fixed. |  -  |
| **401** | Your request was sent without or with an incorrect API key. This most frequently happens when the &#x60;x-api-key&#x60; header wasn&#39;t added or contains an incorrect value. This might also happen if you&#39;re trying to access the production API endpoints with a sandbox API key or vice versa. |  -  |
| **403** | Forbidden |  -  |
| **500** | An internal server error within the Impala platform has occurred. Our team will investigate the error. We recommend that you contact us at support@impala.travel with the x-correlation-id value contained within the response headers. Sending us this value will allow us to identify the precise error you encountered. |  -  |

