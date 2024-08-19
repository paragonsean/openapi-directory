# ImpalaHotelBookingApi.HotelsApi

All URIs are relative to *https://sandbox.impala.travel/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listHotels**](HotelsApi.md#listHotels) | **GET** /hotels | List all hotels
[**retrieveHotel**](HotelsApi.md#retrieveHotel) | **GET** /hotels/{hotelId} | Retrieve a hotel



## listHotels

> ListHotels200Response listHotels(opts)

List all hotels

Returns a list of all hotels worldwide that can be booked through Impala.  You can **filter** the results:  * Adding &#x60;longitude&#x60;, &#x60;latitude&#x60; and a &#x60;radius&#x60; (in meters) query parameters will filter the results to hotels around this location. * Adding &#x60;start&#x60; and &#x60;end&#x60; dates (in ISO 8601 notation, e.g. &#x60;2021-12-31&#x60;) for the expected arrival and departure dates of your guests will limit the results to hotels that have at least one room bookable for this timeframe. * Adding &#x60;starRating&#x60;, &#x60;name&#x60; or &#x60;country&#x60; allows you to filter to hotels based on these values (e.g. &#x60;?starRating[gte]&#x3D;4&amp;name[like]&#x3D;palace&#x60; for hotels with a rating of 4 or up with a name containing \&quot;palace\&quot;) * Adding &#x60;hotelIds&#x60; allows you to limit the results to include only hotels with the ids listed. Its value should be a comma-separated list of hotel ids (e.g. &#x60;?hotelIds[]&#x3D;hotelIdA,hotelIdB&#x60;)  * Adding &#x60;contractable&#x60; allows you to filter to hotels that you can directly negotiate with through our [deals feature](https://docs.impala.travel/docs/booking-api/ZG9jOjcyNjgzMTA-contracting-with-hotels). (e.g &#x60;?contractable&#x3D;true&#x60; or &#x60;?contractable&#x3D;false&#x60;)  You can specify the **sorting order** in which hotels are returned: * This is done by using the &#x60;sortBy&#x60; query parameter. * Results can be sorted by &#x60;name&#x60; alphabetically, star &#x60;rating&#x60; and &#x60;distance_m&#x60; (in meters from the specified latitude/longitude location). * The parameter allows for a comma-separated list of arguments with optional &#x60;:asc&#x60; (ascending, the default if the modifier is omitted) and &#x60;:desc&#x60; (descending) modifiers.  If no hotels match your filter criteria, an empty array will be returned.

### Example

```javascript
import ImpalaHotelBookingApi from 'impala_hotel_booking_api';
let defaultClient = ImpalaHotelBookingApi.ApiClient.instance;
// Configure API key authorization: API_Key_Authentication
let API_Key_Authentication = defaultClient.authentications['API_Key_Authentication'];
API_Key_Authentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API_Key_Authentication.apiKeyPrefix = 'Token';

let apiInstance = new ImpalaHotelBookingApi.HotelsApi();
let opts = {
  'name': {key: null}, // Object | Allows for filtering based on the property name. Available modifiers include equal to (`eq`) or case insensitive search (`like`). Usage example: `?name[like]=palace`
  'starRating': {key: null}, // Object | Allows for filtering based on the starRating of a property. Available modifiers include less than (`lt`), greater than (`gt`), less than or equal to (`lte`), greater than or equal to (`gte`) and equal to (`eq`). Usage example: `?starRating[gt]=3&starRating[lt]=5`
  'country': {key: null}, // Object | Allows for filtering based on the country of a property. The only available modifier for this parameter is equal to (`eq`). Usage example: `?country[eq]=GBR`
  'start': "2021-05-20", // String | The arrival day of the desired stay range in ISO 8601 format (`YYYY-MM-DD`).
  'end': "2021-05-22", // String | The departure day of the desired stay range in ISO 8601 format (`YYYY-MM-DD`).
  'latitude': 58.386186, // Number | The WGS 84 latitude of the location to search around (e.g. `58.386186`).
  'longitude': -9.952549, // Number | The WGS 84 longitude of the location to search around (e.g. `-9.952549`).
  'radius': 25000, // Number | The distance (in meters) to search around the specified location (e.g. `10000` for 10 km).
  'hotelIds': ["8a39290a-bcd0-461e-92c6-38e71a06d2f7"], // [String] | A comma-separated list of hotel ids you wish to filter by (e.g. `60a06628-2c71-44bf-9685-efbd2df4179e,60a06628-2c71-44bf-9685-efbd2df4179e`).
  'created': {key: null}, // Object | Allows for filtering based on the date and time when this hotel was first added to the Impala platform, in ISO 8601 format (e.g. `2020-11-04T17:37:37Z`) and UTC timezone. Available modifiers include less than (`lt`), greater than (`gt`), lower than or equal to (`lte`), greater than or equal to (`gte`) and equal to (`eq`). Usage example: `?created[lte]=2020-11-04T19:37:37Z&created[gte]=2020-11-04T15:56:37.000Z`
  'updated': {key: null}, // Object | Allows for filtering based on the date and time the content of this hotel was last updated, in ISO 8601 format (e.g. `2020-11-04T17:37:37Z`) and UTC timezone. Available modifiers include less than (`lt`), greater than (`gt`), lower than or equal to (`lte`), greater than or equal to (`gte`) and equal to (`eq`). Usage example: `?updated[lte]=2020-11-04T19:37:37Z&updated[gte]=2020-11-04T15:56:37.000Z`
  'size': 40, // Number | Number of hotels returned on a given page (pagination).
  'offset': 25, // Number | Offset from the first hotel in the result (for pagination).
  'sortBy': "name:asc,distance_m:desc" // String | Order in which the results should be sorted. Currently allows you to sort by `name` (alphabetical), star `rating`, and `distance_m` in meters from the specified latitude/longitude. Allows for a comma-separated list of of arguments with modifiers for `:asc` (ascending) and `:desc` (descending) ordering.
};
apiInstance.listHotels(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | [**Object**](.md)| Allows for filtering based on the property name. Available modifiers include equal to (&#x60;eq&#x60;) or case insensitive search (&#x60;like&#x60;). Usage example: &#x60;?name[like]&#x3D;palace&#x60; | [optional] 
 **starRating** | [**Object**](.md)| Allows for filtering based on the starRating of a property. Available modifiers include less than (&#x60;lt&#x60;), greater than (&#x60;gt&#x60;), less than or equal to (&#x60;lte&#x60;), greater than or equal to (&#x60;gte&#x60;) and equal to (&#x60;eq&#x60;). Usage example: &#x60;?starRating[gt]&#x3D;3&amp;starRating[lt]&#x3D;5&#x60; | [optional] 
 **country** | [**Object**](.md)| Allows for filtering based on the country of a property. The only available modifier for this parameter is equal to (&#x60;eq&#x60;). Usage example: &#x60;?country[eq]&#x3D;GBR&#x60; | [optional] 
 **start** | **String**| The arrival day of the desired stay range in ISO 8601 format (&#x60;YYYY-MM-DD&#x60;). | [optional] 
 **end** | **String**| The departure day of the desired stay range in ISO 8601 format (&#x60;YYYY-MM-DD&#x60;). | [optional] 
 **latitude** | **Number**| The WGS 84 latitude of the location to search around (e.g. &#x60;58.386186&#x60;). | [optional] 
 **longitude** | **Number**| The WGS 84 longitude of the location to search around (e.g. &#x60;-9.952549&#x60;). | [optional] 
 **radius** | **Number**| The distance (in meters) to search around the specified location (e.g. &#x60;10000&#x60; for 10 km). | [optional] 
 **hotelIds** | [**[String]**](String.md)| A comma-separated list of hotel ids you wish to filter by (e.g. &#x60;60a06628-2c71-44bf-9685-efbd2df4179e,60a06628-2c71-44bf-9685-efbd2df4179e&#x60;). | [optional] 
 **created** | [**Object**](.md)| Allows for filtering based on the date and time when this hotel was first added to the Impala platform, in ISO 8601 format (e.g. &#x60;2020-11-04T17:37:37Z&#x60;) and UTC timezone. Available modifiers include less than (&#x60;lt&#x60;), greater than (&#x60;gt&#x60;), lower than or equal to (&#x60;lte&#x60;), greater than or equal to (&#x60;gte&#x60;) and equal to (&#x60;eq&#x60;). Usage example: &#x60;?created[lte]&#x3D;2020-11-04T19:37:37Z&amp;created[gte]&#x3D;2020-11-04T15:56:37.000Z&#x60; | [optional] 
 **updated** | [**Object**](.md)| Allows for filtering based on the date and time the content of this hotel was last updated, in ISO 8601 format (e.g. &#x60;2020-11-04T17:37:37Z&#x60;) and UTC timezone. Available modifiers include less than (&#x60;lt&#x60;), greater than (&#x60;gt&#x60;), lower than or equal to (&#x60;lte&#x60;), greater than or equal to (&#x60;gte&#x60;) and equal to (&#x60;eq&#x60;). Usage example: &#x60;?updated[lte]&#x3D;2020-11-04T19:37:37Z&amp;updated[gte]&#x3D;2020-11-04T15:56:37.000Z&#x60; | [optional] 
 **size** | **Number**| Number of hotels returned on a given page (pagination). | [optional] [default to 25]
 **offset** | **Number**| Offset from the first hotel in the result (for pagination). | [optional] [default to 0]
 **sortBy** | **String**| Order in which the results should be sorted. Currently allows you to sort by &#x60;name&#x60; (alphabetical), star &#x60;rating&#x60;, and &#x60;distance_m&#x60; in meters from the specified latitude/longitude. Allows for a comma-separated list of of arguments with modifiers for &#x60;:asc&#x60; (ascending) and &#x60;:desc&#x60; (descending) ordering. | [optional] [default to &#39;createdAt:desc&#39;]

### Return type

[**ListHotels200Response**](ListHotels200Response.md)

### Authorization

[API_Key_Authentication](../README.md#API_Key_Authentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrieveHotel

> HotelFullDetail retrieveHotel(hotelId, opts)

Retrieve a hotel

Returns the full content, room types and rates for the specified hotel.  When querying the hotels API you can query with or without dates. Where querying with dates requires providing valid values for the &#x60;start&#x60; and &#x60;end&#x60; parameters. Requests without these values will be considered a query without dates.  **Querying without dates:**  When you query without dates, the search result will include all properties that match your request. Including all content that is associated with those properties. However you will find that the &#x60;rates&#x60; attribute for each room will always be empty.  **Querying with dates:**  When you query with dates, the search result will include all properties that match your request, including all content that is associated with those properties. Rooms which do not have available prices for the provided dates will appear with an empty &#x60;rates&#x60; array.  For rooms where there are available prices the &#x60;rates&#x60; array will include both the public rates of the hotel, along with prices that come from deals in which you are participating. This would include private deals which you have negotiated with a hotel, along with Impala deals which you have been verified for.  Using the &#x60;rateId&#x60; of any of those rates, you can use the [Create a booking](https://docs.impala.travel/docs/booking-api/spec/openapi.seller.yaml/paths/~1bookings/post) endpoint to make a booking.

### Example

```javascript
import ImpalaHotelBookingApi from 'impala_hotel_booking_api';
let defaultClient = ImpalaHotelBookingApi.ApiClient.instance;
// Configure API key authorization: API_Key_Authentication
let API_Key_Authentication = defaultClient.authentications['API_Key_Authentication'];
API_Key_Authentication.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//API_Key_Authentication.apiKeyPrefix = 'Token';

let apiInstance = new ImpalaHotelBookingApi.HotelsApi();
let hotelId = "hotelId_example"; // String | The unique identifier of this hotel on the Impala platform.
let opts = {
  'start': "2021-05-20", // String | The arrival day of the desired stay range in ISO 8601 format (`YYYY-MM-DD`).
  'end': "2021-05-22" // String | The departure day of the desired stay range in ISO 8601 format (`YYYY-MM-DD`).
};
apiInstance.retrieveHotel(hotelId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hotelId** | **String**| The unique identifier of this hotel on the Impala platform. | 
 **start** | **String**| The arrival day of the desired stay range in ISO 8601 format (&#x60;YYYY-MM-DD&#x60;). | [optional] 
 **end** | **String**| The departure day of the desired stay range in ISO 8601 format (&#x60;YYYY-MM-DD&#x60;). | [optional] 

### Return type

[**HotelFullDetail**](HotelFullDetail.md)

### Authorization

[API_Key_Authentication](../README.md#API_Key_Authentication)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

