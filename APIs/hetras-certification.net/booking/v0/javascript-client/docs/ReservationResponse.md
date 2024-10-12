# HetrasBookingApiVersion0.ReservationResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**warnings** | **[String]** | Warnings that came up when your request was processed. Your request will still be processed successfull when              you see such warnings in your response | [optional] 
**addonServices** | **[String]** | A list of addon service codes that are currently booked on the reservation. Services which are charged              once per stay are only visible before and on the day they are booked for. | [optional] 
**adults** | **Number** | The number of adults per room | [optional] 
**arrivalDate** | **Date** | The arrival date of the guests | [optional] 
**balance** | **Number** | The balance for all folios of this reservartion. It is calculated by all already charged room and service              rates plus manual charges or charges from other systems like POS minus all payments. A negative balance              indicates the reservation is overpaid, a positive balance that the guest owes the hotel money | [optional] 
**block** | [**BlockInfo**](BlockInfo.md) |  | [optional] 
**cancellationId** | **String** | Given the reservation was cancelled, this field contains the cancellation id | [optional] 
**cancellationPolicies** | [**[CancellationPolicy]**](CancellationPolicy.md) | The cancellation policies that were applicable on the date the booking was done | [optional] 
**channelCode** | **String** | The code of the channel that was used when the booking has been created. It is also known as source.               Possible values can be OTA, GDS or DIRECT, but it is configurable per hotel | [optional] 
**checkinTime** | **Date** | The real checkin time of the guests. It will be set after the checkin has been performed | [optional] 
**checkoutTime** | **Date** | The real checkout time of the guests. It will be set after the checkout has been performed | [optional] 
**comment** | **String** | The comment for this reservation | [optional] 
**company** | [**Company**](Company.md) |  | [optional] 
**confirmationId** | **String** | The confirmation id for the booking which the guest can use to check in on the kiosk, add the              booking to the mobile app etc. It is used as identifier for all reservations done with the same              booking request | [optional] 
**contact** | [**ContactResponse**](ContactResponse.md) |  | [optional] 
**created** | **Date** | Timestamp the reservation was created | [optional] 
**currency** | **String** | The currency all amounts of this reservation will be shown in | [optional] 
**departureDate** | **Date** | The departure date of the guests | [optional] 
**externalId** | **String** | The external id for this reservation is the unique identifier from the system that created the booking in hetras. It could be the id of an              OTA like Expedia or booking.com or one of the GDS systems like Amadeus or Galileo | [optional] 
**generalPolicies** | [**[GeneralPolicy]**](GeneralPolicy.md) | The general policies that were applicable on the date the booking was done | [optional] 
**guarantee** | [**GuaranteeResponse**](GuaranteeResponse.md) |  | [optional] 
**guests** | [**[CustomerResponse]**](CustomerResponse.md) | A list of guest details for this reservation | [optional] 
**hotelId** | **Number** | The id of the hotel this reservation is valid for | [optional] 
**labels** | **[String]** | A list of labels that are attached to the reservation. | [optional] 
**marketCode** | **String** | The code of the market segment the rate plan for this reservation is linked to | [optional] 
**noshowPolicy** | [**NoShowPolicy**](NoShowPolicy.md) |  | [optional] 
**paymentMethod** | **String** | The payment method for this reservation | [optional] 
**ratePlan** | [**RatePlan**](RatePlan.md) |  | [optional] 
**reservationNumber** | **Number** | The reservation number of the reservation | [optional] 
**reservationStatus** | **String** | The current status of this reservation | [optional] 
**room** | [**EmbeddedRoom**](EmbeddedRoom.md) |  | [optional] 
**roomRates** | [**[DailyRate]**](DailyRate.md) | The breakdown for all daily room rates and service charges for this reservation | [optional] 
**rooms** | **Number** | The number of rooms this reservation is valid for. After a multi-room booking is done there will be               one reservation in hetras for this booking for all rooms. The hotel staff then will split this reservation into              one reservation per room to be able to check in the guests | [optional] 
**services** | [**[Service]**](Service.md) | A list of details for all services included and addon service booked on this reservation | [optional] 
**subchannelCode** | **String** | The code of the subchannel that was used when the booking has been created. Possible values can be               BOOKING, EXPEDIA or WALKIN, but it is configurable per hotel | [optional] 
**totalStay** | [**Rate**](Rate.md) |  | [optional] 
**updated** | **Date** | Timestamp of when the reservation was changed the last time | [optional] 



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





## Enum: ReservationStatusEnum


* `Tentative` (value: `"Tentative"`)

* `Waitlisted` (value: `"Waitlisted"`)

* `OnRequest` (value: `"OnRequest"`)

* `NonGuaranteed` (value: `"NonGuaranteed"`)

* `Guaranteed` (value: `"Guaranteed"`)

* `InHouse` (value: `"InHouse"`)

* `CheckedOut` (value: `"CheckedOut"`)

* `NoShow` (value: `"NoShow"`)

* `Denied` (value: `"Denied"`)

* `Cancelled` (value: `"Cancelled"`)

* `Released` (value: `"Released"`)

* `Walked` (value: `"Walked"`)

* `Expired` (value: `"Expired"`)

* `WalkIn` (value: `"WalkIn"`)

* `Registered` (value: `"Registered"`)




