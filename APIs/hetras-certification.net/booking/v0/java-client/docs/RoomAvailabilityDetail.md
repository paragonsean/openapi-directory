

# RoomAvailabilityDetail


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**Map&lt;String, LinkObject&gt;**](LinkObject.md) | Collection of links to related resources |  [optional] |
|**available** | **Integer** | The number of rooms that were originally available to sell. This is the the house count reduced by rooms set              to OutOfOrder but increased by the set overbooking |  [optional] |
|**blocked** | [**Blocked**](Blocked.md) |  |  [optional] |
|**code** | **String** | Code of the room type |  [optional] |
|**dayUse** | **Integer** | The number of day use reservations |  [optional] |
|**_default** | **Boolean** | Specifies if the room type is the default room type of the hotel |  [optional] |
|**houseCount** | **Integer** | The total count of physical rooms reduced by the number of rooms set to OutOfInventory |  [optional] |
|**maintenance** | [**Maintenance**](Maintenance.md) |  |  [optional] |
|**overbooking** | **Integer** | The manually set overbooking |  [optional] |
|**roomCount** | **Integer** | The total count of physical rooms |  [optional] |
|**sold** | **Integer** | The count of rooms sold. It sums up the rooms sold through individual reservations plus rooms blocked definitely |  [optional] |
|**toSell** | **Integer** | The number of rooms still available to sell. It is available reduced by the already sold rooms |  [optional] |



