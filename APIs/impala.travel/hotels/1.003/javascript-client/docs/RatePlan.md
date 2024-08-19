# ImpalaHotelBookingApi.RatePlan

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjustments** | [**[RateAdjustment]**](RateAdjustment.md) | A list of adjustments that could apply to this rate. | [optional] 
**components** | [**[RateComponent]**](RateComponent.md) |  | [optional] 
**conditions** | [**Conditions**](Conditions.md) |  | 
**description** | **String** | Human-readable summary describing this rate plan. | 
**hotelId** | **String** | The unique identifier of the hotel this rate plan is available for. | 
**ratePlanId** | **Number** | The integer identifier of this rate plan. | 
**restrictions** | [**RatePlanRestrictions**](RatePlanRestrictions.md) |  | 
**roomTypes** | [**[RatePlanRoomType]**](RatePlanRoomType.md) | A list of room types this rate plan is bookable for. | 


