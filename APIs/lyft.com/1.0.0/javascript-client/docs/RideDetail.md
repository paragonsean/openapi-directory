# Lyft.RideDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**beaconColor** | **String** | Hex color code of the driver AMP device. | [optional] 
**canCancel** | **[String]** |  | [optional] 
**canceledBy** | **String** | The role of user who canceled the ride (if applicable) | [optional] 
**cancellationPrice** | [**CancellationCost**](CancellationCost.md) | The cost of cancellation if there would be a penalty | [optional] 
**destination** | [**RideLocation**](RideLocation.md) | The *requested* location for passenger drop off | [optional] 
**distanceMiles** | **Number** | The distance, in miles, that this ride traveled. This field is only present after drop-off | [optional] 
**driver** | [**DriverDetail**](DriverDetail.md) |  | [optional] 
**dropoff** | [**PickupDropoffLocation**](PickupDropoffLocation.md) | The *actual* location of passenger drop off | [optional] 
**durationSeconds** | **Number** | Duration of the ride in seconds from pickup to drop-off. This field is only present after drop-off. | [optional] 
**feedback** | **String** | The written feedback the user left for this ride | [optional] 
**generatedAt** | **Date** | The request timestamp in date and time | [optional] 
**lineItems** | [**[LineItem]**](LineItem.md) | The break down of cost | [optional] 
**location** | [**CurrentRideLocation**](CurrentRideLocation.md) | The *current* location info of the ride | [optional] 
**origin** | [**RideLocation**](RideLocation.md) | The *requested* location for passenger pickup | [optional] 
**passenger** | [**PassengerDetail**](PassengerDetail.md) |  | [optional] 
**pickup** | [**PickupDropoffLocation**](PickupDropoffLocation.md) | The *actual* location of passenger pickup | [optional] 
**price** | [**Cost**](Cost.md) | The total price for the current ride | [optional] 
**pricingDetailsUrl** | **String** | The web view showing the pricing structure for the geographic area where the ride was taken  | [optional] 
**primetimePercentage** | **String** | The Prime Time percentage applied to the base price | [optional] 
**rating** | **Number** | The rating the user left for this ride, from 1 to 5 | [optional] 
**requestedAt** | **Date** | The ride requested timestamp in date and time | [optional] 
**rideId** | **String** | The unique ID of this ride | [optional] 
**rideProfile** | [**RideProfileEnum**](RideProfileEnum.md) | Indicates whether the ride was requested from the business profile or personal profile of the user.  | [optional] 
**rideType** | [**RideTypeEnumWithOther**](RideTypeEnumWithOther.md) |  | [optional] 
**routeUrl** | **String** | The web view showing the passenger, driver, and route for this ride. This field will only be present for rides created through this API, or that have been shared through the \&quot;Share my Route\&quot; feature  | [optional] 
**status** | [**RideStatusEnum**](RideStatusEnum.md) |  | [optional] 
**vehicle** | [**VehicleDetail**](VehicleDetail.md) |  | [optional] 



## Enum: [CanCancelEnum]


* `driver` (value: `"driver"`)

* `passenger` (value: `"passenger"`)

* `dispatcher` (value: `"dispatcher"`)




