# ImpalaHotelBookingApi.HotelAgreementStub

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | **[String]** | A deal may have conditions set to it. For example, the deal may only apply for a closed user group (PRIVATE_RATE) or sold along with another component e.g flights (PACKAGED) | [optional] 
**dealId** | **String** | The unique identifier for this deal request. | 
**dealsSellable** | [**HotelAgreementStubDealsSellable**](HotelAgreementStubDealsSellable.md) |  | [optional] 
**discount** | [**HotelAgreementStubDiscount**](HotelAgreementStubDiscount.md) |  | [optional] 
**hotelAgreementId** | **String** | Unique identifier for the hotel agreement. | 
**href** | **String** | URI that allows access to the full deal information. | [optional] 
**specialInstructions** | **String** | These are conditions set by you the seller or the hotel for which the deal can be sold. For example: this deal can only be sold on mobile. Any specialInstructions will override other variables, for example, if an instruction includes: All bookings are non refundable, this will override any pre-existing cancellationPolicy. | 


