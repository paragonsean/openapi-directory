

# ClusterPendingModifiedValues

This data type is used as a response element in the <code>ModifyDBCluster</code> operation and contains changes that will be applied during the next maintenance window.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pendingCloudwatchLogsExports** | [**ClusterPendingModifiedValuesPendingCloudwatchLogsExports**](ClusterPendingModifiedValuesPendingCloudwatchLogsExports.md) |  |  [optional] |
|**dbClusterIdentifier** | [**String**](String.md) |  |  [optional] |
|**iaMDatabaseAuthenticationEnabled** | [**Boolean**](Boolean.md) |  |  [optional] |
|**engineVersion** | [**String**](String.md) |  |  [optional] |
|**backupRetentionPeriod** | [**Integer**](Integer.md) |  |  [optional] |
|**allocatedStorage** | [**Integer**](Integer.md) |  |  [optional] |
|**iops** | [**Integer**](Integer.md) |  |  [optional] |



