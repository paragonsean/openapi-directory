

# HotelAgreement

Hotel agreements detail which hotels have accepted/rejected the conditions of your deal request. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cancellationPolicy** | [**HotelAgreementCancellationPolicy**](HotelAgreementCancellationPolicy.md) |  |  |
|**commission** | [**HotelAgreementCommission**](HotelAgreementCommission.md) |  |  |
|**conditions** | [**List&lt;ConditionsEnum&gt;**](#List&lt;ConditionsEnum&gt;) | A deal may have conditions set to it. For example, the deal may only apply for a closed user group (PRIVATE_RATE) or sold along with another component e.g flights (PACKAGED) |  |
|**createdAt** | **OffsetDateTime** | Date and time (in UTC and ISO 8601 format) when the hotel&#39;s stable content (i.e. all the details of the hotel excluding its rates) was created. |  |
|**dealsSellable** | [**HotelAgreementDealsSellable**](HotelAgreementDealsSellable.md) |  |  |
|**discount** | [**HotelAgreementDiscount**](HotelAgreementDiscount.md) |  |  |
|**hotelAgreementId** | **String** | The unique identifier for this hotel agreement |  |
|**hotelAgreementStatus** | [**HotelAgreementStatusEnum**](#HotelAgreementStatusEnum) |  |  |
|**hotelId** | **String** | The unique identifier for this deal request |  |
|**lengthOfStay** | [**HotelAgreementLengthOfStay**](HotelAgreementLengthOfStay.md) |  |  |
|**sellableInDateRanges** | [**Set&lt;HotelAgreementSellableInDateRangesInner&gt;**](HotelAgreementSellableInDateRangesInner.md) | The date ranges within which you can sell rates using this deal. |  |
|**specialInstructions** | **String** | These are conditions set by you the seller or the hotel for which the deal can be sold. For example: this deal can only be sold on mobile. Any specialInstructions will override other variables, for example, if an instruction includes: All bookings are non refundable, this will override any pre-existing cancellationPolicy. |  |
|**stayDateRanges** | [**Set&lt;DealRequestStayDateRangesInner&gt;**](DealRequestStayDateRangesInner.md) | The date ranges within which guests you sell can stay at the hotel with the conditions you agree, given the hotel has rooms available. |  |
|**updatedAt** | **OffsetDateTime** | Date and time (in UTC and ISO 8601 format) when the hotel&#39;s stable content (i.e. all the details of the hotel excluding its rates)  was last updated. |  |



## Enum: List&lt;ConditionsEnum&gt;

| Name | Value |
|---- | -----|
| PACKAGED | &quot;PACKAGED&quot; |
| PRIVATE_RATE | &quot;PRIVATE_RATE&quot; |



## Enum: HotelAgreementStatusEnum

| Name | Value |
|---- | -----|
| ACCEPTED | &quot;ACCEPTED&quot; |
| REJECTED | &quot;REJECTED&quot; |
| PENDING | &quot;PENDING&quot; |



