# HetrasBookingApiVersion0.AvailabilityDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**{String: LinkObject}**](LinkObject.md) | Collection of links to related resources | [optional] 
**available** | **Number** | The number of rooms that were originally available to sell. This is the the house count reduced by rooms set              to OutOfOrder but increased by the set overbooking | [optional] 
**blocked** | [**Blocked**](Blocked.md) |  | [optional] 
**dayUse** | **Number** | The number of day use reservations | [optional] 
**houseCount** | **Number** | The total count of physical rooms reduced by the number of rooms set to OutOfInventory | [optional] 
**maintenance** | [**Maintenance**](Maintenance.md) |  | [optional] 
**overbooking** | **Number** | The manually set overbooking | [optional] 
**roomCount** | **Number** | The total count of physical rooms | [optional] 
**sold** | **Number** | The count of rooms sold. It sums up the rooms sold through individual reservations plus rooms blocked definitely | [optional] 
**toSell** | **Number** | The number of rooms still available to sell. It is available reduced by the already sold rooms | [optional] 


