# HetrasBookingApiVersion0.AcceptedGuaranteeTypes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted** | **[String]** | In this list you find all the accepted guarantee types for this offer. They are sorted in ascending              order. | [optional] 
**minimum** | **String** | Based on the rateplan a reservation does need to have a minimum guarantee. When you create a new booking you              can always use a higher guarantee type starting from the minimum. If you do not specify a guarantee when creating              a new booking using this offer this guarantee type will be used by default. See               https://developer.hetras.com/docs/tutorials#payment for information about guarantee types and payment details | [optional] 



## Enum: [AcceptedEnum]


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





## Enum: MinimumEnum


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




