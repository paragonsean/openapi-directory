# AmazonSimpleSystemsManagerSsm.InstancePatchState

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instanceId** | **String** |  | 
**patchGroup** | **String** |  | 
**baselineId** | **String** |  | 
**snapshotId** | **String** |  | [optional] 
**installOverrideList** | **String** |  | [optional] 
**ownerInformation** | **String** |  | [optional] 
**installedCount** | **Number** |  | [optional] 
**installedOtherCount** | **Number** |  | [optional] 
**installedPendingRebootCount** | **Number** |  | [optional] 
**installedRejectedCount** | **Number** |  | [optional] 
**missingCount** | **Number** |  | [optional] 
**failedCount** | **Number** |  | [optional] 
**unreportedNotApplicableCount** | **Number** |  | [optional] 
**notApplicableCount** | **Number** |  | [optional] 
**operationStartTime** | **Date** |  | 
**operationEndTime** | **Date** |  | 
**operation** | [**PatchOperationType**](PatchOperationType.md) |  | 
**lastNoRebootInstallOperationTime** | **Date** |  | [optional] 
**rebootOption** | [**RebootOption**](RebootOption.md) |  | [optional] 
**criticalNonCompliantCount** | **Number** |  | [optional] 
**securityNonCompliantCount** | **Number** |  | [optional] 
**otherNonCompliantCount** | **Number** |  | [optional] 


