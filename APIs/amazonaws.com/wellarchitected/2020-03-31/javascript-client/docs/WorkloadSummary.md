# AwsWellArchitectedTool.WorkloadSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workloadId** | **String** | The ID assigned to the workload. This ID is unique within an Amazon Web Services Region. | [optional] 
**workloadArn** | **String** | The ARN for the workload. | [optional] 
**workloadName** | **String** | &lt;p&gt;The name of the workload.&lt;/p&gt; &lt;p&gt;The name must be unique within an account within an Amazon Web Services Region. Spaces and capitalization are ignored when checking for uniqueness.&lt;/p&gt; | [optional] 
**owner** | **String** | An Amazon Web Services account ID. | [optional] 
**updatedAt** | **Date** | The date and time recorded. | [optional] 
**lenses** | **[String]** | The list of lenses associated with the workload. Each lens is identified by its &lt;a&gt;LensSummary$LensAlias&lt;/a&gt;. | [optional] 
**riskCounts** | **{String: Number}** | A map from risk names to the count of how many questions have that rating. | [optional] 
**improvementStatus** | [**WorkloadImprovementStatus**](WorkloadImprovementStatus.md) |  | [optional] 
**profiles** | **Array** |  | [optional] 
**prioritizedRiskCounts** | **{String: Number}** | A map from risk names to the count of how many questions have that rating. | [optional] 


