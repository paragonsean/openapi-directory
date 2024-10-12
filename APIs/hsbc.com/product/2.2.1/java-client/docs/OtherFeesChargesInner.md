

# OtherFeesChargesInner

Contains details of fees and charges which are not associated with either Overdraft or features/benefits

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**feeChargeCap** | [**List&lt;FeeChargeCapInner&gt;**](FeeChargeCapInner.md) | Details about any caps (maximum charges) that apply to a particular fee/charge |  [optional] |
|**feeChargeDetail** | [**List&lt;FeeChargeDetailInner&gt;**](FeeChargeDetailInner.md) | Other fees/charges details |  |
|**otherTariffType** | **Object** | Other tariff type which is not in the standard list. |  [optional] |
|**tariffName** | **String** | Name of the tariff |  [optional] |
|**tariffType** | [**TariffTypeEnum**](#TariffTypeEnum) | TariffType which defines the fee and charges. |  [optional] |



## Enum: TariffTypeEnum

| Name | Value |
|---- | -----|
| ELECTRONIC | &quot;Electronic&quot; |
| MIXED | &quot;Mixed&quot; |
| OTHER | &quot;Other&quot; |



