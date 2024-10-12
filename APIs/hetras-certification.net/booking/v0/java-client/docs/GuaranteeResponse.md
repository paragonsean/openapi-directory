

# GuaranteeResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**guaranteeType** | [**GuaranteeTypeEnum**](#GuaranteeTypeEnum) | The guarantee type of the reservation |  [optional] |
|**validToken** | **Boolean** | Tells you if there is a token for a valid creadit card on the reservation that can be used to              capture the reservations amount or to guarantee for the reservation |  [optional] |



## Enum: GuaranteeTypeEnum

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



