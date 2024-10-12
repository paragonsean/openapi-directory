

# ModifyDBClusterMessage

Represents the input to <a>ModifyDBCluster</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dbClusterIdentifier** | [**String**](String.md) |  |  |
|**newDBClusterIdentifier** | [**String**](String.md) |  |  [optional] |
|**applyImmediately** | [**Boolean**](Boolean.md) |  |  [optional] |
|**backupRetentionPeriod** | [**Integer**](Integer.md) |  |  [optional] |
|**dbClusterParameterGroupName** | [**String**](String.md) |  |  [optional] |
|**vpcSecurityGroupIds** | [**List**](List.md) |  |  [optional] |
|**port** | [**Integer**](Integer.md) |  |  [optional] |
|**masterUserPassword** | [**String**](String.md) |  |  [optional] |
|**preferredBackupWindow** | [**String**](String.md) |  |  [optional] |
|**preferredMaintenanceWindow** | [**String**](String.md) |  |  [optional] |
|**cloudwatchLogsExportConfiguration** | [**ModifyDBClusterMessageCloudwatchLogsExportConfiguration**](ModifyDBClusterMessageCloudwatchLogsExportConfiguration.md) |  |  [optional] |
|**engineVersion** | [**String**](String.md) |  |  [optional] |
|**allowMajorVersionUpgrade** | [**Boolean**](Boolean.md) |  |  [optional] |
|**deletionProtection** | [**Boolean**](Boolean.md) |  |  [optional] |



