

# ReservationDetails


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addonRates** | [**List&lt;AddonRate&gt;**](AddonRate.md) | A breakdown of addon services with their prices for every stay day |  [optional] |
|**adults** | **Integer** | The number of adults per room |  [optional] |
|**arrivalDate** | **OffsetDateTime** | The arrival date of the guests |  [optional] |
|**channelCode** | **String** | The channel code for this reservation. You can find available channels in the codes for the hotel. |  [optional] |
|**comment** | **String** | The comment you want to add for this reservation |  [optional] |
|**company** | [**Company**](Company.md) |  |  [optional] |
|**contact** | [**Contact**](Contact.md) |  |  [optional] |
|**departureDate** | **OffsetDateTime** | The departure date of the guests |  [optional] |
|**externalId** | **String** | The external id for this reservation. You can put here your own id used by you or the external system              you integrate hetras with |  [optional] |
|**groupCode** | **String** | The group code based on which the reservation will be created. |  [optional] |
|**guarantee** | [**Guarantee**](Guarantee.md) |  |  [optional] |
|**guests** | [**List&lt;Customer&gt;**](Customer.md) | A list of guests with some basic guest details |  [optional] |
|**hotelId** | **Integer** | The id of the hotel this reservation is valid for |  |
|**paymentMethod** | [**PaymentMethodEnum**](#PaymentMethodEnum) | The payment method for this reservation |  [optional] |
|**prepayDiscount** | **Double** | If you create a booking for a rateplan requiring prepayment this amount will be deducted from the booking value before              the prepayment will be taken. This feature is useful when the booker redeems a gift voucher and you want to               only capture the remaining amount from the guest´s credit card |  [optional] |
|**roomRates** | [**List&lt;RoomRate&gt;**](RoomRate.md) | A breakdown of room rates specified for every stay day |  [optional] |
|**rooms** | **Integer** | The number of rooms this reservation is for. After a multi-room booking is done there will be               one reservation in hetras for all rooms. The hotel staff then will split this reservation into              one reservation per room to be able to check in the guests |  [optional] |
|**travelAgent** | [**Company**](Company.md) |  |  [optional] |



## Enum: PaymentMethodEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| CASH | &quot;Cash&quot; |
| CREDIT_CARD | &quot;CreditCard&quot; |
| WIRE_TRANSFER | &quot;WireTransfer&quot; |
| CHARGE_TO_COMPANY | &quot;ChargeToCompany&quot; |
| CHECK | &quot;Check&quot; |
| VOUCHER | &quot;Voucher&quot; |
| DEBIT_CARD | &quot;DebitCard&quot; |
| TOKEN | &quot;Token&quot; |
| MISCELLANEOUS | &quot;Miscellaneous&quot; |
| DIGITAL_PAYMENT | &quot;DigitalPayment&quot; |



