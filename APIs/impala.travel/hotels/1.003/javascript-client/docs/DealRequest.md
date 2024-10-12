# ImpalaHotelBookingApi.DealRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bookingWindowRestriction** | [**DealRequestBookingWindowRestriction**](DealRequestBookingWindowRestriction.md) |  | 
**cancellationPolicy** | [**DealRequestCancellationPolicy**](DealRequestCancellationPolicy.md) |  | 
**commission** | [**DealRequestCommission**](DealRequestCommission.md) |  | 
**conditions** | **[String]** | A deal may have conditions set to it. For example, the deal may only apply for a closed user group (PRIVATE_RATE) or sold along with another component e.g flights (PACKAGED) | 
**createdAt** | **Date** | Date and time (in UTC and ISO 8601 format) when the deal&#39;s static content was created. | 
**dealRequestId** | **String** | The unique identifier for this deal request | 
**dealRequestStatus** | **String** | The status of the deal request. | 
**dealType** | **String** | The type of the deal request. | 
**discount** | [**DealRequestDiscount**](DealRequestDiscount.md) |  | 
**lengthOfStay** | [**DealRequestLengthOfStay**](DealRequestLengthOfStay.md) |  | 
**sellableInDateRanges** | [**[DealRequestSellableInDateRangesInner]**](DealRequestSellableInDateRangesInner.md) | The date ranges within which you can sell rates using this deal. | 
**specialInstructions** | **String** | These are conditions set by you the seller or the hotel for which the deal can be sold. For example: this deal can only be sold on mobile. Any specialInstructions will override other variables, for example, if an instruction includes: All bookings are non refundable, this will override any pre-existing cancellationPolicy.  | 
**stayDateRanges** | [**[DealRequestStayDateRangesInner]**](DealRequestStayDateRangesInner.md) | The date ranges within which guests you sell can stay at the hotel with the conditions you agree, given the hotel has rooms available. | 
**updatedAt** | **Date** | Date and time (in UTC and ISO 8601 format) when the deal&#39;s static content was last updated. | 



## Enum: [ConditionsEnum]


* `PACKAGED` (value: `"PACKAGED"`)

* `PRIVATE_RATE` (value: `"PRIVATE_RATE"`)





## Enum: DealRequestStatusEnum


* `PENDING` (value: `"PENDING"`)

* `ACCEPTED` (value: `"ACCEPTED"`)

* `REJECTED` (value: `"REJECTED"`)





## Enum: DealTypeEnum


* `SENT_ON_IMPALA` (value: `"SENT_ON_IMPALA"`)

* `EXTERNAL` (value: `"EXTERNAL"`)

* `IMPALA_SHARED` (value: `"IMPALA_SHARED"`)




