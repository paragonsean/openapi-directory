# LegalEntityManagementApi.CapabilitySettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amountPerIndustry** | [**{String: Amount}**](Amount.md) | The maximum amount a card holder can spend per industry. | [optional] 
**authorizedCardUsers** | **Boolean** | The number of card holders who can use the card. | [optional] 
**fundingSource** | **[String]** | The funding source of the card, for example **debit**. | [optional] 
**interval** | **String** | The period when the rule conditions apply. | [optional] 
**maxAmount** | [**Amount**](Amount.md) | The maximum amount a card holder can withdraw per day. | [optional] 



## Enum: [FundingSourceEnum]


* `credit` (value: `"credit"`)

* `debit` (value: `"debit"`)

* `prepaid` (value: `"prepaid"`)





## Enum: IntervalEnum


* `daily` (value: `"daily"`)

* `monthly` (value: `"monthly"`)

* `weekly` (value: `"weekly"`)




