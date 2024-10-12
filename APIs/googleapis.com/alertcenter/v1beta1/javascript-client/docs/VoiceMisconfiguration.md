# GoogleWorkspaceAlertCenterApi.VoiceMisconfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entityName** | **String** | Name of the entity whose configuration is now invalid. | [optional] 
**entityType** | **String** | Type of the entity whose configuration is now invalid. | [optional] 
**fixUri** | **String** | Link that the admin can follow to fix the issue. | [optional] 
**membersMisconfiguration** | [**TransferMisconfiguration**](TransferMisconfiguration.md) |  | [optional] 
**transferMisconfiguration** | [**TransferMisconfiguration**](TransferMisconfiguration.md) |  | [optional] 
**voicemailMisconfiguration** | [**VoicemailMisconfiguration**](VoicemailMisconfiguration.md) |  | [optional] 



## Enum: EntityTypeEnum


* `ENTITY_TYPE_UNSPECIFIED` (value: `"ENTITY_TYPE_UNSPECIFIED"`)

* `AUTO_ATTENDANT` (value: `"AUTO_ATTENDANT"`)

* `RING_GROUP` (value: `"RING_GROUP"`)




