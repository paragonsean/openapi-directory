

# AcceptedGuaranteeTypes


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accepted** | [**List&lt;AcceptedEnum&gt;**](#List&lt;AcceptedEnum&gt;) | In this list you find all the accepted guarantee types for this offer. They are sorted in ascending              order. |  [optional] |
|**minimum** | [**MinimumEnum**](#MinimumEnum) | Based on the rateplan a reservation does need to have a minimum guarantee. When you create a new booking you              can always use a higher guarantee type starting from the minimum. If you do not specify a guarantee when creating              a new booking using this offer this guarantee type will be used by default. See               https://developer.hetras.com/docs/tutorials#payment for information about guarantee types and payment details |  [optional] |



## Enum: List&lt;AcceptedEnum&gt;

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



## Enum: MinimumEnum

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



