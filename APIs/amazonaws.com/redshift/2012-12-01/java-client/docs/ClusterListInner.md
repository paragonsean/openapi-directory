

# ClusterListInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clusterIdentifier** | [**String**](String.md) |  |  [optional] |
|**nodeType** | [**String**](String.md) |  |  [optional] |
|**clusterStatus** | [**String**](String.md) |  |  [optional] |
|**clusterAvailabilityStatus** | [**String**](String.md) |  |  [optional] |
|**modifyStatus** | [**String**](String.md) |  |  [optional] |
|**masterUsername** | [**String**](String.md) |  |  [optional] |
|**dbName** | [**String**](String.md) |  |  [optional] |
|**endpoint** | [**ClusterEndpoint**](ClusterEndpoint.md) |  |  [optional] |
|**clusterCreateTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**automatedSnapshotRetentionPeriod** | [**Integer**](Integer.md) |  |  [optional] |
|**manualSnapshotRetentionPeriod** | [**Integer**](Integer.md) |  |  [optional] |
|**clusterSecurityGroups** | [**List**](List.md) |  |  [optional] |
|**vpcSecurityGroups** | [**List**](List.md) |  |  [optional] |
|**clusterParameterGroups** | [**List**](List.md) |  |  [optional] |
|**clusterSubnetGroupName** | [**String**](String.md) |  |  [optional] |
|**vpcId** | [**String**](String.md) |  |  [optional] |
|**availabilityZone** | [**String**](String.md) |  |  [optional] |
|**preferredMaintenanceWindow** | [**String**](String.md) |  |  [optional] |
|**pendingModifiedValues** | [**ClusterPendingModifiedValues**](ClusterPendingModifiedValues.md) |  |  [optional] |
|**clusterVersion** | [**String**](String.md) |  |  [optional] |
|**allowVersionUpgrade** | [**Boolean**](Boolean.md) |  |  [optional] |
|**numberOfNodes** | [**Integer**](Integer.md) |  |  [optional] |
|**publiclyAccessible** | [**Boolean**](Boolean.md) |  |  [optional] |
|**encrypted** | [**Boolean**](Boolean.md) |  |  [optional] |
|**restoreStatus** | [**ClusterRestoreStatus**](ClusterRestoreStatus.md) |  |  [optional] |
|**dataTransferProgress** | [**ClusterDataTransferProgress**](ClusterDataTransferProgress.md) |  |  [optional] |
|**hsmStatus** | [**ClusterHsmStatus**](ClusterHsmStatus.md) |  |  [optional] |
|**clusterSnapshotCopyStatus** | [**ClusterClusterSnapshotCopyStatus**](ClusterClusterSnapshotCopyStatus.md) |  |  [optional] |
|**clusterPublicKey** | [**String**](String.md) |  |  [optional] |
|**clusterNodes** | [**List**](List.md) |  |  [optional] |
|**elasticIpStatus** | [**ClusterElasticIpStatus**](ClusterElasticIpStatus.md) |  |  [optional] |
|**clusterRevisionNumber** | [**String**](String.md) |  |  [optional] |
|**tags** | [**List**](List.md) |  |  [optional] |
|**kmsKeyId** | [**String**](String.md) |  |  [optional] |
|**enhancedVpcRouting** | [**Boolean**](Boolean.md) |  |  [optional] |
|**iamRoles** | [**List**](List.md) |  |  [optional] |
|**pendingActions** | [**List**](List.md) |  |  [optional] |
|**maintenanceTrackName** | [**String**](String.md) |  |  [optional] |
|**elasticResizeNumberOfNodeOptions** | [**String**](String.md) |  |  [optional] |
|**deferredMaintenanceWindows** | [**List**](List.md) |  |  [optional] |
|**snapshotScheduleIdentifier** | [**String**](String.md) |  |  [optional] |
|**snapshotScheduleState** | [**ScheduleState**](ScheduleState.md) |  |  [optional] |
|**expectedNextSnapshotScheduleTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**expectedNextSnapshotScheduleTimeStatus** | [**String**](String.md) |  |  [optional] |
|**nextMaintenanceWindowStartTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**resizeInfo** | [**ClusterResizeInfo**](ClusterResizeInfo.md) |  |  [optional] |
|**availabilityZoneRelocationStatus** | [**String**](String.md) |  |  [optional] |
|**clusterNamespaceArn** | [**String**](String.md) |  |  [optional] |
|**totalStorageCapacityInMegaBytes** | [**Integer**](Integer.md) |  |  [optional] |
|**aquaConfiguration** | [**ClusterAquaConfiguration**](ClusterAquaConfiguration.md) |  |  [optional] |
|**defaultIamRoleArn** | [**String**](String.md) |  |  [optional] |
|**reservedNodeExchangeStatus** | [**ClusterReservedNodeExchangeStatus**](ClusterReservedNodeExchangeStatus.md) |  |  [optional] |
|**customDomainName** | [**String**](String.md) |  |  [optional] |
|**customDomainCertificateArn** | [**String**](String.md) |  |  [optional] |
|**customDomainCertificateExpiryDate** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |



