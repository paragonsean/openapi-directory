# HetrasHotelApiVersion0.RateResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**{String: LinkObject}**](LinkObject.md) | Collection of links to related resources | [optional] 
**basePrice** | **Number** | The price for this business day for the default room type and occupancy of one adult. The price is              only available for base rateplans. Please be aware that it might be the case that the default room              type is not sold by the rateplan. Nevertheless the supplements will always be added to the price for               the default room type and one adult | [optional] 
**businessDay** | **Date** | The business day | [optional] 
**cancellationPolicy** | [**Policy**](Policy.md) |  | [optional] 
**derivation** | [**PriceDerivation**](PriceDerivation.md) |  | [optional] 
**minimumGuaranteeType** | **String** | The minimum guarantee | [optional] 
**perPersonSurcharge** | **Number** | The surcharge per additional adult staying in the room. It is only available on base rateplans | [optional] 
**roomTypeSupplements** | [**[RoomTypeSupplement]**](RoomTypeSupplement.md) | List of supplements added to the price per room type | [optional] 



## Enum: MinimumGuaranteeTypeEnum


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




