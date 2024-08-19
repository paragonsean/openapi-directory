

# CapabilitySettings


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amountPerIndustry** | [**Map&lt;String, Amount&gt;**](Amount.md) |  |  [optional] |
|**authorizedCardUsers** | **Boolean** |  |  [optional] |
|**fundingSource** | [**List&lt;FundingSourceEnum&gt;**](#List&lt;FundingSourceEnum&gt;) |  |  [optional] |
|**interval** | [**IntervalEnum**](#IntervalEnum) |  |  [optional] |
|**maxAmount** | [**Amount**](Amount.md) |  |  [optional] |



## Enum: List&lt;FundingSourceEnum&gt;

| Name | Value |
|---- | -----|
| CREDIT | &quot;credit&quot; |
| DEBIT | &quot;debit&quot; |
| PREPAID | &quot;prepaid&quot; |



## Enum: IntervalEnum

| Name | Value |
|---- | -----|
| DAILY | &quot;daily&quot; |
| MONTHLY | &quot;monthly&quot; |
| WEEKLY | &quot;weekly&quot; |



