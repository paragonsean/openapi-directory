# AmazonSimpleSystemsManagerSsm.UpdatePatchBaselineRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baselineId** | **String** |  | 
**name** | **String** |  | [optional] 
**globalFilters** | [**CreatePatchBaselineRequestGlobalFilters**](CreatePatchBaselineRequestGlobalFilters.md) |  | [optional] 
**approvalRules** | [**CreatePatchBaselineRequestApprovalRules**](CreatePatchBaselineRequestApprovalRules.md) |  | [optional] 
**approvedPatches** | **Array** |  | [optional] 
**approvedPatchesComplianceLevel** | [**PatchComplianceLevel**](PatchComplianceLevel.md) |  | [optional] 
**approvedPatchesEnableNonSecurity** | **Boolean** |  | [optional] 
**rejectedPatches** | **Array** |  | [optional] 
**rejectedPatchesAction** | [**PatchAction**](PatchAction.md) |  | [optional] 
**description** | **String** |  | [optional] 
**sources** | **Array** |  | [optional] 
**replace** | **Boolean** |  | [optional] 


