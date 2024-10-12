# AwsAuditManager.CreateAssessmentRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** |  The name of the assessment to be created.  | 
**description** | **String** |  The optional description of the assessment to be created.  | [optional] 
**assessmentReportsDestination** | [**CreateAssessmentRequestAssessmentReportsDestination**](CreateAssessmentRequestAssessmentReportsDestination.md) |  | 
**scope** | [**CreateAssessmentRequestScope**](CreateAssessmentRequestScope.md) |  | 
**roles** | [**[Role]**](Role.md) |  The list of roles for the assessment.  | 
**frameworkId** | **String** |  The identifier for the framework that the assessment will be created from.  | 
**tags** | **{String: String}** |  The tags that are associated with the assessment.  | [optional] 


