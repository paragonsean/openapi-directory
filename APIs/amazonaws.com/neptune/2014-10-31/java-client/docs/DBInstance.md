

# DBInstance

<p>Contains the details of an Amazon Neptune DB instance.</p> <p>This data type is used as a response element in the <a>DescribeDBInstances</a> action.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dbInstanceIdentifier** | [**String**](String.md) |  |  [optional] |
|**dbInstanceClass** | [**String**](String.md) |  |  [optional] |
|**engine** | [**String**](String.md) |  |  [optional] |
|**dbInstanceStatus** | [**String**](String.md) |  |  [optional] |
|**masterUsername** | [**String**](String.md) |  |  [optional] |
|**dbName** | [**String**](String.md) |  |  [optional] |
|**endpoint** | [**DBInstanceEndpoint**](DBInstanceEndpoint.md) |  |  [optional] |
|**allocatedStorage** | [**Integer**](Integer.md) |  |  [optional] |
|**instanceCreateTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**preferredBackupWindow** | [**String**](String.md) |  |  [optional] |
|**backupRetentionPeriod** | [**Integer**](Integer.md) |  |  [optional] |
|**dbSecurityGroups** | [**List**](List.md) |  |  [optional] |
|**vpcSecurityGroups** | [**List**](List.md) |  |  [optional] |
|**dbParameterGroups** | [**List**](List.md) |  |  [optional] |
|**availabilityZone** | [**String**](String.md) |  |  [optional] |
|**dbSubnetGroup** | [**DBInstanceDBSubnetGroup**](DBInstanceDBSubnetGroup.md) |  |  [optional] |
|**preferredMaintenanceWindow** | [**String**](String.md) |  |  [optional] |
|**pendingModifiedValues** | [**DBInstancePendingModifiedValues**](DBInstancePendingModifiedValues.md) |  |  [optional] |
|**latestRestorableTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**multiAZ** | [**Boolean**](Boolean.md) |  |  [optional] |
|**engineVersion** | [**String**](String.md) |  |  [optional] |
|**autoMinorVersionUpgrade** | [**Boolean**](Boolean.md) |  |  [optional] |
|**readReplicaSourceDBInstanceIdentifier** | [**String**](String.md) |  |  [optional] |
|**readReplicaDBInstanceIdentifiers** | [**List**](List.md) |  |  [optional] |
|**readReplicaDBClusterIdentifiers** | [**List**](List.md) |  |  [optional] |
|**licenseModel** | [**String**](String.md) |  |  [optional] |
|**iops** | [**Integer**](Integer.md) |  |  [optional] |
|**optionGroupMemberships** | [**List**](List.md) |  |  [optional] |
|**characterSetName** | [**String**](String.md) |  |  [optional] |
|**secondaryAvailabilityZone** | [**String**](String.md) |  |  [optional] |
|**publiclyAccessible** | [**Boolean**](Boolean.md) |  |  [optional] |
|**statusInfos** | [**List**](List.md) |  |  [optional] |
|**storageType** | [**String**](String.md) |  |  [optional] |
|**tdeCredentialArn** | [**String**](String.md) |  |  [optional] |
|**dbInstancePort** | [**Integer**](Integer.md) |  |  [optional] |
|**dbClusterIdentifier** | [**String**](String.md) |  |  [optional] |
|**storageEncrypted** | [**Boolean**](Boolean.md) |  |  [optional] |
|**kmsKeyId** | [**String**](String.md) |  |  [optional] |
|**dbiResourceId** | [**String**](String.md) |  |  [optional] |
|**caCertificateIdentifier** | [**String**](String.md) |  |  [optional] |
|**domainMemberships** | [**List**](List.md) |  |  [optional] |
|**copyTagsToSnapshot** | [**Boolean**](Boolean.md) |  |  [optional] |
|**monitoringInterval** | [**Integer**](Integer.md) |  |  [optional] |
|**enhancedMonitoringResourceArn** | [**String**](String.md) |  |  [optional] |
|**monitoringRoleArn** | [**String**](String.md) |  |  [optional] |
|**promotionTier** | [**Integer**](Integer.md) |  |  [optional] |
|**dbInstanceArn** | [**String**](String.md) |  |  [optional] |
|**timezone** | [**String**](String.md) |  |  [optional] |
|**iaMDatabaseAuthenticationEnabled** | [**Boolean**](Boolean.md) |  |  [optional] |
|**performanceInsightsEnabled** | [**Boolean**](Boolean.md) |  |  [optional] |
|**performanceInsightsKMSKeyId** | [**String**](String.md) |  |  [optional] |
|**enabledCloudwatchLogsExports** | [**List**](List.md) |  |  [optional] |
|**deletionProtection** | [**Boolean**](Boolean.md) |  |  [optional] |



