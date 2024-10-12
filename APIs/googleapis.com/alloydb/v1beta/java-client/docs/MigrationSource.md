

# MigrationSource

Subset of the source instance configuration that is available when reading the cluster resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hostPort** | **String** | Output only. The host and port of the on-premises instance in host:port format |  [optional] [readonly] |
|**referenceId** | **String** | Output only. Place holder for the external source identifier(e.g DMS job name) that created the cluster. |  [optional] [readonly] |
|**sourceType** | [**SourceTypeEnum**](#SourceTypeEnum) | Output only. Type of migration source. |  [optional] [readonly] |



## Enum: SourceTypeEnum

| Name | Value |
|---- | -----|
| MIGRATION_SOURCE_TYPE_UNSPECIFIED | &quot;MIGRATION_SOURCE_TYPE_UNSPECIFIED&quot; |
| DMS | &quot;DMS&quot; |



