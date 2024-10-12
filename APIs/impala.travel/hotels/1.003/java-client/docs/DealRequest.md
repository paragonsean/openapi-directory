

# DealRequest

A deal request you've sent to hotels on Impala. [Read more about how deal requests work.](deal-requests-and-hotel-agreements.md)

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bookingWindowRestriction** | [**DealRequestBookingWindowRestriction**](DealRequestBookingWindowRestriction.md) |  |  |
|**cancellationPolicy** | [**DealRequestCancellationPolicy**](DealRequestCancellationPolicy.md) |  |  |
|**commission** | [**DealRequestCommission**](DealRequestCommission.md) |  |  |
|**conditions** | [**List&lt;ConditionsEnum&gt;**](#List&lt;ConditionsEnum&gt;) | A deal may have conditions set to it. For example, the deal may only apply for a closed user group (PRIVATE_RATE) or sold along with another component e.g flights (PACKAGED) |  |
|**createdAt** | **OffsetDateTime** | Date and time (in UTC and ISO 8601 format) when the deal&#39;s static content was created. |  |
|**dealRequestId** | **String** | The unique identifier for this deal request |  |
|**dealRequestStatus** | [**DealRequestStatusEnum**](#DealRequestStatusEnum) | The status of the deal request. |  |
|**dealType** | [**DealTypeEnum**](#DealTypeEnum) | The type of the deal request. |  |
|**discount** | [**DealRequestDiscount**](DealRequestDiscount.md) |  |  |
|**lengthOfStay** | [**DealRequestLengthOfStay**](DealRequestLengthOfStay.md) |  |  |
|**sellableInDateRanges** | [**Set&lt;DealRequestSellableInDateRangesInner&gt;**](DealRequestSellableInDateRangesInner.md) | The date ranges within which you can sell rates using this deal. |  |
|**specialInstructions** | **String** | These are conditions set by you the seller or the hotel for which the deal can be sold. For example: this deal can only be sold on mobile. Any specialInstructions will override other variables, for example, if an instruction includes: All bookings are non refundable, this will override any pre-existing cancellationPolicy.  |  |
|**stayDateRanges** | [**Set&lt;DealRequestStayDateRangesInner&gt;**](DealRequestStayDateRangesInner.md) | The date ranges within which guests you sell can stay at the hotel with the conditions you agree, given the hotel has rooms available. |  |
|**updatedAt** | **OffsetDateTime** | Date and time (in UTC and ISO 8601 format) when the deal&#39;s static content was last updated. |  |



## Enum: List&lt;ConditionsEnum&gt;

| Name | Value |
|---- | -----|
| PACKAGED | &quot;PACKAGED&quot; |
| PRIVATE_RATE | &quot;PRIVATE_RATE&quot; |



## Enum: DealRequestStatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;PENDING&quot; |
| ACCEPTED | &quot;ACCEPTED&quot; |
| REJECTED | &quot;REJECTED&quot; |



## Enum: DealTypeEnum

| Name | Value |
|---- | -----|
| SENT_ON_IMPALA | &quot;SENT_ON_IMPALA&quot; |
| EXTERNAL | &quot;EXTERNAL&quot; |
| IMPALA_SHARED | &quot;IMPALA_SHARED&quot; |



