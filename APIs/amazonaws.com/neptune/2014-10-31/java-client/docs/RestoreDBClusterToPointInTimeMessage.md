

# RestoreDBClusterToPointInTimeMessage


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dbClusterIdentifier** | [**String**](String.md) |  |  |
|**restoreType** | [**String**](String.md) |  |  [optional] |
|**sourceDBClusterIdentifier** | [**String**](String.md) |  |  |
|**restoreToTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**useLatestRestorableTime** | [**Boolean**](Boolean.md) |  |  [optional] |
|**port** | [**Integer**](Integer.md) |  |  [optional] |
|**dbSubnetGroupName** | [**String**](String.md) |  |  [optional] |
|**optionGroupName** | [**String**](String.md) |  |  [optional] |
|**vpcSecurityGroupIds** | [**List**](List.md) |  |  [optional] |
|**tags** | [**List**](List.md) |  |  [optional] |
|**kmsKeyId** | [**String**](String.md) |  |  [optional] |
|**enableIAMDatabaseAuthentication** | [**Boolean**](Boolean.md) |  |  [optional] |
|**enableCloudwatchLogsExports** | [**List**](List.md) |  |  [optional] |
|**dbClusterParameterGroupName** | [**String**](String.md) |  |  [optional] |
|**deletionProtection** | [**Boolean**](Boolean.md) |  |  [optional] |
|**serverlessV2ScalingConfiguration** | [**ServerlessV2ScalingConfiguration**](ServerlessV2ScalingConfiguration.md) |  |  [optional] |



