# GraphHopperDirectionsApi.Vehicle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_break** | [**VehicleBreak**](VehicleBreak.md) |  | [optional] 
**earliestStart** | **Number** | Earliest start of vehicle in seconds. It is recommended to use the unix timestamp. | [optional] [default to 0]
**endAddress** | [**Address**](Address.md) |  | [optional] 
**latestEnd** | **Number** | Latest end of vehicle in seconds, i.e. the time the vehicle needs to be at its end location at latest. | [optional] 
**maxActivities** | **Number** | Specifies the maximum number of activities a vehicle can conduct. | [optional] 
**maxDistance** | **Number** | Specifies the maximum distance (in meters) a vehicle can go. | [optional] 
**maxDrivingTime** | **Number** | Specifies the maximum drive time (in seconds) a vehicle/driver can go, i.e. the maximum time on the road (service and waiting times are not included here) | [optional] 
**maxJobs** | **Number** | Specifies the maximum number of jobs a vehicle can load. | [optional] 
**minJobs** | **Number** | Specifies the minimum number of jobs a vehicle should load. This is a soft constraint, i.e. if it is not possible to fulfill “min_jobs”, we will still try to get as close as possible to this constraint. | [optional] 
**moveToEndAddress** | **Boolean** | Indicates whether a vehicle should be moved even though it has not been assigned any jobs. | [optional] 
**returnToDepot** | **Boolean** | If it is false, the algorithm decides where to end the vehicle route. It ends in one of your customers&#39; locations. The end is chosen such that it contributes to the overall objective function, e.g. min transport_time. If it is true, you can either specify a specific end location (which is then regarded as end depot) or you can leave it and the driver returns to its start location. | [optional] [default to true]
**skills** | **[String]** | Array of skills, i.e. array of string (not case sensitive). | [optional] 
**startAddress** | [**Address**](Address.md) |  | 
**typeId** | **String** | The type ID assigns a vehicle type to this vehicle. You can specify types in the array of vehicle types. If you omit the type ID, the default type is used. The default type is a &#x60;car&#x60; with a capacity of 0. | [optional] [default to &#39;default-type&#39;]
**vehicleId** | **String** | Specifies the ID of the vehicle. Ids must be unique, i.e. if there are two vehicles with the same ID, an error is returned. | 


