# AwsBackup.DescribeCopyJobOutputCopyJob

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** |  | [optional] 
**copyJobId** | **String** |  | [optional] 
**sourceBackupVaultArn** | **String** |  | [optional] 
**sourceRecoveryPointArn** | **String** |  | [optional] 
**destinationBackupVaultArn** | **String** |  | [optional] 
**destinationRecoveryPointArn** | **String** |  | [optional] 
**resourceArn** | **String** |  | [optional] 
**creationDate** | **Date** |  | [optional] 
**completionDate** | **Date** |  | [optional] 
**state** | [**CopyJobState**](CopyJobState.md) |  | [optional] 
**statusMessage** | **String** |  | [optional] 
**backupSizeInBytes** | **Number** |  | [optional] 
**iamRoleArn** | **String** |  | [optional] 
**createdBy** | [**RecoveryPointCreator**](RecoveryPointCreator.md) |  | [optional] 
**resourceType** | **String** |  | [optional] 
**parentJobId** | **String** |  | [optional] 
**isParent** | **Boolean** |  | [optional] 
**compositeMemberIdentifier** | **String** |  | [optional] 
**numberOfChildJobs** | **Number** |  | [optional] 
**childJobsInState** | **Object** |  | [optional] 
**resourceName** | **String** |  | [optional] 


