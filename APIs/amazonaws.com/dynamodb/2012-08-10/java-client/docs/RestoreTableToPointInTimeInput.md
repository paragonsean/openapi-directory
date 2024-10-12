

# RestoreTableToPointInTimeInput


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**sourceTableArn** | [**String**](String.md) |  |  [optional] |
|**sourceTableName** | [**String**](String.md) |  |  [optional] |
|**targetTableName** | [**String**](String.md) |  |  |
|**useLatestRestorableTime** | [**Boolean**](Boolean.md) |  |  [optional] |
|**restoreDateTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**billingModeOverride** | [**BillingMode**](BillingMode.md) |  |  [optional] |
|**globalSecondaryIndexOverride** | [**List**](List.md) |  |  [optional] |
|**localSecondaryIndexOverride** | [**List**](List.md) |  |  [optional] |
|**provisionedThroughputOverride** | [**RestoreTableFromBackupInputProvisionedThroughputOverride**](RestoreTableFromBackupInputProvisionedThroughputOverride.md) |  |  [optional] |
|**ssESpecificationOverride** | [**RestoreTableFromBackupInputSSESpecificationOverride**](RestoreTableFromBackupInputSSESpecificationOverride.md) |  |  [optional] |



