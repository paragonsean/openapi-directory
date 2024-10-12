

# ModifyDBInstanceMessage


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dbInstanceIdentifier** | [**String**](String.md) |  |  |
|**allocatedStorage** | [**Integer**](Integer.md) |  |  [optional] |
|**dbInstanceClass** | [**String**](String.md) |  |  [optional] |
|**dbSubnetGroupName** | [**String**](String.md) |  |  [optional] |
|**dbSecurityGroups** | [**List**](List.md) |  |  [optional] |
|**vpcSecurityGroupIds** | [**List**](List.md) |  |  [optional] |
|**applyImmediately** | [**Boolean**](Boolean.md) |  |  [optional] |
|**masterUserPassword** | [**String**](String.md) |  |  [optional] |
|**dbParameterGroupName** | [**String**](String.md) |  |  [optional] |
|**backupRetentionPeriod** | [**Integer**](Integer.md) |  |  [optional] |
|**preferredBackupWindow** | [**String**](String.md) |  |  [optional] |
|**preferredMaintenanceWindow** | [**String**](String.md) |  |  [optional] |
|**multiAZ** | [**Boolean**](Boolean.md) |  |  [optional] |
|**engineVersion** | [**String**](String.md) |  |  [optional] |
|**allowMajorVersionUpgrade** | [**Boolean**](Boolean.md) |  |  [optional] |
|**autoMinorVersionUpgrade** | [**Boolean**](Boolean.md) |  |  [optional] |
|**licenseModel** | [**String**](String.md) |  |  [optional] |
|**iops** | [**Integer**](Integer.md) |  |  [optional] |
|**optionGroupName** | [**String**](String.md) |  |  [optional] |
|**newDBInstanceIdentifier** | [**String**](String.md) |  |  [optional] |
|**storageType** | [**String**](String.md) |  |  [optional] |
|**tdeCredentialArn** | [**String**](String.md) |  |  [optional] |
|**tdeCredentialPassword** | [**String**](String.md) |  |  [optional] |
|**caCertificateIdentifier** | [**String**](String.md) |  |  [optional] |
|**domain** | [**String**](String.md) |  |  [optional] |
|**copyTagsToSnapshot** | [**Boolean**](Boolean.md) |  |  [optional] |
|**monitoringInterval** | [**Integer**](Integer.md) |  |  [optional] |
|**dbPortNumber** | [**Integer**](Integer.md) |  |  [optional] |
|**publiclyAccessible** | [**Boolean**](Boolean.md) |  |  [optional] |
|**monitoringRoleArn** | [**String**](String.md) |  |  [optional] |
|**domainIAMRoleName** | [**String**](String.md) |  |  [optional] |
|**promotionTier** | [**Integer**](Integer.md) |  |  [optional] |
|**enableIAMDatabaseAuthentication** | [**Boolean**](Boolean.md) |  |  [optional] |
|**enablePerformanceInsights** | [**Boolean**](Boolean.md) |  |  [optional] |
|**performanceInsightsKMSKeyId** | [**String**](String.md) |  |  [optional] |
|**cloudwatchLogsExportConfiguration** | [**ModifyDBInstanceMessageCloudwatchLogsExportConfiguration**](ModifyDBInstanceMessageCloudwatchLogsExportConfiguration.md) |  |  [optional] |
|**deletionProtection** | [**Boolean**](Boolean.md) |  |  [optional] |



