

# PerformVerificationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountHolderCode** | **String** | The code of the account holder to verify. |  |
|**accountStateType** | [**AccountStateTypeEnum**](#AccountStateTypeEnum) | The state required for the account holder. &gt; Permitted values: &#x60;Processing&#x60;, &#x60;Payout&#x60;. |  |
|**tier** | **Integer** | The tier required for the account holder. |  |



## Enum: AccountStateTypeEnum

| Name | Value |
|---- | -----|
| LIMITED_PAYOUT | &quot;LimitedPayout&quot; |
| LIMITED_PROCESSING | &quot;LimitedProcessing&quot; |
| LIMITLESS_PAYOUT | &quot;LimitlessPayout&quot; |
| LIMITLESS_PROCESSING | &quot;LimitlessProcessing&quot; |
| PAYOUT | &quot;Payout&quot; |
| PROCESSING | &quot;Processing&quot; |



