# AwsAuditManager.CreateAssessmentFrameworkRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** |  The name of the new custom framework.  | 
**description** | **String** |  An optional description for the new custom framework.  | [optional] 
**complianceType** | **String** |  The compliance type that the new custom framework supports, such as CIS or HIPAA.  | [optional] 
**controlSets** | [**[CreateAssessmentFrameworkControlSet]**](CreateAssessmentFrameworkControlSet.md) |  The control sets that are associated with the framework.  | 
**tags** | **{String: String}** |  The tags that are associated with the framework.  | [optional] 


