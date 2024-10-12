

# CreateDBInstanceMessage


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dbName** | [**String**](String.md) |  |  [optional] |
|**dbInstanceIdentifier** | [**String**](String.md) |  |  |
|**allocatedStorage** | [**Integer**](Integer.md) |  |  [optional] |
|**dbInstanceClass** | [**String**](String.md) |  |  |
|**engine** | [**String**](String.md) |  |  |
|**masterUsername** | [**String**](String.md) |  |  [optional] |
|**masterUserPassword** | [**String**](String.md) |  |  [optional] |
|**dbSecurityGroups** | [**List**](List.md) |  |  [optional] |
|**vpcSecurityGroupIds** | [**List**](List.md) |  |  [optional] |
|**availabilityZone** | [**String**](String.md) |  |  [optional] |
|**dbSubnetGroupName** | [**String**](String.md) |  |  [optional] |
|**preferredMaintenanceWindow** | [**String**](String.md) |  |  [optional] |
|**dbParameterGroupName** | [**String**](String.md) |  |  [optional] |
|**backupRetentionPeriod** | [**Integer**](Integer.md) |  |  [optional] |
|**preferredBackupWindow** | [**String**](String.md) |  |  [optional] |
|**port** | [**Integer**](Integer.md) |  |  [optional] |
|**multiAZ** | [**Boolean**](Boolean.md) |  |  [optional] |
|**engineVersion** | [**String**](String.md) |  |  [optional] |
|**autoMinorVersionUpgrade** | [**Boolean**](Boolean.md) |  |  [optional] |
|**licenseModel** | [**String**](String.md) |  |  [optional] |
|**iops** | [**Integer**](Integer.md) |  |  [optional] |
|**optionGroupName** | [**String**](String.md) |  |  [optional] |
|**characterSetName** | [**String**](String.md) |  |  [optional] |
|**publiclyAccessible** | [**Boolean**](Boolean.md) |  |  [optional] |
|**tags** | [**List**](List.md) |  |  [optional] |
|**dbClusterIdentifier** | [**String**](String.md) |  |  |
|**storageType** | [**String**](String.md) |  |  [optional] |
|**tdeCredentialArn** | [**String**](String.md) |  |  [optional] |
|**tdeCredentialPassword** | [**String**](String.md) |  |  [optional] |
|**storageEncrypted** | [**Boolean**](Boolean.md) |  |  [optional] |
|**kmsKeyId** | [**String**](String.md) |  |  [optional] |
|**domain** | [**String**](String.md) |  |  [optional] |
|**copyTagsToSnapshot** | [**Boolean**](Boolean.md) |  |  [optional] |
|**monitoringInterval** | [**Integer**](Integer.md) |  |  [optional] |
|**monitoringRoleArn** | [**String**](String.md) |  |  [optional] |
|**domainIAMRoleName** | [**String**](String.md) |  |  [optional] |
|**promotionTier** | [**Integer**](Integer.md) |  |  [optional] |
|**timezone** | [**String**](String.md) |  |  [optional] |
|**enableIAMDatabaseAuthentication** | [**Boolean**](Boolean.md) |  |  [optional] |
|**enablePerformanceInsights** | [**Boolean**](Boolean.md) |  |  [optional] |
|**performanceInsightsKMSKeyId** | [**String**](String.md) |  |  [optional] |
|**enableCloudwatchLogsExports** | [**List**](List.md) |  |  [optional] |
|**deletionProtection** | [**Boolean**](Boolean.md) |  |  [optional] |



