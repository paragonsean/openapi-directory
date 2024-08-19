# ImpalaHotelBookingApi.HotelAgreement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancellationPolicy** | [**HotelAgreementCancellationPolicy**](HotelAgreementCancellationPolicy.md) |  | 
**commission** | [**HotelAgreementCommission**](HotelAgreementCommission.md) |  | 
**conditions** | **[String]** | A deal may have conditions set to it. For example, the deal may only apply for a closed user group (PRIVATE_RATE) or sold along with another component e.g flights (PACKAGED) | 
**createdAt** | **Date** | Date and time (in UTC and ISO 8601 format) when the hotel&#39;s stable content (i.e. all the details of the hotel excluding its rates) was created. | 
**dealsSellable** | [**HotelAgreementDealsSellable**](HotelAgreementDealsSellable.md) |  | 
**discount** | [**HotelAgreementDiscount**](HotelAgreementDiscount.md) |  | 
**hotelAgreementId** | **String** | The unique identifier for this hotel agreement | 
**hotelAgreementStatus** | **String** |  | 
**hotelId** | **String** | The unique identifier for this deal request | 
**lengthOfStay** | [**HotelAgreementLengthOfStay**](HotelAgreementLengthOfStay.md) |  | 
**sellableInDateRanges** | [**[HotelAgreementSellableInDateRangesInner]**](HotelAgreementSellableInDateRangesInner.md) | The date ranges within which you can sell rates using this deal. | 
**specialInstructions** | **String** | These are conditions set by you the seller or the hotel for which the deal can be sold. For example: this deal can only be sold on mobile. Any specialInstructions will override other variables, for example, if an instruction includes: All bookings are non refundable, this will override any pre-existing cancellationPolicy. | 
**stayDateRanges** | [**[DealRequestStayDateRangesInner]**](DealRequestStayDateRangesInner.md) | The date ranges within which guests you sell can stay at the hotel with the conditions you agree, given the hotel has rooms available. | 
**updatedAt** | **Date** | Date and time (in UTC and ISO 8601 format) when the hotel&#39;s stable content (i.e. all the details of the hotel excluding its rates)  was last updated. | 



## Enum: [ConditionsEnum]


* `PACKAGED` (value: `"PACKAGED"`)

* `PRIVATE_RATE` (value: `"PRIVATE_RATE"`)





## Enum: HotelAgreementStatusEnum


* `ACCEPTED` (value: `"ACCEPTED"`)

* `REJECTED` (value: `"REJECTED"`)

* `PENDING` (value: `"PENDING"`)




