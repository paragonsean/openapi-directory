# HetrasHotelApiVersion0.RoomsApi

All URIs are relative to *https://api.hetras-certification.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**roomsGetAvailableRooms**](RoomsApi.md#roomsGetAvailableRooms) | **GET** /api/hotel/v0/hotels/{hotelId}/rooms/available | Request available rooms using a given criteria.
[**roomsGetRoom**](RoomsApi.md#roomsGetRoom) | **GET** /api/hotel/v0/hotels/{hotelId}/rooms/{roomNumber} | Get all the details for a specific room in the hotel.
[**roomsGetRooms**](RoomsApi.md#roomsGetRooms) | **GET** /api/hotel/v0/hotels/{hotelId}/rooms | Get a list of rooms using the provided filtering and pagination criteria.
[**roomsGetRoomsCount**](RoomsApi.md#roomsGetRoomsCount) | **GET** /api/hotel/v0/hotels/{hotelId}/rooms/$count | Get the count of all rooms in the hotel matching the given filter criteria.
[**roomsPatchRoom**](RoomsApi.md#roomsPatchRoom) | **PATCH** /api/hotel/v0/hotels/{hotelId}/rooms/{roomNumber} | Partially updates a room.



## roomsGetAvailableRooms

> RoomListResponse roomsGetAvailableRooms(appId, appKey, hotelId, from, to, opts)

Request available rooms using a given criteria.

### Example

```javascript
import HetrasHotelApiVersion0 from 'hetras_hotel_api_version_0';

let apiInstance = new HetrasHotelApiVersion0.RoomsApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let hotelId = 56; // Number | The hotel you are looking for available rooms.
let from = new Date("2013-10-20T19:20:30+01:00"); // Date | Rooms returned will not be assigned to a reservation or be under maintenance between this date              and the specified to date. Still there could be departing reservations or ending maintenances              for this date.
let to = new Date("2013-10-20T19:20:30+01:00"); // Date | Rooms returned will not be assigned to a reservation or be under maintenance between the specified              from date and this date. Still there could be arriving reservations or beginning maintenances              for this date.
let opts = {
  'adults': null, // Blob | Specifies number of adults the returned rooms will have to be able to house. The default value is 1.
  'includeOutOfService': true, // Boolean | Should rooms that are set OutOfService in the defined time period be returned as available. By default              they are not.
  'roomTypes': ["null"], // [String] | Return result only for rooms for the given room types. Allows to pass a comma-separated list of room types.
  'amenities': ["null"], // [String] | Return result only for rooms having all of the given amenities. You can provide a comma seperated list of               amenity codes.
  'views': ["null"], // [String] | Return result only for rooms having at least one of the specified views. You can provide a comma seperated list of               view codes.
  'locations': ["null"], // [String] | Return result only for rooms having at least one of the specified locations. You can provide a comma seperated list of               location codes.
  'skip': 56, // Number | Amount of items to skip.
  'top': 56, // Number | Amount of items to select.
  'inlinecount': "inlinecount_example" // String | Return total number of items for a given filter criteria.
};
apiInstance.roomsGetAvailableRooms(appId, appKey, hotelId, from, to, opts, (error, data, response) => {
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
 **appId** | **String**| Application identifier | 
 **appKey** | **String**| Application key. | 
 **hotelId** | **Number**| The hotel you are looking for available rooms. | 
 **from** | **Date**| Rooms returned will not be assigned to a reservation or be under maintenance between this date              and the specified to date. Still there could be departing reservations or ending maintenances              for this date. | 
 **to** | **Date**| Rooms returned will not be assigned to a reservation or be under maintenance between the specified              from date and this date. Still there could be arriving reservations or beginning maintenances              for this date. | 
 **adults** | **Blob**| Specifies number of adults the returned rooms will have to be able to house. The default value is 1. | [optional] 
 **includeOutOfService** | **Boolean**| Should rooms that are set OutOfService in the defined time period be returned as available. By default              they are not. | [optional] 
 **roomTypes** | [**[String]**](String.md)| Return result only for rooms for the given room types. Allows to pass a comma-separated list of room types. | [optional] 
 **amenities** | [**[String]**](String.md)| Return result only for rooms having all of the given amenities. You can provide a comma seperated list of               amenity codes. | [optional] 
 **views** | [**[String]**](String.md)| Return result only for rooms having at least one of the specified views. You can provide a comma seperated list of               view codes. | [optional] 
 **locations** | [**[String]**](String.md)| Return result only for rooms having at least one of the specified locations. You can provide a comma seperated list of               location codes. | [optional] 
 **skip** | **Number**| Amount of items to skip. | [optional] 
 **top** | **Number**| Amount of items to select. | [optional] 
 **inlinecount** | **String**| Return total number of items for a given filter criteria. | [optional] 

### Return type

[**RoomListResponse**](RoomListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## roomsGetRoom

> Room roomsGetRoom(appId, appKey, hotelId, roomNumber)

Get all the details for a specific room in the hotel.

With this call you can load the details about a specific room in the hotel. It will show you the current status of the room.

### Example

```javascript
import HetrasHotelApiVersion0 from 'hetras_hotel_api_version_0';

let apiInstance = new HetrasHotelApiVersion0.RoomsApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let hotelId = 56; // Number | The hotel id the room belongs to.
let roomNumber = "roomNumber_example"; // String | The room number you want to see details for.
apiInstance.roomsGetRoom(appId, appKey, hotelId, roomNumber, (error, data, response) => {
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
 **appId** | **String**| Application identifier | 
 **appKey** | **String**| Application key. | 
 **hotelId** | **Number**| The hotel id the room belongs to. | 
 **roomNumber** | **String**| The room number you want to see details for. | 

### Return type

[**Room**](Room.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## roomsGetRooms

> RoomListResponse roomsGetRooms(appId, appKey, hotelId, opts)

Get a list of rooms using the provided filtering and pagination criteria.

Find all rooms for the hotel that match the specified filter criteria. The filtering will be done based on the current state of              the rooms.

### Example

```javascript
import HetrasHotelApiVersion0 from 'hetras_hotel_api_version_0';

let apiInstance = new HetrasHotelApiVersion0.RoomsApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let hotelId = 56; // Number | The hotel you are trying to find rooms for.
let opts = {
  'occupancy': "occupancy_example", // String | Return results only for rooms that have the given frontdesk ocuppancy status.
  'conditions': ["null"], // [String] | Return results only for rooms that have the given room condition status.
  'maintenances': ["null"], // [String] | Return results only for rooms that have the given maintenance status.
  'roomTypes': ["null"], // [String] | Return result only for rooms for the given room types. Allows to pass a comma-separated list of room types.
  'amenities': ["null"], // [String] | Return result only for rooms having all of the given amenities. You can provide a comma seperated list of               amenity codes.
  'views': ["null"], // [String] | Return result only for rooms having at least one of the specified views. You can provide a comma seperated list of               view codes.
  'locations': ["null"], // [String] | Return result only for rooms having at least one of the specified locations. You can provide a comma seperated list of               location codes.
  'skip': 56, // Number | Amount of items to skip.
  'top': 56, // Number | Amount of items to select.
  'inlinecount': "inlinecount_example" // String | Return total number of items for a given filter criteria.
};
apiInstance.roomsGetRooms(appId, appKey, hotelId, opts, (error, data, response) => {
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
 **appId** | **String**| Application identifier | 
 **appKey** | **String**| Application key. | 
 **hotelId** | **Number**| The hotel you are trying to find rooms for. | 
 **occupancy** | **String**| Return results only for rooms that have the given frontdesk ocuppancy status. | [optional] 
 **conditions** | [**[String]**](String.md)| Return results only for rooms that have the given room condition status. | [optional] 
 **maintenances** | [**[String]**](String.md)| Return results only for rooms that have the given maintenance status. | [optional] 
 **roomTypes** | [**[String]**](String.md)| Return result only for rooms for the given room types. Allows to pass a comma-separated list of room types. | [optional] 
 **amenities** | [**[String]**](String.md)| Return result only for rooms having all of the given amenities. You can provide a comma seperated list of               amenity codes. | [optional] 
 **views** | [**[String]**](String.md)| Return result only for rooms having at least one of the specified views. You can provide a comma seperated list of               view codes. | [optional] 
 **locations** | [**[String]**](String.md)| Return result only for rooms having at least one of the specified locations. You can provide a comma seperated list of               location codes. | [optional] 
 **skip** | **Number**| Amount of items to skip. | [optional] 
 **top** | **Number**| Amount of items to select. | [optional] 
 **inlinecount** | **String**| Return total number of items for a given filter criteria. | [optional] 

### Return type

[**RoomListResponse**](RoomListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## roomsGetRoomsCount

> TotalCountResponse roomsGetRoomsCount(appId, appKey, hotelId, opts)

Get the count of all rooms in the hotel matching the given filter criteria.

### Example

```javascript
import HetrasHotelApiVersion0 from 'hetras_hotel_api_version_0';

let apiInstance = new HetrasHotelApiVersion0.RoomsApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let hotelId = 56; // Number | The hotel you are counting the rooms for.
let opts = {
  'occupancy': "occupancy_example", // String | Return results only for rooms that have the given frontdesk ocuppancy status.
  'conditions': ["null"], // [String] | Return results only for rooms that have the given room condition status.
  'maintenances': ["null"], // [String] | Return results only for rooms that have the given maintenance status.
  'roomTypes': ["null"], // [String] | Return result only for rooms for the given room types. Allows to pass a comma-separated list of room types.
  'amenities': ["null"], // [String] | Return result only for rooms having all of the given amenities. You can provide a comma seperated list of               amenity codes.
  'views': ["null"], // [String] | Return result only for rooms having at least one of the specified views. You can provide a comma seperated list of               view codes.
  'locations': ["null"] // [String] | Return result only for rooms having at least one of the specified locations. You can provide a comma seperated list of               location codes.
};
apiInstance.roomsGetRoomsCount(appId, appKey, hotelId, opts, (error, data, response) => {
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
 **appId** | **String**| Application identifier | 
 **appKey** | **String**| Application key. | 
 **hotelId** | **Number**| The hotel you are counting the rooms for. | 
 **occupancy** | **String**| Return results only for rooms that have the given frontdesk ocuppancy status. | [optional] 
 **conditions** | [**[String]**](String.md)| Return results only for rooms that have the given room condition status. | [optional] 
 **maintenances** | [**[String]**](String.md)| Return results only for rooms that have the given maintenance status. | [optional] 
 **roomTypes** | [**[String]**](String.md)| Return result only for rooms for the given room types. Allows to pass a comma-separated list of room types. | [optional] 
 **amenities** | [**[String]**](String.md)| Return result only for rooms having all of the given amenities. You can provide a comma seperated list of               amenity codes. | [optional] 
 **views** | [**[String]**](String.md)| Return result only for rooms having at least one of the specified views. You can provide a comma seperated list of               view codes. | [optional] 
 **locations** | [**[String]**](String.md)| Return result only for rooms having at least one of the specified locations. You can provide a comma seperated list of               location codes. | [optional] 

### Return type

[**TotalCountResponse**](TotalCountResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## roomsPatchRoom

> Object roomsPatchRoom(appId, appKey, hotelId, roomNumber, patchRequest)

Partially updates a room.

The hetras API is using this &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/patch\&quot; onfocus&#x3D;\&quot;this.blur()\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Patch Specification&lt;/a&gt;              to partially update an existing resource. Currently this call only allows to modify condition and housekeeping occupancy status of the room.              &lt;br /&gt;&lt;br /&gt;              A request example:&lt;br /&gt;&lt;pre&gt;              [                {                  \&quot;op\&quot;: \&quot;replace\&quot;, \&quot;path\&quot;: \&quot;/status/condition\&quot;, \&quot;value\&quot;: \&quot;CleanNotInspected\&quot;                }, {                  \&quot;op\&quot;: \&quot;replace\&quot;, \&quot;path\&quot;: \&quot;/status/housekeeping_occupancy\&quot;, \&quot;value\&quot;: \&quot;Vacant\&quot;                }              ]              &lt;/pre&gt;&lt;br /&gt;              For more details on how the API responds to errors please check our documentation on               &lt;a href&#x3D;\&quot;https://developer.hetras.com/docs/errors/\&quot; onfocus&#x3D;\&quot;this.blur()\&quot;&gt;Error Handling&lt;/a&gt;.&lt;br /&gt;

### Example

```javascript
import HetrasHotelApiVersion0 from 'hetras_hotel_api_version_0';

let apiInstance = new HetrasHotelApiVersion0.RoomsApi();
let appId = "appId_example"; // String | Application identifier
let appKey = "appKey_example"; // String | Application key.
let hotelId = 56; // Number | The hotel id the room belongs to.
let roomNumber = "roomNumber_example"; // String | The room number of the room you would like to update.
let patchRequest = [new HetrasHotelApiVersion0.OperationRoomPatchRequest()]; // [OperationRoomPatchRequest] | A set of JSON Patch operations.
apiInstance.roomsPatchRoom(appId, appKey, hotelId, roomNumber, patchRequest, (error, data, response) => {
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
 **appId** | **String**| Application identifier | 
 **appKey** | **String**| Application key. | 
 **hotelId** | **Number**| The hotel id the room belongs to. | 
 **roomNumber** | **String**| The room number of the room you would like to update. | 
 **patchRequest** | [**[OperationRoomPatchRequest]**](OperationRoomPatchRequest.md)| A set of JSON Patch operations. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

