

# Payment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Integer** | Amount paid by the current payment |  |
|**category** | [**CategoryEnum**](#CategoryEnum) | The category of payment method used at the time of purchase. Most common values are listed in the enum. |  |
|**paymentProfileId** | **String** | Unique identifier of the payment profile used by current payment |  |
|**subcategory** | [**SubcategoryEnum**](#SubcategoryEnum) | The subcategory of payment method used at the time of purchase.  This field is only set for certain payment categories, such as ACH and CREDIT_CARD. Most common values are listed in the enum. |  [optional] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| CREDIT_CARD | &quot;CREDIT_CARD&quot; |
| PAYPAL | &quot;PAYPAL&quot; |
| ACH | &quot;ACH&quot; |
| GIFT_CARD | &quot;GIFT_CARD&quot; |
| IN_STORE_CREDIT | &quot;IN_STORE_CREDIT&quot; |
| PREPAID | &quot;PREPAID&quot; |



## Enum: SubcategoryEnum

| Name | Value |
|---- | -----|
| CHECKING_PERSONAL | &quot;CHECKING_PERSONAL&quot; |
| CHECKING_BUSINESS | &quot;CHECKING_BUSINESS&quot; |
| VISA | &quot;VISA&quot; |
| MASTER_CARD | &quot;MASTER_CARD&quot; |
| AMEX | &quot;AMEX&quot; |
| JCB | &quot;JCB&quot; |
| UNIONPAY | &quot;UNIONPAY&quot; |



