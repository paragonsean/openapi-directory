# AwsAuditManager.CreateControlRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** |  The name of the control.  | 
**description** | **String** |  The description of the control.  | [optional] 
**testingInformation** | **String** |  The steps to follow to determine if the control is satisfied.  | [optional] 
**actionPlanTitle** | **String** |  The title of the action plan for remediating the control.  | [optional] 
**actionPlanInstructions** | **String** |  The recommended actions to carry out if the control isn&#39;t fulfilled.  | [optional] 
**controlMappingSources** | [**[CreateControlMappingSource]**](CreateControlMappingSource.md) |  The data mapping sources for the control.  | 
**tags** | **{String: String}** |  The tags that are associated with the control.  | [optional] 


