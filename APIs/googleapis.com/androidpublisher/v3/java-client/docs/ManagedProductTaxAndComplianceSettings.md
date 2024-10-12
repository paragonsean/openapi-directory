

# ManagedProductTaxAndComplianceSettings

Details about taxation and legal compliance for managed products.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eeaWithdrawalRightType** | [**EeaWithdrawalRightTypeEnum**](#EeaWithdrawalRightTypeEnum) | Digital content or service classification for products distributed to users in the European Economic Area (EEA). The withdrawal regime under EEA consumer laws depends on this classification. Refer to the [Help Center article](https://support.google.com/googleplay/android-developer/answer/10463498) for more information. |  [optional] |
|**isTokenizedDigitalAsset** | **Boolean** | Whether this in-app product is declared as a product representing a tokenized digital asset. |  [optional] |
|**taxRateInfoByRegionCode** | [**Map&lt;String, RegionalTaxRateInfo&gt;**](RegionalTaxRateInfo.md) | A mapping from region code to tax rate details. The keys are region codes as defined by Unicode&#39;s \&quot;CLDR\&quot;. |  [optional] |



## Enum: EeaWithdrawalRightTypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;WITHDRAWAL_RIGHT_TYPE_UNSPECIFIED&quot; |
| DIGITAL_CONTENT | &quot;WITHDRAWAL_RIGHT_DIGITAL_CONTENT&quot; |
| SERVICE | &quot;WITHDRAWAL_RIGHT_SERVICE&quot; |



