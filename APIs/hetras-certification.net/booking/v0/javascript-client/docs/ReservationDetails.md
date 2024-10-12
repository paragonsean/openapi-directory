# HetrasBookingApiVersion0.ReservationDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addonRates** | [**[AddonRate]**](AddonRate.md) | A breakdown of addon services with their prices for every stay day | [optional] 
**adults** | **Number** | The number of adults per room | [optional] 
**arrivalDate** | **Date** | The arrival date of the guests | [optional] 
**channelCode** | **String** | The channel code for this reservation. You can find available channels in the codes for the hotel. | [optional] 
**comment** | **String** | The comment you want to add for this reservation | [optional] 
**company** | [**Company**](Company.md) |  | [optional] 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**departureDate** | **Date** | The departure date of the guests | [optional] 
**externalId** | **String** | The external id for this reservation. You can put here your own id used by you or the external system              you integrate hetras with | [optional] 
**groupCode** | **String** | The group code based on which the reservation will be created. | [optional] 
**guarantee** | [**Guarantee**](Guarantee.md) |  | [optional] 
**guests** | [**[Customer]**](Customer.md) | A list of guests with some basic guest details | [optional] 
**hotelId** | **Number** | The id of the hotel this reservation is valid for | 
**paymentMethod** | **String** | The payment method for this reservation | [optional] 
**prepayDiscount** | **Number** | If you create a booking for a rateplan requiring prepayment this amount will be deducted from the booking value before              the prepayment will be taken. This feature is useful when the booker redeems a gift voucher and you want to               only capture the remaining amount from the guest´s credit card | [optional] 
**roomRates** | [**[RoomRate]**](RoomRate.md) | A breakdown of room rates specified for every stay day | [optional] 
**rooms** | **Number** | The number of rooms this reservation is for. After a multi-room booking is done there will be               one reservation in hetras for all rooms. The hotel staff then will split this reservation into              one reservation per room to be able to check in the guests | [optional] 
**travelAgent** | [**Company**](Company.md) |  | [optional] 



## Enum: PaymentMethodEnum


* `None` (value: `"None"`)

* `Cash` (value: `"Cash"`)

* `CreditCard` (value: `"CreditCard"`)

* `WireTransfer` (value: `"WireTransfer"`)

* `ChargeToCompany` (value: `"ChargeToCompany"`)

* `Check` (value: `"Check"`)

* `Voucher` (value: `"Voucher"`)

* `DebitCard` (value: `"DebitCard"`)

* `Token` (value: `"Token"`)

* `Miscellaneous` (value: `"Miscellaneous"`)

* `DigitalPayment` (value: `"DigitalPayment"`)




