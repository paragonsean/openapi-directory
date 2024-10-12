

# BackupRule

Specifies a scheduled task used to back up a selection of resources.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ruleName** | [**String**](String.md) |  |  |
|**targetBackupVaultName** | [**String**](String.md) |  |  |
|**scheduleExpression** | [**String**](String.md) |  |  [optional] |
|**startWindowMinutes** | [**Integer**](Integer.md) |  |  [optional] |
|**completionWindowMinutes** | [**Integer**](Integer.md) |  |  [optional] |
|**lifecycle** | [**BackupRuleLifecycle**](BackupRuleLifecycle.md) |  |  [optional] |
|**recoveryPointTags** | [**Map**](Map.md) |  |  [optional] |
|**ruleId** | [**String**](String.md) |  |  [optional] |
|**copyActions** | [**List**](List.md) |  |  [optional] |
|**enableContinuousBackup** | [**Boolean**](Boolean.md) |  |  [optional] |



