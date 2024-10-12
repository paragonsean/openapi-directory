

# DatabaseMetadata

Metadata for individual databases created in an instance. i.e. spanner instance can have multiple databases with unique configuration settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupConfiguration** | [**BackupConfiguration**](BackupConfiguration.md) |  |  [optional] |
|**backupRun** | [**BackupRun**](BackupRun.md) |  |  [optional] |
|**product** | [**Product**](Product.md) |  |  [optional] |
|**resourceId** | [**DatabaseResourceId**](DatabaseResourceId.md) |  |  [optional] |
|**resourceName** | **String** | Required. Database name. Resource name to follow CAIS resource_name format as noted here go/condor-common-datamodel |  [optional] |



