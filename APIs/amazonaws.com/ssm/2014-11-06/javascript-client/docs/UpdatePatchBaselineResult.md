# AmazonSimpleSystemsManagerSsm.UpdatePatchBaselineResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baselineId** | **String** |  | [optional] 
**name** | **String** |  | [optional] 
**operatingSystem** | [**OperatingSystem**](OperatingSystem.md) |  | [optional] 
**globalFilters** | [**GetPatchBaselineResultGlobalFilters**](GetPatchBaselineResultGlobalFilters.md) |  | [optional] 
**approvalRules** | [**CreatePatchBaselineRequestApprovalRules**](CreatePatchBaselineRequestApprovalRules.md) |  | [optional] 
**approvedPatches** | **Array** |  | [optional] 
**approvedPatchesComplianceLevel** | [**PatchComplianceLevel**](PatchComplianceLevel.md) |  | [optional] 
**approvedPatchesEnableNonSecurity** | **Boolean** |  | [optional] 
**rejectedPatches** | **Array** |  | [optional] 
**rejectedPatchesAction** | [**PatchAction**](PatchAction.md) |  | [optional] 
**createdDate** | **Date** |  | [optional] 
**modifiedDate** | **Date** |  | [optional] 
**description** | **String** |  | [optional] 
**sources** | **Array** |  | [optional] 


