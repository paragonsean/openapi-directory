

# RateResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**Map&lt;String, LinkObject&gt;**](LinkObject.md) | Collection of links to related resources |  [optional] |
|**basePrice** | **Double** | The price for this business day for the default room type and occupancy of one adult. The price is              only available for base rateplans. Please be aware that it might be the case that the default room              type is not sold by the rateplan. Nevertheless the supplements will always be added to the price for               the default room type and one adult |  [optional] |
|**businessDay** | **OffsetDateTime** | The business day |  [optional] |
|**cancellationPolicy** | [**Policy**](Policy.md) |  |  [optional] |
|**derivation** | [**PriceDerivation**](PriceDerivation.md) |  |  [optional] |
|**minimumGuaranteeType** | [**MinimumGuaranteeTypeEnum**](#MinimumGuaranteeTypeEnum) | The minimum guarantee |  [optional] |
|**perPersonSurcharge** | **Double** | The surcharge per additional adult staying in the room. It is only available on base rateplans |  [optional] |
|**roomTypeSupplements** | [**List&lt;RoomTypeSupplement&gt;**](RoomTypeSupplement.md) | List of supplements added to the price per room type |  [optional] |



## Enum: MinimumGuaranteeTypeEnum

| Name | Value |
|---- | -----|
| PM4_HOLD | &quot;PM4Hold&quot; |
| PM6_HOLD | &quot;PM6Hold&quot; |
| GUARANTEE_TO_CREDIT_CARD | &quot;GuaranteeToCreditCard&quot; |
| GUARANTEE_TO_GUEST_ACCOUNT | &quot;GuaranteeToGuestAccount&quot; |
| GUARANTEE_BY_TRAVEL_AGENT | &quot;GuaranteeByTravelAgent&quot; |
| GUARANTEE_BY_COMPANY | &quot;GuaranteeByCompany&quot; |
| DEPOSIT | &quot;Deposit&quot; |
| VOUCHER | &quot;Voucher&quot; |
| PREPAYMENT | &quot;Prepayment&quot; |
| NON_GUARANTEED | &quot;NonGuaranteed&quot; |
| TENTATIVE | &quot;Tentative&quot; |
| WAITLIST | &quot;Waitlist&quot; |



