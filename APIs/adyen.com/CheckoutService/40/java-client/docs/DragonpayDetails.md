

# DragonpayDetails


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**issuer** | **String** | The Dragonpay issuer value of the shopper&#39;s selected bank. Set this to an **id** of a Dragonpay issuer to preselect it. |  |
|**shopperEmail** | **String** | The shopper’s email address. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | **dragonpay** |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| EBANKING | &quot;dragonpay_ebanking&quot; |
| OTC_BANKING | &quot;dragonpay_otc_banking&quot; |
| OTC_NON_BANKING | &quot;dragonpay_otc_non_banking&quot; |
| OTC_PHILIPPINES | &quot;dragonpay_otc_philippines&quot; |



