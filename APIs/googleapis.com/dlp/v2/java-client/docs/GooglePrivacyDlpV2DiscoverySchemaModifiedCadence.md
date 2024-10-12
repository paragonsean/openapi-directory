

# GooglePrivacyDlpV2DiscoverySchemaModifiedCadence

The cadence at which to update data profiles when a schema is modified.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**frequency** | [**FrequencyEnum**](#FrequencyEnum) | How frequently profiles may be updated when schemas are modified. Defaults to monthly. |  [optional] |
|**types** | [**List&lt;TypesEnum&gt;**](#List&lt;TypesEnum&gt;) | The type of events to consider when deciding if the table&#39;s schema has been modified and should have the profile updated. Defaults to NEW_COLUMNS. |  [optional] |



## Enum: FrequencyEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UPDATE_FREQUENCY_UNSPECIFIED&quot; |
| NEVER | &quot;UPDATE_FREQUENCY_NEVER&quot; |
| DAILY | &quot;UPDATE_FREQUENCY_DAILY&quot; |
| MONTHLY | &quot;UPDATE_FREQUENCY_MONTHLY&quot; |



## Enum: List&lt;TypesEnum&gt;

| Name | Value |
|---- | -----|
| MODIFICATION_UNSPECIFIED | &quot;SCHEMA_MODIFICATION_UNSPECIFIED&quot; |
| NEW_COLUMNS | &quot;SCHEMA_NEW_COLUMNS&quot; |
| REMOVED_COLUMNS | &quot;SCHEMA_REMOVED_COLUMNS&quot; |



