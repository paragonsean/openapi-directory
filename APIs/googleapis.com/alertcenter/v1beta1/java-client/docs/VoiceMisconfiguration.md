

# VoiceMisconfiguration

An alert triggered when Google Voice configuration becomes invalid, generally due to an external entity being modified or deleted.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entityName** | **String** | Name of the entity whose configuration is now invalid. |  [optional] |
|**entityType** | [**EntityTypeEnum**](#EntityTypeEnum) | Type of the entity whose configuration is now invalid. |  [optional] |
|**fixUri** | **String** | Link that the admin can follow to fix the issue. |  [optional] |
|**membersMisconfiguration** | [**TransferMisconfiguration**](TransferMisconfiguration.md) |  |  [optional] |
|**transferMisconfiguration** | [**TransferMisconfiguration**](TransferMisconfiguration.md) |  |  [optional] |
|**voicemailMisconfiguration** | [**VoicemailMisconfiguration**](VoicemailMisconfiguration.md) |  |  [optional] |



## Enum: EntityTypeEnum

| Name | Value |
|---- | -----|
| ENTITY_TYPE_UNSPECIFIED | &quot;ENTITY_TYPE_UNSPECIFIED&quot; |
| AUTO_ATTENDANT | &quot;AUTO_ATTENDANT&quot; |
| RING_GROUP | &quot;RING_GROUP&quot; |



