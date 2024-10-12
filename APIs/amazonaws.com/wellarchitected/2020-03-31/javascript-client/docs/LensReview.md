# AwsWellArchitectedTool.LensReview

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lensAlias** | **String** | &lt;p&gt;The alias of the lens.&lt;/p&gt; &lt;p&gt;For Amazon Web Services official lenses, this is either the lens alias, such as &lt;code&gt;serverless&lt;/code&gt;, or the lens ARN, such as &lt;code&gt;arn:aws:wellarchitected:us-east-1::lens/serverless&lt;/code&gt;. Note that some operations (such as ExportLens and CreateLensShare) are not permitted on Amazon Web Services official lenses.&lt;/p&gt; &lt;p&gt;For custom lenses, this is the lens ARN, such as &lt;code&gt;arn:aws:wellarchitected:us-west-2:123456789012:lens/0123456789abcdef01234567890abcdef&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;Each lens is identified by its &lt;a&gt;LensSummary$LensAlias&lt;/a&gt;.&lt;/p&gt; | [optional] 
**lensArn** | **String** |  | [optional] 
**lensVersion** | **String** |  | [optional] 
**lensName** | **String** | The full name of the lens. | [optional] 
**lensStatus** | [**LensStatus**](LensStatus.md) |  | [optional] 
**pillarReviewSummaries** | [**[PillarReviewSummary]**](PillarReviewSummary.md) | List of pillar review summaries of lens review in a workload. | [optional] 
**updatedAt** | **Date** | The date and time recorded. | [optional] 
**notes** | **String** | The notes associated with the workload. | [optional] 
**riskCounts** | **{String: Number}** | A map from risk names to the count of how many questions have that rating. | [optional] 
**nextToken** | **String** | The token to use to retrieve the next set of results. | [optional] 
**profiles** | **Array** |  | [optional] 
**prioritizedRiskCounts** | **{String: Number}** | A map from risk names to the count of how many questions have that rating. | [optional] 


