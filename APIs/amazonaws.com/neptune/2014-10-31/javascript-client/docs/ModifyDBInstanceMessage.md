# AmazonNeptune.ModifyDBInstanceMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dBInstanceIdentifier** | **String** |  | 
**allocatedStorage** | **Number** |  | [optional] 
**dBInstanceClass** | **String** |  | [optional] 
**dBSubnetGroupName** | **String** |  | [optional] 
**dBSecurityGroups** | **Array** |  | [optional] 
**vpcSecurityGroupIds** | **Array** |  | [optional] 
**applyImmediately** | **Boolean** |  | [optional] 
**masterUserPassword** | **String** |  | [optional] 
**dBParameterGroupName** | **String** |  | [optional] 
**backupRetentionPeriod** | **Number** |  | [optional] 
**preferredBackupWindow** | **String** |  | [optional] 
**preferredMaintenanceWindow** | **String** |  | [optional] 
**multiAZ** | **Boolean** |  | [optional] 
**engineVersion** | **String** |  | [optional] 
**allowMajorVersionUpgrade** | **Boolean** |  | [optional] 
**autoMinorVersionUpgrade** | **Boolean** |  | [optional] 
**licenseModel** | **String** |  | [optional] 
**iops** | **Number** |  | [optional] 
**optionGroupName** | **String** |  | [optional] 
**newDBInstanceIdentifier** | **String** |  | [optional] 
**storageType** | **String** |  | [optional] 
**tdeCredentialArn** | **String** |  | [optional] 
**tdeCredentialPassword** | **String** |  | [optional] 
**cACertificateIdentifier** | **String** |  | [optional] 
**domain** | **String** |  | [optional] 
**copyTagsToSnapshot** | **Boolean** |  | [optional] 
**monitoringInterval** | **Number** |  | [optional] 
**dBPortNumber** | **Number** |  | [optional] 
**publiclyAccessible** | **Boolean** |  | [optional] 
**monitoringRoleArn** | **String** |  | [optional] 
**domainIAMRoleName** | **String** |  | [optional] 
**promotionTier** | **Number** |  | [optional] 
**enableIAMDatabaseAuthentication** | **Boolean** |  | [optional] 
**enablePerformanceInsights** | **Boolean** |  | [optional] 
**performanceInsightsKMSKeyId** | **String** |  | [optional] 
**cloudwatchLogsExportConfiguration** | [**ModifyDBInstanceMessageCloudwatchLogsExportConfiguration**](ModifyDBInstanceMessageCloudwatchLogsExportConfiguration.md) |  | [optional] 
**deletionProtection** | **Boolean** |  | [optional] 


