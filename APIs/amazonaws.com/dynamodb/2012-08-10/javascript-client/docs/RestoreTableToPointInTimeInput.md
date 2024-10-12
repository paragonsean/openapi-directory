# AmazonDynamoDb.RestoreTableToPointInTimeInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sourceTableArn** | **String** |  | [optional] 
**sourceTableName** | **String** |  | [optional] 
**targetTableName** | **String** |  | 
**useLatestRestorableTime** | **Boolean** |  | [optional] 
**restoreDateTime** | **Date** |  | [optional] 
**billingModeOverride** | [**BillingMode**](BillingMode.md) |  | [optional] 
**globalSecondaryIndexOverride** | **Array** |  | [optional] 
**localSecondaryIndexOverride** | **Array** |  | [optional] 
**provisionedThroughputOverride** | [**RestoreTableFromBackupInputProvisionedThroughputOverride**](RestoreTableFromBackupInputProvisionedThroughputOverride.md) |  | [optional] 
**sSESpecificationOverride** | [**RestoreTableFromBackupInputSSESpecificationOverride**](RestoreTableFromBackupInputSSESpecificationOverride.md) |  | [optional] 


