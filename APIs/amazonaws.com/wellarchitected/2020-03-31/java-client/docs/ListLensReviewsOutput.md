

# ListLensReviewsOutput

Output of a list lens reviews call.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**workloadId** | **String** | The ID assigned to the workload. This ID is unique within an Amazon Web Services Region. |  [optional] |
|**milestoneNumber** | **Integer** | &lt;p&gt;The milestone number.&lt;/p&gt; &lt;p&gt;A workload can have a maximum of 100 milestones.&lt;/p&gt; |  [optional] |
|**lensReviewSummaries** | [**List&lt;LensReviewSummary&gt;**](LensReviewSummary.md) | List of lens summaries of lens reviews of a workload. |  [optional] |
|**nextToken** | **String** | The token to use to retrieve the next set of results. |  [optional] |



