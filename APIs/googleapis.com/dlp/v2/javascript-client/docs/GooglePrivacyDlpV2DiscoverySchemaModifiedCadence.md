# SensitiveDataProtectionDlp.GooglePrivacyDlpV2DiscoverySchemaModifiedCadence

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency** | **String** | How frequently profiles may be updated when schemas are modified. Defaults to monthly. | [optional] 
**types** | **[String]** | The type of events to consider when deciding if the table&#39;s schema has been modified and should have the profile updated. Defaults to NEW_COLUMNS. | [optional] 



## Enum: FrequencyEnum


* `UNSPECIFIED` (value: `"UPDATE_FREQUENCY_UNSPECIFIED"`)

* `NEVER` (value: `"UPDATE_FREQUENCY_NEVER"`)

* `DAILY` (value: `"UPDATE_FREQUENCY_DAILY"`)

* `MONTHLY` (value: `"UPDATE_FREQUENCY_MONTHLY"`)





## Enum: [TypesEnum]


* `MODIFICATION_UNSPECIFIED` (value: `"SCHEMA_MODIFICATION_UNSPECIFIED"`)

* `NEW_COLUMNS` (value: `"SCHEMA_NEW_COLUMNS"`)

* `REMOVED_COLUMNS` (value: `"SCHEMA_REMOVED_COLUMNS"`)




