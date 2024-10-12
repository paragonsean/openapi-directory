# HetrasBookingApiVersion0.GuaranteeResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guaranteeType** | **String** | The guarantee type of the reservation | [optional] 
**validToken** | **Boolean** | Tells you if there is a token for a valid creadit card on the reservation that can be used to              capture the reservations amount or to guarantee for the reservation | [optional] 



## Enum: GuaranteeTypeEnum


* `PM4Hold` (value: `"PM4Hold"`)

* `PM6Hold` (value: `"PM6Hold"`)

* `GuaranteeToCreditCard` (value: `"GuaranteeToCreditCard"`)

* `GuaranteeToGuestAccount` (value: `"GuaranteeToGuestAccount"`)

* `GuaranteeByTravelAgent` (value: `"GuaranteeByTravelAgent"`)

* `GuaranteeByCompany` (value: `"GuaranteeByCompany"`)

* `Deposit` (value: `"Deposit"`)

* `Voucher` (value: `"Voucher"`)

* `Prepayment` (value: `"Prepayment"`)

* `NonGuaranteed` (value: `"NonGuaranteed"`)

* `Tentative` (value: `"Tentative"`)

* `Waitlist` (value: `"Waitlist"`)




