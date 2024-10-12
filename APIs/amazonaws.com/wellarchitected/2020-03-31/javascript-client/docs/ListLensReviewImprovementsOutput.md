# AwsWellArchitectedTool.ListLensReviewImprovementsOutput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workloadId** | **String** | The ID assigned to the workload. This ID is unique within an Amazon Web Services Region. | [optional] 
**milestoneNumber** | **Number** | &lt;p&gt;The milestone number.&lt;/p&gt; &lt;p&gt;A workload can have a maximum of 100 milestones.&lt;/p&gt; | [optional] 
**lensAlias** | **String** | &lt;p&gt;The alias of the lens.&lt;/p&gt; &lt;p&gt;For Amazon Web Services official lenses, this is either the lens alias, such as &lt;code&gt;serverless&lt;/code&gt;, or the lens ARN, such as &lt;code&gt;arn:aws:wellarchitected:us-east-1::lens/serverless&lt;/code&gt;. Note that some operations (such as ExportLens and CreateLensShare) are not permitted on Amazon Web Services official lenses.&lt;/p&gt; &lt;p&gt;For custom lenses, this is the lens ARN, such as &lt;code&gt;arn:aws:wellarchitected:us-west-2:123456789012:lens/0123456789abcdef01234567890abcdef&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;Each lens is identified by its &lt;a&gt;LensSummary$LensAlias&lt;/a&gt;.&lt;/p&gt; | [optional] 
**lensArn** | **String** |  | [optional] 
**improvementSummaries** | [**[ImprovementSummary]**](ImprovementSummary.md) | List of improvement summaries of lens review in a workload. | [optional] 
**nextToken** | **String** | The token to use to retrieve the next set of results. | [optional] 


