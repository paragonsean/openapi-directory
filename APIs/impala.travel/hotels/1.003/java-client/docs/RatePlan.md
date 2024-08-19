

# RatePlan

Rate plan encapsulates rates given a set of internal conditions like cancellation policy or meal plan.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adjustments** | [**Set&lt;RateAdjustment&gt;**](RateAdjustment.md) | A list of adjustments that could apply to this rate. |  [optional] |
|**components** | [**List&lt;RateComponent&gt;**](RateComponent.md) |  |  [optional] |
|**conditions** | [**Conditions**](Conditions.md) |  |  |
|**description** | **String** | Human-readable summary describing this rate plan. |  |
|**hotelId** | **UUID** | The unique identifier of the hotel this rate plan is available for. |  |
|**ratePlanId** | **BigDecimal** | The integer identifier of this rate plan. |  |
|**restrictions** | [**RatePlanRestrictions**](RatePlanRestrictions.md) |  |  |
|**roomTypes** | [**Set&lt;RatePlanRoomType&gt;**](RatePlanRoomType.md) | A list of room types this rate plan is bookable for. |  |



