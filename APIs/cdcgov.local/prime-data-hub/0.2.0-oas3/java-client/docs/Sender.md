

# Sender

An sender of reports to the data hub

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Display ready description of the sender |  |
|**format** | [**FormatEnum**](#FormatEnum) | the payload format |  |
|**meta** | [**SettingMetadata**](SettingMetadata.md) |  |  [optional] |
|**name** | **String** | Unique name for the senders, includes the orgninzation name |  |
|**organizationName** | **String** | Name of the organization that this sender belongs to |  [optional] [readonly] |
|**schema** | **String** | the schema name for this sender |  |
|**topic** | **String** | Topic of for this sender. Must match the supported topics. |  |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| CSV | &quot;CSV&quot; |



