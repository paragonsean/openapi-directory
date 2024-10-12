

# GooglePrivacyDlpV2DiscoveryTableModifiedCadence

The cadence at which to update data profiles when a table is modified.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**frequency** | [**FrequencyEnum**](#FrequencyEnum) | How frequently data profiles can be updated when tables are modified. Defaults to never. |  [optional] |
|**types** | [**List&lt;TypesEnum&gt;**](#List&lt;TypesEnum&gt;) | The type of events to consider when deciding if the table has been modified and should have the profile updated. Defaults to MODIFIED_TIMESTAMP. |  [optional] |



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
| MODIFICATION_UNSPECIFIED | &quot;TABLE_MODIFICATION_UNSPECIFIED&quot; |
| MODIFIED_TIMESTAMP | &quot;TABLE_MODIFIED_TIMESTAMP&quot; |



