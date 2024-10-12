# AmazonSimpleSystemsManagerSsm.CreatePatchBaselineRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operatingSystem** | [**OperatingSystem**](OperatingSystem.md) |  | [optional] 
**name** | **String** |  | 
**globalFilters** | [**CreatePatchBaselineRequestGlobalFilters**](CreatePatchBaselineRequestGlobalFilters.md) |  | [optional] 
**approvalRules** | [**CreatePatchBaselineRequestApprovalRules**](CreatePatchBaselineRequestApprovalRules.md) |  | [optional] 
**approvedPatches** | **Array** |  | [optional] 
**approvedPatchesComplianceLevel** | [**PatchComplianceLevel**](PatchComplianceLevel.md) |  | [optional] 
**approvedPatchesEnableNonSecurity** | **Boolean** |  | [optional] 
**rejectedPatches** | **Array** |  | [optional] 
**rejectedPatchesAction** | [**PatchAction**](PatchAction.md) |  | [optional] 
**description** | **String** |  | [optional] 
**sources** | **Array** |  | [optional] 
**clientToken** | **String** |  | [optional] 
**tags** | **Array** |  | [optional] 


