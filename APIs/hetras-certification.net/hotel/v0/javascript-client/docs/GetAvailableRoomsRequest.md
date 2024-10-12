# HetrasHotelApiVersion0.GetAvailableRoomsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adults** | **Blob** | Specifies number of adults the returned rooms will have to be able to house. The default value is 1. | [optional] 
**amenities** | **[String]** | Return result only for rooms having all of the given amenities. You can provide a comma seperated list of               amenity codes. | [optional] 
**from** | **Date** | Rooms returned will not be assigned to a reservation or be under maintenance between this date              and the specified to date. Still there could be departing reservations or ending maintenances              for this date. | 
**includeOutOfService** | **Boolean** | Should rooms that are set OutOfService in the defined time period be returned as available. By default              they are not. | [optional] 
**locations** | **[String]** | Return result only for rooms having at least one of the specified locations. You can provide a comma seperated list of               location codes. | [optional] 
**roomTypes** | **[String]** | Return result only for rooms for the given room types. Allows to pass a comma-separated list of room types. | [optional] 
**to** | **Date** | Rooms returned will not be assigned to a reservation or be under maintenance between the specified              from date and this date. Still there could be arriving reservations or beginning maintenances              for this date. | 
**views** | **[String]** | Return result only for rooms having at least one of the specified views. You can provide a comma seperated list of               view codes. | [optional] 


