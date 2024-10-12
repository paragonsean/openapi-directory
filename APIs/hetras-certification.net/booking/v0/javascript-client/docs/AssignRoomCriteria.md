# HetrasBookingApiVersion0.AssignRoomCriteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amenities** | **[String]** | Ensure the assigned room will have all the amenities specified. You can provide a comma seperated list of amenity codes. | [optional] 
**condition** | **String** | Here you can define to limit the list of assignable rooms based on their current condition. This is only applicable if the underlying reservation              is due to arrive on the current business day. If not set by default only clean rooms will be assigned. | [optional] 
**includeOutOfService** | **Boolean** | Sometimes you might want to assign rooms which are out of service (small repair needed) if no other rooms are available anymore. If you set              include_out_of_service to true even those rooms will be considered. The default is false. | [optional] 
**locations** | **[String]** | Ensure the assigned room will have at least one of the specified locations. You can provide a comma seperated list of location codes. | [optional] 
**respectGuestPreferences** | **Boolean** | Defines if the preferences for locations, amenities and views of the primary guest should be taken into account. All defined preferences in the guest              profile override any of the criteria defined in the request body. The default is false. | [optional] 
**roomNumber** | **String** | If you define a specific room number this room will be assigned if not assigned to another reservation, has proper room type and is not OutOfOrder               or OutOfInventory for the stay duration of the underlying reservaton. If set all other filter criteria will be ignored. | [optional] 
**views** | **[String]** | Ensure the assigned room will have at least one of the specified views. You can provide a comma seperated list of view codes. | [optional] 



## Enum: ConditionEnum


* `CleanNotInspected` (value: `"CleanNotInspected"`)

* `Clean` (value: `"Clean"`)

* `Dirty` (value: `"Dirty"`)

* `Any` (value: `"Any"`)




