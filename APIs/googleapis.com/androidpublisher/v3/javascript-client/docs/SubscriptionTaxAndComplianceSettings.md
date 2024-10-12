# GooglePlayAndroidDeveloperApi.SubscriptionTaxAndComplianceSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eeaWithdrawalRightType** | **String** | Digital content or service classification for products distributed to users in the European Economic Area (EEA). The withdrawal regime under EEA consumer laws depends on this classification. Refer to the [Help Center article](https://support.google.com/googleplay/android-developer/answer/10463498) for more information. | [optional] 
**isTokenizedDigitalAsset** | **Boolean** | Whether this subscription is declared as a product representing a tokenized digital asset. | [optional] 
**taxRateInfoByRegionCode** | [**{String: RegionalTaxRateInfo}**](RegionalTaxRateInfo.md) | A mapping from region code to tax rate details. The keys are region codes as defined by Unicode&#39;s \&quot;CLDR\&quot;. | [optional] 



## Enum: EeaWithdrawalRightTypeEnum


* `TYPE_UNSPECIFIED` (value: `"WITHDRAWAL_RIGHT_TYPE_UNSPECIFIED"`)

* `DIGITAL_CONTENT` (value: `"WITHDRAWAL_RIGHT_DIGITAL_CONTENT"`)

* `SERVICE` (value: `"WITHDRAWAL_RIGHT_SERVICE"`)




