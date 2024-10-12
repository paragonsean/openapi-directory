# SensitiveDataProtectionDlp.GooglePrivacyDlpV2DiscoveryTableModifiedCadence

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **String** | How frequently data profiles can be updated when tables are modified. Defaults to never. | [optional] 
**types** | **[String]** | The type of events to consider when deciding if the table has been modified and should have the profile updated. Defaults to MODIFIED_TIMESTAMP. | [optional] 



## Enum: FrequencyEnum


* `UNSPECIFIED` (value: `"UPDATE_FREQUENCY_UNSPECIFIED"`)

* `NEVER` (value: `"UPDATE_FREQUENCY_NEVER"`)

* `DAILY` (value: `"UPDATE_FREQUENCY_DAILY"`)

* `MONTHLY` (value: `"UPDATE_FREQUENCY_MONTHLY"`)





## Enum: [TypesEnum]


* `MODIFICATION_UNSPECIFIED` (value: `"TABLE_MODIFICATION_UNSPECIFIED"`)

* `MODIFIED_TIMESTAMP` (value: `"TABLE_MODIFIED_TIMESTAMP"`)




