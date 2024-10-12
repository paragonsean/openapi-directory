

# UpgradeAppliedSchemaRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**publishedSchemaArn** | **String** | The revision of the published schema to upgrade the directory to. |  |
|**directoryArn** | **String** | The ARN for the directory to which the upgraded schema will be applied. |  |
|**dryRun** | **Boolean** | Used for testing whether the major version schemas are backward compatible or not. If schema compatibility fails, an exception would be thrown else the call would succeed but no changes will be saved. This parameter is optional. |  [optional] |



